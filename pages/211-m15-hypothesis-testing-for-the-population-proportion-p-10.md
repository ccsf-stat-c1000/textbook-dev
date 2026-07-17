# The Effect of Sample Size on Testing

```{admonition} Learning Objectives
:class: note

- Apply the concepts of: sample size, statistical significance vs. practical importance, and the relationship between hypothesis testing and confidence intervals.
```

## More About Hypothesis Testing

The issues regarding hypothesis testing that we will discuss are:

1. The effect of sample size on hypothesis testing.
2. Statistical significance vs. practical importance.
3. One-sided alternative vs. two-sided alternative—understanding what is going on.
4. Hypothesis testing and confidence intervals—how are they related?

Let's start.

## 1. The Effect of Sample Size on Hypothesis Testing

We have already seen the effect that the sample size has on inference, when we discussed point and interval estimation for the population mean (μ) and population proportion (p). Intuitively...

Larger sample sizes give us more information to pin down the true nature of the population. We can therefore expect the *sample* mean and *sample* proportion obtained from a larger sample to be closer to the population mean and proportion, respectively. As a result, for the same level of confidence, we can report a smaller margin of error, and get a narrower confidence interval. What we've seen, then, is that a larger sample size gives a boost to how much we trust our sample results.

In hypothesis testing, larger sample sizes have a similar effect. The following two examples will illustrate that a larger sample size provides more convincing evidence, and how the evidence manifests itself in hypothesis testing. Let's go back to our example 2 (marijuana use at a certain liberal arts college).

:::{admonition} Example 2 (Original: n = 100)
:class: tip

Recall: $H_0: p = 0.157$ vs. $H_a: p > 0.157$; a random sample of n = 100 students gave $\hat{p} = 19/100 = 0.19$; the test statistic was z = 0.91 and the p-value was 0.182.

The data *do not* provide enough evidence that the proportion of marijuana users at the college is higher than the proportion among all U.S. college students, which is 0.157.

So far, nothing new. Let's make small changes to the problem (and call it example 2*).
:::

:::{admonition} Example 2*: A Larger Sample
:class: tip

There are rumors that students in a certain liberal arts college are more inclined to use drugs than U.S. college students in general. Suppose that *in a simple random sample of 400 students from the college, 76 admitted to marijuana use*. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is 0.157?

We now have a larger sample (400 instead of 100), and we also changed the number of marijuana users (76 instead of 19). Let's carry out the test in this case.

*Step 1:* The question of interest did not change, so we are testing the same hypotheses: $H_0: p = 0.157$ vs. $H_a: p > 0.157$.

*Step 2:* We select a random sample of size *400* and find that 76 are marijuana users. (Note that the data satisfy the conditions that allow us to use this test—verify this yourself.)

Let's summarize the data: $\hat{p} = \frac{76}{400} = 0.19$.

This is the same sample proportion as in the original problem, so it seems that the data give us the same evidence. But when we calculate the test statistic, we see that actually this is not the case:

$$z=\frac{0.19-0.157}{\sqrt{\frac{0.157(1-0.157)}{400}}}\approx1.81$$

Even though the sample proportion is the same (0.19), since here it is based on a larger sample (400 instead of 100), it is 1.81 standard deviations above the null value of 0.157 (as opposed to 0.91 standard deviations in the original problem).

*Step 3:* Using statistical software, we find that the p-value = 0.035.

The p-value here is 0.035 (as opposed to 0.182 in the original problem). In other words, when $H_0$ is true (i.e., when p = 0.157), it is quite unlikely (probability of 0.035) to get a sample proportion of 0.19 or higher based on a sample of size 400, and not very unlikely when the sample size is 100 (probability 0.182).

*Step 4:* Our results here are significant. In other words, in example 2* the data provide enough evidence to reject $H_0$ and conclude that the proportion of marijuana users at the college is higher than among all U.S. students.
:::

What do we learn from these two examples?

We see that sample results that are based on a larger sample carry more weight.

