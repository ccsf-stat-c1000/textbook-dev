# Equally Likely Outcomes: Counting Your Way to Probability

```{admonition} Learning Objectives
:class: note

- Find the probability of events in the case in which all outcomes are equally likely.
```

In the Introduction to Probability, we learned how the relative frequency approach can be used to estimate the probability of an event. While sometimes this is the only method that can be used to estimate probability (such as when figuring out the probabilities of the occurrence of different blood types among the population), this method requires a lot of time and effort, especially since in order to get reliable estimates we need to repeat the random experiment many times. We are now moving on to a different method, which can be applied in cases in which the random experiment produces outcomes that are all equally likely. We'll start with a simple example to introduce the idea of the method, and then move on to more interesting examples.

:::{admonition} Example: Rolling a Fair Die
:class: tip

When an ordinary fair die is rolled once, what is the probability that the number rolled is even? We'll denote this event by E (for even), so we are interested in finding P(E). Let's analyze this problem:

- The random experiment is rolling a fair die once.
- The sample space of all possible outcomes in this case is S = {1, 2, 3, 4, 5, 6}.
- Since the die is fair, this means that all 6 possible outcomes are *equally likely* (each having a probability of 1/6 of occurring).
- We are interested in a particular type of outcome, which is represented by event E—getting an even number.

Since 3 out of the 6 equally likely outcomes make up the event E (the outcomes {2, 4, 6}), the probability of event E is simply P(E) = 3/6.
:::

## Let's Generalize

In the special situation where all the outcomes in S are equally likely, we can find the probability of any event A by dividing the number of outcomes in A by the number of outcomes in S:

$$P(A) = \frac{\text{number of outcomes in A}}{\text{number of outcomes in S}}$$

The purpose of the next activity is to give you guided practice on how to find the probability of an event in situations in which all the possible outcomes are equally likely.

## Learn By Doing

A couple is planning to have 3 children. Assuming that having a boy and having a girl are equally likely, and that the gender of one child has no influence on (or, is independent of) the gender of another, what is the probability that the couple will have exactly 2 girls?

The "random experiment" in this case is having 3 children, as odd as that may sound in this context. The next and most important step is to determine what all of the possible outcomes are, and list them (i.e., list the sample space S). In this case, each outcome represents a possible combination of genders of 3 children (note that examples with the same number of boys and girls but a different birth order must be listed separately).

:::{quiz} How many equally likely outcomes are in the sample space for the genders of 3 children (in birth order)?
:hint: Each of the 3 children can be a boy or a girl: 2 × 2 × 2.
:feedback-0: 6 would be the count if order didn't matter and repeats were excluded—but each birth is a separate two-way choice.
:feedback-1: Correct! S = {BBB, BBG, BGB, GBB, BGG, GBG, GGB, GGG}—8 outcomes, all equally likely.
:feedback-2: 4 is the number of outcomes for 2 children; here there are 3 children.
* 6
* *8
* 4
:::

:::{quiz} Which outcomes make up the event "exactly 2 girls"?
:hint: Find the sequences containing exactly two G's and one B.
:feedback-0: Correct! The boy can be born first, second, or third: BGG, GBG, GGB.
:feedback-1: GGG has three girls, not exactly two.
:feedback-2: There are three such outcomes, one for each position the boy can occupy.
* *BGG, GBG, GGB
* BGG, GBG, GGB, GGG
* BGG and GGB only
:::

:::{quiz} So what is the probability that the couple will have exactly 2 girls?
:hint: Divide the number of outcomes in the event by the total number of equally likely outcomes.
:feedback-0: Correct! P(exactly 2 girls) = 3/8.
:feedback-1: 1/2 would ignore the actual counts; only 3 of the 8 outcomes have exactly two girls.
:feedback-2: 2/8 misses one of the three arrangements of two girls and one boy.
* *3/8
* 1/2
* 2/8
:::
