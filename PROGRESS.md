# Cleanup Progress Tracker

Working conventions: see `STYLE_GUIDE.md`. Reference page: `pages/011-m04-exploratory-data-analysis-2-of-2.md`.

Per-page work: fix directive formatting → remove OLI cruft/applet refs → convert
table-images to markdown tables → redraw remaining figures as SVG in
`pages/images/gen/` → author quizzes at every former activity placeholder →
generalize technology references.

## Status by module

| Module | Pages | Status |
| --- | --- | --- |
| Config + style guide | — | done |
| m01 Introduction | 002 | done |
| m02 Learning Strategies | 005-007 | done |
| m03 The Big Picture | 009 | done |
| m04 Examining Distributions | 010-037 | done |
| m05 Examining Relationships | 039-066 | done |
| m06 Sampling | 067-071 | done |
| m07 Designing Studies | 073-087 | done |
| m08 Probability Intro | 089-096 | done |
| m09 Finding Probability | 098-114 | done |
| m10 Conditional Probability | 116-126 | done |
| m11 Random Variables | 128-162 | done |
| m12 Sampling Distributions | 164-173 | done |
| m13 Intro to Inference | 174-178 | done |
| m14 Estimation | 180-194 | done |
| m15 Hypothesis Testing | 196-226 | done |
| m16 Inference for Relationships | 228-253 | done |
| m17 Inference (continued) | 255-264 | done |
| Final verification | — | done |

## Verification results (final pass)

- No remaining "Interactive activity"/"Sectionnest" placeholders in `pages/`
  (the only match is `pages/unused/003-m01-pre-course-survey.md`, which is
  excluded from the build).
- No references to legacy `images/*.gif` or `images/*.png` files (only the
  CC license badge URL in `intro.md`).
- No indented/broken `{admonition}` blocks remain.
- No technology-specific references (Minitab, StatCrunch, Excel, TI, R
  instructions, applets) remain; outputs were converted to generic tables.
- All figure references resolve to SVGs in `pages/images/gen/` (~170 files).
- Numeric corrections made along the way, most recently: m14 CI for p
  example 1 (0.123, 0.197); m17 9/11 responder table reconciled to
  793/1102/1234/1653.

Remaining for the user: run `myst build` (or `myst start`) to confirm the
book builds cleanly — the sandbox here could not run the build.

## Structure change (post-verification)

Per instructor request, the old Sections 1 (Introduction, m01) and
2 (Learning Strategies, m02) were removed from the book:

- `toc.yml`: the book now opens with "The Big Picture" (m03) as a top-level
  entry, followed by Unit 1 EDA (Sections 1-2), Unit 2 Producing Data
  (Sections 3-4), Unit 3 Probability (Sections 5-9), and Unit 4 Inference
  (Sections 10-14).
- `myst.yml`: `pages/*m01*.md`, `pages/*m02*.md`, and `pages/unused/*.md`
  added to the exclude list (files left on disk but not built).
- `pages/009-m03-the-big-picture.md` and
  `pages/images/gen/m03-big-picture-units.svg` updated to the new unit
  numbering (EDA = Unit 1, Producing Data = Unit 2, Probability = Unit 3,
  Inference = Unit 4).

## Unit order swap: Producing Data before EDA

Per instructor request, Producing Data is now Unit 1 (Sections 1-2) and EDA
is Unit 2 (Sections 3-4). The order is encoded in exactly these places, each
marked with a "UNIT ORDER" comment containing the alternative wording, so
switching back is a matter of swapping the toc blocks and following the
comments:

- `toc.yml` — unit blocks and section numbers (revert instructions in the
  header comment).
- `pages/images/gen/m03-big-picture-units.svg` — Unit 1/Unit 2 labels.
- `pages/009-m03-the-big-picture.md` — "Book Structure" sentence + figure
  alt text.
- `pages/010-m04-exploratory-data-analysis-1-of-2.md` — opening transition
  sentence.
- `pages/067-m06-introduction-to-producing-data.md` — opening transition
  sentence.
- `pages/089-m08-probability.md` — removed the EDA-first parenthetical
  (kept in a comment).

In addition, `pages/074-m07-introduction.md` and
`pages/086-m07-wrap-up-designing-studies.md` were reworded to be
order-neutral (they refer to the EDA unit without implying it came before
or after), so they need no changes if the order is swapped again.

## Descriptive page titles + editorial review (July 2026)

- Descriptive H1 titles: every built page (m03-m17) now has a descriptive
  title instead of the OLI "Topic (n of m)" boilerplate. The only pages still
  using numbered titles are the two excluded m02 pages (`006`, `007`).
- Editorial review recorded in `BOOK_REVIEW.md`. Fixes applied from it:
  `intro.md` polished (US "License", unwrapped prose, trailing spaces removed);
  the lone `## Example` H2 (page `011`) converted to the admonition tip form and
  "Example #1/#2" numbering fixed on page `165`; the z-table leading-zero
  convention documented as a deliberate exception in `STYLE_GUIDE.md`.
- "Comment" sections standardized: short caveats are now `:class: important`
  admonitions and subtopic "Comment" headings were renamed to descriptive
  section titles (rule recorded in `STYLE_GUIDE.md`).
- Quiz-section headings standardized: every quiz section now uses
  `## Check Your Understanding: <topic>` (replacing the generic "Concept
  Check" / "Did I Get This?" / "Learn By Doing" labels). Rule recorded in
  `STYLE_GUIDE.md`. All seven review findings are now complete.

## Notes / open questions

- `pages/unused/003-m01-pre-course-survey.md` left unused.
- OLI scrape gaps (`oli_content/oli_pages/undefined_*.html`) were interactive
  activities (StatTutor, simulations); per decision they are removed, not recreated.
