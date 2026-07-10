# Binomial Random Variables (2 of 4)

```{admonition} Learning Objectives
:class: note

- Fit the binomial model when appropriate, and use it to perform simple calculations.
```

Now that we understand what a binomial random variable is, and when it arises, it's time to discuss its probability distribution. We'll start with a simple example and then generalize to a formula.

:::{admonition} Example: Deck of Cards
:class: tip

Consider a regular deck of 52 cards, in which there are 13 cards of each suit: hearts, diamonds, clubs and spades. We select 3 cards at random *with replacement*. Let X be the number of diamond cards we got (out of the 3).

We have 3 trials here, and they are independent (since the selection is with replacement). The outcome of each trial can be either success (diamond) or failure (not diamond), and the probability of success is 1/4 in each of the trials.

X, then, is binomial with n = 3 and p = 1/4.

Let's build the probability distribution of X as we did in the chapter on probability distributions. Recall that we begin with a table in which we record all possible outcomes in 3 selections (each selection may result in success, a diamond D, or failure, a non-diamond N), find the value of X for each outcome, and use simple probability principles to find the probability of each outcome:

| Outcome | X | Probability |
| --- | --- | --- |
| NNN | 0 | (3/4)(3/4)(3/4) |
| NND | 1 | (3/4)(3/4)(1/4) |
| NDN | 1 | (3/4)(1/4)(3/4) |
| DNN | 1 | (1/4)(3/4)(3/4) |
| NDD | 2 | (3/4)(1/4)(1/4) |
| DND | 2 | (1/4)(3/4)(1/4) |
| DDN | 2 | (1/4)(1/4)(3/4) |
| DDD | 3 | (1/4)(1/4)(1/4) |

With the help of the addition principle, we condense the information in this table to construct the actual probability distribution table:

| x | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| P(X = x) | 1(3/4)³ | 3(1/4)¹(3/4)² | 3(1/4)²(3/4)¹ | 1(1/4)³ |
:::

In order to establish a general formula for the probability that a binomial random variable X takes any given value x, we will look for patterns in the above distribution. From the way we constructed this probability distribution, we know that, in general:

P(X = x) = (number of possible outcomes with x successes out of 3) × (probability of each outcome that has x successes out of 3)

Let's start with the second part, the probability of an outcome with x successes out of 3, where the probability of success is 1/4. Notice that the fractions multiplied in each case are for the probability of x successes (where each success has a probability of p = 1/4) and the remaining (3 − x) failures (where each failure has probability of 1 − p = 3/4). So in general:

$$\text{probability of each outcome with } x \text{ successes out of } 3 = \left(\tfrac{1}{4}\right)^{x}\left(\tfrac{3}{4}\right)^{3-x}$$

Let's move on to talk about the number of possible outcomes with x successes out of three. Here it is harder to see the pattern, so we'll give the following mathematical result.

## Result

Consider a random experiment that consists of n trials, each one ending up in either success or failure. The number of possible outcomes in the sample space that have exactly k successes out of n is:

$$\frac{n!}{k!(n-k)!}$$

Note that n! is read "n factorial" and is defined to be the product 1 × 2 × 3 × ... × n. 0! is defined to be 1.

:::{admonition} Example: Ear Piercings
:class: tip

You choose 12 male college students at random and record whether they have any ear piercings (success) or not. There are many possible outcomes to this experiment (actually, 4,096 of them!).

In how many of the possible outcomes of this experiment are there exactly 8 successes (students who have at least one ear pierced)?

There is no way that we would start listing all these possible outcomes. The result above comes to our rescue.

The result says that in an experiment like this, where you repeat a trial n times (in our case, we repeat it n = 12 times, once for each student we choose), the number of possible outcomes with exactly 8 successes (out of 12) is:

$$\frac{12!}{8!(12-8)!}=\frac{1 \times 2 \times 3 \times \cdots \times 12}{(1 \times 2 \times \cdots \times 8)(1 \times 2 \times 3 \times 4)}=495$$
:::

:::{quiz} In how many of the possible outcomes of 5 coin tosses are there exactly 2 heads?
:hint: Compute 5!/(2!·3!).
:feedback-0: Correct! 5!/(2!3!) = 120/(2 × 6) = 10.
:feedback-1: 20 would be 5!/3!—don't forget to divide by 2! as well.
:feedback-2: 5 counts only the outcomes where the two heads are adjacent-first arrangements; the formula counts all 10.
* *10
* 20
* 5
:::

:::{admonition} Example: Cards Revisited
:class: tip

Let's go back to our example, in which we have n = 3 trials (selecting 3 cards). We saw that there were 3 possible outcomes with exactly 2 successes out of 3. The result confirms this since:

$$\frac{3!}{2!(3-2)!}=\frac{1 \times 2 \times 3}{(1 \times 2)(1)}=\frac{6}{2}=3$$
:::

In general, then, the number of ways to get x successes (and n − x failures) in n trials is $\frac{n!}{x!(n-x)!}$. Therefore, the probability of x successes (and n − x failures) in n trials, where the probability of success in each trial is p (and the probability of failure is 1 − p), is equal to the number of outcomes in which there are x successes out of n trials, times the probability of x successes, times the probability of n − x failures:

```{admonition} The Binomial Probability Formula
:class: note

$$P(X=x)=\frac{n!}{x!(n-x)!}\,p^{x}(1-p)^{n-x}$$

where x may take any value 0, 1, ..., n.
```
