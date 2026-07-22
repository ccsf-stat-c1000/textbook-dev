# Type I and Type II Errors

## What Can Go Wrong: Two Types of Errors

Statistical investigations involve making decisions in the face of uncertainty, so there is always some chance of making a wrong decision. In hypothesis testing, the following decisions can occur:

- If the null hypothesis is true and we do not reject it, it is a *correct decision*.
- If the null hypothesis is false and we reject it, it is a *correct decision*.
- If the null hypothesis is true, but we reject it, this is a *type I error*.
- If the null hypothesis is false, but we fail to reject it, this is a *type II error*.

| | $H_0$ is true | $H_0$ is false |
| --- | --- | --- |
| **Reject $H_0$** | Type I error | Correct decision |
| **Do not reject $H_0$** | Correct decision | Type II error |

Type I and type II errors are not caused by mistakes. They are the result of random chance. The *data* provide evidence for a conclusion that is false. It's no one's fault!

:::{admonition} Example: A Courtroom Analogy for Hypothesis Tests
:class: tip

Defendants standing trial for a crime are considered innocent until evidence shows they are guilty. It is the job of the prosecution to present evidence that shows the defendant is guilty "beyond a reasonable doubt." It is the job of the defense to challenge this evidence and establish a reasonable doubt. The jury weighs the evidence and makes a decision.

When a jury makes a decision, only two verdicts are possible:

- *Guilty:* the jury concludes that there is enough evidence to convict the defendant. The evidence is so strong that there is not a reasonable doubt of the defendant's guilt.
- *Not guilty:* the jury concludes that there is not enough evidence to conclude beyond a reasonable doubt that the person is guilty.

Notice that a verdict of "not guilty" is not a conclusion that the defendant is innocent. This verdict says only that there is not enough evidence to return a guilty verdict.

*How is this like a hypothesis test?*

The null hypothesis, $H_0$, in American courtrooms is "the defendant is innocent." The alternative hypothesis, $H_a$, is "the defendant is guilty." The evidence presented in the case is the data on which the verdict is based. In a courtroom, the defendant is assumed to be innocent until proven guilty. In a hypothesis test, we assume the null hypothesis is true until the data indicate otherwise.

The two possible verdicts are similar to the two conclusions that are possible in a hypothesis test. *Rejecting the null hypothesis* is equivalent to a guilty verdict: the evidence is strong enough for the jury to reject the initial assumption of innocence. *Failing to reject the null hypothesis* is equivalent to a "not guilty" verdict: the evidence is not strong enough to reject the assumption of innocence—which is not the same as proving innocence.

*How does the courtroom analogy relate to type I and type II errors?*

- *Type I error:* the evidence leads the jury to convict an innocent person. By analogy, we reject a true null hypothesis and accept a false alternative hypothesis.
- *Type II error:* the evidence leads the jury to declare a defendant not guilty when he is in fact guilty. By analogy, we fail to reject a null hypothesis that is false.

It would be nice to know when each of these errors is happening, but statistical decisions are based on evidence gathered through sampling, and our sampling evidence will sometimes fool us. As long as we are making decisions, we will never be able to eliminate the potential for these two types of errors. Thus, we need to learn how to adjust to the consequences of making them.
:::

## Check Your Understanding: Identifying Type I and Type II Errors

A double-blind experiment is conducted to investigate the side effects of hormone replacement therapy (HRT) for women with menopausal symptoms. The experiment randomly assigns more than 16,000 American women to either a hormone treatment or a placebo. After five years, the HRT study finds no significant difference in the proportion of women developing breast cancer and heart disease. Researchers decide, based on this finding, to allow the study to continue.

:::{quiz} If the researchers' decision is wrong, which type of error occurred?
:hint: The null hypothesis (no difference in side effects) was NOT rejected.
:feedback-0: Correct! Failing to reject H₀ when it is actually false (HRT really does increase risk) is a type II error.
:feedback-1: A type I error can only occur when H₀ IS rejected.
:feedback-2: One of the two errors is possible here—since H₀ was not rejected, only a type II error could have occurred.
* *Type II—the study may have missed a real increase in risk
* Type I—the study may have found a difference that isn't real
* No error is possible in this situation
:::

Suppose instead that at the end of the five-year study, a greater proportion of the hormone-treated group have breast cancer and heart disease. This observed difference is statistically significant. Researchers are so alarmed by the results that the experiment is ended early to prevent further harm to the health of the women participating in the hormone group.

