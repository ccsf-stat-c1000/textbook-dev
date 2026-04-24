# Linear Relationships (7 of 8)

```{admonition} Learning Objectives
    - In the special case of linear relationship, use the least squares regression line as a summary of the overall pattern, and use it to make predictions.
```

Like any other line, the equation of the least-squares regression line for summarizing the linear relationship between the response variable(Y) and the explanatory variable (X) has the form: $Y = a + bX$

All we need to do is calculate the intercept *a*, and the slope *b*, which is easily done if we know:

- $\bar{X}$—the mean of the explanatory variable's values
- S~X~—the standard deviation of the explanatory variable's values
- $\bar{Y}$—the mean of the response variable's values
- S~Y~—the standard deviation of the response variable's values
- r—the correlation coefficient

Given the five quantities above, the slope and intercept of the least squares regression line are found using the following formulas:

- $b = r \left(\frac{S_{Y}}{S_{X}}\right)$
- $a = \bar{Y} −b\bar{X}$

## Comments

1. Note that since the formula for the intercept *a* depends on the value of the slope, *b*, you need to find *b* first.
2. The slope of the least squares regression line can be interpreted as the average change in the response variable when the explanatory variable increases by 1 unit.

```{admonition} Example: Age-Distance
    Let's revisit our age-distance example, and find the *least-squares regression line*. The following output will be helpful in getting the 5 values we need:

    RStatCrunchMinitabExcel 2007Excel 2003TI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. The *slope*of the line is: $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$. This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 423 - (-3 * 51) = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)Dependent Varialbe: Distance Independent Variable: AgeR (correlation coefficient)= -0.7929The *slope*of the line is: $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$. This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 423 - (-3 * 51) = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)The *slope*of the line is: $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$. This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 423 - (-3 * 51) = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)The *slope*of the line is: $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$. This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 423 - (-3 * 51) = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)The *slope*of the line is: $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$. This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 423 - (-3 * 51) = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)The *slope*of the line is: b = -3 This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is: a = 576 and therefore the *least squares regression line*for this example is: Distance = 576 + (- 3 * Age)The *slope*of the line is $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$ . This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is $a=423-(-3\times51)=576$ and therefore the *least-squares regression line* for this example is Distance = 576 + (−3 * Age)The *slope*of the line is $b = \left(−0.793\right) \times \left(\frac{82.8}{21.78}\right) = −3$ . This means that for every 1-unit increase of the explanatory variable, there is, on average, a 3-unit decrease in the response variable. The interpretation *in context* of the slope being -3 is, therefore: For every year a driver gets older, the maximum distance at which he/she can read a sign decreases, *on average*, by 3 feet. The *intercept* of the line is $a=423-(-3\times51)=576$ and therefore the *least-squares regression line* for this example is Distance = 576 + (−3 * Age)

    Here is the regression line plotted on the scatterplot: As we can see, the regression line fits the linear pattern of the data quite well.
```

## Comment

As we mentioned before, hand-calculation is not the focus of this course. We wanted you to see one example in which the least squares regression line is calculated by hand, but in general we'll let a statistics package do that for us.
