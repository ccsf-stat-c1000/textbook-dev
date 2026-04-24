# ANOVA (4 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 2: Checking Conditions and Finding the Test Statistic

The test statistic of the ANOVA F-test, called the *F statistic*, has the form

```{figure} images/image164.gif
:alt: F = Variation Among Sample Means / Variation Within Groups

F = Variation Among Sample Means / Variation Within Groups
```

It has a different structure from all the test statistics we've looked at so far, but it is similar in that it is still a measure of the evidence against H~0~. The larger F is (which happens when the denominator, the variation within groups, is small relative to the numerator, the variation among the sample means), the more evidence we have against H~0~.

## Did I Get This?

Consider the following generic situation:

```{figure} images/image16.png
:alt: We have a situation in which k = 3. So, we have 3 populations, each with its own μ. For Population 1, we obtain a sample of size 100, and find that its Y-bar_1 = 35. For Population 2, we also get a sample of size 100. Y-bar_2 = 30. For the third sample of size 100 generated from the Population 3, we find that Y-bar_3 = 25. These are three independent samples.

We have a situation in which k = 3. So, we have 3 populations, each with its own μ. For Population 1, we obtain a sample of size 100, and find that its Y-bar_1 = 35. For Population 2, we also get a sample of size 100. Y-bar_2 = 30. For the third sample of size 100 generated from the Population 3, we find that Y-bar_3 = 25. These are three independent samples.
```

In this case, we are testing

- H~0~: μ~1~ = μ~2~ = μ~3~
- H~a~: Not all the μ's are equal

The following are two possible scenarios of the data (note in both scenarios the sample means are 25, 30, and 35).

```{figure} images/image154.gif
:alt: Scenario 1, illustrated by a dot plot. The dot plot is split with three horizontal axes, one for each sample. We see that for each population, the distribution is approximately normal and there is very little, if any, overlap between each distribution.

Scenario 1, illustrated by a dot plot. The dot plot is split with three horizontal axes, one for each sample. We see that for each population, the distribution is approximately normal and there is very little, if any, overlap between each distribution.
```

```{figure} images/image155.gif
:alt: Scenario 2, with a dot plot as in the previous image. However, each sample&apos;s distribution has a much wider spread. Samples 2 and 3 approximate a normal distribution, but sample 1 does not. In addition, the distributions have data points in common. They overlap quite a lot.

Scenario 2, with a dot plot as in the previous image. However, each sample&apos;s distribution has a much wider spread. Samples 2 and 3 approximate a normal distribution, but sample 1 does not. In addition, the distributions have data points in common. They overlap quite a lot.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Learn by Doing

Suppose that we would like to compare four populations (for example, four races/ethnicities or four age groups) with respect to a certain psychological test score. More specifically we would like to test

- H~0~: μ~1~ = μ~2~ = μ~3~ = μ~3~
- H~a~: Not all the μ's are equal

where μ~1~ is the mean test score in population 1, μ~2~ is the mean test score in population 2, μ~3~ is the mean test score in population 3, and μ~4~ is the mean test score in population 4.

We take a random sample from each population and use these four independent samples in order to carry out the test.

The following are two possible scenarios for the data:

Note that in both scenarios, the score averages of the four samples are very similar.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comments

1. The focus here is for you to understand the idea behind this test statistic, so we do not go into detail about how the two variations are measured. We instead rely on software output to obtain the F-statistic.
2. This test is called the ANOVA F-test. So far, we have explained the ANOVA part of the name. Based on the previous tests we introduced, it should not be surprising that the "F-test" part comes from the fact that the null distribution of the test statistic, under which the p-values are calculated, is called an F-distribution. We will say very little about the F-distribution in this course, which will essentially be limited to this comment and the next one.
3. It is fairly straightforward to decide if a z-statistic is large. Even without tables, we should realize by now that a z-statistic of 0.8 is not especially large, whereas a z-statistic of 2.5 is large. In the case of the t-statistic, it is less straightforward, because there is a different t-distribution for every sample size n (and degrees of freedom n − 1). However, the fact that a t-distribution with a large number of degrees of freedom is very close to the z (standard normal) distribution can help to assess the magnitude of the t-test statistic. When the size of the F-statistic must be assessed, the task is even more complicated, because there is a different F-distribution for every combination of the number of groups we are comparing and the total sample size. We will nevertheless say that for most situations, an F-statistic greater than 4 would be considered rather large, but tables or software are needed to get a truly accurate assessment.

```{admonition} Example
    RStatCrunchMinitabExcel 2007Excel 2003TI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. Here is the R output for the ANOVA F-test. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~. (We can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well).The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~. StatCrunch reports that the p-value is less than 0.0001, which supports the conclusion as well.The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~ (we can also see that the p-value is so small that Minitab reports that it is 0, which supports that conclusion as well).The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~ (we can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well).The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~ (we can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well).Here is the TI graphing calculator output for the ANOVA F-test. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~. (We can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well.)The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~ (we can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well).The parts of the output that we focus on here have been highlighted. In particular, note that the F-statistic is 46.60, which is very large, indicating that the data provide a lot of evidence against H~0~ (we can also see that the p-value is so small that it is essentially 0, which supports that conclusion as well).
