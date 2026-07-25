# The Binomial Formula in Action

Let's look at another example:

:::{admonition} Example: Blood Type A
:class: tip

The probability of having blood type A is 0.4. Choose 4 people at random and let X be the number with blood type A.

X is a binomial random variable with $n = 4$ and $p = 0.4$.

As a review, let's first find the probability distribution of X the long way: construct an interim table of all possible outcomes in S, the corresponding values of X, and probabilities (using A for blood type A and N for not type A). Outcomes with the same number of A's have the same probability: for example, each of the four outcomes with exactly one A (NNNA, NNAN, NANN, ANNN) has probability $(0.4)^1(0.6)^3$.

As usual, the addition rule lets us combine probabilities for each possible value of X:

| x | count of outcomes | Probability |
| --- | --- | --- |
| 0 | 1 | $1 \times (0.4)^0(0.6)^4 = 0.1296$ |
| 1 | 4 | $4 \times (0.4)^1(0.6)^3 = 0.3456$ |
| 2 | 6 | $6 \times (0.4)^2(0.6)^2 = 0.3456$ |
| 3 | 4 | $4 \times (0.4)^3(0.6)^1 = 0.1536$ |
| 4 | 1 | $1 \times (0.4)^4(0.6)^0 = 0.0256$ |

Now let's apply the formula for the probability distribution of a binomial random variable, and see that by using it, we get exactly what we got the long way.

Recall that the general formula for the probability distribution of a binomial random variable with n trials and probability of success p is:

$$P(X=x)=\frac{n!}{x!(n-x)!}\,p^{x}(1-p)^{n-x} \quad \text{for } x = 0, 1, 2, \ldots, n$$

In our case, X is a binomial random variable with $n = 4$ and $p = 0.4$, so its probability distribution is:

$$P(X=x)=\frac{4!}{x!(4-x)!}\,(0.4)^{x}(0.6)^{4-x} \quad \text{for } x = 0, 1, 2, 3, 4$$

Let's use this formula to find P(X = 2) and see that we get exactly what we got before:

$$P(X=2)=\frac{4!}{2!(4-2)!}\,(0.4)^{2}(0.6)^{2}=6(0.16)(0.36)=0.3456$$
:::

:::{quiz} Using the same setup (n = 4, $p = 0.4)$, what is the probability that NONE of the 4 people have blood type A?
:hint: P(X = $0) = (0.6)^4$.
:feedback-0: Correct! P(X = $0) = 1 \times (0.4)^0(0.6)^4 = 0.1296$.
:feedback-1: 0.6 is the probability that ONE person is not type A; all four must be.
:feedback-2: 0.0256 is P(X = 4), the probability that all four ARE type A.
* *0.1296
* 0.6
* 0.0256
:::

Here is another interesting example.

:::{admonition} Example: Choosing Numbers at Random
:class: tip

Do people really choose numbers at random?

Each student in a group of 15 students is asked to pick a number from 1 to 20 completely at random. 3 of the 15 happen to pick the number 7 (this is a proportion of 0.20). Is this an improbably high proportion to choose a particular number?

If the selections are truly random, then each number from 1 to 20, including 7, has probability $p = 1/20 = 0.05$ of being selected. The number of trials is $n = 15$. The probability of at least 3 successes in 15 trials, when each trial has probability of success 0.05, can be found by applying the binomial formula.

To make the notation easier, we will use the shorthand notation $\binom{n}{x}$ for $\frac{n!}{x!(n-x)!}$.

$$P(X\geq3)=P(X=3)+P(X=4)+ \cdots +P(X=15)$$

$$=\binom{15}{3}(0.05)^{3}(0.95)^{12}+\binom{15}{4}(0.05)^{4}(0.95)^{11}+ \cdots +\binom{15}{15}(0.05)^{15}(0.95)^{0}$$

$$= 0.0307 + 0.0049 + 0.0006 + \cdots = 0.0362$$

where all remaining terms after the first 3 are less than 0.0001. The probability of at least 3 out of 15 people picking 7, when choosing at random from the numbers 1 to 20, is only 0.0362. Thus, 3 out of 15 is rather improbably high. People may think they are choosing at random, but in fact they tend to favor certain numbers, like the number 7.
:::

Now let's look at some truly practical applications of binomial random variables.

:::{admonition} Example: Airline Flights
:class: tip

Past studies have shown that 90% of the booked passengers actually arrive for a flight. Suppose that a small shuttle plane has 45 seats. We will assume that passengers arrive independently of each other. (This assumption is not really accurate, since not all people travel alone, but we'll use it for the purposes of our experiment.)

Many times airlines "*overbook*" flights. This means that the airline sells more tickets than there are seats on the plane. This is due to the fact that sometimes passengers don't show up, and the plane must be flown with empty seats. However, if they do overbook, they run the risk of having more passengers than seats. So, some passengers may be unhappy. They also have the extra expense of putting those passengers on another flight and possibly supplying lodging.

With these risks in mind, the airline decides to sell more than 45 tickets. If they wish to keep the probability of having more than 45 passengers show up to get on the flight to less than 0.05, how many tickets should they sell?

This is a binomial random variable that represents the number of passengers that show up for the flight. It has $p = 0.90$, and n to be determined.

Suppose the airline sells 50 tickets. Now we have $n = 50$ and $p = 0.90$. We want to know P(X > 45), which is 1 - P(X $\leq 45) = 1 - 0.57 = 0.43$. (The details of this calculation are done with statistical software or a calculator.) This is certainly more than 0.05, so the airline must sell fewer seats.

If we reduce the number of tickets sold, we should be able to reduce this probability. We have calculated the probabilities in the following table:

| # tickets sold | P(X > 45) |
| --- | --- |
| 50 | 0.43 |
| 49 | 0.26 |
| 48 | 0.13 |
| 47 | 0.04 |
| 46 | 0.008 |

From this table, we can see that by selling 47 tickets, the airline can reduce the probability that it will have more passengers show up than there are seats to less than 5%.

Note: For practice in finding binomial probabilities, you may wish to verify one or more of the results from the table above.
:::

:::{quiz} Suppose the airline is more cautious and wants the probability of overbooking (more than 45 passengers showing up) to be less than 1%. Using the table above, how many tickets can it sell?
:hint: Find the largest number of tickets with P(X > 45) below 0.01.
:feedback-0: Correct! Selling 46 tickets gives P(X > $45) = 0.008 < 0.01$; selling 47 gives 0.04, which is too high.
:feedback-1: At 47 tickets the probability is 0.04, which exceeds 1%.
:feedback-2: 45 tickets makes overbooking impossible, but the airline can sell 46 and still meet the 1% requirement.
* *46
* 47
* 45
:::
