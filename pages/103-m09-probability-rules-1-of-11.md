# Rules 1 and 2: What Every Probability Must Obey

## Basic Probability Rules

In the previous section we considered situations in which all the possible outcomes of a random experiment are equally likely, and learned a simple way to find the probability of any event in this special case. We are now moving on to learn how to find the probability of events in the general case (when the possible outcomes are not necessarily equally likely), using five basic probability rules. Fortunately, these basic rules of probability are very intuitive, and as long as they are applied systematically, they will let us solve more complicated problems; in particular, those problems for which our intuition might be inadequate.

```{admonition} Rule 1
:class: note

*For any event A, $0 \leq$ P(A) $\leq 1.*$
```

This first rule simply reminds us of the basic property of probability that we've already learned. The probability of an event, which informs us of the likelihood of it occurring, can range anywhere from 0 (indicating that the event will never occur) to 1 (indicating that the event is certain). One practical use of this rule is that it can be used to identify any probability calculation that comes out to be more than 1 as wrong.

Before moving on to the other rules, let's first look at an example that will provide a context for illustrating the next several rules.

:::{admonition} Example: Blood Types
:class: tip

As previously discussed, all human blood can be typed as O, A, B or AB. In addition, the frequency of the occurrence of these blood types varies by ethnic and racial groups. According to Stanford University's Blood Center, these are the probabilities of human blood types in the United States (the probability for type A has been omitted on purpose):

| Blood Type | O | A | B | AB |
| --- | --- | --- | --- | --- |
| Probability | 0.44 | ? | 0.10 | 0.04 |

*Motivating question for rule 2:* A person in the United States is chosen at random. What is the probability of the person having blood type A?

*Answer:* Our intuition tells us that since the four blood types O, A, B, and AB exhaust all the possibilities, their probabilities together must sum to 1, which is the probability of a "certain" event (a person has one of these 4 blood types for certain). Since the probabilities of O, B, and AB together sum to $0.44 + 0.10 + 0.04 = 0.58$, the probability of type A must be the remaining $0.42 (1 - 0.58 = 0.42)$:

| Blood Type | O | A | B | AB |
| --- | --- | --- | --- | --- |
| Probability | 0.44 | 0.42 | 0.10 | 0.04 |
:::

This example illustrates our second rule, which tells us that the probability of all outcomes in the sample space together must be 1.

```{admonition} Rule 2
:class: note

*P(S) = 1; that is, the sum of the probabilities of all possible outcomes is 1.*
```

::::{admonition} Comment
:class: important

This is a good place to compare and contrast what we're doing here with what we learned in the Exploratory Data Analysis (EDA) section. Notice that in this problem we are essentially focusing on a single categorical variable: blood type. We summarized this variable above, as we summarized single categorical variables in the EDA section, by listing what values the variable takes and how often it takes them. In EDA we used percentages, and here we're using probabilities, but the two convey the same information. In the EDA section, we learned that a pie chart provides an appropriate display when a single categorical variable is involved, and similarly we can use it here (using percentages instead of probabilities):

```{figure} images/gen/m09-blood-pie.svg
:alt: A pie chart titled Blood Types in the United States. Type O takes up 44% of the pie, A takes 42%, B takes 10%, and AB takes 4%.
```

Even though what we're doing here is indeed similar to what we've done in the EDA section, there is a subtle but important difference between the underlying situations in this section and the ones in the Exploratory Data Analysis section. In EDA, we summarized data that were obtained from a {term}`sample` of individuals for whom values of the variable of interest were recorded. Here, when we present the frequency, or probability, of each blood type, we have in mind the entire {term}`population` of people in the United States, for which we are presuming to know the overall frequency of values taken by the variable of interest.
::::

## Check Your Understanding: The Basic Probability Rules

:::{quiz} A four-sided spinner has regions with probabilities P(red) = 0.35, P(blue) = 0.25, and P(green) = 0.15. What must P(yellow) be?
:hint: The probabilities of all outcomes must sum to 1 (Rule 2).
:feedback-0: Correct! P(yellow) = $1 - (0.35 + 0.25 + 0.15) = 0.25$.
:feedback-1: Check the sum: the three given probabilities total 0.75, leaving 0.25 for yellow.
:feedback-2: Probabilities must sum to exactly 1, so yellow's probability is fully determined.
* *0.25
* 0.35
* It cannot be determined
:::
