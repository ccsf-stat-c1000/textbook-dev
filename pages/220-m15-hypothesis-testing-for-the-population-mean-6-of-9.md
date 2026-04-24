# Hypothesis Testing for the Population Mean (6 of 9)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Tests About μ When σ is Unknown—The t-test for the Population Mean

As we mentioned earlier, only in a few cases is it reasonable to assume that the population standard deviation, σ, is known. The case where σ is unknown is much more common in practice. What can we use to replace σ? If you don't know the population standard deviation, the best you can do is find the sample standard deviation, S, and use it instead of σ. (Note that this is exactly what we did when we discussed confidence intervals).

```{figure} images/image355.gif
:alt: A large circle represents the population of interest. μ is unknown and σ is unknown. From the population we create a SRS of size n, represented by a smaller circle. We can find x-bar for this SRS, and we can also obtain S. We use this instead of the unknown σ.

A large circle represents the population of interest. μ is unknown and σ is unknown. From the population we create a SRS of size n, represented by a smaller circle. We can find x-bar for this SRS, and we can also obtain S. We use this instead of the unknown σ.
```

Is that it? Can we just use S instead of σ, and the rest is the same as the previous case? Unfortunately, it's not that simple, but not very complicated either.

We will first go through the four steps of the t-test for the population mean and explain in what way this test is different from the z-test in the previous case. For comparison purposes, we will then apply the t-test to a variation of the two examples we used in the previous case, and end with an activity where you'll get to carry out the t-test yourself.

Let's start by describing the four steps for the t-test:

*I.*Stating the hypotheses.

In this step there are no changes:

* The null hypothesis has the form:

$H_{0}:\mu=\mu_{0}$

(where $\mu_{0}$ is the null value).

* The alternative hypothesis takes one of the following three forms (depending on the context):

$H_{a}:\mu<\mu_{0}$(one-sided)

$H_{a}:\mu>\mu_{0}$ (one-sided)

$H_{a}:\mu\neq\mu_{0}$ (two-sided)

*II.* Checking the conditions under which the t-test can be safely used and summarizing the data.

Technically, this step only changes slightly compared to what we do in the z-test. However, as you'll see, this small change has important implications. The conditions under which the t-test can be safely carried out are exactly the same as those for the z-test:

(i) The sample is random (or at least can be considered random in context).

(ii) We are in one of the three situations marked with a green check mark in the following table (which ensure that $\bar{X}$ is at least approximately normal):

```{figure} images/image325.gif
:alt: A table which has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;

A table which has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;
```

Assuming that the conditions are met, we calculate the sample mean $\bar{x}$ and the sample standard deviation, S (which replaces σ), and summarize the data with a test statistic. As in the z-test, our test statistic will be the standardized score of $\bar{x}$assuming that $\mu=\mu_{0}$ (H~o~ is true). The difference here is that we don't know σ, so we use S instead. The test statistic for the t-test for the population mean is therefore:

$t=\frac{\bar{x}&minus;\mu_{0}}{\frac{s}{\sqrt{n}}}$

The change is in the denominator: while in the z-test we divided by the standard *deviation* of $\bar{X}$, namely $\frac{\sigma}{\sqrt{n}}$, here we divide by the standard *error* of $\bar{X}$, namely $\frac{s}{\sqrt{n}}$. Does this have an effect on the rest of the test? Yes. The t-test statistic in the test for the mean does not follow a standard normal distribution. Rather, it follows another bell-shaped distribution called the t distribution. So we first need to introduce you to this new distribution as a general object. Then, we’ll come back to our discussion of the t-test for the mean and how the t-distribution arises in that context.

## The t Distribution

We have seen that variables can be visually modeled by many different sorts of shapes, and we call these shapes distributions. Several distributions arise so frequently that they have been given special names, and they have been studied mathematically. So far in the course, the only one we’ve named is the normal distribution, but there are others. One of them is called the t distribution.

The t distribution is another bell-shaped (unimodal and symmetric) distribution, like the normal distribution; and the center of the t distribution is standardized at zero, like the center of the normal distribution.

Like all distributions that are used as probability models, the normal and the t distribution are both scaled, so the total area under each of them is 1.

So how is the t distribution fundamentally *different* from the normal distribution?

The *spread*.

The following picture illustrates the fundamental difference between the normal distribution and the t distribution:

