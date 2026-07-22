# Step 3: Finding the P-value for a Proportion

## Step 3: Finding the P-value of the Test

So far we've talked about the p-value at the intuitive level: understanding what it is (or what it measures) and how we use it to draw conclusions about the significance of our results. We will now go more deeply into how the p-value is calculated.

It should be mentioned that eventually we will rely on technology to calculate the p-value for us (as well as the test statistic), but in order to make intelligent use of the output, it is important to first *understand* the details, and only then let the computer do the calculations for us. Let's start.

Recall that so far we have said that the p-value is the probability of obtaining data like those observed assuming that $H_0$ is true. Like the test statistic, the p-value is, therefore, a measure of the evidence against $H_0$. In the case of the *test statistic*, the *larger* it is in magnitude (positive or negative), the further $\hat{p}$ is from $p_0$, and the *more evidence* we have against $H_0$. In the case of the *p-value*, it is the opposite; the *smaller* it is, the more unlikely it is to get data like those observed when $H_0$ is true, and the *more evidence* the data provide against $H_0$.

One can actually draw conclusions in hypothesis testing just using the test statistic, and as we'll see, the p-value is, in a sense, just another way of looking at the test statistic. The reason that we take the extra step in this course and derive the p-value from the test statistic is that even though in this case (the test about the population proportion) and some other tests, the value of the test statistic has a very clear and intuitive interpretation, there are some tests where its value is not as easy to interpret. On the other hand, the p-value keeps its intuitive appeal across all statistical tests.

*How is the p-value calculated?*

Intuitively, the p-value is the *probability* of observing *data like those observed* assuming that $H_0$ is true. Let's be a bit more formal:

- Since this is a probability question about the *data*, it makes sense that the calculation will involve the data summary, the *test statistic*.
- What do we mean by *"like"* those observed? By "like" we mean *"as extreme or even more extreme."*

Putting it all together, we get that in *general*:

*The p-value is the probability of observing a test statistic as extreme as that observed (or even more extreme) assuming that the null hypothesis is true.*

By *"extreme"* we mean extreme *in the direction of the alternative* hypothesis. *Specifically*, for the z-test for the population proportion:

1. If the alternative hypothesis is $H_a: p < p_0$ (*less than*), then "extreme" means *small*, and the p-value is the probability of observing a test statistic *as small as that observed or smaller* if the null hypothesis is true.
2. If the alternative hypothesis is $H_a: p > p_0$ (*greater than*), then "extreme" means *large*, and the p-value is the probability of observing a test statistic *as large as that observed or larger* if the null hypothesis is true.
3. If the alternative is $H_a: p \neq p_0$ (*different from*), then "extreme" means *large in magnitude* (either small or large), and the p-value is the probability of observing a test statistic *as large in magnitude as that observed or larger* if the null hypothesis is true.

(Examples: if z = −2.5, the p-value is the probability of observing a test statistic as small as −2.5 or smaller, or as large as 2.5 or larger. If z = 1.5, the p-value is the probability of observing a test statistic as large as 1.5 or larger, or as small as −1.5 or smaller.)

*OK, that makes sense. But how do we actually calculate it?*

Recall the important comment from our discussion about the test statistic

$$z=\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}}$$

which said that when the null hypothesis is true (i.e., when $p=p_0$), the possible values of our test statistic (because it is a z-score) follow a standard normal (N(0,1), denoted by Z) distribution. Therefore, the p-value calculations (which assume that $H_0$ is true) are simply standard normal distribution calculations for the three possible alternative hypotheses.

## Less Than

The p-value is the probability of observing a test statistic as *small as that observed or smaller*, assuming that the values of the test statistic follow a standard normal distribution:

```{figure} images/gen/m15-pvalue-left.svg
:alt: A standard normal curve with z-scores 0 and z marked on the horizontal axis. z is to the left of 0. The p-value is the shaded area to the left of z under the curve, so p-value equals P(Z less than or equal to z).
```

Looking at the shaded region, you can see why this is often referred to as a *left-tailed* test. We shaded to the left of the test statistic, since less than is to the left.

## Greater Than

The p-value is the probability of observing a test statistic as *large as that observed or larger*, assuming that the values of the test statistic follow a standard normal distribution:

```{figure} images/gen/m15-pvalue-right.svg
:alt: A standard normal curve with z-scores 0 and z marked on the horizontal axis. z is to the right of 0. The p-value is the shaded area to the right of z under the curve, so p-value equals P(Z greater than or equal to z).
```

Looking at the shaded region, you can see why this is often referred to as a *right-tailed* test. We shaded to the right of the test statistic, since greater than is to the right.

## Not Equal To

