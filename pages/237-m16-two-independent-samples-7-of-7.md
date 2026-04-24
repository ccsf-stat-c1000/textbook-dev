# Two Independent Samples (7 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Comment

As we've seen in previous tests, as well as in the two-samples case, the 95% confidence interval for $\mu_{1}−\mu_{2}$ can be used for testing in the two-sided case ($H_{o}:\mu_{1}−\mu_{2}=0$ vs. $H_{a}:\mu_{1}−\mu_{2}\neq0$ ):

If the null value, 0, falls outside the confidence interval, H~o~ is rejected

If the null value, 0, falls inside the confidence interval, H~o~ is not rejected

```{admonition} Example
    Let's go back to our leading example of the looks vs. personality score where we had a two-sided test.

    RStatCrunchMinitabExcel 2007Excel 2003TI CalculatorTip: Alternative versions are available, click the arrow to switch. 

    Excel told us that the 95% confidence interval is (-3.69590,
                                    -1.49625), and that the p-value is 0.000.

    Excel told us that the 95% confidence interval is (-3.69590,
                                    -1.49625), and that the p-value is 0.000.

    We used the fact that the p-value is so small to conclude that Ho can be rejected. We can also use the confidence interval to reach the same conclusion since 0 falls outside the confidence interval. In other words, since 0 is not a plausible value for $\mu_{1}−\mu_{2}$ we can reject H~o~, which claims that $\mu_{1}−\mu_{2}=0$ .
```

```{note}
    **Learn By Doing**

    Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

Below you'll find three sample outputs of the two-sided two-sample t-test:

```{figure} images/image157.gif
:alt: H_0: μ_1 - μ_2 = 0 vs. H_a: μ_1 - μ_2 ≠ 0

H_0: μ_1 - μ_2 = 0 vs. H_a: μ_1 - μ_2 ≠ 0
```

However, only one of the outputs could be correct (the other two contain an inconsistency). Your task is to decide which of the following outputs is the correct one (*Hint:* No calculations are necessary in order to answer this question. Instead pay attention to the p-value and confidence interval).

- *Output A:*
  - p-value: 0.289
  - 95% Confidence Interval: (-5.93090, -1.78572)

- *Output B:*
  - p-value: 0.003
  - 95% Confidence Interval: (-13.97384, 2.89733)

- *Output C:*
  - p-value: 0.223
  - 95% Confidence Interval: (-9.31432, 2.20505)

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Let's Summarize

We have completed our discussion of the two-sample t-test for comparing two populations’ means when the samples are independent. Let’s summarize what we have learned.

- The two sample t-test is used for comparing the means of a quantitative variables (Y) in two populations (which we initially called sub-populations).
- Our goal is comparing μ ~1~ and μ ~2~ (which in practice is done by making inference on the difference μ ~1~ - μ ~2~ ). The null hypotheses is and the alternative hypothesis is one of the following (depending on the context of the problem):
  - Ho: μ ~1~ - μ ~2~ = 0
  - Ha: μ ~1~ - μ ~2~ < 0
  - Ha: μ ~1~ - μ ~2~ > 0
  - Ha: μ ~1~ - μ ~2~ ≠ 0
- The two-sample t-test can be safely used when the samples are independent and at least one of the following two conditions hold: When the sample sizes are not large (and we therefore need to check the normality of Y in both population), what we do in practice is look at the histograms of the two samples and make sure that there are no signs of non-normality such as extreme skewedness and/or outliers.
  - The variable Y is known to have a normal distribution in both populations
  - The two sample sizes are large.
- The test statistic is as follows and has a t distribution when the null hypothesis is true:
- P-values are obtained from the output, and conclusions are drawn as usual, comparing the p-value to the significance level alpha.
- If H ~o~ is rejected, a 95% confidence interval for μ ~1~ - μ ~2~ can be very insightful and can also be used for the two-sided test.

## Section Questions

```{note}
    **My Response**

    About Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```
