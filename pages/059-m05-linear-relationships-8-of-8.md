# Linear Relationships (8 of 8)

```{admonition} Learning Objectives
    - In the special case of linear relationship, use the least squares regression line as a summary of the overall pattern, and use it to make predictions.
```

Let's go back now to our motivating example, in which we wanted to predict the maximum distance at which a sign is legible for a 60-year-old. Now that we have found the least squares regression line, this prediction becomes quite easy:

Practically, what the figure tells us is that in order to find the predicted legibility distance for a 60-year-old, we plug Age = 60 into the regression line equation, to find that:

```
Predicted distance = 576 + (- 3 * 60) = 396
```

396 feet is our best prediction for the maximum distance at which a sign is legible for a 60-year-old.

## Did I Get This?

*Background:*A statistics department is interested in tracking the progress of its students from entry until graduation. As part of the study, the department tabulates the performance of 10 students in an introductory course and in an upper-level course required for graduation. The scatterplot below includes the least squares line (the line that best explains the upper-level course average based on the lower-level course average), and its equation:

```{figure} images/linear21.gif
:alt: The scatterplot for Introductory Course Average vs. Upper Level Course Average. In addition to the data plotted on the scatterplot, we have a least squares regression line. The line's equation is Y = -1.4 + X.

The scatterplot for Introductory Course Average vs. Upper Level Course Average. In addition to the data plotted on the scatterplot, we have a least squares regression line. The line's equation is Y = -1.4 + X.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on to the next page. If not, then click the link below for some additional practice.

```{note}
    **Did I Get This?**

    Linear Relationships: Extra Problems

    *(Interactive activity — available in the OLI platform)*
```

## Comment About Predictions

Suppose a government agency wanted to design a sign appropriate for an even wider range of drivers than were present in the original study. They want to predict the maximum distance at which the sign would be legible for a 90-year-old. Using the least squares regression line again as our summary of the linear dependence of the distances upon the drivers' ages, the agency predicts that 90-year-old drivers can see the sign at no more than 576 + (- 3 * 90) = 306 feet:

(The green segment of the line is the region of ages beyond 82, the age of the oldest individual in the study.)

```{admonition} Question & Answer
    **Question:** Is our prediction for 90-year-old drivers reliable?

    **Answer:** Our original age data ranged from 18 (youngest driver) to 82 (oldest
                            driver), and our regression line is therefore a summary of the linear
                            relationship
                                *in
                                that age range only.* When we plug the value 90
                            into the regression line equation, we are assuming that the same linear
                            relationship extends beyond the range of our age data (18-82) into the green
                            segment. *There is no justification for such an assumption.* It might
                            be the case that the vision of drivers older than 82 falls off more rapidly
                            than it does for younger drivers. (i.e., the slope changes from -3 to
                            something more negative). Our prediction for age = 90 is therefore
                                *not
                                reliable.*
```

## In General

Prediction for ranges of the explanatory variable that are not in the data is called *extrapolation*. Since there is no way of knowing whether a relationship holds beyond the range of the explanatory variable in the data, extrapolation is not reliable, and should be avoided. In our example, like most others, extrapolation can lead to very poor or illogical predictions.

```{note}
    **Learn By Doing**

    Linear Relationships

    *(Interactive activity — available in the OLI platform)*
```

## Let's Summarize

- A special case of the relationship between two quantitative variables is the *linear* relationship. In this case, a straight line simply and
                        adequately summarizes the relationship.
- When the scatterplot displays a linear relationship, we supplement it with
                        the *correlation coefficient (r)* , which measures the *strength* and
                        direction
                        of a linear relationship between two quantitative variables. The correlation
                        ranges between -1 and 1. Values near -1 indicate a strong negative linear
                        relationship, values near 0 indicate a weak linear relationship, and values
                        near 1 indicate a strong positive linear relationship.
- The correlation is only an appropriate numerical measure for linear
                        relationships, and is sensitive to outliers. Therefore, the correlation
                        should only be used as a supplement to a scatterplot (after we look at the
                        data).
- The most commonly used criterion for finding a line that summarizes the
                        pattern of a linear relationship is "least squares." The *least squares
                            regression line* has the smallest sum of squared vertical
                        deviations of the data points from the line.
- The slope of the least squares regression line can be interpreted as the
                        average change in the response variable when the explanatory variable
                        increases by 1 unit.
- The least squares regression line predicts the value of the response
                        variable for a given value of the explanatory variable. *Extrapolation* is prediction of values of the explanatory
                        variable that fall outside the range of the data. Since there is no way of
                        knowing whether a relationship holds beyond the range of the explanatory
                        variable in the data, extrapolation is not reliable, and should be
                        avoided.

## Section Questions

```{note}
    **My Response**

    About Linear Relationships

    *(Interactive activity — available in the OLI platform)*
```
