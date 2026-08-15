# The ANOVA F-Test: A Worked Example

Before we give you hands-on practice in carrying out the ANOVA F-test, let's look at another example.

:::{admonition} Example: Reading Level of Magazine Ads
:class: tip

Do advertisers alter the reading level of their ads based on the target audience of the magazine they advertise in?

In 1981, a study of magazine advertisements was conducted (F.K. Shuptrine and D.D. McVicker, "Readability Levels of Magazine Ads," *Journal of Advertising Research*, 21:5, October 1981). Researchers selected random samples of advertisements from each of three groups of magazines:

- Group 1—highest educational level magazines (such as *Scientific American*, *Fortune*, *The New Yorker*)
- Group 2—middle educational level magazines (such as *Sports Illustrated*, *Newsweek*, *People*)
- Group 3—lowest educational level magazines (such as *National Enquirer*, *Grit*, *True Confessions*)

The measure that the researchers used to assess the level of the ads was the number of words in the ad. 18 ads were randomly selected from each of the magazine groups, and the number of words per ad was recorded. The sample means were $\bar{y}_1=140.0$, $\bar{y}_2=121.4$, and $\bar{y}_3=106.5$.

Our question of interest is whether the number of words in ads (Y) is related to the educational level of the magazine (X). To answer this question, we need to compare $\mu_1, \mu_2, \mu_3$, the mean number of words in ads of the three magazine groups. It seems that what the data suggest makes sense: the magazines in group 1 have the largest number of words per ad (on average), followed by group 2, and then group 3.

The question is whether these differences between the sample means are significant. In other words, are the differences among the observed sample means due to true differences among the $\mu's$, or merely due to sampling variability? To answer this question, we need to carry out the ANOVA F-test.

*Step 1: Stating the hypotheses.* We are testing:

$$H_0: \mu_1 = \mu_2 = \mu_3 \quad \text{vs.} \quad H_a: \text{not all the } \mu\text{'s are equal}$$

Conceptually, the null hypothesis claims that the number of words in ads is not related to the educational level of the magazine, and the alternative hypothesis claims that there is a relationship.

*Step 2: Checking conditions and summarizing the data.*

1. The ads were selected at random from each magazine group, so the three samples are independent.
2. Side-by-side boxplots of the data do not display any alarming violations of the normality assumption. There is some skewness in groups 2 and 3, but not extremely so, and there are no outliers in the data.
3. The sample standard deviations are 74.0 (group 1), 64.3 (group 2), and 57.6 (group 3). We can assume that the equal standard deviation condition is met, since the rule of thumb is satisfied: $74.0/57.6 < 2$.

Before we move on, let's look again at the data. It is easy to see the trend of the sample means. However, there is so much variation within each of the groups that there is almost complete overlap between the three boxplots, and the differences between the means are overshadowed and seem like something that could have happened just by chance. Let's move on and see whether the ANOVA F-test supports this observation.

Using statistical software to conduct the ANOVA F-test, we find that the F-statistic is 1.18, which is not very large. We also find that the p-value is 0.317.

*Step 3: Finding the p-value.* The p-value is 0.317, which tells us that getting data like those observed is not very surprising assuming that there are no differences between the three magazine groups with respect to the mean number of words in ads (which is what $H_0$ claims). In other words, the large p-value tells us that it is quite reasonable that the differences between the observed sample means could have happened just by chance (i.e., due to sampling variability) and not because of true differences between the means.

*Step 4: Making conclusions in context.* The large p-value indicates that the results are not significant, and that we cannot reject $H_0$. We therefore conclude that the study does not provide evidence that the mean number of words in ads is related to the educational level of the magazine. In other words, the study does not provide evidence that advertisers alter the reading level of their ads (as measured by the number of words) based on the educational level of the target audience of the magazine.
:::

## Check Your Understanding: Within-Group Variation and Significance

:::{quiz} In the magazine ads example, the three sample means (140.0, 121.4, 106.5) look quite different, yet the test was not significant. Which feature of the data explains this?
:hint: Look at the standard deviations (74.0, 64.3, 57.6) relative to the differences among the means.
:feedback-0: Correct! The within-group standard deviations (57-74 words) are large relative to the differences among the means (~33 words at most), so the boxplots overlap almost completely and F is small (1.18).
:feedback-1: The samples were the same size (18 each); the issue is the within-group variability.
:feedback-2: The conditions were checked and satisfied; the non-significance reflects weak evidence, not an invalid test.
* *The variation within each group is very large compared to the differences among the sample means
* The sample sizes were unequal
* The conditions for the test were violated
:::

:::{quiz} Suppose the same three sample means had come from samples with standard deviations of about 20 words each. How would the test likely change?
:hint: Shrinking the denominator of F...
:feedback-0: Correct! Smaller within-group variation would shrink F's denominator, making F much larger and the p-value smaller—likely a significant result.
:feedback-1: Reducing within-group spread makes differences among means MORE detectable, not less.
:feedback-2: The F-statistic depends on both variations, so it would definitely change.
* *F would be much larger and the result likely significant
* F would be smaller and the result less significant
* Nothing would change
:::
