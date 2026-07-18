# The Normal Distribution: Shape, Center, and Spread

```{admonition} Learning Objectives
:class: note

- Find probabilities associated with the normal distribution.
```

In the Exploratory Data Analysis unit of this course, we encountered data sets, *such as lengths of human pregnancies*, whose distributions naturally followed a symmetric unimodal bell shape, bulging in the middle and tapering off at the ends.

```{figure} images/gen/m11-foot-density.svg
:alt: A symmetric, unimodal, bell-shaped density curve.
```

Many variables, such as pregnancy lengths, shoe sizes, foot lengths, and other human physical characteristics exhibit these properties: symmetry indicates that the variable is just as likely to take a value a certain distance below its mean as it is to take a value that same distance above its mean; the bell-shape indicates that values closer to the mean are more likely, and it becomes increasingly unlikely to take values far from the mean in either direction. The particular shape exhibited by these variables has been studied since the early part of the nineteenth century, when they were first called "normal" as a way of suggesting their depiction of a common, natural pattern.

## Observations of Normal Distributions

There are many normal distributions. Even though all of them have the bell-shape, they vary in their center and spread:

```{figure} images/gen/m11-normal-curves.svg
:alt: Three normal curves. A black curve and a red curve are both centered at 10, but the red curve is flatter and more spread out, indicating a larger standard deviation. A green curve has the same shape and spread as the black curve but is centered at 14.
```

More specifically, the center of the distribution is determined by its *mean* ($\mu$) and the spread is determined by its standard deviation ($\sigma$).

Some observations we can make as we look at this graph are:

- The black and the red normal curves have means or centers at $\mu$ = 10. However, the red curve is more spread out and thus has a larger standard deviation. As you look at these two normal curves, notice that as the red graph is squished down, the spread gets larger, thus allowing the area under the curve to remain the same.
- The black and the green normal curves have the same standard deviation or spread, but different centers—the green curve is centered 4 units to the right.

Even more important than the fact that many variables themselves follow the normal curve is the role played by the normal curve in sampling theory, as we'll see in the next module of probability. Understanding the normal distribution is an important step in the direction of our overall goal, which is to relate sample means or proportions to population means or proportions. The goal of this section is to better understand normal random variables and their distributions.

## Check Your Understanding: The Normal Distribution

:::{quiz} Two normal curves are drawn on the same axes. Curve A is tall and narrow; curve B is short and wide. Both are centered at 50. Which statement is correct?
:hint: Spread is controlled by σ; total area is always 1.
:feedback-0: Correct! Both have μ = 50, but B's larger σ spreads its (fixed, total = 1) area over a wider range, forcing the peak lower.
:feedback-1: Both curves, like all density curves, have total area 1.
:feedback-2: The taller curve has the SMALLER standard deviation—its values cluster tightly near the mean.
* *They share the same mean, but curve B has a larger standard deviation
* Curve A has more total area under it
* Curve A has a larger standard deviation
:::
