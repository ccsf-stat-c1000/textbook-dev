# Matched Pairs (4 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 2: Checking Conditions and Calculating the Test Statistic

The paired t-test, as a special case of a one-sample t-test, can be safely used as long as:

1. The sample of differences is random (or at least can be considered so in
                    context).
2. We are in one of the three situations marked with a green check mark in the
                    following table

```{figure} images/image074.gif
:alt: A table which has two columns and two rows. The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally" and "Variable doesn't vary normally." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally, Small sample size: OK (in this case, we should check normality visually using a histogram of the sample differences); Variable varies normally, Large sample size: OK; Variable doesn't vary normally, Small sample size: NOT OK; Variable doesn't vary normally, Large sample size: OK;

A table which has two columns and two rows. The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally" and "Variable doesn't vary normally." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally, Small sample size: OK (in this case, we should check normality visually using a histogram of the sample differences); Variable varies normally, Large sample size: OK; Variable doesn't vary normally, Small sample size: NOT OK; Variable doesn't vary normally, Large sample size: OK;
```

In other words, in order to use the paired t-test safely, the differences should vary normally unless the sample size is large, in which case it is safe to use the paired t-test regardless of whether the differences vary normally or not. As we indicated in the figure above (and have seen many times already), in practice, normality is checked by looking at the histogram of differences and as long as no clear violation of normality (such as extreme skewness and/or outliers) is apparent, normality is assumed. Assuming that the we can safely use the paired t-test, the data are summarized by a test statistic:

$t=\frac{\bar{x_{d}}−0}{\frac{s_{d}}{\sqrt{n}}}$

where $\bar{x_{d}}$ is the sample mean of the differences, and $s_{d}$ is the sample standard deviation of the differences. This is the test statistic we've developed for the one sample t-test (with $\mu_{0}=0$ ), and has the same conceptual interpretation; it measures (in standard errors) how far our data are (represented by the average of the differences) from the null hypothesis (represented by the null value, 0).

```{admonition} Example
    Let's first check whether we can safely proceed with the paired t-test, by checking the two conditions.

    1. The sample of drivers was chosen at random.
    2. The sample size is not large enough (n = 20), so in order to proceed, we
                            need to look at the histogram of the differences and make sure there is no
                            evidence that the normality assumption is not met. Here is the
                            histogram:

    There is no evidence of violation of the normality assumption (on the contrary, the histogram looks quite normal).

    Also note that the vast majority of the differences are negative (i.e., the total reaction times for most of the drivers are larger after the two beers), suggesting that the data provide evidence against the null hypothesis.

    The question (which the p-value will answer) is whether these data provide strong enough evidence or not. We can safely proceed to calculate the test statistic (which in practice we leave to the software to calculate for us).

    Here is the output of the paired t-test for our example:

    ```{figure} images/image173_excel.gif
    :alt: n = 20, mean difference = -0.501500, stdev difference = 0.868600, t-value = -2.58

    n = 20, mean difference = -0.501500, stdev difference = 0.868600, t-value = -2.58
    ```

    According to the output, the test statistic is -2.58, indicating that the data (represented by the sample mean of the differences) are 2.58 standard errors below the null hypothesis (represented by the null value, 0). Note in the output, that beyond the test statistic itself, we also highlighted the part of the output that provides the ingredients needed in order to calculate it: $n=20, \bar{x_{d}}=−0.5015, s_{d}=0.8686$. Indeed $\frac{−0.5015}{\frac{0.8686}{\sqrt{20}}}=−2.58$.
```
