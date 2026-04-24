# Rules for Means and Variances of Random Variables (2 of 3)

```{admonition} Learning Objectives
    - Apply the rules of means and variances to find the mean and variance of a linear transformation of a random variable and the sum of two independent random variables.
```

The four observations we made on the previous page help illustrate a general rule for how random variables transform if we add, subtract and/or multiply by a constant.

## Rules for a + bX (Linear Transformation of One Random Variable)

If X is a random variable with the mean $\mu_{X}$ and a variance of $\sigma_{X}^{2}$, then the new random variable *a + bX* has a mean and variance (respectively) of:

$\mu_{a+bX}=a+b\mu_{X}$

$\sigma_{a+bX}^{2}=b^{2}\sigma_{X}^{2}$

## Comment

If we take a random variable's distribution and shift it over "a" units, and stretch or shrink its spread by "b" (stretch if b is greater than 1, shrink if b is less than 1), then the mean is shifted and the distribution is stretched or shrunk accordingly. For instance, if we multiply a random variable by 6 and add 3, then the mean is also transformed. The mean is also multiplied by 6 and 3 is added. Shifting by "a," however, has no effect on the variance (or standard deviation) of a random variable, because the spread would not be changed. On the other hand, stretching or shrinking the distribution of a random variable entails stretching or shrinking its spread accordingly. Doubling a random variable's values produces a new random variable whose variance is four times the original variance, but the standard deviation is just double the original standard deviation, as we might expect.

```{admonition} Example: Shifting and Stretching
    Recall that X is the number of defective parts per hour in Xavier's production line, and in the previous section we calculated that:

    $\mu_{x}=1.8$ and that $\sigma_{X}=1.21$.

    We are interested in a new random variable, "50 + 5X," which represents the hourly cost of operation for Xavier's production line. Note that 50 + 5X is of the form "a + bX" (where a = 50 and b = 5), so in order to find the mean and standard deviation of this new random variable, we can use the rules above:

    $\mu_{50+5X}=50+5\mu_{x}=50+5(1.8)=59$

    $\sigma_{50+5X}^{2}=5^{2}\sigma_{X}^{2}=25(1.46)=36.5$

    and therefore: $\sigma_{50+5X}=\sqrt{36.5}=6.04$

    So, we can conclude that the hourly costs for Xavier's production line average $59, and typically the cost is about $6 away from that average.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
