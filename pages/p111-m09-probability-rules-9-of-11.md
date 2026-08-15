# The General Addition Rule: Handling Overlap

We are now getting to the last rule in this module, in which we'll go back to P(A or B).

So far, we've introduced the Addition Rule for finding P(A or B) in the special case when A and B are *disjoint* events—that is, when the events cannot happen together, so P(A and B) = 0. In this special case, P(A or B) refers to the probability of either event A occurring or event B occurring, and we said that P(A or B) = P(A) + P(B). Visually, in the disjoint Venn diagram, P(A or B) can be found by adding the areas of the two non-overlapping circles.

As we mentioned above, the case when A and B are disjoint is a special case, and in many situations the events are *not disjoint*—they can occur at the same time:

```{figure} images/gen/m09-disjoint-venn.svg
:alt: Two Venn diagrams side by side, one showing disjoint events as separate circles, the other showing events that are not disjoint as overlapping circles whose overlap means both can occur together.
```

We are now ready to learn how to find P(A or B) in this more general case—when A and B are not necessarily disjoint. We'll call this rule the "General Addition Rule."

Before we introduce this rule through an example, it is important to understand what P(A or B) represents in the case when A and B are not disjoint. P(A or B) is represented by the total area covered by the two circles, which in this case includes an overlap corresponding to the probability that both events A and B occur. This difference has an important implication for the meaning of P(A or B) when A and B are not disjoint:

When A and B are not disjoint, P(A or B) means P(A occurs or B occurs or both events occur).

:::{admonition} Example: Overnight Delivery
:class: tip

It is vital that a certain document reach its destination within one day. To maximize the chances of on-time delivery, two copies of the document are sent using two services, service A and service B. It is known that the probabilities of on-time delivery are:

- 0.90 for service A (*P(A) = 0.90*)
- 0.80 for service B (*P(B) = 0.80*)
- 0.75 for both services being on time (*P(A and B) = 0.75*)

(Note that A and B are *not disjoint*. They can happen together with probability 0.75.)

In the context of this problem, the obvious question of interest is:

*What is the probability of on-time delivery of the document using this strategy (of sending it via both services)?*

The document will reach its destination on time as long as it is delivered on time by service A or by service B or by both services. In other words, when event A occurs or event B occurs or both occur, so P(on-time delivery using this strategy) = *P(A or B)*.

We can find P(A or B) by adding P(A) (the left circle) and P(B) (the right circle), and then subtracting P(A and B) (the overlap), since we included it twice, once as part of P(A) and once as part of P(B):

```{figure} images/gen/m09-general-addition.svg
:alt: Three Venn diagram panels showing that P(A or B) equals P(A), shaded in the first panel, plus P(B), shaded in the second panel, minus P(A and B), the overlap shaded in the third panel, because the overlap is counted twice when the two circles are added.
```

If we apply this to our example, we find that:

P(A or B) = P(on-time delivery using this strategy) = $0.90 + 0.80 - 0.75 = 0.95$.

So our strategy of using two delivery services increases our probability of on-time delivery to 0.95.
:::

After this example, the following General Addition Rule for finding P(A or B) should not be surprising:

```{admonition} Rule 6: The General Addition Rule
:class: note

*For any 2 events A and B, P(A or B) = P(A) + P(B) - P(A and B).*
```

*Comment:*

