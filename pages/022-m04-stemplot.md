# Stemplot

```{admonition} Learning Objectives
    - Summarize and describe the distribution of a quantitative variable in context: a) describe the overall pattern, b) describe striking deviations from the pattern.
```

The stemplot (also called stem and leaf plot) is another graphical display of the distribution of quantitative data.

## Idea

Separate each data point into a stem and leaf, as follows:

| The leaf is the right-most digit. |
| --- |
| The stem is everything except the right-most digit. |
| So, if the data point is 34, then 3 is the stem and 4 is the leaf. |
| If the data point is 3.41, then 3.4 is the stem and 1 is the leaf. |

```{admonition} Example: Best Actress Oscar Winners
    We will continue with the Best Actress Oscar winners example (To see the full dataset, click here.)

    34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29 33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44

    *To make a stemplot:*

    1. Separate each observation into a stem and a leaf.
    2. Write the stems in a vertical column with the smallest at the top, and draw a vertical line at the right of this column.
    3. Go through the data points, and write each leaf in the row to the right of its stem.
    4. Rearrange the leaves in an increasing order.

    ```{figure} images/eda_examining_distributions_best_actress_stemplot.jpg
    :alt: The result of steps 1, 2, and 3 on the given data set results in the following: first row: 2|7169658992 second row: 3|3376231383694355023 third row: 4|2119124954 fourth row: 5| fifth row: 6|112 sixth row: 7|4 seventh row: 8|0 Step 4 results in: first row: 2|1256678999 second row: 3|0122333333445566789 third row: 4|1112244599 fourth row: 5| fifth row: 6|112 sixth row: 7|4 seventh row: 8|0 Following the extra step(*): first row: 2|12 second row: 2|56678999 third row: 3|012233333344 fourth row: 3|5566789 fifth row: 4|1112244 sixth row: 4|599 seventh row: 5| eighth row: 5| ninth row: 6|112 tenth row: 7|4 eleventh row:7| twelfth row: 8|0

    The result of steps 1, 2, and 3 on the given data set results in the following: first row: 2|7169658992 second row: 3|3376231383694355023 third row: 4|2119124954 fourth row: 5| fifth row: 6|112 sixth row: 7|4 seventh row: 8|0 Step 4 results in: first row: 2|1256678999 second row: 3|0122333333445566789 third row: 4|1112244599 fourth row: 5| fifth row: 6|112 sixth row: 7|4 seventh row: 8|0 Following the extra step(*): first row: 2|12 second row: 2|56678999 third row: 3|012233333344 fourth row: 3|5566789 fifth row: 4|1112244 sixth row: 4|599 seventh row: 5| eighth row: 5| ninth row: 6|112 tenth row: 7|4 eleventh row:7| twelfth row: 8|0
    ```

    * When some of the stems hold a large number of leaves, we can split each stem into two: one holding the leaves 0-4, and the other holding the leaves 5-9. A statistical software package will often do the splitting for you, when appropriate.

    *Note*that when rotated 90 degrees counterclockwise, the stemplot visually resembles a histogram:

    ```{figure} images/eda_examining_distributions_best_actress_stemplot_rotated.jpg
    :alt: A rotated stem plot. This is the same as the last stem plot given in the previous image, but rotated so that the stems are at the bottom, with the leaves on top.

    A rotated stem plot. This is the same as the last stem plot given in the previous image, but rotated so that the stems are at the bottom, with the leaves on top.
    ```

    This orientation makes the right-skewedness of the distribution clearly visible.
```

The stemplot has additional unique features:

- It preserves the original data.
- It sorts the data (which will become very useful in the next section).

## Comment

There is another type of display that we can use to summarize a quantitative variable graphically—the *dotplot*. The dotplot, like the stemplot, shows each observation, but displays it with a dot rather than with its actual value. Here is the dotplot for the ages of Best Actress Oscar winners.

```{figure} images/eda_examining_distributions_best_actress_dotplot.jpg
:alt: A dotplot titled &quot;Dotplot of Age&quot; A number line is at the bottom of the image, labeled in units of age from 24 to 80. At each age on the number line the a line of dots, each representing one winner of that age, appears above the place of that age on the number line.

A dotplot titled &quot;Dotplot of Age&quot; A number line is at the bottom of the image, labeled in units of age from 24 to 80. At each age on the number line the a line of dots, each representing one winner of that age, appears above the place of that age on the number line.
```

## Let's Summarize

The stemplot is a simple but useful visual display of quantitative data. Its principal virtues are:

- Easy and quick to construct for small, simple datasets.
- Retains the actual data.
- Sorts (ranks) the data.

```{note}
    **Many Students Wonder**

    Stemplot

    *(Interactive activity — available in the OLI platform)*
```

## Questions

```{note}
    **My Response**

    About Stemplots

    *(Interactive activity — available in the OLI platform)*
```
