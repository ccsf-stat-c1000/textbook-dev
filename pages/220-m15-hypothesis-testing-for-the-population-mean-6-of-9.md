# When σ Is Unknown: The t-Test and t Distribution

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Tests About μ When σ Is Unknown: The t-Test for the Population Mean

As we mentioned earlier, only in a few cases is it reasonable to assume that the population standard deviation, σ, is known. The case where σ is unknown is much more common in practice. What can we use to replace σ? If you don't know the population standard deviation, the best you can do is find the sample standard deviation, s, and use it instead of σ. (Note that this is exactly what we did when we discussed confidence intervals.)

Is that it? Can we just use s instead of σ, and the rest is the same as the previous case? Unfortunately, it's not that simple, but not very complicated either.

We will first go through the four steps of the t-test for the population mean and explain in what way this test is different from the z-test in the previous case. For comparison purposes, we will then apply the t-test to a variation of the two examples we used in the previous case, and end with an activity where you'll get to carry out the t-test yourself.

Let's start by describing the four steps for the t-test:

### Step 1: Stating the Hypotheses

In this step there are no changes:

- The null hypothesis has the form $H_0: \mu = \mu_0$ (where $\mu_0$ is the null value).
- The alternative hypothesis takes one of the following three forms (depending on the context): $H_a: \mu < \mu_0$ (one-sided), $H_a: \mu > \mu_0$ (one-sided), or $H_a: \mu \neq \mu_0$ (two-sided).

### Step 2: Checking Conditions and Summarizing the Data

Technically, this step only changes slightly compared to what we do in the z-test. However, as you'll see, this small change has important implications. The conditions under which the t-test can be safely carried out are exactly the same as those for the z-test:

1. The sample is random (or at least can be considered random in context).
2. We are in one of the "OK" situations in the following table (which ensures that $\bar{X}$ is at least approximately normal):

   | Conditions: t-test for a population mean | Small sample size | Large sample size |
   | --- | --- | --- |
   | Variable varies normally in the population | OK | OK |
   | Variable doesn't vary normally in the population | NOT OK | OK |

Assuming that the conditions are met, we calculate the sample mean $\bar{x}$ and the sample standard deviation, s (which replaces σ), and summarize the data with a test statistic. As in the z-test, our test statistic will be the standardized score of $\bar{x}$ assuming that $\mu=\mu_0$ ($H_0$ is true). The difference here is that we don't know σ, so we use s instead. The test statistic for the t-test for the population mean is therefore:

```{admonition} Test Statistic for the t-Test for the Population Mean
:class: note

$$t=\frac{\bar{x}-\mu_{0}}{s/\sqrt{n}}$$
```

The change is in the denominator: while in the z-test we divided by the standard *deviation* of $\bar{X}$, namely $\frac{\sigma}{\sqrt{n}}$, here we divide by the standard *error* of $\bar{X}$, namely $\frac{s}{\sqrt{n}}$. Does this have an effect on the rest of the test? Yes. The t-test statistic does not follow a standard normal distribution. Rather, it follows another bell-shaped distribution called the *t distribution*. So we first need to introduce this new distribution as a general object; then we'll come back to our discussion of the t-test for the mean and how the t distribution arises in that context.

## The t Distribution

We have seen that variables can be visually modeled by many different sorts of shapes, and we call these shapes distributions. Several distributions arise so frequently that they have been given special names, and they have been studied mathematically. So far in the course, the only one we've named is the normal distribution, but there are others. One of them is called the t distribution.

The t distribution is another bell-shaped (unimodal and symmetric) distribution, like the normal distribution, and the center of the t distribution is standardized at zero, like the center of the standard normal distribution. Like all distributions that are used as probability models, the normal and the t distribution are both scaled so the total area under each of them is 1.

So how is the t distribution fundamentally *different* from the normal distribution?

The *spread*.

The following picture illustrates the fundamental difference between the normal distribution and the t distribution:

```{figure} images/gen/m15-t-vs-normal.svg
:alt: A standard normal curve and a t distribution curve, both centered at zero and scaled to have total area 1. The t distribution has a lower peak near the center and fatter tails, reflecting its larger spread. The curves intersect once on each side of the center.
```

You can see in the picture that the t distribution has *slightly less area near the expected central value* than the normal distribution does, and correspondingly *more area in the "tails"* than the normal distribution does. (It's often said that the t distribution has "fatter tails" or "heavier tails" than the normal distribution.)

This reflects the fact that the t distribution *has a larger spread* than the normal distribution. The same total area of 1 is spread out over a slightly wider range, making the t distribution a bit lower near the center compared to the normal distribution, and giving it slightly more probability in the tails.

Therefore, the t distribution ends up being the appropriate model in certain cases where there is *more variability* than would be predicted by the normal distribution. One of these cases is stock values, which have more variability (or "volatility," to use the economic term) than would be predicted by the normal distribution.

There's actually an entire family of t distributions. They all have similar formulas (the math is beyond the scope of this introductory course), and they all have slightly fatter tails than the normal distribution. But some are closer to normal than others. The t distributions that are closer to normal are said to have higher *degrees of freedom*. So there's a t distribution "with 1 degree of freedom," another t distribution "with 2 degrees of freedom" which is slightly closer to normal, another "with 3 degrees of freedom" which is a bit closer to normal than the previous ones, and so on.

The following picture illustrates this idea with a couple of t distributions (note that "degrees of freedom" is abbreviated "d.f."):

```{figure} images/gen/m15-t-df.svg
:alt: The standard normal curve overlaid with a t distribution with 5 degrees of freedom and a t distribution with 2 degrees of freedom. The t distribution with 2 degrees of freedom is shorter and has more spread than the one with 5 degrees of freedom, which in turn is shorter and wider than the standard normal distribution.
```

## Check Your Understanding: The t Distribution vs. the Normal

Consider a standard normal (Z) distribution and a t distribution drawn together, and focus on the region to the right of the value 3.

:::{quiz} Which is larger: P(Z > 3) or P(T > 3)?
:hint: Which curve has more area in its tails?
:feedback-0: Correct! The t distribution's fatter tails mean it has more area beyond any extreme value, so P(T > 3) > P(Z > 3).
:feedback-1: The t distribution has MORE tail area than the normal, not less.
:feedback-2: The two probabilities differ—only near the center are the curves close.
* *P(T > 3)—the t distribution has more area in its tails
* P(Z > 3)—the normal distribution has more area in its tails
* They are equal
:::

## Check Your Understanding: Comparing z and t P-values

:::{quiz} A test statistic of −2 is observed. If the p-value is computed once using the standard normal distribution and once using a t distribution, how do the two p-values compare?
:hint: The p-value is a tail area, and the t distribution has fatter tails.
:feedback-0: Correct! Since the t distribution has more area beyond −2 than the normal does, the t-based p-value is larger.
:feedback-1: It's the reverse—the t distribution's fatter tails produce LARGER p-values for the same test statistic.
:feedback-2: They differ noticeably unless the degrees of freedom are very large.
* *The t-based p-value is larger than the normal-based one
* The t-based p-value is smaller than the normal-based one
* The two p-values are always identical
:::

Now let's return to our discussion of the test for the mean, and see how and why the t distribution arises in that context.
