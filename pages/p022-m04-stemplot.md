# The Stemplot: A Quick Graph by Hand

The stemplot (also called stem and leaf plot) is another graphical display of the distribution of quantitative data.

## Idea

Separate each data point into a stem and leaf, as follows:

- The *leaf* is the right-most digit.
- The *stem* is everything except the right-most digit.
- So, if the data point is 34, then 3 is the stem and 4 is the leaf.
- If the data point is 3.41, then 3.4 is the stem and 1 is the leaf.

::::{admonition} Example: Best Actress Oscar Winners
:class: tip

We will continue with the Best Actress Oscar winners example. Here are the ages of the winners from 1970 to 2013:

```
34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29
33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44
```

*To make a stemplot:*

1. Separate each observation into a stem and a leaf.
2. Write the stems in a vertical column with the smallest at the top, and draw a vertical line at the right of this column.
3. Go through the data points, and write each leaf in the row to the right of its stem.

```
2 | 7 1 6 9 6 5 8 9 9 2
3 | 4 4 7 6 2 3 1 3 8 3 6 9 4 3 5 5 0 2 3
4 | 2 1 1 9 1 2 5 9 5 4
5 |
6 | 1 1 2
7 | 4
8 | 0
```

4. Rearrange the leaves in an increasing order.

```
2 | 1 2 5 6 6 7 8 9 9 9
3 | 0 1 2 2 3 3 3 3 3 4 4 4 5 5 6 6 7 8 9
4 | 1 1 1 2 2 4 5 5 9 9
5 |
6 | 1 1 2
7 | 4
8 | 0
```

*An extra step:* when some of the stems hold a large number of leaves, we can split each stem into two—one holding the leaves 0–4, and the other holding the leaves 5–9:

```
2 | 1 2
2 | 5 6 6 7 8 9 9 9
3 | 0 1 2 2 3 3 3 3 3 4 4 4
3 | 5 5 6 6 7 8 9
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

Statistical software will often do the splitting for you, when appropriate.

*Note* that when rotated 90 degrees counterclockwise, the stemplot visually resembles a histogram:

```{figure} images/gen/m04-stemplot-rotated.svg
:alt: The split-stem stemplot rotated 90 degrees so the stems run along the bottom and the leaves stack upward like histogram bars. The columns are tall around stems 2 and 3 and short and scattered at stems 6, 7, and 8, making the right-skewed shape visible.
```

This orientation makes the right-skewness of the distribution clearly visible.
::::

The stemplot has additional unique features:

- It preserves the original data.
- It sorts the data (which will become very useful in the next section).

## The Dotplot

There is another type of display that we can use to summarize a quantitative variable graphically—the *dotplot*. The dotplot, like the stemplot, shows each observation, but displays it with a dot rather than with its actual value. Here is the dotplot for the ages of Best Actress Oscar winners:

```{figure} images/gen/m04-oscar-actress-dotplot.svg
:alt: A dotplot of the winners' ages. A number line runs from 20 to 80, and each winner is shown as a dot stacked above her age. The dots are concentrated between the mid-twenties and mid-forties, with the tallest stack of five dots at age 33 and a few isolated dots at ages 61, 62, 74, and 80.
```

## Check Your Understanding: Reading a Stemplot

:::{quiz} In the sorted stemplot of the winners' ages, what does the row "8 | 0" represent?
:hint: The stem is the tens digit, the leaf is the ones digit.
:feedback-0: Correct! Stem 8 with leaf 0 represents the single observation 80—one winner was 80 years old.
:feedback-1: A stem with no leaves would represent zero observations; here there is one leaf.
:feedback-2: Read the stem and leaf together as one number: stem 8 and leaf 0 make 80, not 8.
* *One winner was 80 years old
* No winners were in their eighties
* One winner was 8 years old
:::

:::{quiz} Using the stemplot, how many winners were in their sixties when they won?
:hint: Count the leaves on stem 6.
:feedback-0: Check again—stem 6 has three leaves: 1, 1, and 2.
:feedback-1: Correct! Stem 6 holds the leaves 1, 1, 2, representing ages 61, 61, and 62.
:feedback-2: Don't include the winner aged 74; that leaf belongs to stem 7.
* 2
* *3
* 4
:::

## Let's Summarize

The stemplot is a simple but useful visual display of quantitative data. Its principal virtues are:

- Easy and quick to construct for small, simple datasets.
- Retains the actual data.
- Sorts (ranks) the data.
