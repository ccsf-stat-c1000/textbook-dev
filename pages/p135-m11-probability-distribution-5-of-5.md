# Probability Distributions in Action

Here is another example in which we'll use a probability distribution that is associated with a random variable of interest to find probabilities. What will be new in this example is the use of conditional probabilities.

:::{admonition} Example: Xavier's Production Line
:class: tip

The number of defective parts produced each hour by Xavier's production line is a random variable X with the following probability distribution:

| x | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| P(X = x) | 0.15 | 0.30 | 0.25 | 0.20 | 0.10 |

Using the probability distribution of a random variable, we can answer some probability questions:

(a) What is the probability of at least 2 defects in a randomly chosen hour?

$$P(X\geq2)=P(X=2)+P(X=3)+P(X=4)=0.25+0.20+0.10=0.55$$

(Note that the addition principle has been applied.)

(b) Suppose it is known that more than 2 defects were produced in a particular hour. What is the probability that the number of defects was fewer than 4?

We use the conditional probability definition $P(B|A)=\frac{P(A \text{ and } B)}{P(A)}$ to solve:

$$P(X<4|X>2)=\frac{P((X<4) \text{ and } (X>2))}{P(X>2)}=\frac{P(X=3)}{P(X>2)}=\frac{0.2}{0.3}=0.67$$

Note that we are substituting the event "$X < 4$" for event B, and the event "$X > 2$" for event A.

Also note that the only way that (X < 4) and (X > 2) can happen together is if $X = 3$.
:::

The purpose of the next activity is to give you guided practice at using the probability distribution of a random variable to find probabilities of interest.

## Check Your Understanding: Applying a Probability Distribution

The number of sales that a telemarketing salesperson makes in an hour is a random variable X having the following probability distribution:

| x | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| P(X = x) | 10/50 | 12/50 | 12/50 | 10/50 | 6/50 |

:::{quiz} What is the probability that the salesperson makes at least one sale in an hour?
:hint: Use the Complement Rule: 1 - P(X = 0).
:feedback-0: Correct! P(X $\geq 1) = 1 - 10/50 = 40/50 = 0.8$.
:feedback-1: 10/50 is P(X = 0), the complement of "at least one sale."
:feedback-2: 12/50 is only P(X = 1); "at least one" includes 2, 3, and 4 as well.
* *0.8
* 0.2
* 0.24
:::

:::{quiz} What is the probability that the salesperson makes fewer than 3 sales in an hour?
:hint: $X < 3$ means $X = 0$, 1, or 2.
:feedback-0: Correct! P(X < $3) = (10 + 12 + 12)/50 = 34/50 = 0.68$.
:feedback-1: $44/50 = 0.88$ is P(X $\leq 3)$; "fewer than 3" excludes 3.
:feedback-2: 10/50 is only P(X = 3)... which isn't even part of this event.
* *0.68
* 0.88
* 0.2
:::

:::{quiz} Given that the salesperson made at least one sale, what is the probability that they made exactly one sale?
:hint: P(X = 1 | $X \geq 1)$ = P(X = 1)/P(X $\geq 1)$.
:feedback-0: Correct! P(X = 1 | $X \geq 1) = (12/50)/(40/50) = 12/40 = 0.3$.
:feedback-1: $12/50 = 0.24$ is the unconditional P(X = 1); the conditioning restricts the sample space to the 40/50 with at least one sale.
:feedback-2: Divide by P(X $\geq 1) = 0.8$, not by P(X = 0).
* *0.3
* 0.24
* 1.2
:::
