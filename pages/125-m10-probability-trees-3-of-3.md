# Reversing the Condition: Bayes-Style Problems with Trees

```{admonition} Learning Objectives
:class: note

- Use probability trees as a tool for finding probabilities.
```

Here is a more practical example:

:::{admonition} Example: Polygraph Tests
:class: tip

Polygraph (lie-detector) tests are often routinely administered to employees or prospective employees in sensitive positions. A National Research Council study in 2002 found that lie detector results are "better than chance, but well below perfection." Typically, the test may conclude someone is a spy 80% of the time when he or she actually is a spy, but 16% of the time the test will conclude someone is a spy when he or she is not.

Let us assume that 1 in 1,000, or 0.001, of the employees in a certain highly classified workplace are actual spies.

Let *S* be the event of being a spy, and *D* be the event of the polygraph detecting the employee to be a spy.

Let's first express the information using probability notation involving events S and D. We are given:

- 1 in 1,000, or 0.001, of the employees are actual spies → *P(S) = 0.001*
- The test may conclude someone is a spy 80% of the time when he or she actually is a spy → *P(D | S) = 0.80*
- 16% of the time, the test will conclude someone is a spy when he or she is not → *P(D | not S) = 0.16*

(a) Let's create a tree diagram for this problem, starting, as usual, with the event for which a nonconditional probability is given, S. It also makes sense that we start with S, since the natural order is that first a person becomes a spy, and then he/she is either detected or not.

```{figure} images/gen/m10-tree-spy.svg
:alt: A probability tree. The first branches are S with probability 0.001 and not S with probability 0.999. From S, the branches are D given S with probability 0.80 and not D given S with probability 0.20. From not S, the branches are D given not S with probability 0.16 and not D given not S with probability 0.84. The leaves show the joint probabilities 0.0008, 0.0002, 0.15984, and 0.83916. The probabilities given in the problem are marked in red, and the rest are completed with the Complement Rule.
```

(b) What is the probability that a randomly chosen employee is not a spy, and the test does not detect the employee as one? In other words, what is P(not S and not D)?

Following the bottom path of the tree: P(not S and not D) = P(not S) × P(not D | not S) = 0.999 × 0.84 = 0.83916

(c) What is the probability that a randomly chosen employee *is* a spy, and the test does *not* detect the employee as one? (This would be an incorrect conclusion.) In other words, what is P(S and not D)?

Following the S-then-not-D path: P(S and not D) = P(S) × P(not D | S) = 0.001 × 0.20 = 0.0002

(d) Suppose the polygraph detects a spy; are you convinced that the employee is actually a spy? Find the probability of an employee actually being a spy, given that the test claims he or she is. In other words, find P(S | D).

Applying Bayes' Rule, we have

P(S | D) = P(S) × P(D | S) / [P(S) × P(D | S) + P(not S) × P(D | not S)]

= 0.001 × 0.80 / [0.001 × 0.80 + 0.999 × 0.16] = 0.0008/0.16064 = 0.005

The study's conclusion, that more accurate tests than the traditional polygraph are sorely needed, is supported by our answer to part (d): if someone is detected as being a spy, the probability is only 0.005, or half of one percent, that he or she actually is one.
:::

## Comment

This example helps to highlight how different P(B | A) may be from P(A | B): the probability of being detected, given that an employee is a spy, is P(D | S) = 0.80. In contrast, the probability of being a spy, given that an employee has been detected by the polygraph, is P(S | D) = 0.005.

The purpose of the next activity is to give you guided practice in using the information displayed in probability trees in order to answer real-life problems.

## Learn By Doing

Let's consider the engine overheating example again, where H is the event that the engine overheats and W is the event that a warning light turns on. We are given that:

- P(H) = 0.03
- P(W | H) = 0.98
- P(W | not H) = 0.01

and in a previous activity we displayed the information using a probability tree:

```{figure} images/gen/m10-tree-engine.svg
:alt: A probability tree for the engine example. The first branches are H with probability 0.03 and not H with probability 0.97. From H, W given H has probability 0.98 and not W given H has probability 0.02. From not H, W given not H has probability 0.01 and not W given not H has probability 0.99. The leaves show the joint probabilities 0.0294, 0.0006, 0.0097, and 0.9603.
```

:::{quiz} What is the overall probability that the warning light comes on, P(W)?
:hint: Add the two paths that end with W: P(H and W) + P(not H and W).
:feedback-0: Correct! P(W) = 0.0294 + 0.0097 = 0.0391.
:feedback-1: 0.0294 is only the path where the engine actually overheats; add the false-alarm path too.
:feedback-2: 0.98 is P(W | H), the conditional probability, not the overall probability.
* *0.0391
* 0.0294
* 0.98
:::

:::{quiz} The warning light just came on. What is the probability that the engine is really overheating, P(H | W)?
:hint: Bayes' Rule: P(H | W) = P(H and W) / P(W).
:feedback-0: Correct! P(H | W) = 0.0294 / 0.0391 ≈ 0.75. So when the light comes on, there's about a 75% chance of a real problem.
:feedback-1: 0.98 is the reverse conditional, P(W | H). The question conditions on the light being on.
:feedback-2: 0.03 is the unconditional P(H), before seeing the light. The light substantially raises the probability.
* *About 0.75
* 0.98
* 0.03
:::

## Let's Summarize

- The *conditional probability* of B given A, P(B | A) = P(A and B)/P(A), assesses the probability of B in the reduced sample space where A has occurred.
- Two events are *independent* when knowing one occurred does not change the probability of the other (four equivalent checks are available).
- The *General Multiplication Rule*, P(A and B) = P(A) × P(B | A), finds "and" probabilities for any two events, and reduces to the familiar product rule when the events are independent.
- *Probability trees* organize staged problems: multiply along branches for "and," add across paths for "or," and combine the two (Bayes' Rule) to reverse the direction of conditioning.
