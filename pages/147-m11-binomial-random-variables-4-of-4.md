# Binomial Random Variables (4 of 4)

```{admonition} Learning Objectives
    - Fit the binomial model when appropriate, and use it to perform simple calculations.
```

## Mean and Standard Deviation of the Binomial Random Variable

Now that we understand how to find probabilities associated with a random variable X which is binomial, using either its probability distribution formula or software, we are ready to talk about the mean and standard deviation of a binomial random variable. Let's start with an example:

```{admonition} Example: Blood Type B—Mean
    Overall, the proportion of people with blood type B is .1. In other words, roughly 10% of the population has blood type B.

    Suppose we sample 120 people at random. On average, how many would you expect to have blood type B?

    The answer, 12, seems obvious; automatically, you'd multiply the number of people, 120, by the probability of blood type B, .1. This suggests the general formula for finding the mean of a binomial random variable:
```

*Claim:*

If X is binomial with parameters n and p, then

$\mu_{X}=np$

Although the formula for mean is quite intuitive, it is not at all obvious what the variance and standard deviation should be. It turns out that:

*Claim:*

If X is binomial with parameters n and p, then

$\sigma_{X}^{2}=np(1-p);\sigma_{X}=\sqrt{np(1-p)}$

For those who are interested, click the button below to see how these formulas were derived.

```{note}
    **Learnmore**

    Binomial Formulas

    *(Interactive activity — available in the OLI platform)*
```

## Comment

The binomial mean and variance are special cases of our general formulas for the mean and variance of any random variable.

$\mu_{X}=x_{1}p_{1}+x_{2}p_{2}+...+x_{n}p_{n}=\sum_{i=1}^{n}x_{i}p_{i}$

$\sigma_{X}^{2}=(x_{1}-\mu_{X})^{2}p_{1}+(x_{2}-\mu_{X})^{2}p_{2}+...+(x_{n}-\mu_{X})^{2}p_{n}$

$=\sum_{i=1}^{n}(x_{i}-\mu_{X})^{2}p_{i}$

Clearly it is much simpler to use the "shortcut" formulas

$\mu_{X}=np$ and $\sigma_{X}^{2}=np(1-p);\sigma_{X}=\sqrt{np(1-p)}$ than it would be to calculate the mean and variance or standard deviation from scratch.

```{admonition} Example: Blood Type B—Standard Deviation
    Suppose we sample 120 people at random. The number with blood type B should be about 12, give or take how many? In other words, what is the standard deviation of the number X who have blood type B?

    Since n = 120 and p = .1,

    $\sigma_{X}^{2}=120(0.1)(1-0.1)=10.8;\sigma_{X}=\sqrt{10.8}\approx3.3$

    In a random sample of 120 people, we should expect there to be about 12 with blood type B, give or take about 3.3.
```

## Did I Get This?

A Gallup Poll in May 2004 estimated that roughly 70% of U.S. adults are in favor of the death penalty for a person convicted of murder. A random sample of 750 U.S. adults is chosen. Let X be the number of adults (out of 750) who favor the death penalty.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Learn By Doing

Before we move on to continuous random variables, let's investigate the shape of binomial distributions. Using the applet below we will see that for different values of n and p, binomial distributions can be symmetric, skewed right or skewed left.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
