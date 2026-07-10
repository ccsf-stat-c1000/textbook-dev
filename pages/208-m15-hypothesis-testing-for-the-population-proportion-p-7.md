# Hypothesis Testing for the Population Proportion p (7 of 13)

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

Let's find the p-value in each of our three leading examples.

:::{admonition} Example 1: Defective Products
:class: tip

Recall: $H_0: p = 0.20$, $H_a: p < 0.20$, $\hat{p} = 0.16$, and z = −2.

The p-value in this case is:

- The probability of observing a test statistic as small as −2 or smaller, assuming that $H_0$ is true.

*OR (recalling what the test statistic actually means in this case),*

- The probability of observing a sample proportion that is 2 standard deviations or more below $p_0=0.20$, assuming that $p_0$ is the true population proportion.

*OR, more specifically,*

- The probability of observing a sample proportion of 0.16 or lower in a random sample of size 400, when the true population proportion is $p_0=0.20$.

In either case, the p-value is the area under the standard normal curve to the left of −2: $P(Z\leq-2)$.

To find $P(Z\leq-2)$ we can either use a table or software. Eventually, after we understand the details, we will use software to run the test for us and the output will give us all the information we need. The p-value for this specific example is 0.023. The p-value tells us that it is pretty unlikely (probability of 0.023) to get data like those observed (test statistic of −2 or less) assuming that $H_0$ is true.
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

Recall: $H_0: p = 0.157$, $H_a: p > 0.157$, $\hat{p} = 0.19$, and z = 0.91.

The p-value in this case is:

- The probability of observing a test statistic as large as 0.91 or larger, assuming that $H_0$ is true.

*OR (recalling what the test statistic actually means in this case),*

- The probability of observing a sample proportion that is 0.91 standard deviations or more above $p_0=0.157$, assuming that $p_0$ is the true population proportion.

*OR, more specifically,*

- The probability of observing a sample proportion of 0.19 or higher in a random sample of size 100, when the true population proportion is $p_0=0.157$.

In either case, the p-value is the area under the standard normal curve to the right of 0.91: $P(Z\geq0.91)$.

Again, at this point we can either use a table or software to find that the p-value is 0.182. The p-value tells us that it is not very surprising (probability of 0.182) to get data like those observed (which yield a test statistic of 0.91 or higher) assuming that the null hypothesis is true.
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

Recall: $H_0: p = 0.64$, $H_a: p \neq 0.64$, $\hat{p} = 0.675$, and z = 2.31.

The p-value in this case is:

- The probability of observing a test statistic as large as 2.31 (or larger) or as small as −2.31 (or smaller), assuming that $H_0$ is true.

*OR (recalling what the test statistic actually means in this case),*

- The probability of observing a sample proportion that is 2.31 standard deviations or more away from $p_0=0.64$, assuming that $p_0$ is the true population proportion.

*OR, more specifically,*

- The probability of observing a sample proportion as different as 0.675 is from 0.64, or even more different (i.e., as high as 0.675 or higher, or as low as 0.605 or lower) in a random sample of size 1,000, when the true population proportion is $p_0=0.64$.

In either case, the p-value is the sum of the areas in both tails: $P(Z\leq-2.31)+P(Z\geq2.31)=2P(Z\geq2.31)$.

Again, at this point we can either use a table or software to find that the p-value is 0.021. The p-value tells us that it is pretty unlikely (probability of 0.021) to get data like those observed (test statistic as high as 2.31 or higher, or as low as −2.31 or lower) assuming that $H_0$ is true.
:::

```{admonition} Comment
:class: important

We've just seen that finding p-values involves probability calculations about the value of the test statistic assuming that $H_0$ is true. In this case, when $H_0$ is true, the values of the test statistic follow a standard normal distribution (i.e., the sampling distribution of the test statistic when the null hypothesis is true is N(0,1)). Therefore, p-values correspond to areas (probabilities) under the standard normal curve.

Similarly, in *any test*, p-values are found using the sampling distribution of the test statistic when the null hypothesis is true (also known as the "null distribution" of the test statistic). In this case, it was relatively easy to argue that the null distribution of our test statistic is N(0,1). As we'll see, in other tests, other distributions come up (like the t-distribution and the F-distribution), which we will just mention briefly, and rely heavily on the output of our statistical package for obtaining the p-values.
```

We've just completed our discussion about the p-value, and how it is calculated both in general and more specifically for the z-test for the population proportion. Let's go back to the four-step process of hypothesis testing and see what we've covered and what still needs to be discussed.

```{admonition} The Four Steps in Hypothesis Testing
:class: note

1. State the appropriate null and alternative hypotheses, $H_0$ and $H_a$.
2. Obtain a random sample, collect relevant data, and *check whether the data meet the conditions under which the test can be used*. If the conditions are met, summarize the data using a test statistic.
3. Find the p-value of the test.
4. Based on the p-value, decide whether or not the results are significant, and *draw your conclusions in context*.
```

