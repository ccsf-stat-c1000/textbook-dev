# Summary (Inference)

This summary provides a quick recap of the big ideas you've learned in the inference section (without going into any of the technical details). Therefore, this summary does not provide complete coverage of the material and thus should be used only as a checklist or a quick review of the "big ideas" before an exam.

- In the Inference unit, which is the last step in the "Big Picture," we use the evidence provided by the data to infer about the relevant population.
- The inference could be about the *value of unknown parameters* in our population (mean, proportion, difference between means, etc.) or about the existence of a certain *relationship between two variables* in the population.
- We discussed 3 forms of inference: point estimation, interval estimation and hypotheses testing.

## Point Estimation

1. *Idea:* estimating an unknown parameter with a single value (that was obtained from the observed data).
2. We typically estimate: Note that the last two parameters (σ and $\sigma^{2}$ ) are not covered in this course.
  - the population mean *μ* by the sample mean $\bar{x}$
  - the population proportion *p* by the sample proportion $\hat{p}$
  - the population standard deviation *σ* and the population variance $\sigma^{2}$ by the sample standard deviation *s* and the sample variance $s^{2}$
3. $\bar{x}$, $\hat{p}$, s, and $s^{2}$ are unbiased estimators for μ, p, σ, and $\sigma^{2}$, respectively. Their precision increases with the sample size.

## Interval Estimation

1. *Idea:* Estimating an unknown parameter with an interval of plausible values and attaching to the interval our level of confidence that it indeed covers the true value of the parameter. Such an interval is therefore called a confidence interval.
2. The general form of confidence intervals is: $point estimate\pmmargin of error$ where the margin of error represents the maximum estimation error for a given level of confidence, and is the product of the confidence multiplier and the standard deviation (or standard error) of the point estimator.
3. Since the margin of error (and therefore the width of the confidence interval) increases with the level of confidence, there is a trade-off between the level of confidence and the precision of the interval estimation. The price you have to pay for more confidence is less precision (a wider confidence interval) and vice versa.
4. A way to get better precision for a given level of confidence is to increase the sample size. Sample size calculations can be carried out in order to determine the sample size needed for a desired margin of error at a certain level of confidence. We should keep in mind, though, that in practice, larger sample sizes are not always available.
5. For the confidence interval for the population mean, μ, we distinguished between: For large sample sizes, though, and for a given level of confidence, z* is approximately equal to t*. In either case, we can safely use the confidence interval as long as the population is large and/or the sample size is large (> 30).
  - the case where the population standard deviation *σ is known* (in which case we use the z* confidence multipliers), and
  - the case where *σ is unknown* and is replaced by the sample standard deviation S (in which case we use the t* confidence multipliers, and rely on software to do the calculations).
6. The confidence interval for the population proportion p is the primary statistical method used in the analysis of polls, and can be safely used as long as $n⋅\hat{p}\geq10$ and $n⋅\left(1−\hat{p}\right)\geq10$.

## Hypothesis Testing

1. *Idea:* Unlike point and interval estimation, in which the goal is estimating an unknown parameter, in hypothesis testing we are assessing the evidence provided by the data in favor or against some claim about the population.
2. In practice, we have two competing hypotheses, H~o~, which is challenged by H~a~, and we are assessing whether or not the data provide evidence (beyond a reasonable doubt) that we can reject H~o~ in favor of H~a~. If they do, we say that the results are significant; otherwise, if H~o~ cannot be rejected, we say that the results are not significant.
3. H~o~ and H~a~ are two claims about the population. In the one variable case, these claims are about the value of a parameter in the population. In inference about relationships, H~o~ and H~a~ are about the existence/nonexistence of a certain relationship between the two variables. Recall that in case C→Q the existence/nonexistence of the relationship is stated in with μ~1~ - μ~2~, μ~d~, or μ~1~, μ~2~, μ~3~, ... , μ~k~. In case C→C and Q→Q, the relationship is stated in words.
4. After the hypotheses have been formulated, data are collected, and conditions for use are checked, the evidence in the data is assessed by finding the p-value of the test, the probability of getting data like those observed (or even more extreme) if H~o~ were true. If the p-value is small (smaller than some cut-off called the significance level, typically set at .05), meaning that it would be unlikely to get data like those observed if H~o~ were true, we reject H~o~ in favor of H~a~. Otherwise, if the p-value > 0.05, we cannot reject H~o~. Note that 0.05 represents our "reasonable doubt." The p-value can be viewed as a measure of the evidence in the data against H~o~, where the smaller the p-value, the larger the evidence against H~o~.
5. In practice, to find the p-value we use the test statistic, a summary of the data which is some measure of "how far" or "how different" the observed data are from what is claimed in H~o~. The p-value of a test is the probability of getting a test statistic (based on the data) like that observed (or even more extreme), if H~o~ were true. The p-value is therefore calculated using the sampling distribution of the test statistic when H~o~ is true ( called the null distribution).
6. Conclusions are then based on the p-value, and should always be stated in context.
