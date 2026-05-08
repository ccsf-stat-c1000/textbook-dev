# Instructor Overview

## Student Learning Outcomes

From the [STAT C1000 Course Outline of Record](https://ccsf.curricunet.com/DynamicReports/AllFieldsReportByEntity/14744?entityType=Course&reportId=28):

Upon completion of this course, a student will be able to:

- **SLO A.** Assess how data were collected and recognize how data collection affects what conclusions can be drawn from the data.
- **SLO B.** Identify appropriate graphs and summary statistics for variables and relationships between them and correctly interpret information from graphs and summary statistics.
- **SLO C.** Describe and apply probability concepts and distributions.
- **SLO D.** Demonstrate an understanding of, and ability to use, basic ideas of statistical processes, including hypothesis tests and confidence interval estimation.
- **SLO E.** Identify appropriate statistical techniques and use technology-based statistical analysis to describe, interpret, and communicate results.
- **SLO F.** Evaluate ethical issues in statistical practice.

Each learning objective below is tagged with the SLO(s) it supports, e.g., `[SLO A, E]`.

---

## Week 1: Course Orientation and Introduction to Statistical Thinking

**Instructor Overview.** Use the first week to establish classroom culture and introduce students to the fundamental vocabulary of statistics. Begin with the ice-breaker activity to build rapport, then move into distinguishing populations, samples, and subjects using real news articles. Introduce the central distinction between observational studies and experiments, and lay groundwork for the correlation-versus-causation discussion that will run throughout the course. Emphasize that "explanatory" and "response" variables are a framing device students will return to during regression and hypothesis testing. Also introduce, briefly, to be revisited, the contrast between random selection (which gives a representative sample) and random assignment (which gives fair groups).

**Student Overview.** This week, you'll get oriented to the course and start thinking like a statistician. You'll learn how statisticians describe the "who" of a study, the difference between a population (everyone we want to know about) and a sample (the people we actually study). You'll also read real news articles and practice identifying these features. Finally, you'll see that not all studies are the same: some just observe what's happening, while others actively manipulate conditions to test cause and effect.

**Learning objectives.**
- Identify the population, sample, and subjects in a research study or news article. [SLO A]
- Distinguish observational studies from experiments based on the research question. [SLO A]
- Identify explanatory and response variables in a study. [SLO A, B]
- Explain the difference between correlation and causation. [SLO A, F]
- Distinguish random selection (for representativeness) from random assignment (for fair groups). [SLO A]

---

## Week 2: Sampling Methods and Sources of Bias

**Instructor Overview.** Build on last week's foundation by going deeper into how data get collected. Begin with Simple Random Sampling (SRS) and use a simulation or quick demo to address the persistent misconception that "a large population requires a large sample." Introduce systematic, stratified, cluster, and multi-stage sampling using concrete examples, CCSF's student population is a natural context for discussing stratification. Cover selection bias (voluntary response, convenience) and non-selection bias (response, non-response) explicitly; well-known examples (political polls, online reviews) tend to land. Close the unit with experimental design: treatments, control groups, placebos, confounding variables, blinding, double-blinding, and blocking. Hit the "why random assignment?" question with a worked example. This is a natural place to introduce the course's ethical thread (SLO F).

**Student Overview.** How we collect data determines what we can learn from it. This week, you'll learn the difference between random sampling strategies, the gold standard for getting a representative sample, and biased sampling methods that can lead to the wrong conclusions. You'll also look inside experiments: how researchers use control groups, placebos, and "blinding" to make sure treatment effects are real, not imagined or accidental. By the end of the week, you should be able to read a study and spot whether its conclusions are trustworthy.

**Learning objectives.**
- Define and identify a Simple Random Sample (SRS). [SLO A]
- Compare and contrast SRS, systematic, stratified, cluster, and multi-stage sampling strategies. [SLO A, E]
- Identify sampling bias (voluntary, convenience) and non-selection bias (response, non-response). [SLO A, F]
- Identify treatment and response variables and the number of treatment conditions in an experiment. [SLO A]
- Explain the role of control groups, placebos, random assignment, blinding/double-blinding, and blocking in experimental design. [SLO A, F]
- Evaluate whether a study's design supports the conclusions being drawn from it. [SLO A, F]

---

## Week 3: Visualizing Quantitative Data and Measures of Center

**Instructor Overview.** Transition into descriptive statistics. Start by clearly distinguishing categorical from quantitative variables, a recurring theme all semester. Introduce dotplots as a low-barrier entry to the ideas of center, spread, and shape. Move to histograms, emphasizing the construction of a frequency distribution table and the difference between frequency and relative frequency. Watch for common student errors (unequal bin widths, conflating histograms with bar charts). Close the week by introducing the three measures of center, mode, median, and mean, and showing how the shape of a distribution (symmetric, skewed right, skewed left) affects which measure is most representative.

**Student Overview.** This week shifts into the heart of descriptive statistics. You'll learn how to turn a pile of numbers into a picture using dotplots and histograms, and how to describe what you see: Where is the center of the data? How spread out is it? Is it symmetric or lopsided? You'll also meet the three main ways to describe what's "typical" in a dataset, the mode, median, and mean, and learn when to use each one.

**Learning objectives.**
- Distinguish categorical from quantitative variables. [SLO B]
- Construct and interpret dotplots, using visual intuition to identify center, spread, and shape. [SLO B, E]
- Construct a frequency distribution table and create frequency and relative frequency histograms. [SLO B, E]
- Describe the shape of a distribution as symmetric (bell-shaped, uniform) or asymmetric (skewed right, skewed left). [SLO B]
- Compute the mode, median, and mean of a dataset. [SLO B, E]
- Select the most representative measure of center based on the shape of the distribution. [SLO B]

---

## Week 4: Measures of Variability and Exam 1 Review

**Instructor Overview.** Complete the descriptive statistics toolkit with measures of spread. Introduce the IQR and the 1.5 × IQR fence rule for identifying outliers; boxplots are useful for visualization. Then move to standard deviation, compute it by hand once for transparency, then shift to technology. Emphasize the interpretation of SD as a "typical distance from the mean," and introduce the Empirical Rule (68-95-99.7%) for bell-shaped distributions. Reserve the second class period for a comprehensive review of Weeks 1–4 in preparation for Exam 1.

**Student Overview.** This week finishes your toolkit for describing a single variable. You'll learn two ways to measure how spread out a dataset is: the IQR (which pairs with the median) and the standard deviation (which pairs with the mean). You'll also learn a surprisingly powerful rule, the 68-95-99.7 Rule, that lets you make strong predictions about bell-shaped data. We'll end the week reviewing everything so far to get ready for Exam 1.

**Learning objectives.**
- Compute the interquartile range (IQR) and use the 1.5 × IQR fence rule to identify outliers. [SLO B, E]
- Compute the standard deviation (SD) using technology and interpret it as a typical distance from the mean. [SLO B, E]
- Use SD to identify the typical range where the majority of the data fall. [SLO B]
- Apply the Empirical Rule (68-95-99.7%) to bell-shaped distributions. [SLO B, C]
- Select appropriate measures of center and spread based on the shape of the distribution. [SLO B, E]

---

## Week 5: Exam 1 and Contingency Tables

**Instructor Overview.** Administer Exam 1 during one class period. The exam should cover data collection (Unit 1) and univariate descriptive statistics (Unit 2). In the second period, pivot to bivariate data by introducing contingency tables for two categorical variables. Focus on the key distinction between row percentages, column percentages, and joint percentages, and when each is appropriate to answer a given research question. Use examples where students can see that choosing the wrong percentage can flip the apparent conclusion.

**Student Overview.** Exam 1 this week covers everything from Weeks 1–4: sampling, experimental design, and how to describe one variable at a time using graphs and summary statistics. After the exam, we'll move into looking at *two* variables at the same time, starting with contingency tables for categorical data (like "gender" and "major"). You'll learn that how you calculate percentages matters: the same table can tell different stories depending on which direction you divide.

**Learning objectives.**
- Demonstrate mastery of Unit 1 and Unit 2 content through Exam 1. [SLO A, B, E]
- Construct and interpret contingency tables for two categorical variables. [SLO B, E]
- Determine whether to use row, column, or joint percentages to answer a specific research question. [SLO B, E]

---

## Week 6: Correlation, Regression, and Introduction to Probability

**Instructor Overview.** Begin with scatterplots. Emphasize the convention, explanatory variable on the x-axis, response on the y-axis, and teach students to describe form, direction, strength, and influential points. Build intuition for the correlation coefficient by showing scatterplots with known *r* values before reaching for technology. Use technology to fit a least-squares regression line and make predictions; discuss extrapolation as a cautionary tale. Introduce residuals. Shift midweek into probability: define sample space, events, and equally likely outcomes, and the distinction between theoretical and empirical probability. Introduce the Law of Large Numbers with a simple simulation (coin flips work well).

**Student Overview.** This week bridges two big ideas. First, you'll finish looking at relationships, this time between two quantitative variables, using scatterplots and the correlation coefficient (*r*). You'll learn to fit a "line of best fit" and use it to make predictions. Then we'll pivot to probability, the mathematical language of uncertainty. You'll learn the vocabulary (sample space, events) and the crucial difference between what probability predicts in theory and what we actually see in practice.

**Learning objectives.**
- Construct a scatterplot with explanatory and response variables placed correctly. [SLO B, E]
- Describe a scatterplot in terms of form, direction, strength, and influential points. [SLO B]
- Interpret the linear correlation coefficient *r* and distinguish strong from weak linear relationships. [SLO B, E]
- Use technology to find the best-fit line and apply it to make predictions. [SLO B, E]
- Compute and interpret residuals. [SLO B, E]
- Define sample space, events, and equally likely outcomes. [SLO C]
- Distinguish between theoretical and empirical probability and explain the Law of Large Numbers. [SLO C]

---

## Week 7: Probability Rules and Conditional Probability

**Instructor Overview.** Cover the foundational rules of probability: the Addition Law, the Multiplication Law, and the Complement Rule. Use Venn diagrams to build visual intuition for mutually exclusive versus independent events, students often conflate these. Introduce conditional probability formally and work examples where the condition visibly shrinks the sample space. The "percent reduction in risk" framing works well for examples grounded in health data and connects to real-world statistical communication (SLO E).

**Student Overview.** Once you know what probability *is*, you need rules for working with it. This week, you'll learn how to calculate the probability that *either* of two events happens, the probability that *both* happen, and the probability of the "opposite" of an event. You'll also meet conditional probability, the probability of something happening *given* that something else already happened. These tools show up everywhere: weather forecasts, medical tests, insurance, and risk analysis.

**Learning objectives.**
- Define mutually exclusive events, independent events, conditional probability, and the complement of an event. [SLO C]
- Construct and interpret Venn diagrams for probability problems. [SLO C, E]
- Apply the Addition Law, Multiplication Law, and Complement Rule to compute probabilities. [SLO C]
- Compute conditional probabilities using the conditional probability formula. [SLO C]
- Interpret and compute the percent reduction in risk from conditional probabilities. [SLO C, E]

---

## Week 8: Bayes' Reasoning and Random Variables

**Instructor Overview.** Introduce Bayes'-style reasoning through the "hypothetical 10,000 table" approach rather than through Bayes' formula directly, this is far more accessible for introductory students. Frame examples around medical testing (false positives and false negatives) since this is the canonical application and connects to SLO F (ethical reasoning around medical decisions). Then pivot to random variables: define discrete random variables, construct a probability distribution, and compute the expected value and standard deviation. Emphasize that the expected value is the population mean of the random variable and that total probability (the area under the distribution) always equals 1.

**Student Overview.** This week tackles one of the most counterintuitive ideas in probability: even a very accurate medical test can give misleading results if the disease is rare. You'll learn to solve these problems using a simple table rather than a scary formula. Then we'll introduce *random variables*, a way to attach numbers to random outcomes, and learn to compute the *expected value*, which is basically the long-run average of a random process.

**Learning objectives.**
- Distinguish between false positives and false negatives in testing contexts. [SLO C, F]
- Compute conditional probabilities using a hypothetical 10,000 contingency table. [SLO C, E]
- Define a random variable and distinguish discrete from continuous random variables. [SLO C]
- Construct a probability distribution (probability model) for a discrete random variable. [SLO C]
- Compute the expected value E(X) and standard deviation of a discrete random variable and interpret them. [SLO C]
- Explain why total probability (and total area under a probability distribution) equals 1. [SLO C]

---

## Week 9: Continuous Distributions, the Normal Distribution, and Z-scores

**Instructor Overview.** Bridge from discrete to continuous distributions by starting with simple shapes, uniform (rectangles) and triangular, where probability is literally area. This scaffolds naturally into the normal distribution. Revisit the Empirical Rule, now as a property of the normal curve rather than a loose rule for bell-shaped data. Introduce percentiles and z-scores as tools for comparing observations across different distributions. Use technology (Desmos, StatCrunch, or graphing calculator) for computing normal probabilities and inverse normal values. Briefly introduce the binomial formula. This week lays the foundation for everything that follows in inference.

**Student Overview.** The "normal curve" is the most famous shape in statistics, and this week you'll learn why. We'll start by calculating probability as area under simpler shapes (rectangles, triangles) and build up to the bell curve. You'll learn to compute z-scores, a way to express how unusual an observation is, and use technology to find probabilities under the normal curve. This material is the foundation for the second half of the course, so we'll take our time.

**Learning objectives.**
- Compute probabilities under uniform and triangular continuous distributions as areas. [SLO C, E]
- Identify the parameters (mean and standard deviation) of a normal distribution and describe how they determine its shape. [SLO C]
- Apply the Empirical Rule (68-95-99.7%) to the normal distribution. [SLO C]
- Compute and interpret percentiles. [SLO B, C]
- Compute z-scores and interpret them as standardized distances from the mean. [SLO C, E]
- Use technology to find probabilities and z-scores for normal distributions. [SLO C, E]
- Apply the binomial formula to compute binomial probabilities. [SLO C, E]

---

## Week 10: Review and Exam 2

**Instructor Overview.** Use the first class period for a comprehensive review covering bivariate descriptive statistics (contingency tables, correlation, regression) and the full probability unit (rules, conditional probability, random variables, distributions). Focus review time on material students consistently struggle with, typically conditional probability/Bayes' scenarios and z-score computations. Administer Exam 2 in the second period, covering all of Units 3 and 4.

**Student Overview.** This week is dedicated to consolidating everything you've learned about probability and bivariate relationships before Exam 2. Bring your questions to the review session, this is your chance to clear up anything that still feels fuzzy. Exam 2 covers Weeks 6–9: scatterplots, regression, probability rules, conditional probability, random variables, and the normal distribution.

**Learning objectives.**
- Review and synthesize content from Units 3 and 4. [SLO B, C, E]
- Apply probability concepts, conditional probability, and normal distributions to solve multi-step problems. [SLO C, E]
- Demonstrate mastery of Unit 3 and Unit 4 content through Exam 2. [SLO B, C, E]

---

## Week 11: The Central Limit Theorem and Introduction to Confidence Intervals

**Instructor Overview.** This is the conceptual turning point of the course: the move from descriptive to inferential statistics. Clearly distinguish parameters (population) from statistics (sample). Use applets or simulations to show how a sampling distribution arises, and specifically how sample size affects its shape, center, and spread. Introduce the Central Limit Theorem carefully, paying attention to the normality criteria for proportions (commonly np ≥ 10 and n(1−p) ≥ 10). Define standard error. Then introduce the logic of confidence intervals conceptually *before* any computation: margin of error, confidence level, and what "confidence" actually means. This is where persistent misconceptions form, so it pays to invest time.

**Student Overview.** Up to now, you've been describing data you already have. This week begins the big shift toward *inference*, using a sample to learn about a population you can't measure directly. You'll meet the Central Limit Theorem (arguably the most important idea in statistics) and start to understand why larger samples give us more reliable information. Then you'll learn what a "confidence interval" is, and what it actually means when a news article says "52% of voters support X, plus or minus 3%."

**Learning objectives.**
- Distinguish between parameters (population) and statistics (sample). [SLO D]
- Describe the sampling distribution of sample proportions in terms of shape, center, and spread. [SLO C, D]
- Apply the normality criteria for the sampling distribution of a sample proportion. [SLO D]
- State and apply the Central Limit Theorem for sample proportions. [SLO C, D]
- Define and interpret the standard error. [SLO D]
- Explain the concepts of margin of error and confidence level in plain language. [SLO D, E]
- Interpret a confidence interval correctly and identify common misinterpretations. [SLO D, F]

---

## Week 12: Confidence Intervals for Proportions and Sampling Distributions for Means

**Instructor Overview.** Begin by computing confidence intervals for a population proportion. Work through examples at multiple confidence levels (90%, 95%, 99%) and sample sizes so students see how each affects interval width. Cover the sample size formula for achieving a target margin of error. Then turn to the sampling distribution of sample means, noting similarities and differences from the proportion case. Introduce the t-distribution with emphasis on *why* we need it (unknown σ) and how degrees of freedom affect its shape. Compute t-scores.

**Student Overview.** This week you'll start actually building confidence intervals for percentages, the kind you see in polls and news reports. You'll see how things like "95% confidence" and a larger sample size change the estimate. Then we'll repeat the CLT story for averages instead of percentages, which requires a small twist: a new distribution called the *t-distribution*, which looks like the normal distribution but accounts for extra uncertainty when we don't know the true population spread.

**Learning objectives.**
- Define and compute the estimated standard error for a sample proportion. [SLO D, E]
- Construct and interpret confidence intervals for a population proportion at various confidence levels. [SLO D, E]
- Compute the required sample size for a target margin of error and confidence level. [SLO D, E]
- Describe the sampling distribution of sample means in terms of shape, center, and spread. [SLO C, D]
- Explain the role of the t-distribution and compute t-scores. [SLO D, E]

---

## Week 13: Confidence Intervals for Means and Introduction to Hypothesis Testing

**Instructor Overview.** Complete the confidence interval material with intervals for a population mean using the t-distribution. Work through examples at different confidence levels and sample sizes and cover sample size determination for means. Then pivot to hypothesis testing. Set up the logic carefully: null versus alternative hypotheses, Type I and Type II errors, the significance level α, and p-values. Practice writing hypotheses in both symbolic and plain-language form. Introduce left-tailed, right-tailed, and two-tailed tests using a clear visual of the t-curve with shaded regions.

**Student Overview.** First half of the week: you'll build confidence intervals for means, the average height of a population, the average income in a city, and so on. Second half: the other big tool of statistical inference, *hypothesis testing*. This is the formal way statisticians answer yes/no questions with data: Is this new drug better than the old one? Did the intervention actually change behavior? You'll learn the logic, setting up null and alternative hypotheses, and meet the p-value, a number that's often misunderstood in the media.

**Learning objectives.**
- Construct and interpret confidence intervals for a population mean using the t-distribution. [SLO D, E]
- Compute the required sample size for a target margin of error for means. [SLO D, E]
- Define and set up null and alternative hypotheses (H₀ and Hₐ). [SLO D]
- Define and distinguish Type I and Type II errors. [SLO D, F]
- Define significance level (α) and p-value. [SLO D]
- Distinguish left-tailed, right-tailed, and two-tailed tests. [SLO D]

---

## Week 14: Hypothesis Testing for Proportions and Means

**Instructor Overview.** Apply the hypothesis testing framework to two settings: a single population proportion and a single population mean. Walk students through the full procedure repeatedly with different examples so the steps become routine: state hypotheses, check conditions, compute test statistic, find p-value, make a decision, interpret in context. Use technology for the computations but require students to articulate the logic in writing. Address the distinction between statistical significance and practical significance at least once, this connects directly to SLO F.

**Student Overview.** Now that you know the logic of hypothesis testing, you'll put it to work. This week you'll test claims about a single percentage (Is more than half of the city in favor of this policy?) and a single average (Is the average weight of apples at this orchard really 6 ounces?). You'll go through the full procedure using technology. We'll also talk about why "statistically significant" isn't always the same thing as "actually important."

**Learning objectives.**
- Conduct a complete hypothesis test for a population proportion: state hypotheses, check conditions, compute the test statistic, find the p-value, and interpret in context. [SLO D, E]
- Conduct a complete hypothesis test for a population mean using the t-distribution. [SLO D, E]
- Distinguish between statistical significance and practical significance. [SLO D, F]
- Interpret the results of a hypothesis test correctly and communicate them clearly. [SLO D, E, F]

---

## Week 15: Comparing Two Means and Exam 3

**Instructor Overview.** Introduce inference for two groups. Distinguish carefully between dependent samples (paired data, such as before/after measurements on the same subjects) and independent samples. Set up null and alternative hypotheses for both cases. Work through several examples using technology. Then administer Exam 3, covering Unit 5 (sampling distributions and confidence intervals) and Sections 6.1–6.3 (hypothesis testing for one sample). Exam 3 is the last exam before the final.

**Student Overview.** This week adds a crucial tool: comparing *two* groups. Is there a real difference in average outcome between the treatment and control groups? Do men and women actually differ in some measurable way? You'll learn how to do this for paired data (same people, two measurements) and independent groups (different people). Then we'll take Exam 3, which covers confidence intervals and hypothesis tests for one sample.

**Learning objectives.**
- Distinguish between dependent (paired) and independent samples. [SLO D]
- Set up null and alternative hypotheses for comparing two means. [SLO D]
- Conduct a hypothesis test and construct a confidence interval for the difference between two means using technology. [SLO D, E]
- Demonstrate mastery of Unit 5 and Sections 6.1–6.3 content through Exam 3. [SLO D, E]

---

## Week 16: ANOVA (and Optional Chi-Squared)

**Instructor Overview.** Introduce ANOVA as the natural extension of two-group comparisons to three or more groups. Explain "variance between samples" versus "variance within samples" conceptually, this intuition matters far more than the mechanics. Introduce the F-statistic and show a family of F-curves. Work through several examples using technology.

*Optional* The Course Outline lists chi-squared tests as required content (SLO D). If time permits, introduce chi-squared tests for goodness-of-fit and/or independence this week.

**Student Overview.** This week extends the two-group comparison to *three or more* groups using a technique called ANOVA (Analysis of Variance). You might ask: "Is average income different across these five regions?" ANOVA answers that kind of question. You'll focus on the idea, comparing variance *between* groups to variance *within* groups, and use technology for the actual computation. If time permits, we'll also touch on chi-squared tests for categorical data.

**Learning objectives.**
- Explain the logic of ANOVA in terms of variance between samples versus variance within samples. [SLO D]
- Identify the F-statistic and describe the shape of F-curves. [SLO C, D]
- Conduct an ANOVA test using technology and interpret the results in context. [SLO D, E]
- *(Optional)* Conduct and interpret a chi-squared test for goodness-of-fit or independence. [SLO D, E]

---

## Week 17: Comprehensive Final Review

**Instructor Overview.** Dedicate the full week to cumulative review. Emphasize the overall arc of the course: how data collection (Unit 1) affects what conclusions are possible, how descriptive statistics (Units 2–3) summarize what we have, how probability (Unit 4) quantifies uncertainty, and how inference (Units 5–6) lets us generalize from sample to population. Practice problem-identification skills, given a scenario, students should be able to choose the appropriate procedure (CI vs. hypothesis test, one sample vs. two samples, proportion vs. mean, etc.). This procedure-identification skill is usually the hardest part of the final for students. Include at least one example requiring ethical reasoning about data collection or interpretation (SLO F).

**Student Overview.** This week is all about tying the course together. You've come a long way, from learning how to read a dotplot to running full hypothesis tests. The final exam is cumulative, and the hardest part is usually *choosing* the right procedure for a given problem. So this week focuses on that skill: given a scenario, can you identify what kind of question it is and what tools apply? Come to office hours, work through practice problems, and ask questions.

**Learning objectives.**
- Synthesize course concepts to identify the appropriate statistical technique for a given research scenario. [SLO A, B, C, D, E]
- Communicate statistical results clearly and evaluate ethical considerations in data use. [SLO E, F]
- Demonstrate readiness for the comprehensive final exam. [SLO A, B, C, D, E, F]

---

## Week 17.5: Final Exam

**Instructor Overview.** Administer the cumulative final exam. Per the Course Outline, the final should assess all six SLOs and cover the normal distribution, estimation of parameters, tests for hypotheses, applications of the Central Limit Theorem, theoretical probability, and linear regression, ensuring broad coverage across the semester.

**Student Overview.** The comprehensive final exam. You've got this.

**Learning objectives.**
- Demonstrate cumulative mastery of all course content across all six Student Learning Outcomes. [SLO A, B, C, D, E, F]

---

## Notes for Adopting Instructors

- **Pacing flexibility.** The schedule assumes two class meetings per week. If your section meets more or less frequently, exam weeks (5, 10, 15) are the natural first places to adjust, for example, by folding the Week 4 / Week 9 review content into those exam weeks, or by adding a dedicated review day before each exam.
- **Chi-squared coverage.** As noted in Week 16, the Course Outline requires chi-squared content but the handouts do not include it. Confirm that your section covers chi-squared either in Week 16 (time permitting) or elsewhere as a supplement.
- **Technology.** The course outline lists Excel, Minitab, R, StatCrunch, and graphing calculators as acceptable technology. Choose one and use it consistently from Week 3 onward so students build fluency.
- **SLO F (ethics) thread.** Ethics is threaded throughout rather than taught as a standalone unit. Natural touchpoints: bias in sampling (Week 2), correlation vs. causation (Week 1 and revisited in Week 6), false positives in medical testing (Week 8), misinterpretation of p-values and statistical vs. practical significance (Weeks 11, 14), and a wrap-up in Week 17.