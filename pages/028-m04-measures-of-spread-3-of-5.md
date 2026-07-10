# Measures of Spread (3 of 5)

```{admonition} Learning Objectives
:class: note

- Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

::::{admonition} Example: Best Actress Oscar Winners
:class: tip

To find the IQR of the Best Actress Oscar winners distribution, it will be convenient to use the stemplot, with the bottom half and top half of the data marked:

```
bottom half            top half
2 | 1 2                3 | 5 5 6 6 7 8 9
2 | 5 6 6 7 8 9 9 9    4 | 1 1 1 2 2 4
3 | 0 1 2 2 3 3 3 3    4 | 5 5 9 9
3 | 3 4 4 4            5 |
                       6 | 1 1 2
                       7 | 4
                       8 | 0
```

Q1 is the median of the bottom half of the data. Since there are 22 observations in that half, Q1 is the mean of the 11th and 12th ranked observations in that half:

$$Q1 = \frac{30 + 31}{2} = 30.5$$

Similarly, Q3 is the median of the top half of the data, and since there are 22 observations in that half, Q3 is the mean of the 11th and 12th ranked observations in that half:

$$Q3 = \frac{42 + 42}{2} = 42$$

$$IQR = 42 - 30.5 = 11.5$$

Note that in this example, the range covered by all the ages is 59 years, while the range covered by the middle 50% of the ages is only 11.5 years. While the whole dataset is spread over a range of 59 years, the middle 50% of the data is packed into only 11.5 years. Looking again at the histogram will illustrate this:

```{figure} images/gen/m04-oscar-iqr-histogram.svg
:alt: The histogram of the winners' ages, which is skewed right, annotated with two brackets below the axis. A wide bracket spanning ages 21 to 80 is labeled Range equals 59, while a much narrower bracket from 30.5 to 42, located under the tallest bars, is labeled IQR equals 11.5.
```
::::

## Comment

Software packages use different formulas to calculate the quartiles Q1 and Q3. This should not worry you, as long as you understand the idea behind these concepts. For example, here are the quartile values provided by three different statistical software packages for the age of Best Actress Oscar winners:

| Software | Q1 | Q3 |
| --- | --- | --- |
| Package A | 32.50 | 41.25 |
| Package B | 31.50 | 41.75 |
| Package C | 32.50 | 41.25 |

*Note* that Q1 and Q3 as reported by the various software packages differ from each other and are also slightly different from the ones we found here. There are different acceptable ways to find the median and the quartiles. These can give different results occasionally, especially for datasets where n (the number of observations) is fairly small. As long as you know what the numbers mean, and how to interpret them in context, it doesn't really matter much what method you use to find them, since the differences are really negligible.
