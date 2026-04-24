# Probability Rules (3 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

We are now moving to rule 4, which deals with another situation of frequent interest, finding P(A *or* B), the probability of one event *or* another occurring. Before we get to the actual rule, however, we need some clarifications and definitions.

When a parent says to his or her child in a toy store "Do you want toy A or toy B?", this means that the child is going to get only one toy and he or she has to choose between them. Getting both toys is usually not an option.

In contrast,

*In probability, "OR" means either one or the other or both.*

and so,

*P(A or B) = P(event A occurs or event B occurs or both occur)*

Having said that, it should be noted that there are some cases where it is simply impossible for the two events to both occur at the same time, in which case we don't have to worry about the possibility that both occur when we try to find P(A or B). The distinction between events that can happen together and those that cannot is an important one.

Here are two examples:

```{admonition} Example
    Consider the following two events:

    A—a randomly chosen person has blood type A, and

    B—a randomly chosen person has blood type B.

    In rare cases, it is possible for a person to have more than one type of blood flowing through his or her veins, but for our purposes, we are going to assume that each person can have only one blood type. Therefore, it is impossible for the events A and B to occur together.

    On the other hand ...
```

```{admonition} Example
    Consider the following two events:

    A—a randomly chosen person has blood type A

    B—a randomly chosen person is a woman.

    In this case, it *is possible* for events A and B to occur together.

    *Definition:* Two events that cannot occur at the same time are called *disjoint* or *mutually exclusive.* (We will use disjoint.)

    We can therefore say that in the first example events A and B are disjoint, and in the second example they are not disjoint. Using Venn diagrams, we can visualize two events that are disjoint and compare them to two events that are not:

    ```{figure} images/image015.gif
    :alt: A Venn diagram titled "A and B are Disjoint." The entire sample space is represented as a rectangle. Inside the rectangle are two separate circles. One circle represents the events in A and the other represents the events in B.

    A Venn diagram titled "A and B are Disjoint." The entire sample space is represented as a rectangle. Inside the rectangle are two separate circles. One circle represents the events in A and the other represents the events in B.
    ```

    ```{figure} images/image016.gif
    :alt: A Venn diagram titled "A and B are NOT Disjoint." The entire sample space is represented as a rectangle. Inside the rectangle are two circles. One circle represents the occurrences in A and the other represents the occurrences in B. These two are not disjoint, so the two circles partially overlap each other. (Being NOT disjoint, two circles could overlap each other completely, but in this example they do not.)

    A Venn diagram titled "A and B are NOT Disjoint." The entire sample space is represented as a rectangle. Inside the rectangle are two circles. One circle represents the occurrences in A and the other represents the occurrences in B. These two are not disjoint, so the two circles partially overlap each other. (Being NOT disjoint, two circles could overlap each other completely, but in this example they do not.)
    ```
```

The Venn diagrams suggest that another way to think about disjoint versus not disjoint events is that disjoint events *do not overlap*. They do not share any of the possible outcomes, and therefore cannot happen together. On the other hand, events that are not disjoint are overlapping in the sense that they share some of the possible outcomes and therefore can occur at the same time.

The purpose of the following activity is to strengthen your intuition and understanding about disjoint versus not disjoint events.

## Learn By Doing

Recall the couple that is planning to have 3 children, where the sample space S of all possible outcomes is:

S={BBB, BBG, BGB, GBB, GGB, GBG, BGG, GGG}

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

Now that we understand the idea of disjoint events, we can finally get to rule 4. Rule 4 actually has two versions, one for finding P(A or B) in the special case when events A and B are disjoint, and a more general version for when the events are not necessarily disjoint. We will first present the version of rule 4 that is restricted to disjoint events, and later in the module (after rule 5) we will revisit rule 4 and present the more general version.
