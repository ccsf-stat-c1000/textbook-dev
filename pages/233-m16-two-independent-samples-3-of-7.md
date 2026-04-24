# Two Independent Samples (3 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 2: Check Conditions, and Summarize the Data Using a Test Statistic

The two-sample t-test can be safely used as long as the following conditions are met:

1. The two samples are indeed independent.
2. We are in one of the following two scenarios:
  1. Both populations are normal, or more specifically, the distribution of the response Y in both populations is normal, and both samples are random (or at least can be considered as such). In practice, checking normality in the populations is done by looking at each of the samples using a histogram and checking whether there are any signs that the populations are not normal. Such signs could be extreme skewness and/or extreme outliers.
  2. The populations are known or discovered not to be normal, but the sample size of each of the random samples is large enough (we can use the rule of thumb that > 30 is considered large enough).

Assuming that we can safely use the two-sample t-test, we need to summarize the data, and in particular, calculate our data summary—the test statistic.

*The two-sample t-test statistic* is:

$t=\frac{\left(\bar{y_{1}}−\bar{y_{2}}\right)−0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}$

Where:

$\bar{y_{1}}, \bar{y_{2}}$ are the sample means of the samples from population 1 and population 2 respectively.

$s_{1}, s_{2}$ are the sample standard deviations of the samples from population 1 and population 2 respectively.

$n_{1}, n_{2}$ are the sample sizes of the two samples.

## Comment

Let's see why this test statistic makes sense, bearing in mind that our inference is about $\mu_{1}−\mu_{2}$.

- $\bar{y_{1}}$ estimates μ~1~ and $\bar{y_{2}}$ estimates μ~2~, and therefore $\bar{y_{1}}− \bar{y_{2}}$ is what the data tell me about (or, how the data estimate) $\mu_{1}−\mu_{2}$.
- 0 is the "null value" — what the null hypothesis, H~o~, claims that $\mu_{1}−\mu_{2}$ is.
- The denominator $\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}$ is the standard error of $\bar{y_{1}}− \bar{y_{2}}$. (We will not go into the details of why this is true.)

We therefore see that our test statistic, like the previous test statistics we encountered, has the structure:

$\frac{sample estimate−null value}{standard error}$

and therefore, like the previous test statistics, measures (in standard errors) the difference between what the data tell us about the parameter of interest $\mu_{1}−\mu_{2}$ (sample estimate) and what the null hypothesis claims the value of the parameter is (null value).

```{note}
    **Many Students Wonder**

    How to Read Statistical Software Output

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example
    Let's first check whether the conditions that allow us to safely use the two-sample t-test are met.

    1. Here, 239 students were chosen and were naturally divided into a sample of females and a sample of males. Since the students were chosen at random, the sample of females is independent of the sample of males.
    2. Here we are in the second scenario — the sample sizes (150 and 85), are definitely large enough, and so we can proceed regardless of whether the populations are normal or not.

    RStatCrunchMinitabExcel 2013 and 2016 InstructionsExcel 2003TI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. In order to avoid tedious calculations, we use R to find the test statistic. In this case, R gives us a value of -4.66:Just for this first example, let's make sure that we understand what the ingredients are that go into the test statistic calculation and how we use them to find the test statistic. We already know the sample sizes (150 and 85), the means are given in the R output above, and the sample standard deviations can be found using this command:`tapply(looks$Score,factor(looks$Gender),sd, na.rm=TRUE)`In order to avoid tedious calculations, we will lift the test statistic from the output. The StatCrunch output (edited) is shown below:As you can see we highlighted the “ingredients” needed to calculate the test statistic, as well as the test statistic itself. Just for this first example, let’s make sure that we understand what these ingredients are and how to use them to find the test statistic. In order to avoid tedious calculations, we will lift the test statistic from the output:As you can see, we highlighted the "ingredients" needed to calculate the test statistic, as well as the test statistic itself. Just for this first example, let's make sure that we understand what these ingredients are and how we use them to find the test statistic.In order to avoid tedious calculations, we use Excel to find the test statistic. In this case, Excel gives us a t-value of -4.66.Just for this first example, let's make sure that we understand what the ingredients are that go into the test statistic calculation and how we use them to find the test statistic.In order to avoid tedious calculations, we use Excel to find the test statistic. In this case, Excel gives us a t-value of -4.66.Just for this first example, let's make sure that we understand what the ingredients are that go into the test statistic calculation and how we use them to find the test statistic.In order to avoid tedious calculations, we use the TI graphing calculator to find the test statistic. In this case, we get a value of -4.66:Just for this first example, let's make sure that we understand what these ingredients are that go into the test statistic calculation and how we use them to find the test statistic. In order to avoid tedious calculations, we use Excel to find the test statistic. In this case, Excel gives us a t-value of -4.66.Just for this first example, let's make sure that we understand what the ingredients are that go into the test statistic calculation and how we use them to find the test statistic.In order to avoid tedious calculations, we use Excel to find the test statistic. In this case, Excel gives us a t-value of -4.66.Just for this first example, let's make sure that we understand what the ingredients are that go into the test statistic calculation and how we use them to find the test statistic.

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```

    And when we put it all together we get that indeed,

    $t=\frac{\left(\bar{y_{1}}−\bar{y_{2}}\right)−0}{\sqrt{\frac{s_{1}^{2}}{n_{1}}+\frac{s_{2}^{2}}{n_{2}}}}=\frac{10.73−13.33}{\sqrt{\frac{4.25^{2}}{150}+\frac{4.02^{2}}{85}}}=−4.66$

    The test statistic tells us what the data tell us about $\mu_{1}−\mu_{2}$. In this case that difference (10.73 - 13.33) is 4.66 standard errors below what the null hypothesis claims this difference to be (0). 4.66 standard errors is quite a lot and probably indicates that the data provide evidence against H~o~.
```

```{note}
    **Learn By Doing**

    Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```

We have completed step 2 and are ready to proceed to step 3, finding the p-value of the test.
