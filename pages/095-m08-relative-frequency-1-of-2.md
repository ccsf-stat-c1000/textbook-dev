# Relative Frequency (1 of 2)

```{admonition} Learning Objectives
:class: note

- Explain how relative frequency can be used to estimate the probability of an event.
```

If we toss a coin, roll a die, or spin a spinner many times, we hardly ever achieve the exact *theoretical* probabilities that we know we should get, but we can get pretty close. When we run a simulation or when we use a random sample and record the results, we are using *empirical* probability. This is often called the *Relative Frequency* definition of probability.

Here is a realistic example where the relative frequency method was used to find the probabilities:

:::{admonition} Example: Blood Type
:class: tip

Researchers discovered at the beginning of the 20th century that human blood comes in various types (A, B, AB, and O), and that some types are more common than others. How could researchers determine the probability of a particular blood type, say O? Just looking at one or two or a handful of people would not be very helpful in determining the overall chance that a randomly chosen person would have blood type O. But sampling many people at random, and finding the relative frequency of blood type O occurring, provides an adequate estimate. For example, it is now well known that the probability of blood type O among white people in the United States is 0.45. This was found by sampling many (say, 100,000) white people in the country, finding that roughly 45,000 of them had blood type O, and then using the relative frequency: 45,000 / 100,000 = 0.45 as the estimate for the probability for the event *"having blood type O."*

(Comment: Note that there are racial and ethnic differences in the probabilities of blood types. For example, the probability of blood type O among black people in the United States is 0.49, and the probability that a randomly chosen Japanese person has blood type O is only 0.3.)
:::

Let's review the relative frequency method for finding probabilities:

To estimate the probability of event A, written P(A), we may repeat the random experiment many times and count the number of times event A occurs. Then P(A) is estimated by the ratio of the number of times A occurs to the number of repetitions, which is called the *relative frequency of event A*.

$$\text{Relative frequency of event A} = \frac{\text{number of times A occurred}}{\text{total number of repetitions}}$$

## Did I Get This?

What are the breakfast-eating habits of college students?

A group of 460 college students was surveyed over several typical weekdays, and 253 of them reported that they had eaten breakfast that day. Let B be the event of interest—that a college student eats breakfast.

:::{quiz} Based on this survey, what is the estimate of P(B), the probability that a college student eats breakfast?
:hint: Use the relative frequency: the number who ate breakfast divided by the total surveyed.
:feedback-0: Correct! P(B) ≈ 253/460 = 0.55.
:feedback-1: 0.45 is the proportion who did NOT eat breakfast (207/460).
:feedback-2: 253 is the count of breakfast-eaters; divide by the total, 460, to get a probability.
* *About 0.55
* About 0.45
* 253
:::

:::{quiz} Why is 253/460 only an estimate of P(B), rather than its exact value?
:hint: What would happen if a different group of 460 students were surveyed?
:feedback-0: Correct! The relative frequency comes from one particular sample; a different random sample would give a somewhat different proportion. The estimate improves as the number of observations grows.
:feedback-1: The arithmetic is exact; the uncertainty comes from sampling, not from rounding.
:feedback-2: Empirical estimates are legitimate probabilities—in fact, for events like this, they are the only way to estimate the probability.
* *The relative frequency varies from sample to sample; a larger sample would give a more precise estimate
* The division was rounded incorrectly
* Relative frequencies can never be used as probabilities
:::
