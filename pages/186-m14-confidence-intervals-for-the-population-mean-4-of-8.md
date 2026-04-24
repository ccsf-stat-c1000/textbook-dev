# Confidence Intervals for the Population Mean (4 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

So far, we've developed the confidence interval for the population mean from scratch, based on results from probability, and discussed the trade-off between the level of confidence and the precision of the interval. The price you pay for a higher level of confidence is a lower level of precision of the interval (i.e., a wider interval).

Is there a way to bypass this trade-off? In other words, is there a way to increase the precision of the interval (i.e., make it narrower) *without* compromising on the level of confidence? We will answer this question shortly, but first we need to get a deeper understanding of the different components of the confidence interval and its structure.

## Understanding the general structure of the confidence intervals

We explored the confidence interval for μ for different levels of confidenceand found that, in general, it has the following form:

$\bar{x}\pmz^{*}⋅\frac{\sigma}{\sqrt{n}}$ ,

where z* is a general notation for the multiplier that depends on the level of confidence. As we discussed before:

For a 90% level of confidence, z* = 1.645

For a 95% level of confidence, z* = 2 (or 1.96 if you want to be really precise)

For a 99% level of confidence, z* = 2.576

To start our discussion about the structure of the confidence interval, let's denote the $z^{*}⋅\frac{\sigma}{\sqrt{n}}$ formula by m.

The confidence interval, then, has the form: $\bar{x}\pmm$:

```{figure} images/image062.gif
:alt: A formula: x-bar ± z-star × σ/√n Note that z-star × σ/√n is m.

A formula: x-bar ± z-star × σ/√n Note that z-star × σ/√n is m.
```

$\bar{x}$ is the sample mean, the point estimator for the unknown population mean (μ).

*m* is called the *margin of error*, since it represents the maximum estimation error for a given level of confidence.

For example, for a 95% confidence interval, we are 95% sure that our estimate will not depart from the true population mean by more than m, the margin of error.

m is further made up of the product of two components:

z*, the confidence multiplier, and

$\frac{\sigma}{\sqrt{n}}$, which is the standard deviation of $\bar{X}$, the point estimator of μ.

Here is a summary of the different components of the confidence interval and its structure:

```{figure} images/image063.gif
:alt: x-bar is the point estimator. It is either added to or subtracted by the margin of error (m). The margin of error is composed of the confidence multiplier, z-star, which is multiplied by the standard deviation of the point estimator, which is σ/√n .

x-bar is the point estimator. It is either added to or subtracted by the margin of error (m). The margin of error is composed of the confidence multiplier, z-star, which is multiplied by the standard deviation of the point estimator, which is σ/√n .
```

This structure:

$estimate\pmmargin of error$ ,

where the margin of error is further composed of the product of a confidence multiplier and the standard deviation (or, as we'll see, the standard error) is the general structure of all confidence intervals that we will encounter in this course.

Obviously, even though each confidence interval has the same components, what these components actually are is different from confidence interval to confidence interval, depending on what unknown parameter the confidence interval aims to estimate.

Since the structure of the confidence interval is such that it has a margin of error on either side of the estimate, it is centered at the estimate (in our case, $\bar{x}$), and its width (or length) is exactly twice the margin of error:

```{figure} images/image065.gif
:alt: A number line, on which the estimate has been placed. To the left and to the right are two intervals with the size m. So, the confidence interval, which comprises of both margins of errors (the left one and right one) is of width 2m.

A number line, on which the estimate has been placed. To the left and to the right are two intervals with the size m. So, the confidence interval, which comprises of both margins of errors (the left one and right one) is of width 2m.
```

The margin of error, m, is therefore "in charge" of the width (or precision) of the confidence interval, and the estimate is in charge of its location (and has no effect on the width).

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