:::{quiz} If the researchers' decision is wrong, which type of error occurred?
:hint: This time the null hypothesis WAS rejected.
:feedback-0: Correct! Rejecting H₀ when it is actually true (HRT really has no effect, and the observed difference was chance) is a type I error.
:feedback-1: A type II error can only occur when H₀ is NOT rejected.
* *Type I—the significant difference may have been due to chance
* Type II—the study may have missed a real effect
:::

A national poll conducted in 2010 determined that 61 percent of Americans did not support a certain political movement. In a poll of 1,000 Americans this year, 64 percent say they do not support the movement. Has opposition increased since 2010? We tested the following hypotheses at the 5 percent level of significance:

- $H_0$: the proportion of Americans this year who oppose the movement is 0.61.
- $H_a$: the proportion of Americans this year who oppose the movement is greater than 0.61.

The p-value is 0.026, so we reject the null hypothesis and conclude that public opposition is greater than 61% this year.

:::{quiz} Which type of error is possible in this situation, and what would it mean in context?
:hint: H₀ was rejected.
:feedback-0: Correct! Since H₀ was rejected, a type I error is possible: opposition may really still be 61%, and the poll's higher figure was just sampling variability.
:feedback-1: A type II error is not possible here, because H₀ was rejected.
:feedback-2: An error IS possible—rejecting H₀ can never be done with certainty.
* *Type I—opposition may actually still be 61%, and the sample result was due to chance
* Type II—the poll may have missed a real increase
* No error is possible, since the p-value was below 0.05
:::

## What Is the Probability That We Will Make a Type I Error?

If the significance level is 5 percent (α = 0.05), then 5 percent of the time we will reject the null hypothesis even if it is true. Of course we will not know whether the null hypothesis is true. But if it is, the natural variability that we expect in random samples will produce "rare" results 5 percent of the time.

This makes sense, because when we create the sampling distribution, we assume the null hypothesis is true. We look at the variability in random samples selected from the population described by the null hypothesis.

Similarly, if the significance level is 1 percent, then we can expect the sample results to lead us to reject the null hypothesis 1 percent of the time when it is actually true. In other words, about one in 100 data sets would show "rare" results, leading us to reject a true null hypothesis. So the probability of a type I error in this case is 1 percent.

*In general, the probability of a type I error is α.*

## What Is the Probability That We Will Make a Type II Error?

As you have just seen, the probability of a type I error is equal to the significance level, α. The probability of a type II error is much more complicated to calculate, but it is inversely related to the probability of making a type I error: reducing the chance of making a type II error increases the likelihood of a type I error, and vice versa.

## Decreasing the Chance of Type I or Type II Errors

How can we decrease the chance of a type I or type II error? Well, decreasing the chance of a type I error increases the chance of a type II error, so we must weigh the consequences of these errors before deciding how to proceed.

Recall that the probability of committing a type I error is α. When we choose a level of significance (α), we are choosing a benchmark for rejecting the null hypothesis. If the null hypothesis is true, then the probability that we will reject it is α. So the smaller α is, the smaller the probability of a type I error.

It is more complicated to calculate the probability of a type II error. The best way to reduce the probability of a type II error is to *increase the sample size*. But once the sample size is set, larger values of α will decrease the probability of a type II error while increasing the probability of a type I error.

## Check Your Understanding: Controlling Error Probabilities

:::{quiz} A test is conducted at the α = 0.01 significance level. If the null hypothesis is actually true, what is the probability of a type I error?
:hint: The probability of a type I error equals the significance level.
:feedback-0: Correct! P(type I error) = α = 0.01.
:feedback-1: 0.05 would be the answer if α were 0.05—but this test uses α = 0.01.
:feedback-2: The probability of a type I error is exactly the significance level, not its complement.
* *0.01
* 0.05
* 0.99
:::

:::{quiz} A research team is worried about missing a real effect (a type II error). Which action would BEST reduce that risk without raising the chance of a type I error?
:hint: One tool reduces type II errors "for free"; changing α involves a trade-off.
:feedback-0: Correct! Increasing the sample size reduces the probability of a type II error without changing α (the type I error probability).
:feedback-1: Raising α does reduce type II errors, but it directly increases the probability of a type I error.
:feedback-2: Lowering α makes a type II error MORE likely.
* *Increase the sample size
* Increase the significance level α
* Decrease the significance level α
:::

*General guidelines for choosing a level of significance:*

- If the consequences of a type I error are more serious, choose a small level of significance (α).
- If the consequences of a type II error are more serious, choose a larger level of significance (α). But remember that the level of significance is the probability of committing a type I error.
- In general, we choose the largest level of significance that we can tolerate as the chance of making a type I error.

*Note:* it is not always the case that one type of error is worse than the other.
