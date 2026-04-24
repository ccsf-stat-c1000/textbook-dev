# Behavior of Sample Mean (2 of 3)

```{admonition} Learning Objectives
    - Apply the sampling distribution of the sample mean as summarized by the Central Limit Theorem (when appropriate). In particular, be able to identify unusual samples from a given population.
```

The results we got in our simulations are not surprising. Advanced probability theory confirms that by asserting the following:

## The Sampling Distribution of the Sample Mean

If repeated random samples of a given size n are taken from a population of values for a quantitative variable, where the population mean is $\mu$ and the population standard deviation is $\sigma$, then the mean of all sample means ($\bar{x}$) is population mean $\mu$. As for the spread of all sample means, theory dictates the behavior much more precisely than saying that there is less spread for larger samples. In fact, the standard deviation of all sample means ($\bar{x}$) is exactly $\frac{\sigma}{\sqrt{n}}$. Since the square root of sample size n appears in the denominator, the standard deviation does decrease as sample size increases.

##### Learn By Doing

The Federal Pell Grant Program provides need-based grants to low-income undergraduate and certain postbaccalaureate students to promote access to postsecondary education. According to the National Postsecondary Student Aid Study conducted by the U.S. Department of Education in 2008, the average Pell grant award for 2007-2008 was $2,600. Assume that the standard deviation in Pell grant awards was $500.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

Let's compare and contrast what we now know about the sampling distributions for sample means and sample proportions.

|  |  |  | Sampling Distribution | Variable | Parameter | Statistic | Center | Spread | Shape |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Categorical (example: left-handed or not) | p = population proportion | $\hat{p}$ = sample proportion | p | $\sqrt{\frac{p(1-p)}{n}}$ | Normal IF np ≥ 10 and n(1 - p) ≥ 10 |  |  |  |  |
| Quantitative (example: age) | μ = population mean, σ = population standard deviation | $\bar{x}$ = sample mean | μ | $\frac{\sigma}{\sqrt{n}}$ | *When will the distribution of sample means be approximately normal                                 ?* |  |  |  |  |

Now we will investigate the shape of the sampling distribution of sample means. When we were discussing the sampling distribution of sample proportions, we said that this distribution is approximately normal if np ≥ 10 and n(1 - p) ≥ 10. In other words, we had a guideline based on sample size for determining the conditions under which we could use normal probability calculations for sample proportions.

When will the distribution of sample means be approximately normal? Does this depend on the size of the sample?

It seems reasonable that a population with a normal distribution will have sample means that are normally distributed even for very small samples. We saw this illustrated in the previous simulation with samples of size 9.

What happens if the distribution of the variable in the population is heavily skewed? Do sample means have a skewed distribution also? If we take really large samples, will the sample means become more normally distributed?

In the next simulation, we will investigate these questions.

```{note} Video
[Behavior of Sample Mean 2](https://www.youtube.com/watch?v=cyNqdostWzk)
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

To summarize, the distribution of sample means will be approximately normal as long as the sample size is large enough. This discovery is probably the single most important result presented in introductory statistics courses. It is stated formally as the Central Limit Theorem.

We will depend on the Central Limit Theorem again and again in order to do normal probability calculations when we use sample means to draw conclusions about a population mean. We now know that we can do this even if the population distribution is not normal.

How large a sample size do we need in order to assume that sample means will be normally distributed? Well, it really depends on the population distribution, as we saw in the simulation. The general rule of thumb is that samples of size 30 or greater will have a fairly normal distribution regardless of the shape of the distribution of the variable in the population.

Comment: For categorical variables, our claim that sample proportions are approximately normal for large enough n is actually a special case of the Central Limit Theorem.
