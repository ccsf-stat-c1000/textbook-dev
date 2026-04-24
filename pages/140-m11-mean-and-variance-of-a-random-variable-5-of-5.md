# Mean and Variance of a Random Variable (5 of 5)

```{admonition} Learning Objectives
    - Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

The concept of standard deviation is a bit harder to grasp than that of the mean. The purpose of the following examples and activities is to help you gain a better feel for the standard deviation of a random variable:

```{admonition} Example: Xavier's and Yves' Production Lines
    Recall the probability distribution of the random variable X, representing the number of defective parts per hour produced by Xavier's production line, and the probability distribution of the random variable Y, representing the number of defective parts per hour produced by Yves' production line:

    ```{figure} images/image039.gif
    :alt: Two probability distribution tables. The first has two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10; The second table also has two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .05; 1: .05; 2: .10; 3: .75; 4: .05;

    Two probability distribution tables. The first has two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10; The second table also has two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .05; 1: .05; 2: .10; 3: .75; 4: .05;
    ```

    Look carefully at both probability distributions. Both X and Y take the same possible values (0, 1, 2, 3, 4). However, they are very different in the way the probability is distributed among these values. We saw before that this makes a difference in means:

    $\mu_{X}=1.8$

    $\mu_{Y}=2.7$

    We now want to get a sense about how the different probability distributions impact their standard deviations.

    Recall that the standard deviation of a random variable can be interpreted as a typical (or the long-run average) distance between the value of X and its mean.

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```

    So, 75% of the time Y will assume a value (3) that is very close to its mean (2.7), while X will assume a value (2) that is close to its mean (1.8) much less often—only 25% of the time. The long-run average, then, of the distance between the values of Y and their mean will be much smaller than the long-run average of the distance between the values of X and their mean.

    Therefore, $\sigma_{Y}<\sigma_{X}=1.21$ Actually, $\sigma_{Y}=0.85$, so we can draw the following conclusion:

    Yves' production line produces an average of 2.70 defective parts per hour. The number of defective parts varies from hour to hour; typically (or, on average), it is about .85 away from 2.70.
```

## Summary

Here are the histograms for the production lines:

```{figure} images/image_xavier_histo_mean.jpg
:alt: Histogram for Xavier's production line. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The data in the histogram is the same as the data in the probability table for Xavier's line. Moving from left to right across the horizontal axis we see that a peak in probability is reached at X=1, but it is not much higher than X=0. In addition, going right from X=1, the values decay, ultimately to 0.10 at X=4. The mean for Xavier's line is at X=1.8 .

Histogram for Xavier's production line. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The data in the histogram is the same as the data in the probability table for Xavier's line. Moving from left to right across the horizontal axis we see that a peak in probability is reached at X=1, but it is not much higher than X=0. In addition, going right from X=1, the values decay, ultimately to 0.10 at X=4. The mean for Xavier's line is at X=1.8 .
```

```{figure} images/image_yves_histo_mean.jpg
:alt: For Yves's line is another histogram with the same axes. Going left to right, we see a peak at X=3, which is much higher than the other values. All of the other values are roughly the same. The mean is at X=2.7 .

For Yves's line is another histogram with the same axes. Going left to right, we see a peak at X=3, which is much higher than the other values. All of the other values are roughly the same. The mean is at X=2.7 .
```

When we compare distributions, the distribution in which it is *more likely* to find values that are further from the mean will have a *larger* standard deviation. Likewise, the distribution in which it is *less likely* to find values that are further from the mean will have the *smaller* standard deviation.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

The following graphs will be used in the next "Did I Get This?" exercise.

```{figure} images/u4_m3_meanvariance5_digt_imagea.jpg
:alt: A histogram titled "Graph A" showing the following data (presented in "horizontal value: vertical value format"): 1: .07; 2: .10; 3: .12; 4: .13; 5: .16; 6: .13; 7: .12; 8: .10; 9: .07;

A histogram titled "Graph A" showing the following data (presented in "horizontal value: vertical value format"): 1: .07; 2: .10; 3: .12; 4: .13; 5: .16; 6: .13; 7: .12; 8: .10; 9: .07;
```

