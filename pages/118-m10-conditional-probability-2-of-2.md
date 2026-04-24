# Conditional Probability (2 of 2)

```{admonition} Learning Objectives
    - Explain the reasoning behind conditional probability, and how this reasoning is expressed by the definition of conditional probability.
    - Find conditional probabilities and interpret them.
```

A good visual illustration of this conditional probability is provided by the two-way table:

```{figure} images/image002.gif
:alt: The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500; In this table, the first row (Male) has been highlighted. The {Male, Pierced: 36} cell is in dark green, and the rest is in light green, showing that we can use this row to calculate the conditional probability.

The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500; In this table, the first row (Male) has been highlighted. The {Male, Pierced: 36} cell is in dark green, and the rest is in light green, showing that we can use this row to calculate the conditional probability.
```

which shows us that conditional probability is not very different from (and actually quite the same as) the conditional percents we calculated back in section 1.

## Did I Get This?

Consider the piercing example, where the following two-way table is given,

```{figure} images/dig001.gif
:alt: The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;

The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;
```

Recall also that M represents the event of being a male ("not M" represents being a female), and E represents the event of having one or both ears pierced.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Another way to visualize conditional probability is using a Venn diagram:

```{figure} images/image003.gif
:alt: A Venn Diagram, in which a large rectangle represents all of the sample space. There are two circles in the rectangle, labeled M (for Male) and E (for Ear Pierced). Circle M and circle E overlap (but not totally). P(M) = 180/500 = .36, so this is somewhat like the area of circle M. The overlap is the event M and E. P(M and E) = 36/500 = .072, which is also like the area of the overlap area.

A Venn Diagram, in which a large rectangle represents all of the sample space. There are two circles in the rectangle, labeled M (for Male) and E (for Ear Pierced). Circle M and circle E overlap (but not totally). P(M) = 180/500 = .36, so this is somewhat like the area of circle M. The overlap is the event M and E. P(M and E) = 36/500 = .072, which is also like the area of the overlap area.
```

In both the two-way table and the Venn diagram, the reduced sample space (comprised of only males) is shaded light green, and within this sample space, the event of interest (having ears pierced) is shaded darker green. The two-way table illustrates the idea via counts, while the Venn diagram converts the counts to probabilities, which are presented as regions rather than cells.

We may work with counts, as presented in the two-way table, to write

P(E | M) = 36/180.

Or we can work with probabilities, as presented in the Venn diagram, by writing

P(E | M) = (36/500) / (180/500).

We will want, however, to write our formal expression for conditional probabilities in terms of other, ordinary, probabilities and therefore the definition of conditional probability will grow out of the Venn diagram.

Notice that

P(E | M) = (36/500) / (180/500) = P(M and E) / P(M). Generalized, we have a formal definition of conditional probability:

```{admonition} Definition: conditional probability
    The *conditional probability of event B, given event A,* is *P(B | A) = P(A and B) / P(A)*
```

## Comments

1. Note that when we evaluate the conditional probability, we always divide by the probability of the given event. The probability of both goes in the numerator.

2. The above formula holds as long as P(A) > 0, since we cannot divide by 0. In other words, we should not seek the probability of an event given that an impossible event has occurred.

Let's see how we can use this formula in practice:

```{admonition} Example
    On the "Information for the Patient" label of a certain antidepressant, it is claimed that based on some clinical trials, there is a 14% chance of experiencing sleeping problems known as insomnia (denote this event by I), there is a 26% chance of experiencing headache (denote this event by *H*), and there is a 5% chance of experiencing both side effects (*I and H*).

    (a) Suppose that the patient experiences insomnia; what is the probability that the patient will also experience headache?

    Since we know (or it is given) that the patient experienced insomnia, we are looking for P(H | I). According to the definition of conditional probability:

    P(H | I) = P(H and I) / P(I) = .05/.14 = .357.

    (b) Suppose the drug induces headache in a patient; what is the probability that it also induces insomnia?

    Here, we are given that the patient experienced headache, so we are looking for P(I | H).

    Using the definition P(I | H) = P(I and H) / P(H) = .05/.26 = .1923.
```

## Comment

Note that the answers to (a) and (b) above are different. In general, P(A | B) does not equal P(B | A). We'll come back and illustrate this point later in this module.

The purpose of the following activity is to give you guided practice in using the definition of conditional probability, and teach you how the Complement Rule works with conditional probability.

## Learn By Doing

Recall the delivery services example:

It is vital that a certain document reach its destination within one day. To maximize the chances of on-time delivery, two copies of the document are sent using two services, service A and service B, and the following probability table summarizes the chances of on-time delivery:

```{figure} images/lbd001.gif
:alt: A table. The column headings are "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here is the cell data in "Row, Column: Value" format: A,B : .75; A, not B: .15; A, Total: .90; not A, B: .05; not A, not B: .05; not A, Total: .10; Total, B: .80; Total, not B: .20; Total, Total: 1.00;

A table. The column headings are "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here is the cell data in "Row, Column: Value" format: A,B : .75; A, not B: .15; A, Total: .90; not A, B: .05; not A, not B: .05; not A, Total: .10; Total, B: .80; Total, not B: .20; Total, Total: 1.00;
```

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

## Did I Get This?

Recall the smoke alarms example from the previous module. A homeowner has smoke alarms installed in the dining room (adjacent to the kitchen) and an upstairs bedroom (above the kitchen). The two-way table below shows probabilities of smoke in the kitchen triggering the alarm in the dining room (D) or not, and in the bedroom (B) or not. Use this two-way table to answer the following:

```{figure} images/dig002.gif
:alt: A table, in which the column headings are "B," "not B," and "Total." The rows are "D," "not D," and "Total." Here is the data in "Row,Column: Value" format: D, B: .38; D, not B: .57; D, Total: .95; not D, B: .02; not D, not B: .03; not D, Total: .05; Total, B: .40; Total, not B: .60; Total, Total: 1.00;

A table, in which the column headings are "B," "not B," and "Total." The rows are "D," "not D," and "Total." Here is the data in "Row,Column: Value" format: D, B: .38; D, not B: .57; D, Total: .95; not D, B: .02; not D, not B: .03; not D, Total: .05; Total, B: .40; Total, not B: .60; Total, Total: 1.00;
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
