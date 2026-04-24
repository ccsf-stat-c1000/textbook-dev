# Summary (Probability)

This summary provides a quick recap of the material you've learned in the probability unit. Please note that this summary does not provide complete coverage of the material, but just lists the main points. We therefore recommend that you use this summary only as a checklist or a review before going on to the next unit, or before an exam.

## General Remarks

- Probability is a discipline by itself. In the context of the big picture of this course, probability is used to quantify the imperfection associated with drawing conclusions about the entire population based only on a random sample drawn from it.
- We talk about the probability of an event, which is a statement about the outcome of a random experiment. In practice, each event corresponds to a subset of outcomes from the sample space.
- The probability of an event can be as low as 0 (when the event is impossible) and as high as 1 (when the event is certain).
- In some cases, the only way to find the probability of an event of interest is by repeating the random experiment many times and using the relative frequency approach.
- When all the possible outcomes of a random experiment are equally likely, the probability of an event is the fraction of outcomes which satisfy it.

## Probability Principles

Probability principles help us find the probability of events of certain types:

- *The Complement Rule*, P(not A) = 1 - P(A), is especially useful for finding events of the type "at least one of ..."
- To find the probability of *events of the type "A or B"*(interpreted as A occurs or B occurs or both), we use the General Addition Rule: P(A or B) = P(A) + P(B) - P(A and B). In the special case when A and B are disjoint (cannot happen together; P(A and B) = 0) the Addition Rule reduces to: P(A and B) = P(A) + P(B).
- To find the probability of *events of the type "A and B"* (interpreted as both A and B occur), we use the General Multiplication Rule: P(A and B) = P(A) * P(B | A). In the special case when A and B are independent (the occurrence of one event has no effect on the probability of the other occurring; P(B | A) = P(B)) the Multiplication Rule reduces to: P(A and B) = P(A) * P(B).
- P(B | A), the conditional probability of event B occurring given that event A has occurred, can be viewed as a reduction of the sample space S to event A. The conditional probability, then, is the fraction of event A where B occurs as well, P(B | A) = P(A and B) / P(A).

Probability trees are a useful visual tool for displaying and manipulating probabilities of events which naturally happen in sequence (or in stages). It is particularly useful when we are given conditional probability in one direction P(B | A), and need to find the reverse conditional probability P(A | B).

## Random Variables

A random variable is a variable whose values are numerical results of a random experiment.

- A *discrete random variable* is summarized by its probability distribution—a list of its possible values and their corresponding probabilities.
  - The sum of the probabilities of all possible values must be 1.
  - The probability distribution can be represented by a table, histogram, or formula.
- The *probability distribution* of a random variable can be supplemented with numerical measures of the center and spread of the random variable.
  - *Center:* The center of a random variable is measured by its mean (which is sometimes also referred to as the *expected value*). —The mean of a random variable can be interpreted as its long run average. —The mean is a weighted average of the possible values of the random variable weighted by their corresponding probabilities. —An application of the mean of a random variable is determining premiums for insurance policies.
  - *Spread:* The spread of a random variable is measured by its variance, or more typically by its standard deviation (the square root of the variance). —The standard deviation of a random variable can be interpreted as the typical (or long-run average) distance between the value that the random variable assumes and the mean of X.
- *Rules of means and variances* give us an easy way to find the mean and standard deviations of the "new" random variable a + bX (given the mean and standard deviation of X), as well as the mean and standard deviation of the "new" random variable X + Y (given the means and standard deviations of X and Y, and assuming that X and Y are independent).

## Binomial Random Variables

- The binomial random variable is a type of discrete random variable that is quite common.
- The binomial random variable is defined in a random experiment that consists of n independent trials, each having two possible outcomes (called "success" and "failure"), and each having the same probability of success: p. Such a random experiment is called the binomial random experiment.
- The binomial random variable represents the number of successes (out of n) in a binomial experiment. It can therefore have values as low as 0 (if none of the n trials was a success) and as high as n (if all n trials were successes).
- There are "many" binomial random variables, depending on the number of trials (n) and the probability of success (p).
- The probability distribution of the binomial random variable is given in the form of a formula and can be used to find probabilities. Technology can be used as well.
- The mean and standard deviation of a binomial random variable can be easily found using short-cut formulas.

## Continuous Random Variables

The probability distribution of a continuous random variable is represented by a probability density curve. The probability that the random variable takes a value in any interval of interest is the area above this interval and below the density curve.

An important example of a continuous random variable is the *normal random variable*, whose probability density curve is symmetric (bell-shaped), bulging in the middle and tapering at the ends.

- There are "many" normal random variables, each determined by its mean $\mu$ (which determines where the density curve is centered) and standard deviation $\sigma$, (which determines how spread out (wide) the normal density curve is).
- Any normal random variable follows the Standard Deviation Rule, which can help us find probabilities associated with the normal random variable.
- Another way to find probabilities associated with the normal random variable is using the standard normal table. This process involves finding the z-score of values, which tells us how many standard deviations below or above the mean the value is.
- An important application of the normal random variable is that it can be used as an approximation of the binomial random variable (under certain conditions). A continuity correction can improve this approximation.

## Sampling Distributions

A *parameter* is a number that describes the population, and a *statistic* is a number that describes the sample.

- Parameters are fixed, and in practice, usually unknown.
- Statistics change from sample to sample due to sampling variability.
- The behavior of the possible values the statistic can take in repeated samples is called the *sampling distribution* of that statistic.

The *sampling distribution of the sample proportion*, $\hat{p}$, (under certain conditions):

- is centered around p, the proportion in the entire population from which the sample is drawn.
- has standard deviation of $\sqrt{\frac{p(1-p)}{n}}$.
- is approximately normal (under certain conditions).

According to the *Central Limit Theorem*, the *sampling distribution of the sample mean*, $\bar{X}$:

- is centered around $\mu$, the mean in the entire population from which the sample is drawn.
- has a standard deviation of $\frac{\sigma}{\sqrt{n}}$.
- is, for a large enough sample size n, approximately normal (regardless of the shape of the population distribution).
