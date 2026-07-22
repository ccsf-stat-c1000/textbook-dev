# Following a Test with a Confidence Interval

Here is our final point on this subject:

When the data provide enough evidence to reject $H_0$, we can conclude (depending on the alternative hypothesis) that the population proportion is either less than, greater than, or not equal to the null value $p_0$. However, we do not get a more informative statement about its actual value. It might be of interest, then, to follow the test with a 95% confidence interval that will give us more insight into the actual value of p.

:::{admonition} Example: Death Penalty Support
:class: tip

In our example 3 ($H_0: p = 0.64$ vs. $H_a: p \neq 0.64$; $\hat{p} = 0.675$; z = 2.31; p-value = 0.021), we concluded that the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003, when it was 0.64. It is probably of interest not only to know that the proportion has changed, but also to estimate what it has changed to. We calculated the 95% confidence interval for p on the previous page and found that it is (0.645, 0.705).

We can combine our conclusions from the test and the confidence interval and say:

The data provide evidence that the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003, and we are 95% confident that it is now between 0.645 and 0.705 (i.e., between 64.5% and 70.5%).
:::

:::{admonition} Example: Defective Products
:class: tip

Let's look at our example 1 to see how a confidence interval following a test might be insightful in a different way.

Recall the summary of example 1: $H_0: p = 0.20$ vs. $H_a: p < 0.20$; a random sample of 400 products gave $\hat{p} = 0.16$; z = −2; p-value = 0.023; $H_0$ was rejected.

We conclude that as a result of the repair, the proportion of defective products has been reduced to below 0.20 (which was the proportion prior to the repair). It is probably of great interest to the company not only to know that the proportion of defectives has been reduced, but also to estimate what it has been reduced to, to get a better sense of how effective the repair was. A 95% confidence interval for p in this case is:

$$0.16\pm2\cdot\sqrt{\frac{0.16(1-0.16)}{400}}\approx0.16\pm0.037=(0.123,\ 0.197)$$

We can therefore say that the data provide evidence that the proportion of defective products has been reduced, and we are 95% sure that it has been reduced to somewhere between 12.3% and 19.7%. This is very useful information, since it tells us that even though the results were significant (i.e., the repair reduced the number of defective products), the repair might not have been effective enough, if it managed to reduce the number of defective products only to the range provided by the confidence interval. This, of course, ties back in to the idea of statistical significance vs. practical importance that we discussed earlier. Even though the results are significant ($H_0$ was rejected), practically speaking, the repair might be considered ineffective.
:::

## Check Your Understanding: Following Up a Test with an Interval

:::{quiz} A test rejects H₀: p = 0.35 in favor of Hₐ: p > 0.35 with a p-value of 0.008. What is the added value of following up with a 95% confidence interval for p?
:hint: What does the test conclusion tell you about p, and what does it leave out?
:feedback-0: Correct! The test only tells us that p is above 0.35; the confidence interval estimates WHERE p actually is, which lets us judge whether the difference is practically meaningful.
:feedback-1: The interval does not re-test the hypothesis—it adds an estimate of the parameter's actual value.
:feedback-2: A confidence interval cannot make the results "more significant"; it complements the test with an estimate.
* *The interval estimates the actual value of p, so we can judge how far above 0.35 it plausibly is
* The interval double-checks whether the test was done correctly
* The interval increases the significance of the results
:::

## Let's Summarize

Even though this unit is about the z-test for the population proportion, it is loaded with very important ideas that apply to hypothesis testing in general. We've already summarized the details that are specific to the z-test for proportions, so the purpose of this summary is to highlight the general ideas.

The process of hypothesis testing has four steps:

1. *State the null and alternative hypotheses* ($H_0$ and $H_a$).

2. *Obtain a random sample* (or at least one that can be considered random) and collect data. Using the data, *check that the conditions* under which the test can be reliably used are met, and *summarize the data using a test statistic*. The test statistic is a measure of the evidence in the data against $H_0$. The larger the test statistic is in magnitude, the more evidence the data present against $H_0$.

3. *Find the p-value of the test.* The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against $H_0$. The smaller the p-value, the more evidence the data present against $H_0$.

4. *Make conclusions*—first about the *significance of the results*: if the p-value is small, the data present enough evidence to reject $H_0$ (and accept $H_a$); if the p-value is not small, the data do not provide enough evidence to reject $H_0$. To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at 0.05, but should not be considered inviolable. Then, state conclusions *in the context* of the problem.

Additional general ideas:

- Results that are based on a larger sample carry more weight, and therefore *as the sample size increases, results become more significant*.
- Even a very small and practically unimportant effect becomes statistically significant with a large enough sample size. The *distinction between statistical significance and practical importance* should therefore always be considered.
- For given data, the *p-value of the two-sided test is always twice as large as the p-value of the one-sided test*. It is therefore harder to reject $H_0$ in the two-sided case than it is in the one-sided case, in the sense that stronger evidence is required. Intuitively, the hunch or information that leads us to use the one-sided test can be regarded as a head start toward the goal of rejecting $H_0$.
- *Confidence intervals can be used in order to carry out two-sided tests* (at the 0.05 significance level). If the null value is not included in the confidence interval (i.e., is not one of the plausible values for the parameter), we have enough evidence to reject $H_0$. Otherwise, we cannot reject $H_0$.
- If the results are significant, it might be of interest to *follow up the test with a confidence interval* in order to get insight into the actual value of the parameter of interest.

## Reflection

Before moving on, take a moment to write down, in your own words, the meaning of the p-value and why a small p-value is evidence against the null hypothesis. Being able to explain this to someone else is the best check of your understanding.
