# Hypothesis Testing for the Population Mean (9 of 9)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

For comparison purposes, we will use a modified version of the two problems we used in the previous case. We'll first introduce the modified versions and explain the changes.

```{admonition} Example: 1
    The SAT is constructed so that scores have a national average of 500. The distribution is close to normal. The dean of students of Ross College suspects that in recent years the college attracts students who are more quantitatively inclined. A random sample of 4 students entering Ross college had an average math SAT (SAT-M) score of 550, and a sample standard deviation of 100. Does this provide enough evidence for the dean to conclude that the mean SAT-M of all Ross College students is higher than the national mean of 500?

    Here is a figure that represents this example where the changes are marked in blue:

    ```{figure} images/image372.gif
    :alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. The question we need to answer is "is the mean SAT-M 500 (national mean) or is it higher?" We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550, and S = 100.

    A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. The question we need to answer is "is the mean SAT-M 500 (national mean) or is it higher?" We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550, and S = 100.
    ```

    Note that the problem was changed so that the population standard deviation (which was assumed to be 100 before) is now unknown, and instead we assume that the sample of 4 students produced a sample mean of 550 (no change) and a sample standard deviation of s=100. (Sample standard deviations are never such nice rounded numbers, but for the sake of comparison we left it as 100.) Note that due to the changes, the z-test for the population mean is no longer appropriate, and we need to use the t-test.
```

```{admonition} Example: 2
    A certain prescription medicine is supposed to contain an average of 250 parts per million (ppm) of a certain chemical. If the concentration is higher than this, the drug may cause harmful side effects; if it is lower, the drug may be ineffective. The manufacturer runs a check to see if the mean concentration in a large shipment conforms to the target level of 250 ppm or not. A simple random sample of 100 portions is tested, and the sample mean concentration is found to be 247 ppm with a sample standard deviation of 12 ppm. Again, here is a figure that represents this example where the changes are marked in blue:

    ```{figure} images/image373.gif
    :alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. We need to answer "is the mean concentration the required 250ppm or not?" Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247 and S=12.

    A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. We need to answer "is the mean concentration the required 250ppm or not?" Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247 and S=12.
    ```

    The changes are similar to example 1: we no longer assume that the population standard deviation is known, and instead use the sample standard deviation of 12. Again, the problem was thus changed from a z-test problem to a t-test problem.

    However, as we mentioned earlier, due to the large sample size (n = 100) there should not be much difference whether we use the z-test or the t-test. The sample standard deviation, s, is expected to be close enough to the population standard deviation $\sigma$ . We'll see this as we solve the problem.
```

Let's carry out the t-test for both of these problems:

*Example 1:*

1. There are no changes in the hypotheses being tested:

```{figure} images/image374.gif
:alt: H_0: μ = 500, H_a: μ > 500

H_0: μ = 500, H_a: μ > 500
```

2. The conditions that allow us to use the t-test are met since:

(i) The sample is random.

(ii) SAT-M is known to vary normally in the population (which is crucial here, since the sample size is only 4).

In other words, we are in the following situation:

```{figure} images/image328.gif
:alt: A table which has two columns and two rows, and is titled "Conditions: z-test for a population mean." The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally in the population" and "Variable doesn't vary normally in the population." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally in the population, Small sample size: OK (this is the case this example falls in); Variable varies normally in the population, Large sample size: OK; Variable doesn't vary normally in the population, Small sample size: NOT OK; Variable doesn't vary normally in the population, Large sample size: OK;

A table which has two columns and two rows, and is titled "Conditions: z-test for a population mean." The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally in the population" and "Variable doesn't vary normally in the population." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally in the population, Small sample size: OK (this is the case this example falls in); Variable varies normally in the population, Large sample size: OK; Variable doesn't vary normally in the population, Small sample size: NOT OK; Variable doesn't vary normally in the population, Large sample size: OK;
```

The test statistic is $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}=\frac{550−500}{\frac{100}{\sqrt{4}}}=1$

The data (represented by the sample mean) are 1 standard error above the null value.

3. Finding the p-value.

Recall that in general the p-value is calculated under the null distribution of the test statistic, which,

in the t-test case, is t(n-1). In our case, in which n = 4, the p-value is calculated under the t(3) distribution:

```{figure} images/image376.gif
:alt: A t(3) distribution with t-scores 0 and 1 marked. The p-value is the area under the curve to the right of t-score 1.

A t(3) distribution with t-scores 0 and 1 marked. The p-value is the area under the curve to the right of t-score 1.
```

Using statistical software, we find that the p-value is 0.196. For comparison purposes, the p-value that we got when we carried out the z-test for this problem (when we assumed that 100 is the known $\sigma$ rather the calculated sample standard deviation, s) was 0.159.

It is not surprising that the p-value of the t-test is larger, since the t distribution has fatter tails. Even though in this particular case the difference between the two values does not have practical implications (since both are large and will lead to the same conclusion), the difference is not trivial.

4. Making conclusions.

The p-value (0.196) is large, indicating that the results are not significant. The data do not provide enough evidence to conclude that the mean SAT-M among Ross College students is higher than the national mean (500).

