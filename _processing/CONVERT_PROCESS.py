#!/usr/bin/env python3
"""
OLI HTML → MyST Markdown Converter
====================================
Converts Carnegie Mellon OLI course HTML pages to MyST Markdown
for use in a Jupyter Book project.

PROCESS (applied to every file):
1.  Parse HTML with BeautifulSoup.
2.  Extract page title from <title> tag.
3.  Derive output filename slug from the source filename:
      - Strip leading digits + underscore prefix  (e.g. "176_")
      - Non-URL chars (spaces, underscores) → dashes
      - Lowercase; strip .html extension; limit to 50 chars
4.  Locate the content region: all siblings AFTER div#paginationtopwrap.
5.  If present, prepend the learning-objectives block (div#lobjh / div.multi#lobjh).
6.  Walk each content element and call element_to_md() which dispatches on
    element name + CSS classes.
7.  Write one .md file per input HTML file into OUTPUT_DIR.

ELEMENT MAPPING:
  p                         → paragraph (inline-formatted)
  ul / ol                   → markdown lists (nested supported)
  span.imagewrap            → MyST {figure} directive  → images/<filename>
  div.figurewrap            → MyST {figure} or YouTube note
  div.definition            → MyST {admonition} class=definition
  div.pulloutwrap           → MyST {note}
  div.pulloutwrap.tosumup   → MyST {tip} "To Sum Up"
  div.examplewrap           → MyST {admonition} "Example"
  div.activitywrap          → MyST {note} (external activity placeholder)
  div.inquiry               → Q&A block  
  div.section               → ## heading + recursive children
  div.section-didigetthis   → ## heading + recursive children
  table.table.labeled       → GFM markdown table
  table.wbtable             → GFM markdown table
  table.theorem.labeled     → MyST {admonition} "Principle"
  table.formula             → indented code/math block
  div#lobjh / div.multi     → MyST {admonition} "Learning Objectives"
  div.asx                   → MyST {note} (Flash activity, content unavailable)
  img (standalone)          → MyST {figure}
  script[type=math/mml]     → inline $...$ or display $$...$$ (MathML→LaTeX)
  YouTube iframe            → MyST {note} with link

INLINE FORMATTING:
  <em>      → *...*
  <strong>  → **...**
  <span.term> → **...**
  <code>    → `...`
  <a>       → [text](href)
  <sup>     → ^text^  (MyST superscript)
  <sub>     → ~text~  (MyST subscript)
  MathML    → $latex$ (inline) or $$latex$$ (display)

IMAGE PATHS:
  All images are remapped to: images/<basename>
  (Caller is responsible for collecting the actual image files.)

RESUMING AFTER TOKEN LIMIT:
  The script writes a progress file: OUTPUT_DIR/.converted_files.txt
  listing each successfully converted filename (one per line).
  Re-run the script and it will skip already-converted files.
  To force re-convert everything, delete .converted_files.txt.
"""

import os
import re
import sys
import logging
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag
from lxml import etree

# ── Configuration ────────────────────────────────────────────────────────────
INPUT_DIR  = Path("/home/claude/work/extracted")
OUTPUT_DIR = Path("/home/claude/work/markdown")
PROGRESS_FILE = OUTPUT_DIR / ".converted_files.txt"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

# ── Slug helper ──────────────────────────────────────────────────────────────

def _raw_slug(filename: str) -> str:
    """Produce a slug from filename without the leading numeric prefix."""
    stem = Path(filename).stem
    stem = re.sub(r'^\d+_', '', stem)
    stem = re.sub(r'[_\s\.]+', '-', stem)
    stem = stem.lower()
    stem = re.sub(r'-+', '-', stem).strip('-')
    if len(stem) > 50:
        stem = stem[:50].rsplit('-', 1)[0]
    return stem


