# Hypothesis Testing for the Population Proportion p (11 of 13)

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 3. One-Sided Alternative vs. Two-Sided Alternative

Recall that earlier we noticed (only visually) that for a given value of the test statistic z, the p-value of the two-sided test is twice as large as the p-value of the one-sided test. We will now further discuss this issue. In particular, we will use our example 2 (marijuana users at a certain college) to gain better intuition about this fact.

For illustration purposes, we are actually going to use example 2* (where out of a *sample of size 400*, 76 were marijuana users). Let's recall example 2*, but this time give two versions of it: the original version, and a slightly changed version, which we'll call example 2**. The differences are emphasized.

:::{admonition} Example 2*
:class: tip

*There are rumors that students at a certain liberal arts college are more inclined to use drugs than U.S. college students in general.* Suppose that in a simple random sample of 400 students from the college, 76 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is 0.157?
:::

:::{admonition} Example 2**
:class: tip

*The dean of students in a certain liberal arts college was interested in whether the proportion of students who use drugs in her college is different from the proportion among U.S. college students in general.* Suppose that in a simple random sample of 400 students from the college, 76 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) *differs* from the national proportion, which is 0.157?
:::

## Learn By Doing

:::{quiz} What is the appropriate alternative hypothesis in each of the two versions?
:hint: Example 2* starts from rumors of a HIGHER rate; example 2** simply asks whether the rate is DIFFERENT.
:feedback-0: Correct! The rumors in 2* justify the one-sided Hₐ: p > 0.157, while the neutral question in 2** calls for the two-sided Hₐ: p ≠ 0.157.
:feedback-1: It's the reverse—the prior suspicion of a higher rate (2*) is what justifies a one-sided alternative.
:feedback-2: The two versions have different research questions and therefore different alternatives.
* *2*: Hₐ: p > 0.157; 2**: Hₐ: p ≠ 0.157
* 2*: Hₐ: p ≠ 0.157; 2**: Hₐ: p > 0.157
* Both use Hₐ: p > 0.157
:::

Indeed, in example 2* we suspect from the outset (based on the rumors) that the overall proportion (p) of marijuana smokers at the college is *higher* than the reported national proportion of 0.157, and therefore the appropriate alternative is $H_a: p > 0.157$. In example 2**, as a result of the change of wording (which eliminated the part about the rumors), we simply wonder if p is *different* (in either direction) from the reported national proportion of 0.157, and therefore the appropriate alternative is the two-sided $H_a: p \neq 0.157$. Would switching to the two-sided alternative have an effect on our results? Let's explore that.

:::{admonition} Example 2*
:class: tip

We already carried out the test for this example: $H_0: p = 0.157$ vs. $H_a: p > 0.157$; n = 400; $\hat{p} = 76/400 = 0.19$; z = 1.81. The p-value is the area under the standard normal curve to the right of 1.81, which is 0.035. Since 0.035 < 0.05, we rejected $H_0$.
:::

:::{admonition} Example 2**
:class: tip

*Step 1:* Here we are testing $H_0: p = 0.157$ vs. $H_a: p \neq 0.157$.

*Step 2:* Since we have the same data as in example 2* (76 marijuana users out of 400), we have the same sample proportion and the same test statistic: $\hat{p} = 0.19$ and z = 1.81.

*Step 3:* Since the calculation of the p-value depends on the type of alternative we have, here is where things start to be different. For the two-sided alternative, the p-value is the area in *both* tails: the area to the right of 1.81 (0.035) plus the area to the left of −1.81 (0.035), giving a p-value of 0.070.

*Step 4:* If we use the 0.05 level of significance, the p-value we got is not small enough (0.070 > 0.05), and therefore we cannot reject $H_0$. In other words, the data do not provide enough evidence to conclude that the proportion of marijuana smokers in the college is different from the national proportion (0.157).
:::

What happened here?

It should be pretty clear what happened numerically. The p-value of the one-sided test (example 2*) is 0.035, suggesting the results are significant at the 0.05 significance level. However, the p-value of the two-sided test (example 2**) is twice the p-value of the one-sided test, and is therefore 2 × 0.035 = 0.070, suggesting that the results are not significant at the 0.05 significance level.

Here is a more conceptual explanation:

The idea is that in example 2*, we began our hypothesis test with a piece of information (in the form of a rumor) about the unknown population proportion p, which gave us a sort of head start toward the goal of rejecting the null hypothesis. We found that the evidence the data provided was then enough to cross the finish line and reject $H_0$. In example 2**, we had no prior information to go on, and the data alone were not enough evidence to cross the finish line and reject $H_0$.

We can summarize and say that in general it is harder to reject $H_0$ against a two-sided $H_a$ because the p-value is twice as large. Intuitively, a one-sided alternative gives us a head start, and on top of that we have the evidence provided by the data. When our alternative is two-sided, we get no head start and all we have are the data, and therefore it is harder to cross the finish line and reject $H_0$.

## Did I Get This?

Consider the following two hypothesis testing scenarios for the population proportion (p) and corresponding studies:

*I.* The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. A study was designed in order to examine whether that proportion has *changed* since.

*II.* The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. In light of the increasing problem of spyware, a study was designed in order to examine whether that proportion has *increased* since.

:::{quiz} Suppose both studies collect the same data, and the test statistic is z = 1.9. Which study will have the smaller p-value?
:hint: Study I is two-sided; study II is one-sided.
:feedback-0: Correct! Study II's one-sided p-value is P(Z ≥ 1.9) ≈ 0.029, while study I's two-sided p-value doubles it: ≈ 0.057.
:feedback-1: Study I uses a two-sided alternative, which doubles the p-value.
:feedback-2: The p-values differ by a factor of 2 because the alternatives differ.
* *Study II—its one-sided p-value is half of study I's two-sided p-value
* Study I—two-sided tests have smaller p-values
* Both p-values are the same
:::

:::{quiz} With z = 1.9 and α = 0.05, what are the conclusions of the two studies?
:hint: One-sided p-value ≈ 0.029; two-sided p-value ≈ 0.057.
:feedback-0: Correct! Study II rejects H₀ (0.029 < 0.05) while study I does not (0.057 > 0.05)—the same data can lead to different conclusions depending on the alternative.
:feedback-1: The two studies reach DIFFERENT conclusions, since only the one-sided p-value falls below 0.05.
:feedback-2: Study I's p-value (≈0.057) exceeds 0.05, so it cannot reject H₀.
* *Study II rejects H₀; study I does not
* Both studies reject H₀
* Study I rejects H₀; study II does not
:::
