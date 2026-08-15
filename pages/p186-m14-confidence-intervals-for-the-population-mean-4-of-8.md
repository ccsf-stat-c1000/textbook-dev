# The Structure of a Confidence Interval

So far, we've developed the confidence interval for the population mean from scratch, based on results from probability, and discussed the trade-off between the level of confidence and the precision of the interval. The price you pay for a higher level of confidence is a lower level of precision of the interval (i.e., a wider interval).

Is there a way to bypass this trade-off? In other words, is there a way to increase the precision of the interval (i.e., make it narrower) *without* compromising on the level of confidence? We will answer this question shortly, but first we need to get a deeper understanding of the different components of the confidence interval and its structure.

## Understanding the General Structure of Confidence Intervals

We explored the confidence interval for $\mu$ for different levels of confidence and found that, in general, it has the following form:

$$\bar{x} \pm z^{*}\cdot\frac{\sigma}{\sqrt{n}}$$

where z\* is a general notation for the multiplier that depends on the level of confidence. As we discussed before:

- For a 90% level of confidence, z\* = 1.645
- For a 95% level of confidence, z\* = 2 (or 1.96 if you want to be really precise)
- For a 99% level of confidence, z\* = 2.576

To start our discussion about the structure of the confidence interval, let's denote the quantity $z^{*}\cdot\frac{\sigma}{\sqrt{n}}$ by m. The confidence interval, then, has the form: $\bar{x} \pm m$, where:

- $\bar{x}$ is the sample mean, the point estimator for the unknown population mean $(\mu)$.
- *m* is called the {term}`margin of error`, since it represents the maximum estimation error for a given level of confidence.

For example, for a 95% confidence interval, we are 95% sure that our estimate will not depart from the true population mean by more than m, the margin of error.

m is further made up of the product of two components: z\*, the confidence multiplier, and $\frac{\sigma}{\sqrt{n}}$, the standard deviation of $\bar{X}$, the point estimator of $\mu$.

Here is a summary of the different components of the confidence interval and its structure:

```{figure} images/gen/m14-ci-structure.svg
:alt: The formula x-bar plus or minus z-star times sigma over root n, annotated to show that x-bar is the point estimate and z-star times sigma over root n is the margin of error m, the product of the confidence multiplier and the standard deviation of the estimator. Below, a number line shows the interval centered at the estimate, extending a distance m on each side, for a total width of 2m.
```

This structure:

$$\text{estimate} \pm \text{margin of error}$$

where the margin of error is further composed of the product of a confidence multiplier and the standard deviation (or, as we'll see, the standard error), is the general structure of all confidence intervals that we will encounter in this course.

Obviously, even though each confidence interval has the same components, what these components actually are is different from confidence interval to confidence interval, depending on what unknown parameter the confidence interval aims to estimate.

Since the structure of the confidence interval is such that it has a margin of error on either side of the estimate, it is centered at the estimate (in our case, $\bar{x}$), and its width (or length) is exactly twice the margin of error.

The margin of error, m, is therefore "in charge" of the width (or precision) of the confidence interval, and the estimate is in charge of its location (and has no effect on the width).

## Check Your Understanding: The Structure of a Confidence Interval

:::{quiz} A 95% confidence interval for a population mean is reported as (24, 32). What are the point estimate and the margin of error?
:hint: The interval is centered at the estimate, and its total width is twice the margin of error.
:feedback-0: Correct! The center is $(24 + 32)/2 = 28$, and the margin of error is $(32 - 24)/2 = 4$.
:feedback-1: 8 is the full width of the interval; the margin of error is half of that.
:feedback-2: The estimate is the midpoint of the interval, not its lower endpoint.
* *Estimate 28, margin of error 4
* Estimate 28, margin of error 8
* Estimate 24, margin of error 8
:::
