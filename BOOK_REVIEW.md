# STAT C1000 Textbook — Editorial Review

Review date: 2026-07-16 (updated after applying findings 1 and 4–7 and starting finding 3)
Scope: all built content in `pages/` (m03 through m17, plus `intro.md`). Excluded from the build, and therefore from this review's priorities: `pages/*m01*`, `pages/*m02*`, and `pages/unused/*`.
Basis: checked against `STYLE_GUIDE.md` and `PROGRESS.md`.

This document tracks the review findings and their status. Findings 1 and 4–7 have been applied, finding 3 is in progress, and finding 2 is deferred at your request. Each item lists what was found, the evidence, and the change made or proposed.

## Summary

| # | Finding | Priority | Scope |
| --- | --- | --- | --- |
| 1 | Descriptive-title conversion | Resolved | m12–m17 converted (80 pages) |
| 2 | Quiz-section headings inconsistent ("Concept Check" vs "Did I Get This?"/"Learn By Doing") | Deferred (by request) | ~83 pages |
| 3 | "Comment" appears both as an H2 and as an admonition | In progress | ~60 pages; m04 done |
| 4 | "Example" H2 vs admonition; "#" numbering | Resolved | pages 011, 165 |
| 5 | `intro.md`: British "Licence", hard-wrapping, trailing spaces | Resolved | 1 page |
| 6 | Standard normal table omits leading zeros | Resolved (documented exception) | style guide |
| 7 | `PROGRESS.md` is partly stale | Resolved | docs only |

The good news up front: the technology-neutrality goal is fully met, there are no leftover raster images, no empty headings, and the pages sampled in depth are pedagogically strong and cleanly formatted. Details in "What is clean" below.

---

## High priority

### 1. Descriptive-title conversion — RESOLVED

Previously the book was split in two: m03–m11 had descriptive titles while m12–m17 still carried OLI boilerplate of the form "Topic (n of m)". The conversion has now been completed for all 80 remaining built pages (m12–m17), matching the voice used in m03–m11. Only the H1 line was changed on each page; page content is untouched. Nothing is committed, so the diff is easy to review.

The only pages that still use "(n of m)" titles are the two m02 pages (`006`, `007`), which are excluded from the build via `myst.yml` and so do not appear in the book. Convert them too if you ever re-enable m02; otherwise they can stay as is.

The new titles, by module:

m12 Sampling Distributions

- 166 → The Sample Proportion: Center, Spread, and Shape
- 167 → The Sampling Distribution of the Sample Proportion
- 168 → Finding Probabilities for a Sample Proportion
- 169 → The Sample Mean: Center, Spread, and Shape
- 170 → The Central Limit Theorem
- 171 → Applying the Central Limit Theorem

m13 Introduction to Inference

- 176 → From Sample to Population: The Idea of Inference
- 177 → Three Forms of Statistical Inference

m14 Estimation

- 180 → Point Estimation: Estimating with a Single Number
- 181 → What Makes a Good Point Estimator?
- 183 → Confidence Intervals for a Mean: An Overview
- 184 → Building the 95% Confidence Interval for a Mean
- 185 → Confidence Intervals at Other Levels of Confidence
- 186 → The Structure of a Confidence Interval
- 187 → Margin of Error and the Precision of an Interval
- 188 → Choosing a Sample Size for a Desired Margin of Error
- 189 → When Is It Safe to Use This Interval?
- 190 → Confidence Intervals for a Mean: Summary
- 191 → Confidence Intervals for a Proportion: An Overview
- 192 → Constructing a Confidence Interval for a Proportion
- 193 → Choosing a Sample Size for Estimating a Proportion
- 194 → Confidence Intervals for a Proportion: Conditions and Summary

m15 Hypothesis Testing

