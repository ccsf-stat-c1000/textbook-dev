# Why Approximate the Binomial with a Normal?

```{admonition} Learning Objectives
:class: note

- Use the normal distribution as an approximation of the binomial distribution, when appropriate.
```

## Application of Normal Random Variables: Approximation to Binomial

One of the important applications of the normal distribution is that under certain conditions it can provide a very good approximation to the binomial distribution. We've seen before that sometimes calculating binomial probabilities can be quite tedious, and the solution we suggested before is to use statistical software to do the work for you.

In the absence of statistical software, another solution would be to use the normal approximation (when appropriate). Normal calculations never get too complicated; all we have to do is use a table correctly.

Let's start with a motivating example.

:::{admonition} Example: True/False Questions
:class: tip

Suppose a student answers 20 true/false questions completely at random. What is the probability of getting no more than 8 correct? Let X be the number of questions the student gets right (successes) out of the 20 questions (trials), when the probability of success is 0.5. X is therefore a binomial random variable with n = 20 and p = 0.5, and we are looking for

$$P(X\leq8)=P(X=0)+P(X=1)+\cdots+P(X=8)$$

Doing this by hand using the binomial distribution formula is very tedious, and requires us to do 9 complex calculations, as shown below:

$$\frac{20!}{0!20!}0.5^{0}(0.5)^{20}+\frac{20!}{1!19!}0.5^{1}(0.5)^{19}+\cdots+\frac{20!}{8!12!}0.5^{8}(0.5)^{12}$$

One option that we have is to use statistical software, which will provide the answer:

| x | P(X ≤ x) |
| --- | --- |
| 8 | *0.2517* |
:::

Are there any alternatives, if software is not handy?

Yes! The properties of normal distributions can come to our rescue.
