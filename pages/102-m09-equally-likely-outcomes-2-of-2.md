# Equally Likely Outcomes (2 of 2)

```{admonition} Learning Objectives
    - Find the probability of events in the case in which all outcomes are equally likely.
```

Here is a more interesting example:

```{admonition} Example
    A certain college recently announced 2 job openings in its admissions office. From all the applicants, a search committee identified 5 candidates—2 men and 3 women—who seemed equally qualified. Priding itself on a long history as an equal opportunity employer, the college would like to continue that tradition and make the 2 appointments at random. The college's legal department, though, has cautioned the personnel office that doing so may not be a good idea. If the 2 chosen happen to be of the same gender, the selection process will seem to be discriminatory, and the college may become embroiled in expensive litigation. What is the probability that the random selection will result in both chosen candidates having the same gender, and will thus appear to be discriminatory? We'll denote this event by D (for discriminatory).

    Let's identify the 2 men and 3 women as M1, M2, F1, F2 and F3.

    Our random experiment is choosing 2 out of these 5 candidates at random, and the sample space of all possible outcomes of this random experiment is therefore:

    S = { (M1, M2), (M1, F1), (M1, F2), (M1, F3), (M2, F1), (M2, F2), (M2, F3), (F1, F2), (F1, F3), (F2, F3) }.

    ```{figure} images/image008.gif
    ```

    Note that because the order in which the selection is made does not matter, and because 2 candidates are being chosen and they are listed in S as pairs, once we've included (M1, M2) in S, we should not also include (M2, M1). Both represent the same outcome: M1 and M2 are the two that were chosen to get the jobs.

    Thus S consists of 10 outcomes, all equally likely, since the selection of any 2 out of the 5 has been done at random.

    We are interested in event D—that the selection process will appear to be discriminatory, or in other words that the two chosen will be of the same gender. Event D consists of 4 of the 10 possible outcomes:

    D = { (M1,M2), (F1,F2), (F1,F3), (F2,F3) }

    ```{figure} images/image009.gif
    ```

    The probability that the selection will appear to be discriminatory is therefore:

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

## Comment

It should be noted that in this example it was still manageable to list all the possible outcomes, and then count the number of outcomes that are in event D. If we were to change the example slightly, and needed to choose 2 candidates out of, say, 10 (instead of 5), the number of possible outcomes would grow substantially (from 10 to 45) and listing all of those outcomes would be quite time-consuming and tiresome. Later in the probability section we will learn some simple counting methods that will allow us to figure out the number of possible outcomes without actually listing them.

## Did I Get This?

A flight has been overbooked; however, there are 2 seats available—one in business class and one in first class. The ground crew decides to upgrade 2 of the coach (regular class) passengers so that 2 more passengers will be able to get on the flight. The crew has identified 4 passengers, 2 males and 2 females, who are traveling by themselves and who have been loyal frequent fliers on the airline. They decide to choose 2 of those passengers at random for the upgrade. The first chosen will be upgraded to first class, and the second chosen will be upgraded to business class. We'll denote the 2 males and 2 females (as before) with M1, M2, F1 and F2.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

It is important to note that it is not always the case the all the outcomes of a random experiment are equally likely.

A common mistake among students who are exposed to probability for the first time is to assume that all the outcomes of a random experiment are equally likely when in fact they are not.

Here is an example.

```{admonition} Example
    A fair coin is tossed repeatedly until the first ‘H’ is obtained but no more than three times. In this experiment there are four possible outcomes: Getting ‘H’ in the first toss, getting the first ‘H’ in the second toss, getting the first ‘H’ in the third toss, or tossing the coin three times without getting a ‘H’. The sample space in this case is therefore:

    ```{figure} images/fair_coin.png
    ```

    As mentioned above, a common mistake is to wrongly assume that the four outcomes are equally likely, each with probability ¼.

    Note that the first outcomes ‘H’ has probability ½ (since it represents the outcome of tossing the fair coin once and getting ‘H’). If the first outcome has probability ½, it is clear that the outcomes cannot be equally likely since the sum of the probabilities of all outcomes must be 1.
```

## To Summarize

In the special case when all the outcomes of a random experiment are equally likely, there is a simple way to calculate the probability of any event by counting how many of the outcomes satisfy or make up the event, and dividing it by the total number of outcomes in the sample space.

Remember, it is not always the case that the outcomes are equally likely, so make sure to check if they are before applying this method to calculate probabilities. In the next modules you’ll learn other methods which will help you compute probabilities more generally.
