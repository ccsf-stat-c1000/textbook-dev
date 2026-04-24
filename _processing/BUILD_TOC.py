#!/usr/bin/env python3
"""
Build new filenames (with page num + module num) and generate _toc.yml.

New filename format: {page_num:03d}-m{module_num:02d}-{page_slug}.md
  e.g. 009-m03-the-big-picture.md

Unit→module mapping:
  Unit 1: Introduction              → Modules 1–3
  Unit 2: Exploratory Data Analysis → Modules 4–5
  Unit 3: Producing Data            → Modules 6–7
  Unit 4: Probability               → Modules 8–12
  Unit 5: Inference                 → Modules 13–17

No-module pages are assigned by page-number proximity:
  010, 011, 066 → Unit 2 (assign to module 4 or 5 by position)
  067, 087      → Unit 3 (modules 6, 7)
  173, 174, 178 → Unit 5 start (module 13)
  264           → Unit 5 end (module 17)
"""

import os, re, sys
from pathlib import Path
from bs4 import BeautifulSoup

EXTRACTED = Path("/home/claude/work/extracted")
OLD_MD    = Path("/home/claude/work/markdown")
NEW_MD    = Path("/home/claude/work/markdown_new")

# ── Unit definitions ──────────────────────────────────────────────────────────

UNITS = {
    1: "Introduction",
    2: "Exploratory Data Analysis",
    3: "Producing Data",
    4: "Probability",
    5: "Inference",
}

MODULE_TO_UNIT = {}
for mod in range(1, 4):   MODULE_TO_UNIT[mod] = 1
for mod in range(4, 6):   MODULE_TO_UNIT[mod] = 2
for mod in range(6, 8):   MODULE_TO_UNIT[mod] = 3
for mod in range(8, 13):  MODULE_TO_UNIT[mod] = 4
for mod in range(13, 18): MODULE_TO_UNIT[mod] = 5

# No-module page overrides: page_num → module_num
NO_MOD_OVERRIDE = {
    10: 4,   # EDA intro 1 → M4 (Examining Distributions)
    11: 4,   # EDA intro 2 → M4
    66: 5,   # Summary EDA → M5 (last of Unit 2)
    67: 6,   # Intro Producing Data → M6 (Sampling, first of Unit 3)
    87: 7,   # Summary Producing Data → M7 (last of Unit 3)
    173: 12, # Summary Probability → M12 (last of Unit 4)
    174: 13, # Statistical Inference → M13 (first of Unit 5)
    178: 13, # Inference For One Variable → M13
    264: 17, # Summary Inference → M17 (last of Unit 5)
}

# Module titles (from HTML)
MODULE_TITLES = {
    1:  "Introduction",
    2:  "Learning Strategies",
    3:  "The Big Picture",
    4:  "Examining Distributions",
    5:  "Examining Relationships",
    6:  "Sampling",
    7:  "Designing Studies",
    8:  "Introduction to Probability",
    9:  "Finding Probability of Events",
    10: "Conditional Probability and Independence",
    11: "Random Variables",
    12: "Sampling Distributions",
    13: "Introduction to Inference",
    14: "Estimation",
    15: "Hypothesis Testing",
    16: "Inference for Relationships",
    17: "Inference for Relationships Continued",
}

# ── Slug helpers ──────────────────────────────────────────────────────────────

def page_slug(title: str) -> str:
    s = re.sub(r'[→←–—]', '-', title)
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).lower()
    s = re.sub(r'-+', '-', s).strip('-')
    # Limit to 40 chars for reasonable total filename length
    if len(s) > 55:
        s = s[:55].rsplit('-', 1)[0]
    return s

# ── Gather all pages ──────────────────────────────────────────────────────────

def gather_pages():
    pages = []
    for fname in sorted(os.listdir(EXTRACTED)):
        if not fname.endswith('.html'):
            continue

        # Page number
        m = re.match(r'^(\d+)_', fname)
        if m:
            page_num = int(m.group(1))
        else:
            # "undefined_17.html" → use the suffix number
            m2 = re.search(r'(\d+)', fname)
            page_num = int(m2.group(1)) if m2 else 9999

        with open(EXTRACTED / fname, encoding='utf-8', errors='replace') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Page title
        title_tag = soup.find('title')
        title = title_tag.get_text(strip=True) if title_tag else fname

        # Module
        nav = soup.find('div', class_='subNavigation')
        mod_num = None
        mod_title = ''
        if nav:
            current_li = nav.find('li', class_='current')
            if current_li:
                a = current_li.find('a')
                if a:
                    ta = a.get('title', '')
                    m2 = re.match(r'Module\s+(\d+)\s+(.*)', ta)
                    if m2:
                        mod_num = int(m2.group(1))
                        mod_title = m2.group(2)

        # Override for no-module pages
        if mod_num is None:
            mod_num = NO_MOD_OVERRIDE.get(page_num, 1)
        mod_title = mod_title or MODULE_TITLES.get(mod_num, f'Module {mod_num}')

        unit_num = MODULE_TO_UNIT.get(mod_num, 1)
        unit_title = UNITS[unit_num]

        pages.append({
            'page_num': page_num,
            'src_file': fname,
            'title': title,
            'mod_num': mod_num,
            'mod_title': mod_title,
            'unit_num': unit_num,
            'unit_title': unit_title,
        })

    # Sort by unit → module → page number
    pages.sort(key=lambda p: (p['unit_num'], p['mod_num'], p['page_num']))
    return pages

