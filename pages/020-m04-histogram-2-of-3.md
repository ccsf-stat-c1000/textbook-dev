# Histogram (2 of 3)

```{admonition} Learning Objectives
:class: note

- Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
- Summarize and describe the distribution of a quantitative variable in context: a) describe the overall pattern, b) describe striking deviations from the pattern.
```

## Interpreting the Histogram

Once the distribution has been displayed graphically, we can describe the overall pattern of the distribution and mention any striking deviations from that pattern. More specifically, we should consider the following features of the distribution:

```{figure} images/gen/m04-describe-distribution.svg
:alt: Describing a distribution involves two parts. The overall pattern of the distribution is described by its shape, center, and spread. Striking deviations from the pattern are described by outliers.
```

We will get a sense of the overall pattern of the data from the histogram's center, spread and shape, while outliers will highlight deviations from that pattern.

## Shape

When describing the shape of a distribution, we should consider:

1. *Symmetry/skewness* of the distribution.
2. *Peakedness (modality)*—the number of peaks (modes) the distribution has.

We distinguish between:

## Symmetric Distributions

```{figure} images/gen/m04-shape-unimodal.svg
:alt: A symmetric, single-peaked (unimodal) histogram. The bars start low on the left, rise steadily to a single peak near the value 10 at the center, and then fall away symmetrically back down to nearly zero on the right.
```

```{figure} images/gen/m04-shape-bimodal.svg
:alt: A symmetric, double-peaked (bimodal) histogram. The bars rise to a first peak near the value 10, dip down in the middle, rise again to a second peak near the value 20, and then fall back down.
```

```{figure} images/gen/m04-shape-uniform.svg
:alt: A symmetric, uniform histogram. Across the entire range of values the bars are all roughly the same height, with no peak.
```

Note that all three distributions are symmetric, but are different in their modality (peakedness). The first distribution is *unimodal*—it has one mode (roughly at 10) around which the observations are concentrated. The second distribution is *bimodal*—it has two modes (roughly at 10 and 20) around which the observations are concentrated. The third distribution is kind of flat, or *uniform*. The distribution has no modes, or no value around which the observations are concentrated. Rather, we see that the observations are roughly uniformly distributed among the different values.

## Skewed Right Distributions

```{figure} images/gen/m04-shape-skewed-right.svg
:alt: A skewed-right histogram. The bars rise quickly to a peak near the left side of the display and then decrease slowly, forming a long right tail of larger and larger values with smaller and smaller frequencies.
```

A distribution is called *skewed right* if, as in the histogram above, the right tail (larger values) is much longer than the left tail (small values). Note that in a skewed right distribution, the bulk of the observations are small/medium, with a few observations that are much larger than the rest. An example of a real-life variable that has a skewed right distribution is salary. Most people earn in the low/medium range of salaries, with a few exceptions (CEOs, professional athletes etc.) that are distributed along a large range (long "tail") of higher values.

## Skewed Left Distributions

```{figure} images/gen/m04-shape-skewed-left.svg
:alt: A skewed-left histogram. The bars rise slowly from the left, forming a long left tail, reach a peak near the right side of the display, and then drop off quickly.
```

A distribution is called *skewed left* if, as in the histogram above, the left tail (smaller values) is much longer than the right tail (larger values). Note that in a skewed left distribution, the bulk of the observations are medium/large, with a few observations that are much smaller than the rest. An example of a real life variable that has a skewed left distribution is age of death from natural causes (heart disease, cancer etc.). Most such deaths happen at older ages, with fewer cases happening at younger ages.

*Comments:*

1. Note that skewed distributions can also be bimodal. Here is an example. A medium size neighborhood 24-hour convenience store collected data from 537 customers on the amount of money spent in a single visit to the store. The following histogram displays the data. Note that the overall shape of the distribution is skewed to the right with a clear mode around \$25. In addition it has another (smaller) "peak" (mode) around \$50-55. The majority of the customers spend around \$25 but there is a cluster of customers who enter the store and spend around \$50-55.

   ```{figure} images/gen/m04-store-spending-histogram.svg
   :alt: A histogram of the amount spent per visit by 537 customers. The distribution is skewed to the right with a main peak around 25 dollars and a smaller secondary peak around 50 to 55 dollars, followed by a long right tail out to 100 dollars.
   ```

2. If a distribution has more than two modes, we say that the distribution is *multimodal*.

Recall our grades example:

```{figure} images/gen/m04-exam-scores-histogram.svg
:alt: The histogram of the 15 exam grades from earlier, with bars of heights 1, 2, 4, 5, 2, and 1 across the intervals from 40 to 100.
```

As you can see from the histogram, the grades distribution is roughly symmetric.

## Concept Check

:::{quiz} Household income in a country typically has a few households with extremely high incomes, while most households earn small or moderate amounts. What shape would you expect the distribution of household income to have?
:hint: Where is the long tail—toward the small values or the large values?
:feedback-0: A symmetric distribution would require very low incomes to mirror the very high ones.
:feedback-1: Correct! The bulk of households have small/medium incomes and a few have much larger incomes, forming a long right tail.
:feedback-2: Skewed left would mean a few households earn far less than a large majority of high earners—the opposite of reality.
* Symmetric
* *Skewed right
* Skewed left
:::

:::{quiz} Scores on a very easy quiz (where most students score high, but a few score very low) would form a distribution that is:
:hint: The unusual values here are the low scores.
:feedback-0: Correct! Most observations are large, with a long tail stretching toward the small values—skewed left.
:feedback-1: Skewed right would mean most students scored low with a few high scores—that describes a hard quiz.
:feedback-2: With most scores bunched at the top and a tail of low scores, the distribution is not symmetric.
* *Skewed left
* Skewed right
* Symmetric
:::
