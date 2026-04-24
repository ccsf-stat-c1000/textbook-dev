# Measures of Spread (3 of 5)

```{admonition} Learning Objectives
    - Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

```{admonition} Example: Best Actress Oscar Winners
    To find the IQR of the Best Actress Oscar winners distribution, it will be convenient to use the stemplot.

    ```{figure} images/eda_examining_distributions_best_actress_stemplot_IQR.jpg
    :alt: Stem plot of the Best Actress Oscar winners. The lower half of the step plot is the bottom half and the upper half is the top half. The stem plot is described in a stem|leaves format in row order. Note that the bottom half ends and the top half begins in the middle of a line (between two leaves). We begin with the bottom half: 2|12 2|56678999 3|012233333344 3|The top half: 3|4 3|5566789 4|1112244 4|99 5| 5| 6|112 6| 7|4 7| 8|0

    Stem plot of the Best Actress Oscar winners. The lower half of the step plot is the bottom half and the upper half is the top half. The stem plot is described in a stem|leaves format in row order. Note that the bottom half ends and the top half begins in the middle of a line (between two leaves). We begin with the bottom half: 2|12 2|56678999 3|012233333344 3|The top half: 3|4 3|5566789 4|1112244 4|99 5| 5| 6|112 6| 7|4 7| 8|0
    ```

    Q1 is the median of the bottom half of the data. Since there are 22 observations in that half, Q1 is the mean of the 11th and 12th ranked observations in that half:

    $Q1 = \frac{(30 + 31)}{2} = 30.5$

    Similarly, Q3 is the median of the top half of the data, and since there are 22 observations in that half, Q3 is the mean of the 11th and 12th ranked observations in that half:

    $Q3 = \frac{(42 + 42)}{2} = 42$

    $IQR = (42 −30.5 ) = 11.5$

    Note that in this example, the range covered by all the ages is 59 years, while the range covered by the middle 50% of the ages is only 11.5 years. While the whole dataset is spread over a range of 59 years, the middle 50% of the data is packed into only 11.5 years. Looking again at the histogram will illustrate this:

    ```{figure} images/eda_examining_distributions_best_actress_histogram_IQR.jpg
    :alt: Histogram of the Best Actress Oscar Winners with the Range and IQR labeled. Recall that the histogram is skewed right. While the range encompasses the entire histogram, the IQR starts at x=30.5 and ends at x=42 , which is located within area of ages with higher frequencies on the histogram.

    Histogram of the Best Actress Oscar Winners with the Range and IQR labeled. Recall that the histogram is skewed right. While the range encompasses the entire histogram, the IQR starts at x=30.5 and ends at x=42 , which is located within area of ages with higher frequencies on the histogram.
    ```
```

## Comment

Software packages use different formulas to calculate the quartiles Q1 and Q3. This should not worry you, as long as you understand the idea behind these concepts. For example, here are the quartile values provided by three different software packages for the age of best actress Oscar winners:

*R:*

```{figure} images/spread9r.gif
:alt: A snippet of output from R. It shows that: Min=21.00, Q1=32.50, Median=35, Q3=41.25, Max=80.00 .

A snippet of output from R. It shows that: Min=21.00, Q1=32.50, Median=35, Q3=41.25, Max=80.00 .
```

*Minitab:*

```{figure} images/spread9.gif
:alt: A snippet of output from Minitab. It shows that N=32, Mean=38.53, Median=35.00, TrMean=36.89, StDev=12.95, SE Mean=2.29, Minimum=21.00, Maximum=80.00, Q1=31.50, Q2=41.75 .

A snippet of output from Minitab. It shows that N=32, Mean=38.53, Median=35.00, TrMean=36.89, StDev=12.95, SE Mean=2.29, Minimum=21.00, Maximum=80.00, Q1=31.50, Q2=41.75 .
```

*Excel:*

```{figure} images/spread9excel.gif
:alt: Four cells from a Excel spreadsheet showing that Q1=32.5 and Q3=41.25 .

Four cells from a Excel spreadsheet showing that Q1=32.5 and Q3=41.25 .
```

*Note* that Q1 and Q3 as reported by the various software packages differ from each other and are also slightly different from the ones we found here. There are different acceptable ways to find the median and the quartiles. These can give different results occasionally, especially for datasets where n (the number of observations) is fairly small. As long as you know what the numbers mean, and how to interpret them in context, it doesn't really matter much what method you use to find them, since the differences are really negligible.
