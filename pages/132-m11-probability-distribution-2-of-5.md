# Probability Distribution (2 of 5)

```{admonition} Learning Objectives
    - Find the probability distribution of discrete random variables, and use it to find the probability of events of interest.
```

The probability distribution for two flips of a coin was simple enough to construct at once. For more complicated random experiments, it is common to first construct a table of all the outcomes in S and their probabilities, then use the addition principle to condense that information into the actual probability distribution table.

```{admonition} Example: Flipping a Coin Three Times
    A coin is tossed three times. Let the random variable X be the number of tails. Find the probability distribution of X. We'll follow the same reasoning we used in the previous example:

    First, we specify the 8 possible outcomes in S, along with the number and the probability of that outcome. (Because they are all equally likely, each has probability 1/8. Alternatively, by the multiplication principle, each particular sequence of three coin faces has probability 1/2 * 1/2 * 1/2 = 1/8.)

    ```{figure} images/image006.gif
    :alt: A table with two columns, labeled "Outcome," and "Probability." Here is the data, arranged by row: HHH: ½ × ½ × ½ = 1/8; HHT: 1/8; HTH: 1/8; THH: 1/8; HTT: 1/8; THT: 1/8; TTH: 1/8; TTT: 1/8;

    A table with two columns, labeled "Outcome," and "Probability." Here is the data, arranged by row: HHH: ½ × ½ × ½ = 1/8; HHT: 1/8; HTH: 1/8; THH: 1/8; HTT: 1/8; THT: 1/8; TTH: 1/8; TTT: 1/8;
    ```

    Next, we figure out what the value of X is (number of tails) for each possible outcome.

    ```{figure} images/image007.gif
    :alt: A table with three columns, labeled "Outcome," and "Probability," and "X." The data is the same as in the previous table execpt the "X" column has been added. Here is the data, arranged by row (Outcome: Probability, X): HHH: 1/8, 0; HHT: 1/8, 1; HTH: 1/8, 1; THH: 1/8, 1; HTT: 1/8, 2; THT: 1/8, 2; TTH: 1/8, 2; TTT: 1/8, 3

    A table with three columns, labeled "Outcome," and "Probability," and "X." The data is the same as in the previous table execpt the "X" column has been added. Here is the data, arranged by row (Outcome: Probability, X): HHH: 1/8, 0; HHT: 1/8, 1; HTH: 1/8, 1; THH: 1/8, 1; HTT: 1/8, 2; THT: 1/8, 2; TTH: 1/8, 2; TTT: 1/8, 3
    ```

    Next, we use the addition principle to assert that

    P(X = 1) = P(HHT or HTH or THH) = P(HHT) + P(HTH) + P(THH) = 1/8 + 1/8 + 1/8 = 3/8.

    Similarly, P(X = 2) = P(HTT or THT or TTH) = 3/8.

    ```{figure} images/image008a.gif
    :alt: The previous table, annotated with the calculations to calculate P(X=x). For P(X=0), there is only one outcome in the table, so P(X=0) = 1/8. For P(X=1), there are thee outcomes, so P(X=1) = 3 × 1/8 = 3/8. The same thing happens for P(X=2) = 3 × 1/8 = 3/8. For P(X=3), there is only one case so P(X=3) = 1/8.

    The previous table, annotated with the calculations to calculate P(X=x). For P(X=0), there is only one outcome in the table, so P(X=0) = 1/8. For P(X=1), there are thee outcomes, so P(X=1) = 3 × 1/8 = 3/8. The same thing happens for P(X=2) = 3 × 1/8 = 3/8. For P(X=3), there is only one case so P(X=3) = 1/8.
    ```

    The resulting probability distribution is:

    ```{figure} images/image009.gif
    :alt: A two-row probability distribution table. The rows are labeled "X" and "P(X=x)". Here is the data in the table, arranged by column (in "X: P(X=x)" format): 0: 1/8; 1: 3/8; 2: 3/8; 3: 1/8;

    A two-row probability distribution table. The rows are labeled "X" and "P(X=x)". Here is the data in the table, arranged by column (in "X: P(X=x)" format): 0: 1/8; 1: 3/8; 2: 3/8; 3: 1/8;
    ```
```

The purpose of the next activity is to give you guided practice in finding the probability distribution of a discrete random variable.

## Learn By Doing

A young couple decides to try to have children until they have a boy. For financial reasons, the couple decides that they are going to stop trying when they have three children, whether they have a boy or not. (We are assuming that having a boy or a girl is equally likely, and that the child's gender in each birth is independent of the gender in the other births.)

Let the random variable X be the number of children the couple has.

Our goal is to find the probability distribution of X. In other words, we would like to create a table that lists all the possible values of X and the corresponding probabilities. We'll follow the same steps we followed in the two examples we solved.

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
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