In example 2, we saw that a sample proportion of 0.19 based on a sample of size 100 was not enough evidence that the proportion of marijuana users in the college is higher than 0.157. Recall, from our general overview of hypothesis testing, that this conclusion (not having enough evidence to reject the null hypothesis) *doesn't* mean the null hypothesis is necessarily true (so we never "accept" the null); it only means that the particular study didn't yield sufficient evidence to reject the null. It *might* be that the sample size was simply too small to detect a statistically significant difference.

However, in example 2*, we saw that when the sample proportion of 0.19 is obtained from a sample of size 400, it carries much more weight, and in particular, provides enough evidence that the proportion of marijuana users in the college is higher than 0.157 (the national figure). In *this* case, the sample size of 400 *was* large enough to detect a statistically significant difference.

The following activity will allow you to practice the ideas and terminology used in hypothesis testing when a result is not statistically significant.

## Learn By Doing

Suppose that only 40% of the U.S. public supported the general direction of the previous U.S. administration's policies. To gauge whether the nationwide proportion, p, of support for the *current* administration is higher than 40%, a major polling organization conducts a random poll to test the hypotheses $H_0: p = 0.40$ vs. $H_a: p > 0.40$. The results are reported to be *not statistically significant*, with a *p-value of 0.214*.

:::{quiz} Which is the correct interpretation of "not statistically significant" here?
:hint: What does a large p-value permit us to conclude—and not conclude?
:feedback-0: Correct! The data do not provide enough evidence that support for the current administration exceeds 40%; we cannot reject H₀.
:feedback-1: Failing to reject H₀ does not prove that support equals 40%.
:feedback-2: The poll may simply have been too small to detect a real difference—non-significance is not proof of no difference.
* *The poll did not provide enough evidence that support is higher than 40%
* The poll proved that support is exactly 40%
* The poll proved that support is NOT higher than 40%
:::

:::{quiz} Which of the following could explain the non-significant result?
:hint: There are two possibilities: nothing is going on, or something is going on but the study missed it.
:feedback-0: Correct! Either support truly isn't above 40%, or it is above 40% but the sample was too small to detect the difference—the test alone cannot tell us which.
:feedback-1: This is only one of the possibilities—a real difference the study was too small to detect is also consistent with the result.
:feedback-2: This is also only one possibility—it could equally be that support truly is not higher than 40%.
* *Either support truly is not above 40%, or the sample was too small to detect a real difference
* Support is definitely not above 40%
* Support is definitely above 40%, but the sample was too small
:::

Now, we will address the issue of statistical significance versus practical importance (which also involves issues of sample size).

## Learn By Doing

Suppose a national retailer tests whether a website redesign has changed the proportion of visitors who make a purchase, historically p = 0.100. In a random sample of 4,000,000 visits after the redesign, the purchase proportion is 0.1005, and the p-value of the test of $H_0: p = 0.100$ vs. $H_a: p \neq 0.100$ turns out to be about 0.001.

:::{quiz} The result is highly statistically significant. Is it practically important?
:hint: Look at the size of the change itself: from 10% to 10.05%.
:feedback-0: Correct! With an enormous sample, even a trivial change (0.05 of a percentage point) becomes statistically significant. Statistical significance says the change is real, not that it matters.
:feedback-1: The p-value cannot measure the practical size of an effect—only the strength of evidence that some effect exists.
:feedback-2: The significance is legitimate—the issue is that the underlying change is tiny.
* *Probably not—a change from 10% to 10.05% is trivial, even though the huge sample makes it statistically significant
* Yes—a p-value of 0.001 always indicates an important effect
* The test must be invalid because the change is so small
:::

:::{quiz} What is the general lesson about very large samples in hypothesis testing?
:hint: Connect sample size, standard error, and what the test can "detect."
:feedback-0: Correct! As n grows, the standard error shrinks, so even minuscule departures from the null value produce large test statistics and tiny p-values. Always ask whether the observed effect size is meaningful.
:feedback-1: Large samples make tests MORE sensitive, not less.
:feedback-2: Larger samples are generally better for estimation—the caution is about interpreting significance, not about avoiding large samples.
* *With very large samples, even tiny, unimportant differences become statistically significant—so always consider the effect size
* Large samples make it harder to reach statistical significance
* Researchers should avoid collecting large samples
:::
