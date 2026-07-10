# Linear Relationships (3 of 8)

```{admonition} Learning Objectives
:class: note

- Interpret the value of the correlation coefficient, and be aware of its limitations as a numerical measure of the association between two quantitative variables.
```

Now that we understand the use of *r* as a numerical measure for assessing the direction and strength of linear relationships between quantitative variables, we will look at a few examples.

::::{admonition} Example: Highway Sign Visibility
:class: tip

Earlier, we used the scatterplot below to find a *negative linear* relationship between the age of a driver and the maximum distance at which a highway sign was legible. What about the strength of the relationship? It turns out that the correlation between the two variables is r = −0.793.

```{figure} images/gen/m05-signs-scatterplot.svg
:alt: The scatterplot of driver age against sign legibility distance for the 30 drivers, showing a moderately strong negative linear pattern.
```

Since r < 0, it confirms that the direction of the relationship is negative (although we really didn't need r to tell us that). Since *r* is relatively close to −1, it suggests that the relationship is moderately strong. In context, the negative correlation confirms that the maximum distance at which a sign is legible generally decreases with age. Since the value of r indicates that the linear relationship is moderately strong, but not perfect, we can expect the maximum distance to vary somewhat, even among drivers of the same age.
::::

::::{admonition} Example: Statistics Courses
:class: tip

A statistics department is interested in tracking the progress of its students from entry until graduation. As part of the study, the department tabulates the performance of 10 students in an introductory course and in an upper-level course required for graduation. What is the relationship between the students' course averages in the two courses? Here is the scatterplot for the data:

```{figure} images/gen/m05-courses-scatterplot.svg
:alt: A scatterplot of introductory course average against upper-level course average for 10 students. The points rise steadily from lower left to upper right and cluster tightly around a line, with the correlation labeled r equals 0.931.
```

The scatterplot suggests a relationship that is *positive* in direction, *linear* in form, and seems quite strong. The value of the correlation that we find between the two variables is *r* = 0.931, which is very close to 1, and thus confirms that indeed the linear relationship is very strong.
::::

## Comment

Note that in both examples we supplemented the scatterplot with the correlation (r). Now that we have the correlation (r), why do we still need to look at a scatterplot when examining the relationship between two quantitative variables?

The *correlation* coefficient can *only* be interpreted as the *measure of the strength of a linear relationship*, so we need the scatterplot to verify that the relationship indeed looks linear. This point and its importance will be clearer after we examine a few properties of r.

## Concept Check

:::{quiz} A researcher finds r = −0.85 between the number of hours of television watched per day and score on a reading test. Which interpretation is correct?
:hint: Consider both the sign and the magnitude of r.
:feedback-0: Correct! The negative sign means reading scores tend to decrease as television hours increase, and 0.85 is close to 1, indicating a fairly strong linear relationship.
:feedback-1: The magnitude 0.85 indicates a strong relationship, not a weak one—strength is judged by distance from 0.
:feedback-2: The sign of r gives the direction: negative r means the variables move in opposite directions.
* *There is a fairly strong negative linear relationship: more TV time is associated with lower reading scores
* The relationship is weak because r is negative
* There is a strong positive relationship between TV time and reading scores
:::

:::{quiz} For a dataset, r = 0.05. Can we conclude there is no relationship at all between the two variables?
:hint: What kind of relationship does r measure?
:feedback-0: r near 0 rules out only a linear relationship—not any relationship.
:feedback-1: Correct! r measures only linear relationships. The variables could still have a strong curvilinear relationship, which is why we must also look at the scatterplot.
:feedback-2: A small r does not need to be negative to indicate weak linear association.
* Yes—r near 0 means the variables are unrelated
* *No—r only measures linear relationships; a strong curved relationship could still exist
* Yes, as long as r is positive
:::