The p-value is the probability of observing a test statistic which is as *large in magnitude* as that observed or larger, assuming that the values of the test statistic follow a standard normal distribution:

```{figure} images/gen/m15-pvalue-two.svg
:alt: A standard normal curve with z-scores 0, negative absolute z, and positive absolute z marked on the horizontal axis. The p-value is the sum of the shaded area to the left of negative absolute z and the shaded area to the right of positive absolute z, which equals two times P(Z greater than or equal to absolute z).
```

This is often referred to as a *two-tailed* test, since we shaded in both directions.

```{admonition} Comment: The Critical Values Approach
:class: important

As noted earlier, before the widespread use of statistical software, it was common to use *critical values* instead of p-values to assess the evidence provided by the data. In that approach, the observed test statistic is compared with a fixed cutoff value (for example, z\* = 1.645 for a one-sided test at the 0.05 level), and $H_0$ is rejected when the test statistic falls beyond the cutoff. The two approaches always lead to the same conclusion; this course focuses on p-values.
```

On the next page, we will apply the p-value to our three examples. But first, work through the following activities, which should help your understanding.

## Check Your Understanding: Finding the P-value

:::{quiz} A test of H₀: p = 0.30 versus Hₐ: p > 0.30 yields a test statistic of z = 1.8. Which area under the standard normal curve equals the p-value?
:hint: "Greater than" alternatives are right-tailed.
:feedback-0: Correct! For Hₐ: p > p₀, the p-value is the area to the RIGHT of the observed z: P(Z ≥ 1.8).
:feedback-1: The area to the left would be appropriate for a "less than" alternative.
:feedback-2: Two tails are only used for a "not equal to" alternative.
* *The area to the right of 1.8
* The area to the left of 1.8
* The area beyond ±1.8 in both tails
:::

:::{quiz} A test of H₀: p = 0.30 versus Hₐ: p ≠ 0.30 yields a test statistic of z = −2.1. Which area equals the p-value?
:hint: "Not equal to" alternatives are two-tailed.
:feedback-0: Correct! For a two-sided alternative, the p-value is the area in BOTH tails: P(Z ≤ −2.1) + P(Z ≥ 2.1) = 2P(Z ≥ 2.1).
:feedback-1: The left tail alone would be the p-value for Hₐ: p < 0.30.
:feedback-2: The area between −2.1 and 2.1 is everything EXCEPT the p-value.
* *The area to the left of −2.1 plus the area to the right of 2.1
* The area to the left of −2.1 only
* The area between −2.1 and 2.1
:::

:::{quiz} Two tests each produce a test statistic of z = 2.0—one tests Hₐ: p > p₀ and the other tests Hₐ: p ≠ p₀. How do their p-values compare?
:hint: The two-tailed p-value counts the area in both tails.
:feedback-0: Correct! The one-tailed p-value is P(Z ≥ 2) ≈ 0.023, while the two-tailed p-value doubles it: ≈ 0.046.
:feedback-1: The two-sided test's p-value is twice as large, since it includes both tails.
:feedback-2: The p-values differ because the definition of "extreme" differs between the two alternatives.
* *The two-sided test has a p-value twice as large as the one-sided test
* The one-sided test has a p-value twice as large as the two-sided test
* The p-values are equal
:::

:::{quiz} Why is a SMALLER p-value stronger evidence against H₀?
:hint: The p-value measures how likely data like ours would be in a world where H₀ is true.
:feedback-0: Correct! A tiny p-value says data like ours would almost never occur if H₀ were true—so the fact that we observed such data discredits H₀.
:feedback-1: The p-value is not the probability that H₀ is true; it is a probability about the DATA, computed assuming H₀ is true.
:feedback-2: A small p-value indicates the data are FAR from what H₀ predicts, not close to it.
* *Because it means data like ours would be very unlikely if H₀ were true
* Because it is the probability that H₀ is true
* Because it means the data agree closely with H₀
:::

## Check Your Understanding: P-values and Tails

:::{quiz} A figure shows a standard normal curve with only the area to the LEFT of z = −1.4 shaded. Which pair of hypotheses and test statistic matches the figure?
:hint: A single shaded left tail corresponds to a "less than" alternative.
:feedback-0: Correct! A left-tailed shaded region corresponds to Hₐ: p < p₀ with an observed z = −1.4.
:feedback-1: A "greater than" alternative would shade to the right.
:feedback-2: A two-sided alternative would shade both tails.
* *H₀: p = 0.5, Hₐ: p < 0.5, z = −1.4
* H₀: p = 0.5, Hₐ: p > 0.5, z = −1.4
* H₀: p = 0.5, Hₐ: p ≠ 0.5, z = −1.4
:::
