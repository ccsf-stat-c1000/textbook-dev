# The t-Test for a Mean: Worked Examples

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

For comparison purposes, we will use a modified version of the two problems we used in the previous case. We'll first introduce the modified versions and explain the changes.

:::{admonition} Example 1: SAT-M Scores at Ross College (σ Unknown)
:class: tip

The SAT is constructed so that scores have a national average of 500. The distribution is close to normal. The dean of students of Ross College suspects that in recent years the college attracts students who are more quantitatively inclined. A random sample of 4 students entering Ross College had an average math SAT (SAT-M) score of 550 and a *sample standard deviation of 100*. Does this provide enough evidence for the dean to conclude that the mean SAT-M of all Ross College students is higher than the national mean of 500?

Note that the problem was changed so that the population standard deviation (which was assumed to be 100 before) is now unknown, and instead we assume that the sample of 4 students produced a sample mean of 550 (no change) and a sample standard deviation of s = 100. (Sample standard deviations are never such nice rounded numbers, but for the sake of comparison we left it as 100.) Due to the changes, the z-test for the population mean is no longer appropriate, and we need to use the t-test.
:::

:::{admonition} Example 2: Concentration of a Chemical in a Drug (σ Unknown)
:class: tip

A certain prescription medicine is supposed to contain an average of 250 parts per million (ppm) of a certain chemical. If the concentration is higher than this, the drug may cause harmful side effects; if it is lower, the drug may be ineffective. The manufacturer runs a check to see if the mean concentration in a large shipment conforms to the target level of 250 ppm or not. A simple random sample of 100 portions is tested, and the sample mean concentration is found to be 247 ppm with a *sample standard deviation of 12 ppm*.

The changes are similar to example 1: we no longer assume that the population standard deviation is known, and instead use the sample standard deviation of 12. Again, the problem was thus changed from a z-test problem to a t-test problem.

However, as we mentioned earlier, due to the large sample size (n = 100) there should not be much difference whether we use the z-test or the t-test. The sample standard deviation, s, is expected to be close enough to the population standard deviation σ. We'll see this as we solve the problem.
:::

Let's carry out the t-test for both of these problems.

:::{admonition} Example 1: Carrying Out the t-Test
:class: tip

*Step 1:* There are no changes in the hypotheses being tested: $H_0: \mu = 500$ vs. $H_a: \mu > 500$.

*Step 2:* The conditions that allow us to use the t-test are met since (i) the sample is random, and (ii) SAT-M is known to vary normally in the population (which is crucial here, since the sample size is only 4—the "variable varies normally, small sample" case).

The test statistic is:

$$t=\frac{\bar{x}-\mu_{0}}{\frac{s}{\sqrt{n}}}=\frac{550-500}{\frac{100}{\sqrt{4}}}=1$$

The data (represented by the sample mean) are 1 standard error above the null value.

*Step 3:* Recall that in general the p-value is calculated under the null distribution of the test statistic, which, in the t-test case, is t(n − 1). In our case, in which n = 4, the p-value is calculated under the t(3) distribution—the area to the right of 1. Using statistical software, we find that the p-value is 0.196.

For comparison purposes, the p-value that we got when we carried out the z-test for this problem (when we assumed that 100 was the known σ rather than the calculated sample standard deviation) was 0.159. It is not surprising that the p-value of the t-test is larger, since the t distribution has fatter tails. Even though in this particular case the difference between the two values does not have practical implications (since both are large and lead to the same conclusion), the difference is not trivial.

*Step 4:* The p-value (0.196) is large, indicating that the results are not significant. The data do not provide enough evidence to conclude that the mean SAT-M among Ross College students is higher than the national mean (500).
:::

:::{admonition} Example 2: Carrying Out the t-Test
:class: tip

*Step 1:* There are no changes in the hypotheses being tested: $H_0: \mu = 250$ vs. $H_a: \mu \neq 250$.

*Step 2:* The conditions that allow us to use the t-test are met: (i) the sample is random, and (ii) the sample size (n = 100) is large enough for the Central Limit Theorem to apply and ensure the normality of $\bar{X}$.

The test statistic is:

