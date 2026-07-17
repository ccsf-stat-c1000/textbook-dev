# Building a Probability Distribution from Scratch

```{admonition} Learning Objectives
:class: note

- Find the probability distribution of discrete random variables, and use it to find the probability of events of interest.
```

The probability distribution for two flips of a coin was simple enough to construct at once. For more complicated random experiments, it is common to first construct a table of all the outcomes in S and their probabilities, then use the addition principle to condense that information into the actual probability distribution table.

:::{admonition} Example: Flipping a Coin Three Times
:class: tip

A coin is tossed three times. Let the random variable X be the number of tails. Find the probability distribution of X. We'll follow the same reasoning we used in the previous example:

First, we specify the 8 possible outcomes in S, along with the probability of each outcome, and figure out the value of X (number of tails) for each. (Because they are all equally likely, each has probability 1/8. Alternatively, by the multiplication principle, each particular sequence of three coin faces has probability 1/2 × 1/2 × 1/2 = 1/8.)

| Outcome | Probability | X |
| --- | --- | --- |
| HHH | 1/8 | 0 |
| HHT | 1/8 | 1 |
| HTH | 1/8 | 1 |
| THH | 1/8 | 1 |
| HTT | 1/8 | 2 |
| THT | 1/8 | 2 |
| TTH | 1/8 | 2 |
| TTT | 1/8 | 3 |

Next, we use the addition principle to assert that

P(X = 1) = P(HHT or HTH or THH) = P(HHT) + P(HTH) + P(THH) = 1/8 + 1/8 + 1/8 = 3/8.

Similarly, P(X = 2) = P(HTT or THT or TTH) = 3/8.

The resulting probability distribution is:

| x | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| P(X = x) | 1/8 | 3/8 | 3/8 | 1/8 |
:::

The purpose of the next activity is to give you guided practice in finding the probability distribution of a discrete random variable.

## Learn By Doing

A young couple decides to try to have children until they have a boy. For financial reasons, the couple decides that they are going to stop trying when they have three children, whether they have a boy or not. (We are assuming that having a boy or a girl is equally likely, and that the child's gender in each birth is independent of the gender in the other births.)

Let the random variable X be the number of children the couple has.

Our goal is to find the probability distribution of X. In other words, we would like to create a table that lists all the possible values of X and the corresponding probabilities. We'll follow the same steps we followed in the two examples we solved.

:::{quiz} What are the possible outcomes of this "experiment," and their probabilities?
:hint: The couple stops at the first boy, or after three children. The possible sequences are B, GB, GGB, GGG.
:feedback-0: Correct! P(B) = 1/2; P(GB) = (1/2)(1/2) = 1/4; P(GGB) = 1/8; P(GGG) = 1/8.
:feedback-1: The couple stops after a boy, so sequences like BG or BB can't happen.
:feedback-2: The four outcomes are not equally likely—stopping early makes B much more likely than GGB.
* *B (1/2), GB (1/4), GGB (1/8), GGG (1/8)
* B, BG, BB, GG — each with probability 1/4
* B, GB, GGB, GGG — each with probability 1/4
:::

:::{quiz} What is P(X = 1), the probability that the couple has exactly one child?
:hint: Which outcome gives exactly one child?
:feedback-0: Correct! X = 1 only for the outcome B, so P(X = 1) = 1/2.
:feedback-1: 1/4 is the probability of GB, which gives two children.
:feedback-2: With four possible outcomes but unequal probabilities, don't use 1/4 per outcome.
* *1/2
* 1/4
* 1/8
:::

:::{quiz} What is P(X = 3), the probability that the couple has three children?
:hint: X = 3 happens for GGB or GGG.
:feedback-0: Correct! P(X = 3) = P(GGB) + P(GGG) = 1/8 + 1/8 = 1/4.
:feedback-1: 1/8 counts only one of the two outcomes with three children.
:feedback-2: Check: the probability of two girls first is 1/4, and then the third child's gender doesn't change the count of children.
* *1/4
* 1/8
* 1/2
:::

So the probability distribution of X is:

| x | 1 | 2 | 3 |
| --- | --- | --- | --- |
| P(X = x) | 1/2 | 1/4 | 1/4 |

(Check: 1/2 + 1/4 + 1/4 = 1. ✓)
