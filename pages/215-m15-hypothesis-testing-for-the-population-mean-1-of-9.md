# The z-Test for a Mean: Overview

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Overview

So far we have talked about the logic behind hypothesis testing and then illustrated how this process proceeds in practice, using the z-test for the population proportion (p). We are now moving on to discuss testing for the population mean (μ), which is the parameter of interest when the variable of interest is quantitative. Two comments about the structure of this section:

1. The basic groundwork for carrying out hypothesis tests has already been laid in our discussion of tests about proportions, and therefore we can easily modify the four steps to carry out tests about means instead, without going into all the little details.

2. This section will have two parts, as we need to distinguish between two cases: the case where the population standard deviation (σ) is known, and the case where σ is unknown.

   - In the first case (σ known), the test is called the *z-test for the population mean μ*.
   - In the second case (σ unknown), the test is called the *t-test for the population mean μ*.

The reason for the different names (z vs. t) is exactly the same reason that the test for the proportion (p) is called a z-test. In the first case, the test statistic will have a standard normal (z) distribution (when $H_0$ is true), and in the second case, the test statistic will have a t-distribution (when $H_0$ is true).

Let's start.

## Tests About μ When σ Is Known: The z-Test for the Population Mean

In this section, we will proceed under the assumption that the population standard deviation (σ) is known. We've already discussed the practicality of this assumption. In most situations, the population standard deviation is not known, but in some cases, especially when the variable of interest has been investigated thoroughly over the years, it would make sense to assume that σ is known. Such variables are, for example, IQs and other standardized test scores, or heights, weights, and other physical characteristics.

We'll start by introducing two examples that will be our leading examples for this part.

::::{admonition} Example 1: SAT-M Scores at Ross College
:class: tip

The SAT is constructed so that scores in each portion have a national average of 500 and standard deviation of 100. The distribution is close to normal. The dean of students of Ross College suspects that in recent years the college attracts students who are more quantitatively inclined. A random sample of 4 students from a recent entering class at Ross College had an average math SAT (SAT-M) score of 550. Does this provide enough evidence for the dean to conclude that the mean SAT-M of all Ross College students is higher than the national mean of 500? Assume that the standard deviation of 100 applies also to all Ross College students.

*Comment:* this is a situation where it is quite reasonable to assume that the population standard deviation (σ) is known. SAT tests are constructed so that the standard deviation is 100, and provided that there is nothing special about students at Ross College, we can assume that σ = 100 in the population of Ross College students.

Here is a figure that represents this example:

```{figure} images/gen/m15-mean-satm.svg
:alt: A large circle represents all students at Ross College. We are interested in mu, the mean SAT-M score. The question is whether the mean SAT-M is 500 (the national mean) or higher, assuming the standard deviation is 100. A smaller circle represents a random sample of 4 students, whose sample mean is 550.
```
::::

::::{admonition} Example 2: Concentration of a Chemical in a Drug
:class: tip

A certain prescription medicine is supposed to contain an average of 250 parts per million (ppm) of a certain chemical. If the concentration is higher than this, the drug may cause harmful side effects; if it is lower, the drug may be ineffective. The manufacturer runs a check to see if the mean concentration in a large shipment conforms to the target level of 250 ppm or not. A simple random sample of 100 portions is tested, and the sample mean concentration is found to be 247 ppm. It is assumed that the concentration standard deviation in the entire shipment is σ = 12 ppm.

*Comment:* here it is not that clear why the assumption that σ is known to be 12 is reasonable. If shipments are checked on a regular basis, then maybe past experience has shown that indeed σ = 12. In any case, we will come back to this problem and discuss this point again later.

```{figure} images/gen/m15-mean-concentration.svg
:alt: A large circle represents the shipment, the population of interest. Mu is the mean concentration of the chemical. The question is whether the mean concentration is the required 250 ppm or not, assuming the standard deviation is 12. A smaller circle represents a random sample of 100 portions, whose sample mean is 247 ppm.
```
::::

Like any other test, the z-test for the population mean follows the four-step process:

1. Stating the hypotheses $H_0$ and $H_a$.
2. Collecting relevant data, checking that the data satisfy the conditions which allow us to use this test, and summarizing the data using a test statistic.
3. Finding the p-value of the test, the probability of obtaining data as extreme as those collected (or even more extreme, in the direction of the alternative hypothesis), assuming that the null hypothesis is true. In other words, how likely is it that the only reason for getting data like those observed is sampling variability (and not because $H_0$ is not true)?
4. Drawing conclusions, assessing the significance of the results based on the p-value, and stating our conclusions in context. (Do we or don't we have evidence to reject $H_0$ and accept $H_a$?)

We will now go through the four steps specifically for the z-test for the population mean and apply them to our two examples.
