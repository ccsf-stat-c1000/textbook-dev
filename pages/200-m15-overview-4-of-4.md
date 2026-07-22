# Significance Level and Drawing Conclusions

## Hypothesis Testing Step 4: Making Conclusions

Since our conclusion is based on how small the p-value is, or in other words, how surprising our data are when $H_0$ is true, it would be nice to have some kind of guideline or cutoff that will help determine how small the p-value must be, or how "rare" (unlikely) our data must be when $H_0$ is true, for us to conclude that we have enough evidence to reject $H_0$.

This cutoff exists, and because it is so important, it has a special name. It is called the *significance level of the test* and is usually denoted by the Greek letter α. The most commonly used significance level is α = 0.05 (or 5%). This means that:

- If the p-value < α (usually 0.05), then the data we got are considered to be "rare (or surprising) enough" when $H_0$ is true, and we say that the data provide significant evidence against $H_0$, so we reject $H_0$ and accept $H_a$.
- If the p-value > α (usually 0.05), then our data are not considered to be "surprising enough" when $H_0$ is true, and we say that our data do not provide enough evidence to reject $H_0$ (or, equivalently, that the data do not provide enough evidence to accept $H_a$).

*Important comment about wording.* Another common wording (mostly in scientific journals) is:

- "The results are *statistically significant*" — when the p-value < α.
- "The results are *not statistically significant*" — when the p-value > α.

```{admonition} Comments
:class: important

1. Although the significance level provides a good guideline for drawing our conclusions, it should not be treated as an incontrovertible truth. There is a lot of room for personal interpretation. What if your p-value is 0.052? You might want to stick to the rules and say "0.052 > 0.05 and therefore I don't have enough evidence to reject $H_0$," but you might decide that 0.052 is small enough for you to believe that $H_0$ should be rejected. It should be noted that scientific journals do consider 0.05 to be the cutoff point, so that any p-value below the cutoff indicates enough evidence against $H_0$, and any p-value above it, *or even equal to it*, indicates there is not enough evidence against $H_0$.

2. It is important to draw your conclusions *in context*. It is *never enough* to say: "p-value = ..., and therefore I have enough evidence to reject $H_0$ at the 0.05 significance level." You *should always add:* "... and conclude that ... (what it means in the context of the problem)."

3. Let's go back to the nature of the two types of conclusions we can make. *Either* we reject $H_0$ and accept $H_a$ (when the p-value is smaller than the significance level), *or* we cannot reject $H_0$ (when the p-value is larger than the significance level).
```

As we mentioned earlier, note that the second conclusion does not imply that we accept $H_0$, but just that we don't have enough evidence to reject it. Saying (by mistake) "I don't have enough evidence to reject $H_0$ so I accept it" indicates that the data provide evidence that $H_0$ is true, which is *not necessarily the case*. Consider the following slightly artificial yet effective example:

:::{admonition} Example: Equal Opportunity Hiring
:class: tip

An employer claims to subscribe to an "equal opportunity" policy, not hiring men any more often than women for managerial positions. Is this credible? You're not sure, so you want to test the following *two hypotheses:*

- $H_0$: The proportion of male managers hired is 0.5.
- $H_a$: The proportion of male managers hired is more than 0.5.

*Data:* You choose at random three of the new managers who were hired in the last 5 years and find that all 3 are men.

*Assessing evidence:* If the proportion of male managers hired is really 0.5 ($H_0$ is true), then the probability that a random selection of three managers will yield three males is 0.5 × 0.5 × 0.5 = 0.125. This is the p-value.

*Conclusion:* Using 0.05 as the significance level, you conclude that since the p-value = 0.125 > 0.05, the fact that the three randomly selected managers were all males is not enough evidence to reject $H_0$. In other words, you do not have enough evidence to reject the employer's claim of subscribing to an equal opportunity policy.

However, *the data (all three selected are males) definitely do not provide evidence to accept the employer's claim* ($H_0$).
:::

## Check Your Understanding: Interpreting the P-value and Significance

The following two hypotheses are tested:

