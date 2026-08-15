#!/usr/bin/env python3
"""Put the page number back into the site URL.

MyST builds a page's URL slug from its filename, but `createSlug()` calls
`removeLeadingEnumeration()` first, which strips a leading run of
[0-9_.-] characters. So:

    pages/259-m17-case-c-c-5-of-5.md  ->  /pages/m17-case-c-c-5-of-5

The prefix survives only if it does NOT start with a digit-ish character
(or if there are 5+ leading digits). Renaming 259- to p259- therefore gives:

    pages/p259-m17-case-c-c-5-of-5.md ->  /pages/p259-m17-case-c-c-5-of-5

This script does that rename for every numbered page, with `git mv`, and
rewrites any reference to the old filenames elsewhere in the repo.

Usage
-----
    python scripts/rename_pages_for_urls.py              # dry run (default)
    python scripts/rename_pages_for_urls.py --apply      # actually do it
    python scripts/rename_pages_for_urls.py --prefix pg  # use pg259- instead

Run it from anywhere inside the repo. Nothing is written unless --apply
is passed. Commit or stash your work first; this touches ~230 files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Directories never scanned for references or renames.
SKIP_DIRS = {".git", "_build", "node_modules", ".ipynb_checkpoints", "__pycache__"}

# Files scanned for references to renamed pages.
TEXT_SUFFIXES = {
    ".md", ".yml", ".yaml", ".py", ".mjs", ".js", ".json", ".txt",
    ".html", ".css", ".ipynb", ".sh", ".toml", ".cfg",
}

PAGE_RE = re.compile(r"^(?P<num>\d{3,})-(?P<rest>.+)\.md$")


# --- MyST slug logic, mirrored from myst-cli so we can preview URLs ---------

def _remove_leading_enumeration(s: str) -> str:
    if re.match(r"^([12][0-9]{3})([^0-9])?", s):
        return s
    if re.match(r"^([0-9]{5})", s):
        return s
    removed = re.sub(r"^([0-9_.-]+)", "", s)
    return removed or s


def myst_slug(stem: str) -> str:
    """Reproduce myst-cli's createSlug() for a filename stem."""
    name = _remove_leading_enumeration(stem).lower()
    name = re.sub(r"&", "-and-", name)
    name = re.sub(r"[^a-z0-9-]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name[:50]


# --- repo helpers -----------------------------------------------------------

def find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "myst.yml").is_file():
            return candidate
    sys.exit("Could not find myst.yml in this directory or any parent.")


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=False
    )


def is_git_repo(repo: Path) -> bool:
    return git(repo, "rev-parse", "--git-dir").returncode == 0


def iter_text_files(repo: Path):
    for path in repo.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(repo).parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


