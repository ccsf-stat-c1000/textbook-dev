# Applying the Central Limit Theorem

Before we work some examples, let's compare and contrast what we now know about the sampling distributions for sample means and sample proportions:

| Variable | Parameter | Statistic | Center | Spread | Shape |
| --- | --- | --- | --- | --- | --- |
| Categorical (e.g., left-handed or not) | p | $\hat{p}$ | p | $\sqrt{\frac{p(1-p)}{n}}$ | Normal if np $\geq 10$ and n(1 - p) $\geq 10$ |
| Quantitative (e.g., age) | $\mu$, $\sigma$ | $\bar{x}$ | $\mu$ | $\frac{\sigma}{\sqrt{n}}$ | Normal if $n \geq 30$ (always normal if the population is normal) |

## Check Your Understanding: The Central Limit Theorem in Action

Recall our earlier scenario: the average Pell grant award for 2007-2008 was \$2,600, with a standard deviation of \$500. Nothing was said about the shape of the distribution of individual awards.

:::{quiz} Can we compute the probability that the mean award in a random sample of 8 recipients exceeds \$2,800?
:hint: Is the sample large enough for the Central Limit Theorem, and do we know the population's shape?
:feedback-0: Correct! With a small sample (8) and an unknown (possibly non-normal) population shape, the CLT doesn't apply, so we can't do a normal calculation.
:feedback-1: $n = 8$ is far below the rule of thumb of 30, and we don't know the population is normal.
* *No—the sample is too small and the population shape is unknown
* Yes—sample means are always normal
:::

:::{quiz} What about the probability that the mean award in a random sample of 100 recipients exceeds \$2,700?
:hint: $n = 100 \geq 30$, so the CLT applies: SD of the mean = $500/\sqrt{100} = 50$, $z = (2700 - 2600)/50 = 2$.
:feedback-0: Correct! By the CLT, x-bar is approximately normal with mean 2,600 and SD 50; $z = 2$, so $P \approx 0.025$.
:feedback-1: 0.16 corresponds to 1 standard deviation; \$2,700 is 2 standard deviations above the mean here.
:feedback-2: The CLT applies because $n = 100$ is large, even if individual awards aren't normal.
* *Yes—about 0.025
* Yes—about 0.16
* No—we can't compute it
:::

:::{admonition} Example: Household Size
:class: tip

Household size in the United States has a mean of 2.6 people and standard deviation of 1.4 people.

(a) What is the probability that a randomly chosen household has more than 3 people?

A normal approximation should not be used here, because the distribution of household sizes would be considerably skewed to the right. We do not have enough information to solve this problem.

(b) What is the probability that the mean size of a random sample of 10 households is more than 3?

By anyone's standards, 10 is a small sample size. The Central Limit Theorem does not guarantee a sample mean coming from a skewed population to be approximately normal unless the sample size is large.

(c) What is the probability that the mean size of a random sample of 100 households is more than 3?

Now we may invoke the Central Limit Theorem: even though the distribution of household size X is skewed, the distribution of sample mean household size $\bar{X}$ is approximately normal for a large sample size such as 100. Its mean is the same as the population mean, 2.6, and its standard deviation is the population standard deviation divided by the square root of the sample size:

$$\frac{\sigma}{\sqrt{n}}=\frac{1.4}{\sqrt{100}}=0.14$$

The z-score for 3 is

$$z=\frac{3-2.6}{0.14}=2.86$$

The probability of the mean household size in a sample of 100 being more than 3 is therefore P($\bar{X}$ > 3) = P(Z > 2.86) = P(Z < $-2.86) = 0.0021$.

Households of more than 3 people are, of course, quite common, but it would be extremely unusual for the mean size of a sample of 100 households to be more than 3.
:::

The purpose of the next activity is to give guided practice in finding the sampling distribution of the sample mean ($\bar{X}$), and using it to learn about the likelihood of getting certain values of $\bar{X}$.

## Check Your Understanding: Probabilities for a Sample Mean

The annual salary of teachers in a certain state has a mean of \$54,000 and standard deviation of σ = \$5,000.

:::{quiz} For random samples of 64 teachers, what are the mean and standard deviation of the sampling distribution of the mean salary?
:hint: Mean = $\mu$; SD = $5{,}000/\sqrt{64}$.
:feedback-0: Correct! Mean = \$54,000 and SD = 5,000/8 = \$625.
:feedback-1: Divide $\sigma$ by $\sqrt{64} = 8$, not by 64.
:feedback-2: The center of the sampling distribution is the population mean, \$54,000.
* *Mean $54,000, SD $625
* Mean $54,000, SD $78.13
* Mean $52,000, SD $625
:::

:::{quiz} What is the probability that the mean annual salary of a random sample of 64 teachers from this state is less than \$52,000?
:hint: $z = (52{,}000 - 54{,}000)/625 = -3.2$.
:feedback-0: Correct! P(Z < -3.2) = 0.0007—essentially impossible, so such a sample would strongly suggest the state's mean salary is actually lower than \$54,000.
:feedback-1: 0.34 would correspond to $z \approx -0.4$; here the z-score is -3.2, far in the tail.
:feedback-2: -3.2 is the z-score; the question asks for the probability.
* *About 0.0007
* About 0.34
* -3.2
:::

## Check Your Understanding: Sample Means and the Normal Model

Scores on the math portion of the SAT (SAT-M) in a recent year followed a normal distribution with mean $\mu = 507$ and standard deviation $\sigma = 111$.

:::{quiz} What is the probability that the mean SAT-M score of a random sample of 4 students exceeds 600?
:hint: The population is normal, so x-bar is normal for any n. SD of the mean = $111/\sqrt{4} = 55.5$; $z = (600 - 507)/55.5 \approx 1.68$.
:feedback-0: Correct! Since the population is normal, x-bar is normal even for $n = 4$: $z = 1.68$, so $P \approx 0.0465$.
:feedback-1: The CLT rule of thumb (n $\geq 30)$ is unnecessary here—the population itself is normal, so the sample mean is normal for any n.
:feedback-2: Remember to divide $\sigma$ by $\sqrt{4}$ before standardizing.
* *About 0.046
* It cannot be computed because $n < 30$
* About 0.20
:::
