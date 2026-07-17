# The Sample Mean: Center, Spread, and Shape

```{admonition} Learning Objectives
:class: note

- Apply the sampling distribution of the sample mean as summarized by the Central Limit Theorem (when appropriate). In particular, be able to identify unusual samples from a given population.
```

So far, we've discussed the behavior of the statistic $\hat{p}$, the sample proportion, relative to the parameter p, the population proportion (when the variable of interest is categorical). We are now moving on to explore the behavior of the statistic $\bar{X}$, the sample mean, relative to the parameter $\mu$, the population mean (when the variable of interest is quantitative).

## Behavior of Sample Mean (x-bar)

:::{admonition} Example: Birth Weights
:class: tip

Birth weights are recorded for all babies in a town. The mean birth weight is 3,500 grams, µ = 3,500 g. If we collect many random samples of 9 babies at a time, how do you think sample means will behave?

Here again, we are working with a random variable, since random samples will have means that vary unpredictably in the short run but exhibit patterns in the long run.

Based on our intuition and what we have learned about the behavior of sample proportions, we might expect the following about the distribution of sample means:

*Center*: Some sample means will be on the low side—say 3,000 grams or so—while others will be on the high side—say 4,000 grams or so. In repeated sampling, we might expect that the random samples will average out to the underlying population mean of 3,500 g. In other words, the mean of the sample means will be µ, just as the mean of sample proportions was p.

*Spread*: For large samples, we might expect that sample means will not stray too far from the population mean of 3,500. Sample means lower than 3,000 or higher than 4,000 might be surprising. For smaller samples, we would be less surprised by sample means that varied quite a bit from 3,500. In other words, we might expect greater variability in sample means for smaller samples. So sample size will again play a role in the spread of the distribution of sample means, as we observed for sample proportions.

*Shape*: Sample means closest to 3,500 will be the most common, with sample means far from 3,500 in either direction progressively less likely. In other words, the shape of the distribution of sample means should bulge in the middle and taper at the ends with a shape that is somewhat normal. This, again, is what we saw when we looked at the sample proportions.
:::

## Comment

The *distribution* of the values of the sample mean ($\bar{x}$) in repeated *samples* is called the *sampling distribution of* $\bar{x}$.

```{note} Video

[Behavior of Sample Mean 1](https://www.youtube.com/watch?v=fqOOownnkA4)
```

## Concept Check

:::{quiz} Every day, a quality inspector randomly samples 16 boxes of cereal from a filling machine and computes the sample mean weight. Over many days, around what value will these sample means center, if the machine fills boxes with mean μ = 500 grams?
:hint: The sampling distribution of the sample mean is centered at μ.
:feedback-0: Correct! The sample means average out to the population mean, 500 grams.
:feedback-1: Individual boxes vary, but the CENTER of the sample means is exactly μ = 500.
* *500 grams
* Slightly below 500 grams, since averages lose information
:::

:::{quiz} The inspector considers switching from samples of 16 boxes to samples of 64 boxes. How would this change the sampling distribution of the sample mean?
:hint: Larger samples produce sample means that hug the population mean more tightly.
:feedback-0: Correct! The center stays at μ, but the spread of the sample means shrinks—larger samples give more precise estimates.
:feedback-1: The center does not move with sample size; it is always μ for random samples.
:feedback-2: Larger samples REDUCE the variability of the sample mean.
* *Same center, smaller spread
* The center would shift upward
* Same center, larger spread
:::

:::{quiz} A single random sample of 9 babies has a mean birth weight of 3,400 grams, not 3,500. Does this contradict the claim that the sampling distribution is centered at 3,500?
:hint: Individual sample means vary; the center describes the long-run average of many sample means.
:feedback-0: Correct! Sampling variability means individual sample means differ from μ; "centered at 3,500" describes the average over many repeated samples.
:feedback-1: One sample below the mean is entirely expected—about half of all sample means fall below μ.
* *No—individual sample means vary around 3,500 due to sampling variability
* Yes—the sample mean should equal 3,500 every time
:::
