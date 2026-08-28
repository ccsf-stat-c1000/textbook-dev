# The Sampling Distribution of the Sample Proportion

Again, the simulations on the previous page reinforced what makes sense to our intuition. Larger random samples will better approximate the population proportion. When the sample size is large, sample proportions will be closer to p. In other words, the sampling distribution for large samples has less variability. Advanced probability theory confirms our observations and gives a more precise way to describe the standard deviation of the sample proportions. This is described next.

## The Sampling Distribution of the Sample Proportion

If repeated random samples of a given size n are taken from a population of values for a categorical variable, where the proportion in the category of interest is p, then the mean of all sample proportions ($\hat{p}$) is the population proportion (p). As for the spread of all sample proportions, theory dictates the behavior much more precisely than saying that there is less spread for larger samples. In fact, the standard deviation of all sample proportions ($\hat{p}$) is exactly

$$\sigma_{\hat{p}}=\sqrt{\frac{p(1-p)}{n}}$$

Since sample size n appears in the denominator of the square root, the standard deviation does decrease as sample size increases. Finally, the shape of the distribution of $\hat{p}$ will be approximately normal as long as the sample size n is large enough. The convention is to require both np and n(1 - p) to be at least 10.

We can summarize all of the above as follows:

```{admonition} The Sampling Distribution of p-hat
:class: note

$\hat{p}$ has an approximately normal distribution with mean $\mu_{\hat{p}}=p$ and standard deviation $\sigma_{\hat{p}}=\sqrt{\frac{p(1-p)}{n}}$ (as long as np and n(1 - p) are at least 10).
```

Let's apply this result to our example and see how it compares with our simulation.

In our example, $n = 100$ (sample size) and $p = 0.6$. Note that $np = 60 \geq 10$ and $n(1 - p) = 40 \geq 10$. Therefore we can conclude that $\hat{p}$ is approximately normal with mean $p = 0.6$ and standard deviation $\sqrt{\frac{0.6(0.4)}{100}}=0.049$ (which is very close to what we saw in our simulation).

## Check Your Understanding: The Sampling Distribution of the Sample Proportion

According to the National Postsecondary Student Aid Study conducted by the U.S. Department of Education in 2008, 62% of graduates from public universities had student loans. Suppose we take random samples of 100 graduates.

:::{quiz} What are the mean and standard deviation of the sampling distribution of p-hat for samples of size 100?
:hint: Mean = p; SD = $\sqrt{p(1-p)/n} = \sqrt{0.62 \times 0.38/100}$.
:feedback-0: Correct! Mean = 0.62 and SD = $\sqrt{0.002356} \approx 0.049$.
:feedback-1: The mean of the sampling distribution equals the population proportion, 0.62—not 0.5.
:feedback-2: Don't forget to divide by n inside the square root: $\sqrt{0.62 \times 0.38/100} \approx 0.049$.
* *Mean 0.62, SD $\approx 0.049$
* Mean 0.5, SD $\approx 0.049$
* Mean 0.62, SD $\approx 0.485$
:::

:::{quiz} Is it appropriate to describe this sampling distribution as approximately normal?
:hint: Check np = 62 and n(1 - p) = 38.
:feedback-0: Correct! np = 62 and n(1 - p) = 38 are both at least 10, so the normal shape applies.
:feedback-1: Both conditions are satisfied here—recompute np and n(1 - p).
* *Yes—np = 62 and n(1 - p) = 38 both exceed 10
* No—the conditions fail
:::

:::{quiz} A random sample of 100 graduates from one university finds that only 50 had student loans (p-hat = 0.50). Using the 2-standard-deviations criterion, is this sample unusual if p really is 0.62?
:hint: $z = (0.50 - 0.62)/0.049 \approx -2.4$.
:feedback-0: Correct! 0.50 is about 2.4 standard deviations below 0.62—outside the ordinary range (0.52, 0.72)—so this would be an unusual sample (or perhaps this university differs from the population).
:feedback-1: Compare with the ordinary range $0.62 \pm 2(0.049) = (0.52$, 0.72): 0.50 falls outside it.
* *Yes—0.50 is more than 2 standard deviations below 0.62
* No—0.50 is within 2 standard deviations of 0.62
:::

## Check Your Understanding: When the Normal Model Fails

The proportion of left-handed people in the general population is about 0.10. To simulate this population, we constructed a collection in which $p = 0.10$. We then conducted four simulations, drawing 1,005 random samples of each of four different sizes from this collection. Here are the summary statistics of the resulting sampling distributions:

| Sample size n | Mean of p-hats | SD of p-hats | Shape |
| --- | --- | --- | --- |
| 20 | 0.1009 | 0.0675 | strongly skewed right |
| 50 | 0.1027 | 0.0418 | skewed right |
| 100 | 0.1006 | 0.0287 | approximately normal |
| 200 | 0.1001 | 0.0222 | very close to normal |

:::{quiz} Why are the sampling distributions for $n = 20$ and $n = 50$ skewed right rather than normal?
:hint: Check the rule of thumb: np must be at least 10.
:feedback-0: Correct! For $n = 20$, np = 2, and for $n = 50$, np = 5—both below 10—so the normal approximation doesn't hold; the distribution piles up near 0 and stretches right.
:feedback-1: The mean is close to 0.10 in every case; the problem is the shape, governed by whether np $\geq 10$.
:feedback-2: More simulations wouldn't change the shape—the skew comes from the small sample size relative to p.
* *Because np is less than 10 for those sample sizes
* Because their means are wrong
* Because not enough samples were simulated
:::
