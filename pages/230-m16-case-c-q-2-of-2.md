# Independent Samples vs. Matched Pairs

Furthermore, within the sub-case of comparing two means (i.e., examining the relationship between X and Y when X has only two categories) we will distinguish between two (sub-sub) cases. Here, the distinction is somewhat subtle, and has to do with how the samples from each of the two sub-populations we're comparing are chosen—in other words, what study design is implemented. We have learned that many experiments, as well as observational studies, make a comparison between two groups (sub-populations) in order to see how responses differ for the two possible categorical values. In some cases, one group (sub-population 1) has one categorical value, and *another independent group* (sub-population 2) has the other value. Independent samples are then taken from each group for comparison.

```{figure} images/gen/m16-independent-samples.svg
:alt: Sub-population 1 has mean of Y mu 1, and sub-population 2 has mean of Y mu 2. From sub-population 1 we take an SRS of size n 1, and from sub-population 2 we take a separate SRS of size n 2. The two samples are independent.
```

In other cases, a matched pairs sample design may be used, where each observation in one sample is *matched/paired/linked* with an observation in the other sample. These are sometimes called "*dependent samples*."

```{figure} images/gen/m16-matched-pairs.svg
:alt: Sub-population 1 has mean of Y mu 1, and sub-population 2 has mean of Y mu 2. Two samples of the same size n are taken, and each observation in sample 1 is paired with an observation in sample 2. The two samples are matched.
```

Matching could be by person (if the same person is measured twice), or could actually be a pair of individuals who belong together in a relevant way (husband and wife, siblings). In this design, then, the same individual or a matched pair of individuals is used to make two measurements of the response—one for each of the two categorical values.

```{admonition} Comment
:class: important

Note that in the first figure, where the samples are independent, the sample sizes of the two independent samples need not be the same (and thus we used $n_1$ and $n_2$ to indicate the two sample sizes). On the other hand, it is obvious from the design that in matched pairs the sample sizes of the two samples must be the same (and thus we used n for both).
```

:::{admonition} Example: Drinking and Driving
:class: tip

The department of motor vehicles wants to check whether drivers are impaired after drinking two beers. Consider the following two designs:

1. The reaction times (measured in seconds) in an obstacle course are measured for a group of 10 drivers who had no beer. Two beers are given to each of a different group of 9 drivers, and their reaction times on the same obstacle course are measured. (In practice, this was done by selecting a random sample of 19 drivers and randomly assigning them to one of the two groups. The random assignment guarantees, at least in theory, that the two groups are independent.)

2. The reaction times (measured in seconds) in an obstacle course are measured for 8 randomly selected drivers *before and then after* the consumption of two beers.

In the first design, we have two independent samples, and the second design is a matched pairs design, since each individual was measured twice, once before and once after. As we'll see, when we have two independent samples, the comparison of the reaction times is a comparison *between two groups*. In matched pairs, the comparison between the reaction times is done *for each individual*.
:::

To summarize:

```{note} Video
[Inference Case C-Q](https://www.youtube.com/watch?v=kvcUeWwD4Xg)
```

## Check Your Understanding: Independent, Paired, or More Than Two Groups?

Each of the following three questions is an example of a situation in case C→Q (categorical explanatory and quantitative response), and therefore calls for comparing means of several (sub-)populations. Your task is to decide which of the sub-cases of case C→Q each of the examples represents.

(*Comment:* you'll note that each of these examples is a variation on the same story, yet differs in the sub-case it represents. This was done on purpose to highlight the differences between the sub-cases.)

:::{quiz} A researcher compares the average number of hours of sleep of students at a college during exam week and during a regular week by randomly selecting 50 students and recording each student's sleep during both weeks. Which sub-case is this?
:hint: Each student is measured twice—once in each condition.
:feedback-0: Correct! The same students are measured under both conditions, so each pair of measurements is linked—a matched pairs design.
:feedback-1: The samples are not independent: the identical group of students appears in both samples.
:feedback-2: There are only two conditions (k = 2), so ANOVA is not needed.
* *Two means, matched pairs
* Two means, independent samples
* More than two means (ANOVA)
:::

:::{quiz} A researcher compares the average number of hours of sleep of male students and female students by taking a random sample of 45 male students and a separate random sample of 40 female students. Which sub-case is this?
:hint: Two separate, unrelated groups are sampled.
:feedback-0: Correct! Two separate groups (males and females) are sampled independently, and the sample sizes differ—two means from independent samples.
:feedback-1: No pairing links a specific male student to a specific female student.
:feedback-2: The explanatory variable has only two categories, so this is a two-means comparison.
* *Two means, independent samples
* Two means, matched pairs
* More than two means (ANOVA)
:::

:::{quiz} A researcher compares the average number of hours of sleep of freshmen, sophomores, juniors, and seniors, using independent random samples from each class. Which sub-case is this?
:hint: How many groups are being compared?
:feedback-0: Correct! The explanatory variable (year) has four categories, so we compare four means—the ANOVA sub-case.
:feedback-1: There are four groups here, not two.
:feedback-2: The students in different classes are different people, and no matching is involved.
* *More than two means (ANOVA)
* Two means, independent samples
* Two means, matched pairs
:::