Here is a summary:

```{figure} images/image377.gif
:alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ > 500. We take a sample of size n = 4 from the population, represented by a smaller circle. For this sample, we calculate that x-bar = 550 and S = 100. Our conditions are met, so we can find t = 1, and p-value = .196 . This p-value is too high, so the conclusion is that H_0 cannot be rejected.

A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ > 500. We take a sample of size n = 4 from the population, represented by a smaller circle. For this sample, we calculate that x-bar = 550 and S = 100. Our conditions are met, so we can find t = 1, and p-value = .196 . This p-value is too high, so the conclusion is that H_0 cannot be rejected.
```

Example 2:

1. There are no changes in the hypotheses being tested:

```{figure} images/image320.gif
```

2. The conditions that allow us to use the t-test are met:

(i) The sample is random

(ii) The sample size is large enough for the Central Limit Theorem to apply and ensure the normality of $\bar{X}$. In other words, we are in the following situation:

```{figure} images/image333.gif
:alt: The same table as before. The case this example is in is the "Variable doesn't vary normally in the population, Large sample size" case. The table has two columns and two rows, and is titled "Conditions: z-test for a population mean." The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally in the population" and "Variable doesn't vary normally in the population." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn't vary normally in the population, Small sample size: NOT OK; Variable doesn't vary normally in the population, Large sample size: OK (this is the case this example falls in);

The same table as before. The case this example is in is the "Variable doesn't vary normally in the population, Large sample size" case. The table has two columns and two rows, and is titled "Conditions: z-test for a population mean." The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally in the population" and "Variable doesn't vary normally in the population." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn't vary normally in the population, Small sample size: NOT OK; Variable doesn't vary normally in the population, Large sample size: OK (this is the case this example falls in);
```

The test statistic is: $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}=\frac{247−250}{\frac{12}{\sqrt{100}}}=−2.5$

The data (represented by the sample mean) are 2.5 standard errors below the null value.

3. Finding the p-value.

```{figure} images/image379.gif
:alt: A t(99) curve, for which the horizontal axis has been labeled with t-scores of -2.5 and 2.5 . The area under the curve and to the left of -2.5 and to the right of 2.5 is the p-value.

A t(99) curve, for which the horizontal axis has been labeled with t-scores of -2.5 and 2.5 . The area under the curve and to the left of -2.5 and to the right of 2.5 is the p-value.
```

To find the p-value we use statistical software, and we calculate a p-value of 0.014 with a 95% confidence interval of (244.619, 249.381). For comparison purposes, the output we got when we carried out the z-test for the same problem was a p-value of 0.012 with a 95% confidence interval of (244.648, 249.352).

Note that here the difference between the p-values is quite negligible (.002). This is not surprising, since the sample size is quite large (n = 100) in which case, as we mentioned, the z-test (in which we are treating s as the known $\sigma$ ) is a very good approximation to the t-test. Note also how the two 95% confidence intervals are similar (for the same reason).

4. Conclusions:

The p-value is small (.014) indicating that at the 5% significance level, the results are significant. The data therefore provide evidence to conclude that the mean concentration in entire shipment is not the required 250.

Here is a summary:

```{figure} images/image380.gif
:alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that t = -2.5, and that the p-value = .014. This p-value is low enough to let us conclude that we can reject H_0.

A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that t = -2.5, and that the p-value = .014. This p-value is low enough to let us conclude that we can reject H_0.
```

## Comments

1. The 95% confidence interval for $\mu$ can be used here in the same way it is used when $\sigma$ is known: either as a way to conduct the two-sided test (checking whether the null value falls inside or outside the confidence interval) or following a t-test where H~o~ was rejected (in order to get insight into the value of $\mu$ ).

2. While it is true that when $\sigma$ is unknown and for large sample sizes the z-test is a good approximation for the t-test, since we are using software to carry out the t-test anyway, there is not much gain in using the z-test as an approximation instead. We might as well use the more exact t-test regardless of the sample size.

However, it is always worthwhile knowing what happens behind the scenes.

##### Did I Get This?

A group of Internet users 50-65 years of age were randomly chosen and asked to report the weekly number of hours they spend online. The purpose of the study was to determine whether the mean weekly number of hours that Internet users in that age group spend online differs from the mean for Internet users in general, which is 12.5 (as reported by "The Digital Future Report: Surveying the Digital Future, Year Four"). The following information is available:

```{figure} images/image396.gif
:alt: One-Sample T: hr. online. Test of mu = 12.5 vs mu not = 12.5 Variable: hr. online N: 125 Mean: 12.008 StDev: 3.214 SE Mean: 0.287 95% CI: (11,439, ) T: -1.71 P: 0.090

One-Sample T: hr. online. Test of mu = 12.5 vs mu not = 12.5 Variable: hr. online N: 125 Mean: 12.008 StDev: 3.214 SE Mean: 0.287 95% CI: (11,439, ) T: -1.71 P: 0.090
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Mean

    *(Interactive activity — available in the OLI platform)*
```

## To Summarize

1. In hypothesis testing for the population mean ($\mu$ ), we distinguish between two cases:

