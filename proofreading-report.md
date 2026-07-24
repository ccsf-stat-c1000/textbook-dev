# Proofreading Checklist — STAT C1000 Textbook

Scope: all 249 content pages in `pages/` plus the glossary, checked for spelling/grammar, math and statistical accuracy, formatting/markup, and consistency (math verified computation by computation). The book is in excellent shape — every worked calculation and quiz answer checked out. Every item below is minor. Tags: **[Math]** · **[Grammar]** · **[Format]** · **[Consistency]**.

## Priority fixes (reader-visible)

- [x] **084** — `a*closed question` renders run-together; make it `a *closed question*`. **[Grammar]**
- [x] **085** — `surveythat` → `survey that`; `statements.Respondents` → `statements. Respondents`. **[Grammar]**
- [x] **085** — `Asample surveyis` → `A sample survey is`. **[Grammar]**
- [ ] **139** — quiz feedback says σ(Y) ≈ 0.9; change to ≈ 0.85 to match page 140 and the true value (√0.71 ≈ 0.84). **[Math]**

## Front matter + m03

- [ ] **overview.md, Week 2** — "sampling bias (voluntary, convenience)" in the learning objective vs "selection bias" in the instructor text above it; use one term (recommend "selection bias"). **[Consistency]**

## m06 (Sampling)

- [ ] **070** — "Each of those probability sampling plans … **are** not subject to any bias" → "**is** not subject." **[Grammar]**

## m07 (Designing Studies)

- [ ] **073** — stray space after em-dash: "data production**— **sampling—we" → "production—sampling—we." **[Format]**
- [ ] **081** — both "noncompliance" and "non-compliance" appear (same paragraph); standardize on "noncompliance." **[Consistency]**
- [ ] **084** — "a flawed designs such as" → "a flawed design such as" (or "flawed designs such as"). **[Grammar]**

## m04 (Distributions)

- [ ] **020** — "real-life variable" vs "real life variable" on the same page; hyphenate consistently. **[Consistency]**

## m11 (Random Variables / Normal)

- [ ] **152** — filename `...-normal-random-variables2-of-3.md` is missing the hyphen before "2" (siblings 151/153 have it); rename to `...-normal-random-variables-2-of-3.md`. Build not affected. **[Format]**

## Glossary

- [ ] **glossary.md** — entry titled "chi-square test **of** independence" vs prose "chi-square test **for** independence" (m17); match them (prose "for" is the more common convention). Nothing breaks; no `{term}` link points to it. **[Consistency]**

---

## Verified clean (no action needed)

- Front matter (`intro.md`, `overview.md`, `002`, `009-m03`), aside from the item above.
- **m04** — exam-grades histogram, Best Actress stemplot/split-stem/dotplot, all frequency counts and medians.
- **m05, m08–m11** — all worked math (SD, empirical rule, probability rules, Bayes/trees, random variables, binomial, normal table, continuity correction).
- **m12–m13** — sampling distributions (σ_p̂, σ/√n, z-scores, CLT).
- **m14** — confidence intervals, margins of error, sample-size calculations (means and proportions).
- **m15** — every z-test, t-test, test statistic, p-value, CI-vs-test example, Type I/II error material.
- **m16** — two-sample t (t = −4.66, 5.31, −2.02), paired t (t = −2.58), ANOVA.
- **m17** — two-way tables, expected counts, chi-square (1.62; 4.91 tripled), regression predictions.
- **Glossary** — thorough and accurate; all `{term}` references resolve.
