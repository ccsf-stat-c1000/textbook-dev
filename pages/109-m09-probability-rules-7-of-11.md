# Extending the Rules: More Than Two Events

```{admonition} Learning Objectives
:class: note

- Apply probability rules in order to find the likelihood of an event.
```

As you've seen, the last three rules that we've introduced (the Complement Rule, the Addition Rule for Disjoint Events, and the Multiplication Rule for Independent Events) are frequently used in solving problems. Before we move on to our next rule, here are two comments that will help you use these rules in broader types of problems and more effectively.

```{admonition} Comment
:class: important

As we mentioned before, the Addition Rule can be extended to more than two disjoint events. Likewise, the Multiplication Rule can be extended to more than two independent events. So if A, B and C are three independent events, for example, then P(A and B and C) = P(A) × P(B) × P(C). These extensions are quite straightforward, as long as you remember that "or" requires us to add, while "and" requires us to multiply.

An example of a situation where more than two independent events naturally occur is when a random sample of more than two individuals is chosen from a large population.
```

Here is an example:

:::{admonition} Example: Three Type B Donors
:class: tip

Three people are chosen at random from a large population. What is the probability that all three have blood type B? We'll use the usual notation of B1, B2 and B3 for the events that persons 1, 2 and 3 have blood type B, respectively. We need to find P(B1 and B2 and B3). Try it yourself:
:::

:::{quiz} What is P(B1 and B2 and B3), given that P(B) = 0.10 for a randomly chosen person?
:hint: The three choices from a large population are independent; multiply the three probabilities.
:feedback-0: Correct! P(B1 and B2 and B3) = 0.10 × 0.10 × 0.10 = 0.001.
:feedback-1: 0.30 is the sum—but "and" requires multiplication for independent events.
:feedback-2: 0.01 is 0.10 × 0.10, the probability for two people; here there are three.
* *0.001
* 0.30
* 0.01
:::

Here is another example that might be quite surprising.

:::{admonition} Example: Ten Coin Tosses
:class: tip

A fair coin is tossed 10 times. Which of the following two outcomes is more likely?

(a) HHHHHHHHHH

(b) HTTHHTHTTH

Most people feel that (b) "looks more random" and must therefore be more likely. In fact, they are equally likely. The 10 tosses are independent, so we'll use the Multiplication Rule for Independent Events:

P(HHHHHHHHHH) = P(H) × P(H) × ... × P(H) = 1/2 × 1/2 × ... × 1/2 = (1/2)¹⁰

P(HTTHHTHTTH) = P(H) × P(T) × ... × P(H) = 1/2 × 1/2 × ... × 1/2 = (1/2)¹⁰

Here is the idea:

Our random experiment here is tossing a coin 10 times. You can imagine how huge the sample space is. There are actually 1,024 possible outcomes to this experiment, all of which are equally likely. Therefore, while it is true that it is more likely to get an outcome that has 5 heads and 5 tails than an outcome that has only heads (since there is only one possible outcome of the latter kind, and many possible outcomes of the former), if we are comparing 2 *specific outcomes* as we do here, they are equally likely.
:::

## Concept Check

:::{quiz} A slot machine pays off with probability 0.05 on each independent play. A gambler plays 3 times. What is the probability of winning all 3 plays?
:hint: Multiply the three independent probabilities.
:feedback-0: Correct! 0.05 × 0.05 × 0.05 = 0.000125.
:feedback-1: 0.15 is the sum of the probabilities, which is not how "and" works for independent events.
:feedback-2: 0.0025 is the probability of winning two plays in a row; there are three plays here.
* *0.000125
* 0.15
* 0.0025
:::

:::{quiz} A lottery player has played the same "lucky numbers" for years without winning, and reasons that these numbers are now "due" to win. What does probability theory say?
:hint: Are successive lottery drawings independent?
:feedback-0: Correct! Drawings are independent—past losses have no effect on the probability of future drawings, so no combination is ever "due."
:feedback-1: Past outcomes do not change the probabilities of independent future outcomes.
:feedback-2: All number combinations remain equally likely in every drawing.
* *Each drawing is independent, so the numbers are never "due" to win
* The numbers really are more likely to win after many losses
* The numbers are now less likely to win, so the player should switch
:::
