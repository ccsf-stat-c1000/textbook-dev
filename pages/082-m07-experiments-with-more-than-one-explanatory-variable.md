# Experiments With More Than One Explanatory Variable

```{admonition} Learning Objectives
    - Identify the design of a study (controlled experiment vs. observational study) and other features of the study design (randomized, blind etc.).
```

## Experiments
                With
                More
                Than
                One Explanatory Variable

It is not uncommon for experiments to feature two or more explanatory variables (called factors). In this course, we focus on exploratory data analysis and statistical inference in situations which involve only one explanatory variable. Nevertheless, we will now consider the design for experiments involving several explanatory variables, in order to familiarize students with their basic structure.

```{admonition} Example
    Suppose researchers are not only interested in the effect of diet on blood pressure, but also the effect of two new drugs. Subjects are assigned to either Control Diet (no restrictions), Diet #1, or Diet #2, (the variable diet has, then, 3 possible values) and are also assigned to receive either Placebo, Drug #1, or Drug #2 (the variable Drug, then, also has three values). This is an example where the experiment has two explanatory variables and a response variable. In order to set up such an experiment, there has to be *one treatment group for every combination of categories of the two explanatory variables*. Thus, in this case there are 3 * 3 = 9 combinations of the two variables to which the subjects are assigned. The treatment groups are illustrated and labeled in the following table:

    ```{figure} images/image009.gif
    :alt: The column headings for the table are for the Diet variable: "No-diet", "Special diet 1" and "Special diet 2." The Rows are for the drug variable: "Placebo," "Drug 1," and "Drug 2." There are 9 cells in the table, one for every possible combination of row and column. These cells are labeled "tttX", where X is in the range of [1-9], representing each combination.

    The column headings for the table are for the Diet variable: "No-diet", "Special diet 1" and "Special diet 2." The Rows are for the drug variable: "Placebo," "Drug 1," and "Drug 2." There are 9 cells in the table, one for every possible combination of row and column. These cells are labeled "tttX", where X is in the range of [1-9], representing each combination.
    ```

    Subjects would be randomly assigned to one of the nine treatment groups. If we find differences in the proportions of subjects who achieve the lower "moderate zone" blood pressure among the nine treatment groups, then we have evidence that the diets and/or drugs may be effective for reducing blood pressure.

    ```{figure} images/image010.gif
    :alt: From the population we generate a sample. The individuals of the sample are represented as a whole visually with a circle. These individuals are then divided by randomly assigning them to one of the 9 treatment groups. These treatment groups are "ttt1: no-diet and placebo,", "ttt2: diet 1 and placebo", "ttt3: diet 2 and placebo", and so on, up to "ttt9: diet 2 and drug 2." The responses from each of these treatment groups are compared.

    From the population we generate a sample. The individuals of the sample are represented as a whole visually with a circle. These individuals are then divided by randomly assigning them to one of the 9 treatment groups. These treatment groups are "ttt1: no-diet and placebo,", "ttt2: diet 1 and placebo", "ttt3: diet 2 and placebo", and so on, up to "ttt9: diet 2 and drug 2." The responses from each of these treatment groups are compared.
    ```
```

## Comments

1. Recall that randomization may be employed at two stages of an experiment: in the selection of subjects, and in the assignment of treatments. The former may be helpful in allowing us to generalize what occurs among our subjects to what would occur in the general population, but the reality of most experimental settings is that a convenience or volunteer sample is used. Most likely the blood pressure study described above would use volunteer subjects. The important thing is to make sure these subjects are randomly assigned to one of the nine treatment combinations.

2. In order to gain optimal information about individuals in all the various treatment groups, we would like to make assignments not just randomly, but also evenly. If there are 90 subjects in the blood pressure study described above, and 9 possible treatment groups, then each group should be filled randomly with 10 individuals. A simple random sample of 10 could be taken from the larger group of 90, and those individuals would be assigned to the first treatment group. Next, the second treatment group would be filled by a simple random sample of 10 taken from the remaining 80 subjects. This process would be repeated until all 9 groups are filled with 10 individuals each.

##### Did I Get This?

A university was interested in examining the overall effectiveness of its online statistics course, along with the effectiveness of particular aspects of the course. First, the university wanted to see whether the online course was better than a standard course. Second, the university wanted to know whether students learned best using Excel, using Minitab, or using no statistical package at all. The university randomly selected a group of 30 students and administered one of the different variants of the course (i.e., traditional or online, coupled with one of the software options) to each student. The success of each variant was measured by the students' average improvement between a pre-test and a post-test.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
