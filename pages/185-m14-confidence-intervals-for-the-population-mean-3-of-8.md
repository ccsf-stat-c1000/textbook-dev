# Confidence Intervals for the Population Mean (3 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## Other Levels of Confidence

The most commonly used level of confidence is 95%. However, we may wish to increase our level of confidence and produce an interval that is almost certain to contain μ. Specifically, we may want to report an interval for which we are 99% confident—rather than only 95% confident—that it contains the unknown population mean.

Using the same reasoning as in the last comment, in order to create a 99% confidence interval for μ, we should ask: There is a probability of 0.99 that any normal random variable takes values within how many standard deviations of its mean? The precise answer is 2.576, and therefore, a 99% confidence interval for μ is $\bar{x}\pm2.576*\frac{\sigma}{\sqrt{n}}$.

Another commonly used level of confidence is a 90% level of confidence. Since there is a probability of 0.90 that any normal random variable takes values within 1.645 standard deviations of its mean, the 90% confidence interval for μ is $\bar{x}\pm1.645*\frac{\sigma}{\sqrt{n}}$.

```{admonition} Example
    Let's go back to our first example, the IQ example:

    The IQ level of students at a particular university has an unknown mean, μ, and a known standard deviation, $\sigma=15$. A simple random sample of 100 students is found to have a sample mean IQ, $\bar{x}=115$. Estimate μ with 90%, 95%, and 99% confidence intervals.

    A 90% confidence interval for μ is $\bar{x}\pm1.645\frac{\sigma}{\sqrt{n}}=115\pm1.645\left(\frac{15}{\sqrt{100}}\right)=115\pm2.5=\left(112.5, 117.5\right)$.

    A 95% confidence interval for μ is $\bar{x}\pm2\frac{\sigma}{\sqrt{n}}=115\pm2\left(\frac{15}{\sqrt{100}}\right)=115\pm3.0=\left(112, 118\right)$.

    A 99% confidence interval for μ is $\bar{x}\pm2.576\frac{\sigma}{\sqrt{n}}=115\pm2.576\left(\frac{15}{\sqrt{100}}\right)=115\pm4.0=\left(111, 119\right)$.
```

The purpose of this next activity is to give you guided practice at calculating and interpreting confidence intervals, and drawing conclusions from them.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

Note from the previous example and the previous "Did I Get This?" activity, that the more confidence I require, the wider the confidence interval for μ (pronounced and sometimes noted as "mu"). The 99% confidence interval is wider than the 95% confidence interval, which is wider than the 90% confidence interval.

```{figure} images/image058.gif
:alt: A number line illustrating confidence intervals for μ. x-bar is marked at 115. The interval 112.5 and 117.5 is the 90% confidence interval. Enclosing this interval is the interval 112 and 118, which is the 95% confidence interval. Even larger is the 99% confidence interval, ranging from 111 to 119.

A number line illustrating confidence intervals for μ. x-bar is marked at 115. The interval 112.5 and 117.5 is the 90% confidence interval. Enclosing this interval is the interval 112 and 118, which is the 95% confidence interval. Even larger is the 99% confidence interval, ranging from 111 to 119.
```

This is not very surprising, given that in the 99% interval we multiply the standard deviation by 2.576, in the 95% by 2, and in the 90% only by 1.645. Beyond this numerical explanation, there is a very clear intuitive explanation and an important implication of this result.

Let's start with the intuitive explanation. The more certain I want to be that the interval contains the value of μ, the more plausible values the interval needs to include in order to account for that extra certainty. I am 95% certain that the value of μ is one of the values in the interval (112,118). In order to be 99% certain that one of the values in the interval is the value of μ, I need to include more values, and thus provide a wider confidence interval.

```{note}
    **Learn By Doing**

    Visualizing the Relationship between Confidence and Width

    *(Interactive activity — available in the OLI platform)*
```

In our example, the *wider* 99% confidence interval (111, 119) gives us a *less precise* estimation about the value of μ than the narrower 90% confidence interval (112.5, 117.5), because the smaller interval "narrows in" on the plausible values of μ.

The important practical implication here is that researchers must decide whether they prefer to state their results with a higher level of confidence or produce a more precise interval. In other words,

*There is a trade-off between the level of confidence and the precision with which the parameter is estimated*.

The price we have to pay for a higher level of confidence is that the unknown population mean will be estimated with less precision (i.e., with a wider confidence interval). If we would like to estimate μ with more precision (i.e., a narrower confidence interval), we will need to sacrifice and report an interval with a lower level of confidence.

##### Did I Get This?

In a recent study, 1,115 males 25 to 35 years of age were randomly chosen and asked about their exercise habits. Based on the study results, the researchers estimated the mean time that a male 25 to 35 years of age spends exercising with 90%, 95%, and 99% confidence intervals. These were (not necessarily in the same order):

```{figure} images/_u5_m1_dig3a.gif
:alt: Three number lines illustrating three confidence intervals. The first is shows an interval of (3,4). The second, an interval of (2.5, 4.5), and the third, (2,5).

Three number lines illustrating three confidence intervals. The first is shows an interval of (3,4). The second, an interval of (2.5, 4.5), and the third, (2,5).
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on to the next page. If not yet, then click the link below for some additional practice.

```{note}
    **Did I Get This?**

    Confidence Intervals for the Population Mean (extra problems)

    *(Interactive activity — available in the OLI platform)*
```
