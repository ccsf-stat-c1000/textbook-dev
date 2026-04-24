# Independence (1 of 2)

```{admonition} Learning Objectives
    - Determine whether two events are independent or not.
```

As we saw in the Exploratory Data Analysis section, whenever a situation involves more than one variable, it is generally of interest to determine whether or not the variables are related. In probability, we talk about independent events, and in the first module we said that two events A and B are *independent* if event A occurring *does not affect* the probability that event B will occur. Now that we've introduced conditional probability, we can formalize the definition of independence of events and develop four simple ways to check whether two events are independent or not. We will introduce these "independence checks" using examples, and then summarize.

```{admonition} Example
    Consider again the two-way table for all 500 students in a particular high school, classified according to gender and whether or not they have one or both ears pierced.

    ```{figure} images/image001.gif
    :alt: The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;

    The same table of the data for piercings. The column headings are "Pierced," "Not Pierced," and "Total." The Rows are "Male," "Female," and "Total." The data in the cells is given in "Row, Column: Value" format: Male, Pierced: 36; Male, Not Pierced: 144; Male, Total: 180; Female, Pierced: 288; Female, Not Pierced: 32; Female, Total: 320; Total, Pierced: 324; Total, Not Pierced: 176; Total, Total: 500;
    ```

    Would you expect those two variables to be related? That is, would you expect having pierced ears to depend on whether the student is male or female? Or, to put it yet another way, would knowing a student's gender affect the probability that the student's ears are pierced? To answer this, we may compare the overall probability of having pierced ears to the conditional probability of having pierced ears, given that a student is male. Our intuition would tell us that the latter should be lower: male students tend not to have their ears pierced, whereas female students do. Indeed, for students in general, the probability of having pierced ears (event E) is P(E) = 324/500 = .648. But the probability of having pierced ears given that a student is male is only P(E | M) = 36/180 = .20.

    As we anticipated, P(E | M) is lower than P(E). The probability of a student having pierced ears changes (in this case, gets lower) when we know that the student is male, and therefore the events E and M are dependent. (If E and M were independent, knowing or not knowing that the student is male would not have made a difference ... but it did.)

    This example illustrates that one method for determining whether two events are independent is to compare *P(B | A)* and *P(B)*.

    If the two are *equal* (i.e., knowing or not knowing whether A has occurred has no effect on the probability of B occurring) then the two events are *independent*. Otherwise, if the *probability changes* depending on whether we know that A has occurred or not, then the two events are *not independent*. Similarly, using the same reasoning, we can compare *P(A | B)* and *P(A)*.
```

```{admonition} Example
    Recall the side effects example. On the "Information for the Patient" label of a certain antidepressant it is claimed that based on some clinical trials, there is a 14% chance of experiencing sleeping problems known as insomnia (denote this event by *I*), there is a 26% chance of experiencing headache (denote this event by *H*), and there is a 5% chance of experiencing both side effects (*I and H*).

    Are the two side effects independent of each other?

    To check whether the two side effects are independent, let's compare P(H | I) and P(H).

    In the previous part of this module, we found that *P(H | I)* = P(H and I) / P(I) = .05/.14 = *.357*, while *P(H) = .26.*Knowing that a patient experienced insomnia increases the likelihood that he/she will also experience headache from .26 to .357. The conclusion, therefore is that the two side effects are not independent, they are dependent.

    Alternatively, we could have compared P(I | H) to P(I). *P(I) = .14*, and previously we found that *P(I | H)* = P(I and H) / P(H) = .05/.26 = *.1923*, and again, since the two are not equal, we can conclude that the two side effects I and H are dependent.
```

## Did I Get This?

Recall again the smoke alarms example.

A homeowner has smoke alarms installed in the dining room (adjacent to the kitchen) and an upstairs bedroom (above the kitchen). The two-way table below shows probabilities of smoke in the kitchen triggering the alarm in the dining room (D) or not, and in the bedroom (B) or not.

```{figure} images/dig002.gif
:alt: A table, in which the column headings are "B," "not B," and "Total." The rows are "D," "not D," and "Total." Here is the data in "Row,Column: Value" format: D, B: .38; D, not B: .57; D, Total: .95; not D, B: .02; not D, not B: .03; not D, Total: .05; Total, B: .40; Total, not B: .60; Total, Total: 1.00;

A table, in which the column headings are "B," "not B," and "Total." The rows are "D," "not D," and "Total." Here is the data in "Row,Column: Value" format: D, B: .38; D, not B: .57; D, Total: .95; not D, B: .02; not D, not B: .03; not D, Total: .05; Total, B: .40; Total, not B: .60; Total, Total: 1.00;
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
