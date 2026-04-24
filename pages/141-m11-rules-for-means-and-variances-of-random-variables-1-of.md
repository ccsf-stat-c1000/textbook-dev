# Rules for Means and Variances of Random Variables (1 of 3)

```{admonition} Learning Objectives
    - Apply the rules of means and variances to find the mean and variance of a linear transformation of a random variable and the sum of two independent random variables.
```

## Rules for Means and Variances of Random Variables

So far we've learned how to calculate the mean and standard deviation of a random variable, and how to interpret these numerical measures. Let's look at a motivating example that will show us what kinds of situations we may find these rules useful in.

```{admonition} Example: Xavier's Production Line
    Assume that operating Xavier's production line costs $50 per hour, and that the repair cost of one defective part is $5. If X is the number of defective parts produced per hour, then the hourly cost would be *50 + 5X*. Note that since X is a random variable, so is the cost, 50 + 5X, and we might be interested in the mean and standard deviation of the hourly cost of operation for Xavier's production line.

    If we know the mean and standard deviation for the number of defective parts (X), is there an easy way to find the mean and standard deviation for the hourly cost (50 + 5X)?
```

## In General

Sometimes a new random variable of interest arises when we take an existing random variable and multiply by a constant and/or add a constant to its values. In the example above, we both multiplied X by 5 and added 50. We will return to the above example after exploring how such changes affect the center (mean) and spread (standard deviation) of random variables in general.

Consider the random variable X with a probability distribution as shown in the histogram below:

```{figure} images/image055.gif
:alt: A histogram in which the vertical axis is labeled &quot;Probability&quot; and the horizontal axis is labeled &quot;X.&quot; Here is the data represented by the histogram: P(X = -2) = 0.1; P(X = -1) = 0.1; P(X = 0) = 0.6; P(X = 1) = 0.1; P(X = 2) = 0.1; So, the histogram is entire flat with probability = 0.1, except at X=0, where probability is 0.6

A histogram in which the vertical axis is labeled &quot;Probability&quot; and the horizontal axis is labeled &quot;X.&quot; Here is the data represented by the histogram: P(X = -2) = 0.1; P(X = -1) = 0.1; P(X = 0) = 0.6; P(X = 1) = 0.1; P(X = 2) = 0.1; So, the histogram is entire flat with probability = 0.1, except at X=0, where probability is 0.6
```

It can easily be shown that X has a mean of 0, and a standard deviation of 1.

## Adding a Constant to X

What would the mean and standard deviation be if we shifted the entire histogram over 6 units to the right—in other words, what are the mean and standard deviation of X + 6?

```{figure} images/image056.gif
:alt: The same histogram, except that the bars have been shifted over 6 units. This that the data now represented is: P(X = 4) = 0.1; P(X = 5) = 0.1; P(X = 6) = 0.6; P(X = 7) = 0.1; P(X = 8) = 0.1;

The same histogram, except that the bars have been shifted over 6 units. This that the data now represented is: P(X = 4) = 0.1; P(X = 5) = 0.1; P(X = 6) = 0.6; P(X = 7) = 0.1; P(X = 8) = 0.1;
```

We observe that shifting the distribution over to the right 6 units also shifts the center over 6 units: in other words, the mean of (X + 6) should equal the (mean of X) + 6. However, the spread of the distribution is unchanged: in other words, the standard deviation of (X + 6) should equal the standard deviation of X.

Again consider the random variable X with the probability distribution shown in the histogram below:

```{figure} images/image055.gif
:alt: The original histogram we began with. The vertical axis is labeled &quot;Probability&quot; and the horizontal axis is labeled &quot;X.&quot; Here is the data represented by the histogram: P(X = -2) = 0.1; P(X = -1) = 0.1; P(X = 0) = 0.6; P(X = 1) = 0.1; P(X = 2) = 0.1; So, the histogram is entire flat with probability = 0.1, except at X=0, where probability is 0.6

The original histogram we began with. The vertical axis is labeled &quot;Probability&quot; and the horizontal axis is labeled &quot;X.&quot; Here is the data represented by the histogram: P(X = -2) = 0.1; P(X = -1) = 0.1; P(X = 0) = 0.6; P(X = 1) = 0.1; P(X = 2) = 0.1; So, the histogram is entire flat with probability = 0.1, except at X=0, where probability is 0.6
```

## Subtracting a Constant from X

What would the mean and standard deviation be if we shifted the entire histogram over 7 units to the left—in other words, what are the mean and standard deviation of X - 7?

```{figure} images/image057.gif
:alt: The same histogram, except that the bars have been shifted over -7 units. This that the data now represented is: P(X = -9) = 0.1; P(X = -8) = 0.1; P(X = -7) = 0.6; P(X = -6) = 0.1; P(X = -5) = 0.1;

The same histogram, except that the bars have been shifted over -7 units. This that the data now represented is: P(X = -9) = 0.1; P(X = -8) = 0.1; P(X = -7) = 0.6; P(X = -6) = 0.1; P(X = -5) = 0.1;
```

The mean also shifts to the left by 7, from 0 to -7. The standard deviation remains unchanged at 1.

## Multiplying X by a Constant That Is > 1

What would the mean and standard deviation be if we stretched the entire histogram by 4 units—in other words, what are the mean and standard deviation of 4X?

```{figure} images/image058.gif
:alt: The histogram has been stretched by 4 times (but has not moved because the mean is at X=0). The data the histogram represents now is: P(X = -8) = 0.1; P(X = -4) = 0.1; P(X = 0) = 0.6; P(X = 4) = 0.1; P(X = 8) = 0.1;

The histogram has been stretched by 4 times (but has not moved because the mean is at X=0). The data the histogram represents now is: P(X = -8) = 0.1; P(X = -4) = 0.1; P(X = 0) = 0.6; P(X = 4) = 0.1; P(X = 8) = 0.1;
```

Multiplying X by 4 results in a mean that is 4 times the original mean. In this case, the mean transforms from 0 to 4(0) = 0. Multiplying X by 4 is tantamount to stretching the distribution by 4 units, and so the standard deviation will be 4 times the original standard deviation. In other words, the mean of 4X is 4 times the mean of X; the standard deviation of 4X is 4 times the standard deviation of X. The variance, or squared standard deviation, would be 4squared times the original variance;the variance of 4X is 16 times the variance of X.

## Multiplying X by a Constant That Is < 1

Finally, what would the mean and standard deviation be if we shrunk the entire histogram by a fourth—in other words, what are the mean and standard deviation of (1/4) X?

```{figure} images/image059.gif
:alt: The histogram has been shrunk by 4 times (but has not moved because the mean is at X=0). The data the histogram represents now is: P(X = -½) = 0.1; P(X = -¼) = 0.1; P(X = 0) = 0.6; P(X = ¼) = 0.1; P(X = ½) = 0.1;

The histogram has been shrunk by 4 times (but has not moved because the mean is at X=0). The data the histogram represents now is: P(X = -½) = 0.1; P(X = -¼) = 0.1; P(X = 0) = 0.6; P(X = ¼) = 0.1; P(X = ½) = 0.1;
```

Dividing X by 4 results in a mean that is 1/4 the original mean. In this case, the mean transforms from 0 to (1/4)(0) = 0. Dividing X by 4 is tantamount to shrinking the distribution by 4 units, and so the standard deviation will be 1/4 of the original standard deviation. In other words, the mean of (1/4)X is 1/4 times the mean of X; the standard deviation of (1/4)X is 1/4 times the standard deviation of X. The variance, or squared standard deviation, would be 1/4squared times the original variance;the variance of (1/4)X is 1/16 times the variance of X.
