# Hypothesis Testing for the Population Proportion p (9 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Let’s Summarize

We have now completed going through the four steps of hypothesis testing, and in particular, we learned how they are applied to the z-test for the population proportion. Let's briefly summarize:

##### Step 1

State the null and alternative hypotheses:

$H_{0}:p=p_{0}$

```{figure} images/image279.gif
:alt: H_a : p { one of &lt;, &gt;, or ≠ } p_0

H_a : p { one of &lt;, &gt;, or ≠ } p_0
```

where the choice of the appropriate alternative (out of the three) is usually quite clear from the context of the problem.

##### Step 2

Obtain data from a sample and:

(i) Check whether the data satisfy the conditions which allow you to use this test.

- Random sample (or at least a sample that can be considered random in context)
- *n* ⋅ *p*~0~ ≥ 10, *n* ⋅ (1 − *p*~0~) ≥ 10

(ii) Calculate the sample proportion $\hat{p}$, and summarize the data using the test statistic:

$z=\frac{\hat{p}−p_{0}}{\sqrt{\frac{p_{0}\left(1−p_{0}\right)}{n}}}$.

(*Recall:* This standardized test statistic represents how many standard deviations above or below $p_{0}$ our sample proportion $\hat{p}$ is. )

##### Step 3

Find the p-value of the test either by using software or by using the test statistic as follows:

* for $H_{a}:p<p_{0}:P\left(Z\leqz\right)$

* for $H_{a}:p>p_{0}:P\left(Z\geqz\right)$

* for $H_{a}:p\neqp_{0}:2P\left(Z\geq|z|\right)$

##### Step 4

Reach a conclusion first regarding the significance of the results, and then determine what it means in the context of the problem. Recall that:

If the p-value is small (in particular, smaller than the significance level, which is usually .05), the results are significant (in the sense that there is a significant difference between what was observed in the sample and what was claimed in H~o~), and so we reject H~o~. If the p-value is not small, we do not have enough statistical evidence to reject H~o~, and so we continue to believe that H~o~*may* be true. (Remember, in hypothesis testing we never "accept" H~o~).

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Proportion p

    *(Interactive activity — available in the OLI platform)*
```

What's next?

Before we move on to the next test, we use the z-test for proportions to bring up and illustrate some very important issues regarding hypothesis testing.
