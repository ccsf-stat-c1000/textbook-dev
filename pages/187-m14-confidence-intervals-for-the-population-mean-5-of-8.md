# Confidence Intervals for the Population Mean (5 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

Let us now go back to the confidence interval for the mean, and more specifically, to the question that we posed at the beginning of the previous page:

Is there a way to increase the precision of the confidence interval (i.e., make it narrower) *without* compromising on the level of confidence?

Since the width of the confidence interval is a function of its margin of error, let's look closely at the margin of error of the confidence interval for the mean and see how it can be reduced:

$z^{\times}\times\frac{\sigma}{\sqrt{n}}$

Since z* controls the level of confidence, we can rephrase our question above in the following way:

Is there a way to reduce this margin of error other than by reducing z*?

If you look closely at the margin of error, you'll see that the answer is yes. We can do that by increasing the sample size n (since it appears in the denominator).

```{note}
    **Many Students Wonder**

    Confidence Intervals for the Population Mean

    *(Interactive activity — available in the OLI platform)*
```

Let's look at an example first and then explain why increasing the sample size is a way to increase the precision of the confidence interval *without* compromising on the level of confidence.

```{admonition} Example
    Recall the IQ example:

    The IQ level of students at a particular university has an unknown mean (μ) and a known standard deviation of $\sigma=15$. A simple random sample of 100 students is found to have the sample mean IQ $\bar{x}=115$. A 95% confidence interval for μ in this case is:

    $\bar{x}\pm2\frac{\sigma}{\sqrt{n}}=115\pm2\left(\frac{15}{\sqrt{100}}\right)=115\pm3.0=\left(112, 118\right)$

    Note that the margin of error is m = 3, and therefore the width of the confidence interval is 6.

    Now, what if we change the problem slightly by increasing the sample size, and assume that it was 400 instead of 100?

    ```{figure} images/image067.gif
    :alt: A large circle represents the Population of all Students at SU. We are interested in the variable IQ, and the unknown parameter is μ, the population mean IQ level. In addition, we know that σ = 15. From this population we create a sample of size n=400, represented by a smaller circle. In this sample, we find that x bar = 115.

    A large circle represents the Population of all Students at SU. We are interested in the variable IQ, and the unknown parameter is μ, the population mean IQ level. In addition, we know that σ = 15. From this population we create a sample of size n=400, represented by a smaller circle. In this sample, we find that x bar = 115.
    ```

    In this case, the 95% confidence interval for μ is:

    $\bar{x}\pm2\frac{\sigma}{\sqrt{n}}=115\pm2\left(\frac{15}{\sqrt{400}}\right)=115\pm1.5=\left(113.5, 116.5\right)$

    The margin of error here is only m = 1.5, and thus the width is only 3.

    Note that for the same level of confidence (95%) we now have a narrower, and thus more precise, confidence interval.
```

Let's try to understand why a larger sample size will reduce the margin of error for a fixed level of confidence. There are three ways to explain it: mathematically, using probability theory, and intuitively.

We've already alluded to the mathematical explanation; the margin of error is $z^{*}\times\frac{\sigma}{\sqrt{n}}$, and since n, the sample size, appears in the denominator, increasing n will reduce the margin of error.

As we saw in our discussion about point estimates, probability theory tells us that

```{figure} images/image069.gif
:alt: Two sampling distribution curves for x-bar. One is squished down and wider, while the other is much taller and narrower. Both curves share the same μ. The tall, narrow distribution was based on a larger sample size, which has a smaller standard deviation, and so is less spread out. This means that values of x-bar are more likely to be closer to μ when the sample size is larger.

Two sampling distribution curves for x-bar. One is squished down and wider, while the other is much taller and narrower. Both curves share the same μ. The tall, narrow distribution was based on a larger sample size, which has a smaller standard deviation, and so is less spread out. This means that values of x-bar are more likely to be closer to μ when the sample size is larger.
```

This explains why with a larger sample size the margin of error (which represents how far apart we believe $\bar{x}$ might be from μ for a given level of confidence) is smaller.

On an intuitive level, if our estimate $\bar{x}$ is based on a larger sample (i.e., a larger fraction of the population), we have more faith in it, or it is more reliable, and therefore we need to account for less error around it.

## Comment

While it is true that for a given level of confidence, increasing the sample size increases the precision of our interval estimation, in practice, increasing the sample size is not always possible. Consider a study in which there is a non-negligible cost involved for collecting data from each participant (an expensive medical procedure, for example). If the study has some budgetary constraints, which is usually the case, increasing the sample size from 100 to 400 is just not possible in terms of cost-effectiveness. Another instance in which increasing the sample size is impossible is when a larger sample is simply not available, even if we had the money to afford it. For example, consider a study on the effectiveness of a drug on curing a very rare disease among children. Since the disease is rare, there are a limited number of children who could be participants. This is the reality of statistics. Sometimes theory collides with reality, and you just do the best you can.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
