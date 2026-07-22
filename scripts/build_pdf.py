#!/usr/bin/env python3
"""Build a single print-ready PDF of the STAT C1000 textbook.

Why this exists
---------------
The book is a MyST / Jupyter Book 2 site. Two things in it do not survive a
LaTeX export unaided:

  1. The {quiz} / {quiz-multi} directives (pages/quiz.mjs) render as anywidget
     nodes. LaTeX has no idea what those are, so the questions would silently
     vanish from the PDF.
  2. The figures are .gif (407 of them) and .svg (168). pdflatex/xelatex can
     embed neither.

So this script stages a *copy* of the book in a sibling directory
(../textbook-dev-pdf-build), rewrites the quizzes into static numbered questions
with an answer-key appendix at the back, converts every image into something
LaTeX can embed, writes a PDF-flavoured myst.yml, and runs the export. Nothing
in the real source tree is touched.

Usage
-----
    conda activate statc1000book
    python scripts/build_pdf.py             # full build
    python scripts/build_pdf.py --dry-run   # stage + report, no LaTeX run
    python scripts/build_pdf.py --no-images # skip image conversion (fast iteration)

Start with --dry-run and read the staged markdown; it's much faster to spot a
mangled question there than in a 600-page PDF.

Output: introduction-to-statistics.pdf in the repo root.

Requirements
------------
    pip install pyyaml pillow cairosvg
    conda install -c conda-forge tectonic     # or any latexmk/xelatex install

cairosvg is the preferred SVG converter; the script falls back to svglib,
rsvg-convert, then inkscape, and warns (rather than dying) if none are present.
"""

from __future__ import annotations

import argparse
import dataclasses
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent
FINAL_PDF = REPO / "introduction-to-statistics.pdf"

# Staged OUTSIDE the repo on purpose. `myst build` walks up the directory tree
# looking for a myst.yml, so a staging dir inside the repo silently inherits the
# real project config - the quiz.mjs plugin, the site block, the page numbering -
# which is exactly what this build is trying to strip out.
STAGE = REPO.parent / f"{REPO.name}-pdf-build"

# Letters used to label answer choices in both the question and the answer key.
LETTERS = "abcdefghijklmnop"


# ──────────────────────────────────────────────────────────────────────────────
# Table of contents
# ──────────────────────────────────────────────────────────────────────────────


@dataclasses.dataclass
class Entry:
    """One item in the flattened reading order."""

    kind: str  # "divider" or "page"
    title: str  # divider heading, or "" for pages
    source: Path | None = None  # absolute path to the source .md
    number: int = 0  # site page number (matches numbering.title in myst.yml)
    depth: int = 0  # nesting depth in toc.yml
    level: int = 0  # LaTeX sectioning level (-1 part, 0 chapter, 1 section)


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def excluded_matchers(myst: dict) -> list[str]:
    return list(myst.get("project", {}).get("exclude", []) or [])


def is_excluded(rel: str, patterns: list[str]) -> bool:
    from fnmatch import fnmatch

    return any(fnmatch(rel, pat) for pat in patterns)


def flatten_toc(nodes: list, excludes: list[str], depth: int = 0) -> list[Entry]:
    """Walk toc.yml into a flat reading order, expanding `pattern:` globs.

    MyST sorts pattern matches lexically, which is why the source files carry a
    numeric prefix (019-, 020-, ...). We replicate that sort exactly so the page
    numbers in the PDF match the page numbers on the website.
    """
    out: list[Entry] = []
    for node in nodes or []:
        if "file" in node:
            rel = node["file"]
            if not is_excluded(rel, excludes):
                out.append(Entry(kind="page", title="", source=REPO / rel, depth=depth))
        elif "pattern" in node:
            matches = sorted(REPO.glob(node["pattern"]))
            for path in matches:
                rel = path.relative_to(REPO).as_posix()
                if not is_excluded(rel, excludes):
                    out.append(Entry(kind="page", title="", source=path, depth=depth))
        elif "title" in node:
            out.append(Entry(kind="divider", title=node["title"], depth=depth))
        if node.get("children"):
            out.extend(flatten_toc(node["children"], excludes, depth + 1))
    return out


