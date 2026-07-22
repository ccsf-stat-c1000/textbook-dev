# Finding Probabilities for a Sample Proportion

If a sampling distribution is normally shaped, then we can apply the Standard Deviation Rule and use z-scores to determine probabilities. Let's look at some examples.

:::{admonition} Example: Samples of 100
:class: tip

A random sample of 100 students is taken from the population of all part-time students in the United States, for which the overall proportion of females is 0.6.

(a) There is a 95% chance that the sample proportion ($\hat{p}$) falls between what two values?

First note that the distribution of $\hat{p}$ has mean p = 0.6, standard deviation $\sqrt{\frac{0.6(0.4)}{100}}=0.05$, and a shape that is close to normal, since np = 60 and n(1 − p) = 40 are both greater than 10. The Standard Deviation Rule applies: the probability is approximately 0.95 that $\hat{p}$ falls within 2 standard deviations of the mean, that is, between 0.6 − 2(0.05) and 0.6 + 2(0.05). There is roughly a 95% chance that $\hat{p}$ falls in the interval (0.5, 0.7).

(b) What is the probability that sample proportion $\hat{p}$ is less than or equal to 0.56?

To find $P(\hat{p}\leq0.56)$, we standardize 0.56 to z = (0.56 − 0.60)/0.05 = −0.80:

$$P(\hat{p}\leq0.56)=P(Z\leq-0.80)=0.2119$$
:::

To see the impact of the sample size on these probability calculations, consider the following variation of our example.

:::{admonition} Example: Samples of 2,500
:class: tip

A random sample of *2,500* students is taken from the population of all part-time students in the United States, for which the overall proportion of females is 0.6.

(a) There is a 95% chance that the sample proportion ($\hat{p}$) falls between what two values?

First note that the distribution of $\hat{p}$ has mean p = 0.6, standard deviation $\sqrt{\frac{0.6(0.4)}{2500}}=0.01$, and a shape that is close to normal, since np = 1500 and n(1 − p) = 1000 are both greater than 10. The Standard Deviation Rule applies: the probability is approximately 0.95 that $\hat{p}$ falls within 2 standard deviations of the mean, that is, between 0.6 − 2(0.01) and 0.6 + 2(0.01). There is roughly a 95% chance that $\hat{p}$ falls in the interval (0.58, 0.62).

(b) What is the probability that sample proportion $\hat{p}$ is less than 0.56?

To find $P(\hat{p}\leq0.56)$, we standardize 0.56 to z = (0.56 − 0.60)/0.01 = −4.00:

$$P(\hat{p}\leq0.56)=P(Z\leq-4.0)=0 \text{ (approx.)}$$
:::

```{admonition} Comment
:class: important

As long as the sample is truly random, the distribution of $\hat{p}$ is centered at p, no matter what size sample has been taken. Larger samples have less spread. Specifically, when we multiplied the sample size by 25, increasing it from 100 to 2,500, the standard deviation was reduced to 1/5 of the original standard deviation. Sample proportion strays less from population proportion 0.6 when the sample is larger: it tends to fall anywhere between 0.5 and 0.7 for samples of size 100, whereas it tends to fall between 0.58 and 0.62 for samples of size 2,500. It is not so improbable to take a value as low as 0.56 for samples of 100 (probability is more than 20%), but it is almost impossible to take a value as low as 0.56 for samples of 2,500 (probability is virtually zero).
```

The purpose of this next activity is to give guided practice in finding the sampling distribution of the sample proportion ($\hat{p}$), and using it to draw conclusions about what values of $\hat{p}$ we are most likely to get.

## Check Your Understanding: Finding Probabilities for a Sample Proportion

The proportion of left-handed people in the general population is about 0.1. Suppose a random sample of 225 people is observed.

:::{quiz} What are the mean and standard deviation of the sampling distribution of p-hat?
:hint: Mean = p = 0.1; SD = √(0.1 × 0.9/225).
:feedback-0: Correct! Mean = 0.1 and SD = √(0.09/225) = 0.02.
:feedback-1: The mean of the sampling distribution is the population proportion 0.1, not the sample size fraction.
:feedback-2: SD = √(0.1 × 0.9/225) = √0.0004 = 0.02, not 0.09.
* *Mean 0.1, SD 0.02
* Mean 0.5, SD 0.02
* Mean 0.1, SD 0.09
:::

:::{quiz} Can we use the normal distribution to describe p-hat here?
:hint: np = 22.5 and n(1 − p) = 202.5.
:feedback-0: Correct! Both np = 22.5 and n(1 − p) = 202.5 are at least 10.
:feedback-1: Recheck: np = 225 × 0.1 = 22.5 ≥ 10.
* *Yes—both conditions are satisfied
* No—np is too small
:::

:::{quiz} There is a 95% chance that the sample proportion of left-handed people falls between what two values?
:hint: Use mean ± 2 SD: 0.1 ± 2(0.02).
:feedback-0: Correct! 0.1 ± 0.04 gives the interval (0.06, 0.14).
:feedback-1: (0.08, 0.12) is mean ± 1 SD, which covers only about 68%.
:feedback-2: Remember to multiply the SD by 2 for the 95% interval.
* *(0.06, 0.14)
* (0.08, 0.12)
* (0.05, 0.15)
:::

:::{quiz} What is the probability that the sample of 225 people contains a sample proportion of left-handed people greater than 0.15?
:hint: z = (0.15 − 0.10)/0.02 = 2.5.
:feedback-0: Correct! P(Z > 2.5) = P(Z < −2.5) = 0.0062—very unlikely.
:feedback-1: 0.9938 is the probability of being BELOW 0.15.
:feedback-2: 2.5 is the z-score; convert it to a probability with the table.
* *About 0.006
* About 0.994
* 2.5
:::

## Theoretical Derivation (Optional)

The above results for the distribution of sample proportion $\hat{p}$ are directly related to the results already obtained for the distribution of sample count X in a binomial experiment. Remember that X had mean np, standard deviation $\sqrt{np(1-p)}$, and a shape that allowed for normal approximations as long as both np and n(1 − p) were at least 10. Since sample proportion is $\hat{p}=\frac{X}{n}$, we can derive the mean and standard deviation of $\hat{p}$ by applying the Rules for Means and Variances:

$$\mu_{\hat{p}}=\mu_{X/n}=\frac{1}{n}\mu_{X}=\frac{1}{n}(np)=p$$

$$\sigma_{\hat{p}}^{2}=\sigma_{X/n}^{2}=\frac{1}{n^{2}}\sigma_{X}^{2}=\frac{1}{n^{2}}np(1-p)=\frac{p(1-p)}{n} \implies \sigma_{\hat{p}}=\sqrt{\frac{p(1-p)}{n}}$$

The requirements that np and n(1 − p) be at least 10 are the same, whether we are focusing on the distribution of sample count or the distribution of sample proportion. After all, the shape of $\hat{p}$ is the same as the shape of X: the scale of the horizontal axis is just uniformly divided by n.
