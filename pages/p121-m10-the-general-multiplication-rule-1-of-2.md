# The General Multiplication Rule: P(A and B) Without Independence

Now that we have an understanding of conditional probabilities and can express them with concise notation, and have a more formal understanding of what it means for two events to be independent, we can finally establish the General Multiplication Rule, a formal rule for finding P(A and B) that applies to any two events, whether they are independent or dependent.

We begin with an example that contrasts P(A and B) for independent and dependent cases.

:::{admonition} Example: Picking Cards With Replacement
:class: tip

Suppose you pick two cards at random from four cards consisting of one of each suit: club, diamond, heart, and spade, where the first card is replaced before the second card is picked. What is the probability of picking a club and then a diamond? Because the sampling is done with replacement, whether or not a diamond is picked on the second selection is independent of whether or not a club has been picked on the first selection. Rule 5, the multiplication rule for independent events, tells us that:

P(C1 and D2) = P(C1) $\times$ P(D2) = $1/4 \times 1/4 = 1/16$.

[Here we denote the event "club picked on first selection" as C1 and the event "diamond picked on second selection" as D2.] The display below lists all 16 equally likely ordered outcomes; 1/4 of the time we'll pick a club first, and of these times, 1/4 will result in a diamond on the second pick, so 1/16 of the selections will have a club first and then a diamond:

```
SC  SD  SH  SS
HC  HD  HH  HS
DC  DD  DH  DS
CC  CD  CH  CS   ← club first (4 of 16); CD is 1 of these 4
```
:::

:::{admonition} Example: Picking Cards Without Replacement
:class: tip

Suppose you pick two cards at random from four cards consisting of one of each suit: club, diamond, heart, and spade, without replacing the first card before the second card is picked. What is the probability of picking a club and then a diamond? The probability in this case is not $1/4 \times 1/4 = 1/16$, because the sampling is done without replacement, so whether or not a diamond is picked on the second selection *does* depend on what was picked on the first selection. (For instance, if a diamond was picked on the first selection, the probability of another diamond is zero!) As in the example above, 1/4 of the time we'll pick a club first. But since the club has been removed, 1/3 of these selections with a club first will have a diamond second. The probability of a club and then a diamond is $1/4 \times 1/3 = 1/12$; this is the probability of getting a club first, multiplied by the probability of getting a diamond second, given that a club was picked first:

```
SC  SD  SH
HC  HD  HS
DC  DH  DS
CD  CH  CS   ← club first (3 of 12); CD is 1 of these 3
```

Using the notation of conditional probabilities, we can write

P(C1 and D2) = P(C1) $\times$ P(D2 | C1) = $1/4 \times 1/3 = 1/12$.
:::

For independent events A and B, we had the rule P(A and B) = P(A) $\times$ P(B). Due to independence, to find the probability of both, we could multiply the probability of A by the simple probability of B, because the occurrence of A would have no effect on the probability of B occurring. Now, for events A and B that may be dependent, to find the probability of both, we multiply the probability of A by the conditional probability of B, taking into account that A has occurred. Thus, our general multiplication rule is stated as follows:

```{admonition} Rule 7: The General Multiplication Rule
:class: note

*For any two events A and B, P(A and B) = P(A) $\times$ P(B | A)*
```

## Check Your Understanding: The General Multiplication Rule

:::{quiz} A drawer contains 5 batteries, 2 of which are dead. You grab two batteries at random (without replacement). What is the probability that both are dead?
:hint: P(first dead) = 2/5; given the first is dead, only 1 dead battery remains among 4.
:feedback-0: Correct! P(D1 and D2) = P(D1) $\times$ P(D2 | D1) = $(2/5) \times (1/4) = 2/20 = 0.1$.
:feedback-1: $(2/5)^2$ would be right only with replacement—but you don't put the first battery back.
:feedback-2: 2/5 is only the probability that the FIRST battery is dead.
* *0.1
* 0.16
* 0.4
:::
