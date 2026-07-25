# Cautions About Correlation: Linearity, Units, and Outliers

## Properties of r

We now discuss and illustrate several important properties of the correlation coefficient as a numerical measure of the strength of a linear relationship.

### 1. The correlation does not change when the units of measurement change

If we change the units of measurement of the explanatory variable and/or the response variable, the change has *no effect on the correlation (r)*. To illustrate, following are two versions of the scatterplot of the relationship between sign legibility distance and driver's age:

```{figure} images/gen/m05-signs-units.svg
:alt: Two scatterplots of the same negative linear relationship between driver age and sign legibility distance. In the left plot the distances are measured in feet; in the right plot the same distances are measured in meters. The pattern of points is identical and the correlation is negative 0.793 in both plots.
```

The first scatterplot displays the original data where the maximum distance is measured in *feet*. The second scatterplot displays the same relationship but with maximum distances changed to *meters*. Notice that the Y-values have changed, but the correlations are the same. This example illustrates how changing the units of measurement of the response variable has no effect on r, but as we indicated above, the same is true for changing the units of the explanatory variable, or of both variables. This might be a good place to comment that the correlation (r) is *unitless*. It is just a number.

### 2. The correlation measures only the strength of a linear relationship

The correlation *ignores* any other type of relationship, no matter how strong it is. For example, consider the relationship between the average fuel usage of driving a fixed distance in a car, and the speed at which the car drives:

```{figure} images/gen/m05-fuel-speed-scatterplot.svg
:alt: The scatterplot of speed against fuel used, in which the points fall and then rise, following a U-shaped curve very closely.
```

Our data describe a fairly simple curvilinear relationship: the amount of fuel consumed decreases rapidly to a minimum for a car driving 60 kilometers per hour, and then increases gradually for speeds exceeding 60 kilometers per hour. The relationship is very strong, as the observations seem to perfectly fit the curve. Although the relationship is strong, the correlation $r = -0.172$ indicates a weak *linear* relationship. This makes sense considering that the data fail to adhere closely to a linear form.

The correlation is useless for assessing the strength of any type of relationship that is not linear (including relationships that are curvilinear, such as the one in our example). Beware, then, of interpreting the fact that r is close to 0 as an indicator of a weak relationship rather than a weak *linear* relationship. This example also illustrates how important it is to *always look at the data in the scatterplot* because, as in our example, there might be a strong nonlinear relationship that r does not indicate.

Since the correlation was nearly zero when the form of the relationship was not linear, we might ask if the correlation can be used to determine whether or not a relationship is linear.

### 3. The correlation by itself is not sufficient to determine whether a relationship is linear

To see this, let's consider the study that examined the effect of monetary incentives on the return rate of questionnaires. Below is the scatterplot relating the percentage of participants who completed a survey to the monetary incentive that researchers promised to participants, in which we find a *strong curvilinear relationship*:

```{figure} images/gen/m05-incentive-scatterplot.svg
:alt: The scatterplot of incentive against percentage of surveys returned, in which the points rise quickly and then level off, following a curve.
```

The relationship is curvilinear, yet the correlation $r = 0.876$ is quite close to 1. In the last two examples, we have seen two very strong curvilinear relationships, one with a correlation close to 0 and one with a correlation close to 1. Therefore, the correlation alone does not indicate whether a relationship is linear. The important principle here is: *Always look at the data!*

### 4. The correlation is heavily influenced by outliers

The way in which an outlier influences the correlation depends on whether or not the outlier is consistent with the pattern of the linear relationship. The two scatterplots below illustrate the two situations:

```{figure} images/gen/m05-outlier-effect.svg
:alt: Two scatterplots of positive linear data. In the left plot, a red outlier sits in the lower right, far from the upward pattern; adding it drops the correlation from 0.99 to about 0.52. In the right plot, a red outlier sits in the far upper right, exactly along the direction of the pattern; adding it raises the correlation from about 0.71 to 0.86.
```

An outlier that is *not consistent* with the pattern of the relationship (left plot) weakens the linear pattern and can drastically *reduce* the correlation. On the other hand, an outlier that *is consistent* with the direction of the linear relationship (right plot) actually *strengthens* it, pulling the correlation closer to 1.

## Check Your Understanding: Properties of the Correlation r

:::{quiz} A dataset of 20 points has a strong positive linear pattern with $r = 0.95$. One additional point is added far below the rest of the data, well off the linear pattern. What will most likely happen to r?
:hint: Is the new point consistent with the upward pattern or not?
:feedback-0: Correct! An outlier inconsistent with the pattern weakens the linear relationship, so r decreases substantially.
:feedback-1: r would increase only if the outlier extended the existing linear pattern.
:feedback-2: The correlation is heavily influenced by outliers—a single point can change r substantially.
* *r will decrease substantially
* r will increase toward 1
* r will remain essentially unchanged
:::

:::{quiz} A researcher converts a dataset's heights from inches to centimeters and recomputes the correlation with weight. What happens to r?
:hint: Recall property 1: r is unitless.
:feedback-0: Correct! Changing units of measurement has no effect on the correlation.
:feedback-1: Multiplying a variable by a constant does not change r—only the axis labels change.
:feedback-2: The direction of the relationship doesn't change when units change.
* *Nothing—r stays exactly the same
* r increases because centimeters are larger numbers
* r changes sign
:::
