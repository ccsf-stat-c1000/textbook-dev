# ANOVA (5 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Step 3: Finding the p-value

The p-value of the ANOVA F-test is the probability of getting an Fstatistic as large as we got (or even larger), had $H_{0}:\mu_{1}=\mu_{2}=...=\mu_{k}$ been true. In other words, it tells us how surprising it is to find data like those observed, assuming that there is no difference among the population means μ~1~, μ~2~, ..., μ~k~.

```{admonition} Example
    RStatCrunchMinitabExcel 2007Excel 2003TI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is very small ( less than 0.0001 ) telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims). As we already noticed before, the p-value in our example is so small that Minitab reports it to be 0.000, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).As we already noticed before, the p-value in our example is so small that it is essentially 0, telling us that it would be next to impossible to get data like those observed had the mean frustration level of the four majors been the same (as the null hypothesis claims).
```

## Step 4: MakingConclusions in Context

As usual, we base our conclusion on the p-value. A small p-value tells us that our data contain a lot of evidence against H~o~. More specifically, a small p-value tells us that the differences between the sample means are statistically significant (unlikely to have happened by chance), and therefore we reject H~o~. If the p-value is not small, the data do not provide enough evidence to reject H~o~, and so we continue to believe that it may be true. A significance level (cut-off probability) of .05 can help determine what is considered a small p-value.

```{admonition} Example
    In our example, the p-value is extremely small—close to 0—indicating that our data provide extremely strong evidence to reject H~o~. We conclude that the frustration level means of the four majors are not all the same, or in other words, that majors do have an effect on students' academic frustration levels at the school where the test was conducted.
```
