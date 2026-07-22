# Constructing a Confidence Interval for a Proportion

:::{admonition} Example: The Viagra Poll
:class: tip

The drug Viagra became available in the U.S. in May 1998, in the wake of an advertising campaign that was unprecedented in scope and intensity. A Gallup poll found that by the end of the first week in May, 643 out of a random sample of 1,005 adults were aware that Viagra was an impotency medication (based on "Viagra A Popular Hit," a Gallup poll analysis by Lydia Saad, May 1998).

Let's estimate the proportion p of all adults in the U.S. who by the end of the first week of May 1998 were already aware of Viagra and its purpose by setting up a 95% confidence interval for p.

We first need to calculate the sample proportion $\hat{p}$. Out of 1,005 sampled adults, 643 knew what Viagra is used for, so $\hat{p}=\frac{643}{1005}=0.64$.

Therefore, a 95% confidence interval for p is

$$\hat{p}\pm2\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}=0.64\pm2\sqrt{\frac{0.64(0.36)}{1005}}=0.64\pm0.03=(0.61,\ 0.67)$$

We can be 95% sure that the proportion of all U.S. adults who were already familiar with Viagra by that time was between 0.61 and 0.67 (or 61% and 67%).

The fact that the margin of error equals 0.03 says we can be 95% confident that the unknown population proportion p is within 0.03 (3%) of the observed sample proportion 0.64 (64%). In other words, we are 95% confident that 64% is "off" by no more than 3%.
:::

```{admonition} Comment
:class: important

We would like to share with you the methodology part of the poll release of the Viagra example, and show you that you now have the tools to understand how poll results are analyzed:

"The results are based on telephone interviews with a randomly selected national sample of 1,005 adults, 18 years and older, conducted May 8-10, 1998. For results based on samples of this size, one can say with 95 percent confidence that the error attributable to sampling and other random effects could be plus or minus 3 percentage points. In addition to sampling error, question wording and practical difficulties in conducting surveys can introduce error or bias into the findings of public opinion polls."
```

The purpose of the next activity is to provide guided practice in calculating and interpreting the confidence interval for the population proportion p, and drawing conclusions from it.

## Check Your Understanding: Constructing a Confidence Interval for a Proportion

A poll asked a random sample of 1,000 U.S. adults, "Do you think that the use of marijuana should be legalized?" 560 of those asked answered yes.

:::{quiz} What is a 95% confidence interval for p, the proportion of all U.S. adults who favor legalization?
:hint: p-hat = 0.56, and the standard error is √(0.56 × 0.44/1000) ≈ 0.0157.
:feedback-0: Correct! 0.56 ± 2(0.0157) ≈ 0.56 ± 0.03 = (0.53, 0.59).
:feedback-1: (0.55, 0.57) uses only about half the correct margin of error.
:feedback-2: The margin of error is about 0.03, not 0.10.
* *(0.53, 0.59)
* (0.55, 0.57)
* (0.46, 0.66)
:::

:::{quiz} Which is the correct interpretation of this interval?
:hint: The confidence is in the method capturing the fixed parameter p.
:feedback-0: Correct! We are 95% confident that the interval (0.53, 0.59) covers the true proportion of all U.S. adults who favor legalization.
:feedback-1: The interval concerns the population proportion, not the variability of individuals' opinions.
:feedback-2: 95% of SAMPLES would produce intervals covering p—but not "95% of adults are in the interval," which confuses people with proportions.
* *We are 95% confident that the proportion of all U.S. adults who favor legalization is between 0.53 and 0.59
* 95% of U.S. adults have opinions between 0.53 and 0.59
* 95% of the people in the sample favor legalization
:::

:::{quiz} Based on this interval, can we conclude that a majority of U.S. adults favor legalization?
:hint: Is every plausible value in the interval above 0.5?
:feedback-0: Correct! The entire interval (0.53, 0.59) lies above 0.5, so all plausible values of p represent a majority.
:feedback-1: 0.5 is NOT inside the interval—the interval starts at 0.53.
* *Yes—the entire interval lies above 0.50
* No—0.50 is a plausible value for p
:::

Two important results that we discussed at length when we talked about the confidence interval for μ also apply here:

1. There is a trade-off between level of confidence and the width (or precision) of the confidence interval. The more precision you would like the confidence interval for p to have, the more you have to pay by having a lower level of confidence.

2. Since n appears in the denominator of the margin of error of the confidence interval for p, for a fixed level of confidence, the larger the sample, the narrower, or more precise, the interval is. This brings us naturally to our next point.
