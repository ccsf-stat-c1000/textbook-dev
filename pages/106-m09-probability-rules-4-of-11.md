# Probability Rules (4 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

```{admonition} Rule 4: The Addition Rule for Disjoint Events
    *The Addition Rule for Disjoint Events: If A and B are disjoint events, then P(A or B) = P(A) + P(B).*
```

## Comment

When dealing with probabilities, the word "or" will always be associated with the operation of addition; hence the name of this rule, "The Addition Rule."

```{admonition} Example
    Recall the blood type example:

    ```{figure} images/image011.gif
    :alt: Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;

    Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;
    ```

    Here is some additional information:

    * A person with type *A* can donate blood to a person with type *A* or *AB.*

    * A person with type *B* can donate blood to a person with type *B* or *AB.*

    * A person with type *AB* can donate blood to a person with type *AB* only.

    * A person with type *O* blood can donate to anyone.

    What is the probability that a randomly chosen person is a potential donor for a person with blood type A?

    From the information given, we know that being a potential donor for a person with blood type A means having blood type A or O. We therefore need to find P(A or O). Since the events A and O are disjoint, we can use the addition rule for disjoint events to get: P(A or O) = P(A) + P(O) = .42 + .44 = .86. It is easy to see why adding the probability actually makes sense. If 42% of the population has blood type A and 44% of the population has blood type O, then 42% + 44% = 86% of the population has either blood type A or O, and thus are potential donors to a person with blood type A. This reasoning about why the addition rule makes sense can be visualized using the pie chart below:

    ```{figure} images/image017a.gif
    :alt: A pie chart titled "Blood Types." Type A takes up 42% of the pie chart, and type O takes up 44%. Together, as A or O, they take up 86% of the pie chart.

    A pie chart titled "Blood Types." Type A takes up 42% of the pie chart, and type O takes up 44%. Together, as A or O, they take up 86% of the pie chart.
    ```
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Learn By Doing

So far we have introduced the addition rule for the special case in which the events being considered are disjoint. The purpose of this activity is to make you aware of the danger in wrongly using the addition rule for disjoint events in cases where the events are actually not disjoint. Consider the blood type example again.

Recall the blood type example:

```{figure} images/lbd004.gif
:alt: Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;

Data given in "Blood Type: Probability" Format: O: 0.44; A: 0.42; B: 0.10; AB: 0.04;
```

with the following additional information:

A person with type *A* can donate blood to a person with type *A* or *AB*.

A person with type *B* can donate blood to a person with type *B* or *AB*.

A person with type *AB* can donate blood to a person with type *AB* only.

A person with type *O* blood can donate to anyone.

Suppose that there are two patients who are each in need of a blood donation. Patient 1 has blood type A and patient 2 has blood type B. Consider the following events:

D1—a randomly chosen person can be a donor for patient 1.

D2—a randomly chosen person can be a donor for patient 2.

We are interested in finding the probability that a randomly chosen person can be a donor for patient 1 or patient 2. In other words, we are interested in finding P(D1 or D2).

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

As we mentioned earlier, later on in this module we will establish a more general Addition Rule that applies even when two events are not disjoint.

## Comment

The Addition Rule for Disjoint Events can naturally be extended to more than two disjoint events. Let's take three, for example. If A, B and C are three disjoint events,

```{figure} images/image018.gif
:alt: A Venn Diagram showing 3 disjoint events. As usual there is a gray box showing the entire sample space. Inside this gray box are three completely separate circles. The first circle is for the occurrences in A, the second for occurrences in B, and the third for occurrences in C.

A Venn Diagram showing 3 disjoint events. As usual there is a gray box showing the entire sample space. Inside this gray box are three completely separate circles. The first circle is for the occurrences in A, the second for occurrences in B, and the third for occurrences in C.
```

then P(A or B or C) = P(A) + P(B) + P(C). The rule is the same for any number of disjoint events.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

We are now done with the first version of the Addition Rule (the version restricted to disjoint events) and we are ready to move on to rule 5. As mentioned before, the general version of the Addition Rule will be presented after rule 5.
