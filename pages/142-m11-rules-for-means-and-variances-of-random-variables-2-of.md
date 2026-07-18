# Linear Transformations: The Rule for a + bX

```{admonition} Learning Objectives
:class: note

- Apply the rules of means and variances to find the mean and variance of a linear transformation of a random variable and the sum of two independent random variables.
```

The observations we made on the previous page help illustrate a general rule for how random variables transform if we add, subtract and/or multiply by a constant.

## Rules for a + bX (Linear Transformation of One Random Variable)

If X is a random variable with mean $\mu_{X}$ and variance $\sigma_{X}^{2}$, then the new random variable *a + bX* has a mean and variance (respectively) of:

$$\mu_{a+bX}=a+b\mu_{X}$$

$$\sigma_{a+bX}^{2}=b^{2}\sigma_{X}^{2}$$

```{admonition} Comment
:class: important

If we take a random variable's distribution and shift it over "a" units, and stretch or shrink its spread by "b" (stretch if b is greater than 1, shrink if b is less than 1), then the mean is shifted and the distribution is stretched or shrunk accordingly. For instance, if we multiply a random variable by 6 and add 3, then the mean is also transformed: the mean is also multiplied by 6 and 3 is added. Shifting by "a," however, has no effect on the variance (or standard deviation) of a random variable, because the spread would not be changed. On the other hand, stretching or shrinking the distribution of a random variable entails stretching or shrinking its spread accordingly. Doubling a random variable's values produces a new random variable whose variance is four times the original variance, but the standard deviation is just double the original standard deviation, as we might expect.
```

:::{admonition} Example: Shifting and Stretching
:class: tip

Recall that X is the number of defective parts per hour in Xavier's production line, and in the previous section we calculated that:

$\mu_{X}=1.8$ and $\sigma_{X}=1.21$.

We are interested in a new random variable, "50 + 5X," which represents the hourly cost of operation for Xavier's production line. Note that 50 + 5X is of the form "a + bX" (where a = 50 and b = 5), so in order to find the mean and standard deviation of this new random variable, we can use the rules above:

$$\mu_{50+5X}=50+5\mu_{X}=50+5(1.8)=59$$

$$\sigma_{50+5X}^{2}=5^{2}\sigma_{X}^{2}=25(1.46)=36.5$$

and therefore: $\sigma_{50+5X}=\sqrt{36.5}=6.04$

So, we can conclude that the hourly costs for Xavier's production line average \$59, and typically the cost is about \$6 away from that average.
:::

## Check Your Understanding: Linear Transformations of a Random Variable

:::{quiz} A random variable X has mean 10 and standard deviation 2. What are the mean and standard deviation of 3X + 4?
:hint: Mean: a + bμ = 4 + 3(10). SD: |b|σ = 3(2)—the added constant doesn't affect spread.
:feedback-0: Correct! μ = 4 + 3(10) = 34, and σ = 3 × 2 = 6.
:feedback-1: The constant 4 shifts the mean but has no effect on the standard deviation.
:feedback-2: The mean of 3X + 4 is 3(10) + 4 = 34, not 30—don't forget the added constant (for the mean only).
* *Mean 34, standard deviation 6
* Mean 34, standard deviation 10
* Mean 30, standard deviation 6
:::

:::{quiz} Temperatures in Celsius (C) at a weather station have mean 20 and standard deviation 5. Fahrenheit temperature is F = 32 + 1.8C. What are the mean and standard deviation of F?
:hint: Apply the linear transformation rules with a = 32 and b = 1.8.
:feedback-0: Correct! μ(F) = 32 + 1.8(20) = 68, and σ(F) = 1.8 × 5 = 9.
:feedback-1: The 32 shifts the center but not the spread: σ(F) = 1.8 × 5 = 9, not 41.
:feedback-2: Don't forget to add 32 when transforming the mean.
* *Mean 68, standard deviation 9
* Mean 68, standard deviation 41
* Mean 36, standard deviation 9
:::
