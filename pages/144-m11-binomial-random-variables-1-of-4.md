# Binomial Random Variables (1 of 4)

```{admonition} Learning Objectives
    - Fit the binomial model when appropriate, and use it to perform simple calculations.
```

## Binomial Random Variables

So far, in our discussion about discrete random variables, we have been introduced to:

1. The probability distribution, which tells us which values a variable
                            takes, and how often it takes them.
2. The mean of the random variable, which tells us the long-run average
                            value that the random variable takes.
3. The standard deviation of the random variable, which tells us a typical
                            (or long-run average) distance between the mean of the random variable
                            and the values it takes.

We now introduce a special class of discrete random variables that are very common because, as you'll see, they come up in many situations: *binomial random variables.*

Here's how we'll present this material. First, we'll explain what kind of random experiments give rise to a binomial random variable and how the binomial random variable is defined in those types of experiments.

We'll then present the probability distribution of the binomial random variable, which will be presented as a formula (which, as you remember, is one of the three ways in which a probability distribution of a discrete random variable can be presented), and explain why the formula makes sense. We'll conclude our discussion by presenting the mean and standard deviation of the binomial random variable.

As we just mentioned, we'll start by describing what kind of random experiments give rise to a binomial random variable. We'll call this type of random experiment a "binomial experiment."

## Binomial Experiment

Binomial experiments are random experiments that consist of a fixed number of repeated trials, like tossing a coin 10 times, randomly choosing 10 people, rolling a die 5 times, etc. These trials, however, need to be independent in the sense that the outcome in one trial has no effect on the outcome in other trials. In each of these repeated trials there is one outcome that is of interest to us (we call this outcome "success"), and each of the trials is identical in the sense that the probability that the trial will end in a "success" is the same in each of the trials. So for example, if our experiment is tossing a coin 10 times, and we are interested in the outcome "heads" (our "success"), then this will be a binomial experiment, since the 10 trials are independent, and the probability of success is 1/2 in each of the 10 trials. Let's summarize and give more examples.

To summarize, the requirements for a random experiment to be a binomial experiment are as follows:

- A fixed number (n) of trials
- Each trial must be independent of the others
- Each trial has just two possible outcomes, called *success* (the
                            outcome of interest) and *failure*
- There is a constant *probability (p) of success* for each trial, the complement of which
                            is the *probability (1 - p) of failure*

In binomial random experiments, the number of successes in n trials is random. It can be as low as 0, if all the trials end up in failure, or as high as n, if all n trials end in success.

The random variable X that represents the number of successes in those n trials is called *binomial*, and is determined by the values of n and p. We say, "X is binomial with n = ... and p = ..."

```{admonition} Example: Random Experiments (Binomial or Not?)
    Let's consider a few random experiments.

    In each of them, we'll decide whether the random variable is binomial. If it is, we'll determine the values for n and p. If it isn't, we'll explain why not.

    1. A fair coin is flipped 20 times; X represents the number of heads. *X is binomial with n = 20 and p = 0.5*.
    2. You roll a fair die 50 times; X is the number of times you get a
                                    six. *X is binomial with n = 50 and p = 1/6*.
    3. Roll a fair die repeatedly; X is the number of rolls it takes to get
                                    a six. *X is not binomial, because the number of trials is not
                                    fixed*.
    4. Draw 3 cards at
                                    random,
                                    one after the other, *without replacement*, from a set of 4
                                    cards consisting of one club, one diamond, one heart, and one spade;
                                    X is the number of diamonds selected. *X is not binomial, because the selections are not
                                        independent*. (The probability (p) of success is not
                                    constant, because it is affected by previous selections.)
    5. Draw 3 cards at random, one after the other, *with replacement*, from a set of 4 cards
                                    consisting of one club, one diamond, one heart, and one spade; X is
                                    the number of diamonds selected. Sampling with replacement ensures
                                    independence. *X is binomial with n = 3 and p = 1/4*.
    6. Approximately 1 in every 20 children has a certain disease. Let X be the number of children with
                                    the disease out of a random sample of 100 children. Although the
                                    children are sampled without replacement, it is assumed that we are
                                    sampling from such a vast population that the selections are
                                    virtually independent. *X is binomial with n = 100 and p = 1/20 = 0.05*.
    7. The probability of having blood type B is 0.1. Choose 4 people at
                                    random; X is the number with blood type B. *X is binomial with n = 4 and p = 0.1*.
    8. A student answers 10 quiz questions completely at random; the first
                                    five are true/false, the second five are multiple choice, with four
                                    options each. X represents the number of correct answers. *X is not binomial, because p changes from 1/2 to 1/4*.
```

## Comments

*Example D* above was not binomial because sampling without replacement resulted in dependent selections. In particular, the probability of the second card being a diamond is very dependent on whether or not the first card was a diamond: the probability is 0 if the first card was a diamond, 1/3 if the first card was not a diamond.

In contrast, *Example E* was binomial because sampling with replacement resulted in independent selections: the probability of any of the 3 cards being a diamond is 1/4 no matter what the previous selections have been.

On the other hand, when you take a relatively small random sample of subjects from a large population, even though the sampling is without replacement, we can assume independence because the mathematical effect of removing one individual from a very large population on the next selection is negligible. For example, in *Example F*, we sampled 100 children out of the population of all children. Even though we sampled the children without replacement, whether one child has the disease or not really has no effect on whether another child has the disease or not. The same is true for *Example G*.

The convention is to "fudge" the requirement of independence as long as the population is at least 10 times the sample size.

```{admonition} Rule of Thumb
    The number (X) of successes in a sample of size n taken without replacement from a population with proportion (p) of successes is approximately binomial with n and p as long as the sample size (n) is at most 10% of the population size (N).

    In symbols, this would be: *n ≤ .10N*.

    This is the same as saying the population size is greater than or equal to 10 times the sample size. In symbols this is: *N ≥ 10n*.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
