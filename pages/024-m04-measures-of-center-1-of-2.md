# Mode, Median, and Mean: Three Ways to Locate the Center

```{admonition} Learning Objectives
:class: note

- Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

Intuitively speaking, the numerical measure of center is telling us what is a "typical value" of the distribution.

The three main numerical measures for the center of a distribution are the *mode*, the *mean* and the *median*. Each one of these measures is based on a completely different idea of describing the center of a distribution. We will first present each one of the measures, and then compare their properties.

## Mode

So far, when we looked at the shape of the distribution, we identified the mode as the value where the distribution has a "peak" and saw examples when distributions have one mode (unimodal distributions) or two modes (bimodal distributions). In other words, so far we identified the mode visually from the histogram.

Technically, the mode is the most commonly occurring value in a distribution. For simple datasets where the frequency of each value is available or easily determined, the value that occurs with the highest frequency is the mode.

:::{admonition} Example: Best Actress Oscar Winners
:class: tip

We will continue with the Best Actress Oscar winners example.

To find the most commonly occurring, or *modal*, age, it is helpful to list the ages in a frequency table, which gives the following results:

| *Best Actress Age* | 21 | 22 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | **33** | 34 | 35 | 36 | 37 | 38 | 39 | 41 | 42 | 44 | 45 | 49 | 61 | 62 | 74 | 80 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *Count* | 1 | 1 | 1 | 2 | 1 | 1 | 3 | 1 | 1 | 2 | **5** | 3 | 2 | 2 | 1 | 1 | 1 | 3 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |

The mode is 33, since it occurs the most times (5).
:::

:::{admonition} Example: World Cup Soccer
:class: tip

Often, we have large sets of data and use a frequency table to display the data more efficiently.

Data were collected from the last three World Cup soccer tournaments. A total of 192 games were played. The table below lists the number of goals scored per game (not including any goals scored in shootouts).

| Total # Goals/Game | Frequency |
| --- | --- |
| 0 | 17 |
| 1 | 45 |
| 2 | 51 |
| 3 | 37 |
| 4 | 25 |
| 5 | 11 |
| 6 | 3 |
| 7 | 2 |
| 8 | 1 |

We can see that the most frequently occurring value is 2 goals (which occurred 51 times). Therefore, the mode for this set of data is 2.
:::

:::{quiz} A student recorded the number of books read last month by 8 friends: 1, 2, 2, 3, 3, 3, 4, 6. What is the mode of this dataset?
:hint: The mode is the value that occurs most often.
:feedback-0: 2 occurs twice, but another value occurs more often.
:feedback-1: Correct! The value 3 occurs three times, more than any other value.
:feedback-2: 6 is the largest value, not the most frequent one.
* 2
* *3
* 6
:::

## Mean

The mean is the average of a set of observations (i.e., the sum of the observations divided by the number of observations). If the n observations are $x_1, x_2, \ldots, x_n$, their mean, which we denote by $\bar{x}$ (and read x-bar), is therefore

$$\bar{x} = \frac{x_{1} + x_{2} + \cdots + x_{n}}{n}$$

:::{admonition} Example: Best Actress Oscar Winners
:class: tip

Again we use the Best Actress Oscar winners example:

```
34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29
33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44
```

The mean age of the 44 actresses is

$$\bar{x} = \frac{34 + 34 + 27 + \cdots + 62 + 22 + 44}{44} = \frac{1687}{44} \approx 38.3$$
:::

Note that the mean gives a measure of center that is higher than our approximation of the center from looking at the histogram (which was about 35). The reason for this will be clear soon.

:::{admonition} Example: World Cup Soccer
:class: tip

We now continue with the data from the last three World Cup soccer tournaments, displayed in the frequency table above.

To find the mean number of goals scored per game, we would need to find the sum of all 192 numbers, then divide that sum by 192. Rather than add 192 numbers, we use the fact that the same numbers appear many times. For example, the number 0 appears 17 times, the number 1 appears 45 times, the number 2 appears 51 times, etc.

If we add up 17 zeros, we get 0. If we add up 45 ones, we get 45. If we add up 51 twos, we get 102. Repeated addition is multiplication.

Thus, the sum of the 192 numbers = 0(17) + 1(45) + 2(51) + 3(37) + 4(25) + 5(11) + 6(3) + 7(2) + 8(1) = 453.

The mean is 453/192 ≈ 2.36.

This way of calculating a mean is sometimes referred to as a *weighted average*, since each value is "weighted" by its frequency. Note that, in this example, the values of 1, 2, and 3 are most heavily weighted.
:::

:::{quiz} A student's five quiz scores are 6, 8, 7, 9, and 10. What is the mean score?
:hint: Add the scores and divide by how many there are.
:feedback-0: 7 would be the median if you ordered the values—check your sum.
:feedback-1: Correct! (6 + 8 + 7 + 9 + 10)/5 = 40/5 = 8.
:feedback-2: 40 is the sum of the scores; don't forget to divide by 5.
* 7
* *8
* 40
:::

:::{quiz} In 10 games, a soccer team scored 0 goals twice, 1 goal three times, and 2 goals five times. What is the mean number of goals per game?
:hint: Multiply each value by its frequency, add, then divide by the total number of games.
:feedback-0: 1 is the middle value of 0, 1, 2, not the weighted mean.
:feedback-1: Correct! (0×2 + 1×3 + 2×5)/10 = 13/10 = 1.3.
:feedback-2: 13 is the total number of goals; divide by the 10 games.
* 1
* *1.3
* 13
:::

## Median

The median M is the midpoint of the distribution. It is the number such that half of the observations fall above, and half fall below. To find the median:

- Order the data from smallest to largest.
- Consider whether n, the number of observations, is even or odd.
  - If n is *odd*, the median M is the center observation in the ordered list. This observation is the one "sitting" in the *(n + 1)/2 spot* in the ordered list.
  - If n is *even*, the median M is the *mean* of the *two center observations* in the ordered list. These two observations are the ones "sitting" in the *n/2* and *n/2 + 1* spots in the ordered list.

::::{admonition} Example: Median (1)
:class: tip

For a simple visualization of the location of the median, consider the following two simple cases of n = 7 and n = 8 ordered observations, with each observation represented by a solid circle:

```{figure} images/gen/m04-median-position.svg
:alt: Two rows of ordered dots. In the top row of 7 dots, the 4th dot, located at spot (7+1)/2, is highlighted as the median M. In the bottom row of 8 dots, the 4th and 5th dots, located at spots 8/2 and 8/2 + 1, are highlighted, and the median M is the mean of these two center observations.
```
::::

::::{admonition} Example: Median (2)
:class: tip

To find the median age of the Best Actress Oscar winners, we first need to order the data. It would be useful, then, to use the stemplot, a diagram in which the data are already ordered.

Here n = 44 (an even number), so the median M will be the mean of the two center observations. These are located at the n/2 = 44/2 = *22nd* and n/2 + 1 = 44/2 + 1 = *23rd* spots. Counting the leaves from the top of the stemplot:

```
2 | 1 2
2 | 5 6 6 7 8 9 9 9          ← 10 observations so far
3 | 0 1 2 2 3 3 3 3 3 4 4 4  ← the 22nd is the last 4 in this row
3 | 5 5 6 6 7 8 9            ← the 23rd is the first 5 in this row
4 | 1 1 1 2 2 4
4 | 5 5 9 9
5 |
5 |
6 | 1 1 2
6 |
7 | 4
7 |
8 | 0
```

- the 22nd ranked observation is 34
- the 23rd ranked observation is 35

Therefore, the median $M = \frac{34 + 35}{2} = 34.5$
::::

:::{quiz} Find the median of the dataset: 3, 5, 8, 12, 13, 14.
:hint: n = 6 is even, so average the two center observations (the 3rd and 4th).
:feedback-0: 8 is only the 3rd observation; with an even n you must average the two center values.
:feedback-1: Correct! The two center observations are 8 and 12, and (8 + 12)/2 = 10.
:feedback-2: 12 is only the 4th observation; average it with the 3rd.
* 8
* *10
* 12
:::

## Check Your Understanding: Measures of Center

:::{quiz} For the dataset 2, 3, 3, 5, 7, which of the following statements is true?
:hint: Find all three measures: the most frequent value, the middle value, and the average.
:feedback-0: Correct! The mode is 3 (most frequent), the median is 3 (middle of five ordered values), and the mean is (2+3+3+5+7)/5 = 4.
:feedback-1: Check the mean: the sum is 20 and there are 5 observations, so the mean is 4, not 3.
:feedback-2: Check the median: the middle (3rd) observation of the ordered list is 3, not 5.
* *The mode and median both equal 3, and the mean equals 4
* The mode, median, and mean all equal 3
* The median equals 5 and the mean equals 4
:::