$$t=\frac{\bar{x}-\mu_{0}}{\frac{s}{\sqrt{n}}}=\frac{247-250}{\frac{12}{\sqrt{100}}}=-2.5$$

The data (represented by the sample mean) are 2.5 standard errors below the null value.

*Step 3:* The p-value is the combined area in both tails of the t(99) distribution beyond ±2.5. Using statistical software, we calculate a p-value of 0.014 with a 95% confidence interval of (244.619, 249.381). For comparison purposes, the output we got when we carried out the z-test for the same problem was a p-value of 0.012 with a 95% confidence interval of (244.648, 249.352).

Note that here the difference between the p-values is quite negligible (0.002). This is not surprising, since the sample size is quite large (n = 100), in which case, as we mentioned, the z-test (in which we treat s as the known σ) is a very good approximation to the t-test. Note also how the two 95% confidence intervals are similar (for the same reason).

*Step 4:* The p-value is small (0.014), indicating that at the 5% significance level, the results are significant. The data therefore provide evidence to conclude that the mean concentration in the entire shipment is not the required 250 ppm.
:::

```{admonition} Comments
:class: important

1. The 95% confidence interval for μ can be used here in the same way it is used when σ is known: either as a way to conduct the two-sided test (checking whether the null value falls inside or outside the confidence interval) or following a t-test where $H_0$ was rejected (in order to get insight into the value of μ).

2. While it is true that when σ is unknown and the sample size is large the z-test is a good approximation for the t-test, since we are using software to carry out the t-test anyway, there is not much gain in using the z-test as an approximation instead. We might as well use the more exact t-test regardless of the sample size. However, it is always worthwhile knowing what happens behind the scenes.
```

## Check Your Understanding: Reading t-Test Output

A group of Internet users 50-65 years of age were randomly chosen and asked to report the weekly number of hours they spend online. The purpose of the study was to determine whether the mean weekly number of hours that Internet users in that age group spend online differs from the mean for Internet users in general, which is 12.5. Statistical software gives the following output:

| Test of μ = 12.5 vs ≠ 12.5 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **N** | **Mean** | **StDev** | **SE Mean** | **T** | **P** |
| 125 | 12.008 | 3.214 | 0.287 | −1.71 | 0.090 |

:::{quiz} Using α = 0.05, what is the correct conclusion from this output?
:hint: Compare the p-value 0.090 with 0.05.
:feedback-0: Correct! Since 0.090 > 0.05, the data do not provide enough evidence that the mean for this age group differs from 12.5 hours.
:feedback-1: 0.090 exceeds 0.05, so the results are NOT statistically significant.
:feedback-2: Failing to reject H₀ does not prove the mean is exactly 12.5.
* *Do not reject H₀—there is not enough evidence that the mean differs from 12.5 hours
* Reject H₀ and conclude the mean differs from 12.5 hours
* Accept H₀ and conclude the mean is exactly 12.5 hours
:::

:::{quiz} Which distribution was used to find the p-value of 0.090?
:hint: This is a t-test with n = 125.
:feedback-0: Correct! The t-test's null distribution is t(n − 1) = t(124); the p-value is the two-tailed area beyond ±1.71.
:feedback-1: σ was unknown (the StDev shown is the sample standard deviation), so the t distribution is used.
:feedback-2: The degrees of freedom are n − 1 = 124.
* *The t distribution with 124 degrees of freedom
* The standard normal distribution
* The t distribution with 125 degrees of freedom
:::

## Let's Summarize

1. In hypothesis testing for the population mean (μ), we distinguish between two cases: the less common case when the population standard deviation (σ) is known, and the more practical case when the population standard deviation is unknown and the sample standard deviation (s) is used instead.

2. In the case when σ is known, the test for μ is called the z-test, and in the case when σ is unknown and s is used instead, the test is called the t-test.

3. In both cases, the null hypothesis is $H_0: \mu = \mu_0$, and the alternative, depending on the context, is one of the following: $H_a: \mu < \mu_0$, or $H_a: \mu > \mu_0$, or $H_a: \mu \neq \mu_0$.

4. Both tests can be safely used as long as the following two conditions are met: (i) the sample is random (or can at least be considered random in context), and (ii) either the sample size is large (n > 30) or, if not, the variable of interest can be assumed to vary normally in the population.

