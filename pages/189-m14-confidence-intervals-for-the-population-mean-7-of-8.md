# When Is It Safe to Use This Interval?

We are almost done with this section. We need to discuss just a few more questions:

- Is it always okay to use the confidence interval we developed for μ when σ is known?
- What if σ is unknown?
- How can we use statistical software to calculate confidence intervals for us?

## When Is It Safe to Use the Confidence Interval We Developed?

One of the most important things to learn with any inference method is the conditions under which it is safe to use it. It is very tempting to apply a certain method, but if the conditions under which this method was developed are not met, then using this method will lead to unreliable results, which can then lead to wrong and/or misleading conclusions. As you'll see throughout this section, we always discuss the conditions under which each method can be safely used.

In particular, the confidence interval for μ (when σ is known), $\bar{x} \pm z^{*}\cdot\frac{\sigma}{\sqrt{n}}$, was developed assuming that the sampling distribution of $\bar{X}$ is normal; in other words, that the Central Limit Theorem applies. In particular, this allowed us to determine the values of z\*, the confidence multiplier, for different levels of confidence.

First, *the sample must be random.* Assuming that the sample is random, recall from the Probability unit that the Central Limit Theorem works when the *sample size is large* (a common rule of thumb for "large" is n > 30), or, for *smaller sample sizes*, if it is known that the quantitative *variable* of interest is *distributed normally* in the population. The only situation in which we cannot use the confidence interval, then, is when the sample size is small and the variable of interest is not known to have a normal distribution. In that case, other methods, called nonparametric methods, which are beyond the scope of this course, need to be used. This can be summarized in the following table:

| | Small sample size | Large sample size |
| --- | --- | --- |
| **Variable varies normally** | OK | OK |
| **Variable doesn't vary normally** | NOT OK | OK |

## Check Your Understanding: Conditions for the z Interval

Below are four different situations in which a confidence interval formula would be useful:

*Situation A:* A marketing executive wants to estimate the average time, in days, that a watch battery will last. She tests 50 randomly selected batteries and finds that the distribution is skewed to the left, since a couple of the batteries were defective. It is known from past experience that the standard deviation is 25 days.

*Situation B:* A college professor desires an estimate of the mean number of hours per week that full-time college students are employed. He randomly selected 250 college students and found that they worked a mean time of 18.6 hours per week. He uses previously known data for his standard deviation.

*Situation C:* A medical researcher at a sports medicine clinic uses 35 volunteers from the clinic to study the average number of hours the typical American exercises per week. It is known that hours of exercise are normally distributed and past data give him a standard deviation of 1.2 hours.

*Situation D:* A high-end auto manufacturer tests 5 randomly selected cars to find out the damage caused by a 5 mph crash. It is known that this distribution is normal. Assume that the standard deviation is known.

:::{quiz} In which situation is it NOT safe to rely on the z confidence interval for the population mean?
:hint: Check each situation for random sampling and either a large n or a normal population.
:feedback-0: Situations A, B, and D all satisfy the conditions (A and B have large samples; D has a small sample but a normal population).
:feedback-1: Correct! In Situation C the volunteers from a clinic are not a random sample of "typical Americans"—the sampling condition fails, so the interval would be unreliable regardless of the formula.
:feedback-2: D is fine: even with n = 5, the population is known to be normal and σ is known.
* Situation A—the distribution is skewed
* *Situation C—the sample of clinic volunteers is not random
* Situation D—the sample is too small
:::

## What If σ Is Unknown?

As we discussed earlier, when variables have been well-researched in different populations it is reasonable to assume that the population standard deviation (σ) is known. However, this is rarely the case. What if σ is unknown?

Well, there is some good news and some bad news.

The good news is that we can easily replace the population standard deviation, σ, with the *sample* standard deviation, s.

The bad news is that once σ has been replaced by s, we lose the normality of the standardized $\bar{X}$, and therefore the confidence multipliers z\* for the different levels of confidence (1.645, 2, 2.576) are (generally) not accurate any more. The new multipliers come from a different distribution called the "t distribution" and are therefore denoted by t\* (instead of z\*). We will discuss the t distribution in more detail when we talk about hypothesis testing.

The confidence interval for the population mean (μ) when σ is unknown is therefore:

$$\bar{x} \pm t^{*}\cdot\frac{s}{\sqrt{n}}$$

(Note that this interval is very similar to the one when σ is known, with the obvious changes: s replaces σ, and t\* replaces z\*.)

There is an important difference between the confidence multipliers we have used so far (z\*) and those needed for the case when σ is unknown (t\*). Unlike z\*, which depends only on the level of confidence, the new multipliers (t\*) have the *added complexity* that they *depend on both the level of confidence and on the sample size* (for example, the t\* used for 95% confidence when n = 10 is different from the t\* used when n = 40). Due to this added complexity in determining the appropriate t\*, we will rely heavily on technology in this case.

```{admonition} Comments
:class: important

1. Since it is quite rare that σ is known, this interval (sometimes called a *one-sample t confidence interval*) is more commonly used as the confidence interval for estimating μ. (Nevertheless, we could not have presented it without our extended discussion up to this point, which also provided you with a solid understanding of confidence intervals.)

2. The quantity $\frac{s}{\sqrt{n}}$ is called the {term}`standard error` of $\bar{X}$. The Central Limit Theorem tells us that $\frac{\sigma}{\sqrt{n}}$ is the {term}`standard deviation` of $\bar{X}$ (and this is the quantity used in the confidence interval when σ is known). In general, whenever we replace parameters with their sample counterparts in the standard deviation of a statistic, the resulting quantity is called the standard error of the statistic. In this case, we replaced σ with its sample counterpart (s), and thus $\frac{s}{\sqrt{n}}$ is the {term}`standard error` of (the statistic) $\bar{X}$.

3. As before, to safely use this confidence interval, the sample *must be random*, and the only case when this interval cannot be used is when the sample size is small and the variable is not known to vary normally.
```

## Check Your Understanding: z Interval or t Interval?

:::{quiz} A researcher has a random sample of 45 observations with sample mean 82 and sample standard deviation 12; σ is unknown. Which confidence interval should be used for μ?
:hint: σ has been replaced by s—which multiplier goes with that?
:feedback-0: Correct! With σ unknown, we use s and the t multiplier: x-bar ± t*(s/√n).
:feedback-1: The z interval with σ requires knowing the population standard deviation, which we don't.
:feedback-2: The margin of error must divide s by √n, not use s alone.
* *82 ± t*(12/√45)
* 82 ± z*(σ/√45)
* 82 ± t*(12)
:::

```{admonition} Final Comment
:class: important

It turns out that for large values of n, the t\* multipliers are not that different from the z\* multipliers, and therefore using the interval formula

$$\bar{x} \pm z^{*}\cdot\frac{s}{\sqrt{n}}$$

for μ when σ is unknown provides a pretty good approximation.
```
