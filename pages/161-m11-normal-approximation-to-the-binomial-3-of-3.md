# Normal Approximation to the Binomial (3 of 3)

```{admonition} Learning Objectives
    - Use the normal distribution as an approximation of the binomial distribution, when appropriate.
```

Actually, there is another important reason why the binomial approximation example from the middle of the previous page is not too good. The following comment will explain.

## Comment

It is possible to improve the normal approximation to the binomial by adjusting for the discrepancy that arises when we make the shift from the areas of histogram rectangles to the area under a smooth curve. For example, if we want to find the binomial probability that X is less than *or equal to* 8, we are including the area of the entire rectangle over 8, which actually extends to 8.5. Our normal approximation only included the area up to 8. The figure below illustrates this:

```{figure} images/image186.gif
:alt: The probability histogram with a normal distribution curve drawn over it. The vertical axis is labeled "Probability" and horizontal axis is for X. The histogram and curve are the same as the previously shown ones, with a mean of 10 and standard deviation of 2.24 . Since the histogram uses bars, there is a bar which is centered over X=8 . It has a width of 1, so the bar's boundaries are actually 7.5 and 8.5. Thus, in order to calculate P(X ≤ 8), we get the area of all the bars for X=0 to X=8. This means for X=8, we are getting the area of the bar which is P(X = 8) high and 1 wide. In contrast, for the curve, we get the area under the curve to the left of X = 8. This means we do not capture the area in the bar for X=8 from X=8 to X=8.5, since that half of the bar is outside of the normal curve's approximated area.

The probability histogram with a normal distribution curve drawn over it. The vertical axis is labeled "Probability" and horizontal axis is for X. The histogram and curve are the same as the previously shown ones, with a mean of 10 and standard deviation of 2.24 . Since the histogram uses bars, there is a bar which is centered over X=8 . It has a width of 1, so the bar's boundaries are actually 7.5 and 8.5. Thus, in order to calculate P(X ≤ 8), we get the area of all the bars for X=0 to X=8. This means for X=8, we are getting the area of the bar which is P(X = 8) high and 1 wide. In contrast, for the curve, we get the area under the curve to the left of X = 8. This means we do not capture the area in the bar for X=8 from X=8 to X=8.5, since that half of the bar is outside of the normal curve's approximated area.
```

It can be improved upon by making the *continuity correction:*

in this case, we would have

$P(X_{B}\leq8)\approxP(X_{N}\leq8.5)=P(Z\leq\frac{8.5-10}{2.24})=P(Z\leq-0.67)=0.2514$, which is much closer to the actual binomial probability of .2517 than our original approximation (.1867) was.

Similarly, suppose I wanted to answer: What is the probability that the student gets at least 13 questions right?

```{figure} images/image188.gif
:alt: The same histogram as above, but in this case we are trying to find P(X ≥ 13). So, the curve has shaded in the area to the right of X=13. The histogram has shaded in the bars for X=13 through X=20. The approximation that the curve provides does not cover the left half of the bar for X=13, because the bar for X=13 starts at X=12.5 and ends at X=13.5, so it misses X=12.5 thourgh X=13 . This missing area makes the approximation worse.

The same histogram as above, but in this case we are trying to find P(X ≥ 13). So, the curve has shaded in the area to the right of X=13. The histogram has shaded in the bars for X=13 through X=20. The approximation that the curve provides does not cover the left half of the bar for X=13, because the bar for X=13 starts at X=12.5 and ends at X=13.5, so it misses X=12.5 thourgh X=13 . This missing area makes the approximation worse.
```

Here, to calculate the exact probability we are including the area of the entire rectangle over 13, which actually starts from 12.5. Our normal approximation only included the area from 13. The continuity correction in this case would be:

$P(X_{B}\geq13)\approxP(X_{N}\geq12.5)=P(Z\geq\frac{12.5-10}{2.24})=P(Z\geq1.12)=(symmetry)=P(Z\leq-1.12)=(table)=0.1314$

It turns out that the exact probability in this case (using software) is .1316, so the approximation is excellent.

The purpose of the next activity is to give you guided practice in solving word problems involving a binomial random variable, when the normal approximation is appropriate and is extremely helpful.

##### Learn By Doing

Roughly 10% of all college students in the United States are left-handed. Most academic institutions, therefore, try to have at least a few left-handed chairs in each classroom. 225 students are about to enter a lecture hall that has 30 left-handed chairs for a lecture. What is the probability that this is not going to be enough; in other words, what is the probability that more than 30 (or at least 31) of the 225 students are left-handed?

Let's think about this situation.

Let X be the number of left-handed students (success) out of the 225 students (trials). X is therefore binomial with n = 225 and p = .1. We are asked to find P(X > 30) or P(X ≥ 31).

Clearly, doing this using the binomial distribution is out of the question.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
