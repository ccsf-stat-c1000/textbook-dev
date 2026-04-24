# The General Multiplication Rule (1 of 2)

```{admonition} Learning Objectives
    - Use the General Multiplication Rule to find the probability that two events occur (P(A and B)).
```

Now that we have an understanding of conditional probabilities and can express them with concise notation, and have a more formal understanding of what it means for two events to be independent, we can finally establish the General Multiplication Rule, a formal rule for finding P(A and B) that applies to any two events, whether they are independent or dependent.

We begin with an example that contrasts P(A and B) for independent and dependent cases.

```{admonition} Example
    Suppose you pick two cards at random from four cards consisting of one of each suit: club, diamond, heart, and spade, where the first card is replaced before the second card is picked. What is the probability of picking a club and then a diamond? Because the sampling is done with replacement, whether or not a diamond is picked on the second selection is independent of whether or not a club has been picked on the first selection. Rule 5, the multiplication rule for independent events, tells us that:

    P(C1 and D2) = P(C1) * P(D2) = 1/4 * 1/4 = 1/16.

    [Here we denote the event "club picked on first selection" as C1 and the event "diamond picked on second selection" as D2.] The display below shows that 1/4 of the time we'll pick a club first, and of these times, 1/4 will result in a diamond on the second pick: 1/4 * 1/4 = 1/16 of the selections will have a club first and then a diamond.

    ```{figure} images/image007.gif
    :alt: All of the suit possibilities of picking one card, then replacing it and picking a second card. These possibilities are: SC, SD, SH, SS, HC, HD, HH, HS, DC, DD, DH, DS, CC, CD, CH, CS. Note that 1/4 of these have C picked first (the last 4, out of 16 total). Out of these, only one is CD, which is 1/4 of all of the possibilities with C picked first.

    All of the suit possibilities of picking one card, then replacing it and picking a second card. These possibilities are: SC, SD, SH, SS, HC, HD, HH, HS, DC, DD, DH, DS, CC, CD, CH, CS. Note that 1/4 of these have C picked first (the last 4, out of 16 total). Out of these, only one is CD, which is 1/4 of all of the possibilities with C picked first.
    ```
```

```{admonition} Example
    Suppose you pick two cards at random from four cards consisting of one of each suit: club, diamond, heart, and spade, without replacing the first card before the second card is picked. What is the probability of picking a club and then a diamond? The probability in this case is not 1/4 * 1/4 = 1/16; because the sampling is done without replacement, so whether or not a diamond is picked on the second selection *does* depend on what was picked on the first selection. (For instance, if a diamond was picked on the first selection, the probability of another diamond is zero!) As in the example above, 1/4 of the time we'll pick a club first. But since the club has been removed, 1/3 of these selections with a club first will have a diamond second. The probability of a club and then a diamond is 1/4*1/3=1/12; this is the probability of getting a club first, multiplied by the probability of getting a diamond second, given that a club was picked first. Using the notation of conditional probabilities, we can write

    P(C1 and D2) = P(C1) * P(D2 | C1) = 1/4 * 1/3 = 1/12.

    ```{figure} images/image008.gif
    :alt: All of the suit possibilities of picking one card then a second card, without replacing any cards. These possibilities are: SC, SD, SH, HC, HD, HS, DC, DH, DS, CD, CH, CS. Note that 1/4 of these have C picked first (the last 3, out of 12 total). Out of these, only one is CD. CD is 1/3 of all of the possibilities with C picked first.

    All of the suit possibilities of picking one card then a second card, without replacing any cards. These possibilities are: SC, SD, SH, HC, HD, HS, DC, DH, DS, CD, CH, CS. Note that 1/4 of these have C picked first (the last 3, out of 12 total). Out of these, only one is CD. CD is 1/3 of all of the possibilities with C picked first.
    ```
```

For independent events A and B, we had the rule P(A and B) = P(A) * P(B). Due to independence, to find the probability of both, we could multiply the probability of A by the simple probability of B, because the occurrence of A would have no effect on the probability of B occurring. Now, for events A and B that may be dependent, to find the probability of both, we multiply the probability of A by the conditional probability of B, taking into account that A has occurred. Thus, our general multiplication rule is stated as follows:

```{admonition} 
    *The General Multiplication Rule:*For any two events A and B, *P(A and B) = P(A) * P(B | A)*
```
