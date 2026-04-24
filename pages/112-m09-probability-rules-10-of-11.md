# Probability Rules (10 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
    - When appropriate, use tools such as Venn diagrams or probability tables as aids for finding probabilities.
```

In our delivery example, there are two categorical variables of interest in the background:

- On-time delivery by service A (yes/no)
- On-time delivery by service B (yes/no)

Since each of the two has two possible values (yes/no), there are four possible combinations altogether, which correspond to the four possible outcomes of using the two services.

While the Venn diagrams were great to visualize the General Addition Rule, in cases like these it is much easier to display the information in and work with a two-way table of probabilities, much as we examined the relationship between two categorical variables in the Exploratory Data Analysis section.

How do we build a two-way table of probabilities? Let's use our delivery example to illustrate this simple process:

```{note} Video
[Probability Rules](https://www.youtube.com/watch?v=aN0eulm19MM)
```

Now that we’ve completed the table, it is important to understand what each of the table’s entries mean in context.

```{figure} images/prob_table_explained.png
:alt: The table has columns "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here are is some information about the table, organized by cell: At the cell A,B, the value there (0.75) is P(A and B) = P(on-time delivery by both services). At the cell A,not B, the value there (0.15) is P(A and Not B) = P(on-time delivery ONLY by service A). At cell Not A and B, the value (0.05) is P(not A and B) = P(on-time delivery ONLY by service B). At cell Not A and Not B, the value (0.05) is P(not A and not B) = P(Neither service A nor B delivered on time).

The table has columns "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here are is some information about the table, organized by cell: At the cell A,B, the value there (0.75) is P(A and B) = P(on-time delivery by both services). At the cell A,not B, the value there (0.15) is P(A and Not B) = P(on-time delivery ONLY by service A). At cell Not A and B, the value (0.05) is P(not A and B) = P(on-time delivery ONLY by service B). At cell Not A and Not B, the value (0.05) is P(not A and not B) = P(Neither service A nor B delivered on time).
```

## Comment

A common mistake is to confuse between: P(A) = P(event A occurs) and P(A and Not B) = P(ONLY event A occurs)[and similarly, between P(B) = P(event B occurs) and P(Not A and B) = P(only event B occurs)].

Looking at the probability table is a great way to clear-up this confusion:

```{figure} images/prob_table.png
:alt: The table's first row has been highlighted. Here is the highlighted data in "Row, Column" format: A, B: P(A and B) = 0.75; A, not B: P(A and not B) = 0.15; A, Total: P(A) = 0.90 = P(A and B) + P(A and not B)

The table's first row has been highlighted. Here is the highlighted data in "Row, Column" format: A, B: P(A and B) = 0.75; A, not B: P(A and not B) = 0.15; A, Total: P(A) = 0.90 = P(A and B) + P(A and not B)
```

P(A) = 0.90 means that in 90% of the cases when service A is used, it delivers the document on time.

These cases of on-time delivery by service A can be decomposed into two sub-cases:

- P(A and B) = 0.75 → 75% of the time the document is delivered on time also
                        by service B (i.e., the document is delivered on time by both services)
- P(A and Not B) = 0.15 → 15% of the time the document is not delivered on
                        time by service B (i.e., delivered on time only by service A).

Similarly,

```{figure} images/prob_table2.png
:alt: The table's first column has been highlighted. Here is the highlighted data in "Row, Column" format: A,B: P(A and B) = 0.75; not A, B: P(not A and B) = 0.05; B,Total: P(B) = 0.80 = P(A and B) + P(not A and B)

The table's first column has been highlighted. Here is the highlighted data in "Row, Column" format: A,B: P(A and B) = 0.75; not A, B: P(not A and B) = 0.05; B,Total: P(B) = 0.80 = P(A and B) + P(not A and B)
```

P(B) = 0.80 means that in 80% of the cases when service B is used, it delivers the document on time.

These cases of on-time delivery by service B can be decomposed into two sub-cases:

- P(A and B) = 0.75 → 75% of the time the document is delivered on time also
                        by service A (i.e., the document is delivered on time by both services)
- P(Not A and B) = 0.05 → 5% of the time the document is not delivered on
                        time by service A (i.e., delivered on time *only by service
                            B* ).

```{admonition} Example
    Recall the smoke detector example from the last activity. Here is a quick recap:

    D—the dining room alarm is set off by smoke in the kitchen

    B—the bedroom alarm is set off by smoke in the kitchen

    P(D) = 0.95

    P(B) = 0.40

    D and B are independent → P(D and B) = 0.38

    Complete the table below. Start with the information that is given and go from there.
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

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

In both the delivery problem and the smoke detector problem, we knew P(A), P(B) and P(A and B). (In the smoke detector problem, we actually needed to work a bit to get P(A and B), but it wasn't too bad.) Visually, we had the probability for the three shaded cells below, which was enough information to complete the table.

```{figure} images/image031.gif
:alt: The table has columns "B," "not B," and "Total." The rows are "A," "not A," and "Total." We will be naming cells by "{Row, Column}" notation. Cells {A,B}, {A, Total}, and {Total, B} have been shaded.

The table has columns "B," "not B," and "Total." The rows are "A," "not A," and "Total." We will be naming cells by "{Row, Column}" notation. Cells {A,B}, {A, Total}, and {Total, B} have been shaded.
```

This, however, is not the only combination of three cells that would provide sufficient information to complete the table. Essentially, as long as we are given (or can calculate) one cell in each of the margins (the total row and column), and one of the four cells in the body of the table, we'll be able to complete the entire table. Visually, we need:

```{figure} images/image032.gif
:alt: The same table. We need information about one of the cells in the body of the table. These cells are {A,B}, {A, not B}, {not A, B}, and {not A, not B}. In addition, we need information from one of the cells on the right margin. These cells are {A, Total} and {not A, Total}. The last group of cells we need information from is the bottom margin. These cells are {Total, B} and {Total, not B}. With one cell from each of these three groups we can fill in the entire table.

The same table. We need information about one of the cells in the body of the table. These cells are {A,B}, {A, not B}, {not A, B}, and {not A, not B}. In addition, we need information from one of the cells on the right margin. These cells are {A, Total} and {not A, Total}. The last group of cells we need information from is the bottom margin. These cells are {Total, B} and {Total, not B}. With one cell from each of these three groups we can fill in the entire table.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

According to www.jointogether.com, in 2000, 87% of all suicides were committed by males, 56% of all suicides were committed using a gun, and 10% of all suicides were committed by women not using a gun.

(We'll use M for suicide committed by a male, F [= not M] for suicide committed by female, and G for a suicide committed using a gun.)

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

When we used two-way tables in the Exploratory Data Analysis (EDA) section, it was to record values of two categorical variables for a concrete *sample* of individuals. In contrast, the information in a probability two-way table is for an entire *population*, and the values are rather abstract. If we had treated something like the delivery example in the EDA section, we would have recorded the actual numbers of on-time (and not-on-time) deliveries for samples of documents mailed with service A or B. In this section, the long-term probabilities are presented as being known. Presumably, those probabilities were based on relative frequencies recorded over many repetitions.
