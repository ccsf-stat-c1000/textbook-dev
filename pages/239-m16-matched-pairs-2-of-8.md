# Matched Pairs (2 of 8)

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

So far, we have discussed and illustrated cases in which the matched pairs design comes up, and we are now ready to discuss how to carry out the test in this case. We will first present the idea behind the paired t-test, and then go through the four steps in the testing process.

## The Paired t-Test

### Idea

The idea behind the paired t-test is to reduce this two-sample situation, where we are comparing two means, to a single-sample situation, where we are doing inference on a single mean, and then use the simple t-test that we introduced in the previous module. We will first illustrate this idea using our example, and then more generally.

```{note} Video
[Matched Pairs](https://www.youtube.com/watch?v=URPrSH0Lg_M)
```

In our drunk drivers example, instead of comparing the 20 "before" reaction times with the 20 "after" reaction times as two separate samples, we compute for each driver the *difference* in reaction time (before − after). By doing this, we are reducing the problem from a problem where we're comparing two means (i.e., doing inference on $\mu_1-\mu_2$) to a problem where we are making an inference about a *single mean*—μ, the mean of the differences in reaction time (before two beers − after two beers) in the population of all drivers, based on one sample of 20 differences.

In general, in every matched pairs problem, our data consist of 2 samples which are organized in n pairs. We reduce the two samples to only one by calculating, for each pair, the difference between the two observations:

```{figure} images/gen/m16-pairs-to-differences.svg
:alt: A table with rows for pair number, sample 1, and sample 2, with n columns. Each pair is reduced to a difference d by subtracting the sample 2 value from the sample 1 value, producing one sample of n differences d 1 through d n.
```

The paired t-test is based on this one sample of n differences, and it uses those differences as data for a simple t-test on a single mean—the mean of the differences.

This is the general idea behind the paired t-test: it is nothing more than a regular one-sample t-test for the mean of the differences. We will now go through the 4-step process of the paired t-test.

## Concept Check

:::{quiz} Why does the paired t-test work with the differences rather than the two samples separately?
:hint: What does pairing let us cancel out?
:feedback-0: Correct! Each difference compares a subject with itself, so subject-to-subject variation cancels out, and the two-mean comparison reduces to a one-sample inference about the mean difference.
:feedback-1: The differences don't discard information—they capture exactly the within-pair comparison the design was built for.
:feedback-2: The two samples in a matched pairs design are NOT independent, which is why the two-sample t-test cannot be used.
* *Differencing within each pair removes subject-to-subject variability and reduces the problem to a one-sample t-test
* Working with differences throws away half of the data
* Because the two samples are independent
:::