As we mentioned above, P(A or B) = P(A occurs or B occurs or both occur). Another way to interpret P(A or B) is therefore P(at least one of the two events occurs). (Later on this page we'll make the connection to the "at least one of..." type problems we discussed on the previous page.)

## Check Your Understanding: The General Addition Rule

Suppose that Jim is applying to two colleges: College A, an "Ivy League" school, and College B, a state university. Based on his credentials and the requirements of the two colleges, Jim estimates his chances with the following probabilities:

- Probability that he will be admitted to college A is 0.10.
- Probability that he will be admitted to college B is 0.75.
- Probability that he will be admitted to both colleges is 0.05.

:::{quiz} What is the probability that Jim is admitted to at least one of the two colleges?
:hint: Use the General Addition Rule: P(A or B) = P(A) + P(B) - P(A and B).
:feedback-0: Correct! P(A or B) = $0.10 + 0.75 - 0.05 = 0.80$.
:feedback-1: 0.85 comes from adding without subtracting the overlap, which double-counts the case of being admitted to both.
:feedback-2: 0.05 is the probability of being admitted to both colleges, not at least one.
* *0.80
* 0.85
* 0.05
:::

```{admonition} Comments
:class: important

1. Note that although the motivation for this rule was to find P(A or B) when A and B are not disjoint, this rule is general in the sense that if A and B happen to be disjoint (no overlap), then P(A and B) is zero, and we're back to the original version of Rule 4, the Addition Rule for Disjoint Events.

2. Note that in order to find P(A or B) using the General Addition Rule, you need to know P(A and B), the probability that both events occur. In the examples above (document delivery and college admittance), P(A and B) was simply given to us. Sometimes instead of giving us P(A and B) directly, we are given a different piece of information which would allow us to find P(A and B). An example of that draws on our previous work with Rule 5. If A and B are independent, then we can multiply the individual probabilities to compute P(A and B).
```

The next activity will give you guided practice in using the General Addition Rule when events are not disjoint but are independent.

## Check Your Understanding: The General Addition Rule with Independence

A homeowner has two smoke detector alarms installed, one in the dining room (adjacent to the kitchen) and one in an upstairs bedroom (above the kitchen). If cooking produces smoke in the kitchen, the probability of setting off the dining room alarm (D) is 0.95. The probability of setting off the bedroom alarm (B) is 0.40. The two alarms detect smoke independently of each other. If there is smoke in the kitchen, what is the probability that the smoke will be detected and will set off an alarm?

Let's first understand what probability we need to find: The smoke from the fire is detected if it sets off the dining room alarm (D) or the bedroom alarm (B) or both, and therefore P(smoke is detected) = P(D or B), which is the probability we need to find. To that end, we are given a few pieces of information. Let's summarize them:

- P(D) = 0.95
- P(B) = 0.40
- Unlike the previous examples, in which P(A and B) was simply given, here we have a different piece of information: "The two alarms detect smoke *independently* of each other." In other words, instead of being given P(D and B), we are given the fact that D and B are independent.

:::{quiz} How can we find P(D and B)?
:hint: The alarms operate independently—which rule applies?
:feedback-0: Correct! Since D and B are independent, P(D and B) = P(D) $\times$ P(B) = $0.95 \times 0.40 = 0.38$.
:feedback-1: Adding gives 1.35, which is not even a valid probability.
:feedback-2: P(D and B) is not 0—the alarms can certainly both go off; they are independent, not disjoint.
* *Multiply: P(D and B) = $0.95 \times 0.40 = 0.38$
* Add: P(D and B) = $0.95 + 0.40 = 1.35$
* It is 0, because the alarms are in different rooms
:::

:::{quiz} So what is P(D or B), the probability that the smoke is detected?
:hint: Apply the General Addition Rule using P(D and B) = 0.38.
:feedback-0: Correct! P(D or B) = $0.95 + 0.40 - 0.38 = 0.97$.
:feedback-1: 1.35 double-counts the overlap and exceeds 1—remember to subtract P(D and B).
:feedback-2: 0.38 is the probability that BOTH alarms go off, not that at least one does.
* *0.97
* 1.35
* 0.38
:::

```{admonition} Comment
:class: important

The words "at least one of" might remind you of the Complement Rule strategy we used on the previous page for finding the probability that "at least one of many independent events occurred." Note that P(A or B) can also be interpreted as the probability that "at least one of the two events A, B occurs." When the events are independent, the Complement Rule strategy and the General Addition Rule give the same results, as shown below for a birth-month problem: two people are chosen at random, and we want the probability that at least one of them shares your birth month (each with probability 1/12, independently).

Using the General Addition Rule (with independence to find the "and" probability):

P(at least one of the two shares your birth month) = P(A or B) = P(A) + P(B) - P(A and B) = $1/12 + 1/12 - (1/12)(1/12) \approx 0.16$

We could also have used the Complement Rule strategy:

P(at least one of the two shares your birth month) = 1 - P(neither shares your birth month) = $1 - (11/12)(11/12) \approx 0.16$
```
