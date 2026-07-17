# After ANOVA: Which Means Differ?

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Final Comment

The ANOVA F-test does not provide any insight into *why* $H_0$ was rejected; it does not tell us in what way $\mu_1, \mu_2, \ldots, \mu_k$ are not all equal. We would like to know which pairs of μ's are not equal. As an exploratory (or visual) aid to get that insight, we may take a look at the confidence intervals for the group population means that appear in the output. More specifically, we should look at the position of the confidence intervals and the overlap (or lack thereof) between them.

If the confidence interval for, say, $\mu_i$ overlaps with the confidence interval for $\mu_j$, then $\mu_i$ and $\mu_j$ share some plausible values, which means that based on the data we have no evidence that these two μ's are different.

```{figure} images/gen/m16-ci-overlap.svg
:alt: Two confidence intervals on a number line that overlap, indicating shared plausible values and therefore no evidence that the two means differ.
```

If the confidence interval for $\mu_i$ does not overlap with the confidence interval for $\mu_j$, then $\mu_i$ and $\mu_j$ do not share plausible values, which means that the data suggest that these two μ's are different.

```{figure} images/gen/m16-ci-no-overlap.svg
:alt: Two confidence intervals on a number line that do not overlap, with the interval for mu i lying entirely below the interval for mu j, suggesting that mu i is smaller than mu j.
```

Furthermore, if (as in the figure above) the confidence interval for $\mu_i$ lies entirely below the confidence interval for $\mu_j$, then the data suggest that $\mu_i$ is smaller than $\mu_j$.

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

Consider our first example on the level of academic frustration. The software output includes 95% confidence intervals for the four group means:

| Major | Sample mean | 95% confidence interval (approx.) |
| --- | --- | --- |
| Business | 7.3 | (6.5, 8.5) |
| English | 11.8 | (11, 13) |
| Mathematics | 13.2 | (12.5, 14.5) |
| Psychology | 14.0 | (13, 15) |

Based on the small p-value, we rejected $H_0$ and concluded that not all four frustration level means are equal—in other words, that frustration level is related to the student's major. To get more insight into that relationship, we can look at the confidence intervals above.

What we see is that the Business confidence interval is well below the other three (it doesn't overlap with any of them). The Mathematics confidence interval overlaps with both the English and the Psychology confidence intervals; however, there is no overlap between the English and Psychology confidence intervals.

This gives us the impression that the mean frustration level of Business students is lower than the mean in the other three majors. Within the other three majors, we get the impression that the mean frustration of Mathematics students may not differ much from the means of both English and Psychology students; however, the mean frustration of English students may be lower than the mean of Psychology students.

Note that this is only an exploratory/visual way of getting an impression of why $H_0$ was rejected, not a formal one. There is a formal way of doing it, called "multiple comparisons," which is beyond the scope of this course.
:::

## Let's Summarize

- The ANOVA F-test is used for comparing more than two population means when the samples (drawn from each of the populations we are comparing) are independent. We encounter this situation when we want to examine the relationship between a quantitative response variable and a categorical explanatory variable that has more than two values.

- The hypotheses that are being tested in the ANOVA F-test are $H_0: \mu_1=\mu_2=\cdots=\mu_k$ vs. $H_a$: not all the μ's are equal.

- The idea behind the ANOVA F-test is to check whether the variation among the sample means is due to true differences among the μ's or merely due to sampling variability, by looking at

  $$F=\frac{\text{variation among the sample means}}{\text{variation within the groups}}$$

- Once we verify that we can safely proceed with the ANOVA F-test, we use software to carry it out.

- If the ANOVA F-test has rejected the null hypothesis, we can look at the confidence intervals for the population means that are in the output to get a visual insight into why $H_0$ was rejected (i.e., which of the means differ).

## Check Your Understanding

:::{quiz} An ANOVA rejects H₀, and the 95% confidence intervals for the three group means are: group 1 (10, 14), group 2 (13, 17), group 3 (20, 24). What impression do the intervals give?
:hint: Check which intervals overlap.
:feedback-0: Correct! Group 3's interval doesn't overlap either of the others (suggesting μ₃ is larger), while groups 1 and 2 overlap on (13, 14), so we have no evidence those two means differ.
:feedback-1: Groups 1 and 2 DO overlap (both contain values between 13 and 14).
:feedback-2: The intervals give useful exploratory insight, even though a formal analysis would require multiple comparisons.
* *μ₃ appears larger than the other two means; μ₁ and μ₂ may not differ
* All three means appear different from each other
* The intervals tell us nothing about which means differ
:::
