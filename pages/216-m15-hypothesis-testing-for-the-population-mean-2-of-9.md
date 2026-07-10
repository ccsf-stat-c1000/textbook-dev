# Hypothesis Testing for the Population Mean (2 of 9)

```{admonition} Learning Objectives
:class: note

- In a given context, specify the null and alternative hypotheses for the population proportion and mean.
- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Step 1: Stating the Hypotheses

The null and alternative hypotheses for the z-test for the population mean (μ) have exactly the same structure as the hypotheses for the z-test for the population proportion (p):

- The null hypothesis has the form $H_0: \mu = \mu_0$ (where $\mu_0$ is the null value).
- The alternative hypothesis takes one of the following three forms (depending on the context): $H_a: \mu < \mu_0$ (one-sided), $H_a: \mu > \mu_0$ (one-sided), or $H_a: \mu \neq \mu_0$ (two-sided).

:::{admonition} Example 1: SAT-M Scores at Ross College
:class: tip

In our example 1, based on a sample of 4 students from Ross College, we were testing whether the mean SAT-M of all Ross College students is higher than the national mean (which, by construction, is 500). The hypotheses are therefore:

- $H_0: \mu = 500$
- $H_a: \mu > 500$
:::

## Learn By Doing

:::{quiz} A tire manufacturer advertises that its tires last an average of 50,000 miles. A consumer group suspects the true average is lower. What are the appropriate hypotheses?
:hint: The advertised value is the null value; the group suspects LOWER.
:feedback-0: Correct! H₀: μ = 50,000 vs. Hₐ: μ < 50,000.
:feedback-1: The suspicion is specifically that tires last less, so the alternative is one-sided.
:feedback-2: The null hypothesis always states equality with the null value.
* *H₀: μ = 50,000; Hₐ: μ < 50,000
* H₀: μ = 50,000; Hₐ: μ ≠ 50,000
* H₀: μ < 50,000; Hₐ: μ = 50,000
:::

:::{admonition} Example 2: Concentration of a Chemical in a Drug
:class: tip

Here we want to test whether the mean concentration of a certain chemical in a large shipment of a certain prescription drug is the required 250 ppm. Since a concentration that is too high OR too low is a problem, the null and alternative hypotheses in this case are:

- $H_0: \mu = 250$
- $H_a: \mu \neq 250$
:::

## Step 2: Collecting Data and Summarizing Them

Since our parameter of interest is the population mean (μ), once we collect the data, we find the sample mean ($\bar{x}$).

However, we already know that in hypothesis testing we go a step beyond calculating the relevant sample statistic and summarize the data with a test statistic.

Recall that in the z-test for the proportion, the test statistic is the z-score (standardized value) of the sample proportion, assuming that $H_0$ is true. It should not be very surprising that in the z-test for the population mean, we do exactly the same thing.

The test statistic is the z-score (standardized value) of the sample mean ($\bar{x}$) assuming that $H_0$ is true (in other words, assuming that $\mu=\mu_0$).

We rely once again on probability results—in this case, we refer to results about the sampling distribution of the sample mean ($\bar{X}$). When we discussed probability models based on sampling distributions, we concluded that sample means behave as follows:

- *Center:* the mean of the sample means is μ, the population mean.
- *Spread:* the standard deviation of the sample means is $\frac{\sigma}{\sqrt{n}}$.
- *Shape:* the sample means are normally distributed if the variable is normally distributed in the population, or if the sample size is large enough to guarantee approximate normality. Recall that this last statement is the Central Limit Theorem. As a general guideline, we said that if n > 30, the Central Limit Theorem applies and we can use a normal curve as a probability model.

Based on this description of the sampling distribution of $\bar{X}$, we can define a test statistic that measures the distance between the hypothesized value of μ (denoted $\mu_0$) and the sample mean (determined by the data) in standard deviation units:

```{admonition} Test Statistic for the z-Test for the Population Mean
:class: note

$$z=\frac{\bar{x}-\mu_{0}}{\sigma/\sqrt{n}}$$
```

```{admonition} Comments
:class: important

1. Note that our test statistic (because it is a z-score) tells us how far $\bar{x}$ is from the null value $\mu_0$, measured in standard deviations. Since $\bar{x}$ represents the data and $\mu_0$ represents the null hypothesis, the test statistic is a measure of how different our data are from what is claimed in the null hypothesis. The larger the test statistic (in magnitude), the more evidence we have against $H_0$, since what we saw in our data is very different from what $H_0$ claims.

2. All inference procedures are based on probability. We are trying to determine if our sample results are likely or unlikely based on our assumptions about the population. This requires a probability model that describes the long-term behavior of sample results randomly collected from a population that fits our hypothesis. For this reason, the Central Limit Theorem gives us criteria for deciding if the z-test for the population mean can be used. We need to verify that (i) the sample is random (or at least can be considered random in context), and (ii) we are in one of the "OK" situations in the following table:

   | Conditions: z-test for a population mean | Small sample size | Large sample size |
   | --- | --- | --- |
   | Variable varies normally in the population | OK | OK |
   | Variable doesn't vary normally in the population | NOT OK | OK |

