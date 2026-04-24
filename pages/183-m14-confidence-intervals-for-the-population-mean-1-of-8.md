# Confidence Intervals for the Population Mean (1 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## Overview

As we mentioned in the introduction to interval estimation, we start by discussing interval estimation for the population mean μ. Here is a quick overview of how we introduce this topic.

- Learn how a 95% confidence interval for the population mean μ is constructed
                        and interpreted.
- Generalize to confidence intervals with other levels of confidence (for
                        example, what if we want a 99% confidence interval?).
- Understand more broadly the structure of a confidence interval and the
                        importance of the margin of error.
- Understand how the precision of interval estimation is affected by the
                        confidence level and sample size.
- Learn under which conditions we can safely use the methods that are
                        introduced in this section.

Recall the IQ example:

```{admonition} Example
    Suppose that we are interested in studying the IQ levels of students at Smart University (SU). In particular (since IQ level is a quantitative variable), we are interested in estimating μ, the mean IQ level of all the students at SU.

    We will assume that from past research on IQ scores in different universities, it is known that the IQ standard deviation in such populations is $\sigma=15$. In order to estimate μ , a random sample of 100 SU students was chosen, and their (sample) mean IQ level is calculated (let's not assume, for now, that the value of this sample mean is 115, as before).

    We will now show the rationale behind constructing a 95% confidence interval for the population mean μ.

    * We learned in the "Sampling Distributions" module of probability that according to the central limit theorem, the sampling distribution of the sample mean $\bar{X}$ is approximately normal with a mean of μ and standard deviation of $\frac{\sigma}{\sqrt{n}}$. In our example, then, (where $\sigma=15$ and n=100), the possible values of $\bar{X}$, the sample mean IQ level of 100 randomly chosen students, is approximately normal, with mean μ and standard deviation $\frac{15}{\sqrt{100}}=1.5$.

    * Next, we recall and apply the Standard Deviation Rule for the normal distribution, and in particular its second part:

    There is a 95% chance that the sample mean we get in our sample falls within 2 * 1.5 = 3 of μ.

    ```{figure} images/2_iq.png
    :alt: A distribution curve with a horizontal axis labeled "X bar." The curve is centered at X-bar=μ, and marked on the axis is μ+3 and μ-3. There is a 95% chance that any x-bar will fall between μ-3 and μ+3.

    A distribution curve with a horizontal axis labeled "X bar." The curve is centered at X-bar=μ, and marked on the axis is μ+3 and μ-3. There is a 95% chance that any x-bar will fall between μ-3 and μ+3.
    ```

    * Obviously, if there is a certain distance between the sample mean and the population mean, we can describe that distance by starting at either value. So, if the sample mean ($\bar{x}$) falls within a certain distance of the population mean μ, then the population mean μ falls within the same distance of the sample mean.

    Therefore, the statement, "There is a 95% *chance* that the *sample* mean $\bar{x}$ falls within 3 units of μ" can be rephrased as: "We are 95% *confident* that the *population* mean μ falls within 3 units of $\bar{x}$."

    So, if we happen to get a sample mean of $\bar{x}=115$, then we are 95% sure that μ falls within 3 of 115, or in other words that μ is covered by the interval (115 - 3, 115 + 3) = (112,118).

    (On later pages, we will use similar reasoning to develop a general formula for a confidence interval.)
```

## Comment

Note that the first phrasing is about $\bar{x}$, which is a random variable; that's why it makes sense to use probability language. But the second phrasing is about μ, which is a parameter, and thus is a "fixed" value that doesn’t change, and that's why we shouldn’t use probability language to discuss it. This point will become clearer after you do the activities on the next page.
