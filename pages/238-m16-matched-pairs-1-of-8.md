# Comparing Two Means from Paired Data

## Comparing Two Means—Matched Pairs (Paired t-Test)

### Overview

We are still in case $C \to Q$ of inference about relationships, where the explanatory variable is categorical and the response variable is quantitative. As we mentioned in the introduction, we introduce three inferential procedures in this case.

So far we have introduced the first procedure—the two-sample t-test that is used when we are comparing two means and the samples are independent. We now move on to the second procedure, where we also compare two means, but the samples are paired or matched. Every observation in one sample is linked with an observation in the other sample. In this case, the samples are *dependent*.

```{figure} images/gen/m16-matched-pairs.svg
:alt: A two-valued categorical explanatory variable splits the population into population 1 and population 2, with means mu 1 and mu 2. Two samples of the same size n are taken, with each observation in one sample paired with an observation in the other.
```

One of the most common cases where dependent samples occur is when both samples have the same subjects and they are "*paired by subject*." In other words, each subject is measured twice on the response variable, typically before and then after some kind of treatment/intervention, in order to assess its effectiveness.

:::{admonition} Example: SAT Prep Class
:class: tip

Suppose you want to assess the effectiveness of an SAT prep class. It would make sense to use the matched pairs design and record each sampled student's SAT score before and after the SAT prep classes are attended.

Recall that the two populations represent the two values of the explanatory variable (no prep class, prep class). In this situation, those two values come from *a single set of subjects*. In other words, both populations really have the *same students*; each population simply corresponds to a different value of the explanatory variable.
:::

This, however, is not the only case where the paired design is used. Other cases are when the pairs are "natural pairs," such as siblings, twins, or couples. We will present two examples in this part. The first one will be of the type where each subject is measured twice, and the second one will be a study involving twins.

This section on the matched pairs design will be organized very much like the previous section on two independent samples. We will first introduce our leading example, and then present the paired t-test, illustrating each step using our example. We will then look at another example, and finally talk about estimation using a confidence interval. As usual, you'll be able to check your understanding along the way.

:::{admonition} Example: Drunk Drivers
:class: tip

Drunk driving is one of the main causes of car accidents. Interviews with drunk drivers who were involved in accidents and survived revealed that one of the main problems is that drivers do not realize that they are impaired, thinking "I only had 1-2 drinks ... I am OK to drive." A sample of 20 drivers was chosen, and their reaction times in an obstacle course were measured before and after drinking two beers. The purpose of this study was to check whether drivers are impaired after drinking two beers.

Here, the categorical explanatory variable X is "drank 2 beers (yes/no)," and population 1 (before drinking, mean reaction time $\mu_1$) and population 2 (after drinking, mean reaction time $\mu_2$) consist of the *same 20 drivers*, each measured twice.
:::

```{admonition} Comments
:class: important

1. Note that the categorical explanatory variable here is "drinking 2 beers (yes/no)," and the quantitative response variable is the reaction time.

2. Note that by using the matched pairs design in this study (i.e., by measuring each driver twice), the researchers isolated the effect of the two beers on the drivers and eliminated any other confounding factors that might influence the reaction times (such as the driver's experience, age, etc.).

3. For each driver, the two measurements are the total reaction time before drinking two beers, and after.
```
