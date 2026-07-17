# Reading Histograms: Practice and Pitfalls

```{admonition} Learning Objectives
:class: note

- Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
- Summarize and describe the distribution of a quantitative variable in context: a) describe the overall pattern, b) describe striking deviations from the pattern.
```

## Center

The center of the distribution is its *midpoint*—the value that divides the distribution so that approximately half the observations take smaller values, and approximately half the observations take larger values. Note that from looking at the histogram we can get only a rough estimate for the center of the distribution. (More exact ways of finding measures of center will be discussed in the next section.)

Recall our grades example:

```{figure} images/gen/m04-exam-scores-histogram.svg
:alt: The exam grades histogram. The y-axis is labeled count, and the x-axis is labeled score. There is 1 count in the 40-50 score interval, 2 counts in the 50-60 interval, 4 counts in the 60-70 interval, 5 counts in the 70-80 interval, 2 counts in the 80-90 interval, and 1 count in the 90-100 interval.
```

As you can see from the histogram, the center of the grades distribution is roughly 70 (7 students scored below 70, and 8 students scored above 70).

## Spread

The *spread* (also called *variability*) of the distribution can be described by the approximate range covered by the data. From looking at the histogram, we can approximate the smallest observation (*min*), and the largest observation (*max*), and thus approximate the range. (More exact ways of finding measures of spread are discussed in the next section.)

In our example:

| | |
| --- | --- |
| Approximate min: | 45 (the middle of the lowest interval of scores) |
| Approximate max: | 95 (the middle of the highest interval of scores) |
| Approximate range: | 95 − 45 = 50 |

## Outliers

*Outliers* are observations that fall outside the overall pattern. For example, the following histogram represents a distribution that has a highly probable outlier:

```{figure} images/gen/m04-outlier-histogram.svg
:alt: A histogram in which the frequency rises to a peak near 5 and then decreases to zero by about 11. Far to the right, separated from the rest of the data by a gap, a single red bar near 15 stands alone—an outlier.
```

Go back and check the histogram of scores at the top of this page. As you can see, there are no outliers.

::::{admonition} Example: Best Actress Oscar Winners
:class: tip

To provide an example of a histogram applied to actual data, we will look at the ages of Best Actress Oscar winners from 1970 to 2013.

The histogram for the data is shown below.

```{figure} images/gen/m04-oscar-actress-histogram.svg
:alt: A histogram of the ages of Best Actress Oscar winners from 1970 to 2013. Frequencies by five-year age interval are 2 for ages 20-24, 8 for 25-29, 12 for 30-34, 7 for 35-39, 6 for 40-44, 4 for 45-49, none for 50-59, 3 for 60-64, none for 65-69, 1 for 70-74, none for 75-79, and 1 for 80-84. The distribution is skewed right with a long tail toward the older ages.
```

We will now summarize the main features of the distribution of ages as it appears from the histogram:

*Shape:* The distribution of ages is skewed right. We have a concentration of data among the younger ages and a long tail to the right. The vast majority of the "best actress" awards are given to young actresses, with very few awards given to actresses who are older.

*Center:* The data seem to be centered around 34 or 35 years old. Note that this implies that roughly half the awards are given to actresses who are less than 34 years old.

*Spread:* The data range from about 20 to about 80, so the approximate range equals 80 − 20 = 60.

*Outliers:* There seem to be two probable outliers to the far right and possibly three around 62 years old.

You can see how informative it is to know "what to look at" in a histogram. If there is one conclusion that we can make here, it is that Hollywood likes to give Oscars to young actresses.
::::

## Concept Check

Use the Best Actress histogram above to answer the following questions.

:::{quiz} How many of the Best Actress winners were younger than 30 when they won?
:hint: Add the frequencies of the intervals that contain only ages below 30.
:feedback-0: 8 counts only the 25-29 interval; don't forget the two winners aged 20-24.
:feedback-1: Correct! 2 + 8 = 10 winners were in the 20-24 and 25-29 intervals.
:feedback-2: 12 is the count for the 30-34 interval, whose winners were not younger than 30.
* 8
* *10
* 12
:::

:::{quiz} Which description best matches the shape of the distribution of winners' ages?
:hint: Where is the long tail—toward the younger or the older ages?
:feedback-0: A symmetric distribution would have similar tails on both sides; here the right tail is much longer.
:feedback-1: Correct! The data are concentrated at younger ages with a long tail stretching toward the older ages—skewed right.
:feedback-2: Skewed left would mean most winners were old with a tail of unusually young winners.
* Roughly symmetric
* *Skewed right
* Skewed left
:::

:::{quiz} You notice a single observation far from the rest of the data in a histogram. What is the most appropriate next step?
:hint: An outlier is a signal, not necessarily a mistake.
:feedback-0: Deleting data just for being unusual can throw away real (and often interesting) information.
:feedback-1: Correct! Outliers need further investigation—they may be data-entry errors, or genuine unusual observations that deserve attention.
:feedback-2: Ignoring the outlier means possibly missing an error or an important discovery in the data.
* Delete it so it doesn't distort the analysis
* *Investigate it—determine whether it is an error or a genuinely unusual observation
* Ignore it, since one observation can't matter much
:::

## Let's Summarize

- The histogram is a graphical display of the distribution of a quantitative variable. It plots the number (count) of observations that fall in intervals of values.
- When examining the distribution of a quantitative variable, one should describe the overall pattern of the data (shape, center, spread), and any deviations from the pattern (outliers).
- When describing the shape of a distribution, one should consider:
  - Symmetry/skewness of the distribution
  - Peakedness (modality)—the number of peaks (modes) the distribution has.
  - Not all distributions have a simple, recognizable shape.
- Outliers are data points that fall outside the overall pattern of the distribution and need further research before continuing the analysis.
- It is always important to interpret what the features of the distribution (as they appear in the histogram) mean in the context of the data.
