# Probability Rules (9 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
    - When appropriate, use tools such as Venn diagrams or probability tables as aids for finding probabilities.
```

We are now getting to the last rule in this module in which we’ll go back to P(A or B).

So far, we’ve introduced the Addition Rule for finding P(A or B) in the special case when A and B are *disjoint*events - that is when the events cannot happen together → P(A and B)= $0$.

```{figure} images/image1.png
:alt: A Venn Diagram titled "A and B are Disjoint. The entire sample space S is represented as a gray rectangle. Inside are two, separate, non-overlapping blue circles. One circle is for the occurrences in A and the other for occurrences in B.

A Venn Diagram titled "A and B are Disjoint. The entire sample space S is represented as a gray rectangle. Inside are two, separate, non-overlapping blue circles. One circle is for the occurrences in A and the other for occurrences in B.
```

In this special case P(A or B) refers to the probability of either event A occurring or event B occurring and we said that P(A or B)=P(A) + P(B). Visually, in the Venn diagram above we can clearly see that P(A or B), represented by the total blue area, can be found by adding the areas of the two circles, one representing P(A) and the other P(B).

As we mentioned above the case when A and B are disjoint is a special case and in many situations the events are *not disjoint -*they can occur at the same time.

```{figure} images/image2.png
:alt: A venn diagram titled "A and B are NOT Disjoint." A gray box represents the sample space, and inside are two blue circles which have an overlapping area. One circle is labeled A and the other is labeled B. The area where the two circles overlap represents that Events A and B can occur at the same time, so P(A and B) ≠ 0.

A venn diagram titled "A and B are NOT Disjoint." A gray box represents the sample space, and inside are two blue circles which have an overlapping area. One circle is labeled A and the other is labeled B. The area where the two circles overlap represents that Events A and B can occur at the same time, so P(A and B) ≠ 0.
```

We are now ready to learn how to find P(A or B) in this more general case - when A and B are not necessarily disjoint. We'll call this rule the "General Addition Rule".

Before we introduce this rule through an example, it is important to understand what P(A or B) represents in the case when A and B are not disjoint. Let’s look at the Venn diagram above.

Again, P(A or B) is represented by the total blue area which in this case looks different. In this case this area includes an overlap between the two circles which corresponds to the probability that both events A and B occur. This difference has an important implication to the meaning of P(A or B) when A and B are not disjoint.

When A and B are not disjoint P(A or B) means P(A occurs or B occurs or both events occur).

```{admonition} Example
    It is vital that a certain document reach its destination within one day. To maximize the chances of on-time delivery, two copies of the document are sent using two services, service A and service B. It is known that the probabilities of on-time delivery are:

    0.90 for service A (*P(A) = 0.90*)

    0.80 for service B (*P(B) = 0.80*)

    0.75 for both services being on time (*P(A and B) = 0.75*)

    (Note that A and B are n*ot disjoint*. They can happen together with probability 0.75.)

    The Venn diagrams below illustrate the probabilities P(A), P(B), and P(A and B)

    [not drawn to scale]:

    ```{figure} images/image3.png
    :alt: Three Venn Diagrams. In all of them there is a large rectangle representing all of the sample space S. Inside this rectangle are two circles which overlap partially. One circle is labeled A and the other is labeled B. In the first Venn Diagram the circle for A is colored blue, and we see that P(A) = 0.90 . In some sense P(A) is the area of the A circle. In the second Venn Diagram the circle for B is colored blue, and it is marked that P(B) = 0.80 . Just like in the first Venn diagram it can be thought that the circle for B has an area of 0.80 . In the third Venn Diagram the area which is the overlap of circles A and B is colored blue. P(A and B) = 0.75 . The area of the overlap can be thought of as having an area of 0.75 .

    Three Venn Diagrams. In all of them there is a large rectangle representing all of the sample space S. Inside this rectangle are two circles which overlap partially. One circle is labeled A and the other is labeled B. In the first Venn Diagram the circle for A is colored blue, and we see that P(A) = 0.90 . In some sense P(A) is the area of the A circle. In the second Venn Diagram the circle for B is colored blue, and it is marked that P(B) = 0.80 . Just like in the first Venn diagram it can be thought that the circle for B has an area of 0.80 . In the third Venn Diagram the area which is the overlap of circles A and B is colored blue. P(A and B) = 0.75 . The area of the overlap can be thought of as having an area of 0.75 .
    ```

    In the context of this problem, the obvious question of interest is:

    *What is the probability of on-time delivery of the document using this strategy (of sending it via both services)?*

    The document will reach its destination on time as long as it is delivered on time by service A or by service B or by both services. In other words, when event A occurs or event B occurs or both occur. so....

    P(on time delivery using this strategy)= *P(A or B)*, which is represented the by the shaded region in the diagram below:

    ```{figure} images/image6.png
    :alt: The same Venn Diagram except the area of the two circles has been colored blue (shaded). This means the area in the overlap is also colored blue. Note that the overlap area has only been colored once, so even though it is in both circles we will count it once.

    The same Venn Diagram except the area of the two circles has been colored blue (shaded). This means the area in the overlap is also colored blue. Note that the overlap area has only been colored once, so even though it is in both circles we will count it once.
    ```

    We can now use the three Venn diagrams representing P(A), P(B) and P(A and B) to see that we can find P(A or B) by:

    adding P(A) (represented by the left circle) and P(B) (represented by the right circle), then subtracting P(A and B) (represented by the overlap), since we included it twice, once as part of P(A) and once as part of P(B).

    This is shown in the following image:

    ```{figure} images/image7.png
    :alt: The area of both circles in the Venn diagram (counting the overlap area once) is calculated as: the area of A's circle (which includes the overlap) + the area of B's circle (which also includes the overlap) - the area of the overlap. We therefore get: P(A or B) = P(A) + P(B) - P(A and B).

    The area of both circles in the Venn diagram (counting the overlap area once) is calculated as: the area of A's circle (which includes the overlap) + the area of B's circle (which also includes the overlap) - the area of the overlap. We therefore get: P(A or B) = P(A) + P(B) - P(A and B).
    ```

    If we apply this to our example, we find that:

    P(A or B)= P(on-time delivery using this strategy)= 0.90 + 0.80 - 0.75 = 0.95.

    So our strategy of using two delivery services increases our probability of on-time delivery to 0.95.