- 197 → The Logic of Hypothesis Testing
- 198 → The Four Steps of a Hypothesis Test
- 199 → Null and Alternative Hypotheses
- 200 → Significance Level and Drawing Conclusions
- 202 → The z-Test for a Proportion: Overview
- 203 → Step 1: Stating the Hypotheses for a Proportion
- 204 → Step 2: Collecting and Summarizing the Data
- 205 → The Test Statistic for a Proportion
- 206 → Conditions for the z-Test for a Proportion
- 207 → Step 3: Finding the P-value for a Proportion
- 208 → Computing P-values: Worked Examples
- 209 → Step 4: Drawing Conclusions from the P-value
- 210 → The z-Test for a Proportion: Summary
- 211 → The Effect of Sample Size on Testing
- 212 → One-Sided vs. Two-Sided Alternatives
- 213 → Hypothesis Tests and Confidence Intervals for a Proportion
- 214 → Following a Test with a Confidence Interval
- 215 → The z-Test for a Mean: Overview
- 216 → Stating Hypotheses and Summarizing Data for a Mean
- 217 → Step 3: Finding the P-value for a Mean
- 218 → Step 4: Drawing Conclusions for a Mean
- 219 → Tests and Confidence Intervals for a Mean
- 220 → When σ Is Unknown: The t-Test and t Distribution
- 221 → The t-Test Statistic
- 222 → Finding the P-value with the t Distribution
- 223 → The t-Test for a Mean: Worked Examples

m16 Inference for Relationships

- 229 → Case C→Q: Comparing Groups
- 230 → Independent Samples vs. Matched Pairs
- 231 → Comparing Two Means from Independent Samples
- 232 → The Two-Sample t-Test: Stating the Hypotheses
- 233 → The Two-Sample t-Test: Conditions and Test Statistic
- 234 → The Two-Sample t-Test: P-value and Conclusion
- 235 → The Two-Sample t-Test: A Worked Example
- 236 → A Confidence Interval for the Difference of Two Means
- 237 → Connecting the Interval and the Test
- 238 → Comparing Two Means from Paired Data
- 239 → The Idea Behind the Paired t-Test
- 240 → The Paired t-Test: Stating the Hypotheses
- 241 → The Paired t-Test: Conditions and Test Statistic
- 242 → The Paired t-Test: P-value and Conclusion
- 243 → The Paired t-Test: Worked Examples
- 244 → A Confidence Interval for the Mean Difference
- 245 → The Paired t-Test: Summary
- 246 → Comparing More Than Two Means: ANOVA
- 247 → The ANOVA F-Test: Stating the Hypotheses
- 248 → The Idea Behind the ANOVA F-Test
- 249 → The F-Statistic: Conditions and Computation
- 250 → The ANOVA F-Test: P-value and Conclusion
- 251 → The ANOVA F-Test: A Worked Example
- 252 → After ANOVA: Which Means Differ?

m17 Inference for Relationships (continued)

- 255 → Case C→C: Relationships Between Categorical Variables
- 256 → The Chi-Square Test: Hypotheses and the Big Idea
- 257 → The Chi-Square Statistic: Conditions and Computation
- 258 → The Chi-Square Test: P-value and Conclusion
- 259 → The Chi-Square Test: Summary
- 260 → Case Q→Q: Inference for a Linear Relationship
- 261 → Testing for a Linear Relationship
- 262 → Estimating the Regression Line

A note on the repeated "Step 3 / Step 4" phrasing: the proportion and mean test sequences both walk the same four steps, so a few titles share wording (disambiguated by "for a Proportion" / "for a Mean"). This mirrors the parallel structure of the underlying content and reads clearly in the sidebar under each section heading.

### 2. Quiz sections are labeled three different ways — DEFERRED (by request)

You asked to skip this one for now. Summary retained for reference: `STYLE_GUIDE.md` specifies "## Concept Check" as the heading that precedes a run of quizzes. In practice the book uses three labels:

- "## Concept Check" — used on 89 pages (the intended convention)
- "## Did I Get This?" — retained OLI label
- "## Learn By Doing" — retained OLI label

The two OLI labels remain on 83 pages (116 occurrences total). The quizzes underneath them are authored correctly; only the heading was left as OLI named it. A related wrinkle: some pages stack the same OLI heading two or three times (for example, `208-m15-...-p-7.md` has three consecutive "## Learn By Doing" sections, each with its own quiz).

Proposed change: rename every "## Did I Get This?" and "## Learn By Doing" to "## Concept Check" for consistency with the style guide. Where a single page then has multiple identical "## Concept Check" headings in a row, either merge the quizzes under one heading or leave the first heading and drop the repeats, so a page does not repeat the same H2. This is a low-risk find-and-replace plus a light manual pass for the stacked cases.

---

## Medium priority

### 3. "Comment" is presented two ways — IN PROGRESS

