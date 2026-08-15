# STAT C1000 Course Outline Alignment and Pacing Guide

This document maps the content of *Introduction to Statistics* (this Jupyter Book) to the
STAT C1000 Course Outline of Record, and provides pacing schedules for 17.5-week,
16-week, and 12-week terms.

**Verdict: the book aligns with the Course Outline of Record.** All fourteen Part I content
items are covered, and all six course objectives (SLO A–F) are supported by book content.
Two gaps are documented in the [Gaps and Notes](#gaps-and-notes) section: technology-based
statistical analysis (COR Part I item 2 and Part II) is not built into the book and must be
supplied by the instructor, and ethical reasoning (SLO F) is present but thin.

## Sourcing note

CCSF's Course Outline of Record for STAT C1000 lives in CurricUNET
([report link](https://ccsf.curricunet.com/DynamicReports/AllFieldsReportByEntity/14744?entityType=Course&reportId=28)),
which could not be fetched programmatically for this review. The six Student Learning
Outcomes quoted below are taken verbatim from `overview.md` in this repository, which cites
the CCSF COR directly. The Part I / Part II content outline is taken from the Common Course
Numbering STAT C1000 template, which CCSF's COR follows; the SLO wording in `overview.md`
matches the CCN "Course Objectives" list word for word, which is strong evidence the content
outline matches as well. **Before submitting this document to a curriculum committee, verify
the Part I content list against the live CCSF CurricUNET report.**

---

## Part 1: Objective (SLO) Alignment

| SLO | Objective | Where the book covers it |
|---|---|---|
| **A** | Assess how data were collected and recognize how data collection affects what conclusions can be drawn. | Unit 1 entirely. §1 Sampling (pp. 67–71); §2 Designing Studies (pp. 73–87), including observational vs. experimental design, causation, confounding, blinding, blocking, and sample surveys. Reinforced in Unit 2 §4 (Causation and Lurking Variables, pp. 60–64). |
| **B** | Identify appropriate graphs and summary statistics for variables and relationships, and interpret them correctly. | Unit 2 entirely. §3 Examining Distributions (pp. 10–37): categorical/quantitative variables, histograms, stemplots, boxplots, center, spread, standard deviation. §4 Examining Relationships (pp. 39–66): role-type classification, side-by-side comparisons, two-way tables, scatterplots, correlation, least-squares regression. |
| **C** | Describe and apply probability concepts and distributions. | Unit 3 entirely. §5 Introduction (pp. 89–96); §6 Finding Probability of Events (pp. 98–114); §7 Conditional Probability and Independence (pp. 116–126); §8 Random Variables (pp. 128–162), covering discrete distributions, expected value and variance, the binomial distribution, continuous distributions, the normal distribution, and the normal approximation to the binomial; §9 Sampling Distributions (pp. 164–173). |
| **D** | Use the basic ideas of statistical processes, including hypothesis tests and confidence interval estimation. | Unit 4 entirely. §10 Introduction to Inference (pp. 174–178); §11 Estimation (pp. 180–194); §12 Hypothesis Testing (pp. 196–226); §13–14 Inference for Relationships (pp. 228–264). |
| **E** | Identify appropriate statistical techniques and use technology-based statistical analysis to describe, interpret, and communicate results. | **Partially covered.** Technique selection is directly supported by the role-type classification framework (pp. 40–41, 228, 255, 260) and by the Summary pages (pp. 66, 173, 264), which is unusually strong scaffolding for procedure identification. Technology-based analysis is **not** built into the book; see Gaps. |
| **F** | Evaluate ethical issues in statistical practice. | **Thinly covered.** Present in Sampling (p. 69), Causation and Experiments (pp. 79, 81), Wrap-Up Designing Studies (p. 86), and Matched Pairs (p. 243). Threaded rather than taught as a unit; see Gaps. |

---

## Part 2: Content Outline Alignment

COR Part I content items, mapped to book units, sections, and pages.

| # | COR Part I content item | Book coverage | Status |
|---|---|---|---|
| 1 | Introduction to statistical thinking and processes | Intro page; The Big Picture (p. 9) | Covered |
| 2 | Technology-based statistical analysis | Not built into the book | **Gap — instructor supplies** |
| 3 | Applications using data from four or more disciplines | Examples throughout draw on health science, life science, education, psychology, social science, and business | Covered |
| 4 | Units (subjects/cases) and variables in a data set, including multivariable data sets | EDA introduction (pp. 10–11); role-type classification (pp. 40–41); labeled scatterplots with a third variable (p. 51) | Covered |
| 5 | Categorical and quantitative variables | pp. 10–11, 13–17, 40–41 | Covered |
| 6 | Sampling methods, concerns, and limitations, including bias and random variability | Unit 1 §1 (pp. 67–71); Sample Surveys (pp. 84–85) | Covered |
| 7 | Observational studies and experiments | Unit 1 §2 (pp. 73–87) | Covered |
| 8 | Data summaries, visualizations, and descriptive statistics | Unit 2 §3–§4 (pp. 10–66) | Covered |
| 9 | Probability concepts | Unit 3 §5–§7 (pp. 89–126) | Covered |
| 10 | Probability distributions (e.g., binomial, normal) | Binomial (pp. 144–147); normal (pp. 151–158); normal approximation to the binomial (pp. 159–161) | Covered |
| 11 | Sampling distributions and the Central Limit Theorem | Unit 3 §9 (pp. 164–173) | Covered |
| 12 | Estimation and confidence intervals | Unit 4 §11 (pp. 180–194): point estimation, interval estimation, CIs for μ and for p | Covered |
| 13 | Hypothesis testing, including t-tests for one and two populations, chi-squared test(s), and ANOVA | One-sample tests for p and μ (pp. 196–226); two independent samples and matched pairs (pp. 228–245); ANOVA (pp. 246–252); chi-square test of independence, Case C→C (pp. 255–259) | Covered |
| 14 | Regression, including correlation and linear regression equations | Descriptive: scatterplots, correlation, least-squares regression (pp. 47–59). Inferential: Case Q→Q (pp. 260–262) | Covered |
| Part II | Analysis of large data sets using statistical software | Not built into the book | **Gap — instructor supplies** |

### Notable strengths relative to the COR

- **Binomial random variables and ANOVA are both present** (pp. 144–147 and 246–252).
  The COR's textbook rationale for stock OLI *Concepts in Statistics* states that
  "instructor must supplement instruction for Binomial Random Variables and ANOVA not
  contained in the text." This book already includes both, so that supplementation
  requirement is satisfied by the book itself.
- **Chi-square is present** as Case C→C (pp. 255–259), satisfying the COR's chi-squared
  requirement without supplementation.
- **The role-type classification framework** (C→Q, C→C, Q→Q) runs from Unit 2 through
  Unit 4 and gives students an explicit decision procedure for choosing a statistical
  technique. This directly serves SLO E, which is typically the hardest outcome to assess.

### Stale note in `overview.md`

`overview.md`, Week 16, states: *"The Course Outline lists chi-squared tests as required
content (SLO D). If time permits, introduce chi-squared tests..."* and the Notes section
repeats that "the handouts do not include it." This is no longer accurate for the book:
chi-square is fully developed at pp. 255–259 as a required part of Unit 4 §13. That note
should be updated.

---

## Gaps and Notes

### Gap 1: Technology-based statistical analysis (COR Part I item 2, Part II, SLO E)

The COR requires a statistical analysis platform beyond a graphing calculator (R,
StatCrunch, or Excel) and requires analysis of large data sets using that software.
The book mentions software on only a handful of pages (85, 161, 243). Computation in the
book is presented conceptually and by hand or table.

**Recommended remedy.** Adopt one platform and attach a lab or activity stream in parallel
with the reading. Natural attachment points:

| Book location | Lab topic |
|---|---|
| pp. 24–36 | Measures of center and variation; effect of outliers |
| pp. 47–59 | Scatterplots, correlation, least-squares regression |
| pp. 151–158 | Normal probabilities and inverse normal |
| pp. 164–173 | Sampling distribution simulation, CLT |
| pp. 183–194 | Confidence intervals |
| pp. 202–226 | One-sample hypothesis tests |
| pp. 231–252 | Two-sample tests and ANOVA |
| pp. 255–262 | Chi-square and regression inference |

This also satisfies the COR's Methods of Instruction requirement for Activity and Lab hours
(the COR allocates 36 activity hours alongside 36 lecture hours).

### Gap 2: Ethical reasoning (SLO F)

Ethics appears on six pages, mostly within Unit 1. SLO F asks students to *evaluate* ethical
issues, which implies assessable work. Recommended additions, none requiring new book content:

- Unit 1: a written analysis of a study whose sampling design undermines its published claim.
- p. 125 (probability trees) or pp. 123–125: false positives and false negatives in medical
  screening, and the decision consequences of each.
- pp. 224–226: p-value misinterpretation and the gap between statistical and practical
  significance.
- p. 264 (Summary of Inference): a capstone reflection on responsible statistical
  communication.

### Sequencing note

The book covers **confidence intervals for the mean (pp. 183–190) before confidence
intervals for the proportion (pp. 191–194)**. `overview.md`'s weekly plan does the reverse.
Either order works; pick one and make the syllabus consistent with it. The schedules below
follow the book's order.

---

## Part 3: Pacing Schedules

All three schedules follow the book's table of contents order:
Big Picture → Unit 1 Producing Data → Unit 2 Exploratory Data Analysis →
Unit 3 Probability → Unit 4 Inference.

Page numbers refer to the flat page numbers encoded in the `pages/` filenames
(e.g. `p164-m12-sampling-distributions.md` is page 164), which is the numbering students
see in the sidebar.

Content page totals by module:

| Section | Pages | Count |
|---|---|---|
| Intro + The Big Picture | intro, 9 | 2 |
| §1 Sampling | 67–71 | 4 |
| §2 Designing Studies | 73–87 | 15 |
| §3 Examining Distributions | 10–37 | 27 |
| §4 Examining Relationships | 39–66 | 28 |
| §5 Introduction (Probability) | 89–96 | 8 |
| §6 Finding Probability of Events | 98–114 | 17 |
| §7 Conditional Probability and Independence | 116–126 | 11 |
| §8 Random Variables | 128–162 | 34 |
| §9 Sampling Distributions | 164–173 | 10 |
| §10 Introduction to Inference | 174–178 | 4 |
| §11 Estimation | 180–194 | 15 |
| §12 Hypothesis Testing | 196–226 | 30 |
| §13 Inference for Relationships | 228–253 | 26 |
| §14 Inference for Relationships, cont. | 255–264 | 10 |
| **Total** | | **241** |

---

### Schedule A: 17.5-Week Term (standard fall/spring semester)

Assumes two meetings per week, three midterms, and a cumulative final in finals week.
Average load: roughly 15 pages per week.

| Week | Book pages | Topics | Assessment |
|---|---|---|---|
| 1 | intro, 9, 67–71 | Course orientation; the Big Picture; sampling, bias, random variability | |
| 2 | 73–87 | Designing studies: observational vs. experimental, causation, confounding, blinding, blocking, sample surveys | |
| 3 | 10–23 | EDA framework; categorical variables; one quantitative variable; histograms, stemplots | |
| 4 | 24–37 | Measures of center; measures of spread; boxplots; standard deviation; wrap-up distributions | |
| 5 | 39–51 | Role-type classification; Case C→Q; Case C→C (two-way tables); scatterplots | **Exam 1** (Unit 1 + §3) |
| 6 | 52–66 | Linear relationships, correlation, least-squares regression; causation and lurking variables; EDA summary | |
| 7 | 89–113 | Introduction to probability; relative frequency; sample spaces and events; equally likely outcomes; probability rules | |
| 8 | 114, 116–126 | Conditional probability; independence; general multiplication rule; probability trees | |
| 9 | 128–143 | Random variables; discrete probability distributions; mean and variance; rules for means and variances | |
| 10 | 144–162 | Binomial random variables; continuous random variables; the normal distribution; standard normal table; normal approximation to the binomial | **Exam 2** (Unit 2 + §5–§8) |
| 11 | 164–178 | Parameters vs. statistics; behavior of sample proportion and sample mean; the CLT; three forms of inference | |
| 12 | 180–194 | Point estimation; interval estimation; confidence intervals for μ; confidence intervals for p | |
| 13 | 196–214 | Hypothesis testing overview; the four-step process; hypothesis testing for p | |
| 14 | 215–226 | Hypothesis testing for μ; Type I and Type II errors | |
| 15 | 228–245 | Inference for relationships: Case C→Q; two independent samples; matched pairs | **Exam 3** (§9–§12) |
| 16 | 246–259 | ANOVA; Case C→C (chi-square test of independence) | |
| 17 | 260–264 | Case Q→Q (inference for regression); wrap-up; summary of inference; cumulative review | |
| 17.5 | — | Finals week | **Cumulative Final** |

---

### Schedule B: 16-Week Term

Same content, compressed by folding Exam 1 into Week 4, merging the Unit 2 relationships
material into fewer weeks, and moving the cumulative review into Week 16. No COR-required
topic is dropped. Average load: roughly 16 pages per week.

| Week | Book pages | Topics | Assessment |
|---|---|---|---|
| 1 | intro, 9, 67–71 | Big Picture; sampling, bias, random variability | |
| 2 | 73–87 | Designing studies; causation; sample surveys | |
| 3 | 10–23 | EDA framework; categorical and quantitative variables; histograms, stemplots | |
| 4 | 24–37 | Center, spread, boxplots, standard deviation | **Exam 1** (Unit 1 + §3) |
| 5 | 39–59 | Role-type classification; Cases C→Q and C→C; scatterplots; linear relationships and regression | |
| 6 | 60–66, 89–96 | Causation and lurking variables; EDA summary; introduction to probability; relative frequency | |
| 7 | 98–113 | Sample spaces and events; equally likely outcomes; probability rules | |
| 8 | 114, 116–126 | Conditional probability; independence; multiplication rule; probability trees | |
| 9 | 128–147 | Random variables; probability distributions; mean and variance; binomial | |
| 10 | 148–162 | Continuous random variables; normal distribution; standard normal table; normal approximation | **Exam 2** (Unit 2 + §5–§8) |
| 11 | 164–178 | Sampling distributions; CLT; introduction to inference | |
| 12 | 180–194 | Point and interval estimation; confidence intervals for μ and p | |
| 13 | 196–214 | Hypothesis testing logic; hypothesis testing for p | |
| 14 | 215–226 | Hypothesis testing for μ; Type I and Type II errors | **Exam 3** (§9–§12) |
| 15 | 228–252 | Case C→Q; two independent samples; matched pairs; ANOVA | |
| 16 | 255–264 | Case C→C (chi-square); Case Q→Q (regression inference); summary of inference; cumulative review | |
| Finals | — | | **Cumulative Final** |

**What changed from Schedule A:** Week 5 now carries 21 pages (scatterplots through
regression) and Week 15 carries 25 pages (three inference procedures plus ANOVA). Both are
heavy. If your section meets three times a week, use the extra period in those two weeks.

---

### Schedule C: 12-Week Term (accelerated / short term)

All fourteen COR content items are still covered. Compression comes from three sources,
not from dropping required topics:

1. **Wrap-up and summary pages are assigned as independent reading** rather than covered
   in class: pp. 37, 65, 66, 71, 86, 87, 114, 126, 162, 172, 173, 201, 224, 226, 253, 263,
   264. That is 17 pages of consolidation material that students can read on their own.
2. **Two midterms instead of three**, plus a cumulative final.
3. **Unit 1 is delivered in a single week.** It is the least computational unit and reads
   quickly.

Average load: roughly 20 pages per week, about 25% faster than Schedule B. This schedule
assumes a corequisite support section or substantial outside-of-class structure.

| Week | Book pages | Topics | Assessment |
|---|---|---|---|
| 1 | intro, 9, 67–71, 73–87 | **Unit 1 complete.** Big Picture; sampling and bias; observational studies and experiments; causation; sample surveys | |
| 2 | 10–30 | EDA framework; categorical and quantitative variables; histograms, stemplots; measures of center; measures of spread | |
| 3 | 31–37, 39–51 | Boxplots; standard deviation; role-type classification; Cases C→Q and C→C; scatterplots | **Exam 1** (Unit 1 + §3) |
| 4 | 52–66, 89–94 | Linear relationships and regression; causation and lurking variables; introduction to probability | |
| 5 | 95–96, 98–114 | Relative frequency; sample spaces and events; equally likely outcomes; probability rules | |
| 6 | 116–126, 128–135 | Conditional probability; independence; multiplication rule; probability trees; random variables and their distributions | |
| 7 | 136–147, 148–156 | Mean and variance of a random variable; binomial; continuous random variables; the normal distribution; standard normal table | |
| 8 | 157–162, 164–178 | Normal applications; normal approximation to the binomial; sampling distributions; CLT; introduction to inference | **Exam 2** (§3–§9) |
| 9 | 180–194, 196–200 | Point and interval estimation; confidence intervals for μ and p; hypothesis testing overview | |
| 10 | 201–220 | Hypothesis testing for p; hypothesis testing for μ (part 1) | |
| 11 | 221–226, 228–241 | Hypothesis testing for μ (part 2); Type I and Type II errors; Case C→Q; two independent samples; matched pairs (part 1) | |
| 12 | 242–252, 255–264 | Matched pairs (part 2); ANOVA; Case C→C (chi-square); Case Q→Q (regression inference); cumulative review | **Cumulative Final** |

**Pressure points in Schedule C.**

- **Week 12 is the hardest week of the term**, introducing ANOVA, chi-square, and regression
  inference back to back. Two mitigations: (a) regression inference (pp. 260–262) is largely
  a re-framing of the least-squares regression students already learned in Week 4, so it can
  be taught as a short capstone rather than a new procedure; (b) matched pairs (pp. 238–245)
  can be delivered as one worked example plus reading, since the mechanics reduce to the
  one-sample *t* test from Week 11.
- **Weeks 6–8 carry the probability unit** at nearly 20 pages per week. This is where
  students in accelerated sections typically fall behind. Front-load office hours and
  low-stakes practice here.
- **Verify with your department** that a 12-week section still meets the COR's 72 total
  contact hours (36 lecture + 36 activity). A 12-week term requires proportionally longer
  or more frequent meetings to hit that total.

---

## Summary of Recommended Actions

1. Verify the Part I content list against the live CCSF CurricUNET report before submitting
   this document to a curriculum committee.
2. Update the stale chi-square note in `overview.md` (Week 16 and Notes for Adopting
   Instructors). Chi-square is covered at pp. 255–259.
3. Choose a statistical software platform and build the lab/activity stream described in
   Gap 1. This is the one genuine content gap relative to the COR.
4. Add at least two assessed SLO F (ethics) tasks, using the anchor points in Gap 2.
5. Decide on CI ordering (mean-first, per the book, or proportion-first, per `overview.md`)
   and make the syllabus consistent.

---

*Sources: CCSF STAT C1000 Course Outline of Record (SLOs, via `overview.md`);
[Common Course Numbering STAT C1000 COR template](https://www.napavalley.edu/programs-and-academics/academic-affairs/academic-senate/committees/course-outlines-of-record/courses/math/STAT%20C1000%20COR%20FA25.pdf)
(Part I/Part II content outline, methods of instruction, contact hours);
[CCSF catalog listing for STAT C1000](https://www.ccsf.edu/academics/ccsf-catalog/courses-by-department/courses-by-subject/5875701).*
