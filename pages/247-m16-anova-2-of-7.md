# ANOVA (2 of 7)

```{admonition} Learning Objectives
    - Specify the null and alternative hypotheses for comparing groups.
```

## The ANOVA F-test

Now that we understand in what kind of situations ANOVA is used, we are ready to learn how it works, or more specifically, what the idea is behind comparing more than two means. As we mentioned earlier, the test that we will present is called the ANOVA F-test, and as you'll see, this test is different in two ways from all the tests we have presented so far:

- Unlike the previous tests, where we had three possible alternative hypotheses to choose from
                        (depending on the context of the problem), in the ANOVA F-test there is only
                        one alternative, which actually makes life simpler.
- The test statistic will not have the same structure as the test statistics we've seen so far. In
                        other words, it will not have the form: $\frac{sample statistic−null value}{standard error}$ , but a different structure that  captures the essence of the
                        F-test, and clarifies where the name "analysis of variance" is coming from.

Let's start.

## Step 1: Stating the Hypotheses

The null hypothesis claims that there is no relationship between X and Y. Since the relationship is examined by comparing$\mu_{1},\mu_{2},\mu_{3},...,\mu_{k}$, the means of Y in the populations defined by the values of X, no relationship would mean that all the means are equal. Therefore the null hypothesis of the F-test is: $H_{0}:\mu_{1}=\mu_{2}=...=\mu_{k}$

As we mentioned earlier, here we have just one alternative hypothesis, which claims that there *is* a relationship between X and Y. In terms of the means $\mu_{1},\mu_{2},\mu_{3},...,\mu_{k}$, it simply says the opposite of the alternative, that not all the means are equal, and we simply write:$H_{a}:not all the \mu's are equal$.

```{admonition} Example
    Recall our "Is academic frustration related to major?" example:

    ```{figure} images/image100.gif
    :alt: The X variable is major, and it has four categories, which are Business, English, Mathematics, and Psychology. We have four populations, one for each of these categories. We are interested in the level of frustration (Y) mean for each population, so we have 4 μ, one for each population. For each population we take a sample of size 35, resulting in 4 separate samples.

    The X variable is major, and it has four categories, which are Business, English, Mathematics, and Psychology. We have four populations, one for each of these categories. We are interested in the level of frustration (Y) mean for each population, so we have 4 μ, one for each population. For each population we take a sample of size 35, resulting in 4 separate samples.
    ```

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```

    The correct hypotheses for our example are:

    ```{figure} images/image101.gif
    :alt: H_0: μ_1 = μ_2 = μ_3 = μ_4, H_a: not all the μ's are equal

    H_0: μ_1 = μ_2 = μ_3 = μ_4, H_a: not all the μ's are equal
    ```

    Note that there are many ways for $\mu_{1},\mu_{2},\mu_{3},\mu_{4}$ not to be all equal, and	$\mu_{1}\neq\mu_{2}\neq\mu_{3}\neq\mu_{4}$	is just one of them. Another way could be	$\mu_{1}=\mu_{2}=\mu_{3}\neq\mu_{4}$ or	$\mu_{1}=\mu_{2}\neq\mu_{3}=\mu_{4}$. The alternative of the ANOVA F-test simply states that not all of the means are equal, and is not specific about the way in which they are different.
```

Before we move on to the next step (checking conditions and summarizing the data with a test statistic), we will present the idea behind the ANOVA F-test using our example.
