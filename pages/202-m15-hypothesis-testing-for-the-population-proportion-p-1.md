# The z-Test for a Proportion: Overview

```{admonition} Learning Objectives
:class: note

- In a given context, specify the null and alternative hypotheses for the population proportion and mean.
```

## Overview

Now that we understand the process we go through in hypothesis testing and the logic behind it, we are ready to start learning about specific statistical tests (also known as significance tests).

The first test we are going to learn is the test about the population proportion (p). This test is widely known as the *z-test for the population proportion (p)*. (We will understand later where the "z-test" part comes from.)

When we conduct a test about a population proportion, we are working with a categorical variable. Later in the course, after we have learned a variety of hypothesis tests, we will need to be able to identify which test is appropriate for which situation. Identifying the variable as categorical or quantitative is an important component of choosing an appropriate hypothesis test.

:::{quiz} A researcher tests whether the proportion of students who commute by transit differs from 0.40. What type of variable is being studied?
:hint: A test about a proportion always involves classifying individuals into categories.
:feedback-0: Correct! Each student either commutes by transit or does not—a categorical variable. Proportions summarize categorical data.
:feedback-1: Commute TIME would be quantitative, but here each student is simply classified as transit commuter or not.
* *Categorical—each student is classified as a transit commuter or not
* Quantitative—we are measuring how much students commute
:::

Our discussion of hypothesis testing for the population proportion p follows the four steps of hypothesis testing that we introduced in our general discussion, but this time we go into more detail. More specifically, we learn how the test statistic and p-value are calculated and interpreted.

Once we learn how to carry out the test for the population proportion p, we discuss some general topics that are related to hypothesis testing. More specifically, we see what role the sample size plays and understand how hypothesis testing and interval estimation (confidence intervals) are related.

Let's start by introducing the three examples, which will be the leading examples in our discussion. Each example is followed by a figure illustrating the information provided, as well as the question of interest.

::::{admonition} Example 1: Defective Products
:class: tip

A machine is known to produce 20% defective products, and is therefore sent for repair. After the machine is repaired, 400 products produced by the machine are chosen at random and 64 of them are found to be defective. Do the data provide enough evidence that the proportion of defective products produced by the machine (p) has been *reduced* as a result of the repair?

The following figure displays the information, as well as the question of interest:

```{figure} images/gen/m15-prop-machine.svg
:alt: A large circle represents the population of products produced by the machine following the repair. We want to know p, the proportion of defective products, and whether p is still 0.20 or has been reduced. A smaller circle represents a random sample of 400 products, of which 64 are defective.
```

The question of interest helps us formulate the null and alternative hypotheses in terms of p, the proportion of defective products produced by the machine following the repair:

- $H_0$: p = 0.20 (no change; the repair did not help)
- $H_a$: p < 0.20 (the repair was effective)
::::

::::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

There are rumors that students at a certain liberal arts college are more inclined to use drugs than U.S. college students in general. Suppose that in a simple random sample of 100 students from the college, 19 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is 0.157? (This number was reported by the Harvard School of Public Health.)

Again, the following figure displays the information as well as the question of interest:

```{figure} images/gen/m15-prop-marijuana.svg
:alt: A large circle represents the population of students at the college. We want to know p, the proportion of students using marijuana, and whether p is 0.157 like the national figure or higher. A smaller circle represents a random sample of 100 students, of which 19 use marijuana.
```

As before, we can formulate the null and alternative hypotheses in terms of p, the proportion of students in the college who use marijuana:

- $H_0$: p = 0.157 (same as among all college students in the country)
- $H_a$: p > 0.157 (higher than the national figure)
::::

::::{admonition} Example 3: Death Penalty Support
:class: tip

Polls on certain topics are conducted routinely in order to monitor changes in the public's opinions over time. One such topic is the death penalty. In 2003 a poll estimated that 64% of U.S. adults support the death penalty for a person convicted of murder. In a more recent poll, 675 out of 1,000 U.S. adults chosen at random were in favor of the death penalty for convicted murderers. Do the results of this poll provide evidence that the proportion of U.S. adults who support the death penalty for convicted murderers (p) *changed* between 2003 and the later poll?

Here is a figure that displays the information, as well as the question of interest:

