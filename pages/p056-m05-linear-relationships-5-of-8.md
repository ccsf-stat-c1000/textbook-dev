# Summarizing a Linear Relationship with a Line

## Linear Regression: Summarizing the Pattern of the Data with a Line

So far we've used the scatterplot to describe the relationship between two quantitative variables, and in the special case of a linear relationship, we have supplemented the scatterplot with the correlation (r). The correlation, however, doesn't fully characterize the linear relationship between two quantitative variables—it only measures the strength and direction. We often want to describe more precisely how one variable changes with the other (by "more precisely," we mean more than just the direction), or *predict* the value of the response variable for a given value of the explanatory variable. In order to be able to do that, we need to summarize the linear relationship with a line that best fits the linear pattern of the data. In the remainder of this section, we will introduce a way to find such a line, learn how to interpret it, and use it (cautiously) to make predictions.

Again, let's start with a motivating example:

Earlier, we examined the linear relationship between the age of a driver and the maximum distance at which a highway sign was legible, using both a scatterplot and the correlation coefficient. Suppose a government agency wanted to predict the maximum distance at which the sign would be legible for 60-year-old drivers, and thus make sure that the sign could be used safely and effectively.

How would we make this prediction? By summarizing the downward linear pattern of the data with a line, and then using that line: to predict the legibility distance for 60-year-old drivers, we find age 60 on the line and read off the corresponding distance—about 396 feet:

```{figure} images/gen/m05-signs-regression.svg
:alt: The scatterplot of driver age against sign legibility distance with a red line drawn through the downward linear pattern of the points. Dashed green guide lines rise from age 60 on the horizontal axis up to the line and across to the vertical axis, showing a predicted distance of about 396 feet.
```

```{note} Video

[Making Predictions](https://www.youtube.com/watch?v=8hf3dMf59cI)
```

How and why did we pick this particular line (the one shown in red above) to describe the dependence of the maximum distance at which a sign is legible upon the age of a driver? What line exactly did we choose? We will return to this example once we can answer that question with a bit more precision.
