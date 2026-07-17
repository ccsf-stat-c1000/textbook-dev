# Solving Problems with Probability Tables

```{admonition} Learning Objectives
:class: note

- Apply probability rules in order to find the likelihood of an event.
- When appropriate, use tools such as Venn diagrams or probability tables as aids for finding probabilities.
```

Now that we know how to build a two-way probability table, let's see how we can use information from it to solve problems.

:::{admonition} Example: Reading Probabilities from the Table
:class: tip

Let's go back to our delivery example and see how we can "lift" probabilities from the two-way probability table in order to answer the question posed in that example and related questions. Here is the table again:

| | B | not B | Total |
| --- | --- | --- | --- |
| **A** | 0.75 | 0.15 | 0.90 |
| **not A** | 0.05 | 0.05 | 0.10 |
| **Total** | 0.80 | 0.20 | 1.00 |

What is the probability of on-time delivery of the document using the two-services strategy? In other words, what is P(A or B)?

We can use the table in two ways:

(i) We can simply lift P(A) = 0.90, P(B) = 0.80, and P(A and B) = 0.75 from the table and use the General Addition Rule, as we did before: P(A or B) = P(A) + P(B) − P(A and B) = 0.90 + 0.80 − 0.75 = 0.95.

(ii) Another way to use the table is to use the fact that in probability, "A or B" actually means "A or B or both." The corresponding cells for these three options are 0.15 (only A), 0.05 (only B), and 0.75 (both). We can add these up to get P(A or B) = 0.15 + 0.05 + 0.75 = 0.95.
:::

:::{admonition} Example: Exactly One Service
:class: tip

What is the probability of on-time delivery by exactly one service?

On-time delivery by exactly one service occurs if the document arrives on time by service A and not B, or by service B and not A. The probabilities of these two possibilities are 0.15 and 0.05, respectively. Therefore, P(on-time delivery by exactly one service) = 0.15 + 0.05 = 0.20.
:::

:::{admonition} Example: Neither Service
:class: tip

What is the probability that the document will *not* get to its destination on time? This would be the occurrence of the event "not A and not B," whose probability, read directly from the table, is 0.05.
:::

## Concept Check

Use the smoke-detector table you completed on the previous page:

| | B | not B | Total |
| --- | --- | --- | --- |
| **D** | 0.38 | 0.57 | 0.95 |
| **not D** | 0.02 | 0.03 | 0.05 |
| **Total** | 0.40 | 0.60 | 1.00 |

:::{quiz} What is the probability that exactly one of the two alarms is set off by smoke in the kitchen?
:hint: Add the "only D" and "only B" cells.
:feedback-0: Correct! P(exactly one alarm) = P(D and not B) + P(not D and B) = 0.57 + 0.02 = 0.59.
:feedback-1: 0.97 is P(D or B)—at least one alarm—which also includes both alarms going off.
:feedback-2: 0.38 is the probability that both alarms go off.
* *0.59
* 0.97
* 0.38
:::

We are now done with this section, which introduced various probability rules. Let's summarize what we've learned.

1. The Complement Rule states that

   *P(not A) = 1 − P(A)*, or when rearranged, *P(A) = 1 − P(not A).*

   The Complement Rule is very useful when we need to find probabilities of the sort P(at least one of several events occurs), which is hard to calculate directly. In this case, we apply the Complement Rule:

   *P(at least one of several events occurs) = 1 − P(none of the events occur)*, since P(none of the events occur) is usually much easier to find.

2. The General Addition Rule states that for any two events,

   *P(A or B) = P(A) + P(B) − P(A and B)*,

   where by P(A or B) we mean P(A occurs or B occurs or both).

   In the special case when A and B are *disjoint* events (which means that P(A and B) = 0), the general addition rule becomes P(A or B) = P(A) + P(B), which we call the Addition Rule for Disjoint Events. Beware of wrongly using the Addition Rule for Disjoint Events when the events are not disjoint.

3. When we want to find P(A and B), we can use the Multiplication Rule, but so far we've only learned the restricted version of this rule—the Multiplication Rule for Independent Events. Events are independent if the occurrence of one of the events has no effect on the probability of the other occurring, in which case:

   *P(A and B) = P(A) × P(B).*

4. The Addition Rule for Disjoint Events can be naturally extended to more than two events. In other words, if events A, B, and C are disjoint, then P(A or B or C) = P(A) + P(B) + P(C). Similarly, the Multiplication Rule for Independent Events can be naturally extended to more than two independent events: if events A, B, and C are independent, then P(A and B and C) = P(A) × P(B) × P(C). The same is true for 4, 5, ... disjoint/independent events.

5. When there are two categorical variables in the background, each with two possible values, a *two-way probability table* is a quick and easy way to display the probabilities associated with the 4 possible combinations.
