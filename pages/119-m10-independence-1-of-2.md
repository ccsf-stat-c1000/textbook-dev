# Testing for Independence with Conditional Probabilities

```{admonition} Learning Objectives
:class: note

- Determine whether two events are independent or not.
```

As we saw in the Exploratory Data Analysis section, whenever a situation involves more than one variable, it is generally of interest to determine whether or not the variables are related. In probability, we talk about independent events, and in the first module we said that two events A and B are *independent* if event A occurring *does not affect* the probability that event B will occur. Now that we've introduced conditional probability, we can formalize the definition of independence of events and develop four simple ways to check whether two events are independent or not. We will introduce these "independence checks" using examples, and then summarize.

:::{admonition} Example: Pierced Ears (continued)
:class: tip

Consider again the two-way table for all 500 students in a particular high school, classified according to gender and whether or not they have one or both ears pierced:

| | Pierced | Not Pierced | Total |
| --- | --- | --- | --- |
| Male | 36 | 144 | 180 |
| Female | 288 | 32 | 320 |
| **Total** | **324** | **176** | **500** |

Would you expect those two variables to be related? That is, would you expect having pierced ears to depend on whether the student is male or female? Or, to put it yet another way, would knowing a student's gender affect the probability that the student's ears are pierced? To answer this, we may compare the overall probability of having pierced ears to the conditional probability of having pierced ears, given that a student is male. Our intuition would tell us that the latter should be lower: male students tend not to have their ears pierced, whereas female students do. Indeed, for students in general, the probability of having pierced ears (event E) is P(E) = 324/500 = 0.648. But the probability of having pierced ears given that a student is male is only P(E | M) = 36/180 = 0.20.

As we anticipated, P(E | M) is lower than P(E). The probability of a student having pierced ears changes (in this case, gets lower) when we know that the student is male, and therefore the events E and M are dependent. (If E and M were independent, knowing or not knowing that the student is male would not have made a difference ... but it did.)

This example illustrates that one method for determining whether two events are independent is to compare *P(B | A)* and *P(B)*.

If the two are *equal* (i.e., knowing or not knowing whether A has occurred has no effect on the probability of B occurring) then the two events are *independent*. Otherwise, if the *probability changes* depending on whether we know that A has occurred or not, then the two events are *not independent*. Similarly, using the same reasoning, we can compare *P(A | B)* and *P(A)*.
:::

:::{admonition} Example: Side Effects (continued)
:class: tip

Recall the side effects example. On the "Information for the Patient" label of a certain antidepressant it is claimed that based on some clinical trials, there is a 14% chance of experiencing sleeping problems known as insomnia (denote this event by *I*), there is a 26% chance of experiencing headache (denote this event by *H*), and there is a 5% chance of experiencing both side effects (*I and H*).

Are the two side effects independent of each other?

To check whether the two side effects are independent, let's compare P(H | I) and P(H).

In the previous part of this module, we found that *P(H | I)* = P(H and I) / P(I) = 0.05/0.14 = *0.357*, while *P(H) = 0.26.* Knowing that a patient experienced insomnia increases the likelihood that he/she will also experience headache from 0.26 to 0.357. The conclusion, therefore, is that the two side effects are not independent—they are dependent.

Alternatively, we could have compared P(I | H) to P(I). *P(I) = 0.14*, and previously we found that *P(I | H)* = P(I and H) / P(H) = 0.05/0.26 = *0.1923*, and again, since the two are not equal, we can conclude that the two side effects I and H are dependent.
:::

## Check Your Understanding: Independence and Two-Way Tables

Recall again the smoke alarms example, with the two-way probability table:

| | B | not B | Total |
| --- | --- | --- | --- |
| **D** | 0.38 | 0.57 | 0.95 |
| **not D** | 0.02 | 0.03 | 0.05 |
| **Total** | 0.40 | 0.60 | 1.00 |

:::{quiz} Use the table to check: are the events D and B independent?
:hint: Compare P(D | B) = P(D and B)/P(B) with P(D).
:feedback-0: Correct! P(D | B) = 0.38/0.40 = 0.95 = P(D). Knowing the bedroom alarm went off doesn't change the probability for the dining room alarm—the events are independent.
:feedback-1: Compare the conditional and unconditional probabilities: they are both 0.95, so the events ARE independent.
:feedback-2: The events are not disjoint (both alarms can go off together), but that doesn't settle independence—the check is whether P(D | B) = P(D), and it does.
* *Yes—P(D | B) = 0.95 = P(D)
* No—the probabilities differ
* No—the events are not disjoint
:::
