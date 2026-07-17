# Same Mean, Different Risk: Comparing Random Variables

```{admonition} Learning Objectives
:class: note

- Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

The concept of standard deviation is a bit harder to grasp than that of the mean. The purpose of the following examples and activities is to help you gain a better feel for the standard deviation of a random variable:

:::{admonition} Example: Xavier's and Yves' Production Lines
:class: tip

Recall the probability distributions of the random variable X, representing the number of defective parts per hour produced by Xavier's production line, and the random variable Y, representing the number of defective parts per hour produced by Yves' production line:

| x | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| P(X = x) | 0.15 | 0.30 | 0.25 | 0.20 | 0.10 |

| y | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| P(Y = y) | 0.05 | 0.05 | 0.10 | 0.75 | 0.05 |

Look carefully at both probability distributions. Both X and Y take the same possible values (0, 1, 2, 3, 4). However, they are very different in the way the probability is distributed among these values. We saw before that this makes a difference in means:

$$\mu_{X}=1.8 \qquad \mu_{Y}=2.7$$

We now want to get a sense about how the different probability distributions impact their standard deviations. Recall that the standard deviation of a random variable can be interpreted as a typical (or the long-run average) distance between the value of X and its mean.

75% of the time, Y will assume a value (3) that is very close to its mean (2.7), while X will assume a value (2) that is close to its mean (1.8) much less often—only 25% of the time. The long-run average, then, of the distance between the values of Y and their mean will be much smaller than the long-run average of the distance between the values of X and their mean.

Therefore, $\sigma_{Y}<\sigma_{X}=1.21$. Actually, $\sigma_{Y}=0.85$, so we can draw the following conclusion:

Yves' production line produces an average of 2.70 defective parts per hour. The number of defective parts varies from hour to hour; typically (or, on average), it is about 0.85 away from 2.70.
:::

## Summary

Here are the histograms for the production lines:

```{figure} images/gen/m11-xavier-hist.svg
:alt: The probability histogram for Xavier's production line, with bars of heights 0.15, 0.30, 0.25, 0.20, and 0.10 for the values 0 through 4, and a dashed red line marking the mean at 1.8. The probability is spread out across the values.
```

```{figure} images/gen/m11-yves-hist.svg
:alt: The probability histogram for Yves' production line, with a dominant bar of height 0.75 at the value 3 and small bars elsewhere, and a dashed red line marking the mean at 2.7. The probability is concentrated near the mean.
```

When we compare distributions, the distribution in which it is *more likely* to find values that are further from the mean will have a *larger* standard deviation. Likewise, the distribution in which it is *less likely* to find values that are further from the mean will have the *smaller* standard deviation.

The following graphs will be used in the next "Did I Get This?" exercise. Each shows a symmetric distribution on the values 1 through 9, centered at 5:

```{figure} images/gen/m11-spread-graphs.svg
:alt: Four probability histograms, labeled Graph A through Graph D, each symmetric around the value 5. Graph A is nearly flat and widely spread, Graph B has a moderate central peak, Graph C has a strong central peak, and Graph D concentrates almost all its probability at the value 5.
```

:::{quiz} All four distributions have mean 5. Which graph has the SMALLEST standard deviation, and which has the LARGEST?
:hint: Where is the probability more concentrated around the mean?
:feedback-0: Correct! Graph D piles nearly all its probability on the mean itself (smallest spread), while Graph A spreads probability almost evenly across all values (largest spread).
:feedback-1: It's the reverse: concentration near the mean means a small standard deviation.
:feedback-2: Graphs B and C are intermediate; the extremes are D (most concentrated) and A (most spread out).
* *Smallest: Graph D; Largest: Graph A
* Smallest: Graph A; Largest: Graph D
* Smallest: Graph B; Largest: Graph C
:::

## Comment

As we have stated before, using the mean and standard deviation gives us another way to assess which values of a random variable are unusual. Any values of a random variable that fall within 2 standard deviations of the mean would be considered ordinary (not unusual).

:::{admonition} Example: Xavier's Production Line—Unusual or Not?
:class: tip

Looking once again at the probability distribution for Xavier's production line: would it be considered unusual to have 4 defective parts per hour?

We know that $\mu_{X}=1.8$ and $\sigma_{X}=1.21$.

Ordinary values are within 2 standard deviations of the mean. 1.8 − 2(1.21) = −0.62 and 1.8 + 2(1.21) = 4.22. This gives us an interval from −0.62 to 4.22. Since we cannot have a negative number of defective parts, the interval is essentially from 0 to 4.22. Because 4 is within this interval, it would be considered ordinary. Therefore, it is *not unusual*.

Would it be considered unusual to have no defective parts? Zero is within 2 standard deviations of the mean, so it would not be considered unusual to have no defective parts.
:::

The following activity will reinforce this idea.

## Learn By Doing

Recall the probability distribution for changing majors. We have made the following calculations for the mean and standard deviation. For some extra practice, feel free to verify our calculations.

$$\mu_{X}=1.23 \qquad \sigma_{X}=1.08$$

:::{quiz} Using the 2-standard-deviations criterion, would changing majors 4 times be considered unusual?
:hint: Compute μ + 2σ = 1.23 + 2(1.08).
:feedback-0: Correct! The ordinary range extends up to 1.23 + 2(1.08) = 3.39, and 4 falls above it—so changing majors 4 times is unusual.
:feedback-1: Compare 4 with the upper limit 3.39: it falls outside the ordinary range.
* *Yes—4 is more than 2 standard deviations above the mean (above 3.39)
* No—4 is within 2 standard deviations of the mean
:::

"Risk" in investments provides a useful application for the concept of variability. If there is no variability at all in possible outcomes, then the outcome is something we can count on, with no risk involved. At the other extreme, if there is a large amount of variability with possibilities for either tremendous loss or gain, then the associated risk is quite high.

If a variable's possible values just differ somewhat, with some only marginally favorable and others unfavorable, then the underlying random experiment entails just a moderate amount of risk. The following example demonstrates how differing values of standard deviation reflect the amount of risk in a situation.

:::{admonition} Example: Comparing Investments
:class: tip

Consider three possible investments, with returns denoted as X, Y, and Z, respectively, and probability distributions outlined in the tables below.

| x | 14,000 |
| --- | --- |
| P(X = x) | 1 |

Investment X is what we'd call a "sure thing," with a guaranteed return of \$14,000: there is no risk involved at all.

| y | 0 | 1,000,000 |
| --- | --- | --- |
| P(Y = y) | 0.98 | 0.02 |

Investment Y is extremely risky, with a high probability (0.98) of no gain at all, contrasted by a slight probability (0.02) of "making a killing" with a return of a million dollars.

| z | 10,000 | 20,000 |
| --- | --- | --- |
| P(Z = z) | 0.5 | 0.5 |

Investment Z is somewhere in between: there is an equal chance for either a return that's on the low side or a return that's on the high side.

If you only consider the mean return on each investment, would you prefer X, Y, or Z? The means for X, Y, and Z are calculated as follows:

$$\mu_{X}=14000(1)=14000$$

$$\mu_{Y}=0(0.98)+1000000(0.02)=20000$$

$$\mu_{Z}=10000(0.5)+20000(0.5)=15000$$

Clearly, the mean return for Y is highest, and so investment in Y would seem to be preferable.

Now consider the standard deviations, and consider which investment you'd prefer—X, Y, or Z. The standard deviations are:

$$\sigma_{X}^{2}=(14000-14000)^{2}(1)=0 \implies \sigma_{X}=0$$

$$\sigma_{Y}^{2}=(0-20000)^{2}(0.98)+(1{,}000{,}000-20000)^{2}(0.02)=1.96\times10^{10} \implies \sigma_{Y}=140{,}000$$

$$\sigma_{Z}^{2}=(10000-15000)^{2}(0.5)+(20000-15000)^{2}(0.5)=25{,}000{,}000 \implies \sigma_{Z}=5000$$

Granted, the mean returns suggest that investment X is least profitable and investment Y is most profitable. On the other hand, the standard deviations are telling us that the return for X is a sure thing; for Y, the remote chance of making a huge profit is offset by a high risk of losing the investment entirely; for Z, there is a modest amount of risk involved. If you can't afford to lose any money, then investment X would be the way to go. If you have enough assets to take a chance, then investment Y would be worthwhile. In particular, if a large company routinely makes many such investments, then in the long run there will occasionally be such enormous gains that the company is willing to absorb many smaller losses. Investment Z represents the middle ground, somewhere between the other two.
:::
