# Histogram (1 of 3)

```{admonition} Learning Objectives
    - Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
```

## Idea

Break the range of values into intervals and count how many observations fall into each interval.

```{admonition} Example: Exam Grades
    Here are the exam grades of 15 students:

    ```
    88, 48, 60, 51, 57, 85,
                  69, 75, 97, 72, 71, 79, 65, 63, 73
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

    The table above can also be turned into a relative frequency table using the following steps:

    1. Add a row on the bottom and include the total number of observations in the
                    dataset that are represented in the table.
    2. Add a column, at the end of the table, and calculate the relative frequency for
                    each interval, by dividing the number of observations in each row by the total
                    number of observations.

    These two steps are illustrated in red in the following frequency distribution table:

    ```{figure} images/feq_table.png
    ```

    It is also possible to determine the number of scores for an interval, if you have the total number of observations and the relative frequency for that interval. For instance, suppose there are 15 scores (or observations) in a set of data and the relative frequency for an interval is .13. To determine the number of scores in that interval, multiplying the total number of observations by the relative frequency and round up to the next whole number: 15*.13 = 1.95, which rounds up to 2 observations.

    A relative frequency table, like the one above, can be used to determine the frequency of scores occurring at or across intervals. Here are some examples, using the above frequency table:

    1. What is the percentage of exam scores that were 70 and up to, but not including,
                    80? To determine the answer, we look at the relative frequency associated with the
                    [70-80) interval. The relative frequency is .33; to convert to percentage, multiply
                    by 100 (.33*100= 33) or 33%.
    2. What is the percentage of exam scores that are at least 70? To determine the
                    answer, we need to:
      - Add together the relative frequencies for the intervals that have scores of at
                        least 70 or above. Thus, would need to add together the relative frequencies
                        from [70-80), [80-90), and [90-100] = .33+.13+.07 = .53.
      - To get the percentage, need to multiple the calculated relative frequency by
                        100. In this case, it would be .53*100 = 53 or 53%.
```

##### 

Here is the table from above, use it to answer the question.

| Score | Count |
| --- | --- |
| [40–50) | 1 |
| [50–60) | 2 |
| [60–70) | 4 |
| [70–80) | 5 |
| [80–90) | 2 |
| [90–100] | 1 |

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comments

1. It is very important that each observation be counted only in one interval. For the
              most part, it is clear which interval an observation falls in. However, in our
              example, we needed to decide whether to include 60 in the interval 50–60, or the
              interval 60–70, and we chose to count it in the latter. In fact, this decision is
              captured by the way we wrote the intervals. If you scroll up and look at the table,
              you'll see that we wrote the intervals in a peculiar way: [40–50), [50,60), [60,70),
              and so on. The square bracket means "including," and the parenthesis means "not
              including." For example, [50,60) is the interval from 50 to 60, including 50 and not
              including 60; [60,70) is the interval from 60 to 70, including 60, and not including
              70. It does not matter how you decide to set up your intervals as long as you're
              consistent.
2. When data are displayed in a histogram, some information is lost. Note that by
              looking at the histogram we *can* answer: "How many students
              scored 70 or above?" (5 + 2 + 1 = 8) But we *cannot* answer:
              "What was the lowest score?" All we can say is that the lowest score is somewhere
              between 40 and 50, and therefore we can approximate that it is around 45.
3. Obviously, we could have chosen to break the data into intervals differently (for
              example, 45–50, 50–55, 55–60). To see how our choice of bins or intervals affects the histogram, you can use the
              html activity below that lets you change the intervals dynamically. Try changing the
              bin width by dragging the slider underneath the bin width scale.

```{note}
    **Many Students Wonder**

    Histogram

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
