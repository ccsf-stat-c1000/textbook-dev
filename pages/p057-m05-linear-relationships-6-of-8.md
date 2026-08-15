# Least Squares: Finding the Best-Fitting Line

The technique that specifies the dependence of the response variable on the explanatory variable is called *regression*. When that dependence is linear (which is the case in our examples in this section), the technique is called *linear regression*. Linear regression is therefore the technique of finding the line that best fits the pattern of the linear relationship (or in other words, the line that best describes how the response variable linearly depends on the explanatory variable).

To understand how such a line is chosen, consider the following very simplified version of the age-distance example (we left just 6 of the drivers on the scatterplot). There are many lines that look like they would be good candidates to be the line that best fits the data:

```{figure} images/gen/m05-candidate-lines.svg
:alt: A scatterplot of six data points with three different candidate lines drawn through them: a solid red line and two dashed lines with different slopes. All three look like plausible summaries of the downward linear pattern.
```

It is doubtful that everyone would select the same line in the plot above. We need to agree on what we mean by "best fits the data"; in other words, we need to agree on a criterion by which we would select this line. We want the line we choose to be close to the data points. In other words, whatever criterion we choose, it had better somehow take into account the vertical deviations of the data points from the line, which are marked in blue in the plot below:

```{figure} images/gen/m05-vertical-deviations.svg
:alt: The six data points with a single red line through them. At each point a thick blue vertical segment connects the point to the line, showing the vertical deviation of the point from the line. Some points are above the line and some below.
```

The most commonly used criterion is called the *least squares* criterion. This criterion says: Among all the lines that look good on your data, choose the one that has the smallest sum of squared vertical deviations. Visually, each squared deviation is represented by the area of one of the squares in the plot below. Therefore, we are looking for the line that will have the smallest total yellow area:

```{figure} images/gen/m05-squared-deviations.svg
:alt: The six data points and red line again, but now each vertical deviation has been turned into a yellow square whose side length equals the deviation. The least squares criterion chooses the line that minimizes the total area of these squares.
```

This line is called the *least-squares regression line*, and, as we'll see, it fits the linear pattern of the data very well.

## Algebra Review: The Equation of a Line

For the remainder of this lesson, you'll need to feel comfortable with the algebra of a straight line. In particular you'll need to be familiar with the {term}`slope` and the {term}`intercept` in the equation of a line, and their interpretation.

```{admonition} Review: Slope and Intercept
:class: note

A (non-vertical) line can be written as $Y = a + bX$, where:

- $a$ is the {term}`intercept`: the value of Y when $X = 0$ (where the line crosses the Y-axis).
- $b$ is the {term}`slope`: the amount Y changes when X increases by 1 unit. A positive slope means the line rises from left to right; a negative slope means it falls.

For example, the line $Y = 5 + 2X$ crosses the Y-axis at 5, and each 1-unit increase in X raises Y by 2. The line $Y = 100 - 3X$ starts at 100 and drops 3 units of Y for each unit of X.
```
