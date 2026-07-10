# Conclusion of Case C→Q

We are now done with case C→Q. We learned that this case is further classified into sub-cases, depending on the number of groups that we are comparing (i.e., the number of categories that the explanatory variable has) and the design of the study (independent vs. dependent samples). For each of the three sub-cases that we covered, we learned the appropriate inferential method, and emphasized the idea behind the method, the conditions under which it can be safely used, how to carry it out using software, and the interpretation of the results.

The following table summarizes when each of the three sub-cases covered in this module is used:

| Method | When it is used |
| --- | --- |
| Two-sample t-test | Categorical explanatory variable with two categories; comparing two population means based on two *independent* samples; either normal populations or large sample sizes |
| Paired t-test (special case of the one-sample t-test) | Categorical explanatory variable with two categories; comparing two population means when the samples are *dependent* ("matched pairs")—every observation in one sample is linked to an observation in the other sample (e.g., same subjects measured twice, twins) |
| ANOVA F-test | Categorical explanatory variable with *more than two* categories; comparing more than two population means based on independent samples |

The following summary discusses each of the above-named sub-cases of C→Q within the context of the hypothesis testing process.

## Step 1: Stating the Null and Alternative Hypotheses

| Method | Null hypothesis | Alternative hypothesis |
| --- | --- | --- |
| Two-sample t-test | $H_0: \mu_1 - \mu_2 = 0$ (same as $\mu_1 = \mu_2$) | One of: $H_a: \mu_1-\mu_2 < 0$, $H_a: \mu_1-\mu_2 > 0$, $H_a: \mu_1-\mu_2 \neq 0$ |
| Paired t-test | $H_0: \mu_d = 0$ | One of: $H_a: \mu_d < 0$, $H_a: \mu_d > 0$, $H_a: \mu_d \neq 0$ |
| ANOVA F-test | $H_0: \mu_1 = \mu_2 = \cdots = \mu_k$ | $H_a$: not all the μ's are equal |

## Step 2: Check Conditions, and Summarize the Data Using a Test Statistic

*Check that the conditions under which the test can be reliably used are met.*

For the *two-sample t-test*, the conditions are: (1) the two samples are independent and random, and (2) either both populations are normal, or the populations are not normal but both sample sizes are large (> 30).

For the *paired t-test* (as a special case of a one-sample t-test), the conditions are: (1) the sample of differences is random (or at least can be considered so in context), and (2) either the differences vary normally (checked visually with a histogram of the sample differences) or the sample size is large.

For the *ANOVA F-test*, the conditions are: (1) the samples drawn from each of the populations being compared are independent; (2) the response variable varies normally within each of the populations being compared (as is often the case, we do not have to worry about this condition for large sample sizes); and (3) the populations all have the same standard deviation (rule of thumb: largest sample standard deviation divided by smallest is less than 2).

*Summarize the data using a test statistic.*

| Sub-case of C→Q | Test statistic |
| --- | --- |
| Two-sample t-test | $t=\frac{(\bar{y}_{1}-\bar{y}_{2})-0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}$ |
| Paired t-test | $t=\frac{\bar{x}_{d}-0}{\frac{s_{d}}{\sqrt{n}}}$ |
| ANOVA F-test | $F=\frac{\text{variation among the sample means}}{\text{variation within the groups}}$ |

## Step 3: Finding the P-value of the Test

Use statistical software to determine the p-value. The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against $H_0$. The smaller the p-value, the more evidence the data present against $H_0$. The p-values for all three C→Q tests are obtained from the software output.

## Step 4: Making Conclusions

Conclusions about the *significance of the results*: if the p-value is small, the data present enough evidence to reject $H_0$ (and accept $H_a$); if the p-value is not small, the data do not provide enough evidence to reject $H_0$. To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at 0.05, but should not be considered inviolable.

Conclusions should always be stated in the context of the problem.

*Following the test:*

- For a two-sample t-test, a *95% confidence interval* for $\mu_1-\mu_2$ can be very insightful after a test has rejected the null hypothesis, and can also be used for testing in the two-sided case.
- For a paired t-test, a *95% confidence interval* for $\mu_d$ can be very insightful after a test has rejected the null hypothesis, and can also be used for testing in the two-sided case.
- If the ANOVA F-test has rejected the null hypothesis, looking at the *confidence intervals* for the population means in the output can provide visual insight into why $H_0$ was rejected (i.e., which of the means differ).

## Putting It All Together

:::{quiz} A researcher compares mean daily screen time across three age groups (teens, adults, seniors) using independent random samples. Which method applies?
:hint: How many groups? Are the samples independent?
:feedback-0: Correct! Three groups with independent samples calls for the ANOVA F-test.
:feedback-1: The two-sample t-test handles only two groups.
:feedback-2: The samples are independent (different people in each group), not paired.
* *ANOVA F-test
* Two-sample t-test
* Paired t-test
:::

:::{quiz} A researcher measures each participant's blood pressure while sitting and again while standing, to see if position affects blood pressure. Which method applies?
:hint: Each participant is measured twice.
:feedback-0: Correct! Each subject provides both measurements, making the samples dependent—a matched pairs design analyzed with the paired t-test.
:feedback-1: The two samples consist of the same people, so they are not independent.
:feedback-2: There are only two conditions (sitting, standing), so ANOVA is not needed.
* *Paired t-test
* Two-sample t-test
* ANOVA F-test
:::

:::{quiz} A researcher compares the mean starting salaries of graduates from two different degree programs, using separate random samples of 60 graduates from each program. Which method applies?
:hint: Two unrelated groups, separately sampled.
:feedback-0: Correct! Two groups, independently sampled—the two-sample t-test (conditions are met with n = 60 in each group).
:feedback-1: No observation in one sample is linked to an observation in the other, so pairing doesn't apply.
:feedback-2: Only two means are being compared, so ANOVA is not needed.
* *Two-sample t-test
* Paired t-test
* ANOVA F-test
:::