def build_slug_map(html_files: list) -> dict:
    """
    Build a filename → slug mapping that resolves collisions.
    If two files share the same raw slug, fall back to prefixing with
    the numeric part of the original filename (e.g. '141-' + slug).
    Rules:
      - Remove leading numeric prefix (digits + underscore, e.g. "176_")
      - Replace spaces, underscores, dots with hyphens
      - Lowercase; collapse hyphens; limit to 50 chars
      - On collision: prepend the numeric prefix (e.g. "141-") so each
        file gets a unique, stable slug
    """
    # First pass: collect raw slugs
    raw: dict[str, str] = {}      # filename → raw_slug
    counts: dict[str, int] = {}   # raw_slug → count
    for p in html_files:
        slug = _raw_slug(p.name)
        raw[p.name] = slug
        counts[slug] = counts.get(slug, 0) + 1

    # Second pass: assign final slugs
    result: dict[str, str] = {}
    for p in html_files:
        slug = raw[p.name]
        if counts[slug] > 1:
            # Prepend numeric prefix to disambiguate
            m = re.match(r'^(\d+)_', p.name)
            prefix = m.group(1) + '-' if m else ''
            slug = (prefix + slug)[:50].rstrip('-')
        result[p.name] = slug
    return result


def make_slug(filename: str) -> str:
    """Single-file slug (no collision detection). Use build_slug_map for batches."""
    return _raw_slug(filename)


# ── MathML → LaTeX ───────────────────────────────────────────────────────────

MO_MAP = {
    '∗': r'\times', '·': r'\cdot',
    '≤': r'\leq',   '≥': r'\geq',   '≠': r'\neq',
    '±': r'\pm',    '∞': r'\infty', '∑': r'\sum',
    '∏': r'\prod',  '√': r'\sqrt',  '∈': r'\in',
    '∪': r'\cup',   '∩': r'\cap',   '≈': r'\approx',
    '∝': r'\propto','α': r'\alpha', 'β': r'\beta',
    'σ': r'\sigma', 'μ': r'\mu',    'χ': r'\chi',
    'λ': r'\lambda','θ': r'\theta', 'ρ': r'\rho',
    '→': r'\to',    '⟹': r'\Rightarrow',
}

def _mml_node(node) -> str:
    tag = node.tag.split('}')[-1] if '}' in node.tag else node.tag
    ch  = list(node)
    text = (node.text or '').replace('\u00a0', ' ').strip()

    if tag in ('math', 'mrow', 'mstyle', 'mpadded'):
        return ''.join(_mml_node(c) for c in ch)
    if tag == 'mi':
        return text
    if tag == 'mn':
        return text
    if tag == 'mo':
        return MO_MAP.get(text, text)
    if tag == 'mtext':
        t = text.strip()
        return (r'\text{' + t + '}') if t else ' '
    if tag == 'mspace':
        return ' '
    if tag == 'mfrac' and len(ch) == 2:
        return r'\frac{' + _mml_node(ch[0]) + '}{' + _mml_node(ch[1]) + '}'
    if tag == 'msup' and len(ch) == 2:
        return _mml_node(ch[0]) + '^{' + _mml_node(ch[1]) + '}'
    if tag == 'msub' and len(ch) == 2:
        return _mml_node(ch[0]) + '_{' + _mml_node(ch[1]) + '}'
    if tag == 'msubsup' and len(ch) == 3:
        return _mml_node(ch[0]) + '_{' + _mml_node(ch[1]) + '}^{' + _mml_node(ch[2]) + '}'
    if tag == 'mover' and len(ch) == 2:
        base = _mml_node(ch[0])
        over = _mml_node(ch[1])
        if over in ('¯', '-', '‾', '\u00af'):
            return r'\bar{' + base + '}'
        if over in ('^', '\u005e'):
            return r'\hat{' + base + '}'
        if over == '~':
            return r'\tilde{' + base + '}'
        return r'\overset{' + over + '}{' + base + '}'
    if tag == 'munder' and len(ch) == 2:
        base  = _mml_node(ch[0])
        under = _mml_node(ch[1])
        return r'\underset{' + under + '}{' + base + '}'
    if tag == 'mfenced':
        op = node.get('open', '(')
        cl = node.get('close', ')')
        sep = node.get('separators', ',')
        inner_parts = [_mml_node(c) for c in ch]
        inner = (' ' + sep + ' ').join(inner_parts)
        l = r'\left' + op if op else r'\left('
        r_ = r'\right' + cl if cl else r'\right)'
        return l + inner + r_
    if tag == 'msqrt':
        inner = ''.join(_mml_node(c) for c in ch)
        return r'\sqrt{' + inner + '}'
    if tag == 'mroot' and len(ch) == 2:
        return r'\sqrt[' + _mml_node(ch[1]) + ']{' + _mml_node(ch[0]) + '}'
    if tag == 'mtable':
        rows = []
        for mtr in ch:
            cells = [_mml_node(c) for c in mtr]
            rows.append(' & '.join(cells))
        return r'\begin{matrix}' + r' \\ '.join(rows) + r'\end{matrix}'
    if tag in ('mtd', 'mtr'):
        return ''.join(_mml_node(c) for c in ch)
    if tag == 'menclose':
        return ''.join(_mml_node(c) for c in ch)
    if tag == 'none':
        return ''
    # Fallback
    return text + ''.join(_mml_node(c) for c in ch)


