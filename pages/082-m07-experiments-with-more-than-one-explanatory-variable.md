# Experiments With More Than One Explanatory Variable

```{admonition} Learning Objectives
:class: note

- Identify the design of a study (controlled experiment vs. observational study) and other features of the study design (randomized, blind etc.).
```

## Experiments With More Than One Explanatory Variable

It is not uncommon for experiments to feature two or more explanatory variables (called factors). In this course, we focus on exploratory data analysis and statistical inference in situations which involve only one explanatory variable. Nevertheless, we will now consider the design for experiments involving several explanatory variables, in order to familiarize students with their basic structure.

:::{admonition} Example: Diets and Drugs
:class: tip

Suppose researchers are not only interested in the effect of diet on blood pressure, but also the effect of two new drugs. Subjects are assigned to either Control Diet (no restrictions), Diet #1, or Diet #2 (the variable diet has, then, 3 possible values) and are also assigned to receive either Placebo, Drug #1, or Drug #2 (the variable Drug, then, also has three values). This is an example where the experiment has two explanatory variables and a response variable. In order to set up such an experiment, there has to be *one treatment group for every combination of categories of the two explanatory variables*. Thus, in this case there are 3 × 3 = 9 combinations of the two variables to which the subjects are assigned. The treatment groups are illustrated and labeled in the following table:

| | No diet | Special diet 1 | Special diet 2 |
| --- | --- | --- | --- |
| **Placebo** | treatment 1 | treatment 2 | treatment 3 |
| **Drug 1** | treatment 4 | treatment 5 | treatment 6 |
| **Drug 2** | treatment 7 | treatment 8 | treatment 9 |

Subjects would be randomly assigned to one of the nine treatment groups. If we find differences in the proportions of subjects who achieve the lower "moderate zone" blood pressure among the nine treatment groups, then we have evidence that the diets and/or drugs may be effective for reducing blood pressure.
:::

## Comments

1. Recall that randomization may be employed at two stages of an experiment: in the selection of subjects, and in the assignment of treatments. The former may be helpful in allowing us to generalize what occurs among our subjects to what would occur in the general population, but the reality of most experimental settings is that a convenience or volunteer sample is used. Most likely the blood pressure study described above would use volunteer subjects. The important thing is to make sure these subjects are randomly assigned to one of the nine treatment combinations.

2. In order to gain optimal information about individuals in all the various treatment groups, we would like to make assignments not just randomly, but also evenly. If there are 90 subjects in the blood pressure study described above, and 9 possible treatment groups, then each group should be filled randomly with 10 individuals. A simple random sample of 10 could be taken from the larger group of 90, and those individuals would be assigned to the first treatment group. Next, the second treatment group would be filled by a simple random sample of 10 taken from the remaining 80 subjects. This process would be repeated until all 9 groups are filled with 10 individuals each.

## Did I Get This?

A university was interested in examining the overall effectiveness of its online statistics course, along with the effectiveness of particular aspects of the course. First, the university wanted to see whether the online course was better than a standard course. Second, the university wanted to know whether students learned best using statistical software package A, package B, or no statistical package at all. The university randomly selected a group of 30 students and administered one of the different variants of the course (i.e., traditional or online, coupled with one of the software options) to each student. The success of each variant was measured by the students' average improvement between a pre-test and a post-test.

:::{quiz} How many factors (explanatory variables) does this experiment have?
:hint: Count the separate things being varied: course format and software choice.
:feedback-0: There are more than one—the course format is not the only variable being manipulated.
:feedback-1: Correct! There are two factors: course format (traditional or online) and software (package A, package B, or none).
:feedback-2: Six is the number of treatment combinations, not the number of factors.
* 1
* *2
* 6
:::

:::{quiz} How many treatment groups must this experiment have?
:hint: One group for every combination of the two factors: 2 formats × 3 software options.
:feedback-0: 5 is the sum of the numbers of categories; you need the product—every combination gets a group.
:feedback-1: Correct! 2 course formats × 3 software options = 6 treatment combinations.
:feedback-2: 9 would be right if both factors had 3 categories; here the format factor has only 2.
* 5
* *6
* 9
:::

:::{quiz} With 30 students and 6 treatment groups, what is the ideal way to assign students?
:hint: Assignments should be random and even.
:feedback-0: Correct! Randomly assign 5 students to each of the 6 treatment groups, so groups are both random and equal in size.
:feedback-1: Letting students choose would reintroduce self-selection—the very problem experiments avoid.
:feedback-2: Assigning all 30 to one group would leave no comparison groups at all.
* *Randomly assign 5 students to each of the 6 groups
* Let each student pick the variant they prefer
* Assign all 30 students to the most promising variant
:::

## Comment on the response variable

Note that the response variable in this study is quantitative (improvement between pre-test and post-test), and the explanatory variables are categorical—so comparing the treatment groups amounts to case C→Q: comparing the distribution of improvements across the six groups.