def assign_levels(entries: list[Entry]) -> None:
    """Map the toc hierarchy onto LaTeX sectioning commands.

    MyST defaults every article to \\section, which a book class rejects as a
    top level. The docs' fix is an explicit `level` per article:
    -1 part, 0 chapter, 1 section.

    toc.yml nests Unit > Section > pages, so:
      Unit ("Unit 1: Producing Data")   -> \\part
      Section ("Section 1: Sampling")   -> \\chapter
      page                              -> \\section

    Where a top-level heading holds pages directly ("The Big Picture"), there is
    no Section in between, so those pages become chapters instead.
    """
    enclosing_depth: int | None = None
    for entry in entries:
        if entry.kind == "divider":
            entry.level = -1 if entry.depth == 0 else 0
            enclosing_depth = entry.depth
        else:
            entry.level = 1 if enclosing_depth not in (None, 0) else 0


def build_reading_order() -> list[Entry]:
    myst = load_yaml(REPO / "myst.yml")
    toc = load_yaml(REPO / "toc.yml")
    entries = flatten_toc(toc["project"]["toc"], excluded_matchers(myst))
    assign_levels(entries)

    # Number only real pages, 1-based, so "page 30" means the same thing in the
    # PDF as it does in class and on the website.
    n = 0
    for entry in entries:
        if entry.kind == "page":
            n += 1
            entry.number = n
    return entries


# ──────────────────────────────────────────────────────────────────────────────
# Quiz rewriting
# ──────────────────────────────────────────────────────────────────────────────


@dataclasses.dataclass
class Choice:
    text: str
    correct: bool
    feedback: str = ""


@dataclasses.dataclass
class Question:
    number: int
    page_number: int
    page_title: str
    section: str
    prompt: str
    choices: list[Choice]
    multi: bool
    hint: str = ""
    explanation: str = ""


# Opening line of a colon-fenced quiz: ":::{quiz} prompt" (3+ colons).
QUIZ_OPEN = re.compile(r"^(:{3,})\{(quiz|quiz-multi)\}[ \t]*(.*)$")
OPTION_LINE = re.compile(r"^:([a-z0-9-]+):[ \t]*(.*)$")
CHOICE_LINE = re.compile(r"^\* (\*?)(.*)$")


def parse_choices(body: str) -> list[Choice]:
    """Port of parseChoices() in pages/quiz.mjs, so the PDF agrees with the site.

    Choices start with "* "; a leading "*" on the text marks the correct one.
    Fenced code inside a choice is captured verbatim.
    """
    choices: list[Choice] = []
    cur: Choice | None = None
    in_fence = False
    fence_lang = ""
    fence_lines: list[str] = []

    for line in body.split("\n"):
        if cur is not None and not in_fence:
            m = re.match(r"^\s*```(\w*)$", line)
            if m:
                in_fence, fence_lang, fence_lines = True, m.group(1) or "", []
                continue
        if in_fence:
            if re.match(r"^\s*```$", line):
                cur.text += f"```{fence_lang}\n" + "\n".join(fence_lines) + "\n```"
                in_fence, fence_lines, fence_lang = False, [], ""
            else:
                fence_lines.append(line)
            continue
        m = CHOICE_LINE.match(line)
        if m:
            if cur is not None:
                choices.append(cur)
            cur = Choice(text=m.group(2).strip(), correct=m.group(1) == "*")
            continue
        if cur is not None and line.strip():
            cur.text += "\n" + line.strip()

    if cur is not None:
        choices.append(cur)
    return choices


def render_question(q: Question) -> str:
    """The static block that replaces a quiz widget in the PDF."""
    label = f"Question {q.number}"
    if q.multi:
        label += " (select all that apply)"
    lines = [
        f":::{{admonition}} {label}",
        ":class: seealso",
        "",
        q.prompt,
        "",
    ]
    for letter, choice in zip(LETTERS, q.choices):
        # Indent continuation lines so multi-line choices stay inside the bullet.
        text = choice.text.replace("\n", "\n  ")
        lines.append(f"- **({letter})** {text}")
    if q.hint:
        lines += ["", f"*Hint: {q.hint}*"]
    lines += [":::", ""]
    return "\n".join(lines)


