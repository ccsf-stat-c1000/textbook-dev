# The Variance and Standard Deviation of a Random Variable

```{admonition} Learning Objectives
:class: note

- Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

## Variance and Standard Deviation of a Discrete Random Variable

In Exploratory Data Analysis, we used the mean of a sample of quantitative values (their arithmetic average, $\bar{x}$) to tell the center of their distribution, and the standard deviation (s) to tell the typical distance of sample values from their mean. We described the center of a probability distribution for a random variable by reporting its mean $\mu_{X}$, and now we would like to establish an accompanying measure of spread. Our measure of spread will still report the typical distance of values from their means, but in order to distinguish the spread of a population of all of a random variable's values from the spread (s) of sample values, we will denote the standard deviation of the random variable X with the Greek lower case "sigma," and use a subscript to remind us what is the variable of interest (there may be more than one in later problems): $\sigma_X$.

We will also focus more frequently than before on the squared standard deviation, called the *variance*, because some important rules we need to invoke are in terms of variance $\sigma_{X}^{2}$ rather than standard deviation $\sigma_{X}$.

:::{admonition} Example: Xavier's Production Line
:class: tip

Recall that the number of defective parts produced each hour by Xavier's production line is a random variable X with the following probability distribution:

| x | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| P(X = x) | 0.15 | 0.30 | 0.25 | 0.20 | 0.10 |

We found the mean number of defective parts produced per hour to be $\mu_{X}$ = 1.8. Obviously, there is variation about this mean: some hours as few as 0 defective parts are produced, whereas in other hours as many as 4 are produced. Typically, how far does the number of defective parts fall from the mean of 1.8? As we did for the spread of sample values, we measure the spread of a random variable by calculating the square root of the average squared deviation from the mean. Now "average" is a weighted average, where more probable values of the random variable are accordingly given more weight. Let's begin with the variance, or average squared deviation from the mean, and then take its square root to find the standard deviation:

| x | Deviation from mean | Squared deviation | P(X = x) |
| --- | --- | --- | --- |
| 0 | (0 − 1.8) | (0 − 1.8)² | 0.15 |
| 1 | (1 − 1.8) | (1 − 1.8)² | 0.30 |
| 2 | (2 − 1.8) | (2 − 1.8)² | 0.25 |
| 3 | (3 − 1.8) | (3 − 1.8)² | 0.20 |
| 4 | (4 − 1.8) | (4 − 1.8)² | 0.10 |

$$\sigma_{X}^{2}=(0-1.8)^{2}(0.15)+(1-1.8)^{2}(0.30)+(2-1.8)^{2}(0.25)+(3-1.8)^{2}(0.20)+(4-1.8)^{2}(0.1)=1.46$$

$$\sigma_{X}=\sqrt{1.46}=1.21$$
:::

How do we interpret the standard deviation of X?

Xavier's production line produces an average of 1.80 defective parts per hour. The number of defective parts varies from hour to hour; typically (or, on average), it is about 1.21 away from 1.80.

Here is the formal definition:

```{admonition} Definition: Variance and Standard Deviation of a Discrete Random Variable
:class: note

For any discrete random variable X with probability distribution assigning probability $p_i$ to value $x_i$, the *variance* of X is defined to be

$$\sigma_{X}^{2}=(x_{1}-\mu_{X})^{2}p_{1}+(x_{2}-\mu_{X})^{2}p_{2}+\cdots+(x_{n}-\mu_{X})^{2}p_{n}=\sum_{i=1}^{n}(x_{i}-\mu_{X})^{2}p_{i}$$

and the *standard deviation* is

$$\sigma_{X}=\sqrt{\sigma_{X}^{2}}$$
```

## Check Your Understanding: The Standard Deviation of a Random Variable

:::{quiz} A random variable takes the value 1 with probability 0.5 and the value 3 with probability 0.5, so its mean is 2. What is its standard deviation?
:hint: Each value deviates from the mean by exactly 1.
:feedback-0: Correct! σ² = (1−2)²(0.5) + (3−2)²(0.5) = 1, so σ = 1—each value is exactly 1 away from the mean.
:feedback-1: 2 is the mean, not the spread.
:feedback-2: 0.5 is each value's probability, not the typical deviation.
* *1
* 2
* 0.5
:::

:::{quiz} Recall Yves' production line: values 0-4 with probabilities 0.05, 0.05, 0.10, 0.75, 0.05, mean 2.7. Without computing, how should Yves' standard deviation compare to Xavier's (σ = 1.21)?
:hint: How concentrated is Yves' distribution around its mean?
:feedback-0: Correct! Yves' distribution piles 75% of its probability on the single value 3, right next to its mean, so its typical deviation is much smaller. (In fact σ(Y) ≈ 0.9.)
:feedback-1: More concentration around the mean means less spread, not more.
:feedback-2: The two distributions have very different spreads despite sharing the same possible values.
* *Smaller—Yves' distribution is much more concentrated around its mean
* Larger—Yves' mean is larger
* About the same—they have the same possible values
:::
