# Wrap-Up (Inference for Relationships)

We've just completed the part of the course about the inferential methods for relationships between variables. The overall goal of inference for relationships is to assess whether the observed data provide evidence of a significant relationship between the two variables (i.e., a true relationship that exists in the population).

Much like the module about relationships in the Exploratory Data Analysis (EDA) unit, this part of the course was organized according to the role-type classification of the two variables involved. However, unlike the EDA module, when it comes to inferential methods, we further distinguished between three sub-cases in case $C \to Q$, so essentially we covered 5 methods in total.

The following table summarizes both EDA and inference for the relationship between two variables:

| Case | Exploratory display | Numerical summary | Formal inference |
| --- | --- | --- | --- |
| $C \to Q$ (categorical explanatory, quantitative response) | Side-by-side boxplots | Descriptive statistics by group | Two independent samples: two-sample t-test. Two dependent samples (matched pairs): paired t-test. More than two independent samples: ANOVA F-test. (More than two dependent samples: not covered in this course.) |
| $C \to C$ (categorical explanatory, categorical response) | Two-way table | Conditional percentages | Chi-square test for independence |
| $Q \to C$ (quantitative explanatory, categorical response) | — | — | Logistic regression: not covered in this course |
| $Q \to Q$ (quantitative explanatory, quantitative response) | Scatterplot (explanatory on the horizontal axis, response on the vertical axis) | Correlation coefficient r | Significance test for the linear relationship (t-test for the slope), followed by the least squares regression line |

## Check Your Understanding

For each research question, choose the appropriate inferential method.

:::{quiz} Is political party affiliation (Democrat/Republican/Independent) related to opinion on a ballot measure (support/oppose)?
:hint: Classify both variables.
:feedback-0: Correct! Both variables are categorical $(C \to C)$, so the chi-square test for independence applies.
:feedback-1: ANOVA requires a quantitative response variable.
:feedback-2: The t-test for the slope is for two quantitative variables.
* *Chi-square test for independence
* ANOVA F-test
* t-test for the slope
:::

:::{quiz} Is the number of hours studied per week related to GPA among college students?
:hint: Classify both variables.
:feedback-0: Correct! Both variables are quantitative $(Q \to Q)$, so we examine the linear relationship and test it with the t-test for the slope.
:feedback-1: The chi-square test is for two categorical variables.
:feedback-2: The two-sample t-test requires a two-valued categorical explanatory variable.
* *Regression: t-test for the slope of the linear relationship
* Chi-square test for independence
* Two-sample t-test
:::

:::{quiz} Does mean commute time differ among residents of four different neighborhoods, based on independent random samples from each?
:hint: Categorical explanatory with four values, quantitative response.
:feedback-0: Correct! A categorical explanatory variable with more than two categories and a quantitative response (with independent samples) calls for the ANOVA F-test.
:feedback-1: The paired t-test requires dependent (matched) samples of two measurements.
:feedback-2: The two-sample t-test handles only two groups.
* *ANOVA F-test
* Paired t-test
* Two-sample t-test
:::
