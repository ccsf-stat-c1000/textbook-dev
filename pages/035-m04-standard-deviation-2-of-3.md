# The Standard Deviation Rule: 68-95-99.7

```{admonition} Learning Objectives
:class: note

- Apply the standard deviation rule to the special case of distributions having the "normal" shape.
```

## The Standard Deviation Rule

In the previous section we tried to help you develop better intuition about the concept of standard deviation. The rule that we are about to present, called "The Standard Deviation Rule" (also known as "The Empirical Rule") will hopefully also contribute to building your intuition about this concept.

Consider a symmetric mound-shaped distribution. For distributions having this shape (also known as the *normal* shape), the following rule applies:

*The Standard Deviation Rule:*

- Approximately 68% of the observations fall within 1 standard deviation of the mean.
- Approximately 95% of the observations fall within 2 standard deviations of the mean.
- Approximately 99.7% (or virtually all) of the observations fall within 3 standard deviations of the mean.

The following picture illustrates this rule:

```{figure} images/gen/m04-sd-rule.svg
:alt: A normal curve centered at the mean, with the axis marked at 1, 2, and 3 standard deviations on each side of the mean. Brackets below show that about 68% of observations fall within 1 standard deviation of the mean, about 95% within 2 standard deviations, and about 99.7% within 3 standard deviations.
```

This rule provides another way to interpret the standard deviation of a distribution, and thus also provides a bit more intuition about it.

To see how this rule works in practice, consider the following example:

::::{admonition} Example: Male Height
:class: tip

The following histogram represents height (in inches) of 50 males. Note that the data are roughly normal, so we would like to see how the Standard Deviation Rule works for this example.

```{figure} images/gen/m04-male-height-histogram.svg
:alt: A roughly symmetric, mound-shaped histogram of the heights of 50 males, ranging from 64 to 78 inches with a peak around 70 to 72 inches.
```

Here are the numerical summaries of the distribution. Note that the key players here, the mean and standard deviation, have been highlighted.

| Statistic | Height |
| --- | --- |
| N | 50 |
| **Mean** | **70.58** |
| **StDev** | **2.858** |
| min | 64 |
| Q1 | 68 |
| Median | 70.5 |
| Q3 | 72 |
| Max | 77 |

To see how well the Standard Deviation Rule works for this case, we find the intervals within 1, 2, and 3 standard deviations of the mean:

- within 1 SD: 70.58 ± 2.86, or (67.7, 73.4)
- within 2 SD: 70.58 ± 5.72, or (64.9, 76.3)
- within 3 SD: 70.58 ± 8.57, or (62.0, 79.2)

When we count what percentage of the 50 observations actually fall in each of these intervals, the results come out very close to the 68%, 95%, and 99.7% that the rule predicts. The Standard Deviation Rule works *very well* in this example.
::::

## Check Your Understanding: The 68-95-99.7 Rule

:::{quiz} Scores on a standardized test are normally shaped with mean 500 and standard deviation 100. Approximately what percentage of test takers score between 400 and 600?
:hint: How many standard deviations from the mean are 400 and 600?
:feedback-0: Correct! 400 and 600 are each 1 SD from the mean, and about 68% of observations fall within 1 SD.
:feedback-1: 95% corresponds to within 2 SDs of the mean, i.e., between 300 and 700.
:feedback-2: 99.7% corresponds to within 3 SDs of the mean, i.e., between 200 and 800.
* *About 68%
* About 95%
* About 99.7%
:::

:::{quiz} For the same test (mean 500, SD 100), approximately what percentage of test takers score above 700?
:hint: 700 is 2 SDs above the mean. About 95% are within 2 SDs, so 5% are outside—split between the two tails.
:feedback-0: 5% is the total percentage outside 2 SDs on both sides; only half of that is above 700.
:feedback-1: Correct! About 5% fall outside (300, 700), and by symmetry half of them, about 2.5%, score above 700.
:feedback-2: 32% is the percentage falling more than 1 SD from the mean (outside 400 to 600), not more than 2 SDs above it.
* About 5%
* *About 2.5%
* About 32%
:::
