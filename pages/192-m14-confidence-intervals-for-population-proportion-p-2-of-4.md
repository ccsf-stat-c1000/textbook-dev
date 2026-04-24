# Confidence Intervals for Population Proportion p (2 of 4)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

```{admonition} Example
    The drug Viagra became available in the U.S. in May, 1998, in the wake of an advertising campaign that was unprecedented in scope and intensity. A Gallup poll found that by the end of the first week in May, 643 out of a random sample of 1,005 adults were aware that Viagra was an impotency medication (based on "Viagra A Popular Hit," a Gallup poll analysis by Lydia Saad, May 1998).

    Let's estimate the proportion p of all adults in the U.S. who by the end of the first week of May 1998 were already aware of Viagra and its purpose by setting up a 95% confidence interval for p.

    We first need to calculate the sample proportion $\hat{p}$. Out of 1,005 sampled adults, 643 knew what Viagra is used for, so $\hat{p}=\frac{643}{1005}=.64$

    ```{figure} images/image090.gif
    :alt: A large circle represents the population of all US Adults (18+). We are interested in the parameter is p, the proportion who know what Viagra is used for. From this population we create a sample of size n=1005, represented by a smaller circle. In this sample, we find that p hat (the point estimator) is .64 .

    A large circle represents the population of all US Adults (18+). We are interested in the parameter is p, the proportion who know what Viagra is used for. From this population we create a sample of size n=1005, represented by a smaller circle. In this sample, we find that p hat (the point estimator) is .64 .
    ```

    Therefore,

    A 95% confidence interval for p is $\hat{p}\pm2\sqrt{\frac{\hat{p}\left(1−\hat{p}\right)}{n}}=.64\pm2\sqrt{\frac{.64\left(1−.64\right)}{1005}}=.64\pm.03=\left(.61, .67\right)$

    We can be 95% sure that the proportion of all U.S. adults who were already familiar with Viagra by that time was between .61 and .67 (or 61% and 67%).

    The fact that the margin of error equals .03 says we can be 95% confident that unknown population proportion p is within .03 (3%) of the observed sample proportion .64 (64%). In other words, we are 95% confident that 64% is "off" by no more than 3%.

    ```{note}
        **Did I Get This?**

        *(Interactive activity — available in the OLI platform)*
    ```

    ```{note}
        **Did I Get This?**

        *(Interactive activity — available in the OLI platform)*
    ```

    ```{note}
        **Did I Get This?**

        *(Interactive activity — available in the OLI platform)*
    ```
```

## Comment

We would like to share with you the methodology part of the poll release of the Viagra example, and show you that you now have the tools to understand how polls results are analyzed:

"The results are based on telephone interviews with a randomly selected national sample of 1,005 adults, 18 years and older, conducted May 8-10, 1998. For results based on samples of this size, one can say with 95 percent confidence that the error attributable to sampling and other random effects could be plus or minus 3 percentage points. In addition to sampling error, question wording and practical difficulties in conducting surveys can introduce error or bias into the findings of public opinion polls."

The purpose of the next activity is to provide guided practice in calculating and interpreting the confidence interval for the population proportion p, and drawing conclusions from it.

##### Learn By Doing

A poll asked a random sample of 1,000 U.S. adults, "Do you think that the use of marijuana should be legalized?" 560 of those asked answered yes.

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

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Two important results that we discussed at length when we talked about the confidence interval for μ also apply here:

1. There is a trade-off between level of confidence and the width (or precision) of the confidence interval. The more precision you would like the confidence interval for p to have, the more you have to pay by having a lower level of confidence.

2. Since n appears in the denominator of the margin of error of the confidence interval for p, for a fixed level of confidence, the larger the sample, the narrower, or more precise it is. This brings us naturally to our next point.
