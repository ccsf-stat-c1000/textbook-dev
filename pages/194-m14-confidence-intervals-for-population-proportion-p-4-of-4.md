# Confidence Intervals for a Proportion: Conditions and Summary

```{admonition} Learning Objectives
:class: note

- Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
- Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## When Is It Safe to Use These Methods?

As we mentioned before, one of the most important things to learn with any inference method is the conditions under which it is safe to use it.

As we did for the mean, the assumption we made in order to develop the methods in this unit was that the sampling distribution of the sample proportion, $\hat{p}$, is roughly normal. Recall from the Probability unit that the conditions under which this happens are that $np\geq10$ and $n(1-p)\geq10$. Since p is unknown, we will replace it with its estimate, the sample proportion, and set

$$n\hat{p}\geq10 \quad \text{and} \quad n(1-\hat{p})\geq10$$

to be the conditions under which it is safe to use the methods we developed in this section.

## Let's Summarize

- In general, a confidence interval for the unknown population proportion (p) is $\hat{p} \pm z^{*}\cdot\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$, where z\* is 1.645 for 90% confidence, 2 for 95% confidence, and 2.576 for 99% confidence.
- To obtain a desired margin of error (m) in a confidence interval for an unknown population proportion, a conservative sample size is $n=\frac{1}{m^{2}}$.
- The margin of error of a poll is determined (conservatively) by $\frac{1}{\sqrt{n}}$.
- The methods developed in this unit are safe to use as long as $n\hat{p}\geq10$ and $n(1-\hat{p})\geq10$.

## Concept Check

:::{quiz} A quality engineer samples 40 parts and finds 3 defective (p-hat = 0.075). Is it safe to construct the usual z confidence interval for the proportion of defective parts?
:hint: Check n·p-hat and n·(1 − p-hat).
:feedback-0: Correct! n·p-hat = 40(0.075) = 3, which is far below 10—the normality condition fails, so the usual interval is unreliable.
:feedback-1: n·(1 − p-hat) = 37 is fine, but BOTH conditions must hold, and n·p-hat = 3 fails.
* *No—n·p-hat = 3 is less than 10
* Yes—both conditions are met
:::

:::{quiz} A survey of 1,200 randomly selected voters finds 45% support a measure. Is it safe to use the z interval, and what is the approximate 95% margin of error?
:hint: Check the conditions (540 and 660 both ≥ 10), and use m ≈ 1/√n or the exact formula.
:feedback-0: Correct! Conditions easily hold, and m ≈ 1/√1200 ≈ 0.029, or about 3%.
:feedback-1: The conditions hold comfortably: n·p-hat = 540 and n·(1 − p-hat) = 660.
:feedback-2: The margin of error is roughly 1/√n ≈ 0.029, not 0.45.
* *Yes—and the margin of error is about 3 percentage points
* No—the conditions are not met
* Yes—and the margin of error is about 45%
:::
