# Why Intuition Fails: The Need for Probability Tools

```{admonition} Learning Objectives
:class: note

- Relate the probability of an event to the likelihood of this event occurring.
```

Now that we understand how probability fits into the Big Picture as a key element behind statistical inference, we are ready to learn more about it. Our first goal is to introduce some fundamental terminology (the language) and notation that is used when discussing probability. Before we do that, though, let's start with two fun examples that explain the reasons for the careful treatment that we give probability in this course.

Often, relying only on our intuition is not sufficient to determine probability, so we need some tools to work with, which is exactly what we study in this section.

Here are two examples:

:::{admonition} Example: The "Let's Make a Deal" Paradox
:class: tip

*Let's Make a Deal* was a popular television game show, which first aired in the 1960s. The *Let's Make a Deal* paradox is named after that show. In the show, the contestant had to choose between three doors. One of the doors had a big prize behind it such as a car or a lot of cash, and the other two were empty. (Actually, for entertainment's sake, each of the other two doors had some silly gift behind it, like a goat or a chicken, but we'll refer to them here as empty.)

The contestant had to choose one of the three doors, but instead of revealing the chosen door, the host revealed one of the two unchosen doors to be empty. At this point in the game, there were two unopened doors: the door that the contestant had originally chosen and the remaining unchosen door. One of them had the prize behind it.

The contestant was given the option either to *stay* with the door that he or she had initially chosen or *switch* to the other door.

What do you think the contestant should do, stay or switch? What do you think is the probability that you will win the big prize if you stay? What about if you switch?

The intuition of most people is that each of the two doors is equally likely to contain the prize—that there is a 50-50 chance of winning with either selection. This, however, is not the case. Actually, there is a 67% chance—or a probability of 2/3 (2 out of 3)—of winning by switching, and only a 33% chance—or a probability of 1/3 (1 out of 3)—of winning by staying with the door that was originally chosen. This means that a contestant is twice as likely to win if he or she switches to the unchosen door. Isn't this a bit counterintuitive and confusing? Most people think so when they are first faced with this problem. We will now try to explain this paradox to you in two different ways:

```{note} Video

[The "Let's Make a Deal" Paradox Part 1](https://www.youtube.com/watch?v=e7c6_h0Zf6U)
```

If you are still not convinced (or even if you are), here is a different way of explaining the paradox:

```{note} Video

[The "Let's Make a Deal" Paradox Part 2](https://www.youtube.com/watch?v=e3cCUAGHIOI)
```
:::

## Check Your Understanding: The Monty Hall Problem

:::{quiz} In the "Let's Make a Deal" game, your first pick is door 1. The host, who knows where the prize is, opens door 3 to reveal it is empty. Why is switching to door 2 the better strategy?
:hint: What was the probability that your first pick was right, and did the host's action change that?
:feedback-0: Correct! Your original pick wins with probability 1/3, so the prize is behind one of the other doors with probability 2/3—and the host's reveal concentrates that entire 2/3 on the remaining door.
:feedback-1: The two remaining doors are not equally likely: the host's choice of which door to open depends on where the prize is, which breaks the symmetry.
:feedback-2: Switching is better regardless of any pattern in the host's behavior across episodes—the 2/3 advantage comes from the rules of the game itself.
* *Your first pick wins only 1/3 of the time, so the other unopened door must win 2/3 of the time
* The two remaining doors are equally likely, so switching doesn't matter
* Hosts tend to put prizes behind door 2 more often
:::

If this example still did not persuade you that probability is not always intuitive, the next example should definitely do the trick.
