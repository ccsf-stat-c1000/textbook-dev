# Overview Wrap-Up

```{admonition} Learning Objectives
:class: note

- Explain the logic behind and the process of hypothesis testing. In particular, explain what the p-value is and how it is used to draw conclusions.
```

## Let's Summarize

We learned quite a lot about hypothesis testing. We learned the logic behind it, what the key elements are, and what types of conclusions we can and cannot draw in hypothesis testing. Here is a quick recap:

- Hypothesis testing assesses the evidence provided by the data against a null hypothesis ($H_0$, the "nothing special is going on" claim) and in favor of an alternative hypothesis ($H_a$, what we suspect is really going on).
- The process has four steps: state the hypotheses, collect and summarize the data (with a test statistic), assess the evidence with a p-value, and draw conclusions in context.
- The *p-value* is the probability of getting data like those observed (or more extreme) when $H_0$ is true. The smaller the p-value, the stronger the evidence against $H_0$.
- If the p-value is below the significance level α (usually 0.05), we reject $H_0$ and accept $H_a$; the results are *statistically significant*. Otherwise we conclude that the data do not provide enough evidence to reject $H_0$—which is *not* the same as accepting $H_0$.

```{note} Video
[Hypothesis Testing](https://www.youtube.com/watch?v=GzkWcsJyPH4)
```

## Did I Get This?

*Background:* Based on the National Center for Health Statistics, the proportion of babies born at low birth weight (below 2,500 grams) in the United States is roughly 0.078, or 7.8% (based on all the births in the United States in the year 2002). A study was done in order to check whether smoking by pregnant women increases the risk of low birth weight. In other words, the researchers wanted to check whether the proportion of babies born at low birth weight among women who smoked during their pregnancy is higher than the proportion in the general population. The researchers followed a sample of 400 women who had smoked during their pregnancy and recorded the birth weight of the newborns. Based on the data, the p-value was found to be 0.016.

:::{quiz} What are the hypotheses being tested in this study?
:hint: The null hypothesis says smokers are no different from the general population.
:feedback-0: Correct! H₀: the proportion of low-birth-weight babies among smokers is 0.078 (same as the general population); Hₐ: the proportion is higher than 0.078.
:feedback-1: This reverses the null and alternative hypotheses.
:feedback-2: The researchers specifically suspected an INCREASED risk, so the alternative is one-sided (higher), not two-sided.
* *H₀: the proportion among smokers is 0.078; Hₐ: the proportion among smokers is higher than 0.078
* H₀: the proportion among smokers is higher than 0.078; Hₐ: the proportion is 0.078
* H₀: the proportion among smokers is 0.078; Hₐ: the proportion is not 0.078
:::

:::{quiz} Using a 0.05 significance level, what is the correct conclusion from the p-value of 0.016?
:hint: Compare 0.016 with 0.05, and state the conclusion in context.
:feedback-0: Correct! Since 0.016 < 0.05, we reject H₀ and conclude that smoking during pregnancy is associated with an increased proportion of low-birth-weight babies.
:feedback-1: 0.016 is smaller than 0.05, so the data DO provide significant evidence against H₀.
:feedback-2: The conclusion must be drawn in context, not just stated symbolically.
* *Reject H₀ and conclude that the proportion of low-birth-weight babies among smokers is higher than 7.8%
* Do not reject H₀—the evidence is not strong enough
* Reject H₀ (no further conclusion is needed)
:::

The same researchers also wanted to examine whether second-hand smoking (exposure to another person smoking) by pregnant women increases the risk of low birth weight (i.e., whether the proportion of babies born at a low birth weight among women who were second-hand smokers during their pregnancy is higher than the proportion in the general population). The researchers obtained a sample of 175 pregnant women who were second-hand smokers, followed them during their pregnancies, and found that 10.2% of the newborns had low birth weight. Based on these data, the p-value was found to be 0.119.

:::{quiz} What is the correct interpretation of the p-value of 0.119?
:hint: The p-value assumes H₀ (proportion = 0.078) is true.
:feedback-0: Correct! If the true proportion among second-hand smokers were 0.078, there would be a 0.119 probability of getting a sample proportion of 10.2% or higher in a sample of 175.
:feedback-1: The p-value is not the probability that H₀ is true.
:feedback-2: The p-value is not the proportion of low-birth-weight babies—that was 10.2%.
* *If the true proportion were 7.8%, there would be a 0.119 chance of a sample proportion of 10.2% or higher
* There is a 0.119 probability that second-hand smoking has no effect
* 11.9% of the babies in the sample had low birth weight
:::

:::{quiz} Using a 0.05 significance level, what is the correct conclusion for the second-hand smoking study?
:hint: 0.119 > 0.05—and remember what failing to reject does and does not mean.
:feedback-0: Correct! Since 0.119 > 0.05, the data do not provide enough evidence to conclude that second-hand smoking increases the risk of low birth weight.
:feedback-1: The p-value exceeds 0.05, so the results are NOT statistically significant.
:feedback-2: Failing to reject H₀ does not prove that second-hand smoking has no effect—we simply lack sufficient evidence of one.
* *Do not reject H₀—the data do not provide enough evidence that second-hand smoking increases the risk
* Reject H₀ and conclude that second-hand smoking increases the risk
* Accept H₀ and conclude that second-hand smoking has no effect on birth weight
:::

:::{quiz} Even though the sample proportion among second-hand smokers (10.2%) was above 7.8%, the study did not reach a significant result, while the smoking study did. Which factor best explains why a sample result can fail to be significant?
:hint: Think about what makes an observed difference "surprising" under H₀—both the size of the difference and the sample size matter.
:feedback-0: Correct! With a smaller sample (175 vs. 400) and a modest difference, a sample proportion of 10.2% is not surprising enough under H₀—chance alone could reasonably produce it.
:feedback-1: The direction of the difference was consistent with Hₐ; the issue is the strength of the evidence, not its direction.
:feedback-2: The p-value was computed correctly—non-significance reflects insufficient evidence, not an error.
* *The observed difference was small enough, and the sample small enough, that chance alone could plausibly explain it
* The sample proportion went in the wrong direction
* The p-value must have been miscalculated
:::