def mml_to_latex(mml_string: str) -> str:
    """Parse a MathML string and return a LaTeX string."""
    if not mml_string:
        return ''
    mml_string = mml_string.strip()
    if not mml_string.startswith('<math'):
        mml_string = '<math>' + mml_string + '</math>'
    try:
        # lxml does not know HTML entities; replace &nbsp; before parsing
        mml_string = mml_string.replace('&nbsp;', '&#160;')
        # lxml needs bytes; strip namespace decls that cause trouble
        mml_bytes = mml_string.encode('utf-8')
        tree = etree.fromstring(mml_bytes)
        return _mml_node(tree)
    except Exception as exc:
        log.warning("MathML parse error: %s | snippet: %s", exc, mml_string[:80])
        return '[math]'


# ── Inline text converter ─────────────────────────────────────────────────────

def inline_to_md(node) -> str:
    """
    Recursively convert an element's children to inline Markdown.
    Handles: text nodes, em, strong, a, code, sup, sub, span, script[math/mml].
    """
    if node is None:
        return ''
    if isinstance(node, NavigableString):
        return str(node)

    tag  = node.name
    cls  = node.get('class', [])

    # Math via MathJax script inside span
    if tag == 'script' and node.get('type', '') == 'math/mml':
        latex = mml_to_latex(node.string or '')
        # Detect display math: script is a direct child of a block element
        parent_tag = node.parent.name if node.parent else ''
        if parent_tag in ('p', 'li', 'td', 'span', 'div'):
            return f'${latex}$'
        return f'$${latex}$$'

    # MathJax rendered span (the hidden original)
    if tag == 'span' and 'MathJax_Preview' in cls:
        return ''  # Skip – the script[math/mml] carries the content
    # MathJax CHTML/SVG rendered output – skip, the math/mml script has the source
    if tag == 'span' and any(c.startswith('MathJax') or c.startswith('mjx-') for c in cls):
        return 

    # Inline math span (sometimes MathJax puts preview here)
    if tag == 'span' and 'math' in ' '.join(cls).lower():
        # Try to find a math/mml script inside
        script = node.find('script', type='math/mml')
        if script:
            return f'${mml_to_latex(script.string or "")}$'

    children_md = ''.join(r or '' for r in (inline_to_md(c) for c in node.children))

    if tag in ('em', 'i'):
        return f'*{children_md.strip()}*' if children_md.strip() else ''
    if tag in ('strong', 'b'):
        return f'**{children_md.strip()}**' if children_md.strip() else ''
    if tag == 'code':
        return f'`{children_md}`'
    if tag == 'sup':
        return f'^{children_md}^'
    if tag == 'sub':
        return f'~{children_md}~'
    if tag == 'a':
        href = node.get('href', '')
        text = children_md.strip()
        if not text:
            return ''
        if href and not href.startswith('/jcourse') and not href.startswith('javascript'):
            return f'[{text}]({href})'
        return text
    if tag == 'br':
        return '  \n'
    if tag == 'span':
        # term class → bold
        if 'term' in cls:
            return f'**{children_md}**'
        return children_md
    if tag in ('p',):
        return children_md  # inline context: don't add block breaks

    return children_md


