# Hypothesis Testing for the Population Proportion p (4 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

For the reason illustrated in the examples at the end of the previous page, the test statistic cannot simply be the difference $\hat{p}−p_{0}$, but must be some form of that formula that accounts for the sample size. In other words, we need to somehow standardize the difference $\hat{p}−p_{0}$ so that comparison between different situations will be possible. We are very close to revealing the test statistic, but before we construct it, let's be reminded of the following two facts from probability:

1. When we take a random sample of size n from a population with population proportion p, the possible values of the sample proportion $\hat{p}$ (when certain conditions are met) have approximately a normal distribution with:

* mean: p

* standard deviation: $\sqrt{\frac{p\left(1−p\right)}{n}}$

2. The z-score of a normal value (a value that comes from a normal distribution) is:

$z=\frac{value&minus;mean}{standard deviation}$

and it represents how many standard deviations below or above the mean the value is.

We are finally ready to reveal the test statistic:

The test statistic for this test measures the difference between the sample proportion $\hat{p}$ and the null value $p_{0}$ by the z-score (standardized score) of the sample proportion $\hat{p}$, assuming that the null hypothesis is true (i.e., assuming that $p=p_{0}$).

From fact 1, we know that the values of the sample proportion ($\hat{p}$) are normal, and we are given the mean and standard deviation.

Using fact 2, we conclude that the z-score of $\hat{p}$ when $p=p_{0}$ is:

$z=\frac{\hat{p}&minus;p_{0}}{\sqrt{\frac{p_{0}(1&minus;p_{0})}{n}}}$

*This is the test statistic.* It represents the difference between the sample proportion ($\hat{p}$) and the null value ($p_{0}$), measured in standard deviations.

```{figure} images/image237.gif
:alt: A normal curve representing samping distribution of p-hat assuming that p=p_0. Marked on the horizontal axis is p_0 and a particular value of p-hat. z is the difference between p-hat and p_0 measured in standard deviations (with the sign of z indicating whether p-hat is below or above p_0)

A normal curve representing samping distribution of p-hat assuming that p=p_0. Marked on the horizontal axis is p_0 and a particular value of p-hat. z is the difference between p-hat and p_0 measured in standard deviations (with the sign of z indicating whether p-hat is below or above p_0)
```

Here is a representation of the sampling distribution of $\hat{p}$, assuming p = p~0~. In other words, this is a model of how $\hat{p}$'s behave if we are drawing random samples from a population for which H~0~ is true. Notice the center of the sampling distribution is at p~0~, which is the hypothesized proportion given in the null hypothesis (H~0~: p = p~0~.) We could also mark the axis in standard deviation units, $\sqrt{\frac{p_{0}\left(1−p_{0}\right)}{n}}$. For example, if our null hypothesis claims that the proportion of U.S. adults supporting the death penalty is 0.64, then the sampling distribution is drawn as if the null is true. We draw a normal distribution centered at p = 0.64 with a standard deviation dependent on sample size, $\sqrt{\frac{0.64\left(1−0.64\right)}{n}}$.

## Important Comment

Note that under the assumption that H~0~ is true (i.e., $p=p_{0}$), the test statistic, by the nature of the fact that it is a z-score, has N(0,1) (standard normal) distribution. Another way to say the same thing which is quite common is: "The null distribution of the test statistic is N(0,1)." By "null distribution," we mean the distribution under the assumption that H~0~ is true. As we'll see and stress again later, the null distribution of the test statistic is what the calculation of the p-value is based on.

Let's go back to our three examples and find the test statistic in each case:

```{admonition} Example: 1
    ```{figure} images/image238.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still 0.20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = 0.16, and z = -2.

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still 0.20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = 0.16, and z = -2.
    ```

    Since the null hypothesis is H~0~: p = 0.20, the standardized score of $\hat{p}=.16$ is: $z=\frac{.16−.20}{\sqrt{\frac{.20\left(1−.20\right)}{400}}}=−2$.

    This is the value of the test statistic for this example.

    What does this tell me?

    This z-score of −2 tells me that (assuming that H~0~ is true) the sample proportion $\hat{p}=.16$ is 2 standard deviations below the null value (0.20).
```

```{admonition} Example: 2
    ```{figure} images/image241.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = 0.19, and z = 0.91

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = 0.19, and z = 0.91
    ```

    Since the null hypothesis is H~0~: p = 0.157, the standardized score of $\hat{p}=.19$ is: $z=\frac{.19−.157}{\sqrt{\frac{.157\left(1−.157\right)}{100}}}\approx.91$.

    This is the value of the test statistic for this example.

    We interpret this to mean that, assuming that H~0~ is true, the sample proportion $\hat{p}=.19$ is 0.91 standard deviations above the null value (0.157).
```

```{admonition} Example: 3
    ```{figure} images/image244.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was 0.64)?&quot; We take a sample of 1000 US adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = 0.675, and z = 2.31

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was 0.64)?&quot; We take a sample of 1000 US adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = 0.675, and z = 2.31
    ```

    Since the null hypothesis is H~0~: p = 0.64, the standardized score of $\hat{p}=.675$ is: $z=\frac{.675−.64}{\sqrt{\frac{.64\left(1−.64\right)}{1000}}}\approx2.31$.

    This is the value of the test statistic for this example.

    We interpret this to mean that, assuming that H~0~ is true, the sample proportion $\hat{p}=.675$ is 2.31 standard deviations above the null value (0.64).

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

## Comments about the Test Statistic

1. We mentioned earlier that to some degree, the test statistic captures the essence of the test. In this case, the test statistic measures the difference between $\hat{p}$ and $p_{0}$ in standard deviations. This is exactly what this test is about. Get data, and look at the discrepancy between what the data estimates p to be (represented by $\hat{p}$) and what H~0~ claims about p (represented by $p_{0}$).

2. You can think about this test statistic as a measure of evidence in the data against H~0~. The larger the test statistic, the "further the data are from H~0~" and therefore the more evidence the data provide against H~0~.

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Proportion p (4 of 13)

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

The UCLA Internet Report (February 2003) estimated that a proportion of roughly 0.75 of online homes are still using dial-up access, but claimed that the use of dial-up is declining. Is that really the case? To examine this, a follow-up study was conducted a year later in which, out of a random sample of 1,308 households that had Internet access, 804 were connecting using a dial-up modem.

Let p be the proportion of all U.S. Internet-using households who have dial-up access. In the previous activity, we established that the appropriate hypotheses here are:

H~0~: p = 0.75 and H~a~: p < 0.75

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Ann and Sam are both testing the hypothesis that 40% of plain M&M’s are orange, H~0~: p = 0.40. Ann draws a sample of M&M’s and 45% of her sample are orange. She calculates a test statistic of z = 1.25. Sam draws a sample of M&M’s and 50% of his sample are orange. He calculates a test statistic of z = 1.

What can we conclude? Mark each statement as true or false.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