```{figure} images/u4_m3_meanvariance5_digt_imageb.jpg
:alt: A histogram titled "Graph B" showing the following data (presented in "horizontal value: vertical value format"): 1: .02; 2: .08; 3: .10; 4: .15; 5: .30; 6: .15; 7: .10; 8: .08; 9: .02;

A histogram titled "Graph B" showing the following data (presented in "horizontal value: vertical value format"): 1: .02; 2: .08; 3: .10; 4: .15; 5: .30; 6: .15; 7: .10; 8: .08; 9: .02;
```

```{figure} images/u4_m3_meanvariance5_digt_imagec.jpg
:alt: A histogram titled "Graph C" showing the following data (presented in "horizontal value: vertical value format"): 1: .01; 2: .01; 3: .10; 4: .18; 5: .40; 6: .18; 7: .10; 8: .01; 9: .01;

A histogram titled "Graph C" showing the following data (presented in "horizontal value: vertical value format"): 1: .01; 2: .01; 3: .10; 4: .18; 5: .40; 6: .18; 7: .10; 8: .01; 9: .01;
```

```{figure} images/u4_m3_meanvariance5_digt_imaged.jpg
:alt: A histogram titled "Graph D" showing the following data (presented in "horizontal value: vertical value format"): 1: .01; 2: .01; 3: .02; 4: .11; 5: .70; 6: .11; 7: .02; 8: .01; 9: .01;

A histogram titled "Graph D" showing the following data (presented in "horizontal value: vertical value format"): 1: .01; 2: .01; 3: .02; 4: .11; 5: .70; 6: .11; 7: .02; 8: .01; 9: .01;
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

##### Comment

As we have stated before, using the mean and standard deviation gives us another way to assess which values of a random variable are unusual. Any values of a random variable that fall within 2 standard deviations of the mean would be considered ordinary (not unusual).

```{admonition} Example: Xavier's Production
                        Line—Unusual
                        or Not?
    Looking once again at the probability distribution for Xavier's production line:

    ```{figure} images/image_xavier_histo_mean.jpg
    :alt: Histogram for Xavier's production line. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The data in the histogram is the same as the data in the probability table for Xavier's line. Moving from left to right across the horizontal axis we see that a peak in probability is reached at X=1, but it is not much higher than X=0. In addition, going right from X=1, the values decay, to about 0.10 at X=4. The mean for Xavier's line is at X=1.8 .

    Histogram for Xavier's production line. The vertical axis is labeled "Probability" and the horizontal axis is labeled "X." The data in the histogram is the same as the data in the probability table for Xavier's line. Moving from left to right across the horizontal axis we see that a peak in probability is reached at X=1, but it is not much higher than X=0. In addition, going right from X=1, the values decay, to about 0.10 at X=4. The mean for Xavier's line is at X=1.8 .
    ```

    Would it be considered unusual to have 4 defective parts per hour?

    We know that $\mu_{X}=1.8$ and $\sigma_{X}=1.21$.

    Ordinary values are within 2 standard deviations of the mean. 1.8 - 2(1.21) = -.62 and 1.8 + 2(1.21) = 4.22. This gives us an interval from -.62 to 4.22. Since we cannot have a negative number of defective parts, the interval is essentially from 0 to 4.22. Because 4 is within this interval, it would be considered ordinary. Therefore, it is *not unusual*.

    Would it be considered unusual to have no defective parts? Zero is within 2 standard deviations of the mean, so it would not be considered unusual to have no defective parts.