```{figure} images/image363.gif
:alt: A standard normal curve modeling the Z-distribution and a curve modeling the t-distribution. Both have been scaled so that the area under the curve is 1. The standard normal curve has less spread than the t-distribution curve. This means that the left and right tails are closer to each other than in the t-distribution, and that it is taller than the t-distribution. The t-distribution is narrower than the standard normal distribution when close to the center. Because of this, the curves intersect once on each side of the center.

A standard normal curve modeling the Z-distribution and a curve modeling the t-distribution. Both have been scaled so that the area under the curve is 1. The standard normal curve has less spread than the t-distribution curve. This means that the left and right tails are closer to each other than in the t-distribution, and that it is taller than the t-distribution. The t-distribution is narrower than the standard normal distribution when close to the center. Because of this, the curves intersect once on each side of the center.
```

You can see in the picture that the t distribution has *slightly less area near the expected central value* than the normal distribution does, and you can see that the t distribution has correspondingly *more area in the "tails"* than the normal distribution does. (It’s often said that the t distribution has "fatter tails" or "heavier tails" than the normal distribution.)

This reflects the fact that the t distribution *has a larger spread* than the normal distribution. The same total area of 1 is spread out over a slightly wider range on the t distribution, making it a bit lower near the center compared to the normal distribution, and giving the t distribution slightly more probability in the ‘tails’ compared to the normal distribution.

Therefore, the t distribution ends up being the appropriate model in certain cases where there is *more variability* than would be predicted by the normal distribution. One of these cases is stock values, which have more variability (or "volatility," to use the economic term) than would be predicted by the normal distribution.

There’s actually an entire family of t distributions. They all have similar formulas (but the math is beyond the scope of this introductory course in statistics), and they all have slightly "fatter tails" than the normal distribution. But some are closer to normal than others. The t distributions that are closer to normal are said to have higher "degrees of freedom" (that’s a mathematical concept that we won’t use in this course, beyond merely mentioning it here). So, there’s a t distribution "with one degree of freedom," another t distribution "with 2 degrees of freedom" which is slightly closer to normal, another t distribution "with 3 degrees of freedom." which is a bit closer to normal than the previous ones, and so on.

The following picture illustrates this idea with just a couple of t distributions (note that “degrees of freedom” is abbreviated "d.f." on the picture):

```{figure} images/image417.gif
:alt: The standard normal z-distribution curve overlaid with a t-distribution with 5 d.f., and a t-distribution with 2 d.f. The distribution with 2 t.f. is shorter and has more spread than the t-distribution with 5 d.f., which in turn is shorter and wider than the standard normal distribution.

The standard normal z-distribution curve overlaid with a t-distribution with 5 d.f., and a t-distribution with 2 d.f. The distribution with 2 t.f. is shorter and has more spread than the t-distribution with 5 d.f., which in turn is shorter and wider than the standard normal distribution.
```

##### Learn By Doing

The following figure of the standard normal distribution together with a t distribution will visually help you answer the following questions.

```{figure} images/image395.gif
:alt: The standard normal Z distribution curve and the t-distribution curve overlaid on top of each other, centered at a z-score of 0. At z-score = 3, a blue vertical line has been drawn. Here, the t distribution&apos;s wider spread causes it to be higher than the standard normal curve. Going right, we see that the standard normal curve reaches zero much sooner compared to the t distribution curve.

The standard normal Z distribution curve and the t-distribution curve overlaid on top of each other, centered at a z-score of 0. At z-score = 3, a blue vertical line has been drawn. Here, the t distribution&apos;s wider spread causes it to be higher than the standard normal curve. Going right, we see that the standard normal curve reaches zero much sooner compared to the t distribution curve.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### Did I Get This?

The following figure of the standard normal distribution together with a t distribution will visually help you answer the following questions.

```{figure} images/image418.gif
:alt: The standard normal Z distribution curve and the t distribution curve overlaid on top of each other, centered at a z-score of 0. At z-score = -2, a blue vertical line has been drawn. Here, the t distribution and standard normal curve intersect. Going left, we see that the standard normal curve reaches zero much sooner compared to the t distribution curve, and that the t distribution is above the standard normal distribution. Going right from the vertical blue line, we see that the t distribution is under the standard normal distribution and ultimately will have a lower peak value compared to the standard normal distribution.

The standard normal Z distribution curve and the t distribution curve overlaid on top of each other, centered at a z-score of 0. At z-score = -2, a blue vertical line has been drawn. Here, the t distribution and standard normal curve intersect. Going left, we see that the standard normal curve reaches zero much sooner compared to the t distribution curve, and that the t distribution is above the standard normal distribution. Going right from the vertical blue line, we see that the t distribution is under the standard normal distribution and ultimately will have a lower peak value compared to the standard normal distribution.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Now let’s return to our discussion of the test for the mean, and let’s see how and why the t distribution arises in that context.
