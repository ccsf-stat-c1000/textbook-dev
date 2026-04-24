# Binomial Random Variables (3 of 4)

```{admonition} Learning Objectives
    - Fit the binomial model when appropriate, and use it to perform simple calculations.
```

Let's look at another example:

```{admonition} Example: Blood Type A
    The probability of having blood type A is .4. Choose 4 people at random and let X be the number with blood type A.

    X is a binomial random variable with n = 4 and p = .4.

    As a review, let's first find the probability distribution of X the long way: construct an interim table of all possible outcomes in S, the corresponding values of X, and probabilities. Then construct the probability distribution table for X.

    ```{figure} images/image090.gif
    :alt: The probability distribution table, with three columns, &quot;S,&quot; &quot;X,&quot; and &quot;Probability.&quot; Here is the data in the table, given in row format (S: X, Probability): NNNN: 0, .4^0 × .6^4; NNNA: 1, .4^1 × .6^3; NNAN: 1, .4^1 × .6^3; NANN: 1, .4^1 × .6^3; ANNN: 1, .4^1 × .6^3; NNAA: 2, .4^2 × .6^2; NANA: 2, .4^2 × .6^2; NAAN: 2, .4^2 × .6^2; ANNA: 2, .4^2 × .6^2; ANAN: 2, .4^2 × .6^2; AANN: 2, .4^2 × .6^2; NAAA: 3, .4^3 × .6^1; ANAA: 3, .4^3 × .6^1; AANA: 3, .4^3 × .6^1; AAAN: 3, .4^3 × .6^1; AAAA: 4, .4^4 × .6^0;

    The probability distribution table, with three columns, &quot;S,&quot; &quot;X,&quot; and &quot;Probability.&quot; Here is the data in the table, given in row format (S: X, Probability): NNNN: 0, .4^0 × .6^4; NNNA: 1, .4^1 × .6^3; NNAN: 1, .4^1 × .6^3; NANN: 1, .4^1 × .6^3; ANNN: 1, .4^1 × .6^3; NNAA: 2, .4^2 × .6^2; NANA: 2, .4^2 × .6^2; NAAN: 2, .4^2 × .6^2; ANNA: 2, .4^2 × .6^2; ANAN: 2, .4^2 × .6^2; AANN: 2, .4^2 × .6^2; NAAA: 3, .4^3 × .6^1; ANAA: 3, .4^3 × .6^1; AANA: 3, .4^3 × .6^1; AAAN: 3, .4^3 × .6^1; AAAA: 4, .4^4 × .6^0;
    ```

    As usual, the addition rule lets us combine probabilities for each possible value of X:

    ```{figure} images/image091.gif
    :alt: A table with two columns, labeled &quot;X,&quot; and &quot;Probability.&quot; Here is the data, in row format (X, Probability): 0: (1) × .4^0 × .6^4 = .1296; 1: (4) × .4^1 × .6^3 = .3456; 2: (6) × .4^2 × .6^2 = .3456; 3: (4) × .4^3 × .6^1 = .1536; 4: (1) × .4^4 × .6^0 = .0256;

    A table with two columns, labeled &quot;X,&quot; and &quot;Probability.&quot; Here is the data, in row format (X, Probability): 0: (1) × .4^0 × .6^4 = .1296; 1: (4) × .4^1 × .6^3 = .3456; 2: (6) × .4^2 × .6^2 = .3456; 3: (4) × .4^3 × .6^1 = .1536; 4: (1) × .4^4 × .6^0 = .0256;
    ```

    Now let's apply the formula for the probability distribution of a binomial random variable, and see that by using it, we get exactly what we got the long way.

    Recall that the general formula for the probability distribution of a binomial random variable with n trials and probability of success p is:

    $P(X=x)=\frac{n!}{x!(n&minus;x)!} p^{x}(1&minus;p)^{(n&minus;x)}$ for x = 0, 1, 2, 3, ... , n

    In our case, X is a binomial random variable with n = 4 and p = .4, so its probability distribution is:

    $P(X=x)=\frac{4!}{x!(4&minus;x)!} (0.4)^{x}(0.6)^{4&minus;x}$ for x = 0, 1, 2, 3, 4

    Let's use this formula to find P(X = 2) and see that we get exactly what we got before.

    $P(X=2)=\frac{4!}{2!(4&minus;2)!} (0.4)^{2}(0.6)^{4&minus;2}=\frac{1^{&lowast;}2^{&lowast;}3^{&lowast;}4}{(1^{&lowast;}2)(1^{&lowast;}2)} (0.4)^{2}(0.6)^{2}=0.3456$
```

