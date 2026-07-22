#!/usr/bin/env python3
"""Generate the instructor page-reference index for the STAT C1000 textbook.

Why this exists
---------------
The book is a website, so it has no printed page numbers. `myst.yml` turns on
flat title numbering (`numbering.title.offset: 0`), which stamps every page
with a stable number (1, 2, 3, ...) in reading order and shows it in the
sidebar and page heading. This script exports that same numbering to a CSV so
instructors can search it, paste links into Canvas//a syllabus, and say
"open page 30" in class.

Usage
-----
    jupyter-book build --html      # or: myst build --site
    python scripts/make_page_index.py

Writes reference/page-index.csv. Re-run it whenever pages are added, removed,
or reordered in toc.yml, because the page numbers shift.
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys

# Root of the deployed site. Matches BASE_URL in .github/workflows/deploy-jb2.yml.
SITE_ROOT = "https://ccsf-stat-c1000.github.io/textbook"

REPO = pathlib.Path(__file__).resolve().parent.parent
CONTENT = REPO / "_build" / "site" / "content"
OUT = REPO / "reference" / "page-index.csv"

# Source filenames carry an OLI module code (m03-m17). toc.yml groups those
# modules into units and sections; keep this table in sync with toc.yml.
MODULES = {
    "m03": ("(front matter)", "The Big Picture"),
    "m06": ("Unit 1: Producing Data", "Section 1: Sampling"),
    "m07": ("Unit 1: Producing Data", "Section 2: Designing Studies"),
    "m04": ("Unit 2: Exploratory Data Analysis", "Section 3: Examining Distributions"),
    "m05": ("Unit 2: Exploratory Data Analysis", "Section 4: Examining Relationships"),
    "m08": ("Unit 3: Probability", "Section 5: Introduction (Probability)"),
    "m09": ("Unit 3: Probability", "Section 6: Finding Probability of Events"),
    "m10": ("Unit 3: Probability", "Section 7: Conditional Probability and Independence"),
    "m11": ("Unit 3: Probability", "Section 8: Random Variables"),
    "m12": ("Unit 3: Probability", "Section 9: Sampling Distributions"),
    "m13": ("Unit 4: Inference", "Section 10: Introduction to Inference"),
    "m14": ("Unit 4: Inference", "Section 11: Estimation"),
    "m15": ("Unit 4: Inference", "Section 12: Hypothesis Testing"),
    "m16": ("Unit 4: Inference", "Section 13: Inference for Relationships"),
    "m17": ("Unit 4: Inference", "Section 14: Inference for Relationships Continued"),
}


def classify(source_name: str) -> tuple[str, str]:
    """Map a source filename such as '019-m04-histogram-1-of-3.md' to unit/section."""
    match = re.search(r"\bm\d{2}\b", source_name)
    if match and match.group(0) in MODULES:
        return MODULES[match.group(0)]
    return ("(front matter)", "(front matter)")


def page_url(slug: str) -> str:
    """MyST serves the project index at the site root and everything else under /pages/."""
    return SITE_ROOT if slug == "index" else f"{SITE_ROOT}/pages/{slug}"


def sort_key(row: dict) -> tuple:
    """Sort by the numeric enumerator; unnumbered pages sink to the bottom."""
    enumerator = str(row["number"])
    return (0, int(enumerator)) if enumerator.isdigit() else (1, 0)


def main() -> int:
    if not CONTENT.is_dir():
        sys.exit(
            f"No build output at {CONTENT}.\n"
            "Run 'jupyter-book build --html' first, then re-run this script."
        )

    rows = []
    for path in CONTENT.glob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        frontmatter = data.get("frontmatter", {})
        enumerator = frontmatter.get("enumerator")
        if enumerator is None:
            # Pages outside the toc are still built but never numbered; skip them.
            continue
        slug = data.get("slug", "")
        source = (data.get("location") or "").split("/")[-1]
        unit, section = classify(source)
        rows.append(
            {
                "number": enumerator,
                "title": frontmatter.get("title", ""),
                "unit": unit,
                "section": section,
                "url": page_url(slug),
                "source_file": source,
            }
        )

    if not rows:
        sys.exit("Build output contained no numbered pages; is numbering enabled in myst.yml?")

    rows.sort(key=sort_key)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["number", "title", "unit", "section", "url", "source_file"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} pages to {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
