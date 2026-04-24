# Conclusion of Case C→Q

We are now done with case C→Q. We learned that this case is further classified into sub-cases, depending on the number of groups that we are comparing (i.e., the number of categories that the explanatory variable has), and the design of the study (independent vs. dependent samples). For each of the three sub-cases that we covered, we learned the appropriate inferential method, and emphasized the idea behind the method, the conditions under which it can be safely used, how to carry it out using software, and the interpretation of the results.

The following table summarizes when each of the three sub-cases, covered in this module, are used:

```{figure} images/c-q_table.png
:alt: A Two-sample test is used in circumstances: * Categorical explanatory variable with two categories * Comparing two population means based on two independent samples * Either normal populations or large sample size A Paired t-test (special case of the one sample t-test) is used when: * Categorical explanatory variable with two categories * Comparing the two population means, when the samples are dependent on each other or "matched pairs." *Samples are dependent in the sense that every observation in one sample is linked to an observation in another sample. Examples of dependent samples include: -same subjects measured twice, -twins ANOVA is used when * Categorical explanatory variable with more than two categories. * Comparing more than two population means based on independent samples

A Two-sample test is used in circumstances: * Categorical explanatory variable with two categories * Comparing two population means based on two independent samples * Either normal populations or large sample size A Paired t-test (special case of the one sample t-test) is used when: * Categorical explanatory variable with two categories * Comparing the two population means, when the samples are dependent on each other or "matched pairs." *Samples are dependent in the sense that every observation in one sample is linked to an observation in another sample. Examples of dependent samples include: -same subjects measured twice, -twins ANOVA is used when * Categorical explanatory variable with more than two categories. * Comparing more than two population means based on independent samples
```

The following summary discusses each of the above named sub-cases of C→Q within the context of the hypothesis testing process.

*I. Stating the null and alternative hypotheses (H**~0~**and H**~a~**).*

```{figure} images/c-q_table2.png
:alt: In a Two-Sample t-test, the hypotheses are: H_0: μ_1 - μ_2 = 0 (or H_0: μ_1 = μ_2), and one of: * H_a: μ_1 - μ_2 < 0 (same as H_a: μ_1 < μ_2) * H_a: μ_1 - μ_2 > 0 (same as H_a: μ_1 > μ_2) * H_a: μ_1 - μ_2 ≠ 0 (same as H_a: μ_1 ≠ μ_2) For a paired t-test, the hypotheses are H_0: μ_d = 0, and one of: * H_a: μ_d < 0, * H_a: μ_d > 0, * H_0: μ_0 ≠ 0. For ANOVA, H_0: μ_0 = μ_2 = ... = μ_k, and H_a:not all μ's are equal

In a Two-Sample t-test, the hypotheses are: H_0: μ_1 - μ_2 = 0 (or H_0: μ_1 = μ_2), and one of: * H_a: μ_1 - μ_2 < 0 (same as H_a: μ_1 < μ_2) * H_a: μ_1 - μ_2 > 0 (same as H_a: μ_1 > μ_2) * H_a: μ_1 - μ_2 ≠ 0 (same as H_a: μ_1 ≠ μ_2) For a paired t-test, the hypotheses are H_0: μ_d = 0, and one of: * H_a: μ_d < 0, * H_a: μ_d > 0, * H_0: μ_0 ≠ 0. For ANOVA, H_0: μ_0 = μ_2 = ... = μ_k, and H_a:not all μ's are equal
```

*II. Check Conditions, and Summarize the Data Using a Test Statistic*

**Check that the conditions under which the test can be reliably used are met.*

For the Two-Sample t-test, the conditions are:

1. Two samples are independent and random
2. One of the following two scenarios:

- Both populations are normal
- Populations are not normal, but large sample size (>30)

For the Paired t-test (as a special case of a one-sample t-test), the conditions are:

1. The sample of differences is random (or at least can be considered so in
				context).
2. We are in one of the three situations marked with a green check mark in the
				following table:

```{figure} images/image074.gif
:alt: A table which has two columns and two rows. The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally" and "Variable doesn't vary normally." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally, Small sample size: OK (in this case, we should check normality visually using a histogram of the sample differences); Variable varies normally, Large sample size: OK; Variable doesn't vary normally, Small sample size: NOT OK; Variable doesn't vary normally, Large sample size: OK;

A table which has two columns and two rows. The column headings are: "Small Sample Size" and "Large Sample Size. " The row headings are "Variable varies normally" and "Variable doesn't vary normally." Here is the data in the table by cell in "Row, Column: Value" format: Variable varies normally, Small sample size: OK (in this case, we should check normality visually using a histogram of the sample differences); Variable varies normally, Large sample size: OK; Variable doesn't vary normally, Small sample size: NOT OK; Variable doesn't vary normally, Large sample size: OK;
```

For an ANOVA, the conditions are:

1. The samples drawn from each of the populations being compared are independent.
2. The response variable varies normally within each of the populations being compared.
				As is often the case, we do not have to worry about this assumption for large sample
				sizes.
3. The populations all have the same standard deviation.

**Summarize the data using a test statistic.*

| *Special Case of C→Q* | *Test Statistic* |
| --- | --- |
| Two-Sample t-test | $t=\frac{\left(\bar{y_{1}}−\bar{y_{2}}\right)−0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}$ |
| Paired t-test | $t=\frac{\bar{x_{d}}−0}{\frac{s_{d}}{\sqrt{n}}}$ |
| ANOVA | $F=\frac{Variation Among the Sample Means}{Variation Within the Groups}$ |

*III. Finding the p-value of the test*

Use statistical software to determine the p-value. The p-value is the probability of getting data like those observed (or even more extreme) assuming that the null hypothesis is true, and is calculated using the null distribution of the test statistic. The p-value is a measure of the evidence against H~0~. The smaller the p-value, the more evidence the data present against H~0~. The p-values for three C→Q tests are obtained from the output.

*IV. Making conclusions.*

*-Conclusions about the significance of the results:*

If the p-value is small, the data present enough evidence to reject H~o~ (and accept H~a~).

If the p-value is not small, the data do not provide enough evidence to reject H~0~.

To help guide our decision, we use the significance level as a cutoff for what is considered a small p-value. The significance cutoff is usually set at .05, but should not be considered inviolable.

Conclusions should always be stated in the context of the problem.

*Following the test...*

For a two-sample t-test, a *95% confidence interval*for μ~1~−μ~2 ~can be very insightful after a test has rejected the null hypothesis, and can also be used for testing in the two-sided case.

For a paired t-test, a *95% confidence interval*for μ~d ~can be very insightful after a test has rejected the null hypothesis, and can also be used for testing in the two-sided case.

If the ANOVA F-test has rejected the null hypothesis, looking at the *confidence intervals*for the population means that are in the output can provide visual insight into why the H~0~was rejected (i.e., which of the means differ).

The following StatTutor exercise will help you practice what you've learned.

```{note}
    **Lab**

    Analyzing Data From a Course's Grade Book

    *(Interactive activity — available in the OLI platform)*
```