```{figure} images/gen/m15-prop-deathpenalty.svg
:alt: A large circle represents the population of U.S. adults. We want to know p, the proportion who support the death penalty, and whether p has changed since 2003 when it was 0.64. A smaller circle represents a random sample of 1,000 U.S. adults, of which 675 are in favor.
```

Again, we can formulate the null and alternative hypotheses in terms of p, the proportion of U.S. adults who support the death penalty for convicted murderers:

- $H_0$: p = 0.64 (no change from 2003)
- $H_a$: p ≠ 0.64 (some change since 2003)
::::

## Check Your Understanding: Setting Up a Test for a Proportion

According to the American Association of Community Colleges, 23% of community college students receive federal grants. The California Community College Chancellor's Office anticipates that the percentage is smaller for California community college students. They collect a sample of 1,000 community college students in California and find that 210 received federal grants.

:::{quiz} What is the population of interest in this study?
:hint: About which group does the Chancellor's Office want to draw a conclusion?
:feedback-0: Correct! The conclusion is about all California community college students; the 1,000 students are the sample.
:feedback-1: This is the sample, not the population.
:feedback-2: The 23% figure describes community college students nationwide—the baseline, not the population being studied.
* *All community college students in California
* The 1,000 students in the study
* All community college students in the United States
:::

:::{quiz} What are the appropriate hypotheses?
:hint: The null value is the national rate, 0.23; the office anticipates a SMALLER percentage in California.
:feedback-0: Correct! H₀: p = 0.23 (same as the national rate); Hₐ: p < 0.23 (smaller, as anticipated).
:feedback-1: The alternative should be one-sided (smaller), since the office specifically anticipates a smaller percentage.
:feedback-2: The null value should be the claimed baseline 0.23, not the sample result 0.21.
* *H₀: p = 0.23; Hₐ: p < 0.23
* H₀: p = 0.23; Hₐ: p ≠ 0.23
* H₀: p = 0.21; Hₐ: p < 0.21
:::

:::{quiz} What is the sample proportion p-hat in this study?
:hint: 210 out of 1,000.
:feedback-0: Correct! p-hat = 210/1000 = 0.21.
:feedback-1: 0.23 is the national (null) value, not the sample result.
:feedback-2: p-hat is the number of successes divided by the sample size: 210/1000.
* *0.21
* 0.23
* 210
:::

:::{quiz} Which sample results would count as evidence in favor of the alternative hypothesis?
:hint: Hₐ says p < 0.23.
:feedback-0: Correct! Since the alternative is one-sided (p < 0.23), only sample proportions well below 0.23 count as evidence for Hₐ.
:feedback-1: Sample proportions above 0.23 would, if anything, point away from this alternative.
:feedback-2: With a one-sided alternative, only departures in the specified direction count.
* *Sample proportions much smaller than 0.23
* Sample proportions much larger than 0.23
* Sample proportions far from 0.23 in either direction
:::

## Check Your Understanding: Hypotheses and Sample Proportions

Using data from 2008, the American Association of Community Colleges (AACC) reports that community college students constitute 46% of all U.S. undergraduates. Given the downturn in the U.S. economy, the AACC anticipates an increase in this percentage for 2010. A poll of 500 randomly chosen undergraduates taken in 2010 indicates that 52% are attending a community college.

:::{quiz} What are the appropriate hypotheses for this study?
:hint: The null value is the 2008 rate; the AACC anticipates an INCREASE.
:feedback-0: Correct! H₀: p = 0.46; Hₐ: p > 0.46, since an increase is anticipated.
:feedback-1: The AACC anticipates an increase, so the alternative should be one-sided (greater than).
:feedback-2: The null value should be the 2008 baseline 0.46, not the 2010 sample result 0.52.
* *H₀: p = 0.46; Hₐ: p > 0.46
* H₀: p = 0.46; Hₐ: p ≠ 0.46
* H₀: p = 0.52; Hₐ: p > 0.52
:::

:::{quiz} In this study, which value is the sample proportion and which is the null value?
:hint: The null value comes from the prior claim (2008); the sample proportion comes from the 2010 poll.
:feedback-0: Correct! p₀ = 0.46 is the hypothesized (2008) value; p-hat = 0.52 is what the 2010 sample showed.
:feedback-1: It's the reverse—0.46 is the baseline being tested, and 0.52 came from the sample.
* *Null value p₀ = 0.46; sample proportion p-hat = 0.52
* Null value p₀ = 0.52; sample proportion p-hat = 0.46
:::
