# The Mean, Standard Deviation, and Shape of a Binomial

```{admonition} Learning Objectives
:class: note

- Fit the binomial model when appropriate, and use it to perform simple calculations.
```

## Mean and Standard Deviation of the Binomial Random Variable

Now that we understand how to find probabilities associated with a random variable X which is binomial, using either its probability distribution formula or technology, we are ready to talk about the mean and standard deviation of a binomial random variable. Let's start with an example:

:::{admonition} Example: Blood Type B—Mean
:class: tip

Overall, the proportion of people with blood type B is 0.1. In other words, roughly 10% of the population has blood type B.

Suppose we sample 120 people at random. On average, how many would you expect to have blood type B?

The answer, 12, seems obvious; automatically, you'd multiply the number of people, 120, by the probability of blood type B, 0.1. This suggests the general formula for finding the mean of a binomial random variable.
:::

*Claim:* If X is binomial with parameters n and p, then

$$\mu_{X}=np$$

Although the formula for the mean is quite intuitive, it is not at all obvious what the variance and standard deviation should be. It turns out that:

*Claim:* If X is binomial with parameters n and p, then

$$\sigma_{X}^{2}=np(1-p) \qquad \sigma_{X}=\sqrt{np(1-p)}$$

## Comment

The binomial mean and variance are special cases of our general formulas for the mean and variance of any random variable:

$$\mu_{X}=\sum_{i=1}^{n}x_{i}p_{i} \qquad \sigma_{X}^{2}=\sum_{i=1}^{n}(x_{i}-\mu_{X})^{2}p_{i}$$

Clearly it is much simpler to use the "shortcut" formulas $\mu_{X}=np$ and $\sigma_{X}=\sqrt{np(1-p)}$ than it would be to calculate the mean and variance or standard deviation from scratch.

:::{admonition} Example: Blood Type B—Standard Deviation
:class: tip

Suppose we sample 120 people at random. The number with blood type B should be about 12, give or take how many? In other words, what is the standard deviation of the number X who have blood type B?

Since n = 120 and p = 0.1,

$$\sigma_{X}^{2}=120(0.1)(1-0.1)=10.8 \qquad \sigma_{X}=\sqrt{10.8}\approx3.3$$

In a random sample of 120 people, we should expect there to be about 12 with blood type B, give or take about 3.3.
:::

## Did I Get This?

A Gallup Poll in May 2004 estimated that roughly 70% of U.S. adults are in favor of the death penalty for a person convicted of murder. A random sample of 750 U.S. adults is chosen. Let X be the number of adults (out of 750) who favor the death penalty.

:::{quiz} What are the mean and standard deviation of X?
:hint: μ = np = 750(0.7); σ = √(np(1−p)) = √(750 × 0.7 × 0.3).
:feedback-0: Correct! μ = 525 and σ = √157.5 ≈ 12.5.
:feedback-1: 157.5 is the variance—take its square root for the standard deviation.
:feedback-2: The mean is np = 750 × 0.7 = 525, not 375.
* *Mean 525, standard deviation about 12.5
* Mean 525, standard deviation 157.5
* Mean 375, standard deviation about 12.5
:::

:::{quiz} Using the 2-standard-deviations criterion, would it be unusual for only 350 of the 750 sampled adults to favor the death penalty?
:hint: The ordinary range is 525 ± 2(12.5), i.e., 500 to 550.
:feedback-0: Correct! 350 is far below 500 (in fact, 14 standard deviations below the mean)—extremely unusual, and it would make us doubt the claimed 70%.
:feedback-1: 350 is nowhere near the ordinary range of 500 to 550.
* *Yes—350 is far outside the range 500 to 550
* No—350 is within 2 standard deviations of the mean
:::

## The Shape of Binomial Distributions

Before we move on to continuous random variables, let's investigate the shape of binomial distributions. For different values of p, binomial distributions can be symmetric, skewed right, or skewed left:

```{figure} images/gen/m11-binomial-shapes.svg
:alt: Three probability histograms for binomial distributions with n equal to 10. For p equal to 0.1 the distribution is skewed right, with the probability piled up near 0. For p equal to 0.5 it is symmetric, centered at 5. For p equal to 0.9 it is skewed left, with the probability piled up near 10.
```

:::{quiz} A binomial distribution has n = 20 and p = 0.05. What shape would you expect its probability histogram to have?
:hint: With small p, successes are rare—where does the probability pile up?
:feedback-0: Correct! With p much smaller than 0.5, most of the probability is on small values of X, leaving a long right tail—skewed right.
:feedback-1: Skewed left occurs when p is large (close to 1).
:feedback-2: Symmetry occurs when p = 0.5 (or when n is very large).
* *Skewed right
* Skewed left
* Symmetric
:::
