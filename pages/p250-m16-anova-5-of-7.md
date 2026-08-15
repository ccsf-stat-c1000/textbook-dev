# The ANOVA F-Test: P-value and Conclusion

## Step 3: Finding the P-value

The p-value of the ANOVA F-test is the probability of getting an F-statistic as large as we got (or even larger), had $H_0: \mu_1=\mu_2=\cdots=\mu_k$ been true. In other words, it tells us how surprising it is to find data like those observed, assuming that there is no difference among the population means $\mu_1, \mu_2, \ldots, \mu_k$.

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

As we already noticed, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).
:::

## Step 4: Making Conclusions in Context

As usual, we base our conclusion on the p-value. A small p-value tells us that our data contain a lot of evidence against $H_0$. More specifically, a small p-value tells us that the differences between the sample means are statistically significant (unlikely to have happened by chance), and therefore we reject $H_0$. If the p-value is not small, the data do not provide enough evidence to reject $H_0$, and so we continue to believe that it may be true. A significance level (cutoff probability) of 0.05 can help determine what is considered a small p-value.

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

In our example, the p-value is extremely small—close to 0—indicating that our data provide extremely strong evidence to reject $H_0$. We conclude that the frustration level means of the four majors are not all the same, or in other words, that major does have an effect on students' academic frustration levels at the school where the test was conducted.
:::

## Check Your Understanding: Conclusions from an ANOVA F-Test

:::{quiz} An ANOVA F-test comparing five treatments yields $F = 46.6$ and a p-value near 0. What exactly can we conclude?
:hint: The alternative says only "not all the means are equal."
:feedback-0: Correct! Rejecting $H_0$ tells us that the means are not ALL equal—but not which ones differ or how. Follow-up analyses are needed for that.
:feedback-1: The F-test's alternative does not specify which means differ; it only says not all are equal.
:feedback-2: Rejecting $H_0$ is a claim about the population means, not just the sample.
* *At least one population mean differs from the others—but the test doesn't say which
* All five population means differ from each other
* The five sample means are unequal, but nothing about the populations
:::
