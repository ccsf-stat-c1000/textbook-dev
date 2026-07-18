# The Continuity Correction

```{admonition} Learning Objectives
:class: note

- Use the normal distribution as an approximation of the binomial distribution, when appropriate.
```

Actually, there is another important reason why the binomial approximation example from the middle of the previous page is not too good. The following comment will explain.

## Making the Continuity Correction

It is possible to improve the normal approximation to the binomial by adjusting for the discrepancy that arises when we make the shift from the areas of histogram rectangles to the area under a smooth curve. For example, if we want to find the binomial probability that X is less than *or equal to* 8, we are including the area of the entire rectangle over 8, which actually extends to 8.5. Our normal approximation only included the area up to 8. The figure below illustrates this:

```{figure} images/gen/m11-continuity-correction.svg
:alt: The binomial histogram with its normal curve overlay. The bars for 0 through 8 are shaded orange, and a dashed red line marks 8.5, the right edge of the bar over 8. Approximating the orange area with the area under the curve up to 8 misses the right half of that bar, so the corrected approximation uses the area up to 8.5.
```

It can be improved upon by making the *continuity correction*. In this case, we would have

$$P(X_{B}\leq8) \approx P(X_{N}\leq8.5)=P\left(Z\leq\frac{8.5-10}{2.24}\right)=P(Z\leq-0.67)=0.2514$$

which is much closer to the actual binomial probability of 0.2517 than our original approximation (0.1867) was.

Similarly, suppose we wanted to answer: What is the probability that the student gets at least 13 questions right?

Here, to calculate the exact probability we are including the area of the entire rectangle over 13, which actually starts from 12.5. Our normal approximation would only include the area from 13. The continuity correction in this case would be:

$$P(X_{B}\geq13) \approx P(X_{N}\geq12.5)=P\left(Z\geq\frac{12.5-10}{2.24}\right)=P(Z\geq1.12)=P(Z\leq-1.12)=0.1314$$

It turns out that the exact probability in this case (using software) is 0.1316, so the approximation is excellent.

The purpose of the next activity is to give you guided practice in solving word problems involving a binomial random variable, when the normal approximation is appropriate and is extremely helpful.

## Check Your Understanding: Applying the Continuity Correction

Roughly 10% of all college students in the United States are left-handed. Most academic institutions, therefore, try to have at least a few left-handed chairs in each classroom. 225 students are about to enter a lecture hall that has 30 left-handed chairs for a lecture. What is the probability that this is not going to be enough; in other words, what is the probability that more than 30 (or at least 31) of the 225 students are left-handed?

Let's think about this situation.

Let X be the number of left-handed students (success) out of the 225 students (trials). X is therefore binomial with n = 225 and p = 0.1. We are asked to find P(X > 30) or P(X ≥ 31).

Clearly, doing this using the binomial distribution formula is out of the question.

:::{quiz} Is the normal approximation appropriate here, and if so, what are the mean and standard deviation of the approximating normal variable?
:hint: Check np and n(1 − p), then compute μ = np and σ = √(np(1 − p)).
:feedback-0: Correct! np = 22.5 and n(1 − p) = 202.5 both exceed 10, so the approximation applies with μ = 22.5 and σ = √20.25 = 4.5.
:feedback-1: np = 225 × 0.1 = 22.5, which does satisfy the rule of thumb.
:feedback-2: The standard deviation is √(np(1−p)) = √20.25 = 4.5, not 20.25 (that's the variance).
* *Yes; μ = 22.5 and σ = 4.5
* No; np is less than 10
* Yes; μ = 22.5 and σ = 20.25
:::

:::{quiz} Using the normal approximation with continuity correction, what is P(X ≥ 31), the probability of running out of left-handed chairs?
:hint: With the correction, use P(X ≥ 30.5): z = (30.5 − 22.5)/4.5 ≈ 1.78.
:feedback-0: Correct! P(Z ≥ 1.78) = P(Z ≤ −1.78) = 0.0375—about a 4% chance the 30 chairs won't be enough.
:feedback-1: 0.9625 is the probability that the chairs WILL be enough.
:feedback-2: Standardize first: (30.5 − 22.5)/4.5 = 1.78; then find the tail probability from the table.
* *About 0.04
* About 0.96
* 1.78
:::