# ── Assign new filenames (collision-safe) ─────────────────────────────────────

def assign_filenames(pages):
    seen = {}
    for p in pages:
        pn = p['page_num']
        mn = p['mod_num']
        slug = page_slug(p['title'])
        candidate = f"{pn:03d}-m{mn:02d}-{slug}"
        # Collision: same candidate for two pages → shouldn't happen since page_num is unique
        # but protect anyway
        if candidate in seen:
            candidate = f"{pn:03d}-m{mn:02d}-p{pn}-{slug}"
        seen[candidate] = True
        p['new_slug'] = candidate
        p['new_filename'] = candidate + '.md'

# ── Old slug lookup (to find which old .md to read) ──────────────────────────

def _raw_slug_old(filename: str) -> str:
    stem = Path(filename).stem
    stem = re.sub(r'^\d+_', '', stem)
    stem = re.sub(r'[_\s\.]+', '-', stem)
    stem = stem.lower()
    stem = re.sub(r'-+', '-', stem).strip('-')
    if len(stem) > 50:
        stem = stem[:50].rsplit('-', 1)[0]
    return stem

def build_old_slug_map():
    html_files = sorted(EXTRACTED.glob('*.html'))
    raw = {p.name: _raw_slug_old(p.name) for p in html_files}
    counts = {}
    for slug in raw.values():
        counts[slug] = counts.get(slug, 0) + 1
    result = {}
    for p in html_files:
        slug = raw[p.name]
        if counts[slug] > 1:
            m = re.match(r'^(\d+)_', p.name)
            prefix = m.group(1) + '-' if m else ''
            slug = (prefix + slug)[:50].rstrip('-')
        result[p.name] = slug
    return result

# ── Build TOC YAML ────────────────────────────────────────────────────────────

def build_toc(pages):
    """Return _toc.yml content string (Jupyter Book format)."""
    lines = [
        "# Table of Contents",
        "# Jupyter Book _toc.yml",
        "# Auto-generated from OLI Probability & Statistics HTML pages",
        "",
        "format: jb-book",
        "root: intro",
        "parts:",
    ]

    # Group: unit → module → pages
    from collections import OrderedDict
    units = OrderedDict()
    for p in pages:
        u = (p['unit_num'], p['unit_title'])
        m = (p['mod_num'], p['mod_title'])
        units.setdefault(u, OrderedDict()).setdefault(m, []).append(p)

    for (unit_num, unit_title), modules in units.items():
        lines.append(f"  - caption: \"Unit {unit_num}: {unit_title}\"")
        lines.append("    chapters:")

        for (mod_num, mod_title), mod_pages in modules.items():
            # First page of the module is the chapter; rest are sections
            first = mod_pages[0]
            rest  = mod_pages[1:]
            slug  = first['new_slug']
            if rest:
                lines.append(f"    - file: {slug}")
                lines.append(f"      title: \"Module {mod_num}: {mod_title}\"")
                lines.append(f"      sections:")
                for pg in rest:
                    lines.append(f"      - file: {pg['new_slug']}")
            else:
                lines.append(f"    - file: {slug}")
                lines.append(f"      title: \"Module {mod_num}: {mod_title}\"")

    return "\n".join(lines) + "\n"

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    pages = gather_pages()
    assign_filenames(pages)

    # Print new filename mapping
    for p in pages:
        print(f"  {p['page_num']:03d} U{p['unit_num']} M{p['mod_num']:02d} | {p['new_filename']}")

    print(f"\nTotal pages: {len(pages)}")
    # Check for duplicates
    slugs = [p['new_slug'] for p in pages]
    dups = [s for s in slugs if slugs.count(s) > 1]
    if dups:
        print(f"DUPLICATE SLUGS: {set(dups)}")
    else:
        print("No duplicate slugs.")