- $H_0$: The proportion of U.S. adults who support gay marriage is roughly 50%.
- $H_a$: The proportion of U.S. adults who support gay marriage is above 50% (i.e., a majority support it).

Suppose a survey was conducted in which a random sample of 1,100 U.S. adults was asked about their opinions about gay marriage, and based on the data, the p-value was found to be 0.002. Throughout this activity use a 0.05 (5%) significance level (cutoff).

:::{quiz} What is the correct interpretation of the p-value of 0.002 in this context?
:hint: The p-value is a conditional probability: it assumes H₀ is true.
:feedback-0: Correct! The p-value is the probability of observing sample results like ours (or more extreme) IF the true proportion of supporters were 50%.
:feedback-1: The p-value is not the probability that H₀ is true—hypotheses are not events with probabilities in this framework.
:feedback-2: The p-value is not the probability that Hₐ is true.
* *If 50% of U.S. adults supported gay marriage, there would be only a 0.002 chance of getting sample results like those observed (or more extreme)
* There is a 0.002 probability that H₀ is true
* There is a 0.002 probability that a majority supports gay marriage
:::

:::{quiz} Based on the p-value of 0.002, what is the correct conclusion?
:hint: Compare the p-value with α = 0.05.
:feedback-0: Correct! Since 0.002 < 0.05, the data provide significant evidence against H₀, so we reject it and conclude that a majority of U.S. adults support gay marriage.
:feedback-1: 0.002 is SMALLER than 0.05, so we do reject H₀.
:feedback-2: We do reject H₀, but the conclusion must be stated in context—about the proportion of supporters, not just symbols.
* *Reject H₀ and conclude that a majority of U.S. adults support gay marriage
* Do not reject H₀—the evidence is not strong enough
* Accept H₀ and conclude that exactly 50% support gay marriage
:::

:::{quiz} Which statement best describes what "the results are statistically significant" means here?
:hint: Statistical significance is about the strength of the evidence, judged against α.
:feedback-0: Correct! Statistically significant means the p-value fell below the significance level—the data would be quite surprising if H₀ were true.
:feedback-1: Statistical significance does not measure the practical size or importance of an effect.
:feedback-2: A significant result provides strong evidence against H₀, not certainty.
* *The p-value is below 0.05, so the data provide strong evidence against H₀
* The difference found is large and practically important
* We have proven with certainty that a majority supports gay marriage
:::

## Check Your Understanding: Drawing a Conclusion from the P-value

The following two hypotheses are tested:

- $H_0$: The average number of miles driven per year is 12,000.
- $H_a$: The average number of miles driven per year is less than 12,000.

In a survey, 1,600 randomly selected drivers were asked the number of miles they drive yearly. Based upon the results, the p-value = 0.068. Throughout this activity use a 0.05 (5%) significance level.

:::{quiz} What is the correct interpretation of the p-value of 0.068?
:hint: Condition on H₀ being true.
:feedback-0: Correct! If the true average were 12,000 miles, there would be a 0.068 probability of getting sample results like those observed (or more extreme in the direction of Hₐ).
:feedback-1: The p-value is not the probability that H₀ is true.
:feedback-2: This describes α, the significance level—not the p-value.
* *If the true average were 12,000 miles, there would be a 0.068 chance of sample results like these (or more extreme)
* There is a 0.068 probability that the average is 12,000 miles
* 0.068 is the cutoff for deciding whether results are surprising
:::

:::{quiz} Based on the p-value of 0.068, what is the correct conclusion?
:hint: Compare 0.068 with 0.05, and be careful with the wording.
:feedback-0: Correct! Since 0.068 > 0.05, the data do not provide enough evidence to reject H₀. Note that we cannot ACCEPT H₀—we simply lack evidence against it.
:feedback-1: 0.068 is larger than 0.05, so the results are not statistically significant.
:feedback-2: Failing to reject H₀ is not the same as accepting it—the data do not prove the average is 12,000.
* *Do not reject H₀—the data do not provide enough evidence that the average is less than 12,000 miles
* Reject H₀ and conclude the average is less than 12,000 miles
* Accept H₀ and conclude the average is exactly 12,000 miles
:::
