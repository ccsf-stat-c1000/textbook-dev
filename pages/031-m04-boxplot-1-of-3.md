# Boxplot (1 of 3)

```{admonition} Learning Objectives
:class: note

- Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
```

## Introduction

Before we move on to the third measure of spread (standard deviation), we'll summarize what we've learned so far about measuring spread and use it to introduce another graphical display of the distribution of a quantitative variable, the *boxplot*.

## The Five Number Summary

So far, in our discussion about measures of spread, the key players were:

- the extremes (min and Max), which provide the range covered by all the data; and
- the quartiles (Q1, M and Q3), which together provide the IQR, the range covered by the middle 50% of the data.

The combination of all five numbers (min, Q1, M, Q3, Max) is called the *five number summary*, and provides a quick numerical description of both the center and spread of a distribution.

:::{admonition} Example: Best Actress Oscar Winners
:class: tip

We will continue with the Best Actress Oscar winners example:

```
34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29
33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44
```

The five number summary of the age of Best Actress Oscar winners (1970–2013) is:

| min | Q1 | M | Q3 | Max |
| --- | --- | --- | --- | --- |
| 21 | 30.5 | 34.5 | 42 | 80 |
:::

## Concept Check

:::{quiz} A dataset of 12 commute times (in minutes), already ordered, is: 12, 15, 18, 20, 22, 25, 26, 28, 30, 33, 38, 45. What is the five number summary?
:hint: The median is the mean of the 6th and 7th values; Q1 and Q3 are the medians of the bottom and top halves (6 values each).
:feedback-0: Correct! min = 12, Q1 = (18+20)/2 = 19, M = (25+26)/2 = 25.5, Q3 = (30+33)/2 = 31.5, Max = 45.
:feedback-1: Check Q1 and Q3—each half has 6 observations, so each quartile is the mean of two values.
:feedback-2: The median of an even number of observations is the mean of the two center values, not the 6th value alone.
* *min = 12, Q1 = 19, M = 25.5, Q3 = 31.5, Max = 45
* min = 12, Q1 = 18, M = 25.5, Q3 = 33, Max = 45
* min = 12, Q1 = 19, M = 25, Q3 = 31.5, Max = 45
:::
