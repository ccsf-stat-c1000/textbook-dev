# Hypothesis Testing for the Population Proportion p (13 of 13)

```{admonition} Learning Objectives
    - Apply the concepts of: sample size, statistical significance vs. practical importance, and the relationship between hypothesis testing and confidence intervals.
```

Here is our final point on this subject:

When the data provide enough evidence to reject H~o~, we can conclude (depending on the alternative hypothesis) that the population proportion is either less than, greater than or not equal to the null value $p_{0}$. However, we do not get a more informative statement about its actual value. It might be of interest, then, to follow the test with a 95% confidence interval that will give us more insight into the actual value of p.

```{admonition} Example
    In our example 3,

    ```{figure} images/image277.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = .64 and H_a: p ≠ .64 . We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675, z = 2.31, and the p-value is .021 , which is small enough to let us reject H_0.

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = .64 and H_a: p ≠ .64 . We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675, z = 2.31, and the p-value is .021 , which is small enough to let us reject H_0.
    ```

    we concluded that the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003, when it was .64. It is probably of interest not only to know that the proportion has changed, but also to estimate what it has changed to. We've calculated the 95% confidence interval for p on the previous page and found that it is (.645, .705).

    We can combine our conclusions from the test and the confidence interval and say:

    Data provide evidence that the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003, and we are 95% confident that it is now between .645 and .705. (i.e. between 64.5% and 70.5%).
```

```{admonition} Example
    Let's look at our example 1 to see how a confidence interval following a test might be insightful in a different way.

    Here is a summary of example 1:

    ```{figure} images/image275.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = .20 and H_a: p < .20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16, and z = -2 and p-value = .023 . Since the p-value is small we conclude that H_0 can be rejected.

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = .20 and H_a: p < .20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16, and z = -2 and p-value = .023 . Since the p-value is small we conclude that H_0 can be rejected.
    ```

    We conclude that as a result of the repair, the proportion of defective products has been reduced to below .20 (which was the proportion prior to the repair). It is probably of great interest to the company not only to know that the proportion of defective has been reduced, but also estimate what it has been reduced to, to get a better sense of how effective the repair was. A 95% confidence interval for p in this case is:

    $.16\pm2⋅\sqrt{\frac{.16\left(1−.16\right)}{400}}\approx.16\pm.037=\left(.129, .197\right)$

    We can therefore say that the data provide evidence that the proportion of defective products has been reduced, and we are 95% sure that it has been reduced to somewhere between 12.9% and 19.7%. This is very useful information, since it tells us that even though the results were significant (i.e., the repair reduced the number of defective products), the repair might not have been effective enough, if it managed to reduce the number of defective products only to the range provided by the confidence interval. This, of course, ties back in to the idea of statistical significance vs. practical importance that we discussed earlier. Even though the results are significant (H~o~ was rejected), practically speaking, the repair might be considered ineffective.
```

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Proportion p

    *(Interactive activity — available in the OLI platform)*
```

## Let's summarize

Even though this unit is about the z-test for population proportion, it is loaded with very important ideas that apply to hypothesis testing in general. We've already summarized the details that are specific to the z-test for proportions, so the purpose of this summary is to highlight the general ideas.

The process of hypothesis testing has four steps:

*I. Stating the null and alternative hypotheses (H~o~ and H~a~).*

*II.* Obtaining a random sample (or at least one that can be considered random) and collecting data. Using the data:

**Check that the conditions* under which the test can be reliably used are met.

* *Summarize the data using a test statistic.*

The test statistic is a measure of the evidence in the data against H~o~. The larger the test statistic is in magnitude, the more evidence the data present against H~o~.

*III. Finding the p-value of the test.*

The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against H~o~. The smaller the p-value, the more evidence the data present against H~a~.

*IV. Making conclusions.*

- Conclusions about the *significance of the results:*

If the p-value is small, the data present enough evidence to reject H~o~ (and accept H~a~).

If the p-value is not small, the data do not provide enough evidence to reject H~o~.

To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at .05, but should not be considered inviolable.

- Conclusions *in the context* of the problem.

Results that are based on a larger sample carry more weight, and therefore *as the sample size increases, results become more significant.*

Even a very small and practically unimportant effect becomes statistically significant with a large enough sample size. The *distinction between statistical significance and practical importance* should therefore always be considered.

For given data, the *p-value of the two-sided test is always twice as large as the p-value of the one-sided test*. It is therefore harder to reject H~o~ in the two-sided case than it is in the one-sided case in the sense that stronger evidence is required. Intuitively, the hunch or information that leads us to use the one-sided test can be regarded as a head-start toward the goal of rejecting H~o~.

*Confidence intervals can be used in order to carry out two-sided tests* (at the .05 significance level). If the null value is not included in the confidence interval (i.e., is not one of the plausible values for the parameter), we have enough evidence to reject H~o~. Otherwise, we cannot reject H~o~.

If the results are significant, it might be of interest to *follow up the tests with a confidence interval* in order to get insight into the actual value of the parameter of interest.

## End-of-Lesson
                Questions

```{note}
    **My Response**

    About Hypothesis Testing

    *(Interactive activity — available in the OLI platform)*
```
