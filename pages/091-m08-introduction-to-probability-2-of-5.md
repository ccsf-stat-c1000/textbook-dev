# The Birthday Problem: A Surprising Answer

```{admonition} Learning Objectives
:class: note

- Relate the probability of an event to the likelihood of this event occurring.
```

:::{admonition} Example: The Birthday Problem
:class: tip

Suppose that you are at a party with 59 other people (for a total of 60). What are the chances (or, what is the probability) that at least 2 of the 60 guests share the same birthday?

To clarify, by "share the same birthday," we mean that 2 people were born on the same date, not necessarily in the same year. Also, for the sake of simplicity, ignore leap years, and assume that there are 365 days in each year.

Take a guess before reading on: 10%? 50%? 90%?

Indeed, there is a 99.4% chance that at least 2 of the 60 guests share the same birthday. In other words, it is *almost certain* that at least 2 of the guests share the same birthday. This is very counterintuitive.

Unlike the *Let's Make a Deal* example, for this scenario, we don't really have a good step-by-step explanation that will give you insight into this surprising answer. Later in this section, we will revisit this example and explain the solution.
:::

## Check Your Understanding: The Birthday Problem

:::{quiz} With 60 people at a party, the probability that at least two share a birthday is 99.4%. Why do most people guess this probability to be much lower?
:hint: People tend to think about someone matching *their own* birthday.
:feedback-0: Correct! People instinctively think of the chance that someone matches one specific birthday (their own), which is indeed small—but the question counts a match between *any* pair, and 60 people form 1,770 pairs.
:feedback-1: The calculation assumes all 365 days are equally likely; the surprise doesn't come from unequal birthdays.
:feedback-2: 60 out of 365 sounds small, but what matters is the number of *pairs* of people, which is large.
* *They think of matching one specific birthday, but the question is about any match among all 1,770 pairs
* Birthdays are not equally spread across the year
* The answer is actually wrong—the true probability is about 16%
:::

From these two examples, you have seen that your original hunches cannot always be counted upon to give you correct predictions of probabilities.

In general, *probability is not always intuitive*.

Even though these two examples are definitely from the "harder" end of the complexity spectrum, hopefully they have motivated you to learn more about probability. We will need to further expand and extend our understanding of probability. Eventually we will need to develop a more formal approach to probability, but we will begin with an informal discussion of what probability is.
