# Why Eyes Aren't Enough: The Case for Measuring Correlation

## Introduction

So far we have visualized relationships between two quantitative variables using scatterplots, and described the overall pattern of a relationship by considering its direction, form, and strength. We noted that assessing the strength of a relationship just by looking at the scatterplot is quite difficult, and therefore we need to supplement the scatterplot with some kind of numerical measure that will help us assess the strength.

In this part, we will restrict our attention to the *special case of relationships that have a linear form*, since they are quite common and relatively simple to detect. More importantly, there exists a numerical measure that assesses the strength of the linear relationship between two quantitative variables with which we can supplement the scatterplot. We will introduce this numerical measure here and discuss it in detail.

Even though from this point on we are going to focus only on linear relationships, it is important to remember that *not every relationship between two quantitative variables has a linear form.* We have actually seen several examples of relationships that are not linear. The statistical tools that will be introduced here are *appropriate only for examining linear relationships,* and as we will see, when they are used in nonlinear situations, these tools can lead to errors in reasoning.

Let's start with a motivating example. Consider the following two scatterplots.

```{figure} images/gen/m05-scale-illusion.svg
:alt: Two scatterplots displaying exactly the same data. In Plot A the axes span only the range of the data, so the points fill the plotting area and the scatter around the line is easy to see. In Plot B the axes span a much wider range, so the same points are squeezed together and appear to follow the line much more tightly.
```

We can see that in both cases, the direction of the relationship is *positive* and the form of the relationship is *linear*. What about the strength? Recall that the strength of a relationship is the extent to which the data follow its form.

## Check Your Understanding: How Scaling Affects a Scatterplot

:::{quiz} The two scatterplots above display the same 12 data points, yet Plot B appears to show a much stronger relationship than Plot A. What is the correct conclusion?
:hint: The data haven't changed—only the axis scales have.
:feedback-0: The underlying relationship is identical in both plots; only the display changed.
:feedback-1: Correct! Visual impressions of strength depend on the plotting scale, which is exactly why we need a numerical measure of strength.
:feedback-2: Plot A isn't wrong—both plots are legitimate displays of the same data. The problem is relying on visual impressions alone.
* The relationship really is stronger in Plot B
* *Judging strength by eye is unreliable, because it depends on the axis scales—we need a numerical measure
* Plot A must contain a plotting error
:::

The purpose of this example was to illustrate how assessing the strength of the linear relationship from a scatterplot alone is problematic, since our judgment might be affected by the scale on which the values are plotted. This example, therefore, provides a motivation for the *need* to supplement the scatterplot with a *numerical measure* that will *measure the strength* of the linear relationship between two quantitative variables.
