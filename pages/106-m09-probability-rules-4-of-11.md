# The Addition Rule for Disjoint Events: Finding P(A or B)

```{admonition} Learning Objectives
:class: note

- Apply probability rules in order to find the likelihood of an event.
```

```{admonition} Rule 4: The Addition Rule for Disjoint Events
:class: note

*If A and B are disjoint events, then P(A or B) = P(A) + P(B).*
```

```{admonition} Comment
:class: important

When dealing with probabilities, the word "or" will always be associated with the operation of addition; hence the name of this rule, "The Addition Rule."
```

:::{admonition} Example: Potential Donors
:class: tip

Recall the blood type example:

| Blood Type | O | A | B | AB |
| --- | --- | --- | --- | --- |
| Probability | 0.44 | 0.42 | 0.10 | 0.04 |

Here is some additional information:

- A person with type *A* can donate blood to a person with type *A* or *AB*.
- A person with type *B* can donate blood to a person with type *B* or *AB*.
- A person with type *AB* can donate blood to a person with type *AB* only.
- A person with type *O* blood can donate to anyone.

What is the probability that a randomly chosen person is a potential donor for a person with blood type A?

From the information given, we know that being a potential donor for a person with blood type A means having blood type A or O. We therefore need to find P(A or O). Since the events A and O are disjoint, we can use the addition rule for disjoint events to get: P(A or O) = P(A) + P(O) = 0.42 + 0.44 = 0.86. It is easy to see why adding the probabilities actually makes sense. If 42% of the population has blood type A and 44% of the population has blood type O, then 42% + 44% = 86% of the population has either blood type A or O, and thus are potential donors to a person with blood type A. (Picture the pie chart of blood types: the A and O slices together take up 86% of the pie.)
:::

:::{quiz} Using the blood type table, what is the probability that a randomly chosen person has blood type B or AB?
:hint: The blood types are disjoint, so add their probabilities.
:feedback-0: Correct! P(B or AB) = 0.10 + 0.04 = 0.14.
:feedback-1: 0.10 is P(B) alone—don't forget type AB.
:feedback-2: Multiplication is not appropriate here; for disjoint events, "or" means addition.
* *0.14
* 0.10
* 0.004
:::

## Learn By Doing

So far we have introduced the addition rule for the special case in which the events being considered are disjoint. The purpose of this activity is to make you aware of the danger in wrongly using the addition rule for disjoint events in cases where the events are actually not disjoint. Consider the blood type example again, with the same donation rules as above.

Suppose that there are two patients who are each in need of a blood donation. Patient 1 has blood type A and patient 2 has blood type B. Consider the following events:

- D1—a randomly chosen person can be a donor for patient 1.
- D2—a randomly chosen person can be a donor for patient 2.

We are interested in finding the probability that a randomly chosen person can be a donor for patient 1 or patient 2. In other words, we are interested in finding P(D1 or D2).

:::{quiz} Which blood types make up event D1 (can donate to patient 1, who has type A), and what is P(D1)?
:hint: Patient 1 can receive from types A and O.
:feedback-0: Correct! D1 = {A, O}, so P(D1) = 0.42 + 0.44 = 0.86.
:feedback-1: Type B cannot donate to a type A patient.
:feedback-2: Type AB can donate only to AB patients.
* *Types A and O; P(D1) = 0.86
* Types A, B, and O; P(D1) = 0.96
* Types A, AB, and O; P(D1) = 0.90
:::

:::{quiz} Are the events D1 = {A, O} and D2 = {B, O} disjoint?
:hint: Do the two events share any blood type?
:feedback-0: Both events include type O—a person with type O can donate to either patient.
:feedback-1: Correct! Type O belongs to both events, so D1 and D2 are not disjoint, and we cannot simply add their probabilities.
* Yes, they are disjoint
* *No—type O is in both events
:::

:::{quiz} What is the correct value of P(D1 or D2)—the probability that a random person can donate to patient 1 or patient 2?
:hint: D1 or D2 = {A, O, B}—every type except AB.
:feedback-0: Adding P(D1) + P(D2) = 0.86 + 0.54 = 1.40 double-counts type O and exceeds 1, which is impossible!
:feedback-1: Correct! The event "D1 or D2" consists of blood types A, B, and O, so its probability is 0.42 + 0.10 + 0.44 = 0.96 (equivalently, 1 − P(AB)).
:feedback-2: 0.86 is just P(D1); it leaves out the type B donors who can donate to patient 2.
* 1.40
* *0.96
* 0.86
:::

As we mentioned earlier, later on in this module we will establish a more general Addition Rule that applies even when two events are not disjoint.

```{admonition} Comment
:class: important

The Addition Rule for Disjoint Events can naturally be extended to more than two disjoint events. Let's take three, for example. If A, B and C are three disjoint events (three non-overlapping circles in the Venn diagram), then P(A or B or C) = P(A) + P(B) + P(C). The rule is the same for any number of disjoint events.
```

We are now done with the first version of the Addition Rule (the version restricted to disjoint events) and we are ready to move on to rule 5. As mentioned before, the general version of the Addition Rule will be presented after rule 5.
