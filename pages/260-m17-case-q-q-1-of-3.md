# Case Q→Q: Inference for a Linear Relationship

```{admonition} Learning Objectives
:class: note

- Choose the appropriate inferential method for examining the relationship between two variables and justify the choice.
- In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
```

## Inference for the Linear Relationship Between Two Quantitative Variables

### Overview

In inference for relationships, so far we have learned inference procedures for both cases C→Q and C→C from the role-type classification table. The last case to be considered in this course is case Q→Q, where both the explanatory and response variables are quantitative. (Case Q→C requires statistical methods that go beyond the scope of this course.)

```{figure} images/gen/m05-role-type-qq.svg
:alt: The role-type classification table with the Q to Q case highlighted: a quantitative explanatory variable paired with a quantitative response variable.
```

In the Exploratory Data Analysis unit, we examined the relationship between sample values for two quantitative variables by looking at a scatterplot, and focused on the linear relationship by supplementing the scatterplot with the correlation coefficient r.

There was no attempt made to claim that whatever relationship was observed in the sample necessarily held for the larger population from which the sample originated. Now that we have a better understanding of the process of statistical inference, we will present the method for inferring something about the relationship between two quantitative variables in an entire population, based on the relationship seen in the sample. In particular, the method will focus on *linear* relationships and will answer the following question: is the observed linear relationship due to a true linear relationship between the two variables in the population, or could it be that we obtained this kind of pattern in the data just by chance?

If we conclude that we can generalize the observed linear relationship to the entire population, we will then use the data to estimate the line that governs the linear relationship between the two variables in the population, and use it to make predictions.

Let's review the whole process:

- We start by asking whether the two quantitative variables are related (in any way).
- We collect data, and when we summarize them with a scatterplot and the correlation r, we observe a linear relationship.
- Then we get to the inference part of the process, which we are going to learn here: we carry out a test that will tell us whether the observed linear relationship is significant (i.e., can be generalized to the entire population).
- If the observed linear relationship is significant, we can use the data to estimate the line that governs the linear relationship between X and Y in the population, and can use it to make predictions (see comment 1 below).

```{admonition} Comments
:class: important

1. We estimate the line that governs the linear relationship between X and Y in the population by the line that best fits the linear pattern in our observed data. Recall that in the Exploratory Data Analysis unit we actually already learned how to find the least squares regression line—the line that best fits the observed data. You can now see that finding the least squares regression line actually belongs to the inference unit, and while it is true that it is the line that best fits (in some sense) the observed data, it is really an *estimate* of the true linear relationship that exists in the population. The good thing is that we already learned how to obtain this line, so we'll only need to review it.

2. This section on regression will be very qualitative in nature and will rely mostly on conceptual ideas and on software output.

3. This section will be organized around a leading example, with practice along the way.
```

## Check Your Understanding: Regression and Inference

:::{quiz} A researcher computes a least squares regression line from a random sample. In the framework of inference, what does this line represent?
:hint: Sample statistics estimate population parameters.
:feedback-0: Correct! The sample regression line is an estimate of the true line that governs the linear relationship between X and Y in the population.
:feedback-1: The line fits the sample, but the point of inference is generalizing beyond the sample to the population.
:feedback-2: Whether the population relationship is significant must first be established by a test—computing the line alone doesn't settle that.
* *An estimate of the true line governing the linear relationship in the population
* An exact description of the relationship in the sample only, with no wider meaning
* Proof that a linear relationship exists in the population
:::
