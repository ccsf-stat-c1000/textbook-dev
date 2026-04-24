# Probability Rules (8 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

## Comment: Finding the Probability of "At least one of
                ..."

Recall that when we talked about the Complement Rule, we mentioned that we would come back to it later and illustrate its strength. Well, the time has come to do that.

Rule 3: The Complement Rule, P(A) = 1 - P(not A), together with the Multiplication Rule, is *extremely* useful for finding the probability of events like "at least one of ..." in several repetitions of a random experiment.

For example,

- 10 people were randomly chosen. Find P(at least one of the 10 has blood type
                        O).
- A student uses a random guess to answer 10 true/false questions
                        on
                        a test. Find P(the student gets at least one question right).

The key here is to use the fact that the complement event is much easier to deal with than the actual event of interest. Going back to our example:

The complement to *"at least one of* the 10 has blood type O" is *"none* of the 10 has blood type O."

The complement to "getting *at least one* question right" is "getting *none* of the questions right."

(Note how "at least one of" changes to "none" in the complement.)

If you feel unsure about this, go back and redo the "Did I Get This" activity on page 2 of the Probability Rules section.

We'll start with a very simple example in which it is still manageable to find P(at least one of ...) directly, without using the complement rule. Then we'll alter the example slightly and see how trying to find P(at least one of ...) directly can get *VERY COMPLICATED*, and how the complement rule comes to the rescue. Finally, you'll check your understanding by attempting to solve a similar problem yourself.

```{admonition} Example
    Two people are selected at random. What is the probability that at least one of them has blood type O?

    Here is our sample space S = { (O,O) (O, not O) (not O, O) (not O, not O) }

    The event "at least one person chosen has blood type O" consists of the first three possible outcomes, and therefore:

    P(at least one person chosen has blood type O) = P((O and O) or (O and not O) or (not O and O)) = (.44 * .44) + (.44 * .56) + (.56 * .44) = .6864.
```

Now we'll just alter the example slightly by randomly choosing 10 people instead of 2:

```{admonition} Example
    A patient with blood type O desperately needs a blood transfusion. Since a person with blood type O can receive blood only from another person who has blood type O, the blood bank decides to choose 10 donors at random and hope that at least one of them has blood type O. Find P(at least one of the 10 donors has blood type O). To make things simpler, let's denote the event "at least one has blood type O" by L (for at *L*east).

    Solving this using the brute force method would require a prohibitive amount of work. As before, we would need to list all the possible outcomes of blood types of 10 people (using either "O" or "not O"), but this time there are 1,024 of them! We would then need to identify those outcomes that L consists of (i.e., the outcomes in which at least one of the 10 people has blood type O). Next, we would need to find the probability of each of those outcomes and add those probabilities up. *What a pain!* There must be a better way.

    Instead of doing all the work listed above, we can use the Complement Rule, which says P(L) = 1 - P(not L). As we explained before, in this case "not L" is the event "none of the 10 have blood type O," or in other words that all 10 have a blood type other than O. So we can simply solve (using our regular notation from this module):

    P(L) = 1 - P(not L) = 1 - P(not O1 *and* not O2 *and* not O3 *and* not O4 *and* not O5 *and* not O6 *and* not O7 *and* not O8 *and* not O9 *and*not O10). Now, using the multiplication rule, = 1 - (.56 * .56 * .56 * .56 * .56 * .56 * .56 * .56 * .56 * .56) = 1 - .003 = .997.

    Therefore, it is almost certain that if we choose 10 people at random, we'll find that at least one of them has blood type O. This result makes sense, since 44% have blood type O, and so out of 10 people it is almost certain that at least one will have blood type O.
```

The purpose of the following activity is to guide you through another problem that involves finding P(at least one of ... ).

## Learn By Doing

A quiz consists of 10 multiple-choice questions, each with 4 possible answers, only one of which is correct. A student who does not attend lectures on a regular basis has no clue what the answers are, and therefore uses an independent random guess to answer each of the 10 questions. What is the probability that the student gets at least one question right?

Let's decide on some notations.

Let L be the event that the student gets at least one of the questions right.

We'll use R for getting a question right and W for getting it wrong (W is essentially "not R").

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
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
