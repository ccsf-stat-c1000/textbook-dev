#!/usr/bin/env python3
"""Remove the `{admonition} Learning Objectives` blocks from every page in pages/.

Usage:
    python _processing/strip_learning_objectives.py          # apply
    python _processing/strip_learning_objectives.py --dry-run # preview only
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"

OPEN_RE = re.compile(r"^(`{3,})\{admonition\}\s*Learning Objectives\s*$", re.IGNORECASE)


def strip(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out = []
    i = 0
    removed = 0

    while i < len(lines):
        m = OPEN_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        fence = m.group(1)
        close_re = re.compile(r"^" + fence + r"\s*$")
        j = i + 1
        while j < len(lines) and not close_re.match(lines[j]):
            j += 1

        if j >= len(lines):  # unterminated fence: leave untouched
            out.append(lines[i])
            i += 1
            continue

        removed += 1
        i = j + 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        # keep exactly one blank line between what came before and what follows
        while out and out[-1].strip() == "":
            out.pop()
        if out and i < len(lines):
            out.append("")

    result = "\n".join(out)
    result = re.sub(r"\n{3,}", "\n\n", result)
    if not result.endswith("\n"):
        result += "\n"
    return result, removed


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = changed = blocks = 0

    for path in sorted(PAGES.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated, n = strip(original)
        files += 1
        if n:
            blocks += n
            changed += 1
            if not dry:
                path.write_text(updated, encoding="utf-8")

    verb = "would remove" if dry else "removed"
    print(f"{files} pages scanned; {verb} {blocks} block(s) across {changed} file(s).")


if __name__ == "__main__":
    main()
