# Probability Distribution (5 of 5)

```{admonition} Learning Objectives
    - Find the probability distribution of discrete random variables, and use it to find the probability of events of interest.
```

Here is another example in which we’ll use a probability distribution that is associated with a random variable of interest to find probabilities. What will be new in this example is the use of conditional probabilities.

```{admonition} Example: Xavier's Production Line
    The number of defective parts produced each hour by Xavier's production line is a random variable X with the following probability distribution:

    ```{figure} images/image012.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;

    A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;
    ```

    Using the probability distribution of a random variable, we can answer some probability questions:

    (a) What is the probability of at least 2 defects in a randomly chosen hour?

    $P(X\geq2)=P(X=2)+P(X=3)+P(X=4)=0.25+0.20+0.10=0.55$

    (Note that the addition principle has been applied.)

    (b) Suppose it is known that more than 2 defects were produced in a particular hour. What is the probability that the number of defects was fewer than 4?

    We use the conditional probabilities definition$P(B|A)=\frac{P(AandB)}{P(A)}$ to solve:

    $P(X<4|X>2)=\frac{P((X<4)and(X>2))}{P(X>2)}=\frac{P(X=3)}{P(X>2)}=\frac{0.2}{0.3}=0.67$

    Note that we are substituting the event "X < 4" for event B, and the event "X > 2" for event A.

    Also note that the only way that (X < 4) and (X > 2) can happen together is if X = 3.
```

The purpose of the next activity is to give you guided practice at using the probability distribution of a random variable to find probabilities of interest.

## Learn By Doing

Recall the following example:

The number of sales that a telemarketing salesperson makes in an hour is a random variable X having the following probability distribution:

```{figure} images/lbd049.gif
:alt: A probability distribution table with two rows, labeled "x" and "P(X=x)." Here is the data in columns (x: P(X=x)): 0: 10/50; 1: 12/50; 2: 12/50; 3: 10/50; 4: 6/50;

A probability distribution table with two rows, labeled "x" and "P(X=x)." Here is the data in columns (x: P(X=x)): 0: 10/50; 1: 12/50; 2: 12/50; 3: 10/50; 4: 6/50;
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