```{note}
    **Learn By Doing**

    Binomial Random Variables

    *(Interactive activity — available in the OLI platform)*
```

Here is another interesting example.

```{admonition} Example: Choosing Numbers at Random
    Do people really choose numbers at random?

    Each student in a group of 15 students is asked to each pick a number from 1 to 20 completely at random. 3 of the 15 happen to pick the number 7 (this is a probability of .20). Is this an improbably high proportion to choose a particular number?

    If the selections are truly random, then each number from 1 to 20, including 7, has probability p = 1/20 = .05 of being selected. The number of trials is n = 15. The probability of at least 3 successes in 15 trials, when each trial has probability of success .05, can be found by applying the binomial formula.

    To make the notation easier, we will use a shorthand notation for the number of possible outcomes with x successes out of n. $\frac{n!}{x!(n-x)!}$ will be written as: $(_{x}^{n})$ .

    $P(X\geq3)=P(X=3)+P(X=4)+ ... +P(X=15)$

    $=(_{3}^{15})(0.05)^{3}(0.95)^{12}+(_{4}^{15})(0.05)^{4}(0.95)^{11}+ ... +(_{15}^{15})(0.05)^{15}(0.95)^{0}$

    $= .0307 + .0049 + .0006 + ... = .0362$

    where all remaining terms after the first 3 are less than .0001. The probability of at least 3 out of 15 people picking 7, when choosing at random from the numbers 1 to 20, is only .0362. Thus, 3 out of 15 is rather improbably high. People may think they are choosing at random, but in fact they tend to favor certain numbers, like the number 7.
```

Now let's look at some truly practical applications of binomial random variables.

```{admonition} Example: Airline Flights
    Past studies have shown that 90% of the booked passengers actually arrive for a flight. Suppose that a small shuttle plane has 45 seats. We will assume that passengers arrive independently of each other. (This assumption is not really accurate, since not all people travel alone, but we'll use it for the purposes of our experiment).

    Many times airlines "*overbook*" flights. This means that theairline sells more tickets than there are seats on the plane. This is due to the fact that sometimes passengers don't show up, and the plane must be flown with empty seats. However, if they do overbook, they run the risk of having more passengers than seats. So, some passengers may be unhappy. They also have the extra expense of putting those passengers on another flight and possibly supplying lodging.

    With these risks in mind, the airline decides to sell more than 45 tickets. If they wish to keep the probability of having more than 45 passengers show up to get on the flight to less than 0.05, how many tickets should they sell?

    This is a binomial random variable that represents the number of passengers that show up for the flight. It has p = 0.90, and n to be determined.

    Suppose theairline sells 50 tickets. Now we have n = 50 and p = 0.90. We want to know P(X > 45), which is 1 - P(X ≤ 45) = 1 - 0.57 or 0.43. Obviously, all the details of this calculation were not shown, since a statistical technology package was used to calculate the answer. This is certainly more than 0.05, so the airline must sell fewer seats.

    If we reduce the number of tickets sold, we should be able to reduce this probability. We have calculated the probabilities in the following table:

    | # tickets sold | P(X > 45) |
    | --- | --- |
    | 50 | 0.43 |
    | 49 | 0.26 |
    | 48 | 0.13 |
    | 47 | 0.04 |
    | 46 | 0.008 |

    From this table, we can see that by selling 47 tickets,the airline can reduce the probability that it will have more passengers show up than there are seats to less than 5%.

    Note: For practice in finding binomial probabilities, you may wish to verify one or more of the results from the table above.
```

```{note}
    **Learn By Doing**

    An Application of the Binomial Random Variable

    *(Interactive activity — available in the OLI platform)*
```
