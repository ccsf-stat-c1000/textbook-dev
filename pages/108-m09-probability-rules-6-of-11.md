# Probability Rules (6 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

```{admonition} Rule 5: The Multiplication Rule for Independent Events
    *If A and B are two independent events, then P(A and B) = P(A) * P(B).*
```

## Comment

When dealing with probabilities, the word *"and"* will always be associated with the operation of *multiplication*; hence the name of this rule, "The Multiplication Rule."

```{admonition} Example
    Recall the blood type example:

    ```{figure} images/image011.gif
    :alt: Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;

    Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;
    ```

    Two people are selected simultaneously and at random from all people in the United States. What is the probability that both have blood type O?

    Let O1= "person 1 has blood type O" and

    O2= "person 2 has blood type O"

    We need to find P(O1 and O2)

    Since they were chosen simultaneously and at random, the blood type of one has no effect on the blood type of the other. Therefore, O1 and O2 are independent, and we may apply Rule 5:

    P(O1 and O2) = P(O1) * P(O2) = .44 * .44 = .1936.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

So far we have looked at examples where we have to consider and apply only one of the rules. The following example is a case where both the Addition Rule for Disjoint Events and the Multiplication Rule for Independent Events need to be applied in order to find the desired probability.

```{admonition} Example
    Recall the blood types example:

    ```{figure} images/image011.gif
    :alt: Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;

    Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;
    ```

    Two people are chosen simultaneously and at random. What is the probability that both have the same blood type? For both to have the same blood type there are four possibilities. Both have blood type O *or* both have blood type A *or* both have blood type B *or* both have blood type AB.

    ```{figure} images/image023.gif
    :alt: A diagram showing the four possibilities.

    A diagram showing the four possibilities.
    ```

    In other words, and using our regular notations,

    P(same blood type) = P([O1 and O2] or [A1 and A2] or [B1 and B2] or [AB1 and AB2])

    Since our four possibilities of both people having the same blood type are *disjoint*, using our *Addition Rule* we can add their probabilities (i.e., replace every "or" with +). Also, within each of the four possibilities, we can use the *Multiplication Rule* and replace "and" with * (using the same *independence* argument as the first example on this page). Our answer is therefore,

    ```{figure} images/image024.gif
    :alt: P(O and O) = .44 * .44 P(B and B) = .42 * .42 P(B and B) = .10 * .10 P(AB and AB) = .04 * .04 P(Both having the same blood type) = P(O and O) + P(A and A) + P(B and B) + P(AB and AB) = 0.3816

    P(O and O) = .44 * .44 P(B and B) = .42 * .42 P(B and B) = .10 * .10 P(AB and AB) = .04 * .04 P(Both having the same blood type) = P(O and O) + P(A and A) + P(B and B) + P(AB and AB) = 0.3816
    ```

    About 38% of the time, two randomly chosen U.S. people would have the same blood type. Note that in this example we used the Addition Rule and the Multiplication Rule one after the other, justifying along the way why it is appropriate to do so.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

The purpose of this comment is to point out the magnitude of P(A or B) and of P(A and B) relative to either one of the individual probabilities. Since probabilities are never negative, the probability of one event *or* another is always at least as large as either of the individual probabilities. Since probabilities are never more than 1, the probability of one event *and* another generally involves multiplying numbers that are less than 1, therefore can never be more than either of the individual probabilities.

Here is an example:

```{admonition} Example
    Consider the event A that a randomly chosen person has blood type A. Modify it to a more general event—that a randomly chosen person has blood type A or B—and the probability increases. Modify it to a more specific (or restrictive) event—that not just one randomly chosen person has blood type A, but that out of two simultaneously randomly chosen people, person 1 will have type A and person 2 will have type B—and the probability decreases.
```

It is important to mention this in order to root out a common misconception. The word "and" is associated in our minds with "adding more stuff." Therefore, some students *incorrectly* think that P(A and B) should be larger than either one of the individual probabilities, while it is actually smaller, since it is a more specific (restrictive) event. Also, the word "or" is associated in our minds with "having to choose between" or "losing something," and therefore some students incorrectly think that P(A or B) should be smaller than either one of the individual probabilities, while it is actually larger, since it is a more general event.

Practically, you can use this comment to check yourself when solving problems. For example, if you solve a problem that involves "or," and the resulting probability is smaller than either one of the individual probabilities, then you know you have made a mistake somewhere.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
