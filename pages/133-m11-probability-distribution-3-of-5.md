# Probability Distribution (3 of 5)

```{admonition} Learning Objectives
:class: note

- Find the probability distribution of discrete random variables, and use it to find the probability of events of interest.
```

In the previous two examples and activity, we needed to specify the probability distributions ourselves, based on the physical circumstances of the situation. In some situations, as in the following example, the probability distribution may be specified with an algebraic formula. Such a formula must be consistent with the constraints imposed by the laws of probability, so that the probability of each outcome must be between 0 and 1, and the probabilities of all possible outcomes together must sum to 1.

:::{admonition} Example: Formulas to Define Random Variables
:class: tip

A random variable X has a probability distribution of

*P(X = x) = (x + 2) / 25 for x = 1, 2, 3, 4, 5.*

Show the probability distribution in a table, and verify that the above requirements are satisfied.

Substituting x = 1, 2, 3, 4, and 5, respectively, into the formula for P(X = x), we have

| x | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| P(X = x) | 3/25 | 4/25 | 5/25 | 6/25 | 7/25 |

Clearly, each probability is between 0 and 1. Also, the probabilities sum to (3 + 4 + 5 + 6 + 7) / 25 = 25/25 = 1.
:::

## Probability Histograms

We learned to display the distribution of sample values for a quantitative variable with a histogram in which the horizontal axis represented the range of values in the sample. The vertical axis represented the frequency or relative frequency (sometimes given as a percentage) of sample values occurring in that interval. So the width of each rectangle in the histogram was an interval, or part of the possible values for the quantitative variable, and the height of each rectangle was the frequency (or relative frequency) for that interval.

Similarly, we can display the probability distribution of a random variable with a probability histogram. The horizontal axis represents the range of all possible values of the random variable, and the vertical axis represents the probabilities of those values.

Here is the probability histogram for the previous example:

```{figure} images/gen/m11-prob-hist-formula.svg
:alt: A probability histogram with x values 1 through 5 on the horizontal axis and probability on the vertical axis. The bars, centered on each value, have heights 3/25, 4/25, 5/25, 6/25, and 7/25, forming a staircase rising to the right.
```

## Area of a Probability Histogram

Notice that each rectangle in the histogram has a width of 1 unit. The height of each rectangle is the probability that it will occur. Thus, the area of each rectangle is base times height, which for these rectangles is 1 times its probability for each value of X. This means that the sum of the areas of all of the rectangles is the same as the sum of all of the probabilities. Therefore, the total area = 1.

## Learn By Doing

Based upon data collected in the 2000 United States Census, the following histogram was constructed. It shows the distribution of people per household:

```{figure} images/gen/m11-prob-hist-household.svg
:alt: A probability histogram of people per household. The bars have heights 0.28 for one person, 0.34 for two people, 0.18 for three, 0.14 for four, and 0.06 for five or more.
```

:::{quiz} What is the probability that a randomly chosen household has at most 2 people?
:hint: Add the probabilities for 1 and 2 people.
:feedback-0: Correct! P(X ≤ 2) = 0.28 + 0.34 = 0.62.
:feedback-1: 0.34 is only P(X = 2); "at most 2" also includes single-person households.
:feedback-2: 0.38 is P(X ≥ 3), the complement of "at most 2."
* *0.62
* 0.34
* 0.38
:::

## Did I Get This?

The probability distribution of the random variable X is represented by the following histogram:

```{figure} images/gen/m11-prob-hist-digt.svg
:alt: A probability histogram for the values 1, 2, 3, and 4 with bar heights 0.4, 0.3, 0.2, and 0.1, descending from left to right.
```

:::{quiz} What is P(X > 2)?
:hint: "Greater than 2" means X = 3 or X = 4.
:feedback-0: Correct! P(X > 2) = P(X = 3) + P(X = 4) = 0.2 + 0.1 = 0.3.
:feedback-1: 0.6 includes P(X = 2), but "greater than 2" excludes 2 itself.
:feedback-2: 0.2 is only P(X = 3).
* *0.3
* 0.6
* 0.2
:::

:::{quiz} What is P(X ≥ 2)?
:hint: This time 2 is included.
:feedback-0: Correct! P(X ≥ 2) = 0.3 + 0.2 + 0.1 = 0.6 (or 1 − P(X = 1) = 1 − 0.4).
:feedback-1: 0.3 is P(X > 2); the "≥" version includes X = 2 as well.
:feedback-2: 0.4 is P(X = 1), the complement of this event.
* *0.6
* 0.3
* 0.4
:::
