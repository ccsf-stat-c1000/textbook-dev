# The Two-Sample t-Test: A Worked Example

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
- Specify the null and alternative hypotheses for comparing groups.
```

Let's look at another example, and then you'll do one yourself.

:::{admonition} Example: Weight and Age Group
:class: tip

According to the National Health and Nutrition Examination Survey (NHANES) sponsored by the U.S. government, a random sample of 712 males between 20 and 29 years of age and a random sample of 1,001 males over the age of 75 were chosen, and the weight of each of the males was recorded (in kg). Here is a summary of the results:

| Group | n | Mean weight (kg) | Standard deviation |
| --- | --- | --- | --- |
| Males 20-29 years old | 712 | 83.4 | 18.7 |
| Males 75+ years old | 1,001 | 78.5 | 19.0 |

Do the data provide evidence that the younger male population weighs more (on average) than the older male population? (Note that here the data are given in summarized form, unlike the previous problem, where the raw data were given.)

Note that we defined the younger age group and the older age group as population 1 and population 2, respectively, and $\mu_1$ and $\mu_2$ as the mean weight of population 1 and population 2, respectively.

*Step 1:* Since we want to test whether the older age group (population 2) weighs less on average than the younger age group (population 1), we are testing:

$$H_0: \mu_1 - \mu_2 = 0 \quad \text{vs.} \quad H_a: \mu_1 - \mu_2 > 0$$

or equivalently, $H_0: \mu_1 = \mu_2$ vs. $H_a: \mu_1 > \mu_2$.

*Step 2:* We can safely use the two-sample t-test in this case since:

1. The samples are independent, since each of the samples was chosen at random.
2. Both sample sizes are very large (712 and 1,001), and therefore we can proceed regardless of whether the populations are normal or not.

From these data we calculate the t-statistic:

$$t=\frac{(83.4-78.5)-0}{\sqrt{\frac{18.7^{2}}{712}+\frac{19.0^{2}}{1001}}}\approx5.31$$

The t-value is quite large, indicating that our data are very different from what is claimed in the null hypothesis.

*Step 3:* The p-value is essentially 0, indicating that it would be nearly impossible to observe a difference between the sample mean weights of 4.9 kg (or more) if the mean weights in the two age group populations were the same (i.e., if $H_0$ were true).

*Step 4:* A p-value of 0 (or very close to it) indicates that the data provide strong evidence against $H_0$, so we reject it and conclude that the mean weight of males 20-29 years old is higher than the mean weight of males 75 years old and older. In other words, males in the younger age group weigh more, on average, than males in the older age group.
:::

Now you try one!

## Learn By Doing

Recall the pregnancy length study: to check the claim that the pregnancy length of women who smoke during pregnancy is shorter, on average, than that of women who do not smoke, a random sample of 35 pregnant smokers (population 1) and a random sample of 35 pregnant non-smokers (population 2) were followed. The results: smokers had a mean pregnancy length of 260 days with standard deviation 15 days; non-smokers had a mean of 267 days with standard deviation 14 days.

:::{quiz} Can the two-sample t-test be safely used here, and what is the value of the test statistic?
:hint: t = (260 − 267)/√(15²/35 + 14²/35).
:feedback-0: Correct! The samples are independent and both have n = 35 > 30. The standard error is √(225/35 + 196/35) ≈ 3.47, so t = −7/3.47 ≈ −2.02.
:feedback-1: Check the standard error: √(225/35 + 196/35) ≈ 3.47, so t ≈ −2.02, not −0.24.
:feedback-2: The conditions ARE met: independent random samples with 35 in each group.
* *Yes—conditions are met; t ≈ −2.02
* Yes—conditions are met; t ≈ −0.24
* No—the samples are too small
:::

:::{quiz} The one-sided p-value for t = −2.02 is about 0.024. Using α = 0.05, what is the conclusion?
:hint: The alternative was Hₐ: μ₁ − μ₂ < 0 (smokers shorter).
:feedback-0: Correct! Since 0.024 < 0.05, we reject H₀ and conclude that pregnancies of smokers are, on average, shorter than those of non-smokers.
:feedback-1: 0.024 is smaller than 0.05, so the results ARE significant.
:feedback-2: The conclusion should be about mean pregnancy length in the populations, stated in context.
* *Reject H₀—the data provide evidence that smoking during pregnancy is associated with shorter pregnancies
* Do not reject H₀—the evidence is insufficient
* Reject H₀ (no context needed)
:::
