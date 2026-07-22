# A Confidence Interval for the Mean Difference

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
- Specify the null and alternative hypotheses for comparing groups.
```

## Confidence Interval for μ_d (Paired t Confidence Interval)

So far we've discussed the paired t-test, which checks whether there is enough evidence stored in the data to reject the claim that $\mu_d=0$ in favor of one of the three possible alternatives.

If we would like to estimate $\mu_d$, the mean of the differences (response 1 − response 2), we can use the natural point estimate, $\bar{x}_d$, the sample mean of the differences, or preferably, use a 95% confidence interval, which will provide us with a set of plausible values for $\mu_d$.

In particular, if the test has rejected $H_0: \mu_d=0$, a confidence interval for $\mu_d$ can be insightful, since it quantifies the effect that the categorical explanatory variable has on the response variable.

(*Comment:* we will not go into the formula and calculation of the confidence interval, but rather ask our statistical software to do it for us, and focus on interpretation.)

:::{admonition} Example: Drunk Drivers
:class: tip

Recall our leading example about whether drivers are impaired after having two beers, which was reduced to inference about a single mean, the mean of the differences in reaction time (before − after).

The p-value of our test, $H_0: \mu_d=0$ vs. $H_a: \mu_d<0$, was 0.009, and we therefore rejected $H_0$ and concluded that the mean difference in total reaction time (before − after) was negative—or in other words, that drivers are impaired after having two beers. As a follow-up to this conclusion, it would be interesting to quantify the effect that two beers have on the driver, using the 95% confidence interval for $\mu_d$.

Using statistical software, we find that the 95% confidence interval for $\mu_d$, the mean of the differences (before − after), is roughly (−0.9, −0.1).

We can therefore say with 95% confidence that drinking two beers increases the total reaction time of the driver by between 0.1 and 0.9 of a second.
:::

```{admonition} Comment
:class: important

As we've seen in previous tests, the 95% confidence interval for $\mu_d$ can be used for testing in the two-sided case ($H_0: \mu_d=0$ vs. $H_a: \mu_d\neq0$):

- If the null value, 0, falls *outside* the confidence interval, $H_0$ is rejected.
- If the null value, 0, falls *inside* the confidence interval, $H_0$ is not rejected.
```

:::{admonition} Example: IQ Scores of Twins Reared Apart
:class: tip

Let's go back to our twin study example, where we found a 95% confidence interval for $\mu_d$ of (−6.113, 0.301) and a p-value of 0.074.

We used the fact that the p-value is 0.074 to conclude that $H_0$ cannot be rejected (at the 0.05 significance level), and that whether or not a person was raised by his or her birth parents doesn't necessarily have an effect on intelligence (as measured by IQ scores). The comment above tells us that we can also use the confidence interval to reach the same conclusion, since 0 falls inside the confidence interval for $\mu_d$. In other words, since 0 is a plausible value for $\mu_d$, we cannot reject $H_0$, which claims that $\mu_d=0$.
:::

## Check Your Understanding: Confidence Interval for the Mean Difference

A publishing company wanted to test whether typing speed differs when using word processor A or word processor B. A random sample of 25 typists was selected, and the typing speeds (in words per minute) were recorded for each typist when using word processor A and then when using word processor B. (Which word processor was used first was determined for each typist by a coin flip.)

Based on the collected data, a 95% confidence interval for $\mu_d$, the mean difference (word processor A − word processor B), was found to be (2.5, 7.8). The appropriate hypotheses for testing whether the typing speeds differ are the two-sided test $H_0: \mu_d = 0$ vs. $H_a: \mu_d \neq 0$.

:::{quiz} Based on the confidence interval, what is the conclusion of the two-sided test at the 0.05 significance level?
:hint: Is 0 inside (2.5, 7.8)?
:feedback-0: Correct! 0 falls outside the interval, so it is not a plausible value for μ_d, and we reject H₀—typing speeds differ between the two word processors.
:feedback-1: 0 is NOT inside (2.5, 7.8)—the interval starts at 2.5.
:feedback-2: The interval method applies here directly, since the test is two-sided and the levels match (95% and 0.05).
* *Reject H₀—typing speeds differ between the two word processors
* Do not reject H₀—0 is a plausible value for μ_d
* The confidence interval cannot be used to carry out the test
:::

:::{quiz} What additional insight does the interval (2.5, 7.8) provide beyond the test conclusion?
:hint: The differences were computed as (A − B), and the whole interval is positive.
:feedback-0: Correct! Since the interval is entirely positive, typists are faster with word processor A—by between 2.5 and 7.8 words per minute, with 95% confidence.
:feedback-1: The direction is the opposite: positive differences (A − B) mean A produced HIGHER speeds.
:feedback-2: The interval describes the mean difference, not the speeds of individual typists.
* *Typists average between 2.5 and 7.8 more words per minute with word processor A than with B
* Typists are faster with word processor B
* Every typist types 2.5 to 7.8 words per minute faster with A
:::
