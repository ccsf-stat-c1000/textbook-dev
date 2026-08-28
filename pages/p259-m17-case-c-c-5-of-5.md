# The Chi-Square Test: Summary

Let's look at another example.

:::{admonition} Example: Steroid Use in College Sports
:class: tip

Is steroid use different in baseball than in other sports? According to the 2001 National Collegiate Athletic Association (NCAA) survey, which was self-reported and asked of a stratified random selection of teams from each of the three NCAA divisions, reported steroid use among the top 5 men's college sports was as follows:

| Sport | Reported using steroids | Reported not using steroids | Total |
| --- | --- | --- | --- |
| Baseball | 26 | 1,088 | 1,114 |
| Basketball | 13 | 881 | 894 |
| Football | 59 | 1,897 | 1,956 |
| Tennis | 2 | 335 | 337 |
| Track/field | 6 | 486 | 492 |
| **Total** | 106 | 4,687 | 4,793 |

Do the data provide evidence of a significant relationship between steroid use and the type of sport? In other words, are there significant differences in steroid use among the different sports?

Before we carry out the chi-square test for independence, let's get a sense of the data by calculating the conditional percents (percent reporting steroid use within each sport): baseball 2.3%, basketball 1.5%, football 3.0%, tennis 0.6%, track/field 1.2%.

It seems as if there are differences in steroid use among the different sports. Even though the differences do not seem to be overwhelming, since the sample size is so large, these differences might be significant. Let's carry out the test and see.

*Step 1: Stating the hypotheses.*

- $H_0$: Steroid use is not related to the type of sport (type of sport and steroid use are independent).
- $H_a$: Steroid use is related to the type of sport (type of sport and steroid use are not independent).

*Step 2: Checking conditions and finding the test statistic.* Software output for the chi-square test gives, for each cell, the observed count, the expected count, and the contribution to the chi-square statistic:

| Sport | Used: observed (expected) | Contribution | Not used: observed (expected) | Contribution |
| --- | --- | --- | --- | --- |
| Baseball | 26 (24.6) | 0.075 | 1,088 (1,089.4) | 0.002 |
| Basketball | 13 (19.8) | 2.319 | 881 (874.2) | 0.052 |
| Football | 59 (43.3) | 5.729 | 1,897 (1,912.7) | 0.130 |
| Tennis | 2 (7.5) | 3.990 | 335 (329.5) | 0.090 |
| Track/field | 6 (10.9) | 2.189 | 486 (481.1) | 0.050 |

Conditions: (1) we are told that the sample was random; (2) all the expected counts are above 5.

Test statistic: $\chi^2 = 14.626$. Note that the "largest contributors" to the test statistic are 5.729 and 3.990. The first cell corresponds to football players who used steroids, with an observed count larger than we would expect under independence. The second corresponds to tennis players who used steroids, with an observed count lower than we would expect under independence.

*Step 3: Finding the p-value.* According to the output, it would be extremely unlikely (probability of 0.006) to get counts like those observed if the null hypothesis were true. In other words, it would be very surprising to get data like those observed if steroid use were not related to sport type.

*Step 4: Conclusion.* The small p-value indicates that the data provide strong evidence against the null hypothesis, so we reject it and conclude that steroid use is related to the type of sport.
:::

## Let's Summarize

- The chi-square test for independence is used to test whether the relationship between two categorical variables is significant. In other words, the chi-square procedure assesses whether the data provide enough evidence that a true relationship between the two variables exists in the population.

- The hypotheses that are being tested in the chi-square test for independence are:

  - $H_0$: There is no relationship between the two variables (they are independent).
  - $H_a$: There is a relationship between the two variables (they are not independent).

- The idea behind the test is measuring how far the observed data are from the null hypothesis by comparing the observed counts to the expected counts—the counts that we would expect to see had the null hypothesis been true. The expected count of each cell is calculated as:

  $$\text{Expected count}=\frac{\text{column total}\times\text{row total}}{\text{table total}}$$

- The measure of the difference between the observed and expected counts is the chi-square test statistic, whose null distribution is called the chi-square distribution:

  $$\chi^{2}=\sum_{\text{all cells}}\frac{(\text{observed count}-\text{expected count})^{2}}{\text{expected count}}$$

- The conditions for safe use are a random sample and large enough expected counts (all above 5, by the conservative rule). Once we verify these, we use software to carry out the test and use the p-value to guide our conclusions.

## Check Your Understanding: Interpreting the Chi-Square Results

:::{quiz} In the steroid example, which cells provided the strongest evidence against independence, and in what direction?
:hint: Look at the largest contributions to the chi-square statistic.
:feedback-0: Correct! Football's "used" cell (contribution 5.729, observed 59 vs. expected 43.3) shows more use than independence predicts, and tennis's "used" cell (3.990, observed 2 vs. expected 7.5) shows less.
:feedback-1: Baseball's contributions (0.075, 0.002) are tiny—baseball's use is close to what independence predicts.
:feedback-2: The direction matters: football is above expectation and tennis below.
* *Football players used steroids more than expected; tennis players less than expected
* Baseball players used steroids far more than expected
* Football and tennis players both used steroids more than expected
:::

:::{quiz} A survey wants to test whether pet ownership (dog/cat/none) is related to housing type (house/apartment) using a random sample. The expected counts include one cell with an expected count of 3.2. What should the analyst do?
:hint: The conservative condition requires all expected counts above 5.
:feedback-0: Correct! With an expected count below 5, the chi-square approximation may be unreliable—collecting more data (or combining categories) is the standard remedy.
:feedback-1: The condition concerns EXPECTED counts, and one of them fails the threshold.
* *Be cautious—an expected count below 5 violates the conservative condition; more data or combined categories may be needed
* Proceed—only observed counts matter for the conditions
:::
