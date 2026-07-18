# The Histogram: Seeing the Shape of the Data

```{admonition} Learning Objectives
:class: note

- Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
```

## Idea

Break the range of values into intervals and count how many observations fall into each interval.

::::{admonition} Example: Exam Grades
:class: tip

Here are the exam grades of 15 students:

```
88, 48, 60, 51, 57, 85, 69, 75, 97, 72, 71, 79, 65, 63, 73
```

We first need to break the range of values into intervals (also called "bins" or "classes"). In this case, since our dataset consists of exam scores, it will make sense to choose intervals that typically correspond to the range of a letter grade, 10 points wide: 40–50, 50–60, ... 90–100. By counting how many of the 15 observations fall in each of the intervals, we get the following table:

| Score | Count |
| --- | --- |
| [40–50) | 1 |
| [50–60) | 2 |
| [60–70) | 4 |
| [70–80) | 5 |
| [80–90) | 2 |
| [90–100] | 1 |

Note: The observation 60 was counted in the 60–70 interval. See comment 1 below.

To construct the histogram from this table we plot the intervals on the X-axis, and show the number of observations in each interval (frequency of the interval) on the Y-axis, which is represented by the height of a rectangle located above the interval:

```{figure} images/gen/m04-exam-scores-histogram.svg
:alt: A histogram of the 15 exam grades. The horizontal axis shows scores from 40 to 100 in intervals of 10, and the vertical axis shows the count in each interval. The bars have heights 1, 2, 4, 5, 2, and 1, rising to a peak in the 70 to 80 interval and falling away on both sides.
```

The table above can also be turned into a relative frequency table using the following steps:

1. Add a row on the bottom and include the total number of observations in the dataset that are represented in the table.
2. Add a column, at the end of the table, and calculate the relative frequency for each interval, by dividing the number of observations in each row by the total number of observations.

These two steps are illustrated in the following relative frequency table:

| Score | Count | Relative Frequency |
| --- | --- | --- |
| [40–50) | 1 | 1/15 ≈ 0.07 |
| [50–60) | 2 | 2/15 ≈ 0.13 |
| [60–70) | 4 | 4/15 ≈ 0.27 |
| [70–80) | 5 | 5/15 ≈ 0.33 |
| [80–90) | 2 | 2/15 ≈ 0.13 |
| [90–100] | 1 | 1/15 ≈ 0.07 |
| *Total* | *n = 15* | *1.00* |

It is also possible to determine the number of scores for an interval, if you have the total number of observations and the relative frequency for that interval. For instance, suppose there are 15 scores (or observations) in a set of data and the relative frequency for an interval is 0.13. To determine the number of scores in that interval, multiply the total number of observations by the relative frequency and round to the nearest whole number: 15 × 0.13 = 1.95, which rounds to 2 observations.

A relative frequency table, like the one above, can be used to determine the frequency of scores occurring at or across intervals. Here are some examples, using the above frequency table:

1. What is the percentage of exam scores that were 70 and up to, but not including, 80? To determine the answer, we look at the relative frequency associated with the [70–80) interval. The relative frequency is 0.33; to convert to percentage, multiply by 100 (0.33 × 100 = 33) or 33%.
2. What is the percentage of exam scores that are at least 70? To determine the answer, we need to:
   - Add together the relative frequencies for the intervals that have scores of at least 70 or above. Thus, we would need to add together the relative frequencies from [70–80), [80–90), and [90–100]: 0.33 + 0.13 + 0.07 = 0.53.
   - To get the percentage, multiply the calculated relative frequency by 100. In this case, it would be 0.53 × 100 = 53 or 53%.
::::

## Check Your Understanding: Reading a Histogram

Here is the frequency table from above; use it to answer the questions.

| Score | Count |
| --- | --- |
| [40–50) | 1 |
| [50–60) | 2 |
| [60–70) | 4 |
| [70–80) | 5 |
| [80–90) | 2 |
| [90–100] | 1 |

:::{quiz} How many students scored below 60 on the exam?
:hint: Which intervals contain only scores less than 60?
:feedback-0: Don't forget the one student in the [40–50) interval.
:feedback-1: Correct! 1 + 2 = 3 students scored in the [40–50) and [50–60) intervals.
:feedback-2: Careful—[60–70) includes 60 itself, so its 4 students did not score below 60.
* 2
* *3
* 7
:::

:::{quiz} What percentage of the 15 students scored between 60 and 80 (that is, in the intervals [60–70) and [70–80))?
:hint: Add the counts in the two intervals, divide by 15, and convert to a percentage.
:feedback-0: 33% counts only the [70–80) interval.
:feedback-1: Correct! (4 + 5)/15 = 9/15 = 0.60, or 60%.
:feedback-2: 27% counts only the [60–70) interval.
* 33%
* *60%
* 27%
:::

```{admonition} Comments
:class: important

1. It is very important that each observation be counted only in one interval. For the most part, it is clear which interval an observation falls in. However, in our example, we needed to decide whether to include 60 in the interval 50–60, or the interval 60–70, and we chose to count it in the latter. In fact, this decision is captured by the way we wrote the intervals. If you scroll up and look at the table, you'll see that we wrote the intervals in a peculiar way: [40–50), [50–60), [60–70), and so on. The square bracket means "including," and the parenthesis means "not including." For example, [50–60) is the interval from 50 to 60, including 50 and not including 60; [60–70) is the interval from 60 to 70, including 60, and not including 70. It does not matter how you decide to set up your intervals as long as you're consistent.

2. When data are displayed in a histogram, some information is lost. Note that by looking at the histogram we *can* answer: "How many students scored 70 or above?" (5 + 2 + 1 = 8) But we *cannot* answer: "What was the lowest score?" All we can say is that the lowest score is somewhere between 40 and 50, and therefore we can approximate that it is around 45.

3. Obviously, we could have chosen to break the data into intervals differently (for example, 45–50, 50–55, 55–60). There is no single "correct" choice: wider bins give a smoother but coarser picture, while narrower bins show more detail but can look jagged. When you create histograms using statistical software or a calculator, try a few different bin widths and notice how the shape of the histogram changes.
```

:::{quiz} Using only the histogram of the 15 exam grades (not the raw data), which of the following questions can you answer exactly?
:hint: A histogram tells you how many observations fall in each interval, but not the individual values.
:feedback-0: The exact highest score can't be recovered from the histogram—we only know it lies in the [90–100] interval.
:feedback-1: Correct! Counts in intervals (and sums of counts) can be read exactly from a histogram: 2 + 1 = 3 students scored 80 or above.
:feedback-2: The exact average requires the individual scores, which the histogram does not show.
* What was the highest score?
* *How many students scored 80 or above?
* What was the average score?
:::