# ── Image path helper ─────────────────────────────────────────────────────────

def image_path(src: str) -> str:
    """Return the images/<basename> path for a given src URL."""
    if not src:
        return ''
    basename = src.split('/')[-1].split('?')[0]
    return f'images/{basename}'


# ── Table converter ───────────────────────────────────────────────────────────

def table_to_md(table_el) -> str:
    """Convert an HTML table to GFM markdown table."""
    lines = []

    # Collect header row
    headers = []
    thead = table_el.find('thead')
    if thead:
        for th in thead.find_all('th'):
            headers.append(inline_to_md(th).strip().replace('\n', ' '))

    # Collect body rows
    body_rows = []
    tbody = table_el.find('tbody')
    if tbody:
        for tr in tbody.find_all('tr', recursive=False):
            cells = []
            for td in tr.find_all(['td', 'th'], recursive=False):
                # May contain nested table – flatten to text
                inner_table = td.find('table')
                if inner_table:
                    # Render inner table rows as text
                    cell_text = table_to_md(inner_table).replace('\n', '<br>')
                else:
                    cell_text = inline_to_md(td).strip().replace('\n', ' ')
                cells.append(cell_text)
            if any(c.strip() for c in cells):
                body_rows.append(cells)

    if not headers and body_rows:
        # Use first row as header
        headers = body_rows.pop(0)

    if not headers:
        return ''

    col_count = max(len(headers), max((len(r) for r in body_rows), default=0))
    headers += [''] * (col_count - len(headers))

    lines.append('| ' + ' | '.join(headers) + ' |')
    lines.append('| ' + ' | '.join(['---'] * col_count) + ' |')
    for row in body_rows:
        row += [''] * (col_count - len(row))
        lines.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(lines)


# ── List converter ────────────────────────────────────────────────────────────

def list_to_md(el, indent=0) -> str:
    lines = []
    ordered = el.name == 'ol'
    counter = 1
    prefix_sp = '  ' * indent

    for li in el.find_all('li', recursive=False):
        bullet = f'{counter}.' if ordered else '-'
        counter += 1

        # Collect inline + block children of <li>
        parts = []
        sub_lists = []
        for child in li.children:
            if isinstance(child, NavigableString):
                t = str(child).strip()
                if t:
                    parts.append(t)
            elif child.name in ('ul', 'ol'):
                sub_lists.append(child)
            elif child.name == 'p':
                parts.append(inline_to_md(child).strip())
            elif child.name in ('em', 'strong', 'a', 'code', 'span', 'sup', 'sub'):
                parts.append(inline_to_md(child))
            else:
                # recurse inline
                parts.append(inline_to_md(child).strip())

        first_line = ' '.join(p for p in parts if p)
        lines.append(f'{prefix_sp}{bullet} {first_line}')

        for sub in sub_lists:
            lines.append(list_to_md(sub, indent + 1))

    return '\n'.join(lines)


# ── Image/figure helpers ──────────────────────────────────────────────────────

def imagewrap_to_md(el) -> str:
    """Convert span.imagewrap to a MyST figure directive."""
    img = el.find('img')
    if not img:
        # Check for YouTube iframe
        iframe = el.find('iframe')
        if iframe:
            return youtube_to_md(iframe)
        return ''

    src = img.get('src', '')
    alt = re.sub(r'\s+', ' ', img.get('alt', '')).strip()
    path = image_path(src)

    caption_el = el.find('span', class_='caption')
    caption = ''
    if caption_el:
        caption = inline_to_md(caption_el).strip()

    # In MyST the figure *body* (below options) is the visible caption;
    # :alt: is accessibility-only. The OLI source stores descriptions only
    # in alt text, so we use it for both.
    displayed = caption or alt
    directive_lines = [f'```{{figure}} {path}']
    if alt:
        directive_lines.append(f':alt: {alt}')
    if displayed:
        directive_lines.append('')
        directive_lines.append(displayed)
    directive_lines.append('```')
    return '\n'.join(directive_lines)


