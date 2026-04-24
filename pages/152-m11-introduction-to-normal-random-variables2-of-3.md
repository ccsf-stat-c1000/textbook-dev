# Introduction to Normal Random Variables(2 of 3)

```{admonition} Learning Objectives
    - Find probabilities associated with the normal distribution.
```

## The Standard Deviation Rule for Normal Random Variables

We began to get a feel for normal distributions in the Exploratory Data Analysis (EDA) section, when we introduced the Standard Deviation Rule (or the *68-95-99.7* rule) for how values in a normally-shaped *sample data set* behave relative to their mean ($\bar{x}$) and standard deviation (s). This is the same rule that dictates how the distribution of a normal *random variable* behaves relative to its mean $\mu$ and standard deviation $\sigma$. Now we use probability language and notation to describe the random variable's behavior. For example, in the EDA section, we would have said "68% of pregnancies in our data set fall within 1 standard deviation (s) of their mean ($\bar{x}$)." The analogous statement now would be "If X, the length of a randomly chosen pregnancy, is normal with mean ($\mu$) and standard deviation ($\sigma$), then $0.68=P(\mu-\sigma<X<\mu+\sigma)$."

In general, if X is a normal random variable, then the probability is

68% that X falls within 1 $\sigma$ of $\mu$ , that is, in the interval $\mu\pm\sigma$

95% that X falls within 2 $\sigma$ of $\mu$ , that is, in the interval $\mu\pm2\sigma$

99.7% that X falls within 3 $\sigma$ of $\mu$ , that is, in the interval$\mu\pm3\sigma$

Using probability notation, we may write

$0.68=P(\mu-\sigma<X<\mu+\sigma)$

$0.95=P(\mu-2\sigma<X<\mu+2\sigma)$

$0.997=P(\mu-3\sigma<X<\mu+3\sigma)$

```{figure} images/image121.gif
:alt: A normal bell curve with some ranges marked. At the center (peak) of the bell curve is μ. The area under the bell curve between μ-σ < X < μ+σ compromises of 0.68 of the total area under the bell curve (which is 1). The area under the bell curve between μ-2σ < X < μ+2σ is 0.95 of the total area under the curve. Capturing even more area under the bell curve is the range of μ-3σ < X < μ+3σ, which is 0.997 of the total area under the curve.

A normal bell curve with some ranges marked. At the center (peak) of the bell curve is μ. The area under the bell curve between μ-σ < X < μ+σ compromises of 0.68 of the total area under the bell curve (which is 1). The area under the bell curve between μ-2σ < X < μ+2σ is 0.95 of the total area under the curve. Capturing even more area under the bell curve is the range of μ-3σ < X < μ+3σ, which is 0.997 of the total area under the curve.
```

## Comment

Notice that the information from the rule can be interpreted from the perspective of the tails of the normal curve: since .68 is the probability of being within 1 standard deviation of the mean, (1 - .68) / 2 = .16 is the probability of being further than 1 standard deviation below the mean (or further than 1 standard deviation above the mean). Likewise, (1 - .95) / 2 = .025 is the probability of being more than 2 standard deviations below (or above) the mean; (1 - .997) / 2 = .0015 is the probability of being more than 3 standard deviations below (or above) the mean. The three figures below illustrate this.

```{figure} images/image122.gif
:alt: A normal bell curve, in which μ, μ-σ, and μ+σ have been marked on the horizontal axis. The probability of being within one standard deviation of μ, or between μ-σ and μ+σ, is .68 . The probability of being below one standard deviation from the mean is the area under the bell curve to the left of μ-σ which is .16 . Likewise, the probability of being further than one standard deviation above the mean is the area under the bell curve to the right of μ+σ, which is .16 .

A normal bell curve, in which μ, μ-σ, and μ+σ have been marked on the horizontal axis. The probability of being within one standard deviation of μ, or between μ-σ and μ+σ, is .68 . The probability of being below one standard deviation from the mean is the area under the bell curve to the left of μ-σ which is .16 . Likewise, the probability of being further than one standard deviation above the mean is the area under the bell curve to the right of μ+σ, which is .16 .
```

