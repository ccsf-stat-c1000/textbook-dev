# Expected Value: What Happens in the Long Run

```{admonition} Learning Objectives
:class: note

- Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

## Applications of the Mean

Means of random variables are useful for telling us about long-run gains in sales, or for insurance companies.

Here are two examples:

:::{admonition} Example: Pizza Delivery #1
:class: tip

Your favorite pizza place delivers only one kind of pizza, which is sold for \$10, and costs the pizza place \$6 to make. The pizza place has the following policy regarding delivery: if the pizza takes longer than half an hour to arrive, there is no charge. Let the random variable X be the pizza place's gain for any one pizza.

Experience has shown that delivery takes longer than half an hour only 10 percent of the time.

Find the mean gain per pizza, $\mu_{X}$.

In order to find the mean of X, we first need to establish its probability distribution—the possible values and their probabilities.

The random variable X has two possible values: either the pizza costs them \$6 to make and they sell it for \$10, in which case X takes the value \$10 − \$6 = \$4, or it costs them \$6 to make and they give it away, in which case X takes the value \$0 − \$6 = −\$6. The probability of the latter case is given to be 10 percent, or 0.1, so using complements, the former has probability 0.9. Here, then, is the probability distribution of X:

| x | +4 | −6 |
| --- | --- | --- |
| P(X = x) | 0.9 | 0.1 |

Therefore,

$$\mu_{X}=(+4)(0.9)+(-6)(0.1)=+3$$

In the long run, the pizza place gains an average of \$3 per pizza delivered.
:::

:::{admonition} Example: Pizza Delivery #2
:class: tip

If the pizza place wants to increase its mean gain per pizza to \$3.90, how much should it raise the price from \$10? We need to replace the original price of 10 with an as-yet-to-be-determined new price N, resulting in this probability distribution table:

| x | N − 6 | −6 |
| --- | --- | --- |
| P(X = x) | 0.9 | 0.1 |

Next, setting $\mu_{X}$ equal to +3.90 instead of +3, we solve

$$3.9=(N-6)(0.9)+(-6)(0.1)=0.9N-6$$

so 0.9N = 9.9, and therefore the new price must be 11 dollars.
:::

## Learn By Doing

We are going to look at a variation of the pizza delivery example. Here is the scenario.

The Acme Shipping Company has learned from experience that it costs \$14.80 to deliver a small package overnight. The company charges \$20 for such a shipment, but guarantees that they will refund the \$20 charge if it does not arrive within 24 hours. Suppose that 2% of packages fail to arrive within 24 hours. Let the random variable X be the company's gain on a package.

:::{quiz} What are the possible values of X, the company's gain on one package?
:hint: The delivery costs \$14.80 either way; the revenue is \$20 or \$0.
:feedback-0: Correct! On time: 20 − 14.80 = +\$5.20. Late (refunded): 0 − 14.80 = −\$14.80.
:feedback-1: The cost of delivery is incurred whether or not the package is late.
:feedback-2: When the package is late, the \$20 is refunded, so the company loses its \$14.80 delivery cost.
* *+$5.20 (on time) and −$14.80 (late)
* +$20 (on time) and $0 (late)
* +$5.20 (on time) and $0 (late)
:::

:::{quiz} What is the probability distribution of X?
:hint: 2% of packages are late.
:feedback-0: Correct! P(X = 5.20) = 0.98 and P(X = −14.80) = 0.02.
:feedback-1: The two outcomes are far from equally likely—98% of packages arrive on time.
* *P(X = 5.20) = 0.98; P(X = −14.80) = 0.02
* P(X = 5.20) = 0.5; P(X = −14.80) = 0.5
:::

:::{quiz} What is the company's mean gain per package, μ(X)?
:hint: μ(X) = 5.20(0.98) + (−14.80)(0.02).
:feedback-0: Correct! μ(X) = 5.096 − 0.296 = \$4.80 per package in the long run.
:feedback-1: \$5.20 ignores the occasional refunds, which lower the long-run average.
:feedback-2: Remember to weight each value by its probability before adding.
* *$4.80
* $5.20
* $2.60
:::

:::{admonition} Example: Raffle
:class: tip

In order to raise money, a charity decides to raffle off some prizes. The charity sells 2,000 raffle tickets for \$5 each. The prizes are:

- 10 movie packages (two tickets plus popcorn) worth \$25 each
- 5 dinners for two worth \$50 each
- 2 smart phones worth \$200 each
- 1 flat-screen TV worth \$1,500

What is the expected gain or loss if you buy a single raffle ticket? The expected value can be written as E(X).

There are 5 possible outcomes when you buy a ticket: win movie package, win dinner for two, win smart phone, win TV, win nothing.

| prize | net gain or loss | probability |
| --- | --- | --- |
| movie package | 25 − 5 = 20 | 10/2000 |
| dinner for two | 50 − 5 = 45 | 5/2000 |
| smart phone | 200 − 5 = 195 | 2/2000 |
| TV | 1500 − 5 = 1495 | 1/2000 |
| nothing | 0 − 5 = −5 | 1982/2000 |

$$\mu_{X}=E(X)=20\left(\tfrac{10}{2000}\right)+45\left(\tfrac{5}{2000}\right)+195\left(\tfrac{2}{2000}\right)+1495\left(\tfrac{1}{2000}\right)+(-5)\left(\tfrac{1982}{2000}\right)$$

$$E(X)=\frac{-7600}{2000}=-3.80$$

Since we got a negative number, we have an expected loss of \$3.80 for each raffle ticket purchased. Recall that this is based upon a long-run average.

It should not be surprising that you have an expected loss. After all, the charity's goal is to raise money. If you have an expected loss of \$3.80 per ticket, they will have an expected gain of \$3.80 per ticket. Each ticket gives the charity +5 (it was −5 for you). The prizes are reversed, too. For example, the movie package is −20 + 5 for the charity (it was 20 − 5 for you).
:::
