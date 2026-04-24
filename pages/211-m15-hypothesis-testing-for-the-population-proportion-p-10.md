# Hypothesis Testing for the Population Proportion p (10 of 13)

```{admonition} Learning Objectives
    - Apply the concepts of: sample size, statistical significance vs. practical importance, and the relationship between hypothesis testing and confidence intervals.
```

## More About Hypothesis Testing

The issues regarding hypothesis testing that we will discuss are:

1. The effect of sample size on hypothesis testing.

2. Statistical significance vs. practical importance. (This will be discussed in the activity following number 1.)

3. One-sided alternative vs. two-sided alternative—understanding what is going on.

4. Hypothesis testing and confidence intervals—how are they related?

Let's start.

## 1. The Effect of Sample Size on Hypothesis Testing

We have already seen the effect that the sample size has on inference, when we discussed point and interval estimation for the population mean (μ) and population proportion (p). Intuitively...

Larger sample sizes give us more information to pin down the true nature of the population. We can therefore expect the *sample* mean and *sample* proportion obtained from a larger sample to be closer to the population mean and proportion, respectively. As a result, for the same level of confidence, we can report a smaller margin of error, and get a narrower confidence interval. What we've seen, then, is that larger sample size gives a boost to how much we trust our sample results. In hypothesis testing, larger sample sizes have a similar effect. The following two examples will illustrate that a larger sample size provides more convincing evidence, and how the evidence manifests itself in hypothesis testing. Let's go back to our example 2 (marijuana use at a certain liberal arts college).

```{admonition} Example: 2
    ```{figure} images/image276.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19, z = .91, and p-value = .182 . Since the p-value is too large we conclude that H_0 cannot be rejected.

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19, z = .91, and p-value = .182 . Since the p-value is too large we conclude that H_0 cannot be rejected.
    ```

    The data *do not* provide enough evidence that the proportion of marijuana users at the college is higher than the proportion among all U.S. college students, which is .157. So far, nothing new. Let's make small changes to the problem (and call it example 2*). The changes are highlighted and the problem is followed by a new figure that reflects the changes.
```

```{admonition} Example: 2*
    There are rumors that students in a certain liberal arts college are more inclined to use drugs than U.S. college students in general. Suppose that *in a simple random sample of 400 students from the college, 76 admitted to marijuana use*. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is .157? (reported by the Harvard School of Public Health).

    ```{figure} images/image288.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana.

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana.
    ```

    We now have a larger sample (400 instead of 100), and also we changed the number of marijuana users (76 instead of 19).

    Let's carry out the test in this case.

    *I.* The question of interest did not change, so we are testing the same hypotheses:

    H~o~: p = .157

    H~a~: p > .157

    *II.* We select a random sample of size *400* and find that 76 are marijuana users.

    (Note that the data satisfy the conditions that allow us to use this test. Verify this yourself).

    Let's summarize the data:

    ```{figure} images/image289.gif
    :alt: p-hat = 76/400 = .19

    p-hat = 76/400 = .19
    ```

    This is the same sample proportion as in the original problem, so it seems that the data give us the same evidence, but when we calculate the test statistic, we see that actually this is not the case:

    ```{figure} images/image290.gif
    :alt: z = (.19 - .157) / √[( .157 (1 - .157) )/400 ] ≈ 1.81

    z = (.19 - .157) / √[( .157 (1 - .157) )/400 ] ≈ 1.81
    ```

    Even though the sample proportion is the same (.19), since here it is based on a larger sample (400 instead of 100), it is 1.81 standard deviations above the null value of .157 (as opposed to .91 standard deviations in the original problem).

    *III.* For the p-value, we use statistical software to find p-value = 0.035.

    The p-value here is .035 (as opposed to .182 in the original problem). In other words, when H~o~ is true (i.e. when p=.157) it is quite unlikely (probability of .035) to get a sample proportion of .19 or higher based on a sample of size 400 (probability .035), and not very unlikely when the sample size is 100 (probability .182).

    *IV.*

    Our results here are significant. In other words, in example 2* the data provide enough evidence to reject H~o~ and conclude that the proportion of marijuana users at the college is higher than among all U.S. students.

    Let's summarize with a figure:

    ```{figure} images/image291.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana. Conditions are met to use our method, so p-hat = 76/400 = .19, z = 1.81, and p-value = .035 . The p-value is low enough to let us conclude that we can reject H_0.

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana. Conditions are met to use our method, so p-hat = 76/400 = .19, z = 1.81, and p-value = .035 . The p-value is low enough to let us conclude that we can reject H_0.
    ```
```

What do we learn from these two examples?

We see that sample results that are based on a larger sample carry more weight.

In example 2, we saw that a sample proportion of .19 based on a sample of size of 100 was not enough evidence that the proportion of marijuana users in the college is higher than .157. Recall, from our general overview of hypothesis testing, that this conclusion (not having enough evidence to reject the null hypothesis) *doesn't* mean the null hypothesis is necessarily true (so, we never “accept” the null); it only means that the particular study didn’t yield sufficient evidence to reject the null. It *might* be that the sample size was simply too small to detect a statistically significant difference.

However, in example 2*, we saw that when the sample proportion of .19 is obtained from a sample of size 400, it carries much more weight, and in particular, provides enough evidence that the proportion of marijuana users in the college is higher than .157 (the national figure). In *this* case, the sample size of 400 *was* large enough to detect a statistically significant difference.

The following activity will allow you to practice the ideas and terminology used in hypothesis testing when a result is not statistically significant.

##### Learn By Doing

Suppose that only 40% of the U.S. public supported the general direction of the previous U.S. administration's policies. To gauge whether the nationwide proportion, p, of support for the *current* administration is higher than 40%, a major polling organization conducts a random poll to test the hypotheses:

H~o~: p = .40

H~a~: p > .40

The results are reported to be *not statistically significant*, with a*p-value of .214*.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Now, we will address the issue of statistical significance versus practical importance (which also involves issues of sample size).

The following activity will let you explore the effect of the sample size on the significance of the results yourself, and more importantly will discuss issue *2: Statistical significance vs. practical importance.*

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Proportion p

    *(Interactive activity — available in the OLI platform)*
```
