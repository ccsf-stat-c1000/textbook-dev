# Standardizing Values: The z-score

Let's go back to our example of foot length:

How likely or unlikely is it for a male's foot length to be more than 13 inches?

Since 13 inches doesn't happen to be exactly 1, 2, or 3 standard deviations away from the mean, we would only be able to give a very rough estimate of the probability at this point. Clearly, the Standard Deviation Rule only describes the tip of the iceberg, and while it serves well as an introduction to the normal curve, and gives us a good sense of what would be considered likely and unlikely values, it is very limited in the probability questions it can help us answer.

Here is another familiar normal distribution: scores on the math portion of the SAT, which are approximately normal with mean $\mu = 500$ and standard deviation $\sigma = 100$. Suppose we are interested in knowing the probability that a randomly selected student will score 633 or more. Again, 633 does not fall exactly 1, 2, or 3 standard deviations above the mean. Notice, however, that an SAT score of 633 and a foot length of 13 are both about 1/3 of the way between 1 and 2 standard deviations. As you continue to read this page, you'll realize that this positioning relative to the mean is the key to finding probabilities.

## Finding Probabilities for a Normal Random Variable

As we saw, the Standard Deviation Rule is very limited in helping us answer probability questions, and is basically limited to questions involving values that fall exactly 1, 2, and 3 standard deviations away from the mean. How do we answer probability questions in general? The key is the position of the value relative to the mean, measured in standard deviations.

We can approach the answering of probability questions two possible ways: a table and technology. In the next sections, you will learn how to use the "standard normal table," and the same calculations can be done with statistical software or a calculator.

## Standardizing Values

The first step to assessing a probability associated with a normal value is to determine the *relative* value with respect to all the other values taken by that normal variable. This is accomplished by determining how many standard deviations below or above the mean that value is.

:::{admonition} Example: Foot Length
:class: tip

How many standard deviations below or above the mean male foot length is 13 inches? Since the mean is 11 inches, 13 inches is 2 inches above the mean. Since a standard deviation is 1.5 inches, this would be $2 / 1.5 = 1.33$ standard deviations above the mean. Combining these two steps, we could write:

(13 in. - 11 in.) / (1.5 inches per standard deviation) = $(13 - 11) / 1.5$ standard deviations = +1.33 standard deviations.
:::

In the language of statistics, we have just found the {term}`z-score` for a male foot length of 13 inches to be $z = +1.33$. Or, to put it another way, we have *standardized* the value of 13. In general, the standardized value z tells how many standard deviations below or above the mean the original value is, and is calculated as follows:

*z-score = (value - mean)/standard deviation*

The convention is to denote a value of our normal random variable X with the letter "x." Since the mean is written $\mu$ and the standard deviation $\sigma$, we may write the standardized value as

$$z=\frac{x-\mu}{\sigma}$$

Notice that since $\sigma$ is always positive, for values of x above the mean ($\mu$), z will be positive; for values of x below $\mu$, z will be negative.

:::{admonition} Example: Standardizing Foot Measurements
:class: tip

Let's go back to our foot length example, and answer some more questions.

*(a)* What is the standardized value for a male foot length of 8.5 inches? How does this foot length relate to the mean?

$z = (8.5 - 11) / 1.5 = -1.67$. This foot length is 1.67 standard deviations *below* the mean.

*(b)* A man's standardized foot length is +2.5. What is his actual foot length in inches? If $z = +2.5$, then his foot length is 2.5 standard deviations above the mean. Since the mean is 11, and each standard deviation is 1.5, we get that the man's foot length is: $11 + 2.5(1.5) = 14.75$ inches.

z-scores also allow us to compare values of different normal random variables. Here is an example:

*(c)* In general, women's foot length is shorter than men's. Assume that women's foot length follows a normal distribution with a mean of 9.5 inches and standard deviation of 1.2. Ross' foot length is 13.25 inches, and Candace's foot length is only 11.6 inches. Which of the two has a longer foot relative to his or her gender group?

To answer this question, let's find the z-score of each of these two normal values, bearing in mind that each of the values comes from a different normal distribution.

Ross: z-score = $(13.25 - 11) / 1.5 = 1.5$ (Ross' foot length is 1.5 standard deviations above the mean foot length for men).

Candace: z-score = $(11.6 - 9.5) / 1.2 = 1.75$ (Candace's foot length is 1.75 standard deviations above the mean foot length for women).

Note that even though Ross' foot is longer than Candace's, Candace's foot is longer relative to their respective genders.
:::

```{tip}
Part (c) illustrates how z-scores become crucial when you want to *compare distributions*.
```

## Check Your Understanding: Computing z-Scores

Scores on the final exam in Professor Meyer's statistics class follow a normal distribution, with a mean of 82 and a standard deviation of 5.

:::{quiz} What is the z-score of an exam score of 87?
:hint: $z = (87 - 82)/5$.
:feedback-0: Correct! $z = 5/5 = +1$: the score is 1 standard deviation above the mean.
:feedback-1: -1 would be the z-score of 77, which is below the mean.
:feedback-2: 5 is the raw distance from the mean; divide by the standard deviation.
* *+1
* -1
* +5
:::

:::{quiz} What is the z-score of an exam score of 74.5?
:hint: $z = (74.5 - 82)/5$.
:feedback-0: Correct! $z = -7.5/5 = -1.5$: the score is 1.5 standard deviations below the mean.
:feedback-1: +1.5 would be the z-score of 89.5, above the mean.
:feedback-2: -7.5 is the raw deviation; divide by 5 to standardize it.
* *-1.5
* +1.5
* -7.5
:::

:::{quiz} A student's exam z-score is +2.2. What was the student's actual score?
:hint: $x = \mu + z\sigma = 82 + 2.2(5)$.
:feedback-0: Correct! $82 + 2.2(5) = 93$.
:feedback-1: 84.2 adds the z-score directly instead of multiplying it by the standard deviation first.
:feedback-2: 71 corresponds to $z = -2.2$, below the mean.
* *93
* 84.2
* 71
:::

:::{quiz} On a different exam, scores were normal with mean 75 and standard deviation 10. Maria scored 88 on that exam, and Tom scored 90 on Professor Meyer's exam (mean 82, SD 5). Who did better relative to their own class?
:hint: Compare z-scores: Maria (88-75)/10 vs. Tom (90-82)/5.
:feedback-0: Correct! Tom's $z = 1.6$ exceeds Maria's $z = 1.3$, so Tom did better relative to his class, even though the raw comparison is closer.
:feedback-1: Maria's z-score is $(88-75)/10 = 1.3$, which is lower than Tom's 1.6.
:feedback-2: The exams have different means and spreads, so raw scores can't be compared directly—that's exactly what z-scores are for.
* *Tom—his z-score (1.6) is higher than Maria's (1.3)
* Maria—her z-score is higher
* They cannot be compared
:::
