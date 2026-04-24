# Applications (2 of 2)

```{admonition} Learning Objectives
    - Find probabilities associated with the normal distribution.
```

The previous examples all followed the same general form: given values of a normal random variable, you were asked to find an associated probability. The two basic steps in the solution process were to

1. standardize to Z; and
2. find associated probabilities inside the normal table.

The next example will be a different type of problem: given a certain probability, you will be asked to find the associated value of the normal random variable. The solution process will go more or less in reverse order from what it was in the previous examples.

```{admonition} Example: Foot Length Revisited
    Again, foot length of a randomly chosen adult male is a normal random variable with a mean of 11 and standard deviation of 1.5.

    1. The probability is .04 that a randomly chosen adult male foot length will be less than how many inches? According to the normal table, a probability of .04 below (actually .0401) is associated with z = -1.75. In other words, the probability is .04 that a normal variable takes a value lower than 1.75 standard deviations below its mean. For adult male foot lengths, this would be 11 - 1.75(1.5) = 8.375. The probability is .04 that an adult male foot length would be less than 8.375 inches.
    2. The probability is .10 that an adult male foot will be longer than how many inches? Caution is needed here because of the word "longer." Once again, we must remind ourselves that the table only shows the probability of a normal variable taking a value *lower than* a certain number of standard deviations below or above its mean. Adjustments must be made for problems that involve probabilities besides "lower than" or "less than." As usual, we have a choice of invoking either symmetry or the fact that the total area under the normal curve is 1. Students should examine both methods and decide which they prefer to use for their own purposes. *Method 1:* According to the table, a probability of .10 *below* is associated with a z value of -1.28. By symmetry, it follows that a probability of .10 *above* has z = +1.28. We seek the foot length that is 1.28 standard deviations above its mean: 11 + 1.28(1.5) = 12.92, or just under 13 inches. *Method 2*: If the probability is .10 that a foot will be longer than the value we seek, then the probability is .90 that a foot will be shorter than that same value, since the probabilities must sum to 1. According to the table, a probability of .90 below is associated with a z value of +1.28. Again, we seek the foot length that is 1.28 standard deviations above its mean, or 12.92 inches.
```

## Comment

*Part (a) in the above example* could have been re-phrased as:

".04 is the proportion of all adult male foot lengths that are below what value?", which takes the perspective of thinking about the probability as a proportion of occurrences in the long-run. As originally stated, it focuses on the chance of a randomly chosen individual having a normal value in a given interval.

```{admonition} Example: Money Spent for Lunch
    A study reported that the amount of money spent each week for lunch by a worker in a particular city is a normal random variable with a mean of $35 and a standard deviation of $5.

    1. The probability is .97 that a worker will spend less than how much money in a week on lunch? The z associated with a probability of .9700 below is +1.88. The amount that is 1.88 standard deviations above the mean is 35 + 1.88(5) = 44.4, or $44.40.
    2. There is a 30% chance of spending more than how much for lunches in a week? The z associated with a probability of .30 above is +.52. The amount is 35 + .52(5) = 37.6, or $37.60.
```

## Comment

Another way of expressing *Example (part a.)* above would be to ask, "What is the 97th percentile for the amount (X) spent by workers in a week for their lunch?" Many normal variables, such as heights, weights, or exam scores, are often expressed in terms of percentiles.

```{admonition} Example
    The height X (in inches) of a randomly chosen woman is a normal random variable with a mean of 65 and a standard deviation of 2.5. What is the height of a woman who is in the 80th percentile? A probability of .7995 in the table corresponds to z = +.84. Her height is 65 + .84(2.5) = 67.1 inches.
```

By now we have had practice in solving normal probability problems in both directions: those where a normal value is given and we are asked to report a probability, and those where a probability is given and we are asked to report a normal value. Strategies for solving such problems are outlined below:

## Steps in Solving Two Types of Normal Problems

1. Given a normal value x, solve for probability:
  1. Standardize: calculate $z=\frac{x&minus;\mu}{&sigma;}$
  2. Locate z in the margins of the normal table (ones and tenths for the row, hundredths for the column). Find the corresponding probability (given to four decimal places) of a normal random variable taking a value below z inside the table. (Adjust if the problem involves something other than a "less-than" probability, by invoking either symmetry or the fact that the total area under the normal curve is 1.)
2. Given a probability, solve for normal value x:
  1. (Adjust if the problem involves something other than a "less-than" probability, by invoking either symmetry or the fact that the total area under the normal curve is 1.) Locate the probability (given to four decimal places) inside the normal table. Find the corresponding z value in the margins (row for ones and tenths, column for hundredths).
  2. "Unstandardize": calculate $x=\mu+z&lowast;&sigma;$.

This next activity is a continuation of the previous one, and will give you guided practice in solving word problems involving the normal distribution. In particular, we'll solve problems like the ones you just solved, in which you are given a probability and you are asked to find the normal value associated with it.

Recall the example from the last activity:

According to the College Board website, the scores on the math part of the SAT (SAT-M) in a certain year had a mean of 507 and standard deviation of 111. Assume that SAT scores follow a normal distribution.

One of the criteria for admission to a certain engineering school is an SAT-M score in the top 2% of scores. How does this translate to an actual SAT-M score? In other words, how high must a student score on the SAT-M in order for his application to be considered? A different way to ask the same question is "What is the 98th percentile of the SAT-M distribution?"

Let’s work through this problem in a step-by-step manner....

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

In the days before computer software could easily provide high degrees of precision if desired, limitations in the precision of the normal table were offset by the process of interpolating. For example, if z were found to be 1.783, students were sometimes required to calculate the probability that was three tenths of the distance between the probability for 1.78 and that for 1.79. Such calculations are now considered obsolete. For most purposes, it is fine simply to make do with the closest table value provided.

So far, we've seen how to find probabilities associated with a normal random variable using a table.

The following activity will teach you how the same can be done using statistical software.

```{note}
    **Learn By Doing**

    Normal Random Variables

    *(Interactive activity — available in the OLI platform)*
```
