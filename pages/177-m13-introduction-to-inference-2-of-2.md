# Introduction to Inference (2 of 2)

```{admonition} Learning Objectives
:class: note

- Identify inference type, e.g., point estimation, interval estimation, and hypothesis testing.
```

We introduce three forms of statistical inference in this unit, each one representing a different way of using the information obtained in the sample to draw conclusions about the population. These forms are:

- Point estimation
- Interval estimation
- Hypothesis testing

Obviously, each one of these forms of inference will be discussed at length in this section, but it would be useful to get at least an intuitive sense of the nature of each of these inference forms, and the difference between them in terms of the type of conclusions they draw about the population based on the sample results.

In *point estimation*, we estimate an unknown parameter using a *single number* that is calculated from the sample data.

:::{admonition} Example: Point Estimation
:class: tip

Based on sample results, we estimate that p, the proportion of all U.S. adults who are in favor of stricter gun control, is 0.6.
:::

In *interval estimation*, we estimate an unknown parameter using an *interval of values* that is likely to contain the true value of that parameter (and state how confident we are that this interval indeed captures the true value of the parameter).

:::{admonition} Example: Interval Estimation
:class: tip

Based on sample results, we are 95% confident that p, the proportion of U.S. adults who are in favor of stricter gun control, is between 0.57 and 0.63.
:::

In *hypothesis testing*, we have some claim about the population, and we check *whether or not the data* obtained from the sample *provide evidence against this claim.*

:::{admonition} Example: Hypothesis Testing 1
:class: tip

It was claimed that among all U.S. adults, about half are in favor of stricter gun control and about half are against it. In a recent poll of a random sample of 1,200 U.S. adults, 60% were in favor of stricter gun control. This data, therefore, provides some evidence against the claim.
:::

:::{admonition} Example: Hypothesis Testing 2
:class: tip

It is claimed that among drivers 18-23 years of age (our population) there is no relationship between drunk driving and gender. A roadside survey collected data from a random sample of 5,000 drivers and recorded their gender and whether they were drunk. The collected data showed roughly the same percent of drunk drivers among males and among females. These data, therefore, do not give us any reason to reject the claim that drunk driving is not related to gender.
:::

## Did I Get This?

In each of the following scenarios, a conclusion is drawn about a population based on the sample results. Select which form of statistical inference the conclusion represents.

:::{quiz} "Based on a sample of 150 customers, the average wait time at the clinic is estimated to be 23 minutes." Which form of inference is this?
:hint: A single number is used to estimate the parameter.
:feedback-0: Correct! A single number (23 minutes) estimating the population mean is point estimation.
:feedback-1: Interval estimation would report a range of plausible values along with a confidence level.
:feedback-2: Hypothesis testing would assess evidence against a stated claim.
* *Point estimation
* Interval estimation
* Hypothesis testing
:::

:::{quiz} "We are 90% confident that between 42% and 48% of city voters support the bond measure." Which form of inference is this?
:hint: A range of values with a confidence level.
:feedback-0: Point estimation would give a single number, like 45%.
:feedback-1: Correct! A range of plausible values with an attached confidence level is interval estimation.
:feedback-2: No claim is being tested here; the goal is to estimate the parameter.
* Point estimation
* *Interval estimation
* Hypothesis testing
:::

:::{quiz} "The manufacturer claims its batteries last 100 hours on average. Our sample of 50 batteries averaged only 92 hours, providing evidence against the claim." Which form of inference is this?
:hint: A stated claim is being checked against sample evidence.
:feedback-0: The 92-hour average is used here as evidence about a claim, not as the final estimate.
:feedback-1: No interval or confidence level appears; instead a claim is evaluated.
:feedback-2: Correct! Assessing whether the data provide evidence against a claim about the population is hypothesis testing.
* Point estimation
* Interval estimation
* *Hypothesis testing
:::

In terms of organization, the Inference unit consists of two main parts: Inference for One Variable and Inference for Relationships between Two Variables. The organization of each of these parts will be discussed further as we proceed through the unit.