5. In the z-test, the test statistic is $z=\frac{\bar{x}-\mu_{0}}{\sigma/\sqrt{n}}$, whose null distribution is the standard normal distribution (under which the p-values are calculated).

6. In the t-test, the test statistic is $t=\frac{\bar{x}-\mu_{0}}{s/\sqrt{n}}$, whose null distribution is t(n − 1) (under which the p-values are calculated).

7. For large sample sizes, the z-test is a good approximation for the t-test.

8. Confidence intervals can be used to carry out the two-sided test ($H_a: \mu \neq \mu_0$), and in cases where $H_0$ is rejected, the confidence interval can give insight into the value of the population mean (μ).

9. Here is a summary of which test to use under which conditions:

   | Situation | σ known | σ unknown |
   | --- | --- | --- |
   | Large sample size (population normal or not) | z-test | t-test (z-test is a good approximation) |
   | Small sample size, population normal\* | z-test | t-test |
   | Small sample size, population shape not normal or unknown | neither test can be used | neither test can be used |

   \*By "population normal" we mean that either the population is known to be normal, or the population can be reasonably assumed to be normal as judged by the shape of the data histogram.

## Check Your Understanding: Carrying Out a t-Test

*Scenario:* The Intel Corporation is conducting quality control on its circuit boards. Thickness of the manufactured circuit boards varies unavoidably from board to board. Suppose the thickness of the boards produced by a certain factory process varies normally. The distribution of thickness of the circuit boards is supposed to have the mean μ = 12 mm if the manufacturing process is working correctly. A random sample of five circuit boards is selected and measured, and the average thickness is found to be 9.13 mm, and the standard deviation for the sample is computed to be 1.11 mm.

:::{quiz} Which test is appropriate here, and why?
:hint: Is σ known? Is the small sample a problem?
:feedback-0: Correct! σ is unknown (we only have the sample standard deviation 1.11), so we use the t-test; the small sample (n = 5) is acceptable because thickness is known to vary normally.
:feedback-1: We only know the SAMPLE standard deviation, so the z-test is not appropriate.
:feedback-2: Since the population is known to be normal, the small sample size is not a problem.
* *The t-test—σ is unknown, and the normal population makes the small sample acceptable
* The z-test—the standard deviation is known to be 1.11
* Neither—the sample size of 5 is too small
:::

:::{quiz} The test statistic is t = (9.13 − 12)/(1.11/√5) ≈ −5.78, and the two-sided p-value (under t(4)) is about 0.004. What should Intel conclude?
:hint: Compare the p-value to 0.05 and interpret in context.
:feedback-0: Correct! The p-value is far below 0.05, so we reject H₀ and conclude the process mean is not 12 mm—the boards are running thin, and the process needs attention.
:feedback-1: 0.004 is much smaller than 0.05—the results are highly significant.
:feedback-2: The direction matters for the practical conclusion: the sample mean (9.13) is well below the target 12 mm.
* *Reject H₀—the mean thickness differs from 12 mm (the boards appear too thin)
* Do not reject H₀—the evidence is insufficient
* Reject H₀—the boards appear too thick
:::

Now, suppose that Intel is testing a brand-new manufacturing process, for which prior information isn't available. In particular, for this new process, *the population distribution's shape isn't known*.

:::{quiz} For the new process, samples of various sizes are collected. In which case can a t-test for μ safely be used?
:hint: With an unknown population shape, what rescues normality of the sample mean?
:feedback-0: Correct! With the population shape unknown, only a large sample (n > 30) lets the Central Limit Theorem guarantee approximate normality of the sample mean.
:feedback-1: A small sample whose histogram is strongly right-skewed suggests a non-normal population—the t-test would be unreliable.
:feedback-2: With the shape unknown and only 6 observations, we cannot verify normality, so the t-test is risky.
* *A sample of 35 boards, even if its histogram is somewhat skewed
* A sample of 10 boards whose histogram is strongly right-skewed
* Any sample of at least 6 boards
:::

## Reflection

Consider the two versions of each example (σ known vs. σ unknown). Write a sentence or two in your own words explaining when the choice between the z-test and t-test makes a real difference, and when it hardly matters.
