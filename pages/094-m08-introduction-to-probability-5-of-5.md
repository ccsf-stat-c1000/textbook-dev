# Introduction to Probability (5 of 5)

```{admonition} Learning Objectives
:class: note

- Relate the probability of an event to the likelihood of this event occurring.
```

We will now shift our discussion to empirical ways to determine probabilities.

## A Question

A single flip of a coin has an uncertain outcome. So, every time a coin is flipped, the outcome of that flip is unknown until the flip occurs.

*However, if you flip a fair coin over and over again, would you expect P(H) to be exactly 0.5?* In other words, would you expect there to be the same number of results of "heads" as there are "tails"?

In any *particular* series of flips, the proportion of heads will usually not be exactly 0.5—in 10 flips you might easily see 7 heads. But something remarkable happens as the number of flips grows. The figure below shows the running proportion of heads in one series of 1,000 flips of a fair coin:

```{figure} images/gen/m08-coin-convergence.svg
:alt: A line chart of the proportion of heads against the number of coin flips, from 0 to 1,000. The line starts far from 0.5, swinging as high as 0.7 in the early flips, then oscillates less and less and settles very close to the dashed line at 0.5 as the number of flips grows.
```

In the short run the proportion bounces around, but in the long run it settles down toward 0.5. This is the empirical way of seeing that P(H) = 0.5: the probability of an event is the *relative frequency* with which the event occurs in a long series of repetitions. (This long-run behavior is known as the *law of large numbers*.)

## A Second Question

After seeing this, an important question naturally comes to mind. *How would we know if the coin was not fair?* Certainly, classical probability methods would never be able to answer this question. In addition, classical methods could never tell us the actual P(H). The only way to answer this question is to perform an experiment: flip the coin many, many times and watch where the proportion of heads settles. If, after thousands of flips, the proportion of heads settles near 0.6 rather than 0.5, we have empirical evidence that the coin is not fair—and 0.6 is our empirical estimate of P(H).

So, these types of experiments can verify classical probabilities and they can also determine when games of chance are not following *fair* practices. However, their real importance is to answer probability questions that arise when we are faced with a situation that does not follow any pattern and cannot be predetermined. In reality, most of the probabilities of interest to us fit the latter description.

## Concept Check

:::{quiz} A fair coin is flipped 10 times and comes up heads 7 times. Does this contradict P(H) = 0.5?
:hint: Probability describes long-run behavior, not short-run results.
:feedback-0: Correct! Short series of flips vary a lot; P(H) = 0.5 describes the long-run proportion over many, many flips.
:feedback-1: 7 heads in 10 flips is quite common for a fair coin—it is not strong evidence of unfairness.
:feedback-2: The probability doesn't change from flip to flip; each flip of a fair coin has P(H) = 0.5.
* *No—probability describes the long-run relative frequency, and short runs vary
* Yes—the coin must be biased toward heads
* Yes—P(H) has now changed to 0.7
:::

:::{quiz} A basketball player wants to estimate the probability that she makes a free throw. Which method must she use?
:hint: Is there a "game" whose symmetry determines this probability in advance?
:feedback-0: Classical methods only work when the setup itself determines equally likely outcomes, like a fair die.
:feedback-1: Correct! Free-throw success follows no predetermined pattern, so she must estimate the probability empirically—by shooting many free throws and using the relative frequency of makes.
:feedback-2: Intuition may give a rough guess, but a reliable estimate requires observed relative frequency.
* Classical (theoretical) methods
* *Empirical methods—use the relative frequency over many attempts
* No method exists for such probabilities
:::

## To Summarize

1. Probability is a way of quantifying uncertainty.
2. We are interested in the probability of an event—the likelihood of the event occurring.
3. The probability of an event ranges from 0 to 1. The closer the probability is to 0, the less likely the event is to occur. The closer the probability is to 1, the more likely the event is to occur.
4. There are two ways to determine probability: Theoretical (Classical) and Empirical (Observational).
5. Theoretical methods use the nature of the situation to determine probabilities.
6. Empirical methods use a series of trials that produce outcomes that cannot be predicted in advance (hence the uncertainty).
