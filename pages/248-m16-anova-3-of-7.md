# ANOVA (3 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## The idea behind the ANOVA F-Test

Let's think about how we would go about testing whether the population means $\mu_{1},\mu_{2},\mu_{3},\mu_{4}$ are equal. It seems as if the best we could do is to calculate their point estimates—the sample mean in each of our 4 samples (denote them by $\bar{y_{1}},\bar{y_{2}},\bar{y_{3}},\bar{y_{4}}$),

```{figure} images/image7.png
:alt: For each of the four populations (Business, English, Math, and Psych majors), we wish to find the level of frustration (Y) mean, so we have taken a sample size of 35 for each population. For each sample, we have calculated Y-bar, so we have Y-bar_1, Y-bar_2, Y-bar_3, and Y-bar_4.

For each of the four populations (Business, English, Math, and Psych majors), we wish to find the level of frustration (Y) mean, so we have taken a sample size of 35 for each population. For each sample, we have calculated Y-bar, so we have Y-bar_1, Y-bar_2, Y-bar_3, and Y-bar_4.
```

and see how far apart these sample means are, or in other words, measure the variation between the sample means. If we find that the four sample means are not all close together, we'll say that we have evidence against H~o~, and otherwise, if they are close together, we'll say that we do not have evidence against H~o~. This seems quite simple, but is this enough? Let's see.

It turns out that:

* The sample mean frustration score of the 35 business majors is: $\bar{y_{1}}=7.3$

* The sample mean frustration score of the 35 English majors is: $\bar{y_{2}}=11.8$

* The sample mean frustration score of the 35 math majors is: $\bar{y_{3}}=13.2$

* The sample mean frustration score of the 35 psychology majors is: $\bar{y_{4}}=14.0$

Below we present two possible scenarios for our example. In both cases, we construct side-by-side boxplots for four groups of frustration levels that have the same variation among their means. Thus, Scenario #1 and Scenario #2 both show data for four groups with the sample means 7.3, 11.8, 13.2, and 14.0 (indicated with red marks).

```{figure} images/image111.gif
:alt: In this set of box plots, we see that for each population, the interval between the first and third quartile is very large - for Business majors, the first quartile is at about 2, and the third quartile is at about 17. The rest of the majors have smaller ranges, but they are still large, covering 10 or more frustration points. The mean for business is about 9, for English 12, mathematics 13, and psychology about a 13. Every majors' mean is in the interval of every other major's first and third quartiles.

In this set of box plots, we see that for each population, the interval between the first and third quartile is very large - for Business majors, the first quartile is at about 2, and the third quartile is at about 17. The rest of the majors have smaller ranges, but they are still large, covering 10 or more frustration points. The mean for business is about 9, for English 12, mathematics 13, and psychology about a 13. Every majors' mean is in the interval of every other major's first and third quartiles.
```

```{figure} images/image112.gif
:alt: In this set of box plots, the interval between the first and third quartile for each major is much narrower - the worse case is about 7. In addition, we also see that while the means for each major are the same as in the first set of box plots, the box plot for business does not contain any other major's mean in its first and third quartile interval. We also see that no other majors' first and third quartile interval includes business's mean. In fact, they don't even include its third quartile.

In this set of box plots, the interval between the first and third quartile for each major is much narrower - the worse case is about 7. In addition, we also see that while the means for each major are the same as in the first set of box plots, the box plot for business does not contain any other major's mean in its first and third quartile interval. We also see that no other majors' first and third quartile interval includes business's mean. In fact, they don't even include its third quartile.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

The important difference between the two scenarios is that the first represents data with a large amount of variation within each of the four groups; the second represents data with a small amount of variation within each of the four groups.

Scenario 1, because of the large amount of spread within the groups, shows boxplots with plenty of overlap. One could imagine the data arising from 4 random samples taken from 4 populations, all having the same mean of about 11 or 12. The first group of values may have been a bit on the low side, and the other three a bit on the high side, but such differences could conceivably have come about by chance. This would be the case if the null hypothesis, claiming equal population means, were true. Scenario 2, because of the small amount of spread within the groups, shows boxplots with very little overlap. It would be very hard to believe that we are sampling from four groups that have equal population means. This would be the case if the null hypothesis, claiming equal population means, were false.

Thus, in the language of hypothesis tests, we would say that if the data were configured as they are in scenario 1, we would not reject the null hypothesis that population mean frustration levels were equal for the four majors. If the data were configured as they are in scenario 2, we would reject the null hypothesis, and we would conclude that mean frustration levels differ, depending on major.

Let's summarize what we learned from this. The question we need to answer is: Are the differences among the sample means ($\bar{Y}$'s) due to true differences among the μ's (alternative hypothesis), or merely due to sampling variability (null hypothesis)?

In order to answer this question using our data, we obviously need to look at the variation among the sample means, but this alone is not enough. We need to look at the variation among the sample means relative to the variation within the groups. In other words, we need to look at the quantity:

```{figure} images/image163.gif
:alt: variation among sample means / variation within groups

variation among sample means / variation within groups
```

which measures to what extent the difference among the sampled groups' means dominates over the usual variation within sampled groups (which reflects differences in individuals that are typical in random samples).

When the variation within groups is large (like in scenario 1), the variation (differences) among the sample means could become negligible and the data provide very little evidence against H~o~. When the variation within groups is small (like in scenario 2), the variation among the sample means dominates over it, and the data have stronger evidence against H~o~.

Looking at this ratio of variations is the idea behind the comparing more than two means; hence the name analysis of variance (ANOVA).

Now that we understand the idea behind the ANOVA F-test, let's move on to step 2. We'll start by talking about the test statistic, since it will be a natural continuation of what we've just discussed, and then move on to talk about the conditions under which the ANOVA F-test can be used. In practice, however, the conditions need to be checked first, as we did before.
