# Boxplot (2 of 3)

```{admonition} Learning Objectives
:class: note

- Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
```

Now that you understand what each of the five numbers means, you can appreciate how much information about the distribution is packed into the five-number summary. All this information can also be represented visually by using the boxplot.

## The Boxplot

The boxplot graphically represents the distribution of a quantitative variable by visually displaying the five-number summary and any observation that was classified as a suspected outlier using the 1.5(IQR) criterion.

There are several ways to plot the whiskers on a boxplot. One convention is to plot whiskers down to the minimum and up to the maximum value. We use the 1.5(IQR) criterion, also known as the Tukey method, for plotting whiskers. First, calculate the IQR, the difference between the 75th and 25th percentiles (or Q3 − Q1). Multiply the IQR by 1.5. Add this value to the 75th percentile. If the value is greater than (or equal to) the maximum value in the dataset, draw the upper whisker to the maximum value. Otherwise, stop the whisker at the largest value that is less than Q3 + 1.5 × IQR. Plot any values that are greater than this as individual points that are outliers. Similarly, subtract 1.5 × IQR from the 25th percentile. If this value is smaller than the minimum value in the dataset, draw the lower whisker to the minimum value. Otherwise, stop the whisker at the lowest value that is greater than Q1 − 1.5 × IQR. Plot any values that are smaller than this as individual points that are outliers.

Using the Best Actress dataset, here is how we determine where to draw the whiskers:

- Q3 = 42
- Q1 = 30.5
- IQR: 42 − 30.5 = 11.5
- 1.5 × IQR = 1.5 × 11.5 = 17.25
- Q3 + 1.5 × IQR = 42 + 17.25 = 59.25

The largest observation that is less than or equal to 59.25 is 49, so we draw the upper whisker up to 49. All points above 49 are considered outliers (61, 61, 62, 74, 80).

Q1 − 1.5 × IQR = 30.5 − 17.25 = 13.25

The smallest observation that is greater than or equal to 13.25 is 21, so we draw the lower whisker down to 21, which is also the minimum. There are no low outliers.

Here is the resulting boxplot for the Best Actress dataset, with each part labeled:

```{figure} images/gen/m04-actress-boxplot.svg
:alt: A horizontal boxplot of the winners' ages above an axis from 20 to 80. The lower whisker extends to the minimum, 21. The box runs from Q1 equals 30.5 to Q3 equals 42, with the median line at 34.5. The upper whisker stops at 49, the largest value within 1.5 IQR of the box. Five red dots at 61, 61, 62, 74, and 80 mark the outliers.
```

```{note} Video

[Constructing a Boxplot](https://www.youtube.com/watch?v=S50-WYpOm4I)
```

## Concept Check

Use the boxplot of the Best Actress ages to answer the following questions.

:::{quiz} From the boxplot, what percentage of the winners were older than 42 when they won?
:hint: 42 is the right edge of the box—the third quartile.
:feedback-0: 50% of the data lies above the median (34.5), not above Q3.
:feedback-1: Correct! Q3 = 42, and by definition 25% of observations lie above the third quartile.
:feedback-2: Only the five outliers lie above 59.25; a full quarter of the data lies above 42.
* 50%
* *25%
* About 11%
:::

:::{quiz} Why does the upper whisker stop at 49 rather than extending to the maximum value of 80?
:hint: Recall the Tukey (1.5 IQR) convention for whiskers.
:feedback-0: The whisker is not drawn to the maximum when outliers are present—it stops at the largest non-outlier.
:feedback-1: Correct! Under the 1.5(IQR) convention, the whisker extends only to the largest observation within Q3 + 1.5(IQR) = 59.25, which is 49; the larger values are plotted individually as outliers.
:feedback-2: 49 is not Q3 (Q3 = 42); it is the largest observation that is not a suspected outlier.
* The whisker always stops at the second-largest observation
* *49 is the largest observation that falls within Q3 + 1.5(IQR); larger values are plotted as outliers
* 49 is the third quartile of the data
:::
