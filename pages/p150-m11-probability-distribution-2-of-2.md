# Probability as Area Under a Density Curve

Now consider another random variable X = foot length of adult males. Unlike shoe size, this variable is not limited to distinct, separate values, because foot lengths can take any value over a *continuous* range of possibilities, so we cannot present this variable with a probability histogram or a table. The probability distribution of foot length (or any other continuous random variable) can be represented by a smooth curve called a *probability density curve*:

```{figure} images/gen/m11-foot-density.svg
:alt: A bell-shaped probability density curve for male foot length, centered at 11 inches. The total area below the curve equals 1.
```

Like the modified probability histogram we saw before, the total area under the density curve equals 1, and the curve represents probabilities by area.

The probability that X gets values in any interval is represented by the area above this interval and below the density curve. In our foot length example, if our interval of interest is between 10 and 12, and we would like to know P(10 < $X < 12)$, the probability that a randomly chosen male has a foot length anywhere between 10 and 12 inches, we'll have to find the area above our interval of interest (10, 12) and below our density curve, shaded below:

```{figure} images/gen/m11-foot-shaded-10-12.svg
:alt: The foot-length density curve with the region between 10 and 12 inches shaded. The shaded area under the curve is the probability that the foot length falls between 10 and 12 inches.
```

If, for example, we are interested in P(X < 9), the probability that a randomly chosen male has a foot length of less than 9 inches, we'll have to find the area shaded below:

```{figure} images/gen/m11-foot-shaded-lt9.svg
:alt: The foot-length density curve with the region to the left of 9 inches shaded. The shaded area under the curve is the probability that the foot length is less than 9 inches.
```

```{admonition} Comments
:class: important

1. We have seen that for a *discrete* random variable like shoe size, whether we have a strict inequality or not *does matter* when solving for probabilities. In contrast, for a *continuous* random variable like foot length, the probability of a foot length of less than or equal to 9 will be the same as the probability of a foot length of strictly less than 9. In other words, $P(X<9)=P(X\leq9)$. Visually, in terms of our density curve, the area under the curve up to and including a certain point is the same as the area up to and excluding the point, because there is no area over a single point. Conceptually, because a continuous random variable has infinitely many possible values, technically the probability of any single value occurring is zero!

2. It should be clear now why the total area under any probability density curve must be 1. The total area under the curve represents P(X gets a value in the interval of its possible values). Clearly, according to the rules of probability this must be 1, or always true.

3. Density curves, like probability histograms, may have any shape imaginable as long as the total area underneath the curve is 1.
```

## Let's Summarize

The probability distribution of a continuous random variable is represented by a probability density curve. The probability that X gets a value in any interval of interest is the area above this interval and below the density curve:

```{figure} images/gen/m11-density-ab.svg
:alt: A right-skewed density curve with two points a and b marked on the horizontal axis. The area under the curve between a and b is shaded, representing the probability that X falls between a and b.
```

Now that we see how probabilities are found for continuous random variables, we understand why it is more complicated than finding probabilities in the discrete case. As anyone who has studied calculus can attest, finding the area under a curve can be difficult. The general approach is to use *integrals*. For those of you who did study calculus, the following should be familiar:

$$P(a \leq X \leq b)=\text{(area between a and b, below the density curve)}=\int_{a}^{b}f(x)\,dx$$

where f(x) represents the density curve. For those who did not study calculus, don't worry about it. This kind of calculation is definitely beyond the scope of this course.

In this course, we will encounter several important density curves—those for normal random variables, t random variables, chi-square random variables, and F random variables. Normal and t distributions are bell-shaped (single-peaked and symmetric) like the density curve in the foot length example; chi-square and F distributions are single-peaked and skewed right, like in the figure above.

Rather than get bogged down in the calculus of solving for areas under curves, we will find probabilities for the above-mentioned random variables by consulting tables. Also, statistical software automatically provides such probabilities in the appropriate context.

## Check Your Understanding: Density Curves and Continuous Variables

:::{quiz} For a continuous random variable X, what is P(X = 11), the probability that X exactly equals 11?
:hint: How much area sits over a single point?
:feedback-0: Correct! There is no area over a single point, so the probability of any exact value is 0—only intervals have positive probability.
:feedback-1: The height of the curve at 11 is the density, not a probability.
:feedback-2: 0.5 would be the probability of being below the median, not of hitting one exact value.
* *0
* The height of the density curve at 11
* 0.5
:::

In the next section, we will study in more depth one of those random variables, the normal random variable, and see how we can find probabilities associated with it using technology and tables.
