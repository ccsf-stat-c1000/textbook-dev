# Hypothesis Testing for the Population Mean (5 of 9)

```{admonition} Learning Objectives
    - Apply the concepts of: sample size, statistical significance vs. practical importance, and the relationship between hypothesis testing and confidence intervals.
```

## Relating Hypothesis Tests and Confidence Intervals

Just as we did for proportions, we may examine a confidence interval to decide whether a proposed value of the population mean is plausible.

Suppose we want to test $H_{0}:\mu=\mu_{0}$ vs. $H_{a}:\mu\neq\mu_{0}$ using a significance level of $\alpha=.05$. An alternative way to perform this test is to find a 95% confidence interval for μ and make the following conclusions:

If $\mu_{0}$ falls outside the confidence interval, reject H~o~.

If $\mu_{0}$ falls inside the confidence interval, do not reject H~o~.

```{admonition} Example
    We'll use example 2, in which the alternative was two-sided.

    Recall that we want to check whether a medication conforms to a target concentration of a chemical ingredient by testing

    $H_{0}:\mu=250$

    $H_{a}:\mu\neq250$

    We assume that $\sigma=12$, and in a sample of size n = 100 we obtained a sample mean of $\bar{x}=247$.

    A 95% confidence interval for μ is $\bar{x}\pm2\frac{\sigma}{\sqrt{n}}=247\pm2\frac{12}{\sqrt{100}}=247\pm2.4=\left(244.6, 249.4\right)$.

    Since the interval does not contain 250, we reject H~o~ and conclude that the alternative is true: the population mean concentration differs from 250.

    ```{figure} images/image354.gif
    :alt: A number line showing the 95% confidence interval, which is (244.6, 249.4). 250 is also marked on the number line, and it isn&apos;t within the interval, so we can be confident that μ isn&apos;t 250. In other words, we can reject the hypothesis H_0:μ = 250

    A number line showing the 95% confidence interval, which is (244.6, 249.4). 250 is also marked on the number line, and it isn&apos;t within the interval, so we can be confident that μ isn&apos;t 250. In other words, we can reject the hypothesis H_0:μ = 250
    ```
```

## Did I Get This?

One of the following is an actual Minitab output; the others were edited to be incorrect.

```{figure} images/image392.gif
:alt: Output: One-Sample Z: Test of mu=264 vs not = 264 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.047

Output: One-Sample Z: Test of mu=264 vs not = 264 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.047
```

```{figure} images/image393.gif
:alt: Output: One-Sample Z: Test of mu=267 vs not = 267 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.087

Output: One-Sample Z: Test of mu=267 vs not = 267 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.087
```

```{figure} images/image394.gif
:alt: Output: One-Sample Z: Test of mu=266 vs not = 266 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.027

Output: One-Sample Z: Test of mu=266 vs not = 266 The assumed standard deviation = 16 N: 35 Mean: 260.000 SE Mean: 2.704 95% CI: (254.699, 265.301) Z: -2.22 P: 0.027
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on. If not, then click the link below for some additional practice.

```{note}
    **Sectionnest**

    Hypothesis Testing for the Population Mean (Extra Problem)

    *(Interactive activity — available in the OLI platform)*
```

## Comment

Beyond using the confidence interval as a quick way to carry out the two-sided test, the confidence interval can provide insight into the actual value of the population mean if H~o~ is rejected. In the concentration level example, H~o~ was rejected, and all we could conclude about the mean concentration level of the entire shipment, μ, was that it was not 250. The 95% confidence interval for μ (244.6, 249.4) gives us an idea of what plausible values for μ would be. In particular, we can conclude that since the confidence interval lies below 250, at least a large portion of the shipment contains medication that is ineffective.

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Mean

    *(Interactive activity — available in the OLI platform)*
```

*Do you feel that you understand this concept?* If so, then go ahead and move on. If not, then click the link below for some additional practice.

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Mean (Extra Problems)

    *(Interactive activity — available in the OLI platform)*
```

We are done with the case where the population standard deviation, σ, is known. We now move on to the more common case where σ is unknown.
