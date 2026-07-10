# Hypothesis Testing for the Population Mean (8 of 9)

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Step 3: Finding the P-value

The p-value of the t-test is found exactly the same way as it is found for the z-test, except that the t distribution with (n − 1) degrees of freedom is used instead of the Z distribution:

- For $H_a: \mu < \mu_0$: p-value = $P(t_{(n-1)} \leq t)$—the area under the t(n − 1) curve to the left of the observed test statistic (left-tailed).
- For $H_a: \mu > \mu_0$: p-value = $P(t_{(n-1)} \geq t)$—the area under the t(n − 1) curve to the right of the observed test statistic (right-tailed).
- For $H_a: \mu \neq \mu_0$: p-value = $P(t_{(n-1)} \leq -|t|) + P(t_{(n-1)} \geq |t|) = 2P(t_{(n-1)} \geq |t|)$—the combined area in both tails (two-tailed).

The shaded-region pictures are the same as those for the z-test (left tail, right tail, or both tails), just drawn under the t(n − 1) curve rather than the standard normal curve.

```{admonition} Comments
:class: important

1. Even though tables exist for the different t distributions, we will only use software to do the calculation for us.

2. Note that due to the symmetry of the t distribution, for a given value of the test statistic t, the p-value for the two-sided test is twice as large as the p-value of either of the one-sided tests. The same thing happens when p-values are calculated under the t distribution as when they are calculated under the Z distribution.
```

## Step 4: Drawing Conclusions

As usual, based on the p-value (and some significance level of choice) we assess the significance of the results, and draw our conclusions in context.

To summarize:

The main difference between the z-test and the t-test for the population mean is that we use the sample standard deviation s instead of the unknown population standard deviation σ. As a result, the p-values are calculated under the t distribution instead of under the Z distribution. Since we are using software, this doesn't really impact us practically. However, it is important to understand what is going on behind the scenes, and not just use the software mechanically. This is why we went through the trouble of explaining the t distribution.

## Concept Check

:::{quiz} A t-test of H₀: μ = 20 vs. Hₐ: μ > 20 based on n = 12 observations yields t = 2.1. Under which distribution is the p-value calculated?
:hint: Degrees of freedom = n − 1, and the alternative is "greater than."
:feedback-0: Correct! The p-value is the area to the right of 2.1 under the t distribution with 11 degrees of freedom.
:feedback-1: Since σ is unknown (a t-test is being used), the standard normal is not the null distribution.
:feedback-2: The degrees of freedom are n − 1 = 11, not 12.
* *The t distribution with 11 degrees of freedom (area to the right of 2.1)
* The standard normal distribution (area to the right of 2.1)
* The t distribution with 12 degrees of freedom (area to the right of 2.1)
:::

We are now ready to look at two examples.