def youtube_to_md(iframe) -> str:
    """Convert a YouTube iframe to a MyST note with link."""
    src = iframe.get('src', '')
    title = iframe.get('title', 'Video')
    # Extract video ID
    vid_id = ''
    m = re.search(r'embed/([A-Za-z0-9_-]+)', src)
    if m:
        vid_id = m.group(1)
    url = f'https://www.youtube.com/watch?v={vid_id}' if vid_id else src

    return f'''```{{note}} Video
[{title}]({url})
```'''


def figurewrap_to_md(el) -> str:
    """Convert div.figurewrap to MyST figure (image or video)."""
    iframe = el.find('iframe')
    if iframe and 'youtube' in iframe.get('src', ''):
        title_el = el.find('h5')
        title = title_el.get_text(strip=True) if title_el else ''
        caption_el = el.find('span', class_='caption')
        caption = inline_to_md(caption_el).strip() if caption_el else ''
        note_body = youtube_to_md(iframe)
        if title:
            note_body = note_body.replace('```{note} Video', f'```{{note}} {title}')
        if caption:
            note_body = note_body.rstrip('```') + f'\n\n{caption}\n```'
        return note_body

    # Regular image figure
    img_wrap = el.find('span', class_='imagewrap')
    if img_wrap:
        return imagewrap_to_md(img_wrap)

    img = el.find('img')
    if img:
        src = img.get('src', '')
        alt = re.sub(r'\s+', ' ', img.get('alt', '')).strip()
        path = image_path(src)
        caption_el = el.find('span', class_='caption')
        caption = inline_to_md(caption_el).strip() if caption_el else ''
        displayed = caption or alt
        lines = [f'```{{figure}} {path}']
        if alt:
            lines.append(f':alt: {alt}')
        if displayed:
            lines.append('')
            lines.append(displayed)
        lines.append('```')
        return '\n'.join(lines)

    return ''


# ── Admonition helpers ────────────────────────────────────────────────────────

def indent_block(text: str, spaces: int = 4) -> str:
    pad = ' ' * spaces
    return '\n'.join(pad + l if l.strip() else '' for l in text.split('\n'))


def admonition_to_md(kind: str, title: str, body: str) -> str:
    """Produce a MyST admonition block."""
    header = f'```{{admonition}} {title}' if kind == 'admonition' else f'```{{{kind}}}'
    if kind != 'admonition' and title:
        header += f'\n:class: {kind}'
    lines = [header]
    if body.strip():
        lines.append(indent_block(body.strip()))
    lines.append('```')
    return '\n'.join(lines)


# ── Core element dispatcher ───────────────────────────────────────────────────

