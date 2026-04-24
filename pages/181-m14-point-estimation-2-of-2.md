# Point Estimation (2 of 2)

```{admonition} Learning Objectives
    - Determine point estimates in simple cases, and make the connection between the sampling distribution of a statistic, and its properties as a point estimator.
```

## Comment 1

You may feel that since it is so intuitive, you could have figured out point estimation on your own, even without the benefit of an entire course in statistics. Certainly, our intuition tells us that the best estimator for $\mu$ should be $\bar{x}$, and the best estimator for p should be $\hat{p}$.

Probability theory does more than this; it actually gives an explanation (beyond intuition) *why* $\bar{x}$ and $\hat{p}$ are the good choices as point estimators for $\mu$ and p, respectively. In the Sampling Distributions module of the Probability unit, we learned about the sampling distributions of $\bar{X}$ and found that *as long as a sample is taken at random*, the distribution of sample means is exactly centered at the value of population mean.

```{figure} images/image019.gif
:alt: A normal distribution curve, in which the horizontal axis is labeled "X bar." The possible values of x-bar are centered at μ.

A normal distribution curve, in which the horizontal axis is labeled "X bar." The possible values of x-bar are centered at μ.
```

$\bar{X}$ is therefore said to be an *unbiased estimator* for $\mu$ . Any particular sample mean might turn out to be less than the actual population mean, or it might turn out to be more. But in the long run, such sample means are "on target" in that they will not underestimate any more or less often than they overestimate.

Likewise, we learned that the sampling distribution of the sample proportion, $\hat{p}$, is centered at the population proportion p (as long as the sample is taken at random), thus making $\hat{p}$ an *unbiased estimator* for p.

```{figure} images/image020.gif
:alt: A normal distribution curve with a horizontal axis labeled "p hat." The possible values of p-hat are centered at p .

A normal distribution curve with a horizontal axis labeled "p hat." The possible values of p-hat are centered at p .
```

As stated in the introduction, probability theory plays an essential role as we establish results for statistical inference. Our assertion above that sample mean and sample proportion are unbiased estimators is the first such instance.

## Comment 2

Notice how important the principles of sampling and design are for our above results: if the sample of U.S. adults in (example 2 on the previous page) was not random, but instead included predominantly college students, then .56 would be a biased estimate for p, the proportion of all U.S. adults who believe marijuana should be legalized. If the survey design were flawed, such as loading the question with a reminder about the dangers of marijuana leading to hard drugs, or a reminder about the benefits of marijuana for cancer patients, then .56 would be biased on the low or high side, respectively. Our point estimates are truly unbiased estimates for the population parameter only if the *sample is random and the study design is not flawed.*

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comment 3

Not only are sample mean and sample proportion on target as long as the samples are random, but their accuracy improves as sample size increases. Again, there are two "layers" here for explaining this.

Intuitively, larger sample sizes give us more information with which to pin down the true nature of the population. We can therefore expect the sample mean and sample proportion obtained from a larger sample to be closer to the population mean and proportion, respectively. In the extreme, when we sample the whole population (which is called a census), the sample mean and sample proportion will exactly coincide with the population mean and population proportion.

There is another layer here that, again, comes from what we learned about the sampling distributions of the sample mean and the sample proportion. Let's use the sample mean for the explanation.

Recall that the sampling distribution of the sample mean $\bar{X}$ is, as we mentioned before, centered at the population mean $\mu$ and has a standard deviation of $\frac{\sigma}{\sqrt{n}}$. As a result, as the sample size n increases, the sampling distribution of $\bar{X}$ gets less spread out. This means that values of $\bar{X}$ that are based on a larger sample are more likely to be closer to $\mu$ (as the figure below illustrates):

```{figure} images/image022.gif
:alt: Two sampling distribution curves for x-bar. One is squished down and wider, while the other is much taller and narrower. Both curves share the same μ. The tall, narrow distribution was based on a larger sample size, which has a smaller standard deviation, and so is less spread out. This means that values of x-bar are more likely to be closer to μ when the sample size is larger.

Two sampling distribution curves for x-bar. One is squished down and wider, while the other is much taller and narrower. Both curves share the same μ. The tall, narrow distribution was based on a larger sample size, which has a smaller standard deviation, and so is less spread out. This means that values of x-bar are more likely to be closer to μ when the sample size is larger.
```

Similarly, since the sampling distribution of $\hat{p}$ is centered at p and has a standard deviation of $\sqrt{\frac{p(1−p)}{n}}$, which decreases as the sample size gets larger, values of $\hat{p}$ are more likely to be closer to p when the sample size is larger.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comment 4

Another example of a point estimate is using sample variance, $s^{2}=\frac{\left(x_{1}−\bar{x}\right)^{2}+...+\left(x_{n}−\bar{x}\right)^{2}}{n−1}$, to estimate population variance, $\sigma^{2}$ .

In this course, we will not be concerned with estimating $\sigma^{2}$ for its own sake, but since we will often substitute s for $\sigma$ when standardizing the sample mean, it is worth pointing out that $s^{2}$ is an unbiased estimator for $\sigma^{2}$. If we had divided by n instead of n - 1 in our estimator for population variance, then in the long run our sample variance would be guilty of a slight underestimation. Division by n - 1 accomplishes the goal of making this point estimator unbiased. Making unbiased estimators a top priority is, in fact, the reason that our formula for s, introduced in the Exploratory Data Analysis unit, involves division by n - 1 instead of by n.

## Let's Summarize

We use $\hat{p}$ (sample proportion) as a point estimator for p (population proportion). It is an unbiased estimator: its long-run distribution is centered at p as long as the sample is random.

We use $\bar{x}$ (sample mean) as a point estimator for $\mu$ (population mean). It is an unbiased estimator: its long-run distribution is centered at $\mu$ as long as the sample is random.

In both cases, the larger the sample size, the more accurate the point estimator is. In other words, the larger the sample size, the more likely it is that the sample mean (proportion) is close to the unknown population mean (proportion).

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## End-of-Lesson
                Questions

```{note}
    **My Response**

    About Point Estimation

    *(Interactive activity — available in the OLI platform)*
```
