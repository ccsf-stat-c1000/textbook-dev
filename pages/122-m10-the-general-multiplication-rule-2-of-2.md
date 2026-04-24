# The General Multiplication Rule (2 of 2)

```{admonition} Learning Objectives
    - Use the General Multiplication Rule to find the probability that two events occur (P(A and B)).
```

Here, again, is the General Multiplication Rule:

*For any two events A and B, P(A and B) = P(A) * P(B | A)*

## Comments

1. Note that although the motivation for this rule was to find P(A and B) when A and B are not independent, this rule is general in the sense that if A and B happen to be *independent*, then P(B | A) = P(B) is true, and we're back to Rule 5—the Multiplication Rule for Independent Events: P(A and B) = P(A) * P(B).

2. The General Multiplication Rule is just the definition of conditional probability in disguise. Recall the definition of conditional probability: *P(B | A) = P(A and B) / P(A)* Let's isolate P(A and B) by multiplying both sides of the equation by P(A), and we get: *P(A and B) = P(A) * P(B | A)*. That's it ... this is the General Multiplication Rule.

3. The General Multiplication Rule is useful when two events, A and B, occur in stages, first A and then B (like the selection of the two cards in the previous example). Thinking about it this way makes the General Multiplication Rule very intuitive. For both A and B to occur you first need A to occur (which happens with probability P(A)), *and* then you need B to occur, knowing that A has already occurred (which happens with probability P(B | A)).

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

Let's look at another, more realistic example:

```{admonition} Example
    In a certain region, one in every thousand people (0.001) of all individuals are infected by the HIV virus that causes AIDS. Tests for presence of the virus are fairly accurate but not perfect. If someone actually has HIV, the probability of testing positive is .95. Let *H* denote the event of having HIV, and *T* the event of testing positive.

    (a) Express the information that is given in the problem in terms of the events H and T.

    "one in every thousand people (0.001) of all individuals are infected with HIV" → *P(H) = .001*

    "If someone actually has HIV, the probability of testing positive is .95" → *P(T | H) = .95*

    (b) Use the General Multiplication Rule to find the probability that someone chosen at random from the population has HIV and tests positive.

    *P(H and T)* = P(H) * P(T | H) = .001*.95 = .00095.

    (c) If someone has HIV, what is the probability of testing negative? Here we need to find P(not T | H).

    Recall from an activity earlier in this module that the Complement Rule works with conditional probabilities as long as we condition on the same event, therefore: *P(not T | H)* = 1 - P(T | H) = 1 - .95 = .05.
```

The purpose of the next activity is to give you guided practice in expressing information in terms of conditional probabilities, and in using the General Multiplication Rule.

## Learn By Doing

An overheating engine can quickly cause serious damage to a car, and therefore a dashboard red warning light is supposed to come on if that happens.

In a certain model car, there is a 3% chance that the engine will overheat (event H).

The probability of the warning light showing up (event W) when it should (i.e., when the engine is really overheating) is 0.98. However, 1% of the time the warning light appears for no apparent reason (i.e., when the engine temperature is normal).

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
