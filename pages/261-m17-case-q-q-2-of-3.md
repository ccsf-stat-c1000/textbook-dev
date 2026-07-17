# Testing for a Linear Relationship

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
- Specify the null and alternative hypotheses for comparing relationships.
```

Let's introduce our leading example, which was actually our leading example in the Exploratory Data Analysis unit as well.

:::{admonition} Example: Highway Sign Legibility
:class: tip

In a study of the legibility and visibility of highway signs, a Pennsylvania research firm determined the maximum distance at which each of 30 drivers could read a newly designed sign. The 30 participants in the study ranged in age from 18 to 82 years old. The government agency that funded the research hoped to improve highway safety for older drivers, and wanted to examine the relationship between age and sign legibility distance. (Data adapted with permission from Utts and Heckard, *Mind on Statistics*.)

Let's go through the entire process (outlined on the previous page) for this example.

*Starting point:* the researchers wanted to examine the relationship between age (X) and sign legibility distance (Y) in the population of drivers. The researchers collected data from a random sample of 30 drivers—for example: age 18, distance 510 feet; age 20, distance 590; age 22, distance 560; ...; age 79, distance 310; age 82, distance 360.

*Exploratory analysis:* the researchers display the data on a scatterplot:

```{figure} images/gen/m05-signs-scatterplot.svg
:alt: A scatterplot of legibility distance versus driver age. The points show a fairly strong negative linear relationship: as age increases, the maximum distance at which the sign can be read decreases.
```

They observe a negative linear relationship in the data. In order to quantify the strength of that linear relationship, the researchers supplement the scatterplot with a numerical measure—the correlation coefficient—which turns out to be r = −0.8, confirming the researchers' visual assessment of a negative, fairly strong linear relationship between age and legibility distance.
:::

*Inference:* the researchers would now like to see whether the observed linear relationship between age and legibility distance can be generalized to the entire population of drivers. In other words, the researchers want to check whether the observed linearity is due to true linearity in the population, or a pattern that could have happened just by chance.

The test that the researchers are going to carry out is a t-test (most commonly known as the "t-test for the slope," for reasons that we are not going to get into), which tests the following two hypotheses (*step 1*):

- $H_0$: There is no linear relationship between age and distance.
- $H_a$: There is a linear relationship between age and distance.

And in general:

- $H_0$: There is no linear relationship between X and Y.
- $H_a$: There is a linear relationship between X and Y.

```{admonition} Comments
:class: important

1. As we mentioned earlier, we are going to keep this discussion on the qualitative side, and in particular we will not go very deeply into *step 2* of the hypothesis test. As for the *test statistic* in this case, we'll just say that the test is a t-test, which, as we know, means that the null distribution of its test statistic (under which the p-values are calculated) is some t distribution.

2. We are also going to focus on only some of the *conditions* that allow us to safely use this t-test. They are: the observed data indeed look linear (otherwise it would not make sense to try to generalize a linear relationship); the observations are independent; there are no extreme outliers in the data; and the sample size is fairly large.

   Note that in our example all these conditions are met: the data definitely look linear, the observations (drivers) are independent of each other (since they were randomly chosen), there are no extreme observations in the data, and a sample size of n = 30 is fairly large.
```

For *step 3*, the researchers use statistical software to find a test statistic value of −7.09 and a p-value that is so small that it is essentially 0. This means that it would be extremely unlikely to get data like those observed if age and legibility distance were not linearly related. In other words, it would be extremely unlikely to get data like those observed just by chance.

The researchers conclude (*step 4*) that since the p-value is so small, the data provide extremely strong evidence to reject $H_0$, and conclude that age and legibility distance are linearly related.

```{admonition} Note: r vs. the P-value
:class: note

It is important to distinguish between the information provided by r and by the p-value. The correlation coefficient *r informs us about the strength of the linear relationship in the data*: close to +1 or −1 for a strong linear relationship, close to 0 for a weak one. In contrast, the regression *p-value informs us about the strength of evidence* that there is a linear relationship in the population from which the data were obtained.

In our example, since the p-value is essentially 0 and r = −0.8, we would say that we have extremely strong evidence of a fairly strong (negative) relationship between age and distance in the population of drivers.
```

## Did I Get This?

In a study of the relationship between the cry count of newborns and their IQ at age three, we have found the following: the correlation coefficient of the observed data is r = 0.4, and the p-value of the test ($H_0$: there is no linear relationship between cry count and IQ vs. $H_a$: there is a linear relationship) is p = 0.012.

:::{quiz} Which is the correct way to describe these results?
:hint: r describes the strength of the relationship in the data; the p-value describes the strength of the evidence for a relationship in the population.
:feedback-0: Correct! The small p-value (0.012) gives quite strong evidence that SOME linear relationship exists, while r = 0.4 tells us the relationship observed is only moderate in strength.
:feedback-1: This reverses the roles: r measures the strength of the relationship, and the p-value measures the strength of the evidence.
:feedback-2: A significant p-value does not mean the relationship is strong—r = 0.4 indicates a moderate relationship at best.
* *Quite strong evidence of a moderate linear relationship between cry count and IQ
* Moderate evidence of a strong linear relationship
* Strong evidence of a strong linear relationship
:::

:::{quiz} Suppose a different study finds r = 0.15 with a p-value of 0.001, based on a very large sample. What is the correct interpretation?
:hint: A large sample can produce strong evidence for even a weak relationship.
:feedback-0: Correct! The tiny p-value provides very strong evidence that a linear relationship exists, but r = 0.15 says that relationship is weak—statistical significance does not imply practical strength.
:feedback-1: The p-value cannot strengthen the relationship itself—r = 0.15 is weak no matter how significant.
:feedback-2: The results are not contradictory: with enough data, even weak relationships become clearly detectable.
* *Very strong evidence of a weak linear relationship
* Evidence of a strong linear relationship, since the p-value is tiny
* The results contradict each other, so an error must have occurred
:::
