# STAT C1000 Textbook — Editorial & Style Guide

This guide defines the conventions used across all pages so the book stays
consistent as it is edited. Follow it for every page in `pages/`.

## Page structure

1. `# Title` — one H1 per page, matching the TOC entry.
2. Learning objectives (when the page opens a topic):

   ```{admonition} Learning Objectives
   :class: note

   - Objective one.
   - Objective two.
   ```

3. Body prose in H2/H3 sections. No empty headings. No fixed-width
   hard-wrapped prose (let lines run long; one paragraph per line is fine).

## Admonitions

- Directive bodies are **flush left** inside the fence — never indented
  4 spaces (that renders as a code block).
- Use colon fences `:::{admonition}` (or more colons for nesting) whenever the
  body contains another directive, a code fence, a table, or a figure.
- Classes: examples use `:class: tip` with title `Example: <Name>`;
  comments/caveats use `:class: important` with title `Comment`;
  definitions/rules use `:class: note`.

## Quizzes (concept checks)

- Use the `{quiz}` / `{quiz-multi}` directives (plugin: `pages/quiz.mjs`).
  See `pages/011-m04-exploratory-data-analysis-2-of-2.md` for the reference page.
- Every former OLI activity placeholder ("Did I Get This?", "Learn By Doing")
  is replaced with one or more authored quizzes at the same location,
  written from the surrounding content.
- Conventions:
  - 2-4 choices for `{quiz}`; 4-5 for `{quiz-multi}`.
  - Always provide `:hint:` and either `:explanation:` or per-choice
    `:feedback-N:` (feedback for wrong answers should teach, not just say "no").
  - Question text supports inline math `$...$`.
  - Precede a run of quizzes with a short lead-in or `## Concept Check` H2
    when it isn't already flowing from the prose.

## Graphics

All new graphics are hand-authored **SVG** files in `pages/images/gen/`,
named `mXX-short-name.svg`. Legacy OLI GIF/PNG images are being replaced:

- **Images of tables → real markdown tables.** Never keep a table as an image.
- **Charts and diagrams → redrawn SVG** in the shared style below.
- Every figure keeps meaningful `:alt:` text.

### Shared SVG style

- `viewBox="0 0 640 H"` (H as needed, typically 360-420); no fixed width/height
  attributes (let the theme scale it).
- Font: `font-family="Helvetica, Arial, sans-serif"`; axis labels 16px,
  tick labels 13px, titles 18px bold.
- Palette:
  - primary fill `#7cb2e8`, primary stroke `#2b6cb0` (bars, curves, points)
  - accent red `#c53030` (highlights, rejection regions, residuals)
  - green `#2f855a` (secondary series, "correct/success")
  - orange `#dd6b20` (tertiary series)
  - text and axes `#333333`, gridlines `#dddddd`
- Axes: 1.5px stroke `#333`, small outward ticks, unboxed (no top/right spines).
- Bars: 1px stroke `#2b6cb0`, fill `#7cb2e8`; gap between categorical bars,
  no gap for histogram bins.
- Normal curves: 2.5px stroke; shaded areas fill `#7cb2e8` at `fill-opacity="0.55"`
  (accent red for rejection regions).
- Diagrams (flowcharts like the Big Picture): rounded rects `rx="10"`,
  fill `#eaf2fb`, stroke `#2b6cb0`, arrows with a shared `#arrow` marker.

## Technology neutrality

The book is technology-agnostic. Remove or generalize references to specific
software (Excel, Minitab, R, StatCrunch, TI calculators) and to OLI's
interactive applets/simulations. Phrase as "using statistical software or a
calculator". Output-style tables formerly shown as screenshots are retyped as
plain markdown tables labeled "typical software output".

## Language & math

- Decimals get a leading zero (0.44, not .44).
- Math in LaTeX: inline `$\bar{x}$`, display `$$ ... $$`. Prefer LaTeX over
  images of formulas. Standard symbols: $\bar{x}$, $s$, $\mu$, $\sigma$, $\hat{p}$,
  $p$, $H_0$, $H_a$, $\bar{x}_1 - \bar{x}_2$.
- "SD" spelled out on first use per page. US spelling. Serial comma.
- Keep OLI's pedagogy (Big Picture framing, 4-step process, role-type
  classification C→C, C→Q, Q→C, Q→Q) intact.

## Licensing

Content is adapted from OLI Probability & Statistics (CC BY-NC-SA 4.0);
the project license is **CC-BY-NC-SA-4.0** everywhere (myst.yml, intro.md, LICENSE).
