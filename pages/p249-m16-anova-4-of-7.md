# The F-Statistic: Conditions and Computation

## Step 2: Checking Conditions and Finding the Test Statistic

The test statistic of the ANOVA F-test, called the *F-statistic*, has the form

$$F=\frac{\text{variation among sample means}}{\text{variation within groups}}$$

It has a different structure from all the test statistics we've looked at so far, but it is similar in that it is still a measure of the evidence against $H_0$. The larger F is (which happens when the denominator, the variation within groups, is small relative to the numerator, the variation among the sample means), the more evidence we have against $H_0$.

## Check Your Understanding: Understanding the F-Statistic

Consider a situation in which we compare $k = 3$ populations with independent samples of size 100 each, and the sample means are $\bar{y}_1=35$, $\bar{y}_2=30$, and $\bar{y}_3=25$. We are testing $H_0: \mu_1=\mu_2=\mu_3$ vs. $H_a$: not all the $\mu$'s are equal. Two possible scenarios of the data (both with these same sample means):

- *Scenario 1:* the three samples have very little spread, and their dotplots barely overlap.
- *Scenario 2:* the three samples have wide spread, and their dotplots overlap substantially.

:::{quiz} In which scenario is the F-statistic larger?
:hint: F = variation among means / variation within groups—and the numerator is the same in both scenarios.
:feedback-0: Correct! With the same variation among the means, smaller within-group variation (scenario 1) makes the denominator smaller and F larger.
:feedback-1: Scenario 2's large within-group spread INFLATES the denominator, making F smaller.
:feedback-2: The F-statistics differ because the within-group variation differs.
* *Scenario 1—the small within-group variation makes F large
* Scenario 2—the wide spread makes F large
* F is the same in both scenarios
:::

:::{quiz} In which scenario do the data provide stronger evidence against $H_0$?
:hint: Larger F means more evidence against $H_0$.
:feedback-0: Correct! In scenario 1, the differences among means clearly dominate the small within-group variation—strong evidence the population means differ.
:feedback-1: In scenario 2, the overlap means the differences among sample means could plausibly be due to chance.
* *Scenario 1
* Scenario 2
:::

```{admonition} Comments
:class: important

1. The focus here is for you to understand the *idea* behind this test statistic, so we do not go into detail about how the two variations are measured. We instead rely on software output to obtain the F-statistic.

2. This test is called the ANOVA F-test. So far, we have explained the ANOVA part of the name. Based on the previous tests we introduced, it should not be surprising that the "F-test" part comes from the fact that the null distribution of the test statistic, under which the p-values are calculated, is called an *F-distribution*. We will say very little about the F-distribution in this course.

3. It is fairly straightforward to decide if a z-statistic is large. Even without tables, we should realize by now that a z-statistic of 0.8 is not especially large, whereas a z-statistic of 2.5 is large. In the case of the t-statistic, it is less straightforward, because there is a different t-distribution for every sample size n (and degrees of freedom $n - 1)$. However, the fact that a t-distribution with a large number of degrees of freedom is very close to the z (standard normal) distribution can help to assess the magnitude of the t-test statistic. When the size of the F-statistic must be assessed, the task is even more complicated, because there is a different F-distribution for every combination of the number of groups we are comparing and the total sample size. We will nevertheless say that for most situations, an F-statistic greater than 4 would be considered rather large, but tables or software are needed to get a truly accurate assessment.
```

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

For our example, the software output for the ANOVA F-test reports that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against $H_0$. (We can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well.)
:::

Let's move on to talk about the conditions under which we can safely use the ANOVA F-test. The first two conditions are very similar to ones we've seen before, but there is a new third condition. It is safe to use the ANOVA procedure when the following conditions hold:

1. The samples drawn from each of the populations we're comparing are independent.

2. The response variable varies normally within each of the populations we're comparing. As you already know, in practice this is done by looking at the histograms of the samples and making sure that there is no evidence of extreme departure from normality in the form of extreme skewness and outliers. Another possibility is to look at side-by-side boxplots of the data, and add histograms if a more detailed view is necessary. For large sample sizes, we don't really need to worry about normality, although it is always a good idea to look at the data.

3. The populations all have the same standard deviation. The best we can do to check this condition is to find the *sample* standard deviations of our samples and check whether they are "close." A common rule of thumb is to check whether the ratio between the largest sample standard deviation and the smallest is less than 2. If that's the case, this condition is considered to be satisfied.

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

In our example all the conditions are satisfied:

1. All the samples were chosen randomly, and are therefore independent.

2. The sample sizes are large enough (n = 35 per group) that we really don't have to worry about normality; however, looking at the data with side-by-side boxplots (scenario 2 from earlier) is still worthwhile. The data suggest that the frustration level of the Business students is generally lower than that of students from the other three majors. The ANOVA F-test will tell us whether these differences are significant.

3. The four sample standard deviations are 2.088 (Business), 2.362 (English), 2.485 (Mathematics), and 3.082 (Psychology). The rule of thumb is satisfied, since $3.082/2.088 < 2$.
:::

## Check Your Understanding: Conditions for ANOVA

In each of the following questions, you'll find two designs for comparing the number of credits taken by freshmen vs. sophomores vs. juniors vs. seniors. In each case, one of the designs should not be handled with ANOVA. Your task is to identify which one.

:::{quiz} Design A: independent random samples of 50 students from each class level. Design B: a random sample of 50 students, each followed for four years, recording their credits as freshmen, sophomores, juniors, and seniors. Which design should NOT be analyzed with (one-way) ANOVA?
:hint: ANOVA (as presented here) requires independent samples.
:feedback-0: Correct! In design B the same students appear in all four groups—the samples are dependent (repeated measures), so one-way ANOVA for independent samples does not apply.
:feedback-1: Design A uses independent samples from each class level, which is exactly the ANOVA setting.
* *Design B—the four samples consist of the same students and are therefore dependent
* Design A—the samples are too small for ANOVA
:::

:::{quiz} Independent samples of 15 students per class level are taken, and the four sample standard deviations are 3.1, 4.4, 5.2, and 8.7. Is the equal-standard-deviation condition satisfied?
:hint: Compare the largest to the smallest: 8.7/3.1.
:feedback-0: Correct! $8.7/3.1 \approx 2.8$, which exceeds 2, so the rule of thumb fails and ANOVA should not be used.
:feedback-1: The rule of thumb compares the LARGEST to the SMALLEST standard deviation, and $8.7/3.1 \approx 2.8 > 2$.
* *No—the largest standard deviation is more than twice the smallest
* Yes—all standard deviations are below 10
:::
