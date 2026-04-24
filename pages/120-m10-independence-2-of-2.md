# Independence (2 of 2)

```{admonition} Learning Objectives
    - Determine whether two events are independent or not.
```

## Comment

Recall the pierced ears example. We checked the independence of the events M (being a male) and E (having pierced ears) by comparing P(E) to P(E | M).

An alternative method of checking for dependence would be to compare P(E | M) with P(E | not M) [same as P(E | F)]. In our case, P(E | M) = 36/180 = .2, while P(E | not M) = 288/320 = .9, and since the two are very different, we can say that the events E and M are not independent.

In general, another method for checking the independence of events A and B is to compare *P(B | A) and P(B | not A)*. In other words, two events are independent if the probability of one event does not change whether we know that the other event has occurred or we know that the other event has not occurred. It can be shown that *P(B | A) and P(B | not A)*. would differ whenever P(B) and P(B | A) differ, so this is another perfectly legitimate way to establish dependence or independence.

## Did I Get This?

Recall again the smoke alarms example.

A homeowner has smoke alarms installed in the dining room (adjacent to the kitchen) and an upstairs bedroom (above the kitchen). The two-way table below shows probabilities of smoke in the kitchen triggering the alarm in the dining room (D) or not, and in the bedroom (B) or not.

```{figure} images/dig002.gif
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Before we establish a general rule for independence, let's consider an example that will illustrate another method that we can use to check whether two events are independent:

```{admonition} Example
    A group of 100 college students were surveyed about their gender and whether they had decided on a major.

    ```{figure} images/image004.gif
    ```

    Offhand, we wouldn't necessarily have any compelling reason to expect that deciding on a major would depend on a student's gender. We can check for independence by comparing the overall probability of being decided to the probability of being decided given that a student is female:

    P(D) = 45/100 = .45 and P(D | F) = 27/60 = .45.

    The fact that the two are equal tells us that, as we might expect, deciding on a major is independent of gender. Note from the comment that these must also equal P(D | M), which is 18/40 = .45.

    Now let's approach the issue of independence in a different way: first, we may note that the overall probability of being decided is 45/100 = .45.

    ```{figure} images/image005.gif
    ```

    And the overall probability of being female is 60/100 = .60.

    ```{figure} images/image006.gif
    ```

    If being decided is independent of gender, then 45% of the 60% of the class who are female should have a decided major; in other words, the probability of being female and decided should equal the probability of being female multiplied by the probability of being decided. If the events F and D are independent, we should have P(F and D) = P(F) * P(D).

    In fact, P(F and D) = 27/100 = .27 = P(F) * P(D) = .45 * .60. This confirms our alternate verification of independence.
```

In general, another method for checking the independence of events A and B is to compare P(A and B) to P(A) * P(B). If the two are equal, then A and B are independent, otherwise the two are not independent.

Let's summarize all the possible methods we've seen for checking the independence of events in one rule:

Two events A and B are independent if any one of the following hold:

P(B | A) = P(B)

P(A | B) = P(A)

P(B | A) = P(B | not A)

P(A and B) = P(A) * P(B)

## Comment

These various equalities turn out to be equivalent, so that if one equality holds, all are equal, and if one equality does not hold, all are not equal. (This is the case for the same reason that knowing one of the values P(A and B), P(A and not B), P(not A and B), or P(not A and not B), along with P(A) and P(B), allows you to determine the remaining cells of a two-way probability table.)

Therefore, in order to check whether events A and B are independent or not, it is sufficient to check only whether one of the four equalities holds—whichever is easiest for you.

The purpose of the next activity is to practice checking the independence of two events using the four different possible methods that we've provided, and see that all of them will lead us to the same conclusion, regardless of which of the four methods we use.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
