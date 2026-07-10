# Conditional Probability (2 of 2)

```{admonition} Learning Objectives
:class: note

- Explain the reasoning behind conditional probability, and how this reasoning is expressed by the definition of conditional probability.
- Find conditional probabilities and interpret them.
```

A good visual illustration of this conditional probability is provided by the two-way table:

| | Pierced | Not Pierced | Total |
| --- | --- | --- | --- |
| **Male** | **36** | *144* | *180* |
| Female | 288 | 32 | 320 |
| Total | 324 | 176 | 500 |

Restricting attention to the Male row (the reduced sample space of 180 males), the 36 pierced males give P(E | M) = 36/180 = 0.20. This shows us that conditional probability is not very different from (and actually quite the same as) the conditional percents we calculated back in the Exploratory Data Analysis unit.

Another way to visualize conditional probability is using a Venn diagram:

```{figure} images/gen/m10-conditional-venn.svg
:alt: A Venn diagram with overlapping circles M and E inside the sample space of all 500 students. The M circle is shaded light green with probability 0.36, and its overlap with E is shaded dark green with probability 0.072. The conditional probability of E given M is the dark region as a fraction of the whole M circle: 0.072 divided by 0.36 equals 0.20.
```

In both the two-way table and the Venn diagram, the reduced sample space (comprised of only males) is shaded light green, and within this sample space, the event of interest (having ears pierced) is shaded darker green. The two-way table illustrates the idea via counts, while the Venn diagram converts the counts to probabilities, which are presented as regions rather than cells.

We may work with counts, as presented in the two-way table, to write

P(E | M) = 36/180.

Or we can work with probabilities, as presented in the Venn diagram, by writing

P(E | M) = (36/500) / (180/500).

We will want, however, to write our formal expression for conditional probabilities in terms of other, ordinary, probabilities, and therefore the definition of conditional probability will grow out of the Venn diagram.

Notice that

P(E | M) = (36/500) / (180/500) = P(M and E) / P(M). Generalized, we have a formal definition of conditional probability:

```{admonition} Definition: Conditional Probability
:class: note

The *conditional probability of event B, given event A,* is

$$P(B | A) = \frac{P(A \text{ and } B)}{P(A)}$$
```

## Comments

1. Note that when we evaluate the conditional probability, we always divide by the probability of the given event. The probability of both goes in the numerator.
2. The above formula holds as long as P(A) > 0, since we cannot divide by 0. In other words, we should not seek the probability of an event given that an impossible event has occurred.

Let's see how we can use this formula in practice:

:::{admonition} Example: Side Effects
:class: tip

On the "Information for the Patient" label of a certain antidepressant, it is claimed that based on some clinical trials, there is a 14% chance of experiencing sleeping problems known as insomnia (denote this event by I), there is a 26% chance of experiencing headache (denote this event by *H*), and there is a 5% chance of experiencing both side effects (*I and H*).

(a) Suppose that the patient experiences insomnia; what is the probability that the patient will also experience headache?

Since we know (or it is given) that the patient experienced insomnia, we are looking for P(H | I). According to the definition of conditional probability:

P(H | I) = P(H and I) / P(I) = 0.05/0.14 = 0.357.

(b) Suppose the drug induces headache in a patient; what is the probability that it also induces insomnia?

Here, we are given that the patient experienced headache, so we are looking for P(I | H).

Using the definition: P(I | H) = P(I and H) / P(H) = 0.05/0.26 = 0.1923.
:::

## Comment

Note that the answers to (a) and (b) above are different. In general, P(A | B) does not equal P(B | A). We'll come back and illustrate this point later in this module.

The purpose of the following activity is to give you guided practice in using the definition of conditional probability, and teach you how the Complement Rule works with conditional probability.

## Learn By Doing

Recall the delivery services example, with the following probability table:

| | B | not B | Total |
| --- | --- | --- | --- |
| **A** | 0.75 | 0.15 | 0.90 |
| **not A** | 0.05 | 0.05 | 0.10 |
| **Total** | 0.80 | 0.20 | 1.00 |

:::{quiz} Given that service B delivered the document on time, what is the probability that service A also delivered it on time—P(A | B)?
:hint: P(A | B) = P(A and B) / P(B).
:feedback-0: Correct! P(A | B) = 0.75 / 0.80 = 0.9375.
:feedback-1: 0.75 is P(A and B); you must divide by the probability of the given event, P(B).
:feedback-2: 0.833 comes from dividing by P(A) = 0.90—but the given event is B, so divide by P(B) = 0.80.
* *0.9375
* 0.75
* 0.833
:::

:::{quiz} Given that service A did NOT deliver on time, what is the probability that service B delivered on time—P(B | not A)?
:hint: Restrict attention to the "not A" row, which has total probability 0.10.
:feedback-0: Correct! P(B | not A) = P(not A and B) / P(not A) = 0.05 / 0.10 = 0.5.
:feedback-1: 0.05 is the joint probability P(not A and B); divide it by P(not A).
:feedback-2: 0.80 is the unconditional P(B); the condition "not A" changes the picture considerably.
* *0.5
* 0.05
* 0.80
:::

:::{quiz} Complement rule with conditioning: what is P(not B | not A)?
:hint: Given the same condition, conditional probabilities of B and not B still sum to 1.
:feedback-0: Correct! P(not B | not A) = 1 − P(B | not A) = 1 − 0.5 = 0.5. (Equivalently, 0.05/0.10.)
:feedback-1: 0.95 is 1 minus the joint probability, not 1 minus the conditional probability.
:feedback-2: 0.20 is the unconditional P(not B).
* *0.5
* 0.95
* 0.20
:::

## Did I Get This?

Recall the smoke alarms example from the previous module. A homeowner has smoke alarms installed in the dining room (adjacent to the kitchen) and an upstairs bedroom (above the kitchen). The two-way table below shows probabilities of smoke in the kitchen triggering the alarm in the dining room (D) or not, and in the bedroom (B) or not:

| | B | not B | Total |
| --- | --- | --- | --- |
| **D** | 0.38 | 0.57 | 0.95 |
| **not D** | 0.02 | 0.03 | 0.05 |
| **Total** | 0.40 | 0.60 | 1.00 |

:::{quiz} Given that the bedroom alarm went off, what is the probability that the dining room alarm also went off—P(D | B)?
:hint: P(D | B) = P(D and B) / P(B).
:feedback-0: Correct! P(D | B) = 0.38 / 0.40 = 0.95—which equals P(D), as expected, since the alarms operate independently.
:feedback-1: 0.38 is the joint probability; divide by P(B) = 0.40.
:feedback-2: 0.40 is P(B) itself.
* *0.95
* 0.38
* 0.40
:::