def element_to_md(el, depth=0) -> str:
    """
    Convert a single BeautifulSoup element to MyST markdown string.
    depth = heading depth offset (0 = top level, adds ## for h2 etc.)
    """
    if isinstance(el, NavigableString):
        t = str(el).strip()
        return t if t else ''

    tag = el.name
    cls = el.get('class', [])
    el_id = el.get('id', '')

    # ── Skip non-content elements ──────────────────────────────────────────
    if tag in ('script', 'style', 'noscript'):
        return ''
    if tag == 'div' and el_id in ('paginationtop', 'paginationtopwrap',
                                   'paginationbottomwrap', 'paginationbottom',
                                   'tinyfooter', 'MathJax_Message'):
        return ''

    # ── Learning objectives ────────────────────────────────────────────────
    if el_id == 'lobjh' or (tag == 'div' and 'multi' in cls and el_id == 'lobjh'):
        items = []
        for li in el.find_all('li'):
            items.append('- ' + inline_to_md(li).strip())
        body = '\n'.join(items)
        return admonition_to_md('admonition', 'Learning Objectives', body)

    # ── Paragraphs ─────────────────────────────────────────────────────────
    if tag == 'p':
        text = inline_to_md(el).strip()
        # Collapse internal whitespace from HTML indentation
        text = re.sub(r'[ \t]*\n[ \t]*', ' ', text)
        text = re.sub(r' {2,}', ' ', text)
        return text if text else ''

    # ── Lists ──────────────────────────────────────────────────────────────
    if tag in ('ul', 'ol'):
        return list_to_md(el)

    # ── Standalone image ───────────────────────────────────────────────────
    if tag == 'img':
        src = el.get('src', '')
        alt = re.sub(r'\s+', ' ', el.get('alt', '')).strip()
        if not src or 'inline_assessment' in src:
            return ''
        path = image_path(src)
        lines = [f'```{{figure}} {path}']
        if alt:
            lines.append(f':alt: {alt}')
            lines.append('')
            lines.append(alt)   # alt is both accessibility attr and visible caption
        lines.append('```')
        return '\n'.join(lines)

    # ── span.imagewrap ─────────────────────────────────────────────────────
    if tag == 'span' and 'imagewrap' in cls:
        return imagewrap_to_md(el)

    # ── div.figurewrap ─────────────────────────────────────────────────────
    if tag == 'div' and 'figurewrap' in cls:
        return figurewrap_to_md(el)

    # ── div.image.shouldbeleft ─────────────────────────────────────────────
    if tag == 'div' and 'image' in cls:
        img = el.find('img')
        if img:
            return element_to_md(img)
        return ''

    # ── Definitions ────────────────────────────────────────────────────────
    if tag == 'div' and 'definition' in cls:
        dt = el.find('dt')
        dd = el.find('dd')
        term = dt.get_text(strip=True) if dt else ''
        meaning = inline_to_md(dd).strip() if dd else ''
        return admonition_to_md('admonition', f'Definition: {term}', meaning)

    # ── Pullout / note boxes ───────────────────────────────────────────────
    if tag == 'div' and 'pulloutwrap' in cls:
        pullout = el.find('div', class_='pullout')
        content_div = pullout or el
        # Remove the label span before extracting text
        lbl_span = content_div.find('span', class_='pullout-lbl')
        lbl_text = lbl_span.get_text(strip=True) if lbl_span else ''
        if lbl_span:
            lbl_span.decompose()

        body = '\n\n'.join(
            element_to_md(c)
            for c in content_div.children
            if not isinstance(c, NavigableString) or c.strip()
        )
        body = body.strip()

        if 'tosumup' in cls:
            kind, title = 'tip', lbl_text or 'To Sum Up'
        elif 'note' in cls:
            kind, title = 'note', lbl_text or ''
        else:
            kind, title = 'note', lbl_text or ''

        if kind == 'note' and not title:
            return f'```{{note}}\n{indent_block(body)}\n```'
        return admonition_to_md(kind, title, body)

    # ── Examples ───────────────────────────────────────────────────────────
    if tag == 'div' and 'examplewrap' in cls:
        head = el.find('div', class_='exHead')
        title_el = el.find('h5')
        title = title_el.get_text(strip=True) if title_el else 'Example'
        example_div = el.find('div', class_='example')
        body_el = example_div or el
        parts = []
        for child in body_el.children:
            if child == title_el:
                continue
            md = element_to_md(child)
            if md:
                parts.append(md)
        body = '\n\n'.join(parts)
        return admonition_to_md('admonition', f'Example: {title}' if title != 'Example' else 'Example', body)

    # ── Inquiry (Q&A) ──────────────────────────────────────────────────────
    if tag == 'div' and 'inquiry' in cls:
        parts = []
        for div in el.find_all('div', recursive=False):
            label_el = div.find('em')
            label = label_el.get_text(strip=True) if label_el else ''
            if label_el:
                label_el.decompose()
            text = inline_to_md(div).strip()
            if 'answer' in div.get('class', []):
                parts.append(f'**Answer:** {text}')
            else:
                parts.append(f'**{label}** {text}' if label else text)
        body = '\n\n'.join(parts)
        return f'```{{admonition}} Question & Answer\n{indent_block(body)}\n```'

    # ── Activities ─────────────────────────────────────────────────────────
    if tag == 'div' and 'activitywrap' in cls:
        # Extract activity type from classes
        purpose_classes = [c for c in cls if c not in ('activitywrap', 'purpose', 'wbactivity')]
        purpose = purpose_classes[0].replace('-', ' ').title() if purpose_classes else 'Activity'

        # Try to get a title from nested h3/a
        h3 = el.find('h3')
        link = h3.find('a') if h3 else None
        act_title = link.get_text(strip=True) if link else (h3.get_text(strip=True) if h3 else '')

        if purpose.lower() in ('learnbydoing', 'learn by doing'):
            purpose = 'Learn By Doing'
        elif purpose.lower() in ('didigetthis', 'did i get this'):
            purpose = 'Did I Get This?'
        elif purpose.lower() in ('myresponse', 'my response'):
            purpose = 'My Response'
        elif purpose.lower() in ('manystudentswonder', 'many students wonder'):
            purpose = 'Many Students Wonder'

        body_lines = [f'**{purpose}**']
        if act_title:
            body_lines.append(f'\n{act_title}')
        body_lines.append('\n*(Interactive activity — available in the OLI platform)*')
        return f'```{{note}}\n' + indent_block('\n'.join(body_lines)) + '\n```'

    # ── ASX (Flash) ────────────────────────────────────────────────────────
    if tag == 'div' and 'asx' in cls:
        # May wrap an activitywrap — delegate to that
        inner_act = el.find('div', class_='activitywrap')
        if inner_act:
            return element_to_md(inner_act)
        return '```{note}\n    *(Interactive Flash activity — not available in this format)*\n```'

    # ── Theorem table ──────────────────────────────────────────────────────
    if tag == 'table' and 'theorem' in cls:
        thead = el.find('thead')
        title = thead.get_text(strip=True) if thead else 'Principle'
        tbody = el.find('tbody')
        body = inline_to_md(tbody).strip() if tbody else ''
        # Try to get real body from inner theorem div
        thm_div = el.find('div', class_='theorem')
        if thm_div:
            stmt = thm_div.find('div', class_='statement')
            body = '\n\n'.join(element_to_md(c) for c in (stmt or thm_div).children if not isinstance(c, NavigableString) or c.strip())
        return admonition_to_md('admonition', title, body.strip())

    # ── Data / formula tables ──────────────────────────────────────────────
    if tag == 'table' and 'formula' in cls:
        text = el.get_text(separator=' ', strip=True)
        return f'```\n{text}\n```'

    # ── Regular data tables ────────────────────────────────────────────────
    if tag == 'table':
        # Outer labeled wrapper → find inner wbtable
        if 'labeled' in cls:
            inner = el.find('table', class_='wbtable')
            if inner:
                return table_to_md(inner)
        return table_to_md(el)

    # ── Section divs ──────────────────────────────────────────────────────
    if tag == 'div' and ('section' in cls):
        contain = el.find('div', class_='sectionContain') or el
        h2 = contain.find('h2')
        heading_text = ''
        if h2:
            span = h2.find('span')
            heading_text = span.get_text(strip=True) if span else h2.get_text(strip=True)
            h2.decompose()

        parts = []
        if heading_text:
            hashes = '#' * (2 + depth)
            parts.append(f'{hashes} {heading_text}')

        for child in contain.children:
            if isinstance(child, NavigableString):
                t = str(child).strip()
                if t:
                    parts.append(t)
            else:
                md = element_to_md(child, depth + 1)
                if md:
                    parts.append(md)

        return '\n\n'.join(parts)

    # ── Generic div (recurse) ──────────────────────────────────────────────
    if tag == 'div':
        # Skip UI-only divs
        if el_id in ('annotatorcontainer', 'tinyfooter', 'subMenuExpand'):
            return ''
        if any(c in cls for c in ('controlpanel', 'supportPanel', 'head',
                                   'activityhead', 'activityinfo', 'actContain')):
            return ''
        parts = []
        for child in el.children:
            md = element_to_md(child, depth)
            if md:
                parts.append(md)
        return '\n\n'.join(p for p in parts if p)

    # ── Headings ───────────────────────────────────────────────────────────
    if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        level = int(tag[1]) + depth
        level = min(level, 6)
        hashes = '#' * level
        text = el.get_text(strip=True)
        return f'{hashes} {text}'

    # ── Fallback ───────────────────────────────────────────────────────────
    return inline_to_md(el).strip()


