# The Normal Approximation and When to Use It

Consider the appearance of the probability histogram for the distribution of X:

```{figure} images/gen/m11-binomial-normal-overlay.svg
:alt: The probability histogram of a binomial random variable with n equal to 20 and p equal to 0.5, symmetric and peaked at 10, with a red normal curve drawn on top. The histogram closely follows the bell shape of the normal curve.
```

Clearly, the shape of the distribution of X for $n = 20$, $p = 0.5$ has a normal appearance: symmetric, bulging at the middle, and tapering at the ends.

This suggests a method of approximating binomial probabilities:

Estimate the binomial probability of $X_{B}$ taking a value over a certain interval with the probability that a normal random variable $X_{N}$ takes a value over the same interval, where $X_{N}$ has the same mean and standard deviation as $X_{B}$, namely $\mu=np, \sigma=\sqrt{np(1-p)}$.

:::{admonition} Example: True/False Questions (continued)
:class: tip

Suppose a student answers 20 true/false questions completely at random. Use a normal approximation to estimate the probability of getting no more than 8 correct. The number (X) correct is a binomial random variable that represents the number of successes in 20 trials when the probability of success for each trial is 0.5. X has a mean and standard deviation of:

$$\mu=np=20(0.5)=10, \qquad \sigma=\sqrt{np(1-p)}=\sqrt{20(0.5)(0.5)}=2.24$$

and so we approximate the binomial X with a normal random variable having the same mean and standard deviation. Then we solve in the usual way using normal tables:

$$P(X_{B}\leq8) \approx P(X_{N}\leq8)=P\left(Z\leq\frac{8-10}{2.24}\right)=P(Z\leq-0.89)=0.1867$$
:::

Unfortunately, the approximated probability, 0.1867, is quite a bit different from the actual probability, 0.2517. However, this example constitutes something of a "worst-case scenario" according to the usual criteria for use of a normal approximation.

## Rule of Thumb

Probabilities for a binomial random variable X with n and p may be approximated by those for a normal random variable having the same mean and standard deviation as long as the sample size n is large enough relative to the proportions of successes and failures, p and $1 - p$. Our Rule of Thumb will be to require that

$$np\geq10 \quad \text{and} \quad n(1-p)\geq10$$

:::{admonition} Example: Checking the Rule of Thumb
:class: tip

May we use a normal approximation for a binomial X with $n = 20$ and $p = 0.5$? In this case, np = $20(0.5) = 10$ and n(1 - p) = $20(0.5) = 10$. The criteria are just barely satisfied, and so we should not expect the approximation to be especially good.
:::

The purpose of the next activity is to give you practice at deciding whether the normal approximation is appropriate for a given binomial random variable.

## Check Your Understanding: When to Use the Normal Approximation

:::{quiz} Is the normal approximation appropriate for a binomial random variable with $n = 100$ and $p = 0.05$?
:hint: Check np and n(1 - p) against 10.
:feedback-0: np = $100(0.05) = 5$, which is less than 10—the rule of thumb fails.
:feedback-1: Correct! np = $5 < 10$, so the approximation is not appropriate; the distribution is still too skewed right.
:feedback-2: n(1 - p) = 95 is fine, but BOTH conditions must hold, and np = 5 fails.
* Yes—both conditions hold
* *No—np = 5 is less than 10
* No—n(1 - p) is less than 10
:::

:::{quiz} Is the normal approximation appropriate for a binomial random variable with $n = 400$ and $p = 0.1$?
:hint: np = 40 and n(1 - p) = 360.
:feedback-0: Correct! np = $40 \geq 10$ and n(1 - p) = $360 \geq 10$, so the approximation is appropriate.
:feedback-1: Check the arithmetic: np = $400(0.1) = 40$, which satisfies the condition.
* *Yes—np = 40 and n(1 - p) = 360 both exceed 10
* No—p = 0.1 is too small for any n
:::
