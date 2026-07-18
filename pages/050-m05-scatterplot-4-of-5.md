# Scatterplot Practice: From Gestation Periods to Fuel Economy

```{admonition} Learning Objectives
:class: note

- Graphically display the relationship between two quantitative variables and describe: a) the overall pattern, and b) striking deviations from the pattern.
```

We will now look at two more examples:

::::{admonition} Example: Average Gestation Period
:class: tip

The average gestation period, or time of pregnancy, of an animal is closely related to its longevity (the length of its lifespan). Data on the average gestation period and longevity (in captivity) of 40 different species of animals have been examined, with the purpose of examining how the gestation period of an animal is related to (or can be predicted from) its longevity. (Source: Rossman and Chance. (2001). *Workshop statistics: Discovery with data*. Original source: The 1993 world almanac and book of facts.)

Here is the scatterplot of the data.

```{figure} images/gen/m05-gestation-scatterplot.svg
:alt: A scatterplot with longevity in years on the horizontal axis, from 0 to 40, and gestation in days on the vertical axis, from 0 to about 700. The points rise from lower left to upper right. Nearly all the data lie below 26 years and 500 days, but one red point near 40 years and 650 days, the elephant, stands apart as an outlier.
```

What can we learn about the relationship from the scatterplot? The direction of the relationship is *positive*, which means that animals with longer life spans tend to have longer times of pregnancy (this makes intuitive sense). An arrow drawn over the scatterplot below illustrates this:

```{figure} images/gen/m05-gestation-scatterplot-annotated.svg
:alt: The same scatterplot with a green arrow rising from lower left to upper right showing the positive direction, and two red vertical lines: a short one at longevity 5 years, spanning gestations of about 30 to 120 days, and a much longer one at 12 years, spanning about 60 to 415 days, showing that variation in gestation increases with longevity.
```

The form of the relationship is again essentially *linear*. There appears to be *one outlier*, indicating an animal with an exceptionally long longevity and gestation period. (This animal happens to be the elephant.) Note that while this outlier definitely deviates from the rest of the data in terms of its magnitude, it *does* follow the direction of the data.

*Comment:* Another feature of the scatterplot that is worth observing is how the variation in gestation increases as longevity increases. This fact is illustrated by the two red vertical lines at the bottom left part of the graph. Note that the gestation periods for animals who live 5 years range from about 30 days up to about 120 days. On the other hand, the gestation period of animals who live 12 years varies much more, and ranges from about 60 days up to more than 400 days.
::::

::::{admonition} Example: Fuel Usage
:class: tip

As a third example, consider the relationship between the average amount of fuel used (in liters) to drive a fixed distance in a car (100 kilometers), and the speed at which the car is driven (in kilometers per hour). (Source: Moore and McCabe. (2003). *Introduction to the practice of statistics*. Original source: T.N. Lam. (1985). "Estimating fuel consumption for engine size," *Journal of Transportation Engineering*, vol. 111.)

```{figure} images/gen/m05-fuel-speed-scatterplot.svg
:alt: A scatterplot with speed in kilometers per hour on the horizontal axis and fuel used in liters per 100 kilometers on the vertical axis. The points fall rapidly from about 21 liters at low speed to a minimum near 6 liters at 60 kilometers per hour, and then rise gradually as speed increases further, forming a U-shaped curve that the points follow very closely.
```

The data describe a relationship that decreases and then increases—the amount of fuel consumed decreases rapidly to a minimum for a car driving 60 kilometers per hour, and then increases gradually for speeds exceeding 60 kilometers per hour. This suggests that the speed at which a car economizes on fuel the most is about 60 km/h. This forms a curvilinear relationship that seems to be very strong, as the observations seem to perfectly fit the curve. Finally, there do not appear to be any outliers.
::::

## Check Your Understanding: Describing a Scatterplot

A study examined how the percentage of participants who completed a survey is affected by the monetary incentive that researchers promised to participants. Here is the scatterplot displaying the relationship:

```{figure} images/gen/m05-incentive-scatterplot.svg
:alt: A scatterplot with incentive in dollars on the horizontal axis, from 0 to 40, and percentage of surveys returned on the vertical axis. The points rise steeply at first, from 16% at zero dollars to 43% at 10 dollars, and then level off, reaching 57% at 40 dollars, following a curved line that grows more quickly at lower dollar values.
```

:::{quiz} How would you describe the direction, form, and strength of the relationship between incentive and percentage returned?
:hint: Do the points rise or fall? Do they follow a line or a curve? How tightly?
:feedback-0: Correct! Higher incentives are associated with higher return rates (positive), the points follow a curve that levels off (curvilinear), and they follow it very closely (strong).
:feedback-1: Look again at the shape: the increase is steep at first and then levels off—a curve, not a line.
:feedback-2: The relationship is positive: return percentages increase as the incentive increases.
* *Positive, curvilinear, and strong
* Positive, linear, and strong
* Negative, curvilinear, and strong
:::

::::{admonition} Comment
:class: important

This example provides a great opportunity for interpretation of the form of the relationship in context. The positive relationship definitely makes sense in context, but what is the interpretation of the curvilinear form in the context of the problem? How can we explain (in context) the fact that the relationship seems at first to be increasing very rapidly, but then slows down? The following graph will help us:

```{figure} images/gen/m05-incentive-annotated.svg
:alt: The same scatterplot with dashed guide lines showing that raising the incentive from 0 to 10 dollars raises the return rate from 16% to 43%, an increase of 27 percentage points, while raising it from 30 to 40 dollars only raises the return rate from 54% to 57%, an increase of 3 percentage points.
```

Note that when the monetary incentive increases from \$0 to \$10, the percentage of returned surveys increases sharply—an increase of 27% (from 16% to 43%). However, the same increase of \$10 from \$30 to \$40 doesn't result in the same dramatic increase in the percentage of returned surveys—it results in an increase of only 3% (from 54% to 57%). The form displays the phenomenon of "diminishing returns"—a return rate that after a certain point fails to increase proportionately to additional outlays of investment. \$10 is worth more to people relative to \$0 than it is relative to \$30.
::::
