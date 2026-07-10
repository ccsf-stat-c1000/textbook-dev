# ANOVA (1 of 7)

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Comparing More Than Two Means—ANOVA

### Overview

In this part, we continue to handle situations involving one categorical explanatory variable and one quantitative response variable, which is case C→Q in our role-type classification table.

So far we have discussed the two samples and matched pairs designs, in which the categorical explanatory variable is two-valued. As we saw, in these cases, examining the relationship between the explanatory and the response variables amounts to comparing the mean of the response variable (Y) in two populations, which are defined by the two values of the explanatory variable (X). The difference between the two samples and matched pairs designs is that in the former, the two samples are independent, and in the latter, the samples are dependent.

We are now moving on to cases in which the categorical explanatory variable takes *more than two* values. Here, as in the two-valued case, making inferences about the relationship between the explanatory (X) and the response (Y) variables amounts to comparing the means of the response variable in the populations defined by the values of the explanatory variable, where the number of means we are comparing depends, of course, on the number of values of X. Unlike the two-valued case, where we looked at two sub-cases—(1) when the samples are independent (two samples design) and (2) when the samples are dependent (matched pairs design)—here we are just going to discuss the case where the samples are independent. In other words, we are just going to extend the two samples design to more than two independent samples.

```{admonition} Comment
:class: important

The extension of the matched pairs design to more than two dependent samples is called "repeated measures" and is beyond the scope of this course.
```

The inferential method for comparing more than two means that we will introduce in this part is called *Analysis of Variance* (abbreviated as ANOVA), and the test associated with this method is called the *ANOVA F-test*. The structure of this part will be very similar to that of the previous two. We will first present our leading example, and then introduce the ANOVA F-test by going through its 4 steps, illustrating each one using the example. (It will become clear as we explain the idea behind the test where the name "Analysis of Variance" comes from.) We will then present another complete example, and conclude with some comments about possible follow-ups to the test.

Let's start by introducing our leading example.

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

A college dean believes that students with different majors may experience different levels of academic frustration. Random samples of size 35 of Business, English, Mathematics, and Psychology majors are asked to rate their level of academic frustration on a scale of 1 (lowest) to 20 (highest).

```{figure} images/gen/m16-anova-design.svg
:alt: The explanatory variable major has four categories: Business, English, Mathematics, and Psychology, defining four populations, each with its own mean frustration level, mu 1 through mu 4. From each population an independent sample of size 35 is taken.
```

The figure highlights what we have already mentioned: examining the relationship between major (X) and frustration level (Y) amounts to comparing the mean frustration levels ($\mu_1, \mu_2, \mu_3, \mu_4$) among the four majors defined by X. Also, the figure reminds us that we are dealing with a case where the samples are independent.
:::

```{admonition} Comment: Two Ways to Record the Data
:class: important

There are two ways to record data in the ANOVA setting:

*Unstacked:* one column for each of the four majors, with each column listing the frustration levels reported by all sampled students in that major.

| Business | English | Mathematics | Psychology |
| --- | --- | --- | --- |
| 11 | 11 | 9 | 11 |
| 6 | 9 | 16 | 19 |
| 6 | 14 | 11 | 13 |
| ... | ... | ... | ... |

*Stacked:* one column for all the frustration levels, and next to it a column to keep track of which major a student is in.

| Frustration (Y) | Major (X) |
| --- | --- |
| 9 | Business |
| 2 | Business |
| 9 | Business |
| 10 | English |
| 11 | Psychology |
| 13 | English |
| 13 | Psychology |
| 12 | Mathematics |
| ... | ... |

The "unstacked" format helps us to look at the four groups separately, while the "stacked" format helps us remember that there are, in fact, two variables involved: frustration level (the quantitative response variable) and major (the categorical explanatory variable).
```
