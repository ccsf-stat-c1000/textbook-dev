# Normal Approximation to the Binomial (2 of 3)

```{admonition} Learning Objectives
    - Use the normal distribution as an approximation of the binomial distribution, when appropriate.
```

Consider the appearance of the probability histogram for the distribution of X:

```{figure} images/image176.gif
:alt: A probability histogram. The vertical axis is labeled "Probability" and the horizontal axis is labeled "binomial X; n=20, p=.5" . It is in roughly a normal shape, with the mode at X = 10.

A probability histogram. The vertical axis is labeled "Probability" and the horizontal axis is labeled "binomial X; n=20, p=.5" . It is in roughly a normal shape, with the mode at X = 10.
```

Clearly, the shape of the distribution of X for n = 20, p = .5 has a normal appearance: symmetric, bulging at the middle, and tapering at the ends. The following figure should help you visualize this:

```{figure} images/image177.gif
:alt: The same probability histogram with a normal bell curve drawn on top, showing how the histogram closely resembles a normal bell curve.

The same probability histogram with a normal bell curve drawn on top, showing how the histogram closely resembles a normal bell curve.
```

This suggests a method of approximating binomial probabilities:

Estimate the binomial probability of $X_{B}$ taking a value over a certain interval with the probability that a normal random variable $X_{N}$ takes a value over the same interval, where $X_{N}$ has the same mean and standard deviation as $X_{B}$, namely $\mu=np,\sigma=\sqrt{np(1-p)}$

```{admonition} Example
    Suppose a student answers 20 true/false questions completely at random. Use a normal approximation to estimate the probability of getting no more than 8 correct. The number (X) correct is a binomial random variable that represents the number of successes in 20 trials when the probability of success for each trial is .5. X has a mean and standard deviation of:

    $\mu=np=20(0.5)=10,\sigma=\sqrt{np(1-p)}=\sqrt{20(0.5)(1-0.5)}=2.24$

    and so we approximate the binomial X with a normal random variable having the same mean and standard deviation:

    ```{figure} images/image182.gif
    :alt: A probability histogram with a probability distribution curve drawn on top. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The histogram is for binomial X, with mean=10 and standard deviation of 2.24 . The normal curve is for normal X, with mean 10 and standard deviation of 2.24 , the same as for the histogram.

    A probability histogram with a probability distribution curve drawn on top. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The histogram is for binomial X, with mean=10 and standard deviation of 2.24 . The normal curve is for normal X, with mean 10 and standard deviation of 2.24 , the same as for the histogram.
    ```

    Then we solve in the usual way using normal tables:

    $P(X_{B}\leq8)\approxP(X_{N}\leq8)=P(Z\leq\frac{8-10}{2.24})=P(Z\leq-0.89)=0.1867$
```

Unfortunately, the approximated probability, .1867, is quite a bit different from the actual probability, .2517. However, this example constitutes something of a "worst-case scenario" according to the usual criteria for use of a normal approximation.

## Rule of Thumb

Probabilities for a binomial random variable X with n and p may be approximated by those for a normal random variable having the same mean and standard deviation as long as the sample size n is large enough relative to the proportions of successes and failures, p and 1 - p. Our Rule of Thumb will be to require that

$np\geq10$ and $n(1-p)\geq10$

```{admonition} Example
    May we use a normal approximation for a binomial X with n = 20 and p = .5? In this case, np = 20(.5) = 10 and n(1 - p) = 20(1 - .5) = 10. The criteria are just barely satisfied, and so we should not expect the approximation to be especially good.
```

The purpose of the next activity is to give you practice at deciding whether the normal approximation is appropriate for a given binomial random variable. You'll get to practice checking the rule of thumb $(np\geq10$ and $n(1-p)\geq10)$, but also get a visual sense of when the normal approximation is appropriate.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
