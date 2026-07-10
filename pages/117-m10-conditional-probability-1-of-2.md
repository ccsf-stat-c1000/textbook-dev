# Conditional Probability (1 of 2)

```{admonition} Learning Objectives
:class: note

- Explain the reasoning behind conditional probability, and how this reasoning is expressed by the definition of conditional probability.
- Find conditional probabilities and interpret them.
```

In the first part of this module, we'll introduce the concept of conditional probability. The idea here is that the probabilities of certain events may be affected by whether or not other events have occurred. Let's illustrate this idea with a simple example:

:::{admonition} Example: Pierced Ears
:class: tip

All the students in a certain high school were surveyed, then classified according to gender and whether they had either of their ears pierced:

| | Pierced | Not Pierced | Total |
| --- | --- | --- | --- |
| Male | 36 | 144 | 180 |
| Female | 288 | 32 | 320 |
| **Total** | **324** | **176** | **500** |

(Note that this is a two-way table of counts that was first introduced when we talked about the relationship between two categorical variables. It is not surprising that we are using it again in this example, since we indeed have two categorical variables here: *Gender:* M or F (in our notation, "not M"), and *Pierced:* Yes or No.)

Suppose a student is selected at random from the school. Let *M* and *not M* denote the events of being male and female, respectively, and *E* and *not E* denote the events of having ears pierced or not, respectively. We'll start by asking what will seem like simple questions, and we'll build our way to conditional probability:

1. What is the probability that the student has one or both ears pierced? Since a student is chosen at random from the group of 500 students, out of which 324 are pierced, P(E) = 324/500 = 0.648.

2. What is the probability that the student is male? Since a student is chosen at random from the group of 500 students, out of which 180 are male, P(M) = 180/500 = 0.36.

3. What is the probability that the student is male and has ear(s) pierced? Since a student is chosen at random from the group of 500 students, out of which 36 are male and have their ear(s) pierced, P(M and E) = 36/500 = 0.072.

Now something new:

4. *Given* that the student that was chosen is male, what is the probability that he has one or both ears pierced?

At this point, new notation is required, to express the probability of a certain event given that another event holds. We will write "the probability of having one or both ears pierced (E), given that a student is male (M)" as *P(E | M).*

A word about this new notation: The event whose probability we seek (in this case E) is written first, the vertical line stands for the word "given" or "conditioned on," and the event that is given (in this case M) is written after the "|" sign.

We call this probability the *conditional probability* of having one or both ears pierced, given that a student is male: it assesses the probability of having pierced ears under the condition of being male. Now to solve for the probability, we observe that choosing from only the males in the school essentially alters the sample space S from all students in the school to all male students in the school. The total number of possible outcomes is no longer 500, but has changed to 180. Out of those 180 males, 36 have ear(s) pierced, and thus:

P(E | M) = 36/180 = 0.20.
:::

## Concept Check

:::{quiz} Using the same table, what is P(E | not M)—the probability that a randomly chosen female student has pierced ears?
:hint: Restrict the sample space to the 320 female students.
:feedback-0: Correct! Among the 320 females, 288 have pierced ears: P(E | not M) = 288/320 = 0.9.
:feedback-1: 0.648 is P(E), the overall proportion of pierced ears among all 500 students.
:feedback-2: 288/500 = 0.576 is P(female and pierced), not the conditional probability given female.
* *0.9
* 0.648
* 0.576
:::

:::{quiz} Compare P(E) = 0.648 with P(E | M) = 0.20. What does this comparison tell us?
:hint: Does knowing the student is male change the probability of pierced ears?
:feedback-0: Correct! Knowing the student is male sharply lowers the probability of pierced ears, so the events E and M are dependent (not independent).
:feedback-1: If they were independent, the conditional probability would equal the unconditional one—but 0.20 is far from 0.648.
:feedback-2: The comparison tells us a great deal: it reveals the relationship between gender and pierced ears.
* *Gender and pierced ears are related—knowing the gender changes the probability
* The events E and M are independent
* Nothing—the two probabilities answer unrelated questions
:::
