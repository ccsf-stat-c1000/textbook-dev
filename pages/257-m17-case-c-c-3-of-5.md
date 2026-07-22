# The Chi-Square Statistic: Conditions and Computation

## Step 2: Checking the Conditions and Calculating the Test Statistic

Given our discussion on the previous page, it would be natural to present the test statistic, and then come back to the conditions that allow us to safely use the chi-square test, although in practice this is done the other way around.

The single number that summarizes the overall difference between observed and expected counts is the chi-square statistic $\chi^2$, which tells us in a standardized way how far what we observed (data) is from what would be expected if $H_0$ were true.

```{admonition} The Chi-Square Test Statistic
:class: note

$$\chi^{2}=\sum_{\text{all cells}}\frac{(\text{observed count}-\text{expected count})^{2}}{\text{expected count}}$$
```

```{admonition} Comment
:class: important

As we expected, $\chi^2$ is based on each of the differences (observed count − expected count), one such difference for each cell. But why is it squared, and why do we divide each squared difference by the expected count? The reason is so that the test statistic will have a known null distribution (under which p-values can be easily calculated). The details are beyond the scope of this course, but we will just say that the null distribution of $\chi^2$ is called chi-square (which is not very surprising, given that the test is called the chi-square test), and, like the t-distributions, there are many chi-square distributions, distinguished by the number of degrees of freedom associated with them.
```

## Conditions Under Which the Chi-Square Test Can Safely Be Used

1. The sample should be random.
2. In general, the larger the sample, the more accurate and reliable the test results are. There are different versions of the conditions that ensure reliable use of the test, all of which involve the expected counts. One version says that all expected counts need to be greater than 1, and at least 80% of expected counts need to be greater than 5. A more conservative version requires that all expected counts be larger than 5.

:::{admonition} Example: Drunk Driving and Gender
:class: tip

Here, again, are the observed counts alongside the expected counts (in parentheses):

| | Yes | No | Total |
| --- | --- | --- | --- |
| **Male** | 77 (72.3) | 404 (408.7) | 481 |
| **Female** | 16 (20.7) | 122 (117.3) | 138 |
| **Total** | 93 | 526 | 619 |

Checking the conditions:

1. The roadside survey is known to have been random.
2. All the expected counts are above 5.

We can therefore safely proceed with the chi-square test, and the chi-square test statistic is:

$$\chi^{2}=\frac{(77-72.3)^{2}}{72.3}+\frac{(404-408.7)^{2}}{408.7}+\frac{(16-20.7)^{2}}{20.7}+\frac{(122-117.3)^{2}}{117.3}=0.306+0.054+1.067+0.188=1.62$$
:::

## Check Your Understanding: The Chi-Square Statistic

Recall the study on the relationship between gender and ear piercing among high-school students (observed counts: pierced females 576, non-pierced females 64, pierced males 72, non-pierced males 288; expected counts under independence: 414.7, 225.3, 233.3, 126.7).

:::{quiz} Are the conditions for the chi-square test met for the piercing data?
:hint: The sample of 1,000 students was random. Check the expected counts.
:feedback-0: Correct! The sample was random and all four expected counts (414.7, 225.3, 233.3, 126.7) are far above 5.
:feedback-1: The condition involves the EXPECTED counts, and all of them exceed 5 comfortably.
* *Yes—the sample is random and all expected counts exceed 5
* No—some cells have observed counts below 100
:::

:::{quiz} The chi-square statistic for the piercing data is about 495. Compared to the drunk driving example (χ² = 1.62), what does this indicate?
:hint: The chi-square statistic measures the total standardized discrepancy between observed and expected counts.
:feedback-0: Correct! A chi-square statistic of 495 indicates the observed counts are enormously far from what independence predicts—overwhelming evidence of a relationship between gender and piercing.
:feedback-1: It's the opposite—larger chi-square values mean MORE evidence against independence.
:feedback-2: The two statistics are comparable in spirit: both measure discrepancy from independence, and 495 is vastly larger than 1.62.
* *The piercing data provide vastly stronger evidence against independence
* The piercing data provide weaker evidence against independence
* The two statistics cannot be meaningfully compared
:::

```{admonition} Comment
:class: important

Once the chi-square statistic has been calculated, we can get a feel for its size: is there a relatively large difference between what we observed and what the null hypothesis claims, or a relatively small one? It turns out that for a 2-by-2 case like ours, we are inclined to call the chi-square statistic "large" if it is larger than 3.84. Therefore, our drunk driving test statistic (1.62) is not large, indicating that the data are not different enough from the null hypothesis for us to reject it (we will also see this in the p-value not being small). For other cases (other than 2-by-2) there are different cutoffs for what is considered large, which are determined by the null distribution in that case. We are therefore going to rely only on the p-value to draw our conclusions. Even though we cannot always assess the chi-square statistic directly, it was important to learn about it, since it encompasses the idea behind the test.
```

## Check Your Understanding: Conditions for the Chi-Square Test

The purpose of this activity is to continue exploring whether the risk of alcohol problems among New York firefighters and first responders is related to participation in the 9/11 rescue. Here again are the observed counts:

| | No risk | Moderate to severe risk | Total |
| --- | --- | --- | --- |
| **Participated in 9/11 rescue** | 793 | 309 | 1,102 |
| **Did not participate** | 441 | 110 | 551 |
| **Total** | 1,234 | 419 | 1,653 |

:::{quiz} What are the hypotheses being tested in this study?
:hint: The chi-square hypotheses are stated in words, about a relationship.
:feedback-0: Correct! H₀: alcohol risk and 9/11 participation are not related (independent); Hₐ: they are related.
:feedback-1: This reverses the roles of the null and alternative hypotheses.
:feedback-2: The chi-square hypotheses concern the relationship between the variables, not specific proportions of the whole sample.
* *H₀: alcohol risk and 9/11 participation are independent; Hₐ: they are related
* H₀: alcohol risk and 9/11 participation are related; Hₐ: they are independent
* H₀: 28% of all firefighters are at risk; Hₐ: fewer than 28% are at risk
:::

:::{quiz} Using the expected count formula, what is the expected count of participants at moderate-to-severe risk, and is the sample-size condition met?
:hint: Expected count = (419 × 1102)/1653; then check whether all four expected counts exceed 5.
:feedback-0: Correct! (419 × 1102)/1653 ≈ 279.3, and the other expected counts (822.7, 411.3, 139.7) are also far above 5—the condition is met.
:feedback-1: 309 is the OBSERVED count; the expected count under independence is (419 × 1102)/1653 ≈ 279.3.
:feedback-2: All four expected counts are in the hundreds—far above the threshold of 5.
* *About 279; yes, all expected counts are well above 5
* 309; yes, the condition is met
* About 279; no, the condition fails
:::
