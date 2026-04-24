# Two Independent Samples (6 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Confidence Interval for   (Two-Sample t Confidence Interval)

So far we've discussed the two-sample t-test, which checks whether there is enough evidence stored in the data to reject the claim that $\mu_{1}−\mu_{2}=0$ (or equivalently, that $\mu_{1}=\mu_{2}$ ) in favor of one of the three possible alternatives.

If we would like to estimate $\mu_{1}−\mu_{2}$ we can use the natural point estimate, $\bar{y_{1}}− \bar{y_{2}}$ , or preferably, a 95% confidence interval which will provide us with a set of plausible values for the difference between the population means $\mu_{1}−\mu_{2}$ .

In particular, if the test has rejected $H_{o}:\mu_{1}−\mu_{2}=0$ , a confidence interval for $\mu_{1}−\mu_{2}$ can be insightful since it quantifies the effect that the categorical explanatory variable has on the response.

## Comment

We will not go into the formula and calculation of the confidence interval, but rather ask our software to do it for us, and focus on interpretation.

```{admonition} Example
    Recall our leading example about the looks vs. personality score of females and males:

    ```{figure} images/image047.gif
    :alt: The Gender(X) Variable has two categories, which gives us Population 1: Females and Population 2: Males. Each population has its own Y-Mean μ, so population 1&apos;s mean is μ_1 and population 2&apos;s mean is μ_2. For each population we take an SRS. For Population 1, an SRS of size 150 is taken, and for population 2 an SRS of size 85 is taken.

    The Gender(X) Variable has two categories, which gives us Population 1: Females and Population 2: Males. Each population has its own Y-Mean μ, so population 1&apos;s mean is μ_1 and population 2&apos;s mean is μ_2. For each population we take an SRS. For Population 1, an SRS of size 150 is taken, and for population 2 an SRS of size 85 is taken.
    ```

    StatCrunchRMinitabExcel 2007TI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. Here again is the output:Here again is the output:Here again is the output:In this case, Excel tells us that the 95% confidence interval is (-3.69590, -1.49625).Here is the output for STAT/TESTS/0:2-SampTInt:In this case, Excel tells us that the 95% confidence interval is (-3.69590, -1.49625).In this case, Excel tells us that the 95% confidence interval is (-3.69590, -1.49625).

    Recall that we rejected the null hypothesis in favor of the two-sided alternative and concluded that the mean score of females is different from the mean score of males. It would be interesting to supplement this conclusion with more details about this difference between the means, and the 95% confidence interval for $\mu_{1}−\mu_{2}$ does exactly that.

    According to the output the 95% confidence interval for $\mu_{1}−\mu_{2}$ is roughly (-3.7, -1.5). First, note that the confidence interval is strictly negative suggesting that μ~1~ is lower than μ~2~ . Furthermore, the confidence interval tells me that we are 95% confident that the mean "looks vs. personality score" of females ( μ~1~ ) is between 1.5 and 3.7 points lower than the mean looks vs. personality score of males ( μ~2~ ). The confidence interval therefore quantifies the effect that the explanatory variable (gender) has on the response (looks vs personality score).
```

```{note}
    **Learn By Doing**

    Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```
