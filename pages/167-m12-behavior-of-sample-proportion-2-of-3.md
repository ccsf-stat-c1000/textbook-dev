# Behavior of Sample Proportion (2 of 3)

```{admonition} Learning Objectives
    - Apply the sampling distribution of the sample proportion (when appropriate). In particular, be able to identify unusual samples from a given population.
```

Again, the simulations on the previous page reinforced what makes sense to our intuition. Larger random samples will better approximate the population proportion. When the sample size is large, sample proportions will be closer to p. In other words, the sampling distribution for large samples has less variability. Advanced probability theory confirms our observations and gives a more precise way to describe the standard deviation of the sample proportions. This is described next.

## The Sampling Distribution of the Sample Proportion

If repeated random samples of a given size n are taken from a population of values for a categorical variable, where the proportion in the category of interest is p, then the mean of all sample proportions ($\hat{p}$) is the population proportion (p). As for the spread of all sample proportions, theory dictates the behavior much more precisely than saying that there is less spread for larger samples. In fact, the standard deviation of all sample proportions ($\hat{p}$) is exactly $\sqrt{\frac{p(1-p)}{n}}$.

Since sample size n appears in the denominator of the square root, the standard deviation does decrease as sample size increases. Finally, the shape of the distribution of $\hat{p}$ will be approximately normal as long as the sample size n is large enough. The convention is to require both np and n(1 - p) to be at least 10.

We can summarize all of the above by the following:

$\hat{p}$ has a normal distribution with a mean of $\mu_{\hat{p}}=p$ and standard deviation $\sigma_{\hat{p}}=\sqrt{\frac{p(1-p)}{n}}$ (and as long as np and n(1 - p) are at least 10).

Let's apply this result to our example and see how it compares with our simulation.

In our example, n = 25 (sample size) and p = 0.6. Note that np = 15 ≥ 10 and n(1 - p) = 10 ≥ 10. Therefore we can conclude that $\hat{p}$ is approximately a normal distribution with mean p = 0.6 and standard deviation $\sqrt{\frac{p(1-p)}{n}}=\sqrt{\frac{0.6(1-0.6)}{25}}=0.097$ (which is very close to what we saw in our simulation).

##### Learn By Doing

According to the National Postsecondary Student Aid Study conducted by the U.S. Department of Education in 2008, 62% of graduates from public universities had student loans.

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

##### Learn By Doing

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

The proportion of left-handed people in the general population is about 0.10. To simulate this population, we constructed a collection in which p = 0.10. We then conducted four simulations, drawing random samples of different sizes from this collection. Here you see the resulting sampling distributions and corresponding summary tables:

```{figure} images/9_1_img1.gif
:alt: A set of sampling distributions and tables for N=20, 50, 100, and 200 . For each sample size, 1005 samples were taken. For N=200, the resulting distribution histogram very closely resembles a normal shape. The mean is 0.100095, and the stdDev is 0.0221608 . For N=100, the distribution histogram is also an approximation of a normal curve. Since the scale for this histogram is the same as for N=200, the bars are wider. The mean is 0.100557, and the stdDev is 0.0287191 . For N=50, the histogram has even wider bars. The left part of the normal curve has been cut off because it rests below a proportion of 0, which cannot happen. So, the histogram is right skewed. The mean is 0.102706, and the stdDdev is 0.0418382 . For N=20, the histogram suffers the same problem as for N=50, except on a much worse level. The mean is 0.100896, and the stdDev is 0.067461 .

A set of sampling distributions and tables for N=20, 50, 100, and 200 . For each sample size, 1005 samples were taken. For N=200, the resulting distribution histogram very closely resembles a normal shape. The mean is 0.100095, and the stdDev is 0.0221608 . For N=100, the distribution histogram is also an approximation of a normal curve. Since the scale for this histogram is the same as for N=200, the bars are wider. The mean is 0.100557, and the stdDev is 0.0287191 . For N=50, the histogram has even wider bars. The left part of the normal curve has been cut off because it rests below a proportion of 0, which cannot happen. So, the histogram is right skewed. The mean is 0.102706, and the stdDdev is 0.0418382 . For N=20, the histogram suffers the same problem as for N=50, except on a much worse level. The mean is 0.100896, and the stdDev is 0.067461 .
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
