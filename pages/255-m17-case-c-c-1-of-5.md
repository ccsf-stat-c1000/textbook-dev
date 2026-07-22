# Case C→C: Relationships Between Categorical Variables

```{admonition} Learning Objectives
:class: note

- Choose the appropriate inferential method for examining the relationship between two variables and justify the choice.
```

## Inference for the Relationship Between Two Categorical Variables (Chi-Square Test for Independence)

### Overview

The last three procedures that we studied (two-sample t, paired t, and ANOVA) all involve the relationship between a categorical explanatory variable and a quantitative response variable, corresponding to case C→Q in the role-type classification table. Next, we will consider inferences about the relationships between *two categorical variables*, corresponding to case C→C.

```{figure} images/gen/m05-role-type-cc.svg
:alt: The role-type classification table with the C to C case highlighted: a categorical explanatory variable paired with a categorical response variable.
```

In the Exploratory Data Analysis unit of the course, we summarized the relationship between two categorical variables for a given data set (using a two-way table and conditional percents), without trying to generalize beyond the sample data.

Now we perform statistical inference for two categorical variables, using the sample data to draw conclusions about whether or not we have evidence that the variables are related in the larger population from which the sample was drawn. In other words, we would like to assess whether the relationship between X and Y that we observed in the data is due to a real relationship between X and Y in the population, or if it is something that could have happened just by chance due to sampling variability.

The statistical test that will answer this question is called the *chi-square test for independence*. Chi is a Greek letter that looks like this: χ, so the test is sometimes referred to as the χ² test for independence.

The structure of this section will be very similar to that of the previous ones in this module. We will first present our leading example, and then introduce the chi-square test by going through its 4 steps, illustrating each one using the example. We will conclude by presenting another complete example.

Let's start with our leading example.

:::{admonition} Example: Drunk Driving and Gender
:class: tip

In the early 1970s, a young man challenged an Oklahoma state law that prohibited the sale of 3.2% beer to males under age 21 but allowed its sale to females in the same age group. The case (*Craig v. Boren*, 429 U.S. 190, 1976) was ultimately heard by the U.S. Supreme Court.

The main justification provided by Oklahoma for the law was traffic safety. One of the 3 main pieces of data presented to the court was the result of a "random roadside survey" that recorded information on gender, and whether or not the driver had been drinking alcohol in the previous two hours. There were a total of 619 drivers under 20 years of age included in the survey.

The data were recorded driver by driver (gender and whether the driver had been drinking), and the following two-way table summarizes the observed counts in the roadside survey:

| | Drank alcohol: Yes | Drank alcohol: No | Total |
| --- | --- | --- | --- |
| **Male** | 77 | 404 | 481 |
| **Female** | 16 | 122 | 138 |
| **Total** | 93 | 526 | 619 |

Our task is to assess whether these results provide evidence of a significant ("real") relationship between gender and drunk driving. Since we are looking to see whether drunk driving is related to gender, our explanatory variable (X) is gender, and the response variable (Y) is drunk driving. Both variables are two-valued categorical variables, and therefore our two-way table of observed counts is 2-by-2. It should be mentioned that the chi-square procedure is not limited to 2-by-2 situations, but can be applied to any r-by-c situation, where r is the number of rows (corresponding to the number of values of one of the variables) and c is the number of columns (corresponding to the number of values of the other variable).

*Exploratory analysis*

Before we introduce the chi-square test, let's conduct an exploratory data analysis. Recall that the key to reporting appropriate summaries for a two-way table is deciding which of the two categorical variables plays the role of explanatory variable, and then calculating the conditional percentages—the percentages of the response variable for each value of the explanatory variable—separately. In this case, since the explanatory variable is gender, we calculate the percentages of drivers who did (and did not) drink alcohol for males and females separately:

| | Drank alcohol: Yes | Drank alcohol: No | Total |
| --- | --- | --- | --- |
| **Male** | 77/481 = 16.0% | 404/481 = 84.0% | 100% |
| **Female** | 16/138 = 11.6% | 122/138 = 88.4% | 100% |

For the 619 sampled drivers, a larger percentage of males were found to have been drinking than females (16.0% vs. 11.6%). Our data, in other words, provide some evidence that drunk driving is related to gender; however, this in itself is not enough to conclude that such a relationship exists in the larger population of drivers under 20. We need to further investigate the data and decide between the following two points of view:

- The evidence provided by the roadside survey (16.0% vs. 11.6%) is strong enough to conclude (beyond a reasonable doubt) that it must be due to a relationship between drunk driving and gender in the population of drivers under 20.
- The evidence provided by the roadside survey (16.0% vs. 11.6%) is not strong enough to make that conclusion, and could have happened just by chance, due to sampling variability, and not necessarily because a relationship exists in the population.
:::

Actually, these two opposing points of view constitute the null and alternative hypotheses of the chi-square test for independence. So now that we understand our example and what we still need to find out, let's introduce the four-step process of this test.

## Check Your Understanding: Exploring a Relationship Between Categorical Variables

The purpose of this activity is to introduce you to the example that you are going to work through in this section, and for you to get a feeling for the data by conducting exploratory analysis.

*Background: alcoholism risk in 9/11 responders.* Among firefighters and other "first responders" to the World Trade Center on September 11, 2001, there have been reports of increased alcohol-related difficulties. A survey of New York firefighters conducted by Cornell researcher Samuel Bacharach was released in 2004. Based on the research, we can construct the following two-way table of observed counts:

| | No risk for alcohol problems | Moderate to severe risk | Total |
| --- | --- | --- | --- |
| **Participated in 9/11 rescue** | 793 | 309 | 1,102 |
| **Did not participate** | 441 | 110 | 551 |
| **Total** | 1,234 | 419 | 1,653 |

Using the data from this research, we would like to investigate whether alcohol risk among New York firefighters is significantly related to participation in the 9/11 rescue.

:::{quiz} Which variable is the explanatory variable, and which is the response?
:hint: Which variable might affect the other?
:feedback-0: Correct! Participation in the 9/11 rescue (X) may affect alcohol risk (Y).
:feedback-1: It's the reverse—alcohol risk is the outcome we think may be affected by rescue participation.
* *Explanatory: participation in the 9/11 rescue; response: alcohol risk
* Explanatory: alcohol risk; response: participation in the 9/11 rescue
:::

:::{quiz} What are the appropriate conditional percentages for the exploratory analysis, and what do they suggest?
:hint: Compute the percentage at moderate-to-severe risk within each participation group: 309/1102 and 110/551.
:feedback-0: Correct! 309/1102 ≈ 28% of participants were at risk vs. 110/551 ≈ 20% of non-participants—suggesting a possible relationship, which inference must confirm.
:feedback-1: Percentages should be computed within each row (participation group), not out of the overall total.
:feedback-2: The sample percentages DO differ (28% vs. 20%); the question for inference is whether this difference is statistically significant.
* *About 28% of participants vs. 20% of non-participants were at risk—a possible relationship worth testing
* About 19% and 7% of all firefighters were at-risk participants and non-participants respectively
* The percentages are identical, so there is no relationship
:::
