# Measures of Spread (4 of 5)

```{admonition} Learning Objectives
    - Summarize and describe the distribution of a quantitative variable in context: a) describe the overall pattern, b) describe striking deviations from the pattern.
    - Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

## Using the IQR to Detect Outliers

So far we have quantified the idea of center, and we are in the middle of the discussion about measuring spread, but we haven't really talked about a method or rule that will help us classify extreme observations as outliers. The IQR is used as the basis for a rule of thumb for identifying outliers.

## The 1.5(IQR) Criterion for Outliers

An observation is considered a suspected outlier if it is:

- below Q1 - 1.5(IQR) or
- above Q3 + 1.5(IQR)

The following picture illustrates this rule:

```{figure} images/spread10.gif
:alt: A line representing all of the data. The data is ordered so that the minimum point is the leftmost on the line and the maximum point is the rightmost. At the center of the line is M, the median, and to the left of M is Q1. Even farther to the left of Q1 is Q1-1.5(IQR). Points farther left than this are suspected outliers. To the right of M is Q3, and farther to the right is Q3+1.5(IQR). Points even farther than this are also suspected outliers.

A line representing all of the data. The data is ordered so that the minimum point is the leftmost on the line and the maximum point is the rightmost. At the center of the line is M, the median, and to the left of M is Q1. Even farther to the left of Q1 is Q1-1.5(IQR). Points farther left than this are suspected outliers. To the right of M is Q3, and farther to the right is Q3+1.5(IQR). Points even farther than this are also suspected outliers.
```

```{admonition} Example: Best Actress Oscar Winners
    We will continue with the Best Actress Oscar winners example (To see the data, click here).

    ```
    34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29
                  33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44
    ```

    Recall that when we first looked at the histogram of ages of Best Actress Oscar winners, there were 5 observations that looked like possible outliers:

    ```{figure} images/eda_examining_distributions_best_actress_histogram_outliers.jpg
    :alt: A histogram of the Oscar winners in which for x=62 the frequency is 3 and for x=74 and x=80, the frequency is 1. Those points are thought to be possible outliers.

    A histogram of the Oscar winners in which for x=62 the frequency is 3 and for x=74 and x=80, the frequency is 1. Those points are thought to be possible outliers.
    ```

    We can now use the 1.5(IQR) criterion to check whether the 5 observations should indeed be classified as outliers:

    - For this example we found that $Q1=30.5  and  Q3=42.5 \Rightarrow IQR=11.5$
    - $Q1 − 1.5\left(IQR\right) = 30.5 − \left(1.5\right)\left(11.5\right) = 13.25$
    - $Q3 + 1.5\left(IQR\right) = 42.5 + \left(1.5\right)\left(11.5\right) = 59.25$

    The 1.5(IQR) criterion tells us that any observation that is below 13.25 or above 59.25 is considered a suspected outlier.

    We therefore conclude that the observations 61, 61, 62, 74 and 80 should be flagged as suspected outliers in the distribution of ages. Note that since the smallest observation is 21, there are no suspected low outliers in this distribution.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on to the next page. If not, then click the link below for some additional practice.

```{note}
    **Did I Get This?**

    Measures of Spread: Extra Problems

    *(Interactive activity — available in the OLI platform)*
```
