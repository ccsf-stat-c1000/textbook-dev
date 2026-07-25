# Wrap-Up (Hypothesis Testing)

This module covered the z-test for the population proportion and both the z-test and t-test for the population mean. The following table summarizes when each of the tests is used:

| Test | Parameter | Variable of interest | Standard deviation |
| --- | --- | --- | --- |
| z-test for the population proportion | p | Categorical | (not applicable) |
| z-test for the population mean | $\mu$ | Quantitative | Population $\sigma$ known |
| t-test for the population mean | $\mu$ | Quantitative | Population $\sigma$ unknown; sample s used instead |

The module is also loaded with very important ideas that apply to the general process of hypothesis testing. Thus, the following summary discusses each of the above-named hypothesis tests within the context of the hypothesis testing process.

The process of hypothesis testing has four steps:

## Step 1: Stating the Null and Alternative Hypotheses

| Type of hypothesis test | Null hypothesis | Alternative hypothesis |
| --- | --- | --- |
| z-test for the population proportion | $H_0: p = p_0$ | $H_a: p \neq p_0$ or $H_a: p < p_0$ or $H_a: p > p_0$ |
| z-test for the population mean | $H_0: \mu = \mu_0$ | $H_a: \mu \neq \mu_0$ or $H_a: \mu < \mu_0$ or $H_a: \mu > \mu_0$ |
| t-test for the population mean | $H_0: \mu = \mu_0$ | $H_a: \mu \neq \mu_0$ or $H_a: \mu < \mu_0$ or $H_a: \mu > \mu_0$ |

## Step 2: Collecting Data, Checking Conditions, and Summarizing with a Test Statistic

*Check that the conditions under which the test can be reliably used are met.*

For the *z-test for the population proportion*, we can reliably use the test if the sample is random and $np_0 \geq 10$ and $n(1-p_0) \geq 10$.

For the *z-test* and *t-test for the population mean*, the following table summarizes the conditions under which they can be reliably used, and which test to use when:

| Situation | $\sigma$ known | $\sigma$ unknown |
| --- | --- | --- |
| Large sample size (population normal or not) | z-test | t-test (z-test is a good approximation) |
| Small sample size, population normal\* | z-test | t-test |
| Small sample size, population shape not normal or unknown | neither test can be used | neither test can be used |

\*By "population normal" we mean that either the population is known to be normal, or the population can be reasonably assumed to be normal as judged by the shape of the data histogram.

*Summarize the data using a test statistic.* The test statistic is a measure of the evidence in the data against $H_0$. The larger the test statistic is in magnitude, the more evidence the data present against $H_0$.

| Hypothesis test | Test statistic |
| --- | --- |
| z-test for the population proportion | $z=\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}}$ |
| z-test for the population mean | $z=\frac{\bar{x}-\mu_{0}}{\sigma/\sqrt{n}}$ |
| t-test for the population mean | $t=\frac{\bar{x}-\mu_{0}}{s/\sqrt{n}}$ |

## Step 3: Finding the P-value of the Test

The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against $H_0$. The smaller the p-value, the more evidence the data present against $H_0$.

In this module, we learned how to compute the p-value for the two z-tests (the z-test for the population proportion and the z-test for the population mean). However, for the t-test (and, actually, from this point on in the course), we will use software to find the p-value for us.

## Step 4: Making Conclusions

Conclusions about the *significance of the results*: if the p-value is small, the data present enough evidence to reject $H_0$ (and accept $H_a$); if the p-value is not small, the data do not provide enough evidence to reject $H_0$. To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at 0.05, but should not be considered inviolable.

Conclusions should always be made in the *context* of the problem.

## Additional Big Ideas About Hypothesis Testing

(*Note:* these ideas were already mentioned in the summary for hypothesis testing for the population proportion p; they are worth repeating because they apply to hypothesis testing in general.)

- Results that are based on a larger sample carry more weight, and therefore results that are not significant (do not provide evidence to reject $H_0$) may become significant if based on a larger sample size. As a result, even a very small and practically unimportant effect becomes statistically significant with a large enough sample size. The distinction between statistical significance and practical importance should therefore always be considered.
- For given data, the p-value of the two-sided test is always twice as large as the p-value of the one-sided test. It is therefore harder to reject $H_0$ in the two-sided case than it is in the one-sided case, in the sense that stronger evidence is required. Intuitively, the hunch or information that leads us to use the one-sided test can be regarded as a head start toward the goal of rejecting $H_0$.
- *95% confidence intervals* can be used in order to carry out *two-sided tests* (at the 0.05 significance level). If the null value is not included in the confidence interval (i.e., is not one of the plausible values for the parameter), we have enough evidence to reject $H_0$. Otherwise, we cannot reject $H_0$.
- If the results are significant, it might be of interest to follow up the test with a confidence interval in order to get insight into the actual value of the parameter of interest.

## Putting It All Together

:::{quiz} A nutrition researcher wants to test whether the mean daily sodium intake of adults in a city differs from the recommended 2,300 mg. She collects a random sample of 45 adults and records their intake; the population standard deviation is unknown. Which test should she use?
:hint: The variable (sodium intake) is quantitative, and only the sample standard deviation will be available.
:feedback-0: Correct! Quantitative variable + unknown $\sigma$ = t-test for the population mean. The large sample $(45 > 30)$ satisfies the conditions.
:feedback-1: The z-test for the mean requires a KNOWN population standard deviation.
:feedback-2: The z-test for the proportion is for categorical variables.
* *The t-test for the population mean
* The z-test for the population mean
* The z-test for the population proportion
:::

:::{quiz} A pollster tests whether the proportion of voters who favor a ballot measure exceeds 0.5, using a random sample of 800 voters. Which test should be used?
:hint: Favoring or not favoring the measure is a categorical variable.
:feedback-0: Correct! The variable is categorical and the parameter is a proportion, so the z-test for the population proportion applies (conditions: $800 \times 0.5 = 400 \geq 10$ in both groups).
:feedback-1: The t-test is for a quantitative variable's mean.
:feedback-2: The z-test for the mean is for a quantitative variable with $\sigma$ known.
* *The z-test for the population proportion
* The t-test for the population mean
* The z-test for the population mean
:::
