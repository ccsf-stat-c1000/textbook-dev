# Hypothesis Testing for the Population Proportion p (7 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

```{admonition} Example: 1
    ```{figure} images/image264.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = .20 and H_a: p &lt; .20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16, and z = -2.

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The two hypotheses are H_0: p = .20 and H_a: p &lt; .20. We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16, and z = -2.
    ```

    The p-value in this case is:

    * The probability of observing a test statistic as small as -2 or smaller, assuming that H~o~ is true.

    *OR (recalling what the test statistic actually means in this case),*

    * The probability of observing a sample proportion that is 2 standard deviations or more below $p_{0}=.20$, assuming that $p_{0}$ is the true population proportion.

    *OR, more specifically,*

    * The probability of observing a sample proportion of .16 or lower in a random sample of size 400, when the true population proportion is $p_{0}=.20$.

    In either case, the p-value is found as shown in the following figure:

    ```{figure} images/image266.gif
    :alt: A normal N(0,1) curve. Marked on the horizontal axis are z-scores of 0 and -2. We are interested in the area to the left of -2, which is the p-value.

    A normal N(0,1) curve. Marked on the horizontal axis are z-scores of 0 and -2. We are interested in the area to the left of -2, which is the p-value.
    ```

    To find $P\left(Z\leq−2\right)$ we can either use a table or software. Eventually, after we understand the details, we will use software to run the test for us and the output will give us all the information we need. The p-value that the statistical software provides for this specific example is 0.023. The p-value tells me that it is pretty unlikely (probability of .023) to get data like those observed (test statistic of -2 or less) assuming that H~o~ is true.
```

```{admonition} Example: 2
    ```{figure} images/image268.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19, and z = .91

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19, and z = .91
    ```

    The p-value in this case is:

    * The probability of observing a test statistic as large as .91 or larger, assuming that H~o~ is true.

    *OR (recalling what the test statistic actually means in this case),*

    * The probability of observing a sample proportion that is .91 standard deviations or more above $p_{0}=.157$, assuming that $p_{0}$ is the true population proportion.

    *OR, more specifically,*

    * The probability of observing a sample proportion of .19 or higher in a random sample of size 100, when the true population proportion is $p_{0}=.157$.

    In either case, the p-value is found as shown in the following figure:

    ```{figure} images/image270.gif
    :alt: A N(0,1) curve for the sampling distribution. Marked on the horizontal axis are z-scores of 0 and .91 . The p-value is the area under the curve to the right of .91 .

    A N(0,1) curve for the sampling distribution. Marked on the horizontal axis are z-scores of 0 and .91 . The p-value is the area under the curve to the right of .91 .
    ```

    Again, at this point we can either use a table or software to find that the p-value is 0.182.

    The p-value tells us that it is not very surprising (probability of .182) to get data like those observed (which yield a test statistic of .91 or higher) assuming that the null hypothesis is true.
```

```{admonition} Example: 3
    ```{figure} images/image271.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = .64 and H_a: p ≠ .64 . We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675, and z = 2.31

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The two hypothesis are H_0: p = .64 and H_a: p ≠ .64 . We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675, and z = 2.31
    ```

    The p-value in this case is:

    * The probability of observing a test statistic as large as 2.31 (or larger) or as small as -2.31 (or smaller), assuming that H~o~ is true.

    *OR (recalling what the test statistic actually means in this case),*

    * The probability of observing a sample proportion that is 2.31 standard deviations or more away from $p_{0}=.64$, assuming that $p_{0}$ is the true population proportion.

    *OR, more specifically,*

    * The probability of observing a sample proportion as different as .675 is from .64, or even more different (i.e. as high as .675 or higher or as low as .605 or lower) in a random sample of size 1,000, when the true population proportion is $p_{0}=.64$.

    In either case, the p-value is found as shown in the following figure:

    ```{figure} images/image274.gif
    :alt: A N(0,1) sampling distribution curve, with the z-scores -2.31, 0, and 2.31 marked on the horizontal axis. The p-value is the sum of the area under the curve to the left of -2.31 and the area under the curve to the right of 2.31

    A N(0,1) sampling distribution curve, with the z-scores -2.31, 0, and 2.31 marked on the horizontal axis. The p-value is the sum of the area under the curve to the left of -2.31 and the area under the curve to the right of 2.31
    ```

    Again, at this point we can either use a table or software to find that the p-value is 0.021.

    The p-value tells us that it is pretty unlikely (probability of .021) to get data like those observed (test statistic as high as 2.31 or higher or as low as -2.31 or lower) assuming that H~o~ is true.
```

