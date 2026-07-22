# Disjoint Events: When Two Things Can't Both Happen

We are now moving to rule 4, which deals with another situation of frequent interest, finding P(A *or* B), the probability of one event *or* another occurring. Before we get to the actual rule, however, we need some clarifications and definitions.

When a parent says to his or her child in a toy store "Do you want toy A or toy B?", this means that the child is going to get only one toy and he or she has to choose between them. Getting both toys is usually not an option.

In contrast,

*In probability, "OR" means either one or the other or both.*

and so,

*P(A or B) = P(event A occurs or event B occurs or both occur)*

Having said that, it should be noted that there are some cases where it is simply impossible for the two events to both occur at the same time, in which case we don't have to worry about the possibility that both occur when we try to find P(A or B). The distinction between events that can happen together and those that cannot is an important one.

Here are two examples:

:::{admonition} Example: Disjoint Events
:class: tip

Consider the following two events:

- A—a randomly chosen person has blood type A, and
- B—a randomly chosen person has blood type B.

In rare cases, it is possible for a person to have more than one type of blood flowing through his or her veins, but for our purposes, we are going to assume that each person can have only one blood type. Therefore, it is impossible for the events A and B to occur together.
:::

:::{admonition} Example: Events That Are Not Disjoint
:class: tip

Consider the following two events:

- A—a randomly chosen person has blood type A
- B—a randomly chosen person is a woman.

In this case, it *is possible* for events A and B to occur together.
:::

*Definition:* Two events that cannot occur at the same time are called {term}`disjoint <disjoint events>` or {term}`mutually exclusive <disjoint events>`. (We will use disjoint.)

We can therefore say that in the first example events A and B are disjoint, and in the second example they are not disjoint. Using Venn diagrams, we can visualize two events that are disjoint and compare them to two events that are not:

```{figure} images/gen/m09-disjoint-venn.svg
:alt: Two Venn diagrams side by side. In the first, labeled A and B are disjoint, the two circles are completely separate, so the events cannot occur together. In the second, labeled A and B are not disjoint, the two circles partially overlap, so the events can occur at the same time.
```

The Venn diagrams suggest that another way to think about disjoint versus not disjoint events is that disjoint events *do not overlap*. They do not share any of the possible outcomes, and therefore cannot happen together. On the other hand, events that are not disjoint are overlapping in the sense that they share some of the possible outcomes and therefore can occur at the same time.

The purpose of the following activity is to strengthen your intuition and understanding about disjoint versus not disjoint events.

## Check Your Understanding: Disjoint Events

Recall the couple that is planning to have 3 children, where the sample space S of all possible outcomes is:

S = {BBB, BBG, BGB, GBB, GGB, GBG, BGG, GGG}

:::{quiz} Consider the events A: "the couple has at most one girl" and B: "the couple has 3 girls." Are these events disjoint?
:hint: List the outcomes in each event and check for overlap. A = {BBB, BBG, BGB, GBB}; B = {GGG}.
:feedback-0: Correct! A contains outcomes with zero or one girl, while B is GGG—they share no outcomes, so they cannot occur together.
:feedback-1: Check again: no outcome has both at most one girl and three girls.
* *Yes—they share no outcomes, so they are disjoint
* No—they can occur together
:::

:::{quiz} Now consider events C: "the first child is a boy" and D: "the couple has exactly one girl." Are these events disjoint?
:hint: C = {BBB, BBG, BGB, BGG}; D = {BBG, BGB, GBB}. Do they share any outcomes?
:feedback-0: The two events do share outcomes—look at BBG and BGB.
:feedback-1: Correct! The outcomes BBG and BGB are in both events, so C and D can occur together—they are not disjoint.
* Yes—they are disjoint
* *No—they share the outcomes BBG and BGB, so they are not disjoint
:::

:::{quiz} Which of the following pairs of events is ALWAYS disjoint, for any event A?
:hint: Think of an event and its complement.
:feedback-0: Correct! An event and its complement can never occur together (and together they cover all of S).
:feedback-1: Two different events can easily overlap—like "type A blood" and "is a woman."
:feedback-2: An event always overlaps with itself.
* *A and "not A"
* Any two different events
* A and A
:::

Now that we understand the idea of disjoint events, we can finally get to rule 4. Rule 4 actually has two versions, one for finding P(A or B) in the special case when events A and B are disjoint, and a more general version for when the events are not necessarily disjoint. We will first present the version of rule 4 that is restricted to disjoint events, and later in the module (after rule 5) we will revisit rule 4 and present the more general version.
