# Conditional Percentages: Making a Two-Way Table Talk

So far, we have organized the raw data in a much more informative display—the two-way table:

| Gender | About right | Overweight | Underweight | Total |
| --- | --- | --- | --- | --- |
| Female | 560 | 163 | 37 | 760 |
| Male | 295 | 72 | 73 | 440 |
| **Total** | **855** | **235** | **110** | **1200** |

Remember, though, that our primary goal is to explore how body image is related to gender. Exploring the relationship between two categorical variables (in this case, body image and gender) amounts to comparing the distributions of the response variable (in this case body image) across the different values of the explanatory variable (in this case, males and females).

Note that it doesn't make sense to compare raw counts, because there are more females than males overall. So, for example, it is not very informative to say, "There are 560 females who responded 'about right' compared to only 295 males," since the 560 females are out of a total of 760, and the 295 males are out of a total of only 440.

We need to supplement our display, the two-way table, with some numerical summaries that will allow us to compare the distributions. These numerical summaries are found by simply *converting the counts to percentages within (or restricted to) each value of the explanatory variable separately*.

In our example, we look at each gender separately and convert the counts to percentages *within that gender*. Let's start with females:

| Gender | About right | Overweight | Underweight | Total |
| --- | --- | --- | --- | --- |
| Female | 560/760 = 73.7% | 163/760 = 21.5% | 37/760 = 4.9% | 760/760 = 100% |

Note that each count is converted to percents by dividing by the total number of females, 760. These numerical summaries are called *conditional percentages*, since we find them by "conditioning" on one of the genders.

## Check Your Understanding: Conditional Percentages

:::{quiz} Now compute the conditional percentages for the males. What percentage of the males feel they are underweight?
:hint: Divide the count of underweight males by the total number of males, 440.
:feedback-0: 4.9% is the percentage of *females* who feel underweight.
:feedback-1: Correct! 73/440 ≈ 16.6% of the males feel underweight.
:feedback-2: 73 is the raw count; convert it to a percentage of the 440 males.
* 4.9%
* *16.6%
* 73%
:::

Here is the completed table of conditional (row) percentages, along with a double bar chart of the same information:

| Gender | About right | Overweight | Underweight | Total |
| --- | --- | --- | --- | --- |
| Female | 73.7% | 21.5% | 4.9% | 100% |
| Male | 67.0% | 16.4% | 16.6% | 100% |

```{figure} images/gen/m05-body-image-double-bar.svg
:alt: A double bar chart of the conditional percentages. For About right, females are 73.7% and males 67.0%. For Overweight, females are 21.5% and males 16.4%. For Underweight, females are 4.9% and males 16.6%, a striking difference.
```

```{admonition} Comments
:class: important

1. In our example, we chose to organize the data with the explanatory variable gender in rows and the response variable body image in columns, and thus our conditional percentages were *row percentages*, calculated within each row separately. Similarly, if the explanatory variable happens to sit in columns and the response variable in rows, our conditional percentages will be *column percentages*, calculated within each column separately. For an example, see the exercises below.
2. Another way to visualize the conditional percentages, instead of in a table, is to use a *double bar chart* (as above). This display is quite common in newspapers.
```

Now that we have summarized the relationship between the categorical variables gender and body image, let's go back and interpret the results in the context of the questions that we posed.

:::{quiz} Which of the following is the best interpretation of the relationship between gender and body image in this sample?
:hint: Compare the conditional percentages row by row—especially the Underweight category.
:feedback-0: Correct! Roughly similar majorities of both genders feel about right, but among the rest, females lean toward feeling overweight (21.5% vs. 4.9% underweight) while males are about evenly split (16.4% overweight vs. 16.6% underweight).
:feedback-1: Comparing raw counts is misleading here because there are many more females (760) than males (440) in the sample; conditional percentages must be used.
:feedback-2: There is a noticeable difference, particularly in the Underweight category (4.9% of females vs. 16.6% of males).
* *Similar majorities of both genders feel about right, but females who don't are far more likely to feel overweight than underweight, while males are evenly split
* Females are more likely than males to feel about right because 560 is larger than 295
* The distributions of body image are essentially identical for the two genders
:::

## Check Your Understanding: Interpreting a Two-Way Table

Suppose a study were done to answer the question: "Is the smoking of students related to their parents' smoking habits?" in which data were collected from 5,375 students and organized in the following two-way table:

| | Parents Do Not Smoke | Parents Smoke | Total |
| --- | --- | --- | --- |
| Student Does Not Smoke | 1168 | 3203 | 4371 |
| Student Smokes | 188 | 816 | 1004 |
| **Total** | **1356** | **4019** | **5375** |

:::{quiz} In this table, parents' smoking (the explanatory variable) sits in the columns. Which conditional percentages should we compare to explore the relationship?
:hint: Conditional percentages are computed within each value of the explanatory variable separately.
:feedback-0: Row percentages would condition on the response variable (student smoking), not the explanatory variable.
:feedback-1: Correct! Since the explanatory variable is in the columns, we compute column percentages—the distribution of student smoking within each parental smoking group.
:feedback-2: Percentages out of the grand total do not let us compare the two parental smoking groups directly.
* Row percentages (within each student smoking category)
* *Column percentages (within each parents' smoking category)
* Overall percentages (each cell divided by 5,375)
:::

:::{quiz} What percentage of students whose parents smoke are smokers themselves, and how does it compare to students whose parents do not smoke?
:hint: Compute 816/4019 and 188/1356, then compare.
:feedback-0: Correct! 816/4019 ≈ 20.3% of students with smoking parents smoke, versus 188/1356 ≈ 13.9% of students with non-smoking parents—suggesting an association between parents' and students' smoking.
:feedback-1: 816/1004 ≈ 81% is a row percentage—the share of student smokers whose parents smoke—which conditions on the wrong variable.
:feedback-2: The two percentages differ noticeably (20.3% vs. 13.9%), suggesting the variables are related.
* *About 20.3%, compared with about 13.9%—students with smoking parents are more likely to smoke
* About 81%, compared with about 19%
* The percentages are essentially the same in both groups
:::

## Let's Summarize

- The relationship between two categorical variables is summarized using
  - *Data display:* Two-way table, supplemented by
  - *Numerical summaries:* Conditional percentages.
- Conditional percentages are calculated for each value of the explanatory variable separately. They can be row percentages if the explanatory variable "sits" in the rows, or column percentages if the explanatory variable "sits" in the columns.
- When we try to understand the relationship between two categorical variables, we compare the distributions of the response variable for values of the explanatory variable. In particular, we look at how the pattern of conditional percentages differs between the values of the explanatory variable.
