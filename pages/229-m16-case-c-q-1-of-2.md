# Case C→Q: Comparing Groups

Recall the role-type classification table framing our discussion on inference about the relationship between two variables.

```{figure} images/gen/m05-role-type-cq.svg
:alt: The role-type classification table with the C to Q case highlighted: a categorical explanatory variable paired with a quantitative response variable.
```

We start with case C→Q, where the explanatory variable is categorical and the response variable is quantitative. Recall that in the Exploratory Data Analysis unit, examining the relationship between X and Y in this case amounts, in practice, to comparing the distributions of the (quantitative) response Y for each value (category) of the explanatory X. To do that, we used side-by-side boxplots (each representing the distribution of Y in one of the groups defined by X), and supplemented the display with the corresponding descriptive statistics.

What will we do in inference? To understand the logic, we'll start with an example and then generalize.

::::{admonition} Example: GPA and Year in College
:class: tip

Say that our variable of interest is the GPA of college students in the United States. From the previous module we know that since GPA is quantitative, we do inference on μ, the (population) mean GPA among all U.S. college students. Since this module is about relationships, let's assume that what we are really interested in is not simply GPA, but the relationship between:

- *X:* year in college (1 = freshman, 2 = sophomore, 3 = junior, 4 = senior), and
- *Y:* GPA

In other words, we want to explore whether GPA is related to year in college. The way to think about this is that the population of U.S. college students is now broken into *4 sub-populations*: freshmen, sophomores, juniors, and seniors. Within each of these four groups, we are interested in the GPA.

The inference must therefore involve the 4 sub-population means:

- $\mu_1$: mean GPA among freshmen in the United States
- $\mu_2$: mean GPA among sophomores in the United States
- $\mu_3$: mean GPA among juniors in the United States
- $\mu_4$: mean GPA among seniors in the United States

It makes sense that the inference about the relationship between year and GPA has to be based on some kind of comparison of these four means. If we infer that these four means are not all equal (i.e., that there are some differences in GPA across years in college), then that's equivalent to saying GPA is related to year in college. Let's summarize this example with a figure:

```{figure} images/gen/m16-cq-gpa-year.svg
:alt: The population of U.S. college students, for which we ask whether GPA and year are related, is broken into four sub-populations: freshmen with mean GPA mu 1, sophomores with mean GPA mu 2, juniors with mean GPA mu 3, and seniors with mean GPA mu 4. Inference about the relationship requires comparing these four means.
```
::::

In general, then, making inferences about the relationship between X and Y in case C→Q boils down to comparing the means of Y in the sub-populations, which are created by the categories defined by X (say k categories).

As the introduction to this module mentioned, we will learn three inferential methods in case C→Q, corresponding to a sub-division of this case. First we will distinguish between cases where the explanatory X has only two categories (k = 2), and cases where X has more than two categories (k > 2). In other words, we will look separately at cases where we are comparing two sub-population means:

```{figure} images/gen/m16-cq-two-subpops.svg
:alt: A population, for which we ask whether Y and X are related, is broken into two sub-populations because X has two categories. Sub-population 1 has mean of Y mu 1 and sub-population 2 has mean of Y mu 2. Inference requires comparing these two means.
```

and cases where we are comparing more than 2 sub-population means:

```{figure} images/gen/m16-cq-k-subpops.svg
:alt: A population, for which we ask whether Y and X are related, is broken into k sub-populations because X has more than two categories. Each sub-population has its own mean of Y, from mu 1 through mu k. Inference requires comparing these k means.
```

For example, if we are interested in whether GPA (Y) is related to gender (X), this is a case where *k = 2* (since gender has only two categories in this study: male, female), and the inference will boil down to comparing the mean GPA in the sub-population of males to that in the sub-population of females. On the other hand, in the example we looked at earlier, the relationship between GPA (Y) and year (X) is a case where *k > 2*, or more specifically, k = 4 (since year has four categories). In terms of inference, these two examples will be treated differently!
