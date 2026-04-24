# Behavior of Sample Mean (3 of 3)

```{admonition} Learning Objectives
    - Apply the sampling distribution of the sample mean as summarized by the Central Limit Theorem (when appropriate). In particular, be able to identify unusual samples from a given population.
```

Before we work some examples. Let’s compare and contrast what we now know about the sampling distributions for sample means and sample proportions.

|  |  |  | Sampling Distribution | Variable | Parameter | Statistic | Center | Spread | Shape |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Categorical (example: left-handed or not) | p = population proportion | $\hat{p}$ = sample proportion | p | $\sqrt{\frac{p(1-p)}{n}}$ | Normal IF np ≥ 10 and n(1 - p) ≥ 10 |  |  |  |  |
| Quantitative (example: age) | μ = population mean, σ = population standard deviation | $\bar{x}$ = sample mean | μ | $\frac{\sigma}{\sqrt{n}}$ | Normal if n > 30 (always normal if population is normal) |  |  |  |  |

## Learn By Doing

Recall our earlier scenario: The Federal Pell Grant Program provides need-based grants to low-income undergraduate and certain postbaccalaureate students to promote access to postsecondary education. According to the National Postsecondary Student Aid Study conducted by the U.S. Department of Education in 2008, the average Pell grant award for 2007-2008 was $2,600. Assume that the standard deviation in Pell grants awards was $500.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example
    Household size in the United States has a mean of 2.6 people and standard deviation of 1.4 people.

    (a) What is the probability that a randomly chosen household has more than 3 people?

    A normal approximation should not be used here, because the distribution of household sizes would be considerably skewed to the right. We do not have enough information to solve this problem.

    (b) What is the probability that the mean size of a random sample of 10 households is more than 3?

    By anyone's standards, 10 is a small sample size. The Central Limit Theorem does not guarantee sample mean coming from a skewed population to be approximately normal unless the sample size is large.

    (c) What is the probability that the mean size of a random sample of 100 households is more than 3?

    Note: To review how to determine probabilities for z scores, please refer to the Standard Normal Table section of the Random Variables module.

    Now we may invoke the Central Limit Theorem: even though the distribution of household size X is skewed, the distribution of sample mean household size $\bar{X}$ is approximately normal for a large sample size such as 100. Its mean is the same as the population mean, 2.6, and its standard deviation is the population standard deviation divided by the square root of the sample size: $\frac{\sigma}{\sqrt{n}}=\frac{1.4}{\sqrt{100}}=.14.$ The z-score for 3 is $\frac{3-2.6}{\frac{1.4}{\sqrt{100}}}=\frac{0.4}{0.14}=2.86$ The probability of the mean household size in a sample of 100 being more than 3 is therefore P($\bar{X}$ > 3) = P(Z > 2.86) = P(Z < -2.86) = .0021.

    Households of more than 3 people are, of course, quite common, but it would be extremely unusual for the mean size of a sample of 100 households to be more than 3.
```

The purpose of the next activity is to give guided practice in finding the sampling distribution of the sample mean ($\bar{X}$), and use it to learn about the likelihood of getting certain values of $\bar{X}$ .

## Learn By Doing

The annual salary of teachers in a certain state X has a mean of $54,000 and standard deviation of σ = $5,000.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

What is the probability that the mean annual salary of a random sample of 64 teachers from this state is less than $52,000?

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

Scores on the math portion of the SAT (SAT-M) in a recent year have followed a normal distribution with mean μ = 507 and standard deviation σ = 111.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
