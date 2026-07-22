# A Confidence Interval for the Difference of Two Means

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Confidence Interval for μ₁ − μ₂ (Two-Sample t Confidence Interval)

So far we've discussed the two-sample t-test, which checks whether there is enough evidence stored in the data to reject the claim that $\mu_1-\mu_2=0$ (or equivalently, that $\mu_1=\mu_2$) in favor of one of the three possible alternatives.

If we would like to estimate $\mu_1-\mu_2$, we can use the natural point estimate, $\bar{y}_1-\bar{y}_2$, or preferably, a 95% confidence interval, which will provide us with a set of plausible values for the difference between the population means $\mu_1-\mu_2$.

In particular, if the test has rejected $H_0: \mu_1-\mu_2=0$, a confidence interval for $\mu_1-\mu_2$ can be insightful, since it quantifies the effect that the categorical explanatory variable has on the response.

```{admonition} Comment
:class: important

We will not go into the formula and calculation of the confidence interval, but rather ask our software to do it for us, and focus on interpretation.
```

:::{admonition} Example: Looks vs. Personality
:class: tip

Recall our leading example about the looks vs. personality score of females (population 1, n = 150) and males (population 2, n = 85). Statistical software tells us that the 95% confidence interval for $\mu_1-\mu_2$ is roughly (−3.7, −1.5).

Recall that we rejected the null hypothesis in favor of the two-sided alternative and concluded that the mean score of females is different from the mean score of males. It would be interesting to supplement this conclusion with more details about this difference between the means, and the 95% confidence interval for $\mu_1-\mu_2$ does exactly that.

First, note that the confidence interval is strictly negative, suggesting that $\mu_1$ is lower than $\mu_2$. Furthermore, the confidence interval tells us that we are 95% confident that the mean "looks vs. personality score" of females ($\mu_1$) is between 1.5 and 3.7 points *lower* than the mean score of males ($\mu_2$). The confidence interval therefore quantifies the effect that the explanatory variable (gender) has on the response (looks vs. personality score).
:::

## Check Your Understanding: Confidence Interval for a Difference of Means

In the NHANES weight example, software reports that a 95% confidence interval for μ₁ − μ₂ (younger minus older males) is (3.1, 6.7) kg.

:::{quiz} Which is the correct interpretation of this interval?
:hint: The interval estimates the difference between the two population means.
:feedback-0: Correct! We are 95% confident that younger males weigh, on average, between 3.1 and 6.7 kg more than older males.
:feedback-1: The interval describes the difference between population MEANS, not the weights of individuals.
:feedback-2: The interval concerns the difference between the group means, not either group's mean by itself.
* *We are 95% confident that the mean weight of younger males exceeds that of older males by between 3.1 and 6.7 kg
* 95% of younger males weigh 3.1 to 6.7 kg more than older males
* We are 95% confident that the mean weight of younger males is between 3.1 and 6.7 kg
:::

:::{quiz} A different study reports a 95% confidence interval for μ₁ − μ₂ of (−1.2, 4.8). What does this tell us about the two-sided test of H₀: μ₁ − μ₂ = 0 at the 0.05 level?
:hint: Is 0 inside the interval?
:feedback-0: Correct! Since 0 is inside the interval, it is a plausible value for the difference, so H₀ cannot be rejected.
:feedback-1: 0 IS inside (−1.2, 4.8), so we cannot reject H₀.
:feedback-2: The interval tells us exactly what the two-sided test at the matching level would conclude.
* *H₀ would not be rejected—0 is a plausible value for the difference
* H₀ would be rejected—the interval shows a difference exists
* The confidence interval says nothing about the test
:::
