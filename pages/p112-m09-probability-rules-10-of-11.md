# Probability Tables: Organizing the Possibilities

In our delivery example, there are two categorical variables of interest in the background:

- On-time delivery by service A (yes/no)
- On-time delivery by service B (yes/no)

Since each of the two has two possible values (yes/no), there are four possible combinations altogether, which correspond to the four possible outcomes of using the two services.

While the Venn diagrams were great to visualize the General Addition Rule, in cases like these it is much easier to display the information in, and work with, a two-way table of probabilities, much as we examined the relationship between two categorical variables in the Exploratory Data Analysis section.

How do we build a two-way table of probabilities? Let's use our delivery example to illustrate this simple process:

```{note} Video

[Probability Rules](https://www.youtube.com/watch?v=aN0eulm19MM)
```

Here is the completed table for the delivery example:

| | B | not B | Total |
| --- | --- | --- | --- |
| **A** | 0.75 | 0.15 | 0.90 |
| **not A** | 0.05 | 0.05 | 0.10 |
| **Total** | 0.80 | 0.20 | 1.00 |

Now that we've completed the table, it is important to understand what each of the table's entries means in context:

- P(A and B) = $0.75 \to$ on-time delivery by both services
- P(A and not B) = $0.15 \to$ on-time delivery ONLY by service A
- P(not A and B) = $0.05 \to$ on-time delivery ONLY by service B
- P(not A and not B) = $0.05 \to$ neither service delivered on time

:::{admonition} Comment
:class: important

A common mistake is to confuse P(A) = P(event A occurs) with P(A and not B) = P(ONLY event A occurs) (and similarly, P(B) = P(event B occurs) with P(not A and B) = P(only event B occurs)).

Looking at the probability table is a great way to clear up this confusion. Reading across the first row:

$$P(A) = P(A \text{ and } B) + P(A \text{ and not } B) = 0.75 + 0.15 = 0.90$$

P(A) = 0.90 means that in 90% of the cases when service A is used, it delivers the document on time. These cases of on-time delivery by service A can be decomposed into two sub-cases:

- P(A and B) = $0.75 \to 75%$ of the time the document is delivered on time also by service B (i.e., the document is delivered on time by both services)
- P(A and not B) = $0.15 \to 15%$ of the time the document is not delivered on time by service B (i.e., delivered on time only by service A).

Similarly, reading down the first column:

$$P(B) = P(A \text{ and } B) + P(\text{not } A \text{ and } B) = 0.75 + 0.05 = 0.80$$
:::

## Check Your Understanding: Probability Two-Way Tables

Recall the smoke detector example from the last activity. Here is a quick recap:

- D—the dining room alarm is set off by smoke in the kitchen
- B—the bedroom alarm is set off by smoke in the kitchen
- P(D) = 0.95, P(B) = 0.40
- D and B are independent $\to$ P(D and B) = 0.38

Complete the table below. Start with the information that is given and go from there.

| | B | not B | Total |
| --- | --- | --- | --- |
| **D** | 0.38 | ? | 0.95 |
| **not D** | ? | ? | ? |
| **Total** | 0.40 | ? | 1.00 |

:::{quiz} What is P(D and not B)—the probability that only the dining room alarm goes off?
:hint: The D row must add to P(D) = 0.95.
:feedback-0: Correct! P(D and not B) = $0.95 - 0.38 = 0.57$.
:feedback-1: 0.55 doesn't make the D row sum to 0.95—recheck the subtraction.
:feedback-2: 0.02 belongs elsewhere in the table; the D row must total 0.95.
* *0.57
* 0.55
* 0.02
:::

:::{quiz} What is P(not D and not B)—the probability that neither alarm goes off?
:hint: The "not B" column totals 0.60, and P(D and not B) = 0.57.
:feedback-0: Correct! The not-B column totals $1 - 0.40 = 0.60$, so P(not D and not B) = $0.60 - 0.57 = 0.03$. (Check: the not-D row is $0.02 + 0.03 = 0.05 = 1 - 0.95$ ✓)
:feedback-1: 0.05 is P(not D), the whole row total—the question asks for one cell of that row.
:feedback-2: 0.60 is the total probability of "not B"; subtract the part where D occurs.
* *0.03
* 0.05
* 0.60
:::

```{admonition} Comment
:class: important

In both the delivery problem and the smoke detector problem, we knew P(A), P(B) and P(A and B). (In the smoke detector problem, we actually needed to work a bit to get P(A and B), but it wasn't too bad.) That was enough information to complete the table.

This, however, is not the only combination of three values that would provide sufficient information to complete the table. Essentially, as long as we are given (or can calculate) one value in each of the margins (the total row and the total column), and one of the four cells in the body of the table, we'll be able to complete the entire table.
```

## Check Your Understanding: Reading a Probability Table

Records on traffic accidents in a certain region show that 87% of the accidents involved a male driver, 56% of the accidents involved speeding, and in 10% of the accidents the driver was female and was not speeding.

(We'll use M for an accident involving a male driver, F [= not M] for a female driver, and G for an accident involving speeding.)

:::{quiz} What is P(F and G)—the probability that an accident involved a female driver who was speeding?
:hint: P(F) = $1 - 0.87 = 0.13$, and the F row splits into "speeding" and "not speeding."
:feedback-0: Correct! P(F) = 0.13 and P(F and not G) = 0.10, so P(F and G) = $0.13 - 0.10 = 0.03$.
:feedback-1: 0.13 is P(F), the whole row; subtract the not-speeding part.
:feedback-2: 0.10 is P(F and not G), given in the problem.
* *0.03
* 0.13
* 0.10
:::

:::{quiz} What is P(M and G)—the probability that an accident involved a male driver who was speeding?
:hint: The G column totals 0.56, and you just found P(F and G).
:feedback-0: Correct! P(M and G) = P(G) - P(F and G) = $0.56 - 0.03 = 0.53$.
:feedback-1: 0.56 is the total probability of speeding accidents, including female drivers.
:feedback-2: $0.87 \times 0.56$ assumes M and G are independent, which we have no reason to believe here—use the table instead.
* *0.53
* 0.56
* 0.49
:::

```{admonition} Comment
:class: important

When we used two-way tables in the Exploratory Data Analysis (EDA) section, it was to record values of two categorical variables for a concrete {term}`sample` of individuals. In contrast, the information in a probability two-way table is for an entire {term}`population`, and the values are rather abstract. If we had treated something like the delivery example in the EDA section, we would have recorded the actual numbers of on-time (and not-on-time) deliveries for samples of documents mailed with service A or B. In this section, the long-term probabilities are presented as being known. Presumably, those probabilities were based on relative frequencies recorded over many repetitions.
```
