# Linear Relationships (8 of 8)

```{admonition} Learning Objectives
:class: note

- In the special case of linear relationship, use the least squares regression line as a summary of the overall pattern, and use it to make predictions.
```

Let's go back now to our motivating example, in which we wanted to predict the maximum distance at which a sign is legible for a 60-year-old. Now that we have found the least squares regression line, this prediction becomes quite easy:

Practically, what the regression line tells us is that in order to find the predicted legibility distance for a 60-year-old, we plug Age = 60 into the regression line equation, to find that:

$$\text{Predicted distance} = 576 - 3 \times 60 = 396$$

396 feet is our best prediction for the maximum distance at which a sign is legible for a 60-year-old.

## Did I Get This?

*Background:* A statistics department is interested in tracking the progress of its students from entry until graduation. As part of the study, the department tabulates the performance of 10 students in an introductory course and in an upper-level course required for graduation. The scatterplot below includes the least squares line (the line that best explains the upper-level course average based on the introductory course average), and its equation, Y = −1.4 + X:

```{figure} images/gen/m05-courses-regression.svg
:alt: The scatterplot of introductory course average against upper-level course average for 10 students, with the least-squares regression line Y equals negative 1.4 plus X drawn through the strongly positive linear pattern.
```

:::{quiz} Using the regression line Y = −1.4 + X, what is the predicted upper-level course average for a student whose introductory course average is 80?
:hint: Plug X = 80 into the equation.
:feedback-0: Correct! Y = −1.4 + 80 = 78.6.
:feedback-1: Remember to add the intercept: −1.4 + 80 = 78.6, not 80.
:feedback-2: The slope multiplies X; here the slope is 1, so Y = −1.4 + 80.
* *78.6
* 80
* 81.4
:::

:::{quiz} The slope of this regression line is 1. What is the correct interpretation in context?
:hint: The slope is the average change in Y for a 1-unit increase in X.
:feedback-0: Correct! On average, each additional point in the introductory course average is associated with 1 additional point in the upper-level course average.
:feedback-1: That describes the intercept's role, not the slope's.
:feedback-2: A slope of 1 does not mean the two averages are equal—the line also has an intercept of −1.4.
* *On average, a 1-point increase in the introductory average is associated with a 1-point increase in the upper-level average
* Students with an introductory average of 0 are predicted to score 1 in the upper-level course
* Every student scores exactly the same in both courses
:::

:::{quiz} A student's introductory average is 72, and the student's actual upper-level average turned out to be 74. What was the prediction error (actual minus predicted)?
:hint: First find the predicted value: −1.4 + 72.
:feedback-0: Correct! Predicted = −1.4 + 72 = 70.6, so the error is 74 − 70.6 = 3.4.
:feedback-1: −3.4 would mean the actual value was below the prediction; here the student did better than predicted.
:feedback-2: 2 is the difference between 74 and 72; compare the actual value with the predicted value, 70.6.
* *3.4
* −3.4
* 2
:::

## Comment About Predictions

Suppose a government agency wanted to design a sign appropriate for an even wider range of drivers than were present in the original study. They want to predict the maximum distance at which the sign would be legible for a 90-year-old. Using the least squares regression line again as our summary of the linear dependence of the distances upon the drivers' ages, the agency predicts that 90-year-old drivers can see the sign at no more than 576 − 3 × 90 = 306 feet:

```{figure} images/gen/m05-extrapolation.svg
:alt: The scatterplot and regression line for the age-distance data. The solid red line covers the observed ages, from 18 to 82. Beyond age 82 the line continues as a dashed green segment labeled beyond the data, indicating the region where the prediction is an extrapolation.
```

(The green segment of the line is the region of ages beyond 82, the age of the oldest individual in the study.)

:::{admonition} Question & Answer
:class: important

**Question:** Is our prediction for 90-year-old drivers reliable?

**Answer:** Our original age data ranged from 18 (youngest driver) to 82 (oldest driver), and our regression line is therefore a summary of the linear relationship *in that age range only.* When we plug the value 90 into the regression line equation, we are assuming that the same linear relationship extends beyond the range of our age data (18–82) into the green segment. *There is no justification for such an assumption.* It might be the case that the vision of drivers older than 82 falls off more rapidly than it does for younger drivers (i.e., the slope changes from −3 to something more negative). Our prediction for age = 90 is therefore *not reliable.*
:::

## In General

Prediction for ranges of the explanatory variable that are not in the data is called *extrapolation*. Since there is no way of knowing whether a relationship holds beyond the range of the explanatory variable in the data, extrapolation is not reliable, and should be avoided. In our example, like most others, extrapolation can lead to very poor or illogical predictions.

## Let's Summarize

- A special case of the relationship between two quantitative variables is the *linear* relationship. In this case, a straight line simply and adequately summarizes the relationship.
- When the scatterplot displays a linear relationship, we supplement it with the *correlation coefficient (r)*, which measures the *strength* and direction of a linear relationship between two quantitative variables. The correlation ranges between −1 and 1. Values near −1 indicate a strong negative linear relationship, values near 0 indicate a weak linear relationship, and values near 1 indicate a strong positive linear relationship.
- The correlation is only an appropriate numerical measure for linear relationships, and is sensitive to outliers. Therefore, the correlation should only be used as a supplement to a scatterplot (after we look at the data).
- The most commonly used criterion for finding a line that summarizes the pattern of a linear relationship is "least squares." The *least squares regression line* has the smallest sum of squared vertical deviations of the data points from the line.
- The slope of the least squares regression line can be interpreted as the average change in the response variable when the explanatory variable increases by 1 unit.
- The least squares regression line predicts the value of the response variable for a given value of the explanatory variable. *Extrapolation* is prediction for values of the explanatory variable that fall outside the range of the data. Since there is no way of knowing whether a relationship holds beyond the range of the explanatory variable in the data, extrapolation is not reliable, and should be avoided.
