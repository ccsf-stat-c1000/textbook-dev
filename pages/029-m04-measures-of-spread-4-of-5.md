# The 1.5(IQR) Rule: Flagging Suspected Outliers

```{admonition} Learning Objectives
:class: note

- Summarize and describe the distribution of a quantitative variable in context: a) describe the overall pattern, b) describe striking deviations from the pattern.
- Relate measures of center and spread to the shape of the distribution, and choose the appropriate measures in different contexts.
```

## Using the IQR to Detect Outliers

So far we have quantified the idea of center, and we are in the middle of the discussion about measuring spread, but we haven't really talked about a method or rule that will help us classify extreme observations as outliers. The IQR is used as the basis for a rule of thumb for identifying outliers.

## The 1.5(IQR) Criterion for Outliers

An observation is considered a suspected outlier if it is:

- below Q1 − 1.5(IQR) or
- above Q3 + 1.5(IQR)

The following picture illustrates this rule:

```{figure} images/gen/m04-iqr-criterion.svg
:alt: A number line with Q1, the median M, and Q3 marked in the middle. Red boundary lines mark Q1 minus 1.5 IQR on the left and Q3 plus 1.5 IQR on the right. The shaded zones beyond these boundaries are labeled suspected outliers.
```

::::{admonition} Example: Best Actress Oscar Winners
:class: tip

We will continue with the Best Actress Oscar winners example:

```
34 34 27 37 42 41 36 32 41 33 31 74 33 49 38 61 21 41 26 80 42 29
33 36 45 49 39 34 26 25 33 35 35 28 30 29 61 32 33 45 29 62 22 44
```

Recall that when we first looked at the histogram of ages of Best Actress Oscar winners, there were 5 observations that looked like possible outliers:

```{figure} images/gen/m04-oscar-outliers.svg
:alt: The histogram of winners' ages with the bars at ages 60 to 64 (three winners), 70 to 74 (one winner), and 80 to 84 (one winner) shown in red and labeled possible outliers.
```

We can now use the 1.5(IQR) criterion to check whether the 5 observations should indeed be classified as outliers:

- For this example we found that Q1 = 30.5 and Q3 = 42, so IQR = 11.5
- $Q1 - 1.5(IQR) = 30.5 - (1.5)(11.5) = 13.25$
- $Q3 + 1.5(IQR) = 42 + (1.5)(11.5) = 59.25$

The 1.5(IQR) criterion tells us that any observation that is below 13.25 or above 59.25 is considered a suspected outlier.

We therefore conclude that the observations 61, 61, 62, 74 and 80 should be flagged as suspected outliers in the distribution of ages. Note that since the smallest observation is 21, there are no suspected low outliers in this distribution.
::::

## Concept Check

:::{quiz} A dataset has Q1 = 50 and Q3 = 70. According to the 1.5(IQR) criterion, which of the following observations would be flagged as a suspected high outlier?
:hint: First find IQR = Q3 − Q1, then compute Q3 + 1.5(IQR).
:feedback-0: 95 is below the cutoff of Q3 + 1.5(IQR) = 70 + 30 = 100.
:feedback-1: Correct! IQR = 20, so the high cutoff is 70 + 1.5(20) = 100, and 105 exceeds it.
:feedback-2: 85 is well within the cutoff of 100.
* 95
* *105
* 85
:::

:::{quiz} Using the same dataset (Q1 = 50, Q3 = 70), below what value would an observation be flagged as a suspected low outlier?
:hint: Compute Q1 − 1.5(IQR).
:feedback-0: Correct! Q1 − 1.5(IQR) = 50 − 30 = 20, so observations below 20 are suspected low outliers.
:feedback-1: 50 is Q1 itself—the cutoff extends 1.5 IQRs below it.
:feedback-2: 35 would be the cutoff if you used 0.75(IQR); the criterion uses 1.5(IQR).
* *20
* 50
* 35
:::
