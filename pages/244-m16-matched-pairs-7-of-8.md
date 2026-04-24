# Matched Pairs (7 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing groups.
```

## Confidence Interval for μd(Paired
                t
                Confidence
                Interval)

So far we've discussed the paired t-test, which checks whether there is enough evidence stored in the data to reject the claim that $\mu_{d}=0$ in favor of one of the three possible alternatives.

If we would like to estimate $\mu_{d}$, the mean of the differences (response 1 - response 2), we can use the natural point estimate, $\bar{x_{d}}$, the sample mean of the differences, or preferably, use a 95% confidence interval, which will provide us with a set of plausible values for $\mu_{d}$.

In particular, if the test has rejected $H_{0}:\mu_{d}=0$, a confidence interval for $\mu_{d}$ can be insightful, since it quantifies the effect that the categorical explanatory variable has on the response variable.

*Comment:*We will not go into the formula and calculation of the confidence interval, but rather ask our statistical software to do it for us, and focus on interpretation.

```{admonition} Example
    Recall our leading example about whether drivers are impaired after having two beers:

    ```{figure} images/image054.gif
    :alt: The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.

    The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.
    ```

    which is reduced to inference about a single mean, the mean of the differences (before - after):

    ```{figure} images/image067.gif
    :alt: For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.

    For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.
    ```

    The p-value of our test, $H_{0}:\mu_{d}=0$ vs. $H_{0}:\mu_{d}<0$ was .009, and we therefore rejected H~o~ and concluded that the mean difference in total reaction time (before beer - after beer) was negative, or in other words, that drivers are impaired after having two beers. As a follow-up to this conclusion, it would be interesting to quantify the effect that two beers have on the driver, using the 95% confidence interval for $\mu_{d}$.

    Using statistical software, we find that the 95% confidence interval for	$\mu_{d}$, the mean of the differences (before - after), is roughly (-.9, -.1).

    We can therefore say with 95% confidence that drinking two beers increases the total reaction time of the driver by between .1 and .9 of a second.
```

## Comment

As we've seen in previous tests, as well as in the matched pairs case, the 95% confidence interval for $\mu_{d}$ can be used for testing in the two-sided case ($H_{0}:\mu_{d}=0$ vs. $H_{a}:\mu_{d}\neq0$):

If the null value, 0, falls outside the confidence interval, H~o~ is rejected.

If the null value, 0, falls inside the confidence interval, H~o~ is not rejected.

```{admonition} Example
    Let's go back to our twin study example, where we found a 95% confidence interval for	$\mu_{d}$ of (-6.11322, 0.30072) and a p-value of 0.074.

    We used the fact that the p-value is .074 to conclude that H~o~ can not be rejected (at the .05 significance level), and that whether or not a person was raised by his or her birth parents doesn't necessarily have an effect on intelligence (as measured by IQ scores). The last comment tells us that we can also use the confidence interval to reach the same conclusion, since 0 falls inside the confidence interval for $\mu_{d}$. In other words, since 0 is a plausible value for $\mu_{d}$ we cannot reject H~o~ which claims that $\mu_{d}=0$.
```

## Learn By Doing

A publishing company wanted to test whether typing speed differs when using word processor A or word processor B. A random sample of 25 typists was selected and the typing speeds (in words per minute) were recorded for each secretary when using word processor A and then when using word processor B. (Which word processor was used first was determined for each typist by a coin flip).

Based on the collected data, a 95% confidence interval for μ~d~, the mean difference (word processor A - word processor B) was found to be (2.5, 7.8).

The appropriate hypotheses for testing whether the typing speeds differ when using word processor A or word processor B is the two-sided test:

```{figure} images/image417.gif
:alt: H_0: μ_d = 0, H_a: μ_d ≠ 0

H_0: μ_d = 0, H_a: μ_d ≠ 0
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
