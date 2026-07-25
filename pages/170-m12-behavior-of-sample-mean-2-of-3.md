# The Central Limit Theorem

The results we got in our simulations are not surprising. Advanced probability theory confirms them by asserting the following:

## The Sampling Distribution of the Sample Mean

If repeated random samples of a given size n are taken from a population of values for a quantitative variable, where the population mean is $\mu$ and the population standard deviation is $\sigma$, then the mean of all sample means ($\bar{x}$) is the population mean $\mu$. As for the spread of all sample means, theory dictates the behavior much more precisely than saying that there is less spread for larger samples. In fact, the standard deviation of all sample means ($\bar{x}$) is exactly

$$\sigma_{\bar{x}}=\frac{\sigma}{\sqrt{n}}$$

Since the square root of sample size n appears in the denominator, the standard deviation does decrease as sample size increases.

## Check Your Understanding: The Sampling Distribution of the Sample Mean

The Federal Pell Grant Program provides need-based grants to low-income undergraduate and certain postbaccalaureate students to promote access to postsecondary education. According to the National Postsecondary Student Aid Study conducted by the U.S. Department of Education in 2008, the average Pell grant award for 2007-2008 was \$2,600. Assume that the standard deviation in Pell grant awards was \$500.

:::{quiz} If we take random samples of 25 Pell grant recipients, what are the mean and standard deviation of the sampling distribution of the sample mean award?
:hint: Mean = $\mu = 2{,}600$; SD = $\sigma/\sqrt{n} = 500/\sqrt{25}$.
:feedback-0: Correct! Mean = \$2,600 and SD = 500/5 = \$100.
:feedback-1: The standard deviation of the sample mean is $\sigma/\sqrt{n}$, not $\sigma$ itself.
:feedback-2: $\sqrt{25} = 5$, so the SD is $500/5 = 100$, not 20.
* *Mean $2,600, SD $100
* Mean $2,600, SD $500
* Mean $2,600, SD $20
:::

:::{quiz} To cut the standard deviation of the sample mean in half (from \$100 to \$50), how large would the samples need to be?
:hint: $\sigma/\sqrt{n} = 50$ requires $\sqrt{n} = 10$.
:feedback-0: Correct! Halving the SD requires quadrupling the sample size: $n = 100$.
:feedback-1: Doubling the sample size to 50 only reduces the SD by a factor of $\sqrt{2}$.
:feedback-2: n appears under a square root, so the SD shrinks slowly—quadrupling n halves the SD.
* *100
* 50
* 2,500
:::

Let's compare and contrast what we now know about the sampling distributions for sample means and sample proportions:

| Variable | Parameter | Statistic | Center | Spread | Shape |
| --- | --- | --- | --- | --- | --- |
| Categorical (e.g., left-handed or not) | p | $\hat{p}$ | p | $\sqrt{\frac{p(1-p)}{n}}$ | Normal if np $\geq 10$ and n(1 - p) $\geq 10$ |
| Quantitative (e.g., age) | $\mu$, $\sigma$ | $\bar{x}$ | $\mu$ | $\frac{\sigma}{\sqrt{n}}$ | *When will it be approximately normal?* |

Now we will investigate the shape of the sampling distribution of sample means. When we were discussing the sampling distribution of sample proportions, we said that this distribution is approximately normal if np $\geq 10$ and n(1 - p) $\geq 10$. In other words, we had a guideline based on sample size for determining the conditions under which we could use normal probability calculations for sample proportions.

When will the distribution of sample means be approximately normal? Does this depend on the size of the sample?

It seems reasonable that a population with a normal distribution will have sample means that are normally distributed even for very small samples. We saw this illustrated in the previous simulation with samples of size 9.

What happens if the distribution of the variable in the population is heavily skewed? Do sample means have a skewed distribution also? If we take really large samples, will the sample means become more normally distributed?

In the next simulation video, we investigate these questions:

```{note} Video

[Behavior of Sample Mean 2](https://www.youtube.com/watch?v=cyNqdostWzk)
```

To summarize, the distribution of sample means will be approximately normal as long as the sample size is large enough. This discovery is probably the single most important result presented in introductory statistics courses. It is stated formally as the {term}`Central Limit Theorem <central limit theorem>`.

We will depend on the Central Limit Theorem again and again in order to do normal probability calculations when we use sample means to draw conclusions about a population mean. We now know that we can do this even if the population distribution is not normal.

How large a sample size do we need in order to assume that sample means will be normally distributed? Well, it really depends on the population distribution, as we saw in the simulation. The general rule of thumb is that samples of size 30 or greater will have a fairly normal distribution regardless of the shape of the distribution of the variable in the population.

*Comment:* For categorical variables, our claim that sample proportions are approximately normal for large enough n is actually a special case of the Central Limit Theorem.

## Check Your Understanding: The Central Limit Theorem

:::{quiz} Household incomes in a city are strongly skewed right. If we take random samples of 100 households and compute the mean income of each sample, what shape will the distribution of these sample means have?
:hint: Apply the Central Limit Theorem: $n = 100$ is well above 30.
:feedback-0: Correct! By the Central Limit Theorem, with $n = 100$ the sample means are approximately normal even though the population is skewed.
:feedback-1: The skewness of the population does NOT carry over to the sample means when n is large—that's the magic of the CLT.
:feedback-2: The shape is predictable: approximately normal, centered at $\mu$, with SD $\sigma/\sqrt{100}$.
* *Approximately normal
* Skewed right, like the population
* Unpredictable
:::

:::{quiz} A population is exactly normal. How large must samples be for the sampling distribution of the sample mean to be normal?
:hint: What did the simulation with samples of size 9 show?
:feedback-0: Correct! If the population itself is normal, the sample mean is exactly normal for ANY sample size, even $n = 2$.
:feedback-1: The $n \geq 30$ rule of thumb is only needed when the population is NOT normal.
* *Any sample size—the sample mean is normal even for tiny samples
* At least 30, as always
:::
