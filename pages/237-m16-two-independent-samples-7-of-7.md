# Connecting the Interval and the Test

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

As we've seen in previous tests, the 95% confidence interval for $\mu_1-\mu_2$ can be used for testing in the two-sided case ($H_0: \mu_1-\mu_2=0$ vs. $H_a: \mu_1-\mu_2\neq0$):

- If the null value, 0, falls *outside* the confidence interval, $H_0$ is rejected.
- If the null value, 0, falls *inside* the confidence interval, $H_0$ is not rejected.

:::{admonition} Example: Looks vs. Personality
:class: tip

Let's go back to our leading example of the looks vs. personality score, where we had a two-sided test. Software told us that the 95% confidence interval for $\mu_1-\mu_2$ is (−3.696, −1.496), and that the p-value is essentially 0.

We used the fact that the p-value is so small to conclude that $H_0$ can be rejected. We can also use the confidence interval to reach the same conclusion, since 0 falls outside the confidence interval. In other words, since 0 is not a plausible value for $\mu_1-\mu_2$, we can reject $H_0$, which claims that $\mu_1-\mu_2=0$.
:::

## Did I Get This?

Below you'll find three sample outputs of the two-sided two-sample t-test ($H_0: \mu_1-\mu_2=0$ vs. $H_a: \mu_1-\mu_2\neq0$). Only one of the outputs could be correct—the other two contain an inconsistency. Your task is to decide which output is the correct one. (*Hint:* no calculations are necessary; pay attention to the p-value and confidence interval.)

- *Output A:* p-value: 0.289; 95% confidence interval: (−5.931, −1.786)
- *Output B:* p-value: 0.003; 95% confidence interval: (−13.974, 2.897)
- *Output C:* p-value: 0.223; 95% confidence interval: (−9.314, 2.205)

:::{quiz} Which output is internally consistent?
:hint: A p-value below 0.05 must go with an interval that excludes 0, and a p-value above 0.05 with an interval that includes 0.
:feedback-0: Correct! In C, the p-value (0.223) is above 0.05 AND the interval contains 0—both indicate not rejecting H₀. Consistent.
:feedback-1: In A, the p-value (0.289) says "don't reject," but the interval excludes 0, which says "reject"—inconsistent.
:feedback-2: In B, the p-value (0.003) says "reject," but the interval contains 0, which says "don't reject"—inconsistent.
* *Output C
* Output A
* Output B
:::

## Let's Summarize

We have completed our discussion of the two-sample t-test for comparing two populations' means when the samples are independent. Let's summarize what we have learned.

- The two-sample t-test is used for comparing the means of a quantitative variable (Y) in two populations (which we initially called sub-populations).

- Our goal is comparing $\mu_1$ and $\mu_2$ (which in practice is done by making inference on the difference $\mu_1-\mu_2$). The null hypothesis is $H_0: \mu_1-\mu_2=0$, and the alternative hypothesis is one of the following (depending on the context of the problem): $H_a: \mu_1-\mu_2<0$, or $H_a: \mu_1-\mu_2>0$, or $H_a: \mu_1-\mu_2\neq0$.

- The two-sample t-test can be safely used when the samples are independent and at least one of the following two conditions holds: the variable Y is known to have a normal distribution in both populations, or the two sample sizes are large. When the sample sizes are not large (and we therefore need to check the normality of Y in both populations), what we do in practice is look at the histograms of the two samples and make sure that there are no signs of non-normality such as extreme skewness and/or outliers.

- The test statistic is

  $$t=\frac{(\bar{y}_{1}-\bar{y}_{2})-0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}$$

  and has a t distribution when the null hypothesis is true.

- P-values are obtained from the software output, and conclusions are drawn as usual, comparing the p-value to the significance level α.

- If $H_0$ is rejected, a 95% confidence interval for $\mu_1-\mu_2$ can be very insightful, and can also be used for the two-sided test.

## Reflection

Think of a question in your own field of interest that compares two groups on a quantitative outcome. Identify the explanatory and response variables, state the hypotheses, and note whether the samples would be independent or paired.
