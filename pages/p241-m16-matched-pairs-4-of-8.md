# The Paired t-Test: Conditions and Test Statistic

## Step 2: Checking Conditions and Calculating the Test Statistic

The paired t-test, as a special case of a one-sample t-test, can be safely used as long as:

1. The sample of differences is random (or at least can be considered so in context).
2. We are in one of the "OK" situations in the following table:

   | Conditions: paired t-test | Small sample size | Large sample size |
   | --- | --- | --- |
   | Differences vary normally | OK (check with a histogram of the sample differences) | OK |
   | Differences don't vary normally | NOT OK | OK |

In other words, in order to use the paired t-test safely, the differences should vary normally unless the sample size is large, in which case it is safe to use the paired t-test regardless of whether the differences vary normally or not. In practice, normality is checked by looking at the histogram of differences, and as long as no clear violation of normality (such as extreme skewness and/or outliers) is apparent, normality is assumed.

Assuming that we can safely use the paired t-test, the data are summarized by a test statistic:

```{admonition} Test Statistic for the Paired t-Test
:class: note

$$t=\frac{\bar{x}_{d}-0}{\frac{s_{d}}{\sqrt{n}}}$$

where $\bar{x}_d$ is the sample mean of the differences, and $s_d$ is the sample standard deviation of the differences.
```

This is the test statistic we developed for the one-sample t-test (with $\mu_0=0$), and it has the same conceptual interpretation: it measures (in standard errors) how far our data are (represented by the average of the differences) from the null hypothesis (represented by the null value, 0).

:::{admonition} Example: Drunk Drivers
:class: tip

Let's first check whether we can safely proceed with the paired t-test, by checking the two conditions.

1. The sample of drivers was chosen at random.
2. The sample size is not large (n = 20), so in order to proceed, we need to look at the histogram of the differences and make sure there is no evidence that the normality assumption is violated. In this case, the histogram of the 20 differences shows no such evidence (on the contrary, it looks quite normal).

Also note that the vast majority of the differences are negative (i.e., the total reaction times for most of the drivers are larger after the two beers), suggesting that the data provide evidence against the null hypothesis. The question (which the p-value will answer) is whether these data provide strong enough evidence or not. We can safely proceed to calculate the test statistic (which in practice we leave to the software to calculate for us).

Here is the relevant output of the paired t-test for our example:

| n | Mean of differences | StDev of differences | t |
| --- | --- | --- | --- |
| 20 | -0.5015 | 0.8686 | -2.58 |

According to the output, the test statistic is -2.58, indicating that the data (represented by the sample mean of the differences) are 2.58 standard errors below the null hypothesis (represented by the null value, 0). Note that beyond the test statistic itself, the output also provides the ingredients needed to calculate it: $n = 20$, $\bar{x}_d=-0.5015$, $s_d=0.8686$. Indeed:

$$\frac{-0.5015}{\frac{0.8686}{\sqrt{20}}}=-2.58$$
:::

## Check Your Understanding: Conditions for the Paired t-Test

:::{quiz} In a paired study with $n = 25$, the histogram of the 25 differences shows one extreme outlier and strong skewness. Can the paired t-test be safely used?
:hint: $n = 25$ is below the "large sample" guideline.
:feedback-0: Correct! With a small sample and clear evidence of non-normality in the differences, the paired t-test is not reliable.
:feedback-1: The normality check applies to the DIFFERENCES, and it fails here—with only 25 observations the CLT cannot compensate.
* *No—the sample is small and the differences show clear non-normality
* Yes—normality of the original measurements is all that matters
:::
