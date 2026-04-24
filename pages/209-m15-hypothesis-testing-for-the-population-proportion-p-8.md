# Hypothesis Testing for the Population Proportion p (8 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 4. Drawing Conclusions Based on the p-Value

This last part of the four-step process of hypothesis testing is the same across all statistical tests, and actually, we've already said basically everything there is to say about it, but it can't hurt to say it again.

The p-value is a measure of how much evidence the data present against H~o~. The smaller the p-value, the more evidence the data present against H~o~.

We already mentioned that what determines what constitutes enough evidence against H~o~ is the *significance level* (α), a cutoff point below which the p-value is considered small enough to reject H~o~ in favor of H~a~. The most commonly used significance level is 0.05.

It is important to mention again that this step has essentially two sub-steps:

1. Based on the p-value, determine whether or not the results are significant (i.e., the data present enough evidence to reject H~o~).
2. State your conclusions in the context of the problem.

Let's go back to our three examples and draw conclusions.

```{admonition} Example: 1
    (Has the proportion of defective products been reduced from 0.20 as a result of the repair?)

    We found that the p-value for this test was 0.023.

    Since 0.023 is small (in particular, 0.023 < 0.05), the data provide enough evidence to reject H~o~ and conclude that as a result of the repair the proportion of defective products has been reduced to below 0.20. The following figure is the complete story of this example, and includes all the steps we went through, starting from stating the hypotheses and ending with our conclusions:

    ```{figure} images/image275.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = 0.20 and H_a: p &lt; 0.20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = 0.16, and z = -2 and p-value = 0.023. Since the p-value is small we conclude that H_0 can be rejected.

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = 0.20 and H_a: p &lt; 0.20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = 0.16, and z = -2 and p-value = 0.023. Since the p-value is small we conclude that H_0 can be rejected.
    ```
```

```{admonition} Example: 2
    (Is the proportion of students who use marijuana at the college higher than the national proportion, which is 0.157?)

    We found that the p-value for this test was 0.182.

    Since 0.182 is *not* small (in particular, 0.182 > 0.05), the data do not provide enough evidence to reject H~o~.

    We therefore do *not* have enough evidence to conclude that the proportion of students at the college who use marijuana is higher than the national figure. Here is the complete story of this example:

    ```{figure} images/image276.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = 0.157 and H_a: p &gt; 0.157. We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = 0.19, z = 0.91, and p-value = 0.182. Since the p-value is too large, we conclude that H_0 cannot be rejected.

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = 0.157 and H_a: p &gt; 0.157. We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = 0.19, z = 0.91, and p-value = 0.182. Since the p-value is too large, we conclude that H_0 cannot be rejected.
    ```
```

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Proportion p

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example: 3
    (Has the proportion of U.S. adults who support the death penalty for convicted murderers changed since 2003, when it was 0.64?)

    We found that the p-value for this test was 0.021.

    Since 0.021 is small (in particular, 0.021 < 0.05), the data provide enough evidence to reject H~o~, and we conclude that the proportion of adults who support the death penalty for convicted murderers has changed since 2003. Here is the complete story of this example:

    ```{figure} images/image277.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = 0.64 and H_a: p ≠ 0.64. We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = 0.675, z = 2.31, and p-value = 0.021. Because the p-value is small, we conclude that H_0 can be rejected.

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = 0.64 and H_a: p ≠ 0.64. We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = 0.675, z = 2.31, and p-value = 0.021. Because the p-value is small, we conclude that H_0 can be rejected.
    ```
```

##### Did I Get This?

Two hypothesis tests were conducted.

In test I, a significance level of 0.05 was used, and the p-value was calculated to be 0.025.

In test II, a significance level of 0.01 was used, and the p-value was calculated to be 0.025.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Many Students Wonder**

    Hypothesis Testing for the Population Proportion

    *(Interactive activity — available in the OLI platform)*
```