I. The less common case when the population standard deviation ($\sigma$) is known.

II. The more practical case when the population standard deviation is unknown and the sample standard deviation (s) is used instead.

2. In the case when $\sigma$ is known, the test for $\mu$ is called the z-test, and in case when $\sigma$ is unknown and s is used instead, the test is called the t-test.

3. In both cases, the null hypothesis is: $H_{0}:\mu=\mu_{0}$

and the alternative, depending on the context, is one of the following:

$H_{a}:\mu<\mu_{0}$, or $H_{a}:\mu>\mu_{0}$, or $H_{a}:\mu\neq\mu_{0}$

4. Both tests can be safely used as long as the following two conditions are met:

(i) The sample is random (or can at least be considered random in context).

(ii) Either the sample size is large (n > 30) or, if not, the variable of interest can be assumed to vary normally in the population.

5. In the z-test, the test statistic is:

$z=\frac{\bar{X}−\mu_{0}}{\frac{\sigma}{\sqrt{n}}}$

whose null distribution is the standard normal distribution (under which the p-values are calculated).

6. In the t-test, the test statistic is:

$t=\frac{\bar{X}−\mu_{0}}{\frac{s}{\sqrt{n}}}$

whose null distribution is t(n - 1) (under which the p-values are calculated).

7. For large sample sizes, the z-test is a good approximation for the t-test.

8. Confidence intervals can be used to carry out the two-sided test $H_{a}:\mu\neq\mu_{0}$, and in cases where H~o~ is rejected, the confidence interval can give insight into the value of the population mean ($\mu$).

9. Here is a summary of which test to use under which conditions:

```{figure} images/image387.png
:alt: A table. Here is the data in the table: With large sample size (regardless of whether the population is normal or not), we use the z-test if sigma is known, otherwise we use the t-test, keeping in mind that the z-test is a good approximation. With a small sample size, and normal population(* footnote), the z-test is used when we know sigma, and when we don't, we use the t-test. With a small sample size which has a population shape which is not normal or is unknown, we can't use the z-test or t-test. (*)Footnote: by "Population normal" we mean that either the population is known to be normal, or else that the population can be reasonably assumed to be normal as judged by the shape of the data histogram.

A table. Here is the data in the table: With large sample size (regardless of whether the population is normal or not), we use the z-test if sigma is known, otherwise we use the t-test, keeping in mind that the z-test is a good approximation. With a small sample size, and normal population(* footnote), the z-test is used when we know sigma, and when we don't, we use the t-test. With a small sample size which has a population shape which is not normal or is unknown, we can't use the z-test or t-test. (*)Footnote: by "Population normal" we mean that either the population is known to be normal, or else that the population can be reasonably assumed to be normal as judged by the shape of the data histogram.
```

The following activity will reinforce the topics illustrated in the graphic above.

## Learn By Doing

*Scenario:*The Intel Corporation is conducting quality control on its circuit boards. Thickness of the manufactured circuit boards varies unavoidably from board to board. Suppose the thickness of the boards produced by a certain factory process varies normally. The distribution of thickness of the circuit boards is supposed to have the mean μ = 12 mm if the manufacturing process is working correctly. A random sample of five circuit boards is selected and measured, and the average thickness is found to be 9.13 mm, and the standard deviation for the sample is computed to be 1.11 mm.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Now, suppose that Intel is testing a brand new manufacturing process, for which prior information wasn’t available. In particular, for this new process, *the population distribution’s shape isn’t known*. Use the following histograms to help you answer the question below.

```{figure} images/image502.gif
:alt: 4 Histograms, all titled "Histogram of thickness (mm)," with a vertical axis for frequency and horizontal axis for thickness (mm). Histogram A roughly follows a normal shape and has the following data, organized in "thickness: frequency" order: 8: 1.0 9: 2.0 10: 3.0 11: 2.0 12: 1.0 Histogram B is right-skewed: 8: 7 9: 8 10: 5 11: 3 12: 2 13: 2 14: 2 15: 1 16: 1 17: 1 18: 1 19: 1 20: 1 Histogram C is also right skewed: (same data as Histogram B) Histogram D is right skewed: 8: 3.0 9: 2.0 10: 1.0 11: 1.0 12: 1.0 13: 1.0

4 Histograms, all titled "Histogram of thickness (mm)," with a vertical axis for frequency and horizontal axis for thickness (mm). Histogram A roughly follows a normal shape and has the following data, organized in "thickness: frequency" order: 8: 1.0 9: 2.0 10: 3.0 11: 2.0 12: 1.0 Histogram B is right-skewed: 8: 7 9: 8 10: 5 11: 3 12: 2 13: 2 14: 2 15: 1 16: 1 17: 1 18: 1 19: 1 20: 1 Histogram C is also right skewed: (same data as Histogram B) Histogram D is right skewed: 8: 3.0 9: 2.0 10: 1.0 11: 1.0 12: 1.0 13: 1.0
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## End-of-Lesson
                Questions

```{note}
    **My Response**

    About Hypothesis Testing

    *(Interactive activity — available in the OLI platform)*
```
