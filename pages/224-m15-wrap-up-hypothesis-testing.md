# Wrap-Up (Hypothesis Testing)

This module covered the z-test for population proportion and both the z-test and t-test for the population mean. The following table summarizes when each of the tests are used:

```{figure} images/tests.png
:alt: A table of types of hypothesis tests and the circumstances in which they are used. Here is the data in the table: A z-test for the Population Proportion is used when: * testing the population proportion(p) * variable of interest is categorical * population proportion is unknown A z-test for the Population Mean is used when: * testing the Population Mean (μ) * Variable of interest is Quantitative * Population standard deviation is known (σ) A t-test for the Population mean is used when: * Testing the Population Mean (μ) * Response Variable is Quantitative * Population standard deviation is unknown, so sample standard deviation is used (s) instead.

A table of types of hypothesis tests and the circumstances in which they are used. Here is the data in the table: A z-test for the Population Proportion is used when: * testing the population proportion(p) * variable of interest is categorical * population proportion is unknown A z-test for the Population Mean is used when: * testing the Population Mean (μ) * Variable of interest is Quantitative * Population standard deviation is known (σ) A t-test for the Population mean is used when: * Testing the Population Mean (μ) * Response Variable is Quantitative * Population standard deviation is unknown, so sample standard deviation is used (s) instead.
```

The module is also loaded with very important ideas that apply to the general process of hypothesis testing. Thus, the following summary discusses each of the above named hypothesis tests within the context of the hypothesis testing process.

The process of hypothesis testing has four steps:

*I. Stating the null and alternative hypotheses (Ho and Ha).*

| *Type of Hypothesis Test* | *Null Hypothesis* | *Alternative Hypothesis* |
| --- | --- | --- |
| z-test for the Population Proportion | H~0~:*p*=*p*~0~ | H~a~:*p*≠*p*~0                 ~*or*H~a~:*p*<*p*~0 ~*or*Ha*:p*>*p*~0~ |
| z-test for the Population Mean | H~0~:μ=μ~0~ | H~a~:μ≠μ~0 ~*or*H~a~:μ<μ~0 ~*or*H~a~:μ>μ~0~ |
| t-test for the Population Mean | H~0~:μ=μ~0~ | H~a~:μ≠μ~0 ~*or*H~a~:μ<μ~0 ~*or*H~a~:μ>μ~0~ |

*II. Obtaining a random sample (or at least one that can be considered random) and collecting data. Using the data:*

***Check that the conditions under which the test can be reliably used are met.**

For the *z-test for the Population Proportion*, we can reliably use the test is if the following conditions holds: *np**~0~*≥ 10*and n(1-p**~0~**)*≥ 10

For the *z-test for the Population Mean*and the *t-test for the Population Mean*, the following table is a summary the conditions under which they can be reliably used, and which test to use when:

```{figure} images/image387.png
:alt: A table. Here is the data in the table: With large sample size (regardless of whether the population is normal or not), we use the z-test if sigma is known, otherwise we use the t-test, keeping in mind that the z-test is a good approximation. With a small sample size, and normal population(* footnote), the z-test is used when we know sigma, and when we don't, we use the t-test. With a small sample size which has a population shape which is not normal or is unknown, we can't use the z-test or t-test. (*)Footnote: by "Population normal" we mean that either the population is known to be normal, or else that the population can be reasonably assumed to be normal as judged by the shape of the data histogram.

A table. Here is the data in the table: With large sample size (regardless of whether the population is normal or not), we use the z-test if sigma is known, otherwise we use the t-test, keeping in mind that the z-test is a good approximation. With a small sample size, and normal population(* footnote), the z-test is used when we know sigma, and when we don't, we use the t-test. With a small sample size which has a population shape which is not normal or is unknown, we can't use the z-test or t-test. (*)Footnote: by "Population normal" we mean that either the population is known to be normal, or else that the population can be reasonably assumed to be normal as judged by the shape of the data histogram.
```

***Summarize the data using a test statistic.**

The test statistic is a measure of the evidence in the data against the H~o~. The larger the test statistic is in magnitude, the more evidence the data present against the H~o~.

| *Hypothesis**Test* | *Test Statistic* |
| --- | --- |
| z-test for the Population Proportion | $z=\frac{\hat{p}−p_{0}}{\sqrt{\frac{p_{0}(1−p_{0})}{n}}}$ |
| z-test for the Population Mean | $z=\frac{\bar{x}−\mu_{0}}{\frac{\sigma}{\sqrt{n}}}$ |
| t-test for the Population Mean | $t=\frac{\bar{x}−\mu_{0}}{\frac{s}{\sqrt{n}}}$ |

*III. Finding the p-value of the test.*

The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against H~o~. The smaller the p-value, the more evidence the data present against H~o~.

In this module, we learned how to compute the p-value for the two z-tests (z-test for the population proportion and the z-test for the population mean). However, for the t-test (and, actually, from this point on in the course), we will use software to find the p-value for us.

*IV. Making conclusions.*

**-Conclusions about the significance of the results:**

If the p-value is small, the data present enough evidence to reject H~0~ (and accept H~a~).

If the p-value is not small, the data do not provide enough evidence to reject H~0~.

To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at .05, but should not be considered inviolable.

Conclusions should always be made in the context of the problem.

*Additional ‘Big Ideas’ about hypothesis Testing.*

**Note:* These ideas were already mentioned in the summary for hypothesis testing for the population proportion p, however it is worth repeating them and thus stress that these idea apply to hypothesis testing in general!*

Results that are based on a larger sample carry more weight, and therefore results that are not significant (do not provide evidence to reject H~0~) may become significant if based on a larger sample size. As a result...

Even a very small and practically unimportant effect becomes statistically significant with a large enough sample size. The distinction between statistical significance and practical importance should therefore always be considered.

For given data, the p-value of the two-sided test is always twice as large as the p-value of the one-sided test. It is therefore harder to reject H~0~in the two-sided case than it is in the one-sided case in the sense that stronger evidence is required. Intuitively, the hunch or information that leads us to use the one-sided test can be regarded as a head-start toward the goal of rejecting H~0~.

*95% confidence intervals*can be used in order to carry out *two-sided tests* (at the .05 significance level). If the null value is not included in the confidence interval (i.e., is not one of the plausible values for the parameter), we have enough evidence to reject H~0~. Otherwise, we cannot reject H~0~.

If the results are significant, it might be of interest to follow up the tests with a confidence interval in order to get insight into the actual value of the parameter of interest.

The following StatTutor exercise is the first one in which the "More Formal Analysis" (i.e., "inference") node is active. This exercise will therefore give you a chance to practice some of the methods you learned, but most importantly, will give you a sense of how inference fits into and completes the big picture of statistics.

```{note}
    **Lab**

    Cell Phones

    *(Interactive activity — available in the OLI platform)*
```

## End of Section Questions

```{note}
    **My Response**

    About Inference for One Variable

    *(Interactive activity — available in the OLI platform)*
```
