# The Scatterplot: Displaying Two Quantitative Variables

In the previous two cases we had a categorical explanatory variable, and therefore exploring the relationship between the two variables was done by comparing the distribution of the response variable for each category of the explanatory variable:

- In case C→Q we compared distributions of the quantitative response.
- In case C→C we compared distributions of the categorical response.

Case Q→Q is different in the sense that both variables (in particular the explanatory variable) are quantitative, and therefore, as you'll discover, this case will require a different kind of treatment and tools. Let's start with an example:

::::{admonition} Example: Highway Signs
:class: tip

A Pennsylvania research firm conducted a study in which 30 drivers (of ages 18 to 82 years old) were sampled, and for each one, the maximum distance (in feet) at which he/she could read a newly designed sign was determined. The goal of this study was to explore the relationship between a driver's *age* and the *maximum distance* at which signs were legible, and then use the study's findings to improve safety for older drivers. (Reference: Utts and Heckard, *Mind on Statistics* (2002). Original source: Data collected by Last Resource, Inc, Bellefonte, PA.)

Since the purpose of this study is to explore the effect of age on maximum legibility distance,

- the *explanatory* variable is *Age*, and
- the *response* variable is *Distance*.

Here is what the raw data look like:

| Driver | Age | Distance |
| --- | --- | --- |
| driver 1 | 18 | 510 |
| driver 2 | 32 | 410 |
| driver 3 | 55 | 420 |
| ... | ... | ... |
| driver 30 | 82 | 360 |

Note that the data structure is such that for each individual (in this case driver 1 ... driver 30) we have a pair of values (in this case representing the driver's age and distance). We can therefore think about these data as 30 pairs of values: (18, 510), (32, 410), (55, 420), ... , (82, 360).

The first step in exploring the relationship between driver age and sign legibility distance is to create an appropriate and informative graphical display. The appropriate graphical display for examining the relationship between two quantitative variables is the {term}`scatterplot`.

To create a scatterplot, each pair of values is plotted, so that the value of the explanatory variable (X) is plotted on the horizontal axis, and the value of the response variable (Y) is plotted on the vertical axis. In other words, each individual (driver, in our example) appears on the scatterplot as a single point whose X-coordinate is the value of the explanatory variable for that individual, and whose Y-coordinate is the value of the response variable. Here is the completed scatterplot, with the point for driver 1—an 18-year-old who could read the sign from 510 feet—highlighted:

```{figure} images/gen/m05-signs-scatterplot.svg
:alt: A scatterplot with driver age on the horizontal axis, from 18 to 82, and sign legibility distance in feet on the vertical axis, from about 280 to 590. Each of the 30 drivers appears as a dot. The highlighted red point at age 18 and distance 510 represents driver 1. The cloud of points drifts downward from left to right, showing that older drivers tend to have shorter legibility distances.
```
::::

```{admonition} Comment
:class: important

It is important to mention again that when creating a scatterplot, the explanatory variable should always be plotted on the horizontal X-axis, and the response variable should be plotted on the vertical Y-axis. If in a specific example we do not have a clear distinction between explanatory and response variables, each of the variables can be plotted on either axis.
```
