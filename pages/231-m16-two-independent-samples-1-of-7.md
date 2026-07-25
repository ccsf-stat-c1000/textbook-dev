# Comparing Two Means from Independent Samples

## Comparing Two Means—Two Independent Samples (The Two-Sample t-Test)

### Overview

As we mentioned in the summary of the introduction to case $C \to Q$, the first case that we will deal with is comparing two means when the two samples are independent:

```{figure} images/gen/m16-independent-samples.svg
:alt: Sub-population 1 has mean of Y mu 1, and sub-population 2 has mean of Y mu 2. Independent simple random samples of sizes n 1 and n 2 are taken from the two sub-populations.
```

Recall that here we are interested in the effect of a two-valued (k = 2) categorical variable (X) on a quantitative response (Y). Samples are drawn independently from the two sub-populations (defined by the two categories of X), and we need to evaluate whether or not the data provide enough evidence for us to believe that the two sub-population means are different.

In other words, our goal is to test whether the means $\mu_1$ and $\mu_2$ (which are the means of the variable of interest in the two sub-populations) are equal or not, and in order to do that we have two samples, one from each sub-population, which were chosen independently of each other. As the title of this part suggests, the test that we will learn here is commonly known as the *two-sample t-test*. As the name suggests, this is a t-test, which as we know means that the p-values for this test are calculated under some t distribution. Here is how this part is organized: we first introduce our leading example, and then go in detail through the four steps of the two-sample t-test, illustrating each step using our example.

```{admonition} A Note on Terminology
:class: note

Up until now, we have been dividing our population into *sub-populations*, then sampling from these sub-populations. From now on, instead of calling them sub-populations, we will usually call the groups we wish to compare *population 1, population 2,* and so on. These two descriptions of the groups we are comparing can be used interchangeably.
```

:::{admonition} Example: Looks vs. Personality
:class: tip

What is more important to you—personality or looks?

This question was asked of a random sample of 239 college students, who were to answer on a scale of 1 to 25. An answer of 1 means personality has maximum importance and looks no importance at all, whereas an answer of 25 means looks have maximum importance and personality no importance at all. The purpose of this survey was to examine whether males and females differ with respect to the importance of looks vs. personality.

Note that the data have the following format:

| Score (Y) | Gender (X) |
| --- | --- |
| 15 | Male |
| 13 | Female |
| 10 | Female |
| 12 | Male |
| 14 | Female |
| 14 | Male |
| 6 | Male |
| 17 | Male |
| ... | ... |

The format of the data reminds us that we are essentially examining the relationship between the two-valued categorical variable, gender, and the quantitative response, score. The two values of the categorical explanatory variable define the two populations that we are comparing—males and females. The comparison is with respect to the response variable score. Here is a figure that summarizes the example:

```{figure} images/gen/m16-looks-design.svg
:alt: Two populations, females and males, defined by the gender variable X. Each has a mean score: mu 1 for females and mu 2 for males. Independent simple random samples were taken: 150 females and 85 males.
```

*Comments:*

1. Note that this figure emphasizes how the fact that our explanatory variable is a two-valued categorical variable means that in practice we are comparing two populations (defined by these two values) with respect to our response Y.

2. Note that even though the problem description just says that we had 239 students, the figure tells us that there were 85 males in the sample and 150 females.

3. Following up on comment 2, note that $85 + 150 = 235$, and not 239. In these data (which are real) there are four *missing observations*—4 students for whom we do not have the value of the response variable. This could be due to a number of reasons, such as recording error or nonresponse. The bottom line is that even though data were collected from 239 students, effectively we have data from only 235.
:::

```{admonition} Many Students Wonder: Why Not Two Separate Tests?
:class: important

Why can't we just carry out a separate test for each of the two means and compare the results? Because the question we are asking is about the *difference* between the groups, the inference must be based on a single procedure that directly compares the two means (through their difference, $\mu_1 - \mu_2)$, properly accounting for the variability in both samples at once. Running two separate one-sample tests does not assess how likely the observed *gap* between the groups would be by chance.
```

We will now introduce the two-sample t-test by going through its four steps.
