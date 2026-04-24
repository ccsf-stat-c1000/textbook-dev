# Probability Distribution (2 of 2)

```{admonition} Learning Objectives
    - Explain how a density function is used to find probabilities involving continuous random variables.
```

Now consider another random variable X = foot length of adult males. Unlike shoe size, this variable is not limited to distinct, separate values, because foot lengths can take any value over a *continuous* range of possibilities, so we cannot present this variable with a probability histogram or a table. The probability distribution of foot length (or any other continuous random variable) can be represented by a smooth curve called a *probability density curve.*

```{figure} images/image104.gif
:alt: A probability density curve. The horizontal axis is labeled X=Male Foot Length. On this graph, a curve is drawn. The curve appears to be a bell curve (looks like the cross section of a bell), centered at x=11. The area below the curve is equal to 1.

A probability density curve. The horizontal axis is labeled X=Male Foot Length. On this graph, a curve is drawn. The curve appears to be a bell curve (looks like the cross section of a bell), centered at x=11. The area below the curve is equal to 1.
```

Like the modified probability histogram above, the total area under the density curve equals 1, and the curve represents probabilities by area.

The probability that X gets values in any interval is represented by the area above this interval and below the density curve. In our foot length example, if our interval of interest is between 10 and 12 (marked in red below), and we would like to know P(10 < X < 12), the probability that a randomly chosen male has a foot length anywhere between 10 and 12 inches, we'll have to find the area above our interval of interest (10,12) and below our density curve, shaded in blue:

```{figure} images/image105.gif
:alt: The area under the curve and above the horizontal axis from X=10 to X=12 has been shaded in blue. This area is P(10 < X < 12).

The area under the curve and above the horizontal axis from X=10 to X=12 has been shaded in blue. This area is P(10 < X < 12).
```

If, for example, we are interested in P(X < 9), the probability that a randomly chosen male has a foot length of less than 9 inches, we'll have to find the area shaded in blue below:

```{figure} images/image106.gif
:alt: The area under the curve and above the horizontal axis from X = 6 (the left end of the graph) to X = 9 has been shaded. This area is P(X < 9).

The area under the curve and above the horizontal axis from X = 6 (the left end of the graph) to X = 9 has been shaded. This area is P(X < 9).
```

## Comments

1. We have seen that for a *discrete* random variable like shoe size, whether we have a
                            strict inequality or not *does matter* when solving for
                            probabilities. In contrast, for a *continuous* random variable
                            like foot length, the probability of a foot length
                            of
                            less than or equal to 9 will be the same as the
                            probability of a foot length
                            of
                            strictly less than 9. In other words, $P(X<9)=P(X\leq9)$. Visually, in terms of our density curve, the area under the curve up to and including a certain point is the same as the area up to and excluding the point, because there is no area over a single point.  
    Conceptually, because a continuous random variable has infinitely many possible values, technically the probability of any single value occurring is zero!
2. It should be clear now why the total area under any probability density curve must be 1. The
                            total area under the curve represents P(X gets a value in the interval
                            of its possible values). Clearly, according to the rules of probability
                            this must be
                            1,
                            or always true.
3. Density curves, like probability histograms, may have any shape imaginable as long as the total area underneath the curve is 1.

## Let's Summarize

The probability distribution of a continuous random variable is represented by a probability density curve.

The probability that X gets a value in any interval of interest is the area above this interval and below the density curve.

```{figure} images/image108.gif
:alt: A probability density curve. The vertical axis is labeled "Density" and the horizontal axis is labeled "X." The density curve of x has been drawn on the graph, and on the horizontal axis, two points a and b, a < b, have been marked. The area under the density curve and above the horizontal axis from a < X < b has been shaded. This area is P(a ≤ X ≤ b).

A probability density curve. The vertical axis is labeled "Density" and the horizontal axis is labeled "X." The density curve of x has been drawn on the graph, and on the horizontal axis, two points a and b, a < b, have been marked. The area under the density curve and above the horizontal axis from a < X < b has been shaded. This area is P(a ≤ X ≤ b).
```

Now that we see how probabilities are found for continuous random variables, we understand why it is more complicated than finding probabilities in the discrete case. As anyone who has studied calculus can attest, finding the area under a curve can be difficult. The general approach is to use *integrals.* For those of you who did study calculus, the following should be familiar....

$P(a\leqX\leqb)=(area between a and b and below the density curve)=∫_{a}^{b}f(x)dx$ , where f(x) represents the density curve.

For those who did not study calculus, don't worry about it. This kind of calculation is definitely beyond the scope of this course.

In this course, we will encounter several important density curves—those for normal random variables, t random variables, chi-square random variables, and F random variables. Normal and t distributions are bell-shaped (single-peaked and symmetric) like the density curve in the foot length example; chi-square and F distributions are single-peaked and skewed right, like in the figure above.

Rather than get bogged down in the calculus of solving for areas under curves, we will find probabilities for the above-mentioned random variables by consulting tables. Also, statistical software automatically provides such probabilities in the appropriate context.

In the next section, we will study in more depth one of those random variables, the normal random variable, and see how we can find probabilities associated with it using software and tables.
