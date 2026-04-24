# Hypothesis Testing for the Population Proportion p (6 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 3. Finding the P-value of the Test

So far we've talked about the p-value at the intuitive level: understanding what it is (or what it measures) and how we use it to draw conclusions about the significance of our results. We will now go more deeply into how the p-value is calculated.

It should be mentioned that eventually we will rely on technology to calculate the p-value for us (as well as the test statistic), but in order to make intelligent use of the output, it is important to first *understand* the details, and only then let the computer do the calculations for us. Let's start.

Recall that so far we have said that the p-value is the probability of obtaining data like those observed assuming that H~o~ is true. Like the test statistic, the p-value is, therefore, a measure of the evidence against H~o~. In the case of the *test statistic,* the *larger* it is in magnitude (positive or negative) , the further $\hat{p}$ is from $p_{0}$ , the *more evidence we have against H*~*o*~*.*In the case of the *p-value*, it is the opposite; the *smaller* it is, the more unlikely it is to get data like those observed when H~o~ is true, the *more evidence it is against H*~*o*~. One can actually draw conclusions in hypothesis testing just using the test statistic, and as we'll see the p-value is, in a sense, just another way of looking at the test statistic. The reason that we actually take the extra step in this course and derive the p-value from the test statistic is that even though in this case (the test about the population proportion) and some other tests, the value of the test statistic has a very clear and intuitive interpretation, there are some tests where its value is not as easy to interpret. On the other hand, the p-value keeps its intuitive appeal across all statistical tests.

*How is the p-value calculated?*

Intuitively, the p-value is the *probability* of observing *data like those observed* assuming that H~o~is true. Let's be a bit more formal:

- Since this is a probability question about the *data*, it makes sense that the calculation will involve the data summary, the *test statistic.*
- What do we mean by *"like"* those observed? By "like" we mean *"as extreme or even more extreme."*

Putting it all together, we get that in *general:*

*The p-value is the probability of observing a test statistic as extreme as that observed (or even more extreme) assuming that the null hypothesis is true.*

## Comment

By *"extreme"* we mean extreme *in the direction of the alternative* hypothesis.

*Specifically*, for the z-test for the population proportion:

1. If the alternative hypothesis is $H_{a}:p<p_{0}$ (*less* than), then "extreme" means *small*, and the p-value is: The probability of observing a test statistic *as small as that observed or smaller* if the null hypothesis is true.
2. If the alternative hypothesis is $H_{a}:p>p_{0}$ (*greater* than), then "extreme" means *large*, and the p-value is: The probability of observing a test statistic *as large as that observed or larger* if the null hypothesis is true.
3. if the alternative is $H_{a}:p\neqp_{0}$ (*different* from), then "extreme" means extreme in either direction *either small or large (i.e., large in magnitude)*, and the p-value therefore is: The probability of observing a test statistic *as large in magnitude as that observed or larger* if the null hypothesis is true.

(Examples: If z = -2.5: p-value = probability of observing a test statistic as small as -2.5 or smaller or as large as 2.5 or larger.

If z = 1.5: p-value = probability of observing a test statistic as large as 1.5 or larger, or as small as -1.5 or smaller.)

*OK, that makes sense. But how do we actually calculate it?*

Recall the important comment from our discussion about our test statistic,

$z=\frac{\hat{p}&minus;p_{0}}{\sqrt{\frac{p_{0}(1&minus;p_{0}}{n}}}$

which said that when the null hypothesis is true (i.e., when $p=p_{0}$), the possible values of our test statistic (because it is a z-score) follow a standard normal (N(0,1), denoted by Z) distribution. Therefore, the p-value calculations (which assume that H~o~ is true) are simply standard normal distribution calculations for the 3 possible alternative hypotheses.

## Less Than

The probability of observing a test statistic as *small as that observed or smaller*, assuming that the values of the test statistic follow a standard normal distribution. We will now represent this probability in symbols and also using the normal distribution.

```{figure} images/image258.gif
:alt: Ha: p &lt; p_0 ⇒ p-value = P(Z ≤ z)

Ha: p &lt; p_0 ⇒ p-value = P(Z ≤ z)
```

```{figure} images/image259.gif
:alt: A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0 and z. z is to the left of 0 because it is for a test statistic which is smaller than p_0. The p-value is the area to the left of z under the curve.

A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0 and z. z is to the left of 0 because it is for a test statistic which is smaller than p_0. The p-value is the area to the left of z under the curve.
```

Looking at the shaded region, you can see why this is often referred to as a *left-tailed* test. We shaded to the left of the test statistic, since less than is to the left.

## Greater Than

The probability of observing a test statistic as *large as that observed or larger*, assuming that the values of the test statistic follow a standard normal distribution. Again, we will represent this probability in symbols and using the normal distribution.

```{figure} images/image260.gif
:alt: Ha: p &gt; p_0 ⇒ p-value = P(Z ≥ z)

Ha: p &gt; p_0 ⇒ p-value = P(Z ≥ z)
```

```{figure} images/image261.gif
:alt: A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0 and z. z is to the right of 0 because it is for a test statistic which is larger than p_0. The p-value is the area to the right of z under the curve.

A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0 and z. z is to the right of 0 because it is for a test statistic which is larger than p_0. The p-value is the area to the right of z under the curve.
```

Looking at the shaded region, you can see why this is often referred to as a *right-tailed* test. We shaded to the right of the test statistic, since greater than is to the right.

## Not Equal To

The probability of observing a test statistic which is as large as in *magnitude* as that observed or larger, assuming that the values of the test statistic follow a standard normal distribution.

```{figure} images/image262.gif
:alt: Ha: p ≠ p_0 ⇒ p-value = P(Z &lt; |z|) + P(Z ≥ |z|) = 2P(Z ≥ |z|)

Ha: p ≠ p_0 ⇒ p-value = P(Z &lt; |z|) + P(Z ≥ |z|) = 2P(Z ≥ |z|)
```

```{figure} images/image263.gif
:alt: A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0, -|z|, and |z|, where |z| and -|z| is the z-score of the observed test statistic. The p-value is the sum of the area to the right of |z| under the curve and the area to the left of -|z| under the curve.

A normal distribution curve (N(0,1)). Marked on the horizontal axis are z-scores of 0, -|z|, and |z|, where |z| and -|z| is the z-score of the observed test statistic. The p-value is the sum of the area to the right of |z| under the curve and the area to the left of -|z| under the curve.
```

This is often referred to as a *two-tailed* test, since we shaded in both directions.

As noted earlier, before the widespread use of statistical software, it was common to use 'critical values' instead of p-values to assess the evidence provided by the data. Even though the critical values approach is not used in this course, students might find it insightful. Thus, the interested students are encouraged to review the critical value method in the following “Many Students Wonder....” link. If your instructor clearly states that you are required to have knowledge of the critical value method, you should definitely review the information.

```{note}
    **Many Students Wonder**

    The Critical Value Method

    *(Interactive activity — available in the OLI platform)*
```

On the next page, we will apply the p-value to our three examples. But first, work through the following activities, which should help your understanding.

## Learn By Doing

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

In each of the following questions, choose the pair(s) of hypotheses for the population proportion (p) and the z statistic that match the figure.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
