# Type I and Type II Errors

```{admonition} Learning Objectives
    - Determine the likelihood of making type I and type II errors, and explain how to reduce them, in context.
```

## What Can Go Wrong: Two Types of Errors

Statistical investigations involve making decisions in the face of uncertainty. So there is always some chance of making a wrong decision. In hypothesis testing, the following decisions can occur:

- If the null hypothesis is true and we do not reject it, it is a *correct decision.*
- If the null hypothesis is false and we reject it, it is a *correct decision.*
- If the null hypothesis is true, but we reject it. This is a *type I* error.
- If the null hypothesis is false, but we fail to reject it. This is a *type II* error.

Type I and type II errors are not caused by mistakes. They are the result of random chance. The *data*provide evidence for a conclusion that is false. It’s no one’s fault!

```{note}
    **Activity**

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example: A Courtroom Analogy for Hypothesis Tests
    Defendants standing trial for a crime are considered innocent until evidence shows they are guilty. It is the job of the prosecution to present evidence that shows the defendant is guilty “beyond a reasonable doubt.” It is the job of the defense to challenge this evidence and establish a reasonable doubt. The jury weighs the evidence and makes a decision.

    When a jury makes a decision, only two verdicts are possible:

    - *Guilty:* The jury concludes that there is enough evidence
    					to convict the defendant. The evidence is so strong that there is not a
    					reasonable doubt of the defendant’s guilt.
    - *Not guilty:* The jury concludes that there is not enough
    					evidence to conclude beyond a reasonable doubt that the person is guilty.

    Notice that a verdict of “not guilty” is not a conclusion that the defendant is innocent. This verdict says only that there is not enough evidence to return a guilty verdict.

    *How is this like a hypothesis test?*

    The null hypothesis, *H**~0~*, in American courtrooms is “the defendant is innocent.” The alternative hypothesis, *H**~a~*, is “the defendant is guilty.” The evidence presented in the case is the data on which the verdict is based. In a courtroom, the defendant is assumed to be innocent until proven guilty. In a hypothesis test, we assume the null hypothesis is true until the dataindicates otherwise.

    The two possible verdicts are similar to the two conclusions that are possible in a hypothesis test.

    *Reject the null hypothesis:*When we reject a null hypothesis, we accept the alternative hypothesis. This is equivalent to a guilty verdict in the courtroom. The evidence is strong enough for the jury to reject the initial assumption of innocence. In a hypothesis test, the data is strong enough for us to reject the assumption that the null hypothesis is true.

    *Fail to reject the null hypothesis:*When we fail to reject the null hypothesis, we are delivering a “not guilty” verdict. The jury concludes that the evidence is not strong enough to reject the assumption of innocence. So the data is too weak to support a guilty verdict. We conclude the data is not strong enough to reject the null hypothesis. In other words, the data is too weak to accept the alternative hypothesis.

    *How does the courtroom analogy relate to Type I and Type II errors?*

    *Type I error:*The evidence leads the jury to convict an innocent person. By analogy, we reject a true null hypothesis and accept a false alternative hypothesis.

    *Type II error:*The evidence leads the jury to declare a defendant not guilty, when he is in fact guilty. By analogy, we fail to reject a null hypothesis that is false. In other words, we do not accept an alternative hypothesis when it is really true.

    It would be nice to know when each of these errors is happening when we make our decision about the null hypothesis, but statistical decisions are based on evidence gathered through sampling, and our sampling evidence will sometimes fool us. As long as we are making a decision, we will never be able to eliminate the potential for these two types of errors. Thus, we need to learn how to adjust to the consequences of making these types of errors.
```

A double-blind experiment is conducted to investigate the side effects of hormone replacement therapy for women with menopausal symptoms. The experiment randomly assigns more than 16,000 American women to either a hormone treatment or a placebo. After five years, the HRT study finds no significant difference in the proportion of women developing breast cancer and heart disease. Researchers decide, based on this finding, to allow the study to continue.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Suppose that at the end of the five-year study described above, a greater proportion of the hormone-treated group have breast cancer and heart disease. This observed difference is statistically significant. Researchers are so alarmed by the results that the experiment is ended early to prevent further harm to the health of the women participating in the hormone group.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