```

The following activity will reinforce this idea.

## Learn By Doing

Recall the probability distribution for changing majors.

We have made the following calculations for the mean and standard deviation. For some extra practice, feel free to verify our calculations.

$\mu_{X}=1.23$ and $\sigma_{X}=1.08$

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

"Risk" in investments provides a useful application for the concept of variability. If there is no variability at all in possible outcomes, then the outcome is something we can count on, with no risk involved. At the other extreme, if there is a large amount of variability with possibilities for either tremendous loss or gain, then the associated risk is quite high.

If a variable's possible values just differ somewhat, with some only marginally favorable and others unfavorable, then the underlying random experiment entails just a moderate amount of risk. The following example demonstrates how differing values of standard deviation reflect the amount of risk in a situation.

```{admonition} Example: Comparing Investments
    Consider three possible investments, with returns denoted as X, Y, and Z, respectively, and probability distributions outlined in the tables below.

    ```{figure} images/image043.gif
    :alt: A probability table with has two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 14,000: 1; In other words, X only has one value, 14,000, and P(X=14,000) = 1.

    A probability table with has two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 14,000: 1; In other words, X only has one value, 14,000, and P(X=14,000) = 1.
    ```

    Investment X is what we'd call a "sure thing," with a guaranteed return of $14,000: there is no risk involved at all.

    ```{figure} images/image044.gif
    :alt: A probability table with two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .98; 1,000,000: .02; In other words, P(Y = 0) = .98 and P(Y = 1,000,000) = .02

    A probability table with two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .98; 1,000,000: .02; In other words, P(Y = 0) = .98 and P(Y = 1,000,000) = .02
    ```

    Investment Y is extremely risky, with a high probability (.98) of no gain at all, contrasted by a slight probability (.02) of "making a killing" with a return of a million dollars.

    ```{figure} images/image045.gif
    :alt: A probability table with two rows, labeled "Z" and "P(Z=z)." The data in column format (Y: P(Z=z)): 10,000: .5; 20,000: .5; In other words, P(Z = 10,000) = .5 and P(Z = 20,000) = .5

    A probability table with two rows, labeled "Z" and "P(Z=z)." The data in column format (Y: P(Z=z)): 10,000: .5; 20,000: .5; In other words, P(Z = 10,000) = .5 and P(Z = 20,000) = .5
    ```

    Investment Z is somewhere in between: there is an equal chance for either a return that's on the low side or a return that's on the high side.

    If you only consider the mean return on each investment, would you prefer X, Y, or Z? The means for X, Y, and Z are calculated as follows:

    $\mu_{X}=14000(1)=14000$

    $\mu_{Y}=0(0.98)+1000000(0.02)=20000$

    $\mu_{z}=10000(0.5)+20000(0.5)=15000$

    Clearly, the mean return for Y is highest, and so investment in Y would seem to be preferable.

    Now consider the standard deviations, and consider which investment you'd prefer—X, Y, or Z.

    The standard deviations are:

    $\sigma_{x}^{2}=(14000-14000)^{2}(1)=0$

    $\sigma_{x}=0$

    $\sigma_{Y}^{2}=(0-20000)^{2}(0.98)+(1,000,000-20000)^{2}(0.02)=1.96\times10^{10}$

    $\sigma_{Y}=140,000$

    $\sigma_{z}^{2}=(10000-15000)^{2}(0.5)+(20000-15000)^{2}(0.5)=25,000,000$

    $\sigma_{z}=5000$

    Granted, the mean returns suggest that investment X is least profitable and investment Y is most profitable. On the other hand, the standard deviations are telling us that the return for X is a sure thing; for Y, the remote chance of making a huge profit is offset by a high risk of losing the investment entirely; for Z, there is a modest amount of risk involved. If you can't afford to lose any money, then investment X would be the way to go. If you have enough assets to take a chance, then investment Y would be worthwhile. In particular, if a large company routinely makes many such investments, then in the long run there will occasionally be such enormous gains that the company is willing to absorb many smaller losses. Investment Z represents the middle ground, somewhere between the other two.
```

## Section Questions

```{note}
    **My Response**

    About the Mean and Variance of a Random Variable

    *(Interactive activity — available in the OLI platform)*
```
