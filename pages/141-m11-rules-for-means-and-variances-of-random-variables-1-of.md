# Shifting and Scaling a Random Variable

## Rules for Means and Variances of Random Variables

So far we've learned how to calculate the mean and standard deviation of a random variable, and how to interpret these numerical measures. Let's look at a motivating example that will show us what kinds of situations we may find these rules useful in.

:::{admonition} Example: Xavier's Production Line
:class: tip

Assume that operating Xavier's production line costs \$50 per hour, and that the repair cost of one defective part is \$5. If X is the number of defective parts produced per hour, then the hourly cost would be *50 + 5X*. Note that since X is a random variable, so is the cost, 50 + 5X, and we might be interested in the mean and standard deviation of the hourly cost of operation for Xavier's production line.

If we know the mean and standard deviation for the number of defective parts (X), is there an easy way to find the mean and standard deviation for the hourly cost (50 + 5X)?
:::

## In General

Sometimes a new random variable of interest arises when we take an existing random variable and multiply by a constant and/or add a constant to its values. In the example above, we both multiplied X by 5 and added 50. We will return to the above example after exploring how such changes affect the center (mean) and spread (standard deviation) of random variables in general.

Consider the random variable X with the probability distribution P(X = $-2) = 0.1$, P(X = $-1) = 0.1$, P(X = $0) = 0.6$, P(X = $1) = 0.1$, P(X = $2) = 0.1$. It can easily be shown that X has a mean of 0, and a standard deviation of 1.

## Adding or Subtracting a Constant

What would the mean and standard deviation be if we shifted the entire histogram over 6 units to the right—in other words, what are the mean and standard deviation of $X + 6$? And what if we shifted it 7 units to the left, to get $X - 7$?

```{figure} images/gen/m11-shift-hist.svg
:alt: Three identical-shaped probability histograms. The original X is centered at 0. X plus 6 is the same shape shifted so it is centered at 6, and X minus 7 is the same shape centered at negative 7. In all three the spread is unchanged, with standard deviation 1.
```

We observe that shifting the distribution over to the right 6 units also shifts the center over 6 units: in other words, the mean of (X + 6) should equal the (mean of X) + 6. However, the spread of the distribution is unchanged: the standard deviation of (X + 6) equals the standard deviation of X. Likewise, subtracting 7 shifts the mean to -7, and the standard deviation remains unchanged at 1.

## Multiplying X by a Constant

What would the mean and standard deviation be if we stretched the entire histogram by a factor of 4—in other words, what are the mean and standard deviation of 4X? And what if we shrank it by a fourth, to get (1/4)X?

```{figure} images/gen/m11-scale-hist.svg
:alt: Three probability histograms with the same shape but different widths. The original X spans values from negative 2 to 2 with standard deviation 1. The histogram for 4X spans negative 8 to 8, stretched to standard deviation 4. The histogram for X over 4 spans only negative 0.5 to 0.5, shrunk to standard deviation one quarter.
```

Multiplying X by 4 results in a mean that is 4 times the original mean. In this case, the mean transforms from 0 to $4(0) = 0$. Multiplying X by 4 is tantamount to stretching the distribution by a factor of 4, and so the standard deviation will be 4 times the original standard deviation. The variance, or squared standard deviation, would be $4^2$ times the original variance: the variance of 4X is 16 times the variance of X.

Dividing X by 4 results in a mean that is 1/4 the original mean (still 0 here). Dividing X by 4 shrinks the distribution by a factor of 4, and so the standard deviation will be 1/4 of the original standard deviation, and the variance of (1/4)X is 1/16 times the variance of X.
