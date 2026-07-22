# The Correlation Coefficient r

## The Correlation Coefficient—r

The numerical measure that assesses the strength of a linear relationship is called the {term}`correlation coefficient` and is denoted by *r*. We will

- Define the correlation r.
- Discuss the calculation of r.
- Explain how to interpret the value of r.
- Talk about some of the properties of r.

*Definition:* The correlation coefficient (r) is a numerical measure that measures the {term}`strength` and {term}`direction` of a linear relationship between two quantitative variables.

*Calculation:* r is calculated using the following formula:

$$r=\frac{1}{n-1}\sum_{i=1}^{n}\left(\frac{x_{i}-\bar{x}}{S_{x}}\right)\left(\frac{y_{i}-\bar{y}}{S_{y}}\right)$$

However, the calculation of the correlation (r) is not the focus of this course. We will use statistical software or a calculator to compute r for us, and the emphasis of this course is on the *interpretation* of its value.

## Interpretation

Once we obtain the value of r, its interpretation with respect to the strength of linear relationships is quite simple:

- The correlation is always between −1 and 1: $-1 \le r \le 1$.
- The *sign* of r tells us the {term}`direction` of the linear relationship: positive r means a positive relationship; negative r means a negative relationship.
- The *magnitude* of r tells us the {term}`strength`: values close to −1 or 1 indicate points tightly clustered around a line (a strong linear relationship); values close to 0 indicate a weak (or no) linear relationship.
- r = 1 or r = −1 only when the points fall *exactly* on a straight line.

```{note} Video

[Interpreting the value of r](https://www.youtube.com/watch?v=Bt-Ey2ebfvs)
```

To get a better sense of how the value of r relates to the strength of the linear relationship, examine the scatterplots below, which show data with correlations ranging from 1 down to −1:

```{figure} images/gen/m05-r-values.svg
:alt: Six scatterplots arranged in a grid, labeled r equals 1, 0.7, 0.3, negative 0.3, negative 0.7, and negative 1. At r equals 1 and negative 1 the points fall exactly on a rising or falling line. At 0.7 and negative 0.7 the points cluster fairly tightly around a line. At 0.3 and negative 0.3 the points form only a loose upward or downward trend.
```

## Check Your Understanding: The Strength of a Correlation

:::{quiz} Which value of r indicates the strongest linear relationship: r = 0.6, r = −0.9, or r = 0.1?
:hint: Strength is measured by how close r is to −1 or 1, regardless of sign.
:feedback-0: 0.6 indicates a moderate relationship, but another value is closer to ±1.
:feedback-1: Correct! Strength depends on the magnitude of r; |−0.9| = 0.9 is the closest to 1, so it is the strongest (a strong negative relationship).
:feedback-2: 0.1 is close to 0, indicating a very weak linear relationship.
* r = 0.6
* *r = −0.9
* r = 0.1
:::
