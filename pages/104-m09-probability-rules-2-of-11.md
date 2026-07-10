# Probability Rules (2 of 11)

```{admonition} Learning Objectives
:class: note

- Apply probability rules in order to find the likelihood of an event.
```

Let's move on to rule 3. In probability and in its applications, we are frequently interested in finding out the probability that a certain event will *not* occur. An important point to understand here is that "event A does not occur" is *a separate event* that consists of all the outcomes in the sample space S that are not in A. It is for this reason that the event "event A does not occur" is called *"the complement event of A,"* since it complements event A to the whole sample space. Notation: we will write *"not A"* to denote the event that A does *not* occur. Here is a visual representation of how event A and its complement event "not A" together represent the whole sample space.

```{figure} images/gen/m09-complement-venn.svg
:alt: A Venn diagram. The entire sample space S is a shaded rectangle. Inside it is a blue circle representing the outcomes in A. Everything in the rectangle outside the circle is the complement event, not A.
```

## Comment

Such a visual display is called a "Venn diagram." A Venn diagram is a simple way to visualize events and the relationships between them using rectangles and circles. We will use Venn diagrams throughout this module.

Rule 3 deals with the relationship between the probability of an event and the probability of its complement event. Given that event A and event "not A" together make up the whole sample space S, and since rule 2 tells us that P(S) = 1, the following rule should be quite intuitive:

```{admonition} Rule 3: The Complement Rule
:class: note

*P(not A) = 1 − P(A); that is, the probability that an event does not occur is 1 minus the probability that it does occur.*
```

:::{admonition} Example: Blood Types (continued)
:class: tip

Back to the blood type example:

| Blood Type | O | A | B | AB |
| --- | --- | --- | --- | --- |
| Probability | 0.44 | 0.42 | 0.10 | 0.04 |

Here is some additional information:

- A person with type *A* can donate blood to a person with type *A* or *AB*.
- A person with type *B* can donate blood to a person with type *B* or *AB*.
- A person with type *AB* can donate blood to a person with type *AB* only.
- A person with type *O* blood can donate to anyone.

What is the probability that a randomly chosen person cannot donate blood to everyone? In other words, what is the probability that a randomly chosen person does not have blood type O? We need to find P(not O). Using the Complement Rule, P(not O) = 1 − P(O) = 1 − 0.44 = 0.56. In other words, 56% of the U.S. population does not have blood type O.
:::

## Comment

Note that the Complement Rule, *P(not A) = 1 − P(A)*, can be re-formulated as *P(A) = 1 − P(not A).* This seemingly trivial algebraic manipulation has an important application, and actually captures the strength of the complement rule. In some cases, when finding P(A) directly is very complicated, it might be much easier to find P(not A) and then just subtract it from 1 to get the desired P(A). We will come back to this comment and see examples later in this module.

## Did I Get This?

On the "Information for the Patient" label of a certain antidepressant it is claimed that based on some clinical trials, when taking this medication:

- there is a 14% chance of experiencing sleeping problems, or insomnia (denote this event by I),
- there is a 26% chance of experiencing headaches (denote this event by H), and
- there is a 35% chance of experiencing at least one of these two side effects (denote this event by L).

:::{quiz} What is the probability that a patient taking this medication does NOT experience insomnia?
:hint: Use the Complement Rule with P(I) = 0.14.
:feedback-0: Correct! P(not I) = 1 − 0.14 = 0.86.
:feedback-1: 0.14 is the probability of experiencing insomnia; the question asks for its complement.
:feedback-2: Don't subtract from the headache probability—use 1 − P(I).
* *0.86
* 0.14
* 0.74
:::

:::{quiz} What is the probability that a patient experiences NEITHER of the two side effects?
:hint: "Neither" is the complement of "at least one" (event L).
:feedback-0: Correct! P(neither) = 1 − P(L) = 1 − 0.35 = 0.65.
:feedback-1: 0.60 would come from adding P(I) + P(H) and subtracting from 1, but the events can overlap—use the given P(at least one) instead.
:feedback-2: 0.35 is the probability of at least one side effect; "neither" is its complement.
* *0.65
* 0.60
* 0.35
:::