3. If the conditions are met, then $\bar{X}$ values vary normally, or at least close enough to normally to use a normal model to calculate probabilities. When $\bar{X}$ values are normal, the z-scores will be normally distributed with a mean of 0 and a standard deviation of 1.
```

Let's go back to our examples.

:::{admonition} Example 1: SAT-M Scores at Ross College
:class: tip

Recall: $H_0: \mu = 500$ vs. $H_a: \mu > 500$; n = 4; $\bar{x} = 550$; σ = 100.

Let's start by checking the conditions:

1. The sample is random.
2. The variable of interest, SAT-M scores, is assumed to vary normally in the population, so the fact that the sample size is small (n = 4) is not a problem ("variable varies normally, small sample size"—OK). Sample means will be normally distributed, and we can use a normal probability model based on z-scores to determine probabilities.

The sample mean is $\bar{x}=550$, and so the test statistic is:

$$z=\frac{550-500}{\frac{100}{\sqrt{4}}}=1$$

This means that our data (represented by the sample mean) are only 1 standard deviation above the null value (500). Clearly, this provides some evidence against $H_0$, but is this strong enough evidence to reject it? Probably not. This will be confirmed when we find the p-value.
:::

:::{admonition} Example 2: Concentration of a Chemical in a Drug
:class: tip

Recall: $H_0: \mu = 250$ vs. $H_a: \mu \neq 250$; n = 100; $\bar{x} = 247$; σ = 12.

In this case, the conditions that allow us to carry out the z-test are met since:

1. The sample is random.
2. The sample size (n = 100) is large enough for the Central Limit Theorem to apply ("variable doesn't necessarily vary normally, large sample size"—OK; note that in this case the large sample is essential, since the concentration level is not known to vary normally).

The z-statistic in this case is:

$$z=\frac{247-250}{\frac{12}{\sqrt{100}}}=-2.5$$

Our data (represented by the sample mean concentration level, 247) are 2.5 standard deviations below the null value. A difference of 2.5 standard deviations is considered quite strong evidence against $H_0$. (Essentially any difference that is above 2 standard deviations is considered quite large.) This will be confirmed when we find the p-value of the test.
:::

```{note} Video
[Test for Mean](https://www.youtube.com/watch?v=9WT3tK3o3mY)
```

## Learn By Doing

Normal body temperature for healthy, at-rest human beings has long been said to be 98.6°F. A doctor has seen many patients who had a lower or higher body temperature when they were not ill. He has read research that says it is actually lower. So he collected 50 randomly selected temperatures, which had a mean of 98.4°F. The standard deviation is known to be 0.35°F. He tests $H_0: \mu = 98.6$ vs. $H_a: \mu \neq 98.6$.

:::{quiz} Are the conditions for the z-test met, and what is the test statistic?
:hint: n = 50 > 30, and z = (98.4 − 98.6)/(0.35/√50).
:feedback-0: Correct! The sample is random and n = 50 is large enough for the CLT, so the test is safe. z = −0.2/0.0495 ≈ −4.04.
:feedback-1: Check the standard error: 0.35/√50 ≈ 0.0495, so z ≈ −4.04, not −0.57.
:feedback-2: The large sample size (50 > 30) means normality of body temperatures is not required.
* *Conditions are met; z ≈ −4.04
* Conditions are met; z ≈ −0.57
* Conditions are not met because we don't know that body temperature is normally distributed
:::

:::{quiz} A test statistic of z ≈ −4.04 means the sample mean is more than 4 standard deviations below 98.6. What should the doctor anticipate about the p-value?
:hint: How much area lies more than 4 standard deviations from the center of a normal curve?
:feedback-0: Correct! Values beyond ±4 standard deviations are extremely rare under H₀, so the p-value will be tiny (about 0.00005) and the result highly significant.
:feedback-1: It's the opposite—the more extreme the test statistic, the SMALLER the p-value.
* *The p-value will be very small—strong evidence that mean body temperature differs from 98.6°F
* The p-value will be large, since the test statistic is negative
:::

## Did I Get This?

Each histogram below represents a random sample. We do not know if the variable is distributed normally in the population, but we want to be reasonably sure that the distribution of sample means will be normal so that we can use the z-test for testing claims about the population mean.

:::{quiz} A histogram of a sample of n = 15 observations is clearly skewed to the right, suggesting the variable may not be normal in the population. How should we proceed with a z-test for μ?
:hint: Small sample + variable that doesn't appear to vary normally—check the conditions table.
:feedback-0: Correct! With a small sample (15 < 30) and evidence of non-normality, we are in the "NOT OK" cell—sample means can't be assumed normal, so the z-test should not be used.
:feedback-1: 15 is well below the n > 30 guideline, so the CLT cannot rescue us here.
:feedback-2: The skewed histogram suggests the population is NOT normal, so we cannot rely on that condition.
* *Do not use the z-test—the sample is small and the variable does not appear to vary normally
* Use the z-test—the Central Limit Theorem applies
* Use the z-test—the histogram shows the population is normal enough
:::

:::{quiz} A histogram of a sample of n = 250 observations is moderately skewed. How should we proceed with a z-test for μ?
:hint: What does the CLT say for large samples?
:feedback-0: Correct! With n = 250, the Central Limit Theorem guarantees that sample means are approximately normal even though the variable itself is skewed—the z-test is fine.
:feedback-1: Normality of the VARIABLE isn't required when the sample is large; the CLT ensures the sample MEAN is approximately normal.
* *Use the z-test—the sample is large enough for the Central Limit Theorem to apply
* Do not use the z-test—the variable is skewed
:::
