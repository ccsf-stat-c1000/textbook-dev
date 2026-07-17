# The Regression Line in Action: Slope, Intercept, and Prediction

```{admonition} Learning Objectives
:class: note

- In the special case of linear relationship, use the least squares regression line as a summary of the overall pattern, and use it to make predictions.
```

Like any other line, the equation of the least-squares regression line for summarizing the linear relationship between the response variable (Y) and the explanatory variable (X) has the form: $Y = a + bX$

All we need to do is calculate the intercept *a*, and the slope *b*, which is easily done if we know:

- $\bar{X}$—the mean of the explanatory variable's values
- $S_X$—the standard deviation of the explanatory variable's values
- $\bar{Y}$—the mean of the response variable's values
- $S_Y$—the standard deviation of the response variable's values
- r—the correlation coefficient

Given the five quantities above, the slope and intercept of the least squares regression line are found using the following formulas:

$$b = r \left(\frac{S_{Y}}{S_{X}}\right) \qquad\qquad a = \bar{Y} - b\bar{X}$$

```{admonition} Comments
:class: important

1. Note that since the formula for the intercept *a* depends on the value of the slope, *b*, you need to find *b* first.
2. The slope of the least squares regression line can be interpreted as the average change in the response variable when the explanatory variable increases by 1 unit.
```

::::{admonition} Example: Age-Distance
:class: tip

Let's revisit our age-distance example, and find the *least-squares regression line*. The summary statistics below (produced with statistical software) give us the five values we need:

| Quantity | Age (X) | Distance (Y) |
| --- | --- | --- |
| mean | $\bar{X} = 51$ | $\bar{Y} = 423$ |
| standard deviation | $S_X = 21.78$ | $S_Y = 82.8$ |
| correlation | r = −0.793 | |

The *slope* of the line is:

$$b = (-0.793) \times \left(\frac{82.8}{21.78}\right) = -3$$

This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being −3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet.

The *intercept* of the line is:

$$a = 423 - (-3 \times 51) = 576$$

and therefore the *least-squares regression line* for this example is:

$$Distance = 576 - 3 \times Age$$

Here is the regression line plotted on the scatterplot:

```{figure} images/gen/m05-signs-regression.svg
:alt: The scatterplot of driver age against sign legibility distance with the least-squares regression line, Distance equals 576 minus 3 times Age, drawn through the data. The line fits the downward linear pattern of the points well.
```

As we can see, the regression line fits the linear pattern of the data quite well.
::::

```{admonition} Comment
:class: important

As we mentioned before, hand-calculation is not the focus of this course. We wanted you to see one example in which the least squares regression line is calculated by hand, but in general we'll let statistical software or a calculator do that for us.
```

## Concept Check

:::{quiz} A regression line for predicting exam score from hours studied is Score = 42 + 5.5(Hours). What is the correct interpretation of the slope?
:hint: The slope is the average change in the response for a 1-unit increase in the explanatory variable.
:feedback-0: Correct! Each additional hour of study is associated, on average, with a 5.5-point increase in exam score.
:feedback-1: 42 is the intercept—the predicted score for a student who studied 0 hours.
:feedback-2: The slope describes an average change, not a guarantee for each individual student.
* *On average, each additional hour studied is associated with 5.5 more points on the exam
* A student who studies 1 hour is predicted to score 42
* Every student who studies one more hour will score exactly 5.5 points higher
:::

:::{quiz} Using the age-distance regression line Distance = 576 − 3(Age), what is the predicted legibility distance for a 40-year-old driver?
:hint: Substitute Age = 40 into the equation.
:feedback-0: Correct! 576 − 3(40) = 576 − 120 = 456 feet.
:feedback-1: Check the arithmetic: 3 × 40 = 120, and 576 − 120 = 456.
:feedback-2: Remember to multiply the age by the slope before subtracting.
* *456 feet
* 476 feet
* 536 feet
:::