def rewrite_quizzes(text: str, ctx: dict, questions: list[Question]) -> str:
    """Replace every quiz block in `text` with a static numbered question.

    Colon fences nest, so we match the closing fence by exact colon count -
    a ":::" quiz inside a "::::" admonition closes on the next bare ":::".
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = QUIZ_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        fence, kind, prompt = m.group(1), m.group(2), m.group(3).strip()
        close = re.compile(rf"^{fence}\s*$")
        body: list[str] = []
        i += 1
        while i < len(lines) and not close.match(lines[i]):
            body.append(lines[i])
            i += 1
        i += 1  # step past the closing fence

        options: dict[str, str] = {}
        rest: list[str] = []
        for line in body:
            om = OPTION_LINE.match(line)
            if om and not rest:
                options[om.group(1)] = om.group(2).strip()
            else:
                rest.append(line)

        choices = parse_choices("\n".join(rest))
        for idx, choice in enumerate(choices):
            choice.feedback = options.get(f"feedback-{idx}", "")

        ctx["counter"] += 1
        q = Question(
            number=ctx["counter"],
            page_number=ctx["page_number"],
            page_title=ctx["page_title"],
            section=ctx["section"],
            prompt=prompt,
            choices=choices,
            multi=(kind == "quiz-multi"),
            hint=options.get("hint", ""),
            explanation=options.get("explanation", ""),
        )
        questions.append(q)
        out.append(render_question(q))
    return "\n".join(out)


def render_answer_key(questions: list[Question]) -> str:
    """The appendix. Grouped by section so it reads like a textbook answer key."""
    lines = [
        "# Answer Key",
        "",
        "Answers to the Check Your Understanding questions, in book order.",
        "",
    ]
    current_section = None
    for q in questions:
        if q.section != current_section:
            current_section = q.section
            lines += [f"## {current_section or 'Front Matter'}", ""]

        correct = [
            f"**({letter})** {c.text}"
            for letter, c in zip(LETTERS, q.choices)
            if c.correct
        ]
        answer = "; ".join(correct) if correct else "*(no answer marked in source)*"
        where = f"page {q.page_number}"
        if q.page_title:
            where += f", {q.page_title}"
        lines += [f"**{q.number}.** ({where}) {answer}", ""]

        notes = [c.feedback for c in q.choices if c.correct and c.feedback]
        if q.explanation:
            notes.append(q.explanation)
        for note in notes:
            lines += [f"> {note}", ""]
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────────────────
# Images
# ──────────────────────────────────────────────────────────────────────────────


def convert_gif(src: Path, dest: Path) -> bool:
    """First frame of the GIF as PNG. These are static diagrams, not animations."""
    try:
        from PIL import Image
    except ImportError:
        return False
    try:
        with Image.open(src) as im:
            im.seek(0)
            im.convert("RGBA").save(dest, "PNG")
        return True
    except Exception as exc:  # noqa: BLE001 - one bad image shouldn't kill the build
        print(f"  ! gif failed {src.name}: {exc}")
        return False


def convert_svg(src: Path, dest: Path) -> bool:
    """SVG -> PDF, so the figures stay vector-sharp in print.

    Tries the pure-Python converters first because they need no system packages.
    """
    try:
        import cairosvg

        cairosvg.svg2pdf(url=str(src), write_to=str(dest))
        return True
    except ImportError:
        pass
    except Exception as exc:  # noqa: BLE001
        print(f"  ! cairosvg failed {src.name}: {exc}")

    try:
        from reportlab.graphics import renderPDF
        from svglib.svglib import svg2rlg

        drawing = svg2rlg(str(src))
        if drawing is not None:
            renderPDF.drawToFile(drawing, str(dest))
            return True
    except ImportError:
        pass
    except Exception as exc:  # noqa: BLE001
        print(f"  ! svglib failed {src.name}: {exc}")

    for cmd in (
        ["rsvg-convert", "-f", "pdf", "-o", str(dest), str(src)],
        ["inkscape", str(src), "--export-type=pdf", f"--export-filename={dest}"],
    ):
        if shutil.which(cmd[0]):
            if subprocess.run(cmd, capture_output=True).returncode == 0:
                return True
    return False


def stage_images() -> tuple[int, int]:
    """Copy pages/images into the staging tree, converting gif and svg on the way."""
    src_root = REPO / "pages" / "images"
    dest_root = STAGE / "pages" / "images"
    converted = failed = 0

    for src in src_root.rglob("*"):
        if src.is_dir() or src.name.startswith("."):
            continue
        dest = dest_root / src.relative_to(src_root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        suffix = src.suffix.lower()

        if suffix == ".gif":
            ok = convert_gif(src, dest.with_suffix(".png"))
        elif suffix == ".svg":
            ok = convert_svg(src, dest.with_suffix(".pdf"))
        else:
            shutil.copy2(src, dest)
            continue

        if ok:
            converted += 1
        else:
            failed += 1
            shutil.copy2(src, dest)  # leave the original; MyST will warn
    return converted, failed


IMAGE_REF = re.compile(r"([\w./-]+)\.(gif|svg)\b", re.IGNORECASE)


def rewrite_image_paths(text: str) -> str:
    """Point every .gif at its .png and every .svg at its .pdf.

    Only rewrites paths that actually resolve to a file we staged. That guard
    keeps the regex from mangling a remote URL or a filename mentioned in prose.
    """
    known = convertible_image_names()

    def sub(m: re.Match) -> str:
        stem, ext = m.group(1), m.group(2).lower()
        if Path(f"{stem}.{ext}").name.lower() not in known:
            return m.group(0)
        return stem + (".png" if ext == "gif" else ".pdf")

    return IMAGE_REF.sub(sub, text)


_image_names: set[str] | None = None


def convertible_image_names() -> set[str]:
    """Basenames of every .gif/.svg under pages/images, lowercased."""
    global _image_names
    if _image_names is None:
        root = REPO / "pages" / "images"
        _image_names = {
            p.name.lower()
            for p in root.rglob("*")
            if p.suffix.lower() in {".gif", ".svg"}
        }
    return _image_names


# ──────────────────────────────────────────────────────────────────────────────
# Staging
# ──────────────────────────────────────────────────────────────────────────────


def first_heading(text: str) -> str:
    for line in text.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def stamp_page_number(text: str, number: int) -> str:
    """Prefix the page's H1 with its site page number.

    myst.yml numbers pages via `numbering.title`, but that counter would also
    walk the part dividers this script injects, shifting every number. Numbering
    here instead keeps the PDF and the website in agreement.
    """
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            lines[idx] = f"# {number}. {line[2:].strip()}"
            break
    return "\n".join(lines)


def stage(do_images: bool) -> tuple[list[dict], list[Question]]:
    if STAGE.exists():
        shutil.rmtree(STAGE)
    (STAGE / "pages").mkdir(parents=True)

    entries = build_reading_order()
    questions: list[Question] = []
    articles: list[dict] = []
    section = ""
    divider_n = 0

    for entry in entries:
        if entry.kind == "divider":
            divider_n += 1
            section = entry.title
            rel = f"pages/_part-{divider_n:02d}.md"
            (STAGE / rel).write_text(f"# {entry.title}\n", encoding="utf-8")
            articles.append({"file": rel, "level": entry.level})
            continue

        text = entry.source.read_text(encoding="utf-8")
        ctx = {
            "counter": len(questions),
            "page_number": entry.number,
            "page_title": first_heading(text),
            "section": section,
        }
        text = rewrite_quizzes(text, ctx, questions)
        text = rewrite_image_paths(text)
        text = stamp_page_number(text, entry.number)

        rel = f"pages/{entry.source.name}"
        (STAGE / rel).write_text(text, encoding="utf-8")
        articles.append({"file": rel, "level": entry.level})

    # Answer key appendix. At level -1 its "# Answer Key" heading becomes a
    # \part and the per-section "##" headings become chapters inside it.
    if questions:
        (STAGE / "pages" / "zzz-answer-key.md").write_text(
            render_answer_key(questions), encoding="utf-8"
        )
        articles.append({"file": "pages/zzz-answer-key.md", "level": -1})

    if do_images:
        print("Converting images (this takes a minute)...")
        converted, failed = stage_images()
        print(f"  {converted} converted, {failed} could not be converted")

    for extra in ("ccsf.png", "favicon.ico"):
        if (REPO / extra).exists():
            shutil.copy2(REPO / extra, STAGE / extra)

    return articles, questions


def write_myst_config(articles: list[dict], template: str) -> None:
    """PDF-flavoured myst.yml: no site block, no JS plugins, one book export."""
    src = load_yaml(REPO / "myst.yml").get("project", {})
    config = {
        "version": 1,
        "project": {
            "title": src.get("title", "Introduction to Statistics"),
            "authors": src.get("authors", []),
            "license": src.get("license"),
            "exports": [
                {
                    "id": "book",
                    "format": "pdf",
                    "template": template,
                    "output": "exports/introduction-to-statistics.pdf",
                    "articles": articles,
                }
            ],
        },
    }
    with (STAGE / "myst.yml").open("w", encoding="utf-8") as handle:
        yaml.safe_dump(config, handle, sort_keys=False, allow_unicode=True)


# ──────────────────────────────────────────────────────────────────────────────
# Build
# ──────────────────────────────────────────────────────────────────────────────


def check_no_ancestor_config() -> None:
    """Guard the assumption that STAGE sits outside any other MyST project."""
    for parent in STAGE.resolve().parents:
        if (parent / "myst.yml").exists():
            print(
                f"Warning: {parent / 'myst.yml'} is above the staging directory.\n"
                "MyST will merge it into this build. Move the staging directory "
                "with --stage-dir to somewhere outside that project.",
                file=sys.stderr,
            )
            return


def myst_command() -> list[str]:
    if shutil.which("myst"):
        return ["myst"]
    if shutil.which("jupyter-book"):
        return ["jupyter-book"]
    if shutil.which("jupyter"):
        return ["jupyter", "book"]
    sys.exit("Neither `myst` nor `jupyter book` is on PATH. Activate your conda env.")


def check_latex() -> None:
    if shutil.which("tectonic") or shutil.which("latexmk") or shutil.which("xelatex"):
        return
    sys.exit(
        "No LaTeX engine found. Install one, e.g.:\n"
        "    conda install -c conda-forge tectonic\n"
        "    brew install tectonic"
    )


def run_build() -> None:
    cmd = myst_command() + ["build", "--pdf"]
    print(f"Running: {' '.join(cmd)}  (in {STAGE})")
    result = subprocess.run(cmd, cwd=STAGE)
    if result.returncode != 0:
        print(
            "\nBuild failed. If the error mentions the template, list what's "
            "available with:\n    myst templates list --tex\n"
            "then re-run with --template <name>.",
            file=sys.stderr,
        )
        sys.exit(result.returncode)

    produced = sorted(STAGE.glob("exports/*.pdf")) + sorted(STAGE.glob("_build/exports/*.pdf"))
    if not produced:
        sys.exit("Build reported success but produced no PDF; check the log above.")
    shutil.copy2(produced[0], FINAL_PDF)
    print(f"\nWrote {FINAL_PDF.relative_to(REPO)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="stage only, don't run LaTeX")
    parser.add_argument("--no-images", action="store_true", help="skip image conversion")
    parser.add_argument(
        "--template",
        default="plain_latex_book",
        help="MyST LaTeX template (default: plain_latex_book)",
    )
    parser.add_argument("--stage-dir", help="override the staging directory")
    args = parser.parse_args()

    if args.stage_dir:
        global STAGE
        STAGE = Path(args.stage_dir).resolve()

    check_no_ancestor_config()
    articles, questions = stage(not args.no_images)
    write_myst_config(articles, args.template)

    pages = sum(1 for a in articles if not Path(a["file"]).name.startswith("_part-"))
    print(f"Staged {pages} pages and {len(questions)} questions into {STAGE}")

    if args.dry_run:
        print("Dry run: stopping before the LaTeX build.")
        return 0

    check_latex()
    run_build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
