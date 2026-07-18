# What Makes a Good Point Estimator?

```{admonition} Learning Objectives
:class: note

- Determine point estimates in simple cases, and make the connection between the sampling distribution of a statistic and its properties as a point estimator.
```

## Unbiased Estimators

You may feel that since it is so intuitive, you could have figured out point estimation on your own, even without the benefit of an entire course in statistics. Certainly, our intuition tells us that the best estimator for $\mu$ should be $\bar{x}$, and the best estimator for p should be $\hat{p}$.

Probability theory does more than this; it actually gives an explanation (beyond intuition) *why* $\bar{x}$ and $\hat{p}$ are the good choices as point estimators for $\mu$ and p, respectively. In the Sampling Distributions module of the Probability unit, we learned about the sampling distribution of $\bar{X}$ and found that *as long as a sample is taken at random*, the distribution of sample means is exactly centered at the value of the population mean.

$\bar{X}$ is therefore said to be an *unbiased estimator* for $\mu$. Any particular sample mean might turn out to be less than the actual population mean, or it might turn out to be more. But in the long run, such sample means are "on target" in that they will not underestimate any more or less often than they overestimate.

Likewise, we learned that the sampling distribution of the sample proportion, $\hat{p}$, is centered at the population proportion p (as long as the sample is taken at random), thus making $\hat{p}$ an *unbiased estimator* for p.

As stated in the introduction, probability theory plays an essential role as we establish results for statistical inference. Our assertion above that sample mean and sample proportion are unbiased estimators is the first such instance.

## The Role of Random Sampling and Design

Notice how important the principles of sampling and design are for our above results: if the sample of U.S. adults in the marijuana example was not random, but instead included predominantly college students, then 0.56 would be a biased estimate for p, the proportion of all U.S. adults who believe marijuana should be legalized. If the survey design were flawed, such as loading the question with a reminder about the dangers of marijuana leading to hard drugs, or a reminder about the benefits of marijuana for cancer patients, then 0.56 would be biased on the low or high side, respectively. Our point estimates are truly unbiased estimates for the population parameter only if the *sample is random and the study design is not flawed.*

## Accuracy Improves with Sample Size

Not only are sample mean and sample proportion on target as long as the samples are random, but their accuracy improves as sample size increases. Again, there are two "layers" here for explaining this.

Intuitively, larger sample sizes give us more information with which to pin down the true nature of the population. We can therefore expect the sample mean and sample proportion obtained from a larger sample to be closer to the population mean and proportion, respectively. In the extreme, when we sample the whole population (which is called a census), the sample mean and sample proportion will exactly coincide with the population mean and population proportion.

There is another layer here that, again, comes from what we learned about the sampling distributions of the sample mean and the sample proportion. Let's use the sample mean for the explanation.

Recall that the sampling distribution of the sample mean $\bar{X}$ is, as we mentioned before, centered at the population mean $\mu$ and has a standard deviation of $\frac{\sigma}{\sqrt{n}}$. As a result, as the sample size n increases, the sampling distribution of $\bar{X}$ gets less spread out. This means that values of $\bar{X}$ that are based on a larger sample are more likely to be closer to $\mu$ (as the figure below illustrates):

```{figure} images/gen/m14-sample-size-precision.svg
:alt: Two sampling distribution curves for the sample mean, both centered at the population mean. The red curve, from a smaller sample size, is short and widely spread. The blue curve, from a larger sample size, is tall and narrow, so its sample means are much more likely to be close to the population mean.
```

Similarly, since the sampling distribution of $\hat{p}$ is centered at p and has a standard deviation of $\sqrt{\frac{p(1-p)}{n}}$, which decreases as the sample size gets larger, values of $\hat{p}$ are more likely to be closer to p when the sample size is larger.

## Estimating the Population Variance

Another example of a point estimate is using the sample variance, $s^{2}=\frac{(x_{1}-\bar{x})^{2}+\cdots+(x_{n}-\bar{x})^{2}}{n-1}$, to estimate the population variance, $\sigma^{2}$.

In this course, we will not be concerned with estimating $\sigma^{2}$ for its own sake, but since we will often substitute s for $\sigma$ when standardizing the sample mean, it is worth pointing out that $s^{2}$ is an unbiased estimator for $\sigma^{2}$. If we had divided by n instead of n − 1 in our estimator for population variance, then in the long run our sample variance would be guilty of a slight underestimation. Division by n − 1 accomplishes the goal of making this point estimator unbiased. Making unbiased estimators a top priority is, in fact, the reason that our formula for s, introduced in the Exploratory Data Analysis unit, involves division by n − 1 instead of by n.

## Let's Summarize

We use $\hat{p}$ (sample proportion) as a point estimator for p (population proportion). It is an unbiased estimator: its long-run distribution is centered at p as long as the sample is random.

We use $\bar{x}$ (sample mean) as a point estimator for $\mu$ (population mean). It is an unbiased estimator: its long-run distribution is centered at $\mu$ as long as the sample is random.

In both cases, the larger the sample size, the more accurate the point estimator is. In other words, the larger the sample size, the more likely it is that the sample mean (proportion) is close to the unknown population mean (proportion).

## Check Your Understanding: Unbiased Estimators

:::{quiz} What does it mean to say that x-bar is an "unbiased" estimator of μ?
:hint: Think about where the sampling distribution of x-bar is centered.
:feedback-0: Correct! Unbiased means the sampling distribution of x-bar is centered exactly at μ—it neither systematically overestimates nor underestimates.
:feedback-1: Individual sample means almost never equal μ exactly; unbiasedness is a long-run, on-average property.
:feedback-2: Unbiasedness concerns the center of the estimator's distribution, not its spread.
* *In repeated random samples, the values of x-bar average out to exactly μ
* Every sample mean equals μ exactly
* The sample mean has no variability
:::

:::{quiz} Two researchers estimate the same population proportion. One uses a random sample of 400; the other uses a random sample of 4,000. What can we say about the two estimates?
:hint: Both are unbiased, but their sampling distributions have different spreads.
:feedback-0: Correct! Both estimators are unbiased (centered at p), but the larger sample's estimate is more likely to fall close to p because its sampling distribution has a smaller standard deviation.
:feedback-1: Random samples of any size give unbiased estimates; the difference is in precision, not bias.
:feedback-2: The larger sample cannot guarantee a closer estimate in any particular case—it just makes closeness much more likely.
* *Both are unbiased, but the estimate from 4,000 is likely to be closer to p
* The smaller sample gives a biased estimate
* The larger sample's estimate is guaranteed to be closer to p
:::
