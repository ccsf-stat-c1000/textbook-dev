# Case Q→Q (3 of 3)

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
```

So far the researchers have observed linearity in the data, and based on a test concluded that this linear relationship between age and legibility distance can be generalized to the entire population of drivers.

Since that is the case, the researchers would now like to estimate the equation of the straight line that governs the linear relationship between age and legibility distance among drivers. As we commented earlier, this is done by finding the line that best fits the pattern of our observed data. Recall that this line is called the *least squares regression line*—the line that minimizes the sum of the squared vertical deviations of the points from the line.

In the Exploratory Data Analysis unit, we presented the actual formulas for the slope and intercept of the line. We are not going to repeat those here; we will obtain the values from software output:

| Regression analysis: Distance vs. Age | | | | |
| --- | --- | --- | --- | --- |
| **Predictor** | **Coef** | **SE Coef** | **T** | **P** |
| Constant | 576.68 | 23.47 | 24.57 | 0.000 |
| Age | −3.0068 | 0.4243 | −7.09 | 0.000 |

The regression equation is Distance = 577 − 3.01 × Age (with R-sq = 64.2%).

Plotting the line on the scatterplot shows that it fits the data well:

```{figure} images/gen/m05-signs-regression.svg
:alt: The scatterplot of legibility distance versus age with the least squares regression line drawn through it. The negative linear pattern in the points is approximated well by the line.
```

Based on the observed data, the researchers conclude that the linear relationship between age and legibility distance among drivers can be summarized with the line:

$$\text{Distance} = 576.7 - 3.007 \times \text{Age}$$

In particular, the slope of the line is roughly −3, which means that for every year that a driver gets older (a 1-unit increase in X), the maximum legibility distance is reduced, on average, by 3 feet (Y changes by the value of the slope).

The researchers can also use this line to make predictions, remembering to beware of *extrapolation* (predictions for X values that are outside the range of the original data). For example, using the equation of the line, we predict that the maximum legibility distance of a 60-year-old driver is:

$$\text{Distance} = 576.7 - 3.007(60) \approx 396.3 \text{ feet}$$

To summarize all that the researchers have done: they asked how legibility distance (Y) is related to age (X) in the population of all drivers; took a random sample of 30 drivers; observed a linear pattern in the scatterplot with r = −0.8; concluded via the t-test that the evidence of a linear relationship is strong enough to generalize to the population; and estimated the line that governs the relationship in the population to be Distance = 577 − 3 × Age.

## Learn By Doing

:::{quiz} Using the regression line Distance = 576.7 − 3.007 × Age, what is the predicted maximum legibility distance for a 40-year-old driver?
:hint: Substitute Age = 40 into the equation.
:feedback-0: Correct! 576.7 − 3.007(40) = 576.7 − 120.3 ≈ 456 feet.
:feedback-1: Remember to multiply the slope by 40 before subtracting: 3.007 × 40 ≈ 120.
:feedback-2: The prediction requires substituting the age into the full equation.
* *About 456 feet
* About 574 feet
* About 120 feet
:::

:::{quiz} Why would it be inappropriate to use this line to predict the legibility distance of a 10-year-old?
:hint: The drivers in the study ranged in age from 18 to 82.
:feedback-0: Correct! Age 10 is outside the range of the data (18-82); the linear pattern may not hold there, so this would be extrapolation.
:feedback-1: The math produces a number, but there is no evidence the relationship holds outside the observed age range (and 10-year-olds don't drive!).
:feedback-2: The problem isn't the sign of the prediction—it's that 10 lies outside the observed range of X.
* *Age 10 lies outside the range of the observed data—the prediction would be an extrapolation
* The equation cannot be evaluated at age 10
* The predicted distance would be negative
:::

:::{quiz} A classmate interprets the slope by saying "a 50-year-old driver reads signs exactly 3 feet closer than a 49-year-old driver." What is wrong with this statement?
:hint: The slope describes an average pattern, not a rule for individuals.
:feedback-0: Correct! The slope describes the AVERAGE change in legibility distance per year of age across the population—individual drivers vary around the line.
:feedback-1: The slope's magnitude (about 3) is right; the problem is claiming it applies exactly to every individual.
* *The slope describes an average change, not an exact change for every individual driver
* The slope is actually 30 feet per year
:::
