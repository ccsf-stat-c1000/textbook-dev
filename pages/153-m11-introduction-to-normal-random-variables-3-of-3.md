# Introduction to Normal Random Variables (3 of 3)

```{admonition} Learning Objectives
    - Find probabilities associated with the normal distribution.
```

Let's go back to our example of foot length:

How likely or unlikely is it for a male's foot length to be more than 13 inches?

```{figure} images/image129.gif
:alt: The probability distribution curve for foot lengths. It takes the shape of a normal bell curve. The boundaries for the first, second, and third standard deviations have been marked, and we see that no line falls on X=13 . We need the area under the bell curve to the right of X=13 .

The probability distribution curve for foot lengths. It takes the shape of a normal bell curve. The boundaries for the first, second, and third standard deviations have been marked, and we see that no line falls on X=13 . We need the area under the bell curve to the right of X=13 .
```

Since 13 inches doesn't happen to be exactly 1, 2, or 3 standard deviations away from the mean, we would only be able to give a very rough estimate of the probability at this point. Clearly, the Standard Deviation Rule only describes the tip of the iceberg, and while it serves well as an introduction to the normal curve, and gives us a good sense of what would be considered likely and unlikely values, it is very limited in the probability questions it can help us answer.

Here is another familiar normal distribution:

```{figure} images/image_normal_sat1.jpg
:alt: A normal bell curve representing the probability distribution curve for the scores on the math portion of the SAT. The horizontal axis is labeled "X - SAT scores." μ = 500, and σ = 100 . We want to know the probability that a student scores 633 or higher. This is the area under the bell curve to the right of X=633 . Note that 633 is not covered by the Standard Deviation Rule.

A normal bell curve representing the probability distribution curve for the scores on the math portion of the SAT. The horizontal axis is labeled "X - SAT scores." μ = 500, and σ = 100 . We want to know the probability that a student scores 633 or higher. This is the area under the bell curve to the right of X=633 . Note that 633 is not covered by the Standard Deviation Rule.
```

Suppose we are interested in knowing the probability that a randomly selected student will score 633 or more on the math portion of his or her SAT (this is represented by the red area). Again, 633 does not fall exactly 1, 2, or 3 standard deviations above the mean. Notice, however, that an SAT score of 633 and a foot length of 13 are both about 1/3 of the way between 1 and 2 standard deviations. As you continue to read this page, you'll realize that this positioning relative to the mean is the key to finding probabilities.

## Finding Probabilities for a Normal Random Variable

As we saw, the Standard Deviation Rule is very limited in helping us answer probability questions, and basically limited to questions involving values that fall exactly 1, 2, and 3 standard deviations away from the mean. How do we answer probability questions in general? The key is the position of the value relative to the mean, measured in standard deviations.

We can approach the answering of probability questions two possible ways: a table and technology. In the next sections, you will learn how to use the "standard normal table," and then how the same calculations can be done with technology.

## Standardizing Values

The first step to assessing a probability associated with a normal value is to determine the *relative* value with respect to all the other values taken by that normal variable. This is accomplished by determining how many standard deviations below or above the mean that value is.

```{admonition} Example: Foot Length
    How many standard deviations below or above the mean male foot length is 13 inches? Since the mean is 11 inches, 13 inches is 2 inches above the mean. Since a standard deviation is 1.5 inches, this would be 2 / 1.5 = 1.33 standard deviations above the mean. Combining these two steps, we could write:

    (13 in. - 11 in.) / (1.5 inches per standard deviation) = (13 - 11) / 1.5 standard deviations = +1.33 standard deviations.
```

In the language of statistics, we have just found the *z-score*for a male foot length of 13 inches to be z = +1.33. Or, to put it another way, we have *standardized* the value of 13. In general, the standardized value z tells how many standard deviations below or above the mean the original value is, and is calculated as follows:

*z-score = (value - mean)/standard deviation*

The convention is to denote a value of our normal random variable X with the letter "x." Since the mean is written $\mu$ and the standard deviation $\sigma$, we may write the standardized value as $z=\frac{x−\mu}{\sigma}$

Notice that since $\sigma$ is always positive, for values of x above the mean ($\mu$), z will be positive; for values of x below $\mu$, z will be negative.

```{figure} images/image131.gif
:alt: The probability distribution curve for male foot length. We see that the mean (μ) is 11 and that 13 has been marked on the horizontal axis.

The probability distribution curve for male foot length. We see that the mean (μ) is 11 and that 13 has been marked on the horizontal axis.
```

```{figure} images/image132.gif
:alt: The same probability distribution curve as the above image, except that the horizontal axis now represents "standardized foot length z." The location where the mean used to be is now labeled with the z-score of the mean, which is 0. The location of 13 is now labeled 13's z-score, which is 1.33 .

The same probability distribution curve as the above image, except that the horizontal axis now represents "standardized foot length z." The location where the mean used to be is now labeled with the z-score of the mean, which is 0. The location of 13 is now labeled 13's z-score, which is 1.33 .
```

```{admonition} Example: Standardizing Foot Measurements
    Let's go back to our foot length example, and answer some more questions.

    *(a)* What is the standardized value for a male foot length of 8.5 inches? How does this foot length relate to the mean?

    z = (8.5 - 11) / 1.5 = -1.67. This foot length is 1.67 standard deviations *below* the mean.

    *(b)* A man's standardized foot length is +2.5. What is his actual foot length in inches? If z = +2.5, then his foot length is 2.5 standard deviations above the mean. Since the mean is 11, and each standard deviation is 1.5, we get that the man's foot length is: 11 + 2.5(1.5) = 14.75 inches.

    z-scores also allow us to compare values of different normal random variables. Here is an example:

    *(c)* In general, women's foot length is shorter than men's. Assume that women's foot length follows a normal distribution with a mean of 9.5 inches and standard deviation of 1.2. Ross' foot length is 13.25 inches, and Candace's foot length is only 11.6 inches. Which of the two has a longer foot relative to his or her gender group?

    To answer this question, let's find the z-score of each of these two normal values, bearing in mind that each of the values comes from a different normal distribution.

    Ross: z-score = (13.25 - 11) / 1.5 = 1.5 (Ross' foot length is 1.5 standard deviations above the mean foot length for men).

    Candace: z-score = (11.6 - 9.5) / 1.2 = 1.75 (Candace's foot length is 1.75 standard deviations above the mean foot length for women).

    Note that even though Ross' foot is longer than Candace's, Candace's foot is longer relative to their respective genders.
```

```{tip}
:class: tip
    *Part (c)* illustrates how z-scores become crucial when you want to *compare distributions*.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

Scores on the final exam in Professor Meyer's statistics class follow a normal distribution, with a mean of 82 and a standard deviation of 5.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
