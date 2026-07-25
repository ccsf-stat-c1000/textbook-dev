# Probability Trees: Mapping Multi-Stage Problems

So far, when two categorical variables are involved, we have displayed counts or probabilities for various events with two-way tables and with Venn diagrams. Another display tool, called a *probability tree*, is particularly useful for showing probabilities when the events occur in stages and conditional probabilities are involved.

:::{admonition} Example: Commission and Vacation
:class: tip

A sales representative tells his friend that the probability of landing a major contract by the end of the week, resulting in a large commission, is 0.4. If the commission comes through, the probability that he will indulge in a weekend vacation in Bermuda is 0.9. Even if the commission doesn't come through, he may still go to Bermuda, but only with probability 0.3.

First, let's identify the given probabilities for events involving *C* (the commission comes through) and *V* (the sales rep takes a Bermuda vacation):

- P(C) = 0.4 [and so P(not C) = 0.6],
- P(V | C) = 0.9 [and so P(not V | C) = 0.1], and
- P(V | not C) = 0.3 [and so P(not V | not C) = 0.7.]

There are two stages in the problem. First, the sales rep will either get the commission or not. Second, based on what happened in the first stage, the sales rep will either take the Bermuda vacation or not.

We follow exactly the same reasoning when we build the probability tree.
:::

```{note} Video

[Probability Trees](https://www.youtube.com/watch?v=PVQszIj-X_A)
```

Here is the completed tree:

```{figure} images/gen/m10-tree-commission.svg
:alt: A probability tree. From the starting point, two branches represent getting the commission, C with probability 0.4, and not C with probability 0.6. From each of these, two more branches represent taking the vacation or not: V given C is 0.9, not V given C is 0.1, V given not C is 0.3, and not V given not C is 0.7. The four leaves show the joint probabilities: P(C and V) equals 0.36, P(C and not V) equals 0.04, P(not C and V) equals 0.18, and P(not C and not V) equals 0.42.
```

There are two important things to note here:

1. The probabilities in the *first branch-off are non-conditional probabilities*: P(C) = 0.4, P(not C) = 0.6. However, the probabilities that appear in the *second branch-off are conditional probabilities.* The top two branches assume that C occurred: P(V | C) = 0.9, P(not V | C) = 0.1. The bottom two branches assume that not C occurred: P(V | not C) = 0.3, P(not V | not C) = 0.7.

2. The second thing to note is that probabilities of branches that branch out from the same point always add up to one: $0.4 + 0.6 = 1$ at the first stage, and $0.9 + 0.1 = 1$ and $0.3 + 0.7 = 1$ at the second stage.

## Check Your Understanding: Reading a Probability Tree

:::{quiz} In a probability tree for a two-stage problem, what kind of probabilities appear on the second set of branches?
:hint: The second stage happens after (and depends on) the first stage's outcome.
:feedback-0: The non-conditional probabilities appear only on the first branch-off.
:feedback-1: Correct! Second-stage branches carry conditional probabilities, given the outcome of the first stage.
:feedback-2: Joint probabilities appear at the ends of the tree (the leaves), computed by multiplying along a path.
* Non-conditional probabilities
* *Conditional probabilities, given the first-stage outcome
* Joint probabilities of both events
:::

:::{quiz} A tree's first stage has branches with probabilities 0.25 and p. What must p be?
:hint: Branches from the same point sum to 1.
:feedback-0: Correct! Branches from the same point always add up to 1, so $p = 1 - 0.25 = 0.75$.
:feedback-1: 0.25 would make the branch probabilities sum to 0.5, not 1.
:feedback-2: The complement of 0.25 is 0.75.
* *0.75
* 0.25
* 0.5
:::