# --- main -------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="perform the rename (default is a dry run)")
    parser.add_argument("--prefix", default="p", help="letter(s) to put in front of the number (default: p)")
    parser.add_argument("--pages-dir", default="pages", help="directory holding the numbered pages (default: pages)")
    parser.add_argument("--include-unused", action="store_true", help="also rename pages/unused/*.md")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z]+", args.prefix):
        sys.exit(f"--prefix must be lowercase letters only (got {args.prefix!r}); "
                 "anything starting with a digit, '-', '_' or '.' gets stripped by MyST.")

    repo = find_repo_root(Path.cwd().resolve())
    pages = repo / args.pages_dir
    if not pages.is_dir():
        sys.exit(f"No such directory: {pages}")

    use_git = is_git_repo(repo)
    if use_git:
        dirty = git(repo, "status", "--porcelain").stdout.strip()
        if dirty and args.apply:
            print("Working tree is not clean. Commit or stash first, then re-run.\n")
            print(dirty)
            return 1

    # 1. Build the rename plan.
    sources = sorted(pages.glob("*.md"))
    if args.include_unused and (pages / "unused").is_dir():
        sources += sorted((pages / "unused").glob("*.md"))

    plan: list[tuple[Path, Path]] = []
    skipped: list[Path] = []
    for path in sources:
        match = PAGE_RE.match(path.name)
        if not match:
            skipped.append(path)
            continue
        new_name = f"{args.prefix}{match['num']}-{match['rest']}.md"
        plan.append((path, path.with_name(new_name)))

    if not plan:
        print("Nothing to rename: no files matched NNN-*.md")
        return 0

    collisions = [dst for _, dst in plan if dst.exists() and dst not in {s for s, _ in plan}]
    if collisions:
        print("Refusing to run, these target names already exist:")
        for dst in collisions:
            print(f"  {dst.relative_to(repo)}")
        return 1

    # 2. Show what the URLs become.
    print(f"{'old file':<66} {'new file':<68} url")
    print("-" * 170)
    for src, dst in plan:
        old_url = f"/{args.pages_dir}/{myst_slug(src.stem)}"
        new_url = f"/{args.pages_dir}/{myst_slug(dst.stem)}"
        print(f"{src.name:<66} {dst.name:<68} {old_url}  ->  {new_url}")

    print(f"\n{len(plan)} pages to rename.")
    if skipped:
        print(f"{len(skipped)} unnumbered page(s) left alone: "
              + ", ".join(p.name for p in skipped))

    # Flag pages whose new slug still collides (MyST truncates slugs at 50
    # chars and disambiguates with -1, -2, ... which is where the current
    # m14/m15 URLs come from).
    new_slugs: dict[str, list[str]] = {}
    for _, dst in plan:
        new_slugs.setdefault(myst_slug(dst.stem), []).append(dst.name)
    still_colliding = {s: n for s, n in new_slugs.items() if len(n) > 1}
    if still_colliding:
        print("\nWarning: these slugs still collide after 50-char truncation "
              "and will get -1/-2 suffixes:")
        for slug, names in still_colliding.items():
            print(f"  {slug}: {', '.join(names)}")

    # 3. Find references to the old filenames.
    rename_map = {src.name: dst.name for src, dst in plan}
    stem_map = {src.stem: dst.stem for src, dst in plan}
    ref_pattern = re.compile(
        r"(?<![A-Za-z0-9_.-])(" + "|".join(re.escape(s) for s in stem_map) + r")(?![A-Za-z0-9_-])"
    )

    edits: list[tuple[Path, int]] = []
    for path in iter_text_files(repo):
        if path.name in rename_map:
            continue  # the page itself; its own name rarely appears inside it
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new_text, count = ref_pattern.subn(lambda m: stem_map[m.group(1)], text)
        if count:
            edits.append((path, count))
            if args.apply:
                path.write_text(new_text, encoding="utf-8")

    if edits:
        print("\nReferences to old filenames rewritten in:")
        for path, count in edits:
            print(f"  {path.relative_to(repo)}  ({count})")
    else:
        print("\nNo references to old filenames found outside the pages themselves.")

    # 4. Warn about links written against the OLD (number-stripped) slug,
    #    e.g. a hard-coded https://.../pages/m17-case-c-c-5-of-5 URL. Those
    #    change too, and the script does not touch them.
    old_slugs = {myst_slug(src.stem): src.name for src, _ in plan}
    slug_hits: list[str] = []
    slug_pattern = re.compile(
        r"/pages/(" + "|".join(re.escape(s) for s in old_slugs) + r")(?![A-Za-z0-9_-])"
    )
    for path in iter_text_files(repo):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in slug_pattern.finditer(text):
            slug_hits.append(f"  {path.relative_to(repo)}: /pages/{match.group(1)}")
    if slug_hits:
        print("\nHeads up, these hard-coded site URLs use the old slug and are "
              "NOT rewritten (check them by hand):")
        for hit in sorted(set(slug_hits)):
            print(hit)

    if not args.apply:
        print("\nDry run. Nothing changed. Re-run with --apply to do it.")
        return 0

    # 5. Do the rename.
    for src, dst in plan:
        if use_git:
            result = git(repo, "mv", str(src.relative_to(repo)), str(dst.relative_to(repo)))
            if result.returncode != 0:
                src.rename(dst)  # untracked file; plain rename
        else:
            src.rename(dst)

    print(f"\nRenamed {len(plan)} pages"
          + (f" and rewrote references in {len(edits)} file(s)." if edits else "."))
    print("Next: rebuild (`jupyter book build --html`), then re-run "
          "scripts/make_page_index.py so the instructor index picks up the new URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
