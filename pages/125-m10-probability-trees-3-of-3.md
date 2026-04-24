# Probability Trees (3 of 3)

```{admonition} Learning Objectives
    - Use probability trees as a tool for finding probabilities.
```

Here is a more practical example:

```{admonition} Example
    Polygraph (lie-detector) tests are often routinely administered to employees or prospective employees in sensitive positions. A National Research Council study in 2002, headed by Stephen Fienberg from CMU, found that lie detector results are "better than chance, but well below perfection." Typically, the test may conclude someone is a spy 80% of the time when he or she actually is a spy, but 16% of the time the test will conclude someone is a spy when he or she is not.

    Let us assume that 1 in 1,000, or .001, of the employees in a certain highly classified workplace are actual spies.

    Let *S* be the event of being a spy, and *D* be the event of the polygraph detecting the employee to be a spy.

    Let's first express the information using probability notations involving events S and D.

    We are given:

    - 1 in 1,000, or 0.001, of the employees are actual spies → *P(S) = 0.001*
    - The test may conclude someone is a spy 80% of the time when he or she actually is a spy → *P(D | S) = 0.80*
    - 16% of the time, the test will conclude someone is a spy when he or she is not → *P(D | not S) = 0.16*

    (a) Let's create a tree diagram for this problem, starting, as usual, with the event for which a nonconditional probability is given, S. It also makes sense that we start with S, since the natural order is that first a person becomes a spy, and then he/she is either detected or not.

    Note that marked in red are the probabilities that are given, and the rest are completed using the Complement Rule as explained earlier.

    ```{figure} images/image014.gif
    :alt: A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Here is the tree: {S: 0.001 (red), D: 0.80 (red)}; {S: 0.001 (red), not D: 0.20}; {not S: 0.999, D: 0.16 (red)}; {not S: 0.999, not D: 0.84};

    A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Here is the tree: {S: 0.001 (red), D: 0.80 (red)}; {S: 0.001 (red), not D: 0.20}; {not S: 0.999, D: 0.16 (red)}; {not S: 0.999, not D: 0.84};
    ```

    (b) What is the probability that a randomly chosen employee is not a spy, and the test does not detect the employee as one? In other words, what is P(not S and not D)?

    ```{figure} images/image015.gif
    :alt: In the probability tree we take the path {not S: 0.999, not D: 0.84}.

    In the probability tree we take the path {not S: 0.999, not D: 0.84}.
    ```

    P(not S and not D) = P(not S) * P(not D | not S) = 0.999 * 0.84 = 0.83916

    (c) What is the probability that a randomly chosen employee *is* a spy, and the test does *not* detect the employee as one? (This would be an incorrect conclusion.) In other words, what is P(S and not D)?

    ```{figure} images/image016.gif
    :alt: In the probability tree we take the path {S: 0.001, not D: 0.20}.

    In the probability tree we take the path {S: 0.001, not D: 0.20}.
    ```

    P(S and not D) = P(S) * P(not D | S) = 0.001 * 0.20 = 0.0002

    (d) Suppose the polygraph detects a spy; are you convinced that the employee is actually a spy? Find the probability of an employee actually being a spy, given that the test claims he or she is. In other words, find P(S | D).

    Applying Bayes Rule, we have

    P(S | D) = P(S) * P(D | S) / [P(S) * P(D | S) + P(not S) * P(D | not S)]

    = 0.001 * 0.80/[0.001 * 0.80 + 0.999 * 0.16] = 0.0008/0.16064 = 0.005

    The study's conclusion, that more accurate tests than the traditional polygraph are sorely needed, is supported by our answer to part (d): if someone is detected as being a spy, the probability is only 0.005, or half of one percent, that he or she actually is one.

    ```{figure} images/image017.gif
    :alt: In order to calculate P(S | D), we attempt to calculate P(S | D) = P(S and D)/P(D). First, we note that P(S and D) comes from the tree path {S: 0.001, D: 0.80}, so P(S and D) = P(S) and P(D|S) = 0.001 * 0.80 = 0.0008. We also note that P(not S and D) comes from the tree path {not S: 0.999, D: 0.16 }, so P(not S and D) = P(not S) and P(D | not S) = 0.999 * 0.16 = 0.15984. So, now we can calculate P(D) = P(S and D) or P(not S and D) = 0.0008 + 0.15984 = 0.16064. Now, we can calculate P(S | D) = P(S and D)/P(D) = 0.0008/0.16064 = 0.005.

    In order to calculate P(S | D), we attempt to calculate P(S | D) = P(S and D)/P(D). First, we note that P(S and D) comes from the tree path {S: 0.001, D: 0.80}, so P(S and D) = P(S) and P(D|S) = 0.001 * 0.80 = 0.0008. We also note that P(not S and D) comes from the tree path {not S: 0.999, D: 0.16 }, so P(not S and D) = P(not S) and P(D | not S) = 0.999 * 0.16 = 0.15984. So, now we can calculate P(D) = P(S and D) or P(not S and D) = 0.0008 + 0.15984 = 0.16064. Now, we can calculate P(S | D) = P(S and D)/P(D) = 0.0008/0.16064 = 0.005.
    ```
```

## Comment

This example helps to highlight how different P(B | A) may be from P(A | B): the probability of being detected, given that an employee is a spy, is P(D | S) = 0.80. In contrast, the probability of being a spy, given that an employee has been detected by the polygraph, is P(S | D) = 0.005.

The purpose of the next activity is to give you guided practice in using the information displayed in probability trees in order to answer real-life problems.

## Learn By Doing

Let's consider the engine overheating example again, where H is the event that the engine overheats and W is the event that a warning light turns on. We are given that:

P(H) = 0.03

P(W | H) = 0.98

P(W | not H) = 0.01

and in a previous activity we displayed the information using a probability tree:

```{figure} images/lbd002.gif
:alt: Here is the probability tree with paths through the tree shown in "{ 1st branch-off: probability of 1st branch off, 2nd branch-off: probability of 2nd branch off}": {H: 0.03, W: 0.98}; {H: 0.03, not W: 0.02}; {not H: 0.97, W: 0.01}; {not H: 0.97, not W: 0.99};

Here is the probability tree with paths through the tree shown in "{ 1st branch-off: probability of 1st branch off, 2nd branch-off: probability of 2nd branch off}": {H: 0.03, W: 0.98}; {H: 0.03, not W: 0.02}; {not H: 0.97, W: 0.01}; {not H: 0.97, not W: 0.99};
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
