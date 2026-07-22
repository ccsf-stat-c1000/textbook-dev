# The Paired t-Test: Worked Examples

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
- Specify the null and alternative hypotheses for comparing groups.
```

The "driving after having 2 beers" example is a case in which observations are paired by subject. In other words, both samples have the same subjects, so that each subject is measured twice. Typically, as in our example, one of the measurements occurs before a treatment/intervention (2 beers in our case), and the other measurement after the treatment/intervention. Our next example is another typical type of study where the matched pairs design is used—a study involving twins.

:::{admonition} Example: IQ Scores of Twins Reared Apart
:class: tip

Researchers have long been interested in the extent to which intelligence, as measured by IQ score, is affected by "nurture" as opposed to "nature": that is, are people's IQ scores mainly a result of their upbringing and environment, or are they mainly an inherited trait? A study was designed to measure the effect of home environment on intelligence—more specifically, to address the question: "Are there significant differences in IQ scores between people who were raised by their birth parents and those who were raised by someone else?"

In order to answer this question, the researchers needed to get two groups of subjects (one from the population of people who were raised by their birth parents, and one from the population of people who were raised by someone else) who are as similar as possible in all other respects. In particular, since genetic differences may also affect intelligence, the researchers wanted to control for this confounding factor.

We know from our discussion on study design (in the Producing Data unit) that one way to (at least theoretically) control for all confounding factors is randomization—randomizing subjects to the different treatment groups. In this case, however, this is not possible. This is an observational study; you cannot randomize children to either be raised by their birth parents or to be raised by someone else. How else can we eliminate the genetics factor? We can conduct a "twin study."

Because identical twins are genetically the same, a good design for obtaining information to answer this question would be to compare IQ scores for identical twins, one of whom was raised by birth parents and the other by someone else. Such a design (matched pairs) is an excellent way of making a comparison between individuals who differ only with respect to the explanatory variable of interest (upbringing) but are as alike as they can possibly be in all other important aspects (inborn intelligence). Identical twins reared apart were studied by Susan Farber, who published her studies in the book *Identical Twins Reared Apart* (1981, Basic Books). In this problem, we use the IQ scores of 32 pairs of identical twins who were reared apart, as they appear in Farber's book.

Here are the important things to note about the design:

1. We are essentially comparing the mean IQ scores in two populations that are defined by our (two-valued categorical) explanatory variable—upbringing (X), whose two values are: raised by birth parents, raised by someone else.
2. This is a matched pairs design (as opposed to a two independent samples design), since each observation in one sample is linked (matched) with an observation in the second sample. The observations are paired by twins.

Each of the 32 rows in the data set represents one pair of twins. Keeping the notation that we used above, twin 1 is the twin who was raised by his/her birth parents, and twin 2 is the twin who was raised by someone else. Let's carry out the analysis.

*Step 1: Stating the hypotheses.* Recall that in matched pairs, we reduce the data from two samples to one sample of differences, and we state our hypotheses in terms of the mean of the differences, $\mu_d$. Since we would like to test whether there are differences in IQ scores between people who were raised by their birth parents and those who weren't, we are carrying out the two-sided test:

$$H_0: \mu_d = 0 \quad \text{vs.} \quad H_a: \mu_d \neq 0$$

(*Comment:* again, some students find it easier to first think about the hypotheses in terms of $\mu_1$ and $\mu_2$—here $H_0: \mu_1-\mu_2=0$ vs. $H_a: \mu_1-\mu_2\neq0$—and since $\mu_d=\mu_1-\mu_2$, we get back to the hypotheses above.)

*Step 2: Checking conditions and summarizing the data with a test statistic.* Is it safe to use the paired t-test in this case?

1. Clearly, the samples of twins are not random samples from the two populations. However, in this context, they can be considered as random, assuming that there is nothing special about the IQ of a person just because he/she has an identical twin.
2. The sample size here is n = 32. Even though by the n > 30 rule of thumb our sample can be considered large, it is a borderline case, so just to be on the safe side, we should look at the histogram of the differences to make sure we do not see anything extreme. (*Comment:* looking at the histogram of differences in every case is useful even if the sample is very large, just to get a sense of the data. Recall: "Always look at the data.") The data don't reveal anything that we should be worried about (like very extreme skewness or outliers), so we can safely proceed.

Looking at the histogram, we note that most of the differences are negative, indicating that in most of the 32 pairs of twins, twin 2 (raised by someone else) has a higher IQ. From this point we rely on statistical software, and find that the test statistic is t = −1.85: our data (represented by the average of the differences) are 1.85 standard errors below the null hypothesis (represented by the null value 0).

*Step 3: Finding the p-value.* The p-value is 0.074, indicating that there is a 7.4% chance of obtaining data like those observed (or even more extreme) assuming that $H_0$ is true (i.e., assuming that there are no differences in IQ scores between people who were raised by their birth parents and those who weren't).

*Step 4: Making conclusions.* Using the conventional significance level of 0.05, our p-value is not small enough, and we therefore cannot reject $H_0$. In other words, our data do not provide enough evidence to conclude that whether a person was raised by his/her birth parents has an impact on the person's intelligence (as measured by IQ scores).
:::

## Check Your Understanding: One-Sided Tests for Paired Data

:::{quiz} In the twins study, what would the one-sided p-value have been for the alternative Hₐ: μ_d < 0 (birth-parent twins have lower IQs)?
:hint: The two-sided p-value was 0.074, and the test statistic was negative (in the direction of this alternative).
:feedback-0: Correct! The one-sided p-value is half the two-sided one: 0.074/2 = 0.037.
:feedback-1: The one-sided p-value is HALF the two-sided value when the data lean in the alternative's direction.
:feedback-2: The p-value depends on the alternative—one-sided and two-sided tests give different values.
* *0.037
* 0.148
* 0.074
:::

```{admonition} Comment: Data Snooping
:class: important

This means that if, based on prior knowledge, prior research, or just a hunch, we had wanted to test the hypothesis that the IQ level of people raised by their birth parents is *lower*, on average, than the IQ level of people who were raised by someone else, we would have rejected $H_0$ and accepted that hypothesis (at the 0.05 significance level, since 0.037 < 0.05).

It should be stressed, though, that one should set the hypotheses *before* looking at the data. It would be ethically wrong to look at the histogram of differences, note that most of the differences are negative, and then decide to carry out the one-sided test that the data seem to support. This is known as "data snooping," and is considered to be a very bad statistical practice.
```

## Check Your Understanding: The Danger of Data Snooping

:::{quiz} A researcher collects paired data, looks at the results, notices the sample mean difference is positive, and only then chooses the alternative Hₐ: μ_d > 0 to get a smaller p-value. What is wrong with this?
:hint: When must hypotheses be set?
:feedback-0: Correct! Choosing the alternative after peeking at the data ("data snooping") makes the reported p-value misleadingly small—hypotheses must be set before examining the data.
:feedback-1: One-sided alternatives are legitimate when justified in advance; the problem is choosing one AFTER seeing the data.
:feedback-2: The calculation may be arithmetically right, but the inference is invalid because the hypothesis was chosen to fit the data.
* *The alternative was chosen after seeing the data, which invalidates the p-value—this is data snooping
* One-sided alternatives are never allowed
* Nothing—the calculation is correct, so the practice is fine
:::
