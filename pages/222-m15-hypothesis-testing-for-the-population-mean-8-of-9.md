# Hypothesis Testing for the Population Mean (8 of 9)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 3. Finding the p-value

The p-value of the t-test is found exactly the same way as it is found for the z-test, except that the t distribution is used instead of the Zdistribution, as the figures below illustrate.

## Comment:

Even though tables exist for the different t distributions, we will only use software to do the calculation for us.

```{figure} images/image366.gif
:alt: H_a: μ &lt; μ_0 ⇒ p-value = P(t(n-1) ≤ t)

H_a: μ &lt; μ_0 ⇒ p-value = P(t(n-1) ≤ t)
```

```{figure} images/image367.gif
:alt: A t(n-1) distribution with t-scores on its horizontal axis. T-scores of 0 and t have been marked, with t to the left of 0. t has been generated from a observed test statistic. The area to the left of t under the curve is the p-value.

A t(n-1) distribution with t-scores on its horizontal axis. T-scores of 0 and t have been marked, with t to the left of 0. t has been generated from a observed test statistic. The area to the left of t under the curve is the p-value.
```

```{figure} images/image368.gif
:alt: H_a: μ &gt; μ_0 ⇒ p-value = P(t(n-1) ≥ t)

H_a: μ &gt; μ_0 ⇒ p-value = P(t(n-1) ≥ t)
```

```{figure} images/image369.gif
:alt: A t(n-1) distribution with t-scores on its horizontal axis. T-scores of 0 and t have been marked, with t to the right of 0. t has been generated from a observed test statistic. The area to the right of t under the curve is the p-value.

A t(n-1) distribution with t-scores on its horizontal axis. T-scores of 0 and t have been marked, with t to the right of 0. t has been generated from a observed test statistic. The area to the right of t under the curve is the p-value.
```

```{figure} images/image370.gif
:alt: Ha: μ ≠ μ_0 ⇒ p-value = P(t(n-1) ≤ -|t|) + P(t(n-1) ≥ |t|) = 2P(t(n-1) ≥ |t|)

Ha: μ ≠ μ_0 ⇒ p-value = P(t(n-1) ≤ -|t|) + P(t(n-1) ≥ |t|) = 2P(t(n-1) ≥ |t|)
```

```{figure} images/image371.gif
:alt: A t(n-1) distribution with t-scores on its horizontal axis. T-scores of -|t|, 0, and |t| have been marked. -|t| is to the left of 0, and |t| is to the right. t has been generated from a observed test statistic. The sum of the area under the curve to the left of -|t| and to the right of |t| is the p-value.

A t(n-1) distribution with t-scores on its horizontal axis. T-scores of -|t|, 0, and |t| have been marked. -|t| is to the left of 0, and |t| is to the right. t has been generated from a observed test statistic. The sum of the area under the curve to the left of -|t| and to the right of |t| is the p-value.
```

## Comment

Note that due to the symmetry of the t distribution, for a given value of the test statistic t, the p-value for the two-sided test is twice as large as the p-value of either of the one-sided tests. The same thing happens when p-values are calculated under the t distribution as when they are calculated under the Z distribution.

## 4. Drawing Conclusions

As usual, based on the p-value (and some significance level of choice) we assess the significance of results, and draw our conclusions in context.

To summarize:

The main difference between the z-test and the t-test for the population mean is that we use the sample standard deviation s instead of the unknown population standard deviation σ. As a result, the p-values are calculated under the t distribution instead of under the Z distribution. Since we are using software, this doesn't really impact us practically. However, it is important to understand what is going on behind the scenes, and not just use the software mechanically. This is why we went through the trouble of explaining the t distribution.

We are now ready to look at two examples.
