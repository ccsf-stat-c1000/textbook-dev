# Margin of Error and the Precision of an Interval

```{admonition} Learning Objectives
:class: note

- Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
- Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

Let us now go back to the confidence interval for the mean, and more specifically, to the question that we posed at the beginning of the previous page:

Is there a way to increase the precision of the confidence interval (i.e., make it narrower) *without* compromising on the level of confidence?

Since the width of the confidence interval is a function of its margin of error, let's look closely at the margin of error of the confidence interval for the mean and see how it can be reduced:

$$m = z^{*}\cdot\frac{\sigma}{\sqrt{n}}$$

Since z\* controls the level of confidence, we can rephrase our question above in the following way:

Is there a way to reduce this margin of error other than by reducing z\*?

If you look closely at the margin of error, you'll see that the answer is yes. We can do that by increasing the sample size n (since it appears in the denominator).

:::{admonition} Example: Quadrupling the Sample
:class: tip

Recall the IQ example:

The IQ level of students at a particular university has an unknown mean (μ) and a known standard deviation of $\sigma=15$. A simple random sample of 100 students is found to have the sample mean IQ $\bar{x}=115$. A 95% confidence interval for μ in this case is:

$$115\pm2\left(\frac{15}{\sqrt{100}}\right)=115\pm3.0=(112,\ 118)$$

Note that the margin of error is m = 3, and therefore the width of the confidence interval is 6.

Now, what if we change the problem slightly by increasing the sample size, and assume that it was 400 instead of 100?

In this case, the 95% confidence interval for μ is:

$$115\pm2\left(\frac{15}{\sqrt{400}}\right)=115\pm1.5=(113.5,\ 116.5)$$

The margin of error here is only m = 1.5, and thus the width is only 3.

Note that for the same level of confidence (95%) we now have a narrower, and thus more precise, confidence interval.
:::

Let's try to understand why a larger sample size will reduce the margin of error for a fixed level of confidence. There are three ways to explain it: mathematically, using probability theory, and intuitively.

We've already alluded to the mathematical explanation: the margin of error is $z^{*}\cdot\frac{\sigma}{\sqrt{n}}$, and since n, the sample size, appears in the denominator, increasing n will reduce the margin of error.

As we saw in our discussion about point estimates, probability theory tells us that the sampling distribution of $\bar{X}$ is less spread out for larger samples:

```{figure} images/gen/m14-sample-size-precision.svg
:alt: Two sampling distribution curves for the sample mean, both centered at the population mean. The curve from the larger sample size is tall and narrow, so its sample means are much more likely to be close to the population mean than those from the smaller sample.
```

This explains why with a larger sample size the margin of error (which represents how far apart we believe $\bar{x}$ might be from μ for a given level of confidence) is smaller.

On an intuitive level, if our estimate $\bar{x}$ is based on a larger sample (i.e., a larger fraction of the population), we have more faith in it, or it is more reliable, and therefore we need to account for less error around it.

## Comment

While it is true that for a given level of confidence, increasing the sample size increases the precision of our interval estimation, in practice, increasing the sample size is not always possible. Consider a study in which there is a non-negligible cost involved for collecting data from each participant (an expensive medical procedure, for example). If the study has some budgetary constraints, which is usually the case, increasing the sample size from 100 to 400 is just not possible in terms of cost-effectiveness. Another instance in which increasing the sample size is impossible is when a larger sample is simply not available, even if we had the money to afford it. For example, consider a study on the effectiveness of a drug on curing a very rare disease among children. Since the disease is rare, there are a limited number of children who could be participants. This is the reality of statistics. Sometimes theory collides with reality, and you just do the best you can.

## Concept Check

:::{quiz} A 95% confidence interval based on n = 100 has margin of error 3. If everything else stays the same, what margin of error would a sample of n = 900 give?
:hint: The margin of error scales as 1/√n; the sample is 9 times larger.
:feedback-0: Correct! √900/√100 = 3, so the margin of error shrinks by a factor of 3: from 3 to 1.
:feedback-1: Dividing by 9 would be right if n appeared without the square root; it's 1/√n.
:feedback-2: Increasing the sample size DECREASES the margin of error.
* *1
* 1/3
* 9
:::
