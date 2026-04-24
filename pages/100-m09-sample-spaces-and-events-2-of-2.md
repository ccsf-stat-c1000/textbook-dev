# Sample Spaces and Events (2 of 2)

```{admonition} Learning Objectives
    - Determine the sample space of a given random experiment.
```

So far, we have a random experiment and its sample space—the set of all possible outcomes it can produce. Where does probability come into the picture?

Once we have defined a random experiment, we can talk about an *event* of interest, which is a statement about the nature of the outcome that we're actually going to get once the experiment is conducted. Events are denoted by capital letters (other than S, which is reserved for the sample space).

```{admonition} Example: Tossing a Coin 3 Times
    Consider example 3, tossing a coin three times. Recall that the sample space in this case is:

    S = {HHH, THH, HTH, HHT, HTT, THT, TTH, TTT}

    We can define the following events:

    *Event A:* "Getting no H"

    *Event B:* "Getting exactly one H"

    *Event C:* "Getting at least one H"

    Note that each event is indeed a statement about the outcome that the experiment is going to produce.

    In practice, each event corresponds to some collection (subset) of the outcomes in the sample space:

    *Event A:* "Getting no H" → TTT

    *Event B:* "Getting exactly one H" → HTT, THT, TTH

    *Event C:* "Getting at least one H" → HTT, THT, TTH, THH, HTH, HHT, HHH

    Here is a visual representation of events A, B and C.

    ```{figure} images/image003.gif
    :alt: We have a large rectangle labeled "S" which represents the entirety of the sample space. Inside this rectangle we have two circles labeled "A" and "C." A contains only "TTT". Inside of C, we see "HHH," "THH," "HTH," "HHT," and a circle representing event B. Inside B are "HHT," "THT," and "TTH." Note that all of the items inside B are also inside C, so C fully encloses B.

    We have a large rectangle labeled "S" which represents the entirety of the sample space. Inside this rectangle we have two circles labeled "A" and "C." A contains only "TTT". Inside of C, we see "HHH," "THH," "HTH," "HHT," and a circle representing event B. Inside B are "HHT," "THT," and "TTH." Note that all of the items inside B are also inside C, so C fully encloses B.
    ```

    From this visual representation of the events, it is easy to see that event B is totally included in event C, in the sense that every outcome in event B is also an outcome in event C. Also, note that event A stands apart from events B and C, in the sense that they have no outcome in common, or no overlap. At this point these are only noteworthy observations, but as you'll discover later, they are very important ones.
```

```{admonition} Example: Staff Position
    Consider Example 6, where we choose two candidates at random out of four (Ann, Beth, Jim and Dan). Recall that in this case the sample space is:

    S = { (Ann, Beth), (Ann, Jim), (Ann, Dan), (Beth, Jim), (Beth, Dan), (Jim, Dan) }

    In this example, we might be interested in the following events, each of which is a statement about the nature of the outcome that the random experiment will produce:

    *Event A*: "Jim is chosen."

    *Event B:* "The two chosen are of the same gender."

    Again, each event corresponds to some collection of outcomes. Use the exercise below to try this yourself:

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

Once an event is defined, we can talk about the probability that it will occur. So, if we have defined an *Event A*, we can use the notation we previously mentioned to represent its probability, namely *P(A)*.

The following figure summarizes the information in this section:

```{figure} images/image004.gif
:alt: A flow chart. We start with a Random Experiment, which leads to a Sample Space, called S. Then, we define Events (A, B, C...) which correspond to a collection of outcomes in S. After that, we obtain the probability of the events, resulting in P(A), P(B),...

A flow chart. We start with a Random Experiment, which leads to a Sample Space, called S. Then, we define Events (A, B, C...) which correspond to a collection of outcomes in S. After that, we obtain the probability of the events, resulting in P(A), P(B),...
```

## Section Questions

```{note}
    **My Response**

    About Sample Spaces and Events

    *(Interactive activity — available in the OLI platform)*
```