```

After this example, the following General Addition Rule for the probability of finding P(A or B), should not be surprising:

```{admonition} Rule 6: The General Addition Rule
    *For any 2 events A and B, P(A or B) = P(A) + P(B) - P(A and B).*
```

*Comment:*

As we mentioned above P(A or B)= P(A occurs or B occurs or both occur).

Another way to interpret P(A or B) is therefore P(At least one of the two events occur).

(Later in this page we’ll make the connection to the “at least one of...” type problems we discussed on the previous page).

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

Suppose that Jim is applying to two colleges: College A, an “Ivy League” school, and College B, a state university. Based on his credentials and the requirements of the two colleges, Jim estimates his chances with the following probabilities:

- Probability that he will be admitted to college A is 0.10.
- Probability that he will be admitted to college B is 0.75.
- Probability that he will be admitted to both colleges is 0.05.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comments:

1. Note that although the motivation for this rule was to find P(A or B) when A and B are not disjoint, this rule is general in the sense that if A and B happen to be disjoint (no overlap), then P(A and B) is zero, and we're back to the original version of Rule 4, the Addition Rule for Disjoint Events.

2. Note that in order to find P(A or B) using the General Addition Rule, you need to know P(A and B), the probability that both events occur. In all three examples above (document delivery, traffic lights and college admittance) P(A and B) was simply given to us. Sometimes instead of giving us P(A and B) directly, we are given a different piece of information which would allow us to find P(A and B). An example of that draws on our previous work with Rule 5. If A and B are independent, then we can multiply the individual probabilities to compute P(A and B).

The next activity will give you guided practice in using the General Addition Rule when events are not disjoint but are independent.

## Learn By Doing

A homeowner has two smoke detector alarms installed, one in the dining room (adjacent to the kitchen) and one in an upstairs bedroom (above the kitchen). If cooking produces smoke in the kitchen, the probability of setting off the dining room alarm (D) is .95. The probability of setting off the bedroom alarm (B) is .40. The two alarms detect smoke independently of each other. If there is smoke in the kitchen, what is the probability that the smoke will be detected and will set off an alarm?

Let's first understand what probability we need to find: The smoke from the fire is detected if it sets off the dining room alarm (D) or the bedroom alarm (B) or both, and therefore P(smoke is detected) = P(D or B), which is the probability we need to find. To that end, we are given a few pieces of information. Let's summarize them:

To that end, we are given a few pieces of information. Let's summarize them:

* P(D) = .95

* P(B) = .4

* Unlike the previous examples, in which P(A and B) was simply given, here we have a different piece of information: "The two alarms detect smoke *independently*of each other." In other words, instead of being given P(D and B), we are given the fact that D and B are independent.

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

## Comment:

The words “at least one of” might remind you of the Complement Rule strategy we used on the previous page for finding the probability that “at least one of many independent events occurred.” Note that P(A or B) can also be interpreted as the probability that “at least one of the two events A, B occur.” When the events are independent, the Complement Rule strategy and the General Addition Rule give the same results, as shown below for the birth month problem.

* General Addition Rule when events are independent:

P(at least one of the two shares your birth month)=

P(A or B)=P(A)+P(B)–P(A and B)=

1/12 +1/12 -(1/12)(1/12)=0.16.

* We could also have used the Complement Rule strategy:

P(at least one of the two share your birth month)=

1–P(neither shares your birth month)=

1- (11/12)(11/12)=0.16.