## Comment

We've just seen that finding p-values involves probability calculations about the value of the test statistic assuming that H~o~ is true. In this case, when H~o~ is true, the values of the test statistic follow a standard normal distribution (i.e., the sampling distribution of the test statistic when the null hypothesis is true is N(0,1)). Therefore, p-values correspond to areas (probabilities) under the standard normal curve.

Similarly, in *any test*, p-values are found using the sampling distribution of the test statistic when the null hypothesis is true (also known as the "null distribution" of the test statistic). In this case, it was relatively easy to argue that the null distribution of our test statistic is N(0,1). As we'll see, in other tests, other distributions come up (like the t-distribution and the F-distribution), which we will just mention briefly, and rely heavily on the output of our statistical package for obtaining the p-values.

We've just completed our discussion about the p-value, and how it is calculated both in general and more specifically for the z-test for the population proportion. Let's go back to the four-step process of hypothesis testing and see what we've covered and what still needs to be discussed.

## The Four Steps in Hypothesis Testing

1. State the appropriate null and alternative hypotheses, H~o~ and H~a~.
2. Obtain a random sample, collect relevant data, and *check whether the data meet the conditions under which the test can be used.* If the conditions are met, summarize the data using a test statistic.
3. Find the p-value of the test.
4. Based on the p-value, decide whether or not the results are significant, and *draw your conclusions in context.*

With respect to the z-test the population proportion:

Step 1: Completed

Step 2: Completed

Step 3: Completed

Step 4: This is what we will work on next.

##### Learn By Doing

In 2007, a Gallup poll estimated that 45% of U.S. adults rated their financial situation as “good.” We want to know if the proportion is smaller this year. We gather a random sample of 100 U.S. adults this year and find that 39 rate their financial situation as “good.” Use the output from Minitab to complete the following statements about the p-value. Use numbers from the output to fill in the blanks.

```{figure} images/1_img5.gif
:alt: Test and CI for One Proportion. Test of p = 0.45 vs p &lt; 0.45 Sample: 1: X = 39 N = 100 Sample p = 0.390000 95% Upper Bound = 0.485600 Z-Value = -1.21 P-Value = 0.114

Test and CI for One Proportion. Test of p = 0.45 vs p &lt; 0.45 Sample: 1: X = 39 N = 100 Sample p = 0.390000 95% Upper Bound = 0.485600 Z-Value = -1.21 P-Value = 0.114
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### Learn By Doing

The trustees of a local school district commission a survey to determine voter opinions about a possible bond measure to fund school upgrades. In a poll of 293 of the district’s 5,019 registered voters, 178 would support the bond measure. A hypothesis test was conducted using Minitab to determine if such a bond would pass with the required 55% of the vote.

```{figure} images/1_img6.gif
:alt: Minitab output: Test and CI for One Proportion Test of p=0.55 vs p &gt; 0.55 Sample: 1 X: 178 N: 293 Sample p: 0.607509 95% Upper Bound: 0.66342 Z-Value: 1.98 P-Value: 0.024

Minitab output: Test and CI for One Proportion Test of p=0.55 vs p &gt; 0.55 Sample: 1 X: 178 N: 293 Sample p: 0.607509 95% Upper Bound: 0.66342 Z-Value: 1.98 P-Value: 0.024
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### Learn By Doing

Do zinc supplements reduce a child's risk of catching a cold? A medical study reports a p-value of 0.03. Are the following interpretations of the p-value valid or invalid?

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
