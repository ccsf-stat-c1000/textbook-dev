# Probability Rules (11 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
    - When appropriate, use tools such as Venn diagrams or probability tables as aids for finding probabilities.
```

Now that we know how to build a two-way probability table, let's see how we can use information from it to solve problems.

```{admonition} Example
    Let's go back to our delivery example and see how we can "lift" probabilities from the two-way probability table in order to answer the question posed in that example and related questions. Here is the table again:

    ```{figure} images/image033.gif
    :alt: The table has 3 columns and 3 rows. The columns are: "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here is the cell data in "Row, Column: Value" format. A,B: 0.75; A,not B: .15; A,Total: .90; not A, B: .05; not A, not B: .05; not A, Total: .10; Total, B: .80; Total, not B: .20; Total, Total: 1.00

    The table has 3 columns and 3 rows. The columns are: "B," "not B," and "Total." The rows are "A," "not A," and "Total." Here is the cell data in "Row, Column: Value" format. A,B: 0.75; A,not B: .15; A,Total: .90; not A, B: .05; not A, not B: .05; not A, Total: .10; Total, B: .80; Total, not B: .20; Total, Total: 1.00
    ```

    What is the probability of on-time delivery of the document using the two services strategy?

    In other words, what is P(A or B)?

    We can use the table in two ways:

    (i) We can simply lift P(A), P(B) and P(A and B) from the table as shown in the table below and use the General Addition Rule to get 0.95. as we did before: P(A or B) = P(A) + P(B) − P(A and B) = 0.90 + 0.80 − 0.75 = 0.95.

    ```{figure} images/image034.gif
    :alt: Cells are given in "{Row,Column: Value}" format. The same table as the previous, except that the cells {A,B: 0.75}, {A, Total: 0.90}, and {Total, B: 0.80} have been highlighted.

    Cells are given in "{Row,Column: Value}" format. The same table as the previous, except that the cells {A,B: 0.75}, {A, Total: 0.90}, and {Total, B: 0.80} have been highlighted.
    ```

    (ii) Another way to use the table is to use the fact that in probability, "A or B" actually means "A or B or both." The corresponding cells for these three options are shaded below and are 0.15 (only A), 0.05 (only B), and 0.75 (both). We can add these up to get P(A or B) = 0.95.

    ```{figure} images/image035.gif
    :alt: Cells are given in "{Row,Column}" format. The same table as the previous, except that the cells {A,B: 0.75}, {A, not B: 0.15}, and {not A, B: 0.05} have been highlighted.

    Cells are given in "{Row,Column}" format. The same table as the previous, except that the cells {A,B: 0.75}, {A, not B: 0.15}, and {not A, B: 0.05} have been highlighted.
    ```
```

```{admonition} Example
    What is the probability of on-time delivery by exactly one service?

    On-time delivery by exactly one service occurs if the document arrives on-time by service A and not B, or by service B and not A. The probabilities of these two possibilities are represented by the shaded cells in the table below, and are 0.15 and 0.05 respectively. Therefore, P(on-time delivery by exactly one service) = 0.15 + 0.05 = 0.20

    ```{figure} images/image036.gif
    :alt: Cells are given in "{Row,Column}" format. The same table as the previous, except that the cells {A, not B: 0.15} and {not A, B: 0.05} have been highlighted.

    Cells are given in "{Row,Column}" format. The same table as the previous, except that the cells {A, not B: 0.15} and {not A, B: 0.05} have been highlighted.
    ```
```

```{admonition} Example
    What is the probability that the document will *not* get to its destination on time? This would be the occurrence of the event "not A and not B," whose probability is 0.05, as shown in the table:

    ```{figure} images/image037.gif
    :alt: Cells are given in "{Row,Column}" format. The same table as the previous, except that the cell {not A, not B: 0.05} has been highlighted.

    Cells are given in "{Row,Column}" format. The same table as the previous, except that the cell {not A, not B: 0.05} has been highlighted.
    ```
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

We are now done with this section, which introduced various probability rules. Let's summarize what we've learned.

1. The Complement Rule states that

*P(not A) = 1 − P(A)*

or when rearranged

*P(A) = 1 − P(not A).*

The Complement Rule is very useful when we need to find probabilities of the sort: P(At least one of several events occur) which is hard to calculate. In this case, we apply the Complement Rule:

*P(At least one of several events occur) = 1 − P(None of the events occur)*, since P(None of the events occur) is usually much easier to find.

2. The General Addition Rule states that for any two events,

*P(A or B) = P(A) + P(B) − P(A and B),*

where, by P(A or B) we mean P(A occurs or B occurs or both).

In the special case when A and B are *disjoint* events (which means that P(A and B) = 0), the general addition rule becomes P(A or B) = P(A) + P(B), which we call the Addition Rule for Disjoint Events.

Beware of wrongly using the Addition Rule for Disjoint events when the events are not disjoint.

3. When we want to find P(A and B), we can use the Multiplication Rule, but so far we've only learned the restricted version of this rule—the Multiplication Rule for Independent Events. Events are independent if the occurrence of one of the events has no effect on the probability of the other occurring, in which case:

*P(A and B) = P(A) * P(B).*

4. The Additional Rule for Disjoint Events can be naturally extended to more than two events. In other words, if events A, B, and C are disjoint, then

P(A or B or C)=P(A)+P(B)+P(C).

Similarly, the Multiplication Rule for Independent Events can be naturally extended to more than two independent events. In other words, if events A, B, and C are independent, then P(A and B and C) = P(A) * P(B) * P(C). The same is true for 4, 5, ..., disjoint/independent events.

5. When there are two categorical variables in the background, each with two possible values, a *two-way probability table* is a quick and easy way to display the probabilities associated with the 4 possible combinations.
