# Measures of Center (1 of 2)

```{admonition} Learning Objectives
    - Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

Intuitively speaking, the numerical measure of center is telling us what is a “typical value” of the distribution.

The three main numerical measures for the center of a distribution are the *mode*, the *mean* and the *median*. Each one of these measures is based on a completely different idea of describing the center of a distribution. We will first present each one of the measures, and then compare their properties.

## Mode

So far, when we looked at the shape of the distribution, we identified the mode as the value where the distribution has a “peak” and saw examples when distributions have one mode (unimodal distributions) or two modes (bimodal distributions). In other words, so far we identified the mode visually from the histogram.

Technically, the mode is the most commonly occurring value in a distribution. For simple datasets where the frequency of each value is available or easily determined, the value that occurs with the highest frequency is the mode.

```{admonition} Example: Best Actress Oscar Winners
    We will continue with the Best Actress Oscar winners example. (To see the full dataset, click here.)

    To find the most commonly occurring, or *modal*, age, it is helpful to list the ages in a frequency table, which gives the following results:

    | *Best Actress Age* | 21 | 22 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | *33* | 34 | 35 | 36 | 37 | 38 | 39 | 41 | 42 | 44 | 49 | 61 | 62 | 74 | 80 |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | *Count* | 1 | 1 | 1 | 2 | 1 | 1 | 3 | 1 | 1 | 2 | *6* | 2 | 2 | 2 | 1 | 1 | 1 | 3 | 2 | 2 | 2 | 2 | 1 | 1 | 1 |

    The mode is 33, since it occurs the most times (6).
```

```{admonition} Example: World Cup Soccer
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
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Mean

The mean is the average of a set of observations (i.e., the sum of the observations divided by the number of observations). If the n observations are x~1~, x~2~, ... , x~n~, their mean, which we denote by $\bar{x}$ (and read x-bar), is therefore $\bar{x} = \frac{x_{1} + x_{2} +...+x_{n}}{n}$

```{admonition} Example: Best Actress Oscar Winners
    Again we use the Best Actress Oscar winners example. (To see the full dataset, click here.)

    34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29 33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44

    The mean age of the 32 actresses is $\bar{x} = \frac{34 + 34 + 27 +...+ 62 + 22+ 44}{44} = \frac{1687}{44} = 38.3$
```

Note that the mean gives a measure of center that is higher than our approximation of the center from looking at the histogram (which was 35). The reason for this will be clear soon.

```{admonition} Example: World Cup Soccer
    We now continue with the data from the last three World Cup soccer tournaments. A total of 192 games were played. The table below lists the number of goals scored per game (not including any goals scored in shootouts).

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

    To find the mean number of goals scored per game, we would need to find the sum of all 192 numbers, then divide that sum by 192. Rather than add 192 numbers, we use the fact that the same numbers appear many times. For example, the number 0 appears 17 times, the number 1 appears 45 times, the number 2 appears 51 times, etc.

    If we add up 17 zeros, we get 0. If we add up 45 ones, we get 45. If we add up 51 twos, we get 102. Repeated addition is multiplication.

    Thus, the sum of the 192 numbers = 0(17) + 1(45) + 2(51) + 3(37) + 4(25) + 5(11) + 6(3) + 7(2) + 8(1) = 453.

    The mean is 453/192 = 2.359.

    This way of calculating a mean is sometimes referred to as a *weighted average*, since each value is "weighted" by its frequency. Note that, in this example, the values of 1, 2, and 3 are most heavily weighted.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Median

The median M is the midpoint of the distribution. It is the number such that half of the observations fall above, and half fall below. To find the median:

- Order the data from smallest to largest.
- Consider whether n, the number of observations, is even or odd.
  - If n is *odd*, the median M is the center observation in the ordered list. This observation is the one "sitting" in the *(n + 1)/2 spot* in the ordered list.
  - If n is *even*, the median M is the *mean* of the*two center observations* in the ordered list. These two observations are the ones "sitting" in the *n/2* and *n/2 + 1* spots in the ordered list.

```{admonition} Example: Median (1)
    For a simple visualization of the location of the median, consider the following two simple cases of n = 7 and n = 8 ordered observations, with each observation represented by a solid circle:

    ```{figure} images/center1.gif
    :alt: When there are n=7 ordered observations, the median M is the center observation, which is located in the (7+1)/2 = 4th spot in the ordered list. When there are n=8 ordered observations, the mediam M is the mean of the two center observations, which in this care are located at the 8/2=4th and 8/2+1=5th spots in the ordered list.

    When there are n=7 ordered observations, the median M is the center observation, which is located in the (7+1)/2 = 4th spot in the ordered list. When there are n=8 ordered observations, the mediam M is the mean of the two center observations, which in this care are located at the 8/2=4th and 8/2+1=5th spots in the ordered list.
    ```
```

```{admonition} Example: Median (2)
    To find the median age of the Best Actress Oscar winners, we first need to order the data. It would be useful, then, to use the stemplot, a diagram in which the data are already ordered.

    Here n = 44 (an even number), so the median M, will be the mean of the two center observations. These are located at the n / 2 = 44 / 2 = *22nd* and n / 2 + 1 = 44 / 2 + 1 = *23rd* spots. Counting from the top, we find that:

    - the 22nd ranked observation is 34
    - the 23rd ranked observation is 35

    Therefore, the median $M = \frac{(34 + 35)}{2} = 34.5$

    ```{figure} images/eda_examining_distributions_best_actress_stemplot_median2.jpg
    :alt: A stem plot in which the 16th and 17th leaves are highlighted. The stem plot is described in a stem|leaves format in row order. The highlighted entries are surrounded by *: 2|12 2|56678999 3|012233333344 3|5566789 4|1112244 4|599 5| 5| 6|112 6| 7|4 7| 8|0

    A stem plot in which the 16th and 17th leaves are highlighted. The stem plot is described in a stem|leaves format in row order. The highlighted entries are surrounded by *: 2|12 2|56678999 3|012233333344 3|5566789 4|1112244 4|599 5| 5| 6|112 6| 7|4 7| 8|0
    ```
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

##### Calculating mean, median, and mode

```{note} Video
[Finding mean, median, and mode | Descriptive statistics | Probability and Statistics | Khan Academy](https://www.youtube.com/watch?v=k3aKKasOmIw)
```

[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by [Khan Academy](https://www.oercommons.org/courses/statistics-mean-median-and-mode)

Explore this simulation activity to see how well you can calculate the mean and median for different data sets.

To view this interactive simulation in a separate window click [here](http://ggbtu.be/m13347).

[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by [GeoGebra Group](http://www.geogebra.org/)

```{note}
    **Learn By Doing**

    Measures of Center

    *(Interactive activity — available in the OLI platform)*
```
