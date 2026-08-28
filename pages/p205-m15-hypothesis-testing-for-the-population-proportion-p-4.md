# The Test Statistic for a Proportion

For the reason illustrated in the examples at the end of the previous page, the test statistic cannot simply be the difference $\hat{p}-p_{0}$, but must be some form of that formula that accounts for the sample size. In other words, we need to somehow standardize the difference $\hat{p}-p_{0}$ so that comparison between different situations will be possible. We are very close to revealing the test statistic, but before we construct it, let's be reminded of the following two facts from probability:

1. When we take a random sample of size n from a population with population proportion p, the possible values of the sample proportion $\hat{p}$ (when certain conditions are met) have approximately a normal distribution with mean p and standard deviation $\sqrt{\frac{p(1-p)}{n}}$.

2. The z-score of a normal value (a value that comes from a normal distribution) is

   $$z=\frac{\text{value}-\text{mean}}{\text{standard deviation}}$$

   and it represents how many standard deviations below or above the mean the value is.

We are finally ready to reveal the test statistic:

The test statistic for this test measures the difference between the sample proportion $\hat{p}$ and the null value $p_0$ by the z-score (standardized score) of the sample proportion $\hat{p}$, assuming that the null hypothesis is true (i.e., assuming that $p=p_0$).

From fact 1, we know that the values of the sample proportion ($\hat{p}$) are normal, and we are given the mean and standard deviation. Using fact 2, we conclude that the z-score of $\hat{p}$ when $p=p_0$ is:

```{admonition} Test Statistic for the z-Test for the Population Proportion
:class: note

$$z=\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}}$$

It represents the difference between the sample proportion ($\hat{p}$) and the null value ($p_0$), measured in standard deviations.
```

```{figure} images/gen/m15-null-distribution.svg
:alt: A normal curve representing the sampling distribution of p-hat assuming that p equals p-zero. Marked on the horizontal axis are p-zero at the center and a particular value of p-hat. z is the difference between p-hat and p-zero measured in standard deviations, with the sign of z indicating whether p-hat is below or above p-zero.
```

Here is a representation of the sampling distribution of $\hat{p}$, assuming $p = p_0$. In other words, this is a model of how $\hat{p}$ behaves if we are drawing random samples from a population for which $H_0$ is true. Notice the center of the sampling distribution is at $p_0$, which is the hypothesized proportion given in the null hypothesis ($H_0: p = p_0$). We could also mark the axis in standard deviation units, $\sqrt{\frac{p_{0}(1-p_{0})}{n}}$. For example, if our null hypothesis claims that the proportion of U.S. adults supporting the death penalty is 0.64, then the sampling distribution is drawn as if the null is true. We draw a normal distribution centered at $p = 0.64$ with a standard deviation dependent on sample size, $\sqrt{\frac{0.64(1-0.64)}{n}}$.

## Computing the Test Statistic

Note that under the assumption that $H_0$ is true (i.e., $p=p_0$), the test statistic, by the nature of the fact that it is a z-score, has the $N(0,1)$ (standard normal) distribution. Another way to say the same thing, which is quite common, is: "The null distribution of the test statistic is $N(0,1)$." By "null distribution," we mean the distribution under the assumption that $H_0$ is true. As we'll see and stress again later, the null distribution of the test statistic is what the calculation of the p-value is based on.

Let's go back to our three examples and find the test statistic in each case:

:::{admonition} Example 1: Defective Products
:class: tip

Since the null hypothesis is $H_0: p = 0.20$, the standardized score of $\hat{p}=0.16$ is:

$$z=\frac{0.16-0.20}{\sqrt{\frac{0.20(1-0.20)}{400}}}=-2$$

This is the value of the test statistic for this example.

What does this tell us? This z-score of -2 tells us that (assuming that $H_0$ is true) the sample proportion $\hat{p}=0.16$ is 2 standard deviations below the null value (0.20).
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

Since the null hypothesis is $H_0: p = 0.157$, the standardized score of $\hat{p}=0.19$ is:

$$z=\frac{0.19-0.157}{\sqrt{\frac{0.157(1-0.157)}{100}}}\approx0.91$$

This is the value of the test statistic for this example.

We interpret this to mean that, assuming that $H_0$ is true, the sample proportion $\hat{p}=0.19$ is 0.91 standard deviations above the null value (0.157).
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

Since the null hypothesis is $H_0: p = 0.64$, the standardized score of $\hat{p}=0.675$ is:

$$z=\frac{0.675-0.64}{\sqrt{\frac{0.64(1-0.64)}{1000}}}\approx2.31$$

This is the value of the test statistic for this example.