The style guide says comments and caveats should use the `:class: important` admonition. The book was split: ~60 pages used a plain `## Comment(s)` H2 (about 90 occurrences, mostly earlier modules), while ~30 pages already used the admonition box (mostly m15–m17). You chose to standardize on callout boxes everywhere.

Status: I'm converting each `## Comment(s)` H2 section into a `:class: important` admonition, preserving the exact heading text as the box title. To match existing usage I use a backtick ```` ```{admonition} ```` fence for plain-prose comments and a `:::`/`::::` colon fence where the body contains a table or figure. Module 4 is done (pages 016, 019, 022, 027, 028); m05–m17 remain.

Two things to review after your next build:

- A few "## Comments" sections (for example, page 016) are a page's entire body rather than a short aside, so they become large boxes. They are converted for consistency, but you may prefer to rename them to a normal section heading instead.
- I can't run a MyST build here, so when the pass is complete I verify with grep that no `## Comment` headings remain and that admonition fences are balanced; a build is still the definitive check.

### 4. "Example" formatting and numbering — RESOLVED

Examples were already near-uniform: only the reference page `011` used an `## Example` H2, and everywhere else uses the `:class: tip` admonition. That one heading was converted to the admonition form, and the "Example #1/#2" numbering on page `165` was changed to "Example 1/2".

---

## Low priority

### 5. `intro.md` polish — RESOLVED

`intro.md` was rewritten: the "## Licence" heading is now US-spelling "## License", the hard-wrapped prose is unwrapped to one paragraph per line, and trailing whitespace was removed.

### 6. Standard normal table leading zeros — RESOLVED (documented exception)

The z-table pages (`154`, `155`, `156`) omit leading zeros (.0122, .05), which is the universal printed-table convention. Rather than change the tables, `STYLE_GUIDE.md` now records this as a deliberate exception to the leading-zero rule.

### 7. `PROGRESS.md` refreshed — RESOLVED

`PROGRESS.md` now records the descriptive-title conversion and the review-driven fixes, and the obsolete `notebook06.ipynb` note (no longer referenced by `toc.yml`) was removed.

---

## What is clean (verified)

These were checked across the whole book and look good:

- Technology neutrality: no references to Excel, Minitab, StatCrunch, TI calculators, R, Desmos, or OLI applets remain. Software is referred to generically ("statistical software or a calculator").
- Images: no legacy `.gif`/`.png`/`.jpg` references except the Creative Commons badge in `intro.md`. All figures are SVGs.
- Figure paths: every figure directive points into `images/gen/` (no stray paths). A spot check of all m11 figures confirmed the files exist. See the build note below for definitive verification.
- Headings: no empty headings anywhere.
- Quizzes: sampled quizzes consistently include a `:hint:` and either per-choice `:feedback-N:` or an `:explanation:`, with teaching feedback for wrong answers, as the guide requires.
- Decimals: leading zeros are used correctly everywhere except the z-table (finding 6).
- Admonitions: in the pages read in depth, colon fences are flush-left and nested correctly (no accidental code-block indentation).
- Prose and pedagogy: the pages sampled (`011`, `165`, `208`, plus the m11 module) are accurate, well sequenced, and keep the OLI four-step and role-type framing intact.

## Needs a build to confirm

The sandbox cannot run `myst build`, and a few things can only be verified by building. `PROGRESS.md` already lists the build as the remaining user step. Specifically:

- That all ~170 figure references resolve to existing SVGs (paths are correct; a build confirms nothing is missing or misnamed).
- That the quiz plugin (`pages/quiz.mjs`) renders every `{quiz}` / `{quiz-multi}` directive without error.
- That no MyST directive warnings surface from the pages.

## Status of work

1. Title conversion (finding 1): done (m12–m17).
2. Quiz headings (finding 2): deferred at your request.
3. Comment → callout boxes (finding 3): in progress (m04 done; m05–m17 remaining).
4. Examples + page-165 numbering (finding 4): done.
5. `intro.md` polish (finding 5) and `PROGRESS.md` refresh (finding 7): done.
6. z-table exception (finding 6): documented in the style guide.

Remaining: finish the finding 3 conversion through m05–m17, then run `myst build` to confirm the new comment boxes, all figures, and the quiz plugin render cleanly.
