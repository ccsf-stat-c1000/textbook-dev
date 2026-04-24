# Hypothesis Testing for the Population Mean (7 of 9)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

Recall that we were discussing the situation of testing for a mean, in the case when sigma is unknown. We’ve seen previously that when sigma is known, the test statistic is $z=\frac{\bar{x}−\mu_{0}}{\frac{\sigma}{\sqrt{n}}}$ (note the sigma (σ) in the formula), which follows a normal distribution. But when sigma is *unknown*, the test statistic in the test for a mean becomes $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}$ (note the use of "s" in the formula, in place of the unknown sigma). *Here* is where the t-distribution arises in the context of a test for a mean, because $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}$ (with "s" in the formula in place of the unknown sigma) follows a t distribution.

Notice the only difference between the formula for the Z statistic and the formula for the t statistic: In the formula for the Z statistic, sigma (the standard deviation of the population) must be known; whereas, when sigma isn’t known, then "s" (the standard deviation of the sample data) is used in place of the unknown sigma. That’s the change that causes the statistic to be a t statistic.

Why would this single change (using "s" in place of "sigma") result in a sampling distribution that is the t distribution instead of the standard normal (Z) distribution? Remember that the t distribution is more appropriate in cases where there is more variability. So why is there more variability when s is used in place of the unknown sigma?

Well, remember that sigma (σ) is a parameter (it’s the standard deviation of the population), whose value therefore never changes. Whereas, s (the standard deviation of the sample data) varies from sample to sample, and therefore it’s another source of variation. So, using s in place of sigma causes the sampling distribution to be the t distribution because of that extra source of variation:

In the formula $z=\frac{\bar{x}−\mu_{0}}{\frac{\sigma}{\sqrt{n}}}$, the only source of variation is the sampling variability of the sample mean $\bar{X}$ (none of the other terms in that formula vary randomly in a given study);

Whereas in the formula $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}$, there are *two* sources of variation: One source is the sampling variability of the sample mean $\bar{X}$; The *other* source is the sampling variability of sample standard deviation s.

So, in a test for a mean, if sigma isn’t known, then s is used in place of the unknown sigma and that results in the test statistic being a t score.

The t score, in the context of a test for a mean, is summarized by the following figure:

```{figure} images/image365.gif
:alt: The z-score is calculated with z = ( x-bar - μ ) / [ σ/√n ]. Note that there is only one source of variation, x-bar. The standard deviation of x-bar is the denominator, σ/√n. This Z (standard normal) distribution is centered at 0, bell shaped, and has a standard devation of 1. The t-score is calculated with t = ( x-bar - μ) / [ s/√n ] . Note that the denominator, s/√n, is the standard error of x-bar. Also notice that we now have two sources of variation, x-bar and s. The t-distribution (with n-1 d.f.) is centered at zero, bell shaped, and has a larger spread.

The z-score is calculated with z = ( x-bar - μ ) / [ σ/√n ]. Note that there is only one source of variation, x-bar. The standard deviation of x-bar is the denominator, σ/√n. This Z (standard normal) distribution is centered at 0, bell shaped, and has a standard devation of 1. The t-score is calculated with t = ( x-bar - μ) / [ s/√n ] . Note that the denominator, s/√n, is the standard error of x-bar. Also notice that we now have two sources of variation, x-bar and s. The t-distribution (with n-1 d.f.) is centered at zero, bell shaped, and has a larger spread.
```

In fact, the t score that arises in the context of a test for a mean is a t score with (n – 1) degrees of freedom. Recall that each t distribution is indexed according to "degrees of freedom." Notice that, in the context of a test for a mean, the degrees of freedom depend on the sample size in the study. Remember that we said that higher degrees of freedom indicatethat the t distribution is closer to normal. So in the context of a test for the mean, the *larger the sample size*, the higher the degrees of freedom, and *the closer the t distribution is to a normal z distribution*. This is summarized with the notation near the bottom on the following image:

```{figure} images/image419.gif
:alt: The larger the sample size n, the closer the t-distribution gets to the standard normal.

The larger the sample size n, the closer the t-distribution gets to the standard normal.
```

As a result, in the context of a test for a mean, the effect of the t distribution is *most important* for a study with a *relatively small sample size*.

We are now done introducing the t distribution. What are implications of all of this?

1. The null distribution of our t-test statistic: $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}$ is the t distribution with (n-1) d.f. In other words, when H~o~ is true (i.e., when $\mu=\mu_{0}$), our test statistic has a t distribution with (n-1) d.f., and this is the distribution under which we find p-values.

2. For a large sample size (n), the null distribution of the test statistic is approximately Z, so whether we use t(n-1) or Z to calculate the p-values should not make a big difference. Here is another practical way to look at this point. If we havea large n, our sample has more information about the population. Therefore, we can expect the sample standard deviation s to be close enough to the population standard deviation, σ, so that for practical purposes we can use s as the known σ, and we're back to the z-test.
