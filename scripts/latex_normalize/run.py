#!/usr/bin/env python3
"""Apply the Unicode/plaintext -> LaTeX math conversion to all book pages.

Usage:
    python3 scripts/latex_normalize/run.py            # convert in place
    python3 scripts/latex_normalize/run.py --check    # dry run, report only

Idempotent: existing $...$ / code is protected, so re-running is safe.
Review changes with `git diff` and rebuild the book afterwards.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from convert_math import convert

ROOT  = pathlib.Path(__file__).resolve().parents[2]   # textbook-dev/
PAGES = ROOT / 'pages'

def main():
    dry = '--check' in sys.argv or '--dry-run' in sys.argv
    changed = total = 0
    for md in sorted(PAGES.glob('*.md')):
        src = md.read_text(encoding='utf-8')
        out = convert(src)
        total += 1
        if out != src:
            changed += 1
            print(f'{"[dry] " if dry else ""}{md.name}: +{out.count("$") - src.count("$")} $')
            if not dry:
                md.write_text(out, encoding='utf-8')
    print(f'\n{changed}/{total} pages {"would change" if dry else "changed"}.')

if __name__ == '__main__':
    main()
