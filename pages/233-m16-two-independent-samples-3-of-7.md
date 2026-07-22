# The Two-Sample t-Test: Conditions and Test Statistic

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 2: Check Conditions, and Summarize the Data Using a Test Statistic

The two-sample t-test can be safely used as long as the following conditions are met:

1. The two samples are indeed independent.

2. We are in one of the following two scenarios:

   - Both populations are normal—or more specifically, the distribution of the response Y in both populations is normal—and both samples are random (or at least can be considered as such). In practice, checking normality in the populations is done by looking at each of the samples using a histogram and checking whether there are any signs that the populations are not normal. Such signs could be extreme skewness and/or extreme outliers.
   - The populations are known or discovered not to be normal, but the sample size of each of the random samples is large enough (we can use the rule of thumb that n > 30 is considered large enough).

Assuming that we can safely use the two-sample t-test, we need to summarize the data, and in particular, calculate our data summary—the test statistic.

```{admonition} The Two-Sample t-Test Statistic
:class: note

$$t=\frac{(\bar{y}_{1}-\bar{y}_{2})-0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}$$

where $\bar{y}_1, \bar{y}_2$ are the sample means of the samples from population 1 and population 2 respectively; $s_1, s_2$ are the sample standard deviations of the two samples; and $n_1, n_2$ are the sample sizes of the two samples.
```

```{admonition} Comment
:class: important

Let's see why this test statistic makes sense, bearing in mind that our inference is about $\mu_1-\mu_2$:

- $\bar{y}_1$ estimates $\mu_1$ and $\bar{y}_2$ estimates $\mu_2$, and therefore $\bar{y}_1-\bar{y}_2$ is what the data tell us about (or how the data estimate) $\mu_1-\mu_2$.
- 0 is the *null value*—what the null hypothesis, $H_0$, claims that $\mu_1-\mu_2$ is.
- The denominator $\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}$ is the standard error of $\bar{y}_1-\bar{y}_2$. (We will not go into the details of why this is true.)

We therefore see that our test statistic, like the previous test statistics we encountered, has the structure

$$\frac{\text{sample estimate}-\text{null value}}{\text{standard error}}$$

and therefore, like the previous test statistics, measures (in standard errors) the difference between what the data tell us about the parameter of interest $\mu_1-\mu_2$ (sample estimate) and what the null hypothesis claims the value of the parameter is (null value).
```

:::{admonition} Example: Looks vs. Personality
:class: tip

Let's first check whether the conditions that allow us to safely use the two-sample t-test are met.

1. Here, 239 students were chosen and were naturally divided into a sample of females and a sample of males. Since the students were chosen at random, the sample of females is independent of the sample of males.

2. Here we are in the second scenario—the sample sizes (150 and 85) are definitely large enough, and so we can proceed regardless of whether the populations are normal or not.

In order to avoid tedious calculations, we use statistical software to find the test statistic. The relevant summaries of the data are:

| Group | n | Mean | Standard deviation |
| --- | --- | --- | --- |
| Females | 150 | 10.73 | 4.25 |
| Males | 85 | 13.33 | 4.02 |

And when we put it all together we get that indeed:

$$t=\frac{(\bar{y}_{1}-\bar{y}_{2})-0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}=\frac{10.73-13.33}{\sqrt{\frac{4.25^{2}}{150}+\frac{4.02^{2}}{85}}}=-4.66$$

The test statistic tells us what the data say about $\mu_1-\mu_2$. In this case, the observed difference (10.73 − 13.33) is 4.66 standard errors below what the null hypothesis claims this difference to be (0). 4.66 standard errors is quite a lot, and probably indicates that the data provide evidence against $H_0$.
:::

## Check Your Understanding: The Two-Sample t-Test Statistic

:::{quiz} In the looks vs. personality example, which quantity does y-bar₁ − y-bar₂ = −2.6 estimate?
:hint: The sample difference estimates the corresponding population quantity.
:feedback-0: Correct! The difference between the sample means estimates μ₁ − μ₂, the difference between the population means.
:feedback-1: The test statistic is the standardized version of the difference, not the difference itself.
:feedback-2: The sample difference is a point estimate—it doesn't claim the population difference is exactly −2.6.
* *The difference between the population means, μ₁ − μ₂
* The test statistic t
* The exact value of μ₁ − μ₂
:::

:::{quiz} A study compares mean commute times in two cities using independent random samples of 12 from each city. The histogram of one sample shows extreme right skew with two large outliers. Can the two-sample t-test be safely used?
:hint: Small samples require the populations to look normal.
:feedback-0: Correct! With small samples (12 < 30) and clear evidence of non-normality, neither scenario for safe use applies.
:feedback-1: 12 per group is well below the n > 30 guideline, so the CLT cannot compensate for the skewness.
:feedback-2: The independence condition may be fine, but the normality/sample-size condition fails.
* *No—the samples are small and one shows strong evidence of non-normality
* Yes—the total sample size is 24, which is large enough
* No—the samples are not independent
:::

We have completed step 2 and are ready to proceed to step 3, finding the p-value of the test.
