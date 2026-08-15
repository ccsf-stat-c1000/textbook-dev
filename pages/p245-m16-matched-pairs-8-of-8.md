# The Paired t-Test: Summary

## Let's Summarize

- The paired t-test is used to compare two population means when the two samples (drawn from the two populations) are dependent, in the sense that every observation in one sample can be linked to an observation in the other sample. Such a design is called "matched pairs."
- The most common case in which the matched pairs design is used is when the same subjects are measured twice, usually before and then after some kind of treatment and/or intervention. Another classic case is studies involving twins.
- As in the "two independent samples" case, in the background we have a two-valued categorical explanatory variable whose categories define the two populations we are comparing and whose effect on the response variable we are trying to assess.
- The idea behind the paired t-test is to reduce the data from two samples to just one sample of the differences, and use these observed differences as data for inference about a single mean—the mean of the differences, $\mu_d$.
- The paired t-test is therefore simply a one-sample t-test for the mean of the differences $\mu_d$, where the null value is 0.
- Once we verify that we can safely proceed with the paired t-test, we use software output to carry it out.
- A 95% confidence interval for $\mu_d$ can be very insightful after a test has rejected the null hypothesis, and can also be used for testing in the two-sided case.

## Check Your Understanding

:::{quiz} Which of the following studies calls for a paired t-test rather than a two-sample t-test?
:hint: Look for a design where each observation in one sample is linked to one in the other.
:feedback-0: Correct! Measuring the same cars twice (with each fuel type) links the observations in pairs.
:feedback-1: Two separately sampled, unrelated groups call for the two-sample t-test.
:feedback-2: Randomly assigning different subjects to two groups produces independent samples.
* *Fuel efficiency of 15 cars, each measured once with regular fuel and once with premium fuel
* Salaries of a random sample of 40 nurses versus a random sample of 45 teachers
* Test scores of students randomly assigned to two different study methods
:::

:::{quiz} In a matched pairs study, the hypotheses are stated about which parameter?
:hint: The two samples are reduced to one sample of differences.
:feedback-0: Correct! The paired t-test is a one-sample t-test about $\mu_d$, the population mean of the differences (which equals $\mu_1 - \mu_2)$.
:feedback-1: The sample mean of the differences is the estimate, not the parameter.
:feedback-2: The hypotheses concern one parameter $(\mu_d)$, not the two separate means individually.
* *$\mu_d$, the population mean of the differences
* x-bar_d, the sample mean of the differences
* $\mu_1$ and $\mu_2$ separately
:::
