# Events: Subsets of the Sample Space

So far, we have a random experiment and its sample space—the set of all possible outcomes it can produce. Where does probability come into the picture?

Once we have defined a random experiment, we can talk about an *event* of interest, which is a statement about the nature of the outcome that we're actually going to get once the experiment is conducted. Events are denoted by capital letters (other than S, which is reserved for the sample space).

::::{admonition} Example: Tossing a Coin 3 Times
:class: tip

Consider example 3, tossing a coin three times. Recall that the sample space in this case is:

S = {HHH, THH, HTH, HHT, HTT, THT, TTH, TTT}

We can define the following events:

- *Event A:* "Getting no H"
- *Event B:* "Getting exactly one H"
- *Event C:* "Getting at least one H"

Note that each event is indeed a statement about the outcome that the experiment is going to produce.

In practice, each event corresponds to some collection (subset) of the outcomes in the sample space:

- *Event A:* "Getting no H" → TTT
- *Event B:* "Getting exactly one H" → HTT, THT, TTH
- *Event C:* "Getting at least one H" → HTT, THT, TTH, THH, HTH, HHT, HHH

Here is a visual representation of events A, B and C:

```{figure} images/gen/m09-events-venn.svg
:alt: A rectangle labeled S represents the sample space. A red circle labeled A contains only TTT. A large blue ellipse labeled C contains HHH, THH, HTH, HHT and, nested completely inside it, a green ellipse labeled B containing HTT, THT, and TTH. B is entirely contained in C, and A does not overlap either one.
```

From this visual representation of the events, it is easy to see that event B is totally included in event C, in the sense that every outcome in event B is also an outcome in event C. Also, note that event A stands apart from events B and C, in the sense that they have no outcome in common, or no overlap. At this point these are only noteworthy observations, but as you'll discover later, they are very important ones.
::::

::::{admonition} Example: Staff Position
:class: tip

Consider Example 6, where we choose two candidates at random out of four (Ann, Beth, Jim and Dan). Recall that in this case the sample space is:

S = { (Ann, Beth), (Ann, Jim), (Ann, Dan), (Beth, Jim), (Beth, Dan), (Jim, Dan) }

In this example, we might be interested in the following events, each of which is a statement about the nature of the outcome that the random experiment will produce:

- *Event A*: "Jim is chosen."
- *Event B:* "The two chosen are of the same gender."

Again, each event corresponds to some collection of outcomes. Try it yourself:

:::{quiz} Which outcomes make up event A, "Jim is chosen"?
:hint: Find every pair in the sample space that includes Jim.
:feedback-0: Correct! Jim appears in exactly three pairs: (Ann, Jim), (Beth, Jim), and (Jim, Dan).
:feedback-1: (Ann, Beth) does not include Jim.
:feedback-2: (Jim, Dan) also includes Jim and must be part of the event.
* *(Ann, Jim), (Beth, Jim), (Jim, Dan)
* (Ann, Beth), (Ann, Jim), (Beth, Jim)
* (Ann, Jim), (Beth, Jim)
:::

:::{quiz} Which outcomes make up event B, "The two chosen are of the same gender"? (Ann and Beth are women; Jim and Dan are men.)
:hint: Find pairs of two women or two men.
:feedback-0: Correct! The only same-gender pairs are (Ann, Beth), the two women, and (Jim, Dan), the two men.
:feedback-1: (Ann, Jim) is a mixed pair—one woman and one man.
:feedback-2: (Beth, Dan) is also a mixed pair.
* *(Ann, Beth) and (Jim, Dan)
* (Ann, Beth), (Ann, Jim), and (Jim, Dan)
* (Ann, Beth), (Beth, Dan), and (Jim, Dan)
:::
::::

Once an event is defined, we can talk about the probability that it will occur. So, if we have defined an *Event A*, we can use the notation we previously mentioned to represent its probability, namely *P(A)*.

The following figure summarizes the information in this section:

```{figure} images/gen/m09-experiment-flow.svg
:alt: A flow chart: a random experiment leads to a sample space S, events A, B, C are defined as collections of outcomes in S, and finally we obtain the probabilities of the events, P(A), P(B), and so on.
```
