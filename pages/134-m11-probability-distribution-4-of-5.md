# Probability Distribution (4 of 5)

```{admonition} Learning Objectives
:class: note

- Find the probability distribution of discrete random variables, and use it to find the probability of events of interest.
```

We've seen how probability distributions are created. Now it's time to use them to find probabilities.

:::{admonition} Example: Changing Majors
:class: tip

A random sample of graduating seniors was surveyed just before graduation. One question that was asked is: How many times did you change majors? The results are displayed in a probability distribution:

| x | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| P(X = x) | 0.28 | 0.37 | 0.23 | 0.09 | 0.02 | 0.01 |

Using this probability distribution we can answer probability questions such as: What is the probability that a randomly selected senior has changed majors more than once? This can be written as P(X > 1).

More than once would be translated to:

P(X > 1) = P(X = 2) + P(X = 3) + P(X = 4) + P(X = 5) = 0.23 + 0.09 + 0.02 + 0.01 = 0.35
:::

As you just saw in this example, we need to pay attention to the wording of the probability question. The key words that told us which values to use for X are *more than*. The following will clarify and reinforce the *key words* and their meanings.

## Key Words

Let's begin with some everyday situations using *at least* and *at most*.

Suppose someone said to you, "I need you to write *at least 10 pages* for a term paper." What does this mean? It means that 10 pages is the smallest amount you are going to write. In other words, you will write *10 or more* pages for the term paper. This would be the same as saying, "*not less than* 10 pages." So, for example, writing 9 pages would be unacceptable.

On the other hand, suppose you are considering the number of children you will have. You want *at most 3 children*. This means that 3 children is the most that you wish to have. In other words, you will have *3 or fewer* children. This would be the same as saying, "*not more than* 3 children." So, for example, you would not want to have 4 children.

The following table gives a list of some key words to know. Suppose a random variable X had possible values of 0–5.

| Key Words | Meaning | Symbols | Values for X |
| --- | --- | --- | --- |
| more than 2 | strictly larger than 2 | X > 2 | 3, 4, 5 |
| no more than 2 | 2 or fewer | X ≤ 2 | 0, 1, 2 |
| fewer than 2 | strictly smaller than 2 | X < 2 | 0, 1 |
| no less than 2 | 2 or more | X ≥ 2 | 2, 3, 4, 5 |
| at least 2 | 2 or more | X ≥ 2 | 2, 3, 4, 5 |
| at most 2 | 2 or fewer | X ≤ 2 | 0, 1, 2 |
| exactly 2 | 2, no more or no less, only 2 | X = 2 | 2 |

Now try these questions, using the changing-majors distribution above, to see if you get the idea.

## Concept Check

:::{quiz} What is the probability that a randomly selected senior changed majors at most once?
:hint: "At most 1" means X ≤ 1: add P(X = 0) and P(X = 1).
:feedback-0: Correct! P(X ≤ 1) = 0.28 + 0.37 = 0.65.
:feedback-1: 0.37 is only P(X = 1); "at most once" includes those who never changed majors.
:feedback-2: 0.35 is P(X > 1), the complement of this event.
* *0.65
* 0.37
* 0.35
:::

:::{quiz} What is the probability that a randomly selected senior changed majors fewer than 2 times?
:hint: "Fewer than 2" means X < 2, i.e., X = 0 or 1.
:feedback-0: Correct! P(X < 2) = 0.28 + 0.37 = 0.65—the same event as "at most 1."
:feedback-1: 0.88 would be P(X ≤ 2); "fewer than 2" excludes 2 itself.
:feedback-2: 0.23 is P(X = 2), which is excluded by "fewer than 2."
* *0.65
* 0.88
* 0.23
:::

:::{quiz} What is the probability that a senior changed majors at least 3 times?
:hint: "At least 3" means X ≥ 3.
:feedback-0: Correct! P(X ≥ 3) = 0.09 + 0.02 + 0.01 = 0.12.
:feedback-1: 0.09 is only P(X = 3); include 4 and 5 as well.
:feedback-2: 0.03 is P(X ≥ 4).
* *0.12
* 0.09
* 0.03
:::

Before we move on to the next section on the means and variances of a probability distribution, let's revisit the changing majors example:

:::{admonition} Question & Answer
:class: important

**Question:** Based upon this distribution, do you think it would be unusual to change majors 2 or more times?

**Answer:** P(X ≥ 2) = 0.35. So, 35% of the time a student changes majors 2 or more times. This means that it is not unusual to do so.

**Question:** Do you think it would be unusual to change majors 4 or more times?

**Answer:** P(X ≥ 4) = 0.03. So, 3% of the time a student changes majors 4 or more times. This means that it is fairly unusual to do so.
:::

After we learn about means and standard deviations, we will have another way to answer these types of questions.
