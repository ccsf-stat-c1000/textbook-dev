# Step 4: Drawing Conclusions from the P-value

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Step 4: Drawing Conclusions Based on the P-value

This last part of the four-step process of hypothesis testing is the same across all statistical tests, and actually, we've already said basically everything there is to say about it, but it can't hurt to say it again.

The p-value is a measure of how much evidence the data present against $H_0$. The smaller the p-value, the more evidence the data present against $H_0$.

We already mentioned that what determines what constitutes enough evidence against $H_0$ is the *significance level* (α), a cutoff point below which the p-value is considered small enough to reject $H_0$ in favor of $H_a$. The most commonly used significance level is 0.05.

It is important to mention again that this step has essentially two sub-steps:

1. Based on the p-value, determine whether or not the results are significant (i.e., whether the data present enough evidence to reject $H_0$).
2. State your conclusions in the context of the problem.

Let's go back to our three examples and draw conclusions.

:::{admonition} Example 1: Defective Products
:class: tip

Has the proportion of defective products been reduced from 0.20 as a result of the repair?

We found that the p-value for this test was 0.023.

Since 0.023 is small (in particular, 0.023 < 0.05), the data provide enough evidence to reject $H_0$, and we conclude that as a result of the repair the proportion of defective products has been reduced to below 0.20.

Here is the complete story of this example: $H_0: p = 0.20$ vs. $H_a: p < 0.20$; a random sample of n = 400 gave $\hat{p} = 64/400 = 0.16$; the test statistic was z = −2; the p-value was 0.023; since the p-value is small, we reject $H_0$.
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

Is the proportion of students who use marijuana at the college higher than the national proportion, which is 0.157?

We found that the p-value for this test was 0.182.

Since 0.182 is *not* small (in particular, 0.182 > 0.05), the data do not provide enough evidence to reject $H_0$. We therefore do *not* have enough evidence to conclude that the proportion of students at the college who use marijuana is higher than the national figure.

Here is the complete story of this example: $H_0: p = 0.157$ vs. $H_a: p > 0.157$; a random sample of n = 100 gave $\hat{p} = 19/100 = 0.19$; the test statistic was z = 0.91; the p-value was 0.182; since the p-value is not small, we cannot reject $H_0$.
:::

## Learn By Doing

:::{quiz} In example 2 the sample proportion (0.19) was above the national figure (0.157), yet we did not reject H₀. Which statement best explains this?
:hint: Think about how much sample proportions vary in samples of only 100 students.
:feedback-0: Correct! With n = 100, getting a sample proportion of 0.19 when the true proportion is 0.157 is not surprising (probability 0.182)—chance alone is a reasonable explanation.
:feedback-1: The data leaned in the direction of Hₐ, but not strongly enough to rule out chance.
:feedback-2: We can never accept H₀; we simply lack evidence against it.
* *A sample proportion of 0.19 is not surprising when p = 0.157 and n = 100—the difference is within chance variation
* The sample proportion actually contradicted the alternative hypothesis
* We proved that the college's marijuana use rate equals the national rate
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

Has the proportion of U.S. adults who support the death penalty for convicted murderers changed since 2003, when it was 0.64?

We found that the p-value for this test was 0.021.

Since 0.021 is small (in particular, 0.021 < 0.05), the data provide enough evidence to reject $H_0$, and we conclude that the proportion of adults who support the death penalty for convicted murderers has changed since 2003.

Here is the complete story of this example: $H_0: p = 0.64$ vs. $H_a: p \neq 0.64$; a random sample of n = 1,000 gave $\hat{p} = 675/1000 = 0.675$; the test statistic was z = 2.31; the p-value was 0.021; since the p-value is small, we reject $H_0$.
:::

## Did I Get This?

Two hypothesis tests were conducted. In test I, a significance level of 0.05 was used, and the p-value was calculated to be 0.025. In test II, a significance level of 0.01 was used, and the p-value was calculated to be 0.025.

:::{quiz} What is the conclusion of test I?
:hint: Compare the p-value 0.025 with α = 0.05.
:feedback-0: Correct! 0.025 < 0.05, so the results are significant and H₀ is rejected.
:feedback-1: 0.025 is smaller than the significance level 0.05, so H₀ IS rejected.
* *Reject H₀—the results are statistically significant at the 0.05 level
* Do not reject H₀—the results are not statistically significant
:::

:::{quiz} What is the conclusion of test II?
:hint: Compare the p-value 0.025 with α = 0.01.
:feedback-0: Correct! 0.025 > 0.01, so at the stricter 0.01 level the data do not provide enough evidence to reject H₀.
:feedback-1: At the 0.01 level, a p-value of 0.025 is NOT small enough to reject H₀.
* *Do not reject H₀—the results are not statistically significant at the 0.01 level
* Reject H₀—the results are statistically significant
:::

:::{quiz} The same p-value (0.025) led to different conclusions in tests I and II. What does this illustrate?
:hint: The p-value measures the evidence; α is the standard we hold that evidence to.
:feedback-0: Correct! The conclusion depends not only on the strength of the evidence (the p-value) but also on how demanding a standard of evidence (α) we choose before the test.
:feedback-1: The p-value was identical in both tests—what differed was the significance level.
:feedback-2: Neither test was done incorrectly; different fields legitimately use different significance levels.
* *The conclusion depends on the chosen significance level as well as the p-value
* The two tests must have had different p-values
* One of the two tests must have been done incorrectly
:::

```{admonition} Many Students Wonder: Why 0.05?
:class: important

The 0.05 significance level has no deep mathematical justification—it is a convention that has proven practical: strict enough to screen out most chance findings, lenient enough that real effects of reasonable size can be detected with realistic sample sizes. When the consequences of a false rejection are serious (for example, approving a new drug), researchers often use a stricter level such as 0.01. The important thing is to choose the significance level *before* looking at the data.
```
