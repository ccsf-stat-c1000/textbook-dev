# Independence in Practice: Checks and Consequences

```{admonition} Learning Objectives
:class: note

- Determine whether two events are independent or not.
```

## Comment

Recall the pierced ears example. We checked the independence of the events M (being a male) and E (having pierced ears) by comparing P(E) to P(E | M).

An alternative method of checking for dependence would be to compare P(E | M) with P(E | not M) [same as P(E | F)]. In our case, P(E | M) = 36/180 = 0.2, while P(E | not M) = 288/320 = 0.9, and since the two are very different, we can say that the events E and M are not independent.

In general, another method for checking the independence of events A and B is to compare *P(B | A)* and *P(B | not A)*. In other words, two events are independent if the probability of one event does not change whether we know that the other event has occurred or we know that the other event has not occurred. It can be shown that *P(B | A)* and *P(B | not A)* would differ whenever P(B) and P(B | A) differ, so this is another perfectly legitimate way to establish dependence or independence.

## Did I Get This?

Recall again the smoke alarms example:

| | B | not B | Total |
| --- | --- | --- | --- |
| **D** | 0.38 | 0.57 | 0.95 |
| **not D** | 0.02 | 0.03 | 0.05 |
| **Total** | 0.40 | 0.60 | 1.00 |

:::{quiz} Check independence by comparing P(D | B) with P(D | not B). What do you find?
:hint: P(D | B) = 0.38/0.40; P(D | not B) = 0.57/0.60.
:feedback-0: Correct! P(D | B) = 0.95 and P(D | not B) = 0.95—the same—so D and B are independent.
:feedback-1: Compute carefully: 0.38/0.40 = 0.95 and 0.57/0.60 = 0.95; they are equal.
* *Both equal 0.95, so D and B are independent
* They differ, so D and B are dependent
:::

Before we establish a general rule for independence, let's consider an example that will illustrate another method that we can use to check whether two events are independent:

:::{admonition} Example: Deciding on a Major
:class: tip

A group of 100 college students were surveyed about their gender and whether they had decided on a major:

| | Decided (D) | Undecided | Total |
| --- | --- | --- | --- |
| Female (F) | 27 | 33 | 60 |
| Male (M) | 18 | 22 | 40 |
| **Total** | **45** | **55** | **100** |

Offhand, we wouldn't necessarily have any compelling reason to expect that deciding on a major would depend on a student's gender. We can check for independence by comparing the overall probability of being decided to the probability of being decided given that a student is female:

P(D) = 45/100 = 0.45 and P(D | F) = 27/60 = 0.45.

The fact that the two are equal tells us that, as we might expect, deciding on a major is independent of gender. Note from the comment that these must also equal P(D | M), which is 18/40 = 0.45.

Now let's approach the issue of independence in a different way: first, we may note that the overall probability of being decided is 45/100 = 0.45, and the overall probability of being female is 60/100 = 0.60.

If being decided is independent of gender, then 45% of the 60% of the class who are female should have a decided major; in other words, the probability of being female and decided should equal the probability of being female multiplied by the probability of being decided. If the events F and D are independent, we should have P(F and D) = P(F) × P(D).

In fact, P(F and D) = 27/100 = 0.27 = P(F) × P(D) = 0.60 × 0.45. This confirms our alternate verification of independence.
:::

In general, another method for checking the independence of events A and B is to compare P(A and B) to P(A) × P(B). If the two are equal, then A and B are independent; otherwise the two are not independent.

Let's summarize all the possible methods we've seen for checking the independence of events in one rule:

```{admonition} Checking Independence
:class: note

Two events A and B are independent if any one of the following holds:

- P(B | A) = P(B)
- P(A | B) = P(A)
- P(B | A) = P(B | not A)
- P(A and B) = P(A) × P(B)
```

## Comment

These various equalities turn out to be equivalent, so that if one equality holds, all are equal, and if one equality does not hold, all are not equal. (This is the case for the same reason that knowing one of the values P(A and B), P(A and not B), P(not A and B), or P(not A and not B), along with P(A) and P(B), allows you to determine the remaining cells of a two-way probability table.)

Therefore, in order to check whether events A and B are independent or not, it is sufficient to check only whether one of the four equalities holds—whichever is easiest for you.

## Learn By Doing

A random sample of 1,200 adults was surveyed about whether they exercise regularly (X) and whether they get at least 7 hours of sleep most nights (V):

| | V | not V | Total |
| --- | --- | --- | --- |
| **X** | 240 | 160 | 400 |
| **not X** | 480 | 320 | 800 |
| **Total** | **720** | **480** | **1200** |

:::{quiz} Are the events X and V independent? Verify with any of the four checks.
:hint: For instance, compare P(V | X) = 240/400 with P(V) = 720/1200.
:feedback-0: Correct! P(V | X) = 0.6 = P(V); also P(X and V) = 0.2 = P(X) × P(V) = (1/3)(0.6). All four checks agree: independent.
:feedback-1: Run the numbers: P(V | X) = 240/400 = 0.6 and P(V) = 720/1200 = 0.6—equal, so the events are independent.
:feedback-2: The events overlap (240 people are in both), but overlapping is about disjointness, not independence.
* *Yes—for example, P(V | X) = 0.6 = P(V)
* No—the conditional and unconditional probabilities differ
* No—because the events can occur together
:::
