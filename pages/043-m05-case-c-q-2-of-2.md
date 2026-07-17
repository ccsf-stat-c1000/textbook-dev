# Case C→Q in Practice: Boxplots That Tell a Story

```{admonition} Learning Objectives
:class: note

- Compare and contrast distributions (of quantitative data) from two or more groups, and produce a brief summary, interpreting your findings in context.
```

Here is another example:

::::{admonition} Example: SSHA
:class: tip

The Survey of Study Habits and Attitudes (SSHA) is a psychological test designed to measure the motivation, study habits, and attitudes toward learning of college students. Is there a relationship between *gender* and *SSHA scores*? In other words, is there a "gender effect" on SSHA scores? Data were collected from 40 randomly selected college students, and here is what the raw data look like:

| Student | Gender | SSHA Score |
| --- | --- | --- |
| Student 1 | Female | 154 |
| Student 2 | Female | 109 |
| Student 3 | Male | 108 |
| Student 4 | Female | 115 |
| ... | ... | ... |
| Student 40 | Male | 140 |

(Source: Moore, David S., and George P. McCabe. (2003). *Introduction to the Practice of Statistics*, 4th ed. New York: W. H. Freeman.)

Side-by-side boxplots supplemented by descriptive statistics allow us to compare the distribution of SSHA scores within each category of the explanatory variable—gender:

```{figure} images/gen/m05-ssha-boxplots.svg
:alt: Side-by-side vertical boxplots of SSHA scores for females and males. The female boxplot sits higher, with a median of 153, while the male boxplot is lower and more spread out, with a median of 114.5.
```

| Statistic | Female | Male |
| --- | --- | --- |
| min | 103 | 70 |
| Q1 | 128.75 | 95 |
| Median | 153 | 114.5 |
| Q3 | 163.75 | 144.5 |
| Max | 200 | 187 |
::::

## Concept Check

Use the boxplots and the table to explore whether there is a "gender effect" on SSHA scores.

:::{quiz} Based on the display and summaries, which statement best describes the relationship between gender and SSHA score in this sample?
:hint: Compare the medians and the positions of the two boxes.
:feedback-0: Correct! The female median (153) is well above the male median (114.5)—in fact it is above the male third quartile—indicating higher study-habit scores among the sampled women.
:feedback-1: Check the medians: 153 for females versus 114.5 for males—a substantial difference.
:feedback-2: It's the reverse; the female distribution is shifted toward higher scores.
* *Females in the sample tend to score noticeably higher than males
* Females and males score about the same
* Males in the sample tend to score noticeably higher than females
:::

:::{quiz} Which group's SSHA scores show more variability?
:hint: Compare the IQRs: Female Q3 − Q1 = 163.75 − 128.75; Male Q3 − Q1 = 144.5 − 95.
:feedback-0: The female IQR is 35 and range is 97—both smaller than the male IQR of 49.5 and range of 117.
:feedback-1: Correct! The males' IQR (49.5) and range (117) both exceed the females' (35 and 97), so male scores are more spread out.
:feedback-2: The spreads are quite different—compare the box heights in the display.
* The female group
* *The male group
* The two groups have nearly identical spread
:::

## Let's Summarize

- The relationship between a categorical explanatory variable and a quantitative response variable is summarized using:
  - *Data display:* Side-by-side boxplots
  - *Numerical summaries:* Descriptive statistics
- Exploring the relationship between a categorical explanatory variable and a quantitative response variable amounts to comparing the distributions of the quantitative response for each category of the explanatory variable. In particular, we look at how the distribution of the response variable differs between the values of the explanatory variable.