An NBC News/*Wall Street Journal*poll conducted in 2010 determined that 61 percent of Americans did not support the Tea Party movement. In a poll of 1,000 Americans this year, 64 percent say they do not support the Tea Party movement. Has opposition to the Tea Party movement increased since 2010?

We tested the following hypotheses at the 5 percent level of significance:

- *H* *~0~* : The
						proportion of Americans this year who oppose the Tea Party movement is
						0.61.
- *H* *~a~* : The
						proportion of Americans this year who oppose the Tea Party movement is
						greater than 0.61.

The *P* value is .026, so we reject the null hypothesis, *H**~0~* , and accept the alternative hypothesis, *H**~a~*. We conclude that public opposition to the Tea Party movement is greater than 61% this year.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## What is the probability that we will make a Type I error?

If the significance level is 5 percent (α = .05), then 5 percent of the time, we will reject the null hypothesis, even if it is true. Of course we will not know whether the null hypothesis is true. But if it is, the natural variability that we expect in random samples will produce “rare” results 5 percent of the time.

This makes sense, because when we create the sampling distribution, we assume the null hypothesis is true. We look at the variability in random samples selected from the population described by the null hypothesis.

Similarly, if the significance level is 1 percent, then we can expect the sample results to lead us to reject the null hypothesis 1 percent of the time. In other words, about one in 100 data sets would show “rare” results that contrast with the other 99 data sets, leading us to reject the null hypothesis. If the null hypothesis is actually true, then by chance alone, we will reject a true null hypothesis 1 percent of the time. So the probability of a type I error in this case is 1 percent.

In general, the probability of a type I error is α.

## What is the probability that we will make a Type II error?

As you have just seen, the probability of a type I error is equal to the significance level, α. The probability of a type II error is much more complicated to calculate, but it is inversely related to the probability of making a type I error. Thus, reducing the chance of making a type II error causes an increase in the likelihood of a type I error.

## Decreasing the Chance of Type I or Type II Error

How can we decrease the chance of a type I or type II error? Well, decreasing the chance of a type I error increases the chance of a type II error, so we must weigh the consequences of these errors before deciding how to proceed.

Recall that the probability of committing a type I error is α. Why is this? Well, when we choose a level of significance (α), we are choosing a benchmark for rejecting the null hypothesis. If the null hypothesis is true, then the probability that we will reject a true null hypothesis is α. So the smaller α is, the smaller the probability of a type I error there will be.

It is more complicated to calculate the probability of a type II error. The best way to reduce the probability of a type II error is to increase the sample size. But once the sample size is set, larger values of α will decrease the probability of a type II error while increasing the probability of a type I error.

##### 

A double-blind experiment is conducted to investigate the side effects of hormone replacement therapy for women with menopausal symptoms. The experiment randomly assigns more than 16,000 American women to either a hormone treatment or a placebo. After five years, the HRT study finds no significant difference in the proportion of women developing breast cancer and heart disease. Researchers decide, based on this finding, to allow the study to continue. As the null hypothesis was not rejected, there is a chance that the researchers made a type II error.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Suppose that at the end of the five-year study described above, a greater proportion of the hormone-treated group have breast cancer and heart disease. This observed difference is statistically significant. Researchers are so alarmed by the results that the experiment is ended early to prevent further harm to the health of the women participating in the hormone group. Since the null hypothesis was rejected, it is possible researchers made a type I error.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### 

An NBC News/*Wall Street Journal*poll conducted in 2010 determined that 61 percent of Americans did not support the Tea Party movement. In a poll of 1,000 Americans this year, 64 percent say they do not support the Tea Party movement. Has opposition to the Tea Party movement increased since 2010?

We tested the following hypotheses at the 5 percent level of significance:

- *H* *~0~* : The proportion of
								Americans this year who oppose the Tea Party movement is 0.61.
- *H* *~a~* : The proportion of
								Americans this year who oppose the Tea Party movement is greater than
								0.61.

The *P*value is .026, so we reject the null hypothesis, *H**~0~*, and accept the alternative hypothesis, *H**~a~*. We conclude that public opposition to the Tea Party movement is greater than 61% this year. Because the null hypothesis has been rejected, it is possible that the researchers made a type I error.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

*General guidelines for choosing a level of significance:*

- If the consequences of a type I error are more serious, choose a small level
						of significance (α).
- If the consequences of a type II error are more serious, choose a larger
						level of significance (α). But remember that the level of significance is
						the probability of committing a type I error.
- In general, we choose the largest level of significance that we can tolerate
						as the chance of making a type I error.

Note: It is not always the case that one type of error is worse than the other.
