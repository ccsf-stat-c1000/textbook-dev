# Parameters vs. Statistics

To better understand the relationship between sample and population, let's consider the two examples that were mentioned in the introduction.

:::{admonition} Example 1: Blood Type
:class: tip

In the probability section, we presented the distribution of blood types in the entire U.S. {term}`population`. Assume now that we take a {term}`sample` of 500 people in the United States, record their blood type, and display the sample results. And then we take yet another sample of 500:

| Blood type | Population | Sample 1 (n = 500) | Sample 2 (n = 500) |
| --- | --- | --- | --- |
| O | 44% | 221 (44.2%) | 213 (42.6%) |
| A | 42% | 198 (39.6%) | 216 (43.2%) |
| B | 10% | 59 (11.8%) | 39 (7.8%) |
| AB | 4% | 22 (4.4%) | 32 (6.4%) |

Note that the percentages (or proportions) that we got in each sample are slightly different from the population percentages. This is really not surprising. Since we took a sample of just 500, we cannot expect that our sample will behave exactly like the population, but if the sample is random (as it was), we expect to get results which are not that far from the population (as we did). Each sample is also different from the other. This very intuitive idea, that sample results change from sample to sample, is called *sampling variability.*
:::

Let's look at another example:

:::{admonition} Example 2: Heights of Adult Males
:class: tip

Heights among the population of all adult males follow a normal distribution with a mean $\mu=69$ inches and a standard deviation $\sigma=2.8$ inches.

A sample of 200 males was chosen, and their heights were recorded. The sample histogram resembles the normal distribution, but is not as smooth, and the sample mean is $\bar{x}=68.7$ inches with sample standard deviation s = 2.95 inches—slightly different from the population values.

A second sample of 200 males gives a sample mean of $\bar{x}=69.065$ inches and a sample standard deviation of s = 2.659 inches.

Again, as in Example 1, we see the idea of *sampling variability.* The sample results are pretty close to the population, and different from the results we got in the first sample.
:::

In both the examples, we have numbers that describe the population, and numbers that describe the sample. In Example 1, the number 42% is the population proportion of blood type A, and 39.6% is the sample proportion (in sample 1) of blood type A. In Example 2, 69 and 2.8 are the population mean and standard deviation, and (in sample 1) 68.7 and 2.95 are the sample mean and standard deviation.

```{admonition} Definition: Parameter and Statistic
:class: note

A {term}`parameter` is a number that describes the population; a {term}`statistic` is a number that is computed from the sample.
```

In Example 1: 42% is a parameter and 39.6% is a statistic.

In Example 2: 69 and 2.8 are parameters, and 68.7 and 2.95 are statistics.

In this course, as in the examples above, we focus on the following parameters and statistics:

- population proportion and sample proportion
- population mean and sample mean
- population standard deviation and sample standard deviation

The following table summarizes the three pairs, and gives the notation:

| | (Population) Parameter | (Sample) Statistic |
| --- | --- | --- |
| *Proportion* | $p$ | $\hat{p}$ |
| {term}`Mean <mean>` | $\mu$ | $\bar{x}$ |
| {term}`Standard Deviation <standard deviation>` | $\sigma$ | $s$ |

The only new notation here is p for population proportion (p = 0.42 for type A in Example 1), and $\hat{p}$ ("p-hat") for sample proportion ($\hat{p}$ = 0.396 for type A in Example 1).

```{admonition} Comments
:class: important

1. Parameters are usually unknown, because it is impractical or impossible to know exactly what values a variable takes for every member of the population.
2. Statistics are computed from the sample, and vary from sample to sample due to *sampling variability*.
```

In the last part of the course, statistical inference, we will learn how to use a statistic to draw conclusions about an unknown parameter, either by estimating it or by deciding whether it is reasonable to conclude that the parameter equals a proposed value. In this module, we'll learn about the behavior of the statistics assuming that we know the parameters. So, for example, if we know that the population proportion of blood type A in the population is 0.42, and we take a random sample of size 500, what do we expect the sample proportion ($\hat{p}$) to be?

Here are some more examples:

:::{admonition} Example: Picking Numbers
:class: tip

If students picked numbers completely at random from the numbers 1 to 20, the proportion of times that the number 7 would be picked is 0.05. When 15 students picked a number "at random" from 1 to 20, 3 of them picked the number 7. Identify the parameter and accompanying statistic in this situation.

The parameter is the population proportion of random selections resulting in the number 7, which is p = 0.05. The accompanying statistic is the sample proportion of selections resulting in the number 7, which is $\hat{p}=3/15=0.20$.
:::

:::{admonition} Example: Pregnancy Length
:class: tip

The length of human pregnancies has a mean of 266 days and a standard deviation of 16 days. A random sample of 9 pregnant women was observed to have a mean pregnancy length of 270 days, with a standard deviation of 14 days. Identify the parameters and accompanying statistics in this situation.

The parameters are population mean $\mu=266$ and population standard deviation $\sigma=16$. The accompanying statistics are sample mean $\bar{x}=270$ and sample standard deviation $s=14$.
:::

## Check Your Understanding: Parameters and Statistics

:::{quiz} A polling organization reports that 58% of the 1,024 adults it surveyed support a proposal, while government records show that 51% of all registered voters voted in the last election. Which number is a statistic and which is a parameter?
:hint: Which number describes a sample, and which describes an entire population?
:feedback-0: Correct! The 58% comes from a sample (a statistic); the 51% describes the entire population of registered voters (a parameter).
:feedback-1: It's the reverse: the survey result comes from a sample, while the records cover the whole population.
:feedback-2: One of each: survey → statistic, complete records → parameter.
* *58% is a statistic; 51% is a parameter
* 58% is a parameter; 51% is a statistic
* Both are parameters
:::

:::{quiz} Which symbol denotes the sample proportion?
:hint: Sample statistics wear "hats" or bars.
:feedback-0: Correct! $\hat{p}$ (p-hat) is the sample proportion; p is the population proportion.
:feedback-1: p (no hat) denotes the population proportion, a parameter.
:feedback-2: $\bar{x}$ denotes the sample mean, not a proportion.
* *$\hat{p}$
* p
* $\bar{x}$
:::
