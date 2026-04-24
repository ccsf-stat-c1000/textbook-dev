# Scatterplot (4 of 5)

```{admonition} Learning Objectives
    - Graphically display the relationship between two quantitative variables and describe: a) the overall pattern, and b) striking deviations from the pattern.
```

We will now look at two more examples:

```{admonition} Example: Average Gestation Period
    The average gestation period, or time of pregnancy, of an animal is closely related to its longevity (the length of its lifespan.) Data on the average gestation period and longevity (in captivity) of 40 different species of animals have been examined, with the purpose of examining how the gestation period of an animal is related to (or can be predicted from) its longevity. (Source: Rossman and Chance. (2001). Workshop statistics: Discovery with data and Minitab. Original source: The 1993 world almanac and book of facts).

    Here is the scatterplot of the data.

    ```{figure} images/scatterplot17.gif
    :alt: A scatterplot in which the vertical axis is labeled "Gestation (days)" and it ranges from 0 to 700 days. The horizontal axis is labeled "Longevity (years)" and it ranges from 0 to 40 years.

    A scatterplot in which the vertical axis is labeled "Gestation (days)" and it ranges from 0 to 700 days. The horizontal axis is labeled "Longevity (years)" and it ranges from 0 to 40 years.
    ```

    What can we learn about the relationship from the scatterplot? The direction of the relationship is *positive*, which means that animals with longer life spans tend to have longer times of pregnancy (this makes intuitive sense). An arrow drawn over the scatterplot below illustrates this:

    ```{figure} images/scatterplot18.gif
    :alt: The same scatterplot with a line and arrow drawn from the lower left to the upper right corners of the plot. Every point of data is confined to x≤26 and y≤500, but there is one point at roughly x=40 and y=650 which is an outlier. There are also two red vertical lines at x=5 and x=12 which will be explained.

    The same scatterplot with a line and arrow drawn from the lower left to the upper right corners of the plot. Every point of data is confined to x≤26 and y≤500, but there is one point at roughly x=40 and y=650 which is an outlier. There are also two red vertical lines at x=5 and x=12 which will be explained.
    ```

    The form of the relationship is again essentially *linear*. There appears to be *one outlier*, indicating an animal with an exceptionally long longevity and gestation period. (This animal happens to be the elephant.) Note that while this outlier definitely deviates from the rest of the data in term of its magnitude, it *does* follow the direction of the data.

    *Comment:* Another feature of the scatterplot that is worth observing is how the variation in gestation increases as longevity increases. This fact is illustrated by the two red vertical lines at the bottom left part of the graph. Note that the gestation periods for animals who live 5 years range from about 30 days up to about 120 days. On the other hand, the gestation period of animals who live 12 years varies much more, and ranges from about 60 days up to more than400 days.
```

```{admonition} Example: Fuel Usage
    As a third example, consider the relationship between the average amount of fuel used (in liters) to drive a fixed distance in a car (100 kilometers), and the speed at which the car is driven (in kilometers per hour). (Source: Moore and McCabe, (2003). Introduction to the practice of statistics. Original source: T.N. Lam. (1985). "Estimating fuel consumption for engine size," Journal of Transportation Engineering, vol. 111)

    ```{figure} images/scatterplot19.gif
    :alt: A scatterplot of fuel usage in relation to speed. The vertical axis is labeled "Fuel Used (liters/100km)" and the Horizontal axis is labeled "Speed (km/h)"

    A scatterplot of fuel usage in relation to speed. The vertical axis is labeled "Fuel Used (liters/100km)" and the Horizontal axis is labeled "Speed (km/h)"
    ```

    The data describe a relationship that decreases and then increases—the amount of fuel consumed decreases rapidly to a minimum for a car driving 60 kilometers per hour, and then increases gradually for speeds exceeding 60 kilometers per hour. This suggests that the speed at which a car economizes on fuel the most is about 60 km/h. This forms a curvilinear relationship that seems to be very strong, as the observations seem to perfectly fit the curve. Finally, there do not appear to be any outliers.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

The example in the last activity provides a great opportunity for interpretation of the form of the relationship in context. Recall that the example examined how the percentage of participants who completed a survey is affected by the monetary incentive that researchers promised to participants. Here again is the scatterplot that displays the relationship:

```{figure} images/scatterplot25.gif
:alt: A scatterplot. The vertical axis is labeled "Percentage Returned" and the Horizontal Axis is labeled "Incentive (dollars)" The shown data closely follows a curved line which grows more quickly at lower values of dollars.

A scatterplot. The vertical axis is labeled "Percentage Returned" and the Horizontal Axis is labeled "Incentive (dollars)" The shown data closely follows a curved line which grows more quickly at lower values of dollars.
```

The positive relationship definitely makes sense in context, but what is the interpretation of the curvilinear form in the context of the problem? How can we explain (in context) the fact that the relationship seems at first to be increasing very rapidly, but then slows down? The following graph will help us:

```{figure} images/scatterplot26.gif
:alt: The same scatterplot, except that some boxes have been drawn. The first box encompasses the area of the plot from x=0,y=0 to x=0,y=16. x=0,y=16 is the location of the first data point, showing that when the incentive is $0, the return rate is 16%. The next box encompasses the are from x=0,y=0 to x=10,y=43. This shows that when the incentive is $10, the return rate is 43%. The next box is the area between x=0,y=0 and x=30,y=54. The last box is from x=0,y=0 to x=40,y=57.

The same scatterplot, except that some boxes have been drawn. The first box encompasses the area of the plot from x=0,y=0 to x=0,y=16. x=0,y=16 is the location of the first data point, showing that when the incentive is $0, the return rate is 16%. The next box encompasses the are from x=0,y=0 to x=10,y=43. This shows that when the incentive is $10, the return rate is 43%. The next box is the area between x=0,y=0 and x=30,y=54. The last box is from x=0,y=0 to x=40,y=57.
```

Note that when the monetary incentive increases from $0 to $10, the percentage of returned surveys increases sharply—an increase of 27% (from 16% to 43%). However, the same increase of $10 from $30 to $40 doesn't result in the same dramatic increase in the percentage of returned surveys—it results in an increase of only 3% (from 54% to 57%). The form displays the phenomenon of "diminishing returns"—a return rate that after a certain point fails to increase proportionately to additional outlays of investment. $10 is worth more to people relative to $0 than it is relative to $30.
