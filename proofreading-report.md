# Proofreading Report — STAT C1000 Textbook

Scope: all 249 content pages in `pages/` plus the glossary, checked for spelling/grammar, math and statistical accuracy, formatting/markup, and consistency. Math was verified computation by computation.

Bottom line: the book is in excellent shape. Across hundreds of worked calculations and quiz answers, every numerical result was correct. The items below are the full list of issues found — all minor. Severity tags: **[Math]** calculation/definition, **[Grammar]** spelling/grammar/punctuation, **[Format]** markup/link/filename, **[Consistency]** terminology/notation/style.

### Fix these first (reader-visible)

<!-- 1. **084** — `a*closed question` renders run-together (missing space). **[Grammar]**
2. **085** — `surveythat`, `statements.Respondents`, and `Asample surveyis` all render run-together (missing spaces). **[Grammar]**
3. **139** — quiz feedback says σ(Y) ≈ 0.9, but the correct value (and page 140) is 0.85. **[Math]** -->

Everything else is a small grammar/consistency/filename nit, listed by page below.

---

## Front matter + m03 (intro, welcome, big picture)

- **overview.md, Week 2 — [Consistency]** The instructor text calls it "selection bias (voluntary response, convenience) and non-selection bias," but the matching learning objective on the same page calls it "sampling bias (voluntary, convenience)." Use one term (recommend "selection bias") consistently.
- Otherwise front matter (`intro.md`, `overview.md`, `002-m01-welcome.md`, `009-m03-the-big-picture.md`) reads cleanly.

## m06 (Sampling)

- **070-m06-sampling-1-of-2.md — [Grammar]** "Each of those probability sampling plans, if applied correctly, **are** not subject to any bias" — subject "Each" is singular, so it should be "**is** not subject to any bias."

## m07 (Designing Studies)

- **073-m07-designing-studies.md — [Format]** Inconsistent em-dash spacing: "first stage of data production**— **sampling—we can move on" has a stray space after the first em-dash. Elsewhere the book sets em-dashes closed (no surrounding spaces); make it "production—sampling—we."
- **081-m07-causation-and-experiments-3-of-3.md — [Consistency]** Both spellings appear, once in the same paragraph: "problem of **noncompliance**" and "the more worrisome problem of **non-compliance**" (and "**non-compliance**" again in the same sentence). Pick one form (the glossary/most pages use "noncompliance").
- **084-m07-sample-surveys-1-of-2.md — [Grammar]** "avoids the bias that might result from **a flawed designs** such as a convenience sample" — number disagreement. Use "a flawed design such as…" or "flawed designs such as…".
- **084-m07-sample-surveys-1-of-2.md — [Grammar]** Missing space: "Responses are much easier to handle if they come from **a\*closed question:\***" — should be "a *closed question:*".
- **085-m07-sample-surveys-2-of-2.md — [Grammar]** Two missing spaces in one sentence: "Defenders of the club created a **surveythat** included the following **statements.Respondents** were supposed to indicate…" — should be "a survey that included the following statements. Respondents were…".
- **085-m07-sample-surveys-2-of-2.md — [Grammar]** Missing spaces in the summary opener: "**Asample surveyis** a type of observational study" — should be "A sample survey is a type of observational study."

## m04 (Distributions)

- **020-m04-histogram-2-of-3.md — [Consistency]** "real-life variable" (skewed-right paragraph) vs "real life variable" (skewed-left paragraph) on the same page — hyphenate consistently ("real-life" as an adjective).
- Verified: the exam-grades histogram counts, the Best Actress stemplot/split-stem/dotplot, and all histogram frequency counts and medians are internally consistent and correct.

## m11 (Random Variables / Normal) — file naming

- **152-m11-introduction-to-normal-random-variables2-of-3.md — [Format/Consistency]** The filename is missing the hyphen before "2": its siblings are `...-normal-random-variables-1-of-3.md` (151) and `...-normal-random-variables-3-of-3.md` (153), but this one is `...-normal-random-variables2-of-3.md`. Doesn't break the build (the TOC globs `*m11*`), but rename for consistency.
- **139-m11-mean-and-variance-of-a-random-variable-4-of-5.md — [Math/Consistency]** A quiz feedback says of Yves' line, "In fact σ(Y) ≈ 0.9." The next page (140) states σ_Y = 0.85, and the actual value is √0.71 ≈ 0.84. Change the 139 approximation to ≈ 0.85 (or ≈ 0.8) so it matches page 140 and the true value.

## m12–m13 (Sampling distributions, inference intro)

- Clean. Every sampling-distribution computation (σ_p̂, σ/√n, all z-scores and probabilities, CLT examples) verifies.

## m14 (Estimation)

- Clean. All confidence intervals, margins of error, and sample-size calculations (means and proportions) verify.

## m15 (Hypothesis testing)

- Clean. Every z-test, t-test, test statistic, p-value, CI-vs-test example, and the Type I/II error material verifies.

## m16 (Inference for relationships: two means, ANOVA)

- Clean. Two-sample t (t = −4.66, 5.31, −2.02), paired t (t = −2.58), and ANOVA (F, SD-ratio checks) all verify.

## m17 (Chi-square, regression inference)

- Clean. All two-way tables, expected counts, chi-square statistics (1.62; 4.91 for the tripled sample), and regression predictions verify.

## Glossary

- **glossary.md — [Consistency]** The entry is titled "chi-square test **of** independence," but the prose in m17 (pages 255–259, 263) consistently calls it the "chi-square test **for** independence." No `{term}` link points to it, so nothing breaks, but the two spellings should match (the prose form "for independence" is the more common convention). Otherwise the glossary is thorough, accurate, and consistent with the text's `{term}` references (all resolve).

---

## Overall assessment

I read all 249 content pages plus the glossary and verified the mathematics throughout — hundreds of calculations across descriptive statistics, probability, random variables, the normal table, sampling distributions, confidence intervals, and every hypothesis test (z, t, paired t, two-sample t, ANOVA, chi-square, regression). **Every computed result, quiz answer, and feedback value checked out.** The issues above are the complete list, and all are minor: a handful of typos/missing spaces (concentrated in the m07 survey pages), a few terminology/hyphenation inconsistencies, one filename, and one quiz-feedback rounding (σ_Y). Nothing affects the correctness of the statistical content.

Highest-priority fixes: the four missing-space errors on pages **084** and **085** (they will render as run-together words in the published book), and the **σ_Y ≈ 0.9** inconsistency on page **139**.