With respect to the z-test for the population proportion: steps 1, 2, and 3 are completed; step 4 is what we will work on next.

## Learn By Doing

In 2007, a Gallup poll estimated that 45% of U.S. adults rated their financial situation as "good." We want to know if the proportion is smaller this year. We gather a random sample of 100 U.S. adults this year and find that 39 rate their financial situation as "good." Statistical software gives the following output:

| Test of p = 0.45 vs p < 0.45 | | | | |
| --- | --- | --- | --- | --- |
| **X** | **N** | **Sample p** | **Z-Value** | **P-Value** |
| 39 | 100 | 0.39 | −1.21 | 0.114 |

:::{quiz} According to the output, what is the value of the test statistic, and what does it mean?
:hint: Find the Z-Value in the output.
:feedback-0: Correct! z = −1.21: the sample proportion 0.39 is 1.21 standard deviations below the null value 0.45.
:feedback-1: 0.114 is the p-value, not the test statistic.
:feedback-2: 0.39 is the sample proportion; the test statistic is its standardized (z) score.
* *z = −1.21—the sample proportion is 1.21 standard deviations below 0.45
* z = 0.114—the sample proportion is 0.114 standard deviations below 0.45
* z = 0.39—the sample proportion is 0.39 standard deviations below 0.45
:::

:::{quiz} Which statement correctly interprets the p-value of 0.114?
:hint: The alternative is p < 0.45, so "extreme" means small.
:feedback-0: Correct! If the true proportion were still 0.45, there would be a 0.114 probability of getting a sample proportion of 0.39 or lower in a sample of 100.
:feedback-1: The p-value is not the probability that H₀ is true.
:feedback-2: This describes a two-tailed calculation; the alternative here is one-sided (less than).
* *If p were 0.45, the probability of a sample proportion of 0.39 or lower would be 0.114
* There is a 0.114 probability that the proportion is still 0.45
* If p were 0.45, the probability of a sample proportion at least 0.06 away from 0.45 in either direction would be 0.114
:::

:::{quiz} Using α = 0.05, what is the correct conclusion?
:hint: Compare 0.114 with 0.05.
:feedback-0: Correct! Since 0.114 > 0.05, the data do not provide enough evidence to conclude that the proportion has decreased.
:feedback-1: 0.114 is LARGER than 0.05, so we cannot reject H₀.
:feedback-2: Failing to reject H₀ does not prove the proportion is still 0.45.
* *Do not reject H₀—there is not enough evidence that the proportion rating their situation "good" has decreased
* Reject H₀ and conclude the proportion has decreased
* Accept H₀ and conclude the proportion is still 0.45
:::

## Learn By Doing

The trustees of a local school district commission a survey to determine voter opinions about a possible bond measure to fund school upgrades. In a poll of 293 of the district's 5,019 registered voters, 178 would support the bond measure. A hypothesis test was conducted to determine if such a bond would pass with the required 55% of the vote. Statistical software gives the following output:

| Test of p = 0.55 vs p > 0.55 | | | | |
| --- | --- | --- | --- | --- |
| **X** | **N** | **Sample p** | **Z-Value** | **P-Value** |
| 178 | 293 | 0.6075 | 1.98 | 0.024 |

:::{quiz} Using α = 0.05, what should the trustees conclude?
:hint: The p-value is 0.024. What does rejecting H₀ mean in context?
:feedback-0: Correct! Since 0.024 < 0.05, the data provide significant evidence that more than 55% of registered voters support the measure—suggesting the bond would pass.
:feedback-1: 0.024 is smaller than 0.05, so the result IS statistically significant.
:feedback-2: The conclusion needs context: rejecting H₀ here means support exceeds the required 55%.
* *Reject H₀—there is significant evidence that support exceeds 55%, so the bond is likely to pass
* Do not reject H₀—the evidence is not strong enough
* Reject H₀ (nothing further can be said)
:::

## Learn By Doing

Do zinc supplements reduce a child's risk of catching a cold? A medical study reports a p-value of 0.03.

:::{quiz-multi} Which of the following are valid interpretations of the p-value of 0.03? (Select all that apply.)
:hint: The p-value is a probability about the DATA computed assuming the null hypothesis (zinc has no effect) is true.
:feedback-0: Valid! This is exactly what the p-value measures—the chance of results like these if zinc had no effect.
:feedback-1: Valid! Since 0.03 < 0.05, the results are statistically significant at the 0.05 level.
:feedback-2: Invalid—the p-value is not the probability that the null hypothesis is true.
:feedback-3: Invalid—the p-value says nothing about the size of the effect, only the strength of evidence that some effect exists.
* *If zinc had no effect, results like those observed would occur with probability 0.03
* *The results are statistically significant at the 0.05 level
* There is a 3% chance that zinc has no effect on colds
* Zinc reduces the risk of colds by 3%
:::
