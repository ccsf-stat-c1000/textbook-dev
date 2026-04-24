# Conditional Probability (1 of 2)

```{admonition} Learning Objectives
    - Explain the reasoning behind conditional probability, and how this reasoning is expressed by the definition of conditional probability.
    - Find conditional probabilities and interpret them.
```

In the first part of this module, we'll introduce the concept of conditional probability. The idea here is that the probabilities of certain events may be affected by whether or not other events have occurred. Let's illustrate this idea with a simple example:

```{admonition} Example
    All the students in a certain high school were surveyed, then classified according to gender and whether they had either of their ears pierced:

    ```{figure} images/image001.gif
    :alt: A table of the data. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;

    A table of the data. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;
    ```

    (Note that this is a two-way table of counts that was first introduced when we talked about the relationship between two categorical variables. It is not surprising that we are using it again in this example, since we indeed have two categorical variables here: *Gender:* M or F (in our notation, "not M"), and *Pierced:* Yes or No)

    Suppose a student is selected at random from the school. Let *M* and *not M* denote the events of being male and female, respectively, and *E* and *not E* denote the events of having ears pierced or not, respectively. We'll start by asking what will seem like simple questions, and we'll build our way to conditional probability:

    1. What is the probability that the student has one or both ears pierced? Since a student is chosen at random from the group of 500 students, out of which 324 are
                                                      pierced, P(E) = 324/500 = .648
    2. What is the probability that the student is male? Since a student is chosen at random from the group of 500 students, out of which 180 are
                                                      male, P(M) = 180/500 = .36
    3. What is the probability that the student is male and has ear(s) pierced? Since a student is chosen at random from the group of 500 students out of which 36 are male and
                                                      have their ear(s) pierced, P(M and E) = 36/500 =
                                                      .072 Now something new:
    4. *Given* that the student that was chosen is
                                                      male, what is the probability that he has one or
                                                      both ears pierced? At this point, new notation is required, to express the probability of a certain event given
                            that another event holds. We will write "the probability of having one or
                            both ears pierced (E) , given that a student is male (M)" as *P(E |
                                M).*

    A word about this new notation: The event whose probability we seek (in this case E) is written first, the vertical line stands for the word "given" or "conditioned on," and the event that is given (in this case M) is written after the "|" sign.

    We call this probability the *conditional probability* of having one or both ears pierced, given that a student is male: it assesses the probability of having pierced ears under the condition of being male. Now to solve for the probability, we observe that choosing from only the males in the school essentially alters the sample space S from all students in the school to all male students in the school. The total number of possible outcomes is no longer 500, but has changed to 180. Out of those 180 males, 36 have ear(s) pierced, and thus:

    P(E | M) = 36/180 = .20.
```