```{figure} images/image123.gif
:alt: A normal bell curve. The probability of being within two standard deviation of μ is .95 . The probability of being further than two standard deviations below the mean is the area under the bell curve to the left of μ-2σ which is .025 . The probability of being further than two standard deviation above the mean is the area under the bell curve to the right of μ+2σ, which is .025 .

A normal bell curve. The probability of being within two standard deviation of μ is .95 . The probability of being further than two standard deviations below the mean is the area under the bell curve to the left of μ-2σ which is .025 . The probability of being further than two standard deviation above the mean is the area under the bell curve to the right of μ+2σ, which is .025 .
```

```{figure} images/image124.gif
:alt: A normal bell curve. The probability of being within three standard deviation of μ is .997 . The probability of being below three standard deviations from the mean is the area under the bell curve to the left of μ-3σ which is .0015 . The probability of being further than three standard deviation above the mean is the area under the bell curve to the right of μ+3σ, which is .0015 .

A normal bell curve. The probability of being within three standard deviation of μ is .997 . The probability of being below three standard deviations from the mean is the area under the bell curve to the left of μ-3σ which is .0015 . The probability of being further than three standard deviation above the mean is the area under the bell curve to the right of μ+3σ, which is .0015 .
```

```{admonition} Example
    Suppose that foot length of a randomly chosen adult male is a normal random variable with mean $\mu=11$ and standard deviation $\sigma=1.5$. Then the Standard Deviation Rule lets us sketch the probability distribution of X as follows:

    ```{figure} images/image127.gif
    :alt: A probability distribution curve in which the horizontal axis is labeled "X - Foot Length." The curve is a normal bell curve. The mean, μ, is at X=11. The first standard deviation is at X=9.5 and X=12.5, with probability of .68 . The second standard deviation is X=8 and X=14, with probability of .95 . The third standard deviation is at X=6.5 and X=15.5, with probability of .997 .

    A probability distribution curve in which the horizontal axis is labeled "X - Foot Length." The curve is a normal bell curve. The mean, μ, is at X=11. The first standard deviation is at X=9.5 and X=12.5, with probability of .68 . The second standard deviation is X=8 and X=14, with probability of .95 . The third standard deviation is at X=6.5 and X=15.5, with probability of .997 .
    ```

    *(a)* What is the probability that a randomly chosen adult male will have a foot length between 8 and 14 inches? .95, or 95%.

    *(b)* An adult male is almost guaranteed (.997 probability) to have a foot length between what two values? 6.5 and 15.5 inches.

    *(c)* The probability is only 2.5% that an adult male will have a foot length greater than how many inches? 14.

    ```{figure} images/image128.gif
    :alt: The probability distribution curve for foot lengths. The 2nd standard deviation boundaries from the mean have been marked at X=8 and X=14 . The probability of being within 2 standard deviations of the mean is .95, and the probability of being above 2 standard deviations (X > 14) is .025 . The probability of being below the 2nd standard deviation (X < 8) is also .025 .

    The probability distribution curve for foot lengths. The 2nd standard deviation boundaries from the mean have been marked at X=8 and X=14 . The probability of being within 2 standard deviations of the mean is .95, and the probability of being above 2 standard deviations (X > 14) is .025 . The probability of being below the 2nd standard deviation (X < 8) is also .025 .
    ```

    Now you should try a few. (Use the figure that is just before *part (a)* to help you.)

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

## Comment

Notice that there are two types of problems we may want to solve: those like *(a)*, *(d)* and *(e)*, in which a particular interval of values of a normal random variable is given, and we are asked to find a probability, and those like *(b)*, *(c)* and *(f)*, in which a probability is given and we are asked to identify what the normal random variable's values would be.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    Normal Random Variables

    *(Interactive activity — available in the OLI platform)*
```