# ── Page converter ────────────────────────────────────────────────────────────

def convert_file(html_path: Path) -> str:
    """Parse one HTML file and return the full MyST markdown string."""
    with open(html_path, encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # ── Title ──────────────────────────────────────────────────────────────
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else make_slug(html_path.name)

    # ── Content region ─────────────────────────────────────────────────────
    pagination = soup.find('div', id='paginationtopwrap')
    if not pagination:
        log.warning("No paginationtopwrap in %s", html_path.name)
        return ''

    content_elements = list(pagination.find_next_siblings())
    if not content_elements:
        log.warning("No content after pagination in %s", html_path.name)
        return ''

    # ── Build markdown ──────────────────────────────────────────────────────
    parts = [f'# {title}', '']

    for el in content_elements:
        # Skip bottom pagination
        if isinstance(el, Tag) and el.get('id', '') in (
                'paginationbottomwrap', 'paginationbottom', 'tinyfooter',
                'complementary', 'MathJax_Message', 'annotatorcontainer'):
            break

        md = element_to_md(el)
        if md:
            parts.append(md)

    # ── Clean up whitespace ────────────────────────────────────────────────
    text = '\n\n'.join(p for p in parts if p is not None)
    # Collapse 3+ blank lines → 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


# ── Batch runner ──────────────────────────────────────────────────────────────

def collect_image_refs(html_path: Path) -> list[str]:
    """Return list of image src values found in one HTML file's content."""
    with open(html_path, encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f, 'html.parser')
    pagination = soup.find('div', id='paginationtopwrap')
    if not pagination:
        return []
    imgs = []
    for el in pagination.find_next_siblings():
        for img in (el.find_all('img') if hasattr(el, 'find_all') else []):
            src = img.get('src', '')
            if src and 'inline_assessment' not in src:
                imgs.append(src)
    return imgs


def load_progress() -> set:
    if PROGRESS_FILE.exists():
        return set(PROGRESS_FILE.read_text().splitlines())
    return set()


def save_progress(done: set):
    PROGRESS_FILE.write_text('\n'.join(sorted(done)))


def run():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_files = sorted(INPUT_DIR.glob('*.html'))
    if not html_files:
        log.error("No HTML files found in %s", INPUT_DIR)
        sys.exit(1)

    slug_map = build_slug_map(html_files)
    done = load_progress()
    all_images: dict[str, str] = {}   # basename → original src

    converted = 0
    skipped = 0
    errors = 0

    for html_path in html_files:
        fname = html_path.name

        if fname in done:
            log.info("SKIP (already done): %s", fname)
            skipped += 1
            continue

        slug = slug_map[fname]
        out_path = OUTPUT_DIR / f'{slug}.md'

        try:
            md = convert_file(html_path)
            if not md:
                log.warning("Empty output for %s", fname)
                continue

            out_path.write_text(md, encoding='utf-8')
            done.add(fname)
            save_progress(done)
            converted += 1
            log.info("OK: %s → %s", fname, out_path.name)

            # Collect image refs for manifest
            for src in collect_image_refs(html_path):
                basename = src.split('/')[-1].split('?')[0]
                all_images[basename] = src

        except Exception as exc:
            log.error("FAILED: %s — %s", fname, exc)
            import traceback; traceback.print_exc()
            errors += 1

    # Write image manifest
    manifest_path = OUTPUT_DIR / 'image_manifest.txt'
    with open(manifest_path, 'w') as mf:
        mf.write("# Image manifest — original src URLs\n")
        for basename, src in sorted(all_images.items()):
            mf.write(f'{basename}\t{src}\n')

    log.info("\n=== Done: %d converted, %d skipped, %d errors ===", converted, skipped, errors)
    log.info("Image manifest written: %s (%d images)", manifest_path, len(all_images))
    if errors:
        log.warning("Re-run after fixing errors; progress is saved.")


if __name__ == '__main__':
    run()
