# Matched Pairs (5 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 3: Finding the p-value

As a special case of the one-sample t-test, the null distribution of the paired t-test statistic is a t distribution (with n - 1 degrees of freedom), which is the distribution under which the p-values are calculated. We will let the software find the p-value for us, and in this case, Excel gives us a p-value of 0.009.

The small p-value tells us that there is very little chance of getting data like those observed (or even more extreme) if the null hypothesis were true. More specifically, there is less than a 1% chance (.009=.9%) of obtaining a test statistic of -2.58 (or lower), assuming that 2 beers have no impact on reaction times.

## Step 4: Conclusion in Context.

As usual, we draw our conclusion based on the p-value. If the p-value is small, there is a significant difference between what was observed in the sample and what was claimed in H~o~, so we reject H~o~ and conclude that the categorical explanatory variable does affect the quantitative response variable as specified in H~a~. If the p-value is not small, we do not have enough statistical evidence to reject H~o~. In particular, if a cutoff probability, α (significance level), is specified, we reject H~o~ if the p-value is less than α. Otherwise, we do not reject H~o~.

In our example, the p-value is .009, indicating that the data provide enough evidence to reject H~o~ and conclude that drinking two beers does slow the reaction times of drivers, and thus that drivers are impaired after drinking two beers.

## Comment

It is very important to pay attention to whether the two-sample t-test or the paired t-test is appropriate. In other words, being aware of the study design is extremely important. Consider our example. If we had not "caught" that this is a matched pairs design, and had analyzed the data as if the two samples were independent using the two-sample t-test, we would have obtained a p-value of 0.057.

Note that using this (wrong) method to analyze the data, and a significance level of .05, we would conclude that the data do not provide enough evidence for us to conclude that drivers are impaired after drinking two beers. This is an example of how using the wrong statistical method can lead you to wrong conclusions, which in this context can have very serious implications.
