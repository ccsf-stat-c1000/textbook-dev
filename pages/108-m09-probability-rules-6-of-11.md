# The Multiplication Rule for Independent Events: Finding P(A and B)

```{admonition} Rule 5: The Multiplication Rule for Independent Events
:class: note

*If A and B are two independent events, then P(A and B) = P(A) × P(B).*
```

```{admonition} Comment
:class: important

When dealing with probabilities, the word *"and"* will always be associated with the operation of *multiplication*; hence the name of this rule, "The Multiplication Rule."
```

:::{admonition} Example: Two Type O Donors
:class: tip

Recall the blood type example:

| Blood Type | O | A | B | AB |
| --- | --- | --- | --- | --- |
| Probability | 0.44 | 0.42 | 0.10 | 0.04 |

Two people are selected simultaneously and at random from all people in the United States. What is the probability that both have blood type O?

Let O1 = "person 1 has blood type O" and O2 = "person 2 has blood type O."

We need to find P(O1 and O2).

Since they were chosen simultaneously and at random, the blood type of one has no effect on the blood type of the other. Therefore, O1 and O2 are independent, and we may apply Rule 5:

P(O1 and O2) = P(O1) × P(O2) = 0.44 × 0.44 = 0.1936.
:::

:::{quiz} Using the table above, two people are chosen at random from the U.S. population. What is the probability that both have blood type AB?
:hint: The two choices are independent; multiply.
:feedback-0: Correct! P(AB1 and AB2) = 0.04 × 0.04 = 0.0016.
:feedback-1: 0.08 is the sum, which would answer an "or" question for disjoint events, not an "and" question.
:feedback-2: 0.04 is the probability for one person; both having AB is much less likely.
* *0.0016
* 0.08
* 0.04
:::

:::{quiz} A fair coin is tossed and a fair die is rolled. What is the probability of getting heads AND rolling a 6?
:hint: The coin and die don't affect each other—multiply the probabilities.
:feedback-0: Correct! P(H and 6) = (1/2) × (1/6) = 1/12.
:feedback-1: 1/8 would be right if the die had 4 sides; the die's probability is 1/6.
:feedback-2: 2/3 comes from adding—but "and" calls for multiplication here.
* *1/12
* 1/8
* 2/3
:::

So far we have looked at examples where we have to consider and apply only one of the rules. The following example is a case where both the Addition Rule for Disjoint Events and the Multiplication Rule for Independent Events need to be applied in order to find the desired probability.

:::{admonition} Example: Same Blood Type
:class: tip

Two people are chosen simultaneously and at random. What is the probability that both have the same blood type? For both to have the same blood type there are four possibilities: both have blood type O *or* both have blood type A *or* both have blood type B *or* both have blood type AB.

In other words, and using our regular notations,

P(same blood type) = P([O1 and O2] or [A1 and A2] or [B1 and B2] or [AB1 and AB2])

Since our four possibilities of both people having the same blood type are *disjoint*, using our *Addition Rule* we can add their probabilities (i.e., replace every "or" with +). Also, within each of the four possibilities, we can use the {term}`Multiplication Rule <multiplication rule>` and replace "and" with × (using the same *independence* argument as the first example on this page). Our answer is therefore:

$$P(\text{same blood type}) = 0.44^2 + 0.42^2 + 0.10^2 + 0.04^2 = 0.1936 + 0.1764 + 0.01 + 0.0016 = 0.3816$$

About 38% of the time, two randomly chosen U.S. people would have the same blood type. Note that in this example we used the Addition Rule and the Multiplication Rule one after the other, justifying along the way why it is appropriate to do so.
:::

```{admonition} Comment
:class: important

The purpose of this comment is to point out the magnitude of P(A or B) and of P(A and B) relative to either one of the individual probabilities. Since probabilities are never negative, the probability of one event *or* another is always at least as large as either of the individual probabilities. Since probabilities are never more than 1, the probability of one event *and* another generally involves multiplying numbers that are less than 1, and therefore can never be more than either of the individual probabilities.
```

Here is an example:

:::{admonition} Example: More General vs. More Specific
:class: tip

Consider the event A that a randomly chosen person has blood type A. Modify it to a more general event—that a randomly chosen person has blood type A or B—and the probability increases. Modify it to a more specific (or restrictive) event—that not just one randomly chosen person has blood type A, but that out of two simultaneously randomly chosen people, person 1 will have type A and person 2 will have type B—and the probability decreases.
:::

It is important to mention this in order to root out a common misconception. The word "and" is associated in our minds with "adding more stuff." Therefore, some students *incorrectly* think that P(A and B) should be larger than either one of the individual probabilities, while it is actually smaller, since it is a more specific (restrictive) event. Also, the word "or" is associated in our minds with "having to choose between" or "losing something," and therefore some students incorrectly think that P(A or B) should be smaller than either one of the individual probabilities, while it is actually larger, since it is a more general event.

Practically, you can use this comment to check yourself when solving problems. For example, if you solve a problem that involves "or," and the resulting probability is smaller than either one of the individual probabilities, then you know you have made a mistake somewhere.

:::{quiz} A student computes P(A or B) = 0.15 for two events with P(A) = 0.3 and P(B) = 0.25. Without redoing the calculation, how do you know this answer is wrong?
:hint: How does P(A or B) compare to the individual probabilities?
:feedback-0: Correct! "A or B" is a more general event than A alone, so P(A or B) must be at least as large as the larger individual probability (0.3)—0.15 is impossible.
:feedback-1: Probabilities of "or" events don't have to exceed 0.5; the giveaway is comparing with P(A) and P(B).
:feedback-2: The sum being over 0.5 is fine; the problem is that 0.15 is smaller than both P(A) and P(B).
* *P(A or B) can never be smaller than P(A) or P(B) individually
* Any "or" probability must be greater than 0.5
* P(A) + P(B) is more than 0.5, so the answer must be more than 0.5
:::
