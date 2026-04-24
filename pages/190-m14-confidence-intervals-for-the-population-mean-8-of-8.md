# Confidence Intervals for the Population Mean (8 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## Let's summarize

* When the population is normal and/or the sample is large, a confidence interval for unknown population mean μ when σ is known is:

$\bar{x}\pmz\times\frac{\sigma}{\sqrt{n}}$, where z* is 1.645 for 90% confidence, 2 for 95% confidence, and 2.576 for 99% confidence.

* There is a trade-off between the level of confidence and the precision of the interval estimation. The price we have to pay for more precision is sacrificing level of confidence.

* The general form of confidence intervals is an estimate +/- the margin of error (m). In this case,the estimate=$\bar{x}$ and $m=z\times\frac{\sigma}{\sqrt{n}}$. The confidence interval is therefore centered at the estimate and its width is exactly 2m.

* For a given level of confidence, the width of the interval depends on the sample size. We can therefore do a sample size calculation to figure out what sample size is needed in order to get a confidence interval with a desired margin of error m, and a certain level of confidence (assuming we have some flexibility with the sample size). To do the sample size calculation we use:

$n=\left(\frac{z^{*}\sigma}{m}\right)^{2}$

(and round *up* to the next integer).

* When σ is unknown, we use the sample standard deviation, s, instead, but as a result we also need to use a different set of confidence multipliers (t*) associated with the t distribution. The interval is therefore

$\bar{x}\pmt^{*}\times\frac{s}{\sqrt{n}}$

* These new multipliers have the added complexity that they depend not only on the level of confidence, but also on the sample size. Software is therefore very useful for calculating confidence intervals in this case.

* For large values of n, the t* multipliers are not that different from the z* multipliers, and therefore using the interval formula:

$\bar{x}\pmz^{\times}\times\frac{s}{\sqrt{n}}$

for μ when σ is unknown provides a pretty good approximation.
