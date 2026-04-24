# Probability Rules (5 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

Rule 4, the addition rule, deals with finding P(A *or* B). We are now moving on to rule 5, which deals with yet another situation of frequent interest, finding P(A *and* B), the probability that both events A and B occur. In other words,

*P(A and B) = P(event A occurs and event B occurs)*

For example, we might be interested in the probability that if two people are chosen at random, both the first has blood type O *and* the second has blood type O. Since a person with blood type O can donate blood to anyone, this probability might be of particular interest in this context.

Using a Venn diagram, we can visualize "A and B," which is represented by the overlap between events A and B:

```{figure} images/image019.gif
:alt: A rectangle represents the entire sample space. Inside this rectangle are two circles, one for the occurrences in A and one for the occurrences in B. These two circles partially overlap. The area in the overlap contains the ocurrences for A and B.

A rectangle represents the entire sample space. Inside this rectangle are two circles, one for the occurrences in A and one for the occurrences in B. These two circles partially overlap. The area in the overlap contains the ocurrences for A and B.
```

## Comment

There is one special case for which we know what P(A and B) equals without applying any rule.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

So, if events *A and B are disjoint*, then (by definition) *P(A and B)= 0.* But what if the events are not disjoint?

Recall that rule 4, the Addition Rule, has two versions. One is restricted to disjoint events, which we've already covered, and we'll deal with the more general version later in this module. The same is true of rule 5. Rule 5 has two versions. The version we'll present here is restricted to a special case that we'll now discuss, and there is a more general version that we'll present in the next module.

The version of rule 5 that will be presented here applies to the special case in which the two events are *independent* of each other.

```{admonition} Definition: independent
    Two events A and B are said to be *independent* if
                            the
                            fact
                            that
                            one event has occurred *does not affect* the probability that the
                            other event
                            will
                            occur.
                            If whether
                            or not
                            one event occurs *does affect* the probability that
                            the other event
                            will
                            occur,
                            then the two events are said to be *dependent.*
```

Here are a few examples:

```{admonition} Example
    A woman's pocket contains two quarters and two nickels. She randomly extracts one of the coins and, after looking at it, replaces it before picking a second coin.

    Let Q1 be the event that the first coin is a quarter and Q2 be the event that the second coin is a quarter.

    Are Q1 and Q2 independent events? *Yes.* Why?

    Since the first coin that was selected is *replaced*, whether or not Q1 occurred (i.e., whether the first coin was a quarter) has no effect on the probability that the second coin will be a quarter, P(Q2). In either case (whether Q1 occurred or not), when she is selecting the second coin, she has in her pocket:

    ```{figure} images/image020.gif
    :alt: The coins in the woman's pocket. There are 2 Quarters and 2 Nickels.

    The coins in the woman's pocket. There are 2 Quarters and 2 Nickels.
    ```

    and therefore the P(Q2) = 2/4 = 1/2 regardless of whether Q1 occurred.
```

```{admonition} Example
    A woman's pocket contains two quarters and two nickels. She randomly extracts one of the coins, and *without placing* it back into her pocket, she picks a second coin. As before, let Q1 be the event that the first coin is a quarter, and Q2 be the event that the second coin is a quarter.

    Are Q1 and Q2 independent events? *No.* Q1 and Q2 are *not independent*. They are *dependent.* Why?

    Since the first coin that was selected is *not replaced,* whether Q1 occurred (i.e., whether the first coin was a quarter) *does affect* the probability that the second coin is a quarter, P(Q2).

    If Q1 occurred (i.e., the first coin was a quarter), then when the woman is selecting the second coin, she has in her pocket:

    ```{figure} images/image021.gif
    :alt: One Quarter and Two Nickels

    One Quarter and Two Nickels
    ```

    In this case, P(Q2) = 1/3. However, if Q1 has not occurred (i.e., the first coin was not a quarter, but a nickel), then when the woman is selecting the second coin, she has in her pocket:

    ```{figure} images/image022.gif
    :alt: Two Quarters and One Nickel.

    Two Quarters and One Nickel.
    ```

    In this case, P(Q2) = 2/3.

    In these last two examples, we could actually have done some calculation in order to check whether or not the two events are independent or not. Sometimes we can just use common sense to guide us as to whether two events are independent. Here is an example.
```

```{admonition} Example
    A family has 4 children, two of whom are selected at random. Let B1 be the event that one child has blue eyes, and B2 be the event that the other chosen child has blue eyes. In this case, B1 and B2 are not independent, since we know that eye color is hereditary, so whether or not one child is blue-eyed will increase or decrease the chances that the other child has blue eyes, respectively.
```

```{admonition} Example
    Two people are selected at random from all people in the United States. Let B1 be the event that one of the people has blue eyes and B2 be the event that the other person has blue eyes. In this case, since they were chosen at random, whether one of them has blue eyes has no effect on the likelihood that the other one has blue eyes, and therefore B1 and B2 are independent. On the other hand ...
```

*Note:*

We can generalize what we learned in the last example and say that when two individuals are selected at random from a large population (like in the example, the entire U.S.) any event associated with one individual is independent of any event associated with the other individual. The fact that the two are chosen from a large population is key to the independence.

If we were to change the example to: There are 10 people in a room, 4 of which have blue eyes. Two people are chosen at random. Let B1 be the event that the first person has blue eyes and let B2 be the event that the second person has blue eyes. In this case, since the two are chosen from a group of only 10 (rather than a large population) the events B1 and B2 are not independent. Clearly, whether or not the first person has blue eyes (i.e., whether or not B1 occurs) does have an effect on whether B2 occurs. You will get more practice on this point in the activities below the next comment.

## Comment

It is quite common for students to initially get confused about the distinction between the idea of *disjoint events* and the idea of *independent events*. The purpose of this comment (and the activity that follows it) is to help students develop more understanding about these very different ideas.

The idea of *disjoint events* is about whether or not it is possible for the events to occur at the same time (see the examples on page 3 of the Probability Rules section).

The idea of *independent events* is about whether or not the events affect each other in the sense that the occurrence of one event affects the probability of the occurrence of the other (see the examples above).

The following activity deals with the distinction between these concepts.

The purpose of this activity is to help you strengthen your understanding about the concepts of disjoint events and independent events, and the distinction between them.

In each of the following questions, you are presented with a random experiment and two events related to it. You are asked to decide whether the events are disjoint or not, and whether the events are independent or not.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Let’s summarize the three parts of the activity:

- In Example 1: A and B are *not disjoint* and *independent*
- In Example 2: A and B are *not disjoint* and *not independent*
- In Example 3: A and B are *disjoint* and *not independent* .

Why did we leave out the case when the events are disjoint and independent? The reason is that this case DOES NOT EXIST!

|  | *A and B Independent* | *A and B Not Independent* |
| --- | --- | --- |
| *A and B Disjoint* | *DOES NOT EXIST* | Example 3 |
| *A and B Not Disjoint* | Example 1 | Example 2 |

If events are *disjoint* then they *must be not independent (dependent)*

Why is that?

Recall: A and B disjoint means that they cannot happen together. In other words, A and B disjoint implies that if event A occurs then B does not and vice versa. Well… if that’s the case, knowing that event A has occurred dramatically changes the likelihood that event B occurs – that likelihood is $0$. This implies that A and B are not independent.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Now that we understand the idea of independent events, we can finally get to rule 5. As mentioned before, Rule 5 actually has two versions, one for finding P(A and B) in the special case in which the events A and B are independent, and a more general version for use when the events are not necessarily independent. We will first present the version of rule 5 that is restricted to independent events, and in the next module we will revisit Rule 5 and present the more general version.