We interpret this to mean that, assuming that $H_0$ is true, the sample proportion $\hat{p}=0.675$ is 2.31 standard deviations above the null value (0.64).
:::

```{admonition} Comments About the Test Statistic
:class: important

1. We mentioned earlier that to some degree, the test statistic captures the essence of the test. In this case, the test statistic measures the difference between $\hat{p}$ and $p_0$ in standard deviations. This is exactly what this test is about. Get data, and look at the discrepancy between what the data estimate p to be (represented by $\hat{p}$) and what $H_0$ claims about p (represented by $p_0$).

2. You can think about this test statistic as a measure of evidence in the data against $H_0$. The larger the test statistic (in absolute value), the "further the data are from $H_0$" and therefore the more evidence the data provide against $H_0$.
```

## Check Your Understanding: Interpreting the Test Statistic

:::{quiz} In the death penalty example, the test statistic was $z = 2.31$. Which is the correct interpretation of this value?
:hint: A z-score counts standard deviations from the center of the null distribution.
:feedback-0: Correct! Assuming $H_0$ is true (p = 0.64), the observed sample proportion 0.675 lies 2.31 standard deviations above the null value.
:feedback-1: The test statistic is measured in standard deviations, not percentage points.
:feedback-2: z is not a probability—the p-value (a probability) will be derived from it in the next step.
* *The sample proportion is 2.31 standard deviations above the null value, assuming $H_0$ is true
* The sample proportion is 2.31 percentage points above the null value
* There is a 2.31% chance that $H_0$ is true
:::

## Check Your Understanding: The Test Statistic in Context

The UCLA Internet Report (February 2003) estimated that a proportion of roughly 0.75 of online homes were still using dial-up access, but claimed that the use of dial-up was declining. To examine this, a follow-up study was conducted a year later in which, out of a random sample of 1,308 households that had Internet access, 804 were connecting using a dial-up modem.

Let p be the proportion of all U.S. Internet-using households that have dial-up access. In the previous activity, we established that the appropriate hypotheses here are $H_0: p = 0.75$ and $H_a: p < 0.75$.

:::{quiz} What is the sample proportion p-hat in this study?
:hint: 804 out of 1,308.
:feedback-0: Correct! p-hat = $804/1308 \approx 0.615$.
:feedback-1: 0.75 is the null value from the earlier report, not the sample result.
:feedback-2: Divide the number of dial-up households by the total sample size.
* *0.615
* 0.75
* 804
:::

:::{quiz} The test statistic for these data is approximately $z = -11.3$. What does this value tell us?
:hint: How surprising is a sample proportion more than 11 standard deviations below the null value?
:feedback-0: Correct! The sample proportion is more than 11 standard deviations BELOW 0.75—essentially impossible if $H_0$ were true—so the data provide overwhelming evidence that dial-up use declined.
:feedback-1: A negative z simply means p-hat is below the null value—which is exactly the direction the alternative predicts.
:feedback-2: The magnitude matters: 11.3 standard deviations is an enormous discrepancy, providing extremely strong evidence against $H_0$.
* *The sample proportion is 11.3 standard deviations below 0.75—extremely strong evidence that dial-up use declined
* The negative sign means the test was done incorrectly
* The evidence against $H_0$ is weak because z is negative
:::

Ann and Sam are both testing the hypothesis that 40% of plain M&M's are orange, $H_0: p = 0.40$. Ann draws a sample of M&M's and 45% of her sample are orange; she calculates a test statistic of $z = 1.25$. Sam draws a sample of M&M's and 50% of his sample are orange; he calculates a test statistic of $z = 1$.

:::{quiz-multi} Which of the following statements are true? (Select all that apply.)
:hint: The test statistic already accounts for sample size—compare the z values, not the raw percentages. And if Sam's larger difference gave a SMALLER z, what must be true of his standard error?
:feedback-0: True! Evidence is measured by the test statistic, and Ann's |z| = 1.25 exceeds Sam's |z| = 1.
:feedback-1: True! Sam's difference (0.10) is larger than Ann's (0.05), yet his z is smaller—so his standard error must be larger, meaning his sample was smaller.
:feedback-2: False—raw distance from the null value doesn't determine evidence strength; the standardized distance does.
:feedback-3: False—both test statistics are positive and neither is large, so neither sample gives strong evidence; and in any case a test never proves that $H_0$ is true.
* *Ann's data provide stronger evidence against $H_0$ than Sam's, because her test statistic is larger
* *Sam's sample must be smaller than Ann's
* Sam's data provide stronger evidence against $H_0$, because his sample proportion is farther from 0.40
* Both results confirm that exactly 40% of plain M&M's are orange
:::
