# The ANOVA F-Test: Stating the Hypotheses

```{admonition} Learning Objectives
:class: note

- Specify the null and alternative hypotheses for comparing groups.
```

## The ANOVA F-Test

Now that we understand in what kind of situations ANOVA is used, we are ready to learn how it works—or more specifically, what the idea is behind comparing more than two means. As we mentioned earlier, the test that we will present is called the ANOVA F-test, and as you'll see, this test is different in two ways from all the tests we have presented so far:

- Unlike the previous tests, where we had three possible alternative hypotheses to choose from (depending on the context of the problem), in the ANOVA F-test there is only *one* alternative, which actually makes life simpler.
- The test statistic will not have the same structure as the test statistics we've seen so far. In other words, it will not have the form $\frac{\text{sample statistic}-\text{null value}}{\text{standard error}}$, but a different structure that captures the essence of the F-test and clarifies where the name "analysis of variance" comes from.

Let's start.

## Step 1: Stating the Hypotheses

The null hypothesis claims that there is no relationship between X and Y. Since the relationship is examined by comparing $\mu_1, \mu_2, \ldots, \mu_k$ (the means of Y in the populations defined by the values of X), no relationship would mean that all the means are equal. Therefore the null hypothesis of the F-test is:

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k$$

As we mentioned earlier, here we have just one alternative hypothesis, which claims that there *is* a relationship between X and Y. In terms of the means, it simply says the opposite of the null—that not all the means are equal—and we simply write:

$$H_a: \text{not all the } \mu\text{'s are equal}$$

:::{admonition} Example: Is "Academic Frustration" Related to Major?
:class: tip

Recall our example, in which we compare the mean frustration levels of four majors (Business, English, Mathematics, Psychology) using independent samples of size 35 from each. The correct hypotheses for our example are:

$$H_0: \mu_1 = \mu_2 = \mu_3 = \mu_4$$

$$H_a: \text{not all the } \mu\text{'s are equal}$$

Note that there are many ways for $\mu_1, \mu_2, \mu_3, \mu_4$ not to be all equal, and $\mu_1 \neq \mu_2 \neq \mu_3 \neq \mu_4$ is just one of them. Another way could be $\mu_1 = \mu_2 = \mu_3 \neq \mu_4$, or $\mu_1 = \mu_2 \neq \mu_3 = \mu_4$. The alternative of the ANOVA F-test simply states that not all of the means are equal, and is not specific about the way in which they are different.
:::

## Check Your Understanding: The ANOVA Hypotheses

:::{quiz} A study compares the mean recovery times of patients on four different physical-therapy programs. Suppose the truth is that programs 1, 2, and 3 have identical mean recovery times, but program 4's mean is shorter. Is the null hypothesis of the ANOVA F-test true or false in this situation?
:hint: H₀ requires ALL the means to be equal.
:feedback-0: Correct! H₀ says all four means are equal; if even one differs, H₀ is false and the alternative ("not all equal") is true.
:feedback-1: Even though three means are equal, the fourth differs—so it is NOT the case that all the means are equal.
:feedback-2: The alternative doesn't require all means to differ from each other—only that they are not all equal.
* *False—the alternative holds, since not all four means are equal
* True—most of the means are equal
* Neither—ANOVA cannot handle this configuration
:::

Before we move on to the next step (checking conditions and summarizing the data with a test statistic), we will present the idea behind the ANOVA F-test using our example.