```

Let's move on to talk about the conditions under which we can safely use the ANOVA F-test, where the first two conditions are very similar to ones we've seen before, but there is a new third condition. It is safe to use the ANOVA procedure when the following conditions hold:

1. The samples drawn from each of the populations we're comparing are independent.
2. The response variable varies normally within each of the populations we're comparing. As you already know, in practice this is done by looking at the histograms of the samples and making sure that there is no evidence of extreme departure from normality in the form of extreme skewness and outliers. Another possibility is to look at side-by-side boxplots of the data, and add histograms if a more detailed view is necessary. For large sample sizes, we don't really need to worry about normality, although it is always a good idea to look at the data.
3. The populations all have the same standard deviation. The best we can do to check this condition is to find the *sample* standard deviations of our samples and check whether they are "close." A common rule of thumb is to check whether the ratio between the largest sample standard deviation and the smallest is less than 2. If that's the case, this condition is considered to be satisfied.

```{admonition} Example
    In our example all the conditions are satisfied:

    1. All the samples were chosen randomly, and are therefore independent.
    2. The sample sizes are large enough (n = 35) that we really don't have to worry about the normality; however, let's look at the data using side-by-side boxplots, just to get a sense of it: You'll recognize this plot as Scenario 2 from earlier. The data suggest that the frustration level of the business students is generally lower than students from the other three majors. The ANOVA F-test will tell us whether these differences are significant.
    3. In order to use the rule of thumb, we need to get the sample standard deviations of our samples.

    RStatCrunchMinitabExcel 2007Excel 2003TI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. Let's use R to calculate the standard deviation for each of the four samples: We can either ask for the descriptive statistics for each of the four samples:or note that data summaries also appear in the ANOVA F-test output:We can either calculate the standard deviation for each of the four samples by hand, or note that the variance for each sample appears in the Excel output and use that to calculate the standard deviation (remember that the square root of variance is standard deviation). Here, the standard deviation has been calculated and added to the output: We can either calculate the standard deviation for each of the four samples by hand or note that the variance for each sample appears in the Excel output and use that to calculate the standard deviation (remember that the square root of variance is standard deviation). Here, the standard deviation has been calculated and added to the output: Let's use your TI graphing calculator to calculate the standard deviation (`STAT/CALC/1:1-Var Stats`) for each of the four samples: We can either calculate the standard deviation for each of the four samples by hand, or note that the variance for each sample appears in the Excel output and use that to calculate the standard deviation (remember that the square root of variance is standard deviation). Here, the standard deviation has been calculated and added to the output: We can either calculate the standard deviation for each of the four samples by hand, or note that the variance for each sample appears in the Excel output and use that to calculate the standard deviation (remember that the square root of variance is standard deviation). Here, the standard deviation has been calculated and added to the output:

    The rule of thumb is satisfied, since 3.082/2.088 < 2.
```

## Did I Get This?

In each of the following three questions, you'll find two designs for comparing number of credits taken by freshmen versus sophomores versus juniors versus seniors. In each case, one of the designs should not be handled with ANOVA. Your task is to identify which of the two it is.

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
