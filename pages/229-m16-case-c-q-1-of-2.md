# Case C→Q (1 of 2)

```{admonition} Learning Objectives
    - Identify and distinguish among cases where use of calculations specific to independent samples, matched pairs, and ANOVA are appropriate.
```

Recall the role-type classification table framing our discussion on inference about the relationship between two variables.

```{figure} images/image004.gif
:alt: It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q) (highlighted to show we will work on this case), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).

It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q) (highlighted to show we will work on this case), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).
```

We start with case C→Q, where the explanatory variable is categorical and the response variable is quantitative. Recall that in the Exploratory Data Analysis unit, examining the relationship between X and Y in this case amounts, in practice, to comparing the distributions of the (quantitative) response Y for each value (category) of the explanatory X. To do that, we used side-by-side boxplots (each representing the distribution of Y in one of the groups defined by X), and supplemented the display with the corresponding descriptive statistics.

What will we do in inference? To understand the logic, we'll start with an example and then generalize.

```{admonition} Example: GPA and Year in College
    Say that our variable of interest is the GPA of college students in the United States. From the previous module we know that since GPA is quantitative, we do inference on μ, the (population) mean GPA among all U.S. college students. Since this module is about relationships, let's assume that what we are really interested in is not simply GPA, but the relationship between:

    *X :* year in college (1 = freshmen, 2 = sophomore, 3 = junior, 4 = senior) and

    *Y :* GPA

    In other words, we want to explore whether GPA is related to year in college. The way to think about this is that the population of U.S. college students is now broken into *4 sub-populations*: freshmen, sophomores, juniors and seniors. Within each of these four groups, we are interested in the GPA.

    The inference must therefore involve the 4 sub-population means:

    μ~1~ : mean GPA among freshmen in the United States.

    μ~2~ : mean GPA among sophomores in the United States

    μ~3~ : mean GPA among juniors in the United States

    μ~4~ : mean GPA among seniors in the United States

    It makes sense that the inference about the relationship between year and GPA has to be based on some kind of comparison of these four means. If we infer that these four means are not all equal (i.e., that there are some differences in GPA across years in college) then that's equivalent to saying GPA is related to year in college. Let's summarize this example with a figure:

    ```{figure} images/image010.gif
    :alt: The entire population of US College Students is represented by a large circle. For this population we would like to know if GPA (Y) and Year (X) are related. This population is made of 4-sub populations. This is represented by 4 arrows from the population circle to 4 other circles. A circle exists for US Freshmen, with GPA mean μ_1. Another circle exists for US Sophomores, with GPA Mean μ_2. US Juniors has another circle with GPA Mean μ_3. The last circle is for US Seniors, with GPA Mean μ_4. To infer on relationship we&apos;ll need to compare each of these means.

    The entire population of US College Students is represented by a large circle. For this population we would like to know if GPA (Y) and Year (X) are related. This population is made of 4-sub populations. This is represented by 4 arrows from the population circle to 4 other circles. A circle exists for US Freshmen, with GPA mean μ_1. Another circle exists for US Sophomores, with GPA Mean μ_2. US Juniors has another circle with GPA Mean μ_3. The last circle is for US Seniors, with GPA Mean μ_4. To infer on relationship we&apos;ll need to compare each of these means.
    ```
```

In general, then, making inferences about the relationship between X and Y in Case C→Q boils down to comparing the means of Y in the sub-populations, which are created by the categories defined in X (say k categories). The following figure summarizes this:

```{figure} images/image011.gif
:alt: The entire population is represented by a large circle, for which we wonder if there is a relationship between Y and X. This large population is broken up into sub-populations, each with its own mean μ. To infer on relationship between Y and X, we&apos;ll need to compare these means.

The entire population is represented by a large circle, for which we wonder if there is a relationship between Y and X. This large population is broken up into sub-populations, each with its own mean μ. To infer on relationship between Y and X, we&apos;ll need to compare these means.
```

As the introduction to this module mentioned, we will learn three inferential methods in Case C→Q, corresponding to a sub-division of this case. First we will distinguish between cases where the explanatory X has only two categories (k = 2), and cases where X has more than two categories (k > 2). In other words, we will look separately at cases where we are comparing two sub-population means:

```{figure} images/image012.gif
:alt: We have a population for which we want to know if there is a relationship between Y and X. k = 2 in this case, so we have two sub-populations, each with its own Y Mean. Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. To infer on relationship we&apos;ll need to compare these TWO means.

We have a population for which we want to know if there is a relationship between Y and X. k = 2 in this case, so we have two sub-populations, each with its own Y Mean. Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. To infer on relationship we&apos;ll need to compare these TWO means.
```

and cases where we are comparing more than 2 sub-population means:

```{figure} images/image013.gif
:alt: The entire population is represented by a large circle, for which we wonder if there is a relationship between Y and X. k &gt; 2. This large population is broken up into k sub-populations, each with its own mean μ. To infer on relationship between Y and X, we&apos;ll need to compare these k means.

The entire population is represented by a large circle, for which we wonder if there is a relationship between Y and X. k &gt; 2. This large population is broken up into k sub-populations, each with its own mean μ. To infer on relationship between Y and X, we&apos;ll need to compare these k means.
```

For example, if we are interested in whether GPA (Y) is related to gender (X), this is a case where *k = 2* (since gender has only two categories: M, F), and the inference will boil down to comparing the mean GPA in the sub-population of males to that in the sub-population of females. On the other hand, in the example we looked at earlier, the relationship between GPA (Y) and year (X) is a case where *k > 2* or more specifically, k = 4 (since year has four categories). In terms of inference, these two examples will be treated differently!
