# Confidence Intervals at Other Levels of Confidence

## Other Levels of Confidence

The most commonly used level of confidence is 95%. However, we may wish to increase our level of confidence and produce an interval that is almost certain to contain μ. Specifically, we may want to report an interval for which we are 99% confident—rather than only 95% confident—that it contains the unknown population mean.

Using the same reasoning as in the last comment, in order to create a 99% confidence interval for μ, we should ask: there is a probability of 0.99 that any normal random variable takes values within how many standard deviations of its mean? The precise answer is 2.576, and therefore, a 99% confidence interval for μ is $\bar{x}\pm2.576\cdot\frac{\sigma}{\sqrt{n}}$.

Another commonly used level of confidence is a 90% level of confidence. Since there is a probability of 0.90 that any normal random variable takes values within 1.645 standard deviations of its mean, the 90% confidence interval for μ is $\bar{x}\pm1.645\cdot\frac{\sigma}{\sqrt{n}}$.

:::{admonition} Example: Three Confidence Levels
:class: tip

Let's go back to our first example, the IQ example:

The IQ level of students at a particular university has an unknown mean, μ, and a known standard deviation, $\sigma=15$. A simple random sample of 100 students is found to have a sample mean IQ $\bar{x}=115$. Estimate μ with 90%, 95%, and 99% confidence intervals.

A 90% confidence interval for μ is $115\pm1.645\left(\frac{15}{\sqrt{100}}\right)=115\pm2.5=(112.5,\ 117.5)$.

A 95% confidence interval for μ is $115\pm2\left(\frac{15}{\sqrt{100}}\right)=115\pm3.0=(112,\ 118)$.

A 99% confidence interval for μ is $115\pm2.576\left(\frac{15}{\sqrt{100}}\right)=115\pm4.0=(111,\ 119)$.
:::

Note from the previous example that the more confidence I require, the wider the confidence interval for μ. The 99% confidence interval is wider than the 95% confidence interval, which is wider than the 90% confidence interval:

```{figure} images/gen/m14-ci-widths.svg
:alt: A number line centered at the sample mean of 115 with three nested confidence intervals stacked above it: the 90% interval from 112.5 to 117.5 is the narrowest, the 95% interval from 112 to 118 is wider, and the 99% interval from 111 to 119 is the widest.
```

This is not very surprising, given that in the 99% interval we multiply the standard deviation by 2.576, in the 95% by 2, and in the 90% only by 1.645. Beyond this numerical explanation, there is a very clear intuitive explanation and an important implication of this result.

Let's start with the intuitive explanation. The more certain I want to be that the interval contains the value of μ, the more plausible values the interval needs to include in order to account for that extra certainty. I am 95% certain that the value of μ is one of the values in the interval (112, 118). In order to be 99% certain that one of the values in the interval is the value of μ, I need to include more values, and thus provide a wider confidence interval.

In our example, the *wider* 99% confidence interval (111, 119) gives us a *less precise* estimation of the value of μ than the narrower 90% confidence interval (112.5, 117.5), because the smaller interval "narrows in" on the plausible values of μ.

The important practical implication here is that researchers must decide whether they prefer to state their results with a higher level of confidence or produce a more precise interval. In other words,

*There is a trade-off between the level of confidence and the precision with which the parameter is estimated.*

The price we have to pay for a higher level of confidence is that the unknown population mean will be estimated with less precision (i.e., with a wider confidence interval). If we would like to estimate μ with more precision (i.e., a narrower confidence interval), we will need to sacrifice and report an interval with a lower level of confidence.

## Check Your Understanding: Confidence Level and Interval Width

In a recent study, 1,115 males 25 to 35 years of age were randomly chosen and asked about their exercise habits. Based on the study results, the researchers estimated the mean time that a male 25 to 35 years of age spends exercising with 90%, 95%, and 99% confidence intervals. These were (not necessarily in the same order): (3, 4), (2.5, 4.5), and (2, 5) hours.

:::{quiz} Match each interval with its confidence level.
:hint: Higher confidence requires a wider interval.
:feedback-0: Correct! The narrowest interval, (3, 4), goes with the lowest confidence (90%); the widest, (2, 5), goes with 99%.
:feedback-1: It's the reverse: higher confidence levels demand wider intervals.
:feedback-2: The 95% interval must be between the other two in width: (2.5, 4.5).
* *(3, 4) is 90%; (2.5, 4.5) is 95%; (2, 5) is 99%
* (3, 4) is 99%; (2.5, 4.5) is 95%; (2, 5) is 90%
* (3, 4) is 90%; (2.5, 4.5) is 99%; (2, 5) is 95%
:::

:::{quiz} A researcher says: "I want to keep 95% confidence but get a narrower interval." What is the researcher's main option?
:hint: Look at the formula: the width depends on σ/√n.
:feedback-0: Correct! Increasing the sample size shrinks σ/√n, narrowing the interval without sacrificing confidence.
:feedback-1: Lowering the confidence level narrows the interval, but the researcher wants to keep 95%.
:feedback-2: The population standard deviation is not something the researcher can change.
* *Increase the sample size
* Lower the confidence level to 90%
* Reduce the population standard deviation
:::
