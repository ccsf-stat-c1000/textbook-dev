# Trees and Total Probability

```{admonition} Learning Objectives
:class: note

- Use probability trees as a tool for finding probabilities.
```

Now that we understand how to construct the probability tree, let's use the tree to answer some questions:

:::{admonition} Example: The Overall Probability of the Vacation
:class: tip

What is the overall probability that the sales rep will take the Bermuda vacation?

Notice that a V branch can be reached by either a C or a not C branch: either the sales rep gets the commission and takes the vacation, or he does not get the commission and he takes the vacation. Symbolically, V = (C and V) or (not C and V). Thus, the overall probability of taking the vacation is

P(V) = P( (C and V) or (not C and V) ).

Applying the Addition Rule for Disjoint Events, we have

P(V) = P(C and V) + P(not C and V).

Applying the General Multiplication Rule to each term, we have

P(V) = P(C) × P(V | C) + P(not C) × P(V | not C) = 0.4 × 0.9 + 0.6 × 0.3 = 0.36 + 0.18 = 0.54.

The overall probability that the sales rep will take the Bermuda vacation is 0.54. The tree diagram below shows the probabilities obtained via the general multiplication rule, and then the addition rule:

```{figure} images/gen/m10-tree-commission.svg
:alt: The commission and vacation probability tree, in which multiplying along the C then V path gives P(C and V) equal to 0.36, multiplying along the not C then V path gives P(not C and V) equal to 0.18, and adding the two vacation paths gives P(V) equal to 0.54.
```
:::

## Comment

Following one branch to a connected branch, such as C then V, represents the occurrence of one event and then another, which requires multiplication of probabilities. Including outcomes reached via either of two end-branches represents the occurrence of one event or another, which requires addition of probabilities.

In order to illustrate the background situation of either getting the commission or not—which together make up the whole sample space S—along with the follow-up circumstance of either taking the vacation or not, we can draw a different sort of Venn diagram:

```{figure} images/gen/m10-total-prob-venn.svg
:alt: A rectangle representing the sample space is divided into a left region for C and a right region for not C. An ellipse representing V straddles the dividing line, so that V is split into two disjoint pieces: C and V on the left, and not C and V on the right.
```

The diagram shows that V = (C and V) or (not C and V), where (C and V) and (not C and V) are disjoint. Applying first the Addition Rule for Disjoint Events and then the General Multiplication Rule, we have P(V) = P(C and V) + P(not C and V) = P(C) × P(V | C) + P(not C) × P(V | not C), just as we saw in our tree diagram.

We can generalize our solution to obtain an expression for the probability of any event B, based on how B is impacted by the occurrence or non-occurrence of some other event A. We call this the *Law of Total Probability:*

$$P(B) = P(A) \cdot P(B | A) + P(\text{not } A) \cdot P(B | \text{not } A)$$

:::{admonition} Example: Reversing the Conditioning
:class: tip

Suppose the friend finds out that the sales rep has left for Bermuda. Is it likely that the commission came through? Find the probability that the commission came through, given that the sales rep went to Bermuda.

Here, we are asked to find the probability that the commission came through, given that the sales rep took his Bermuda vacation, P(C | V). Using the definition of conditional probability,

P(C | V) = P(C and V) / P(V)

and now, using the tree, and our earlier result (P(V) = 0.54), we get:

P(C | V) = P(C and V) / P(V) = 0.36/0.54 = 0.67

Thus, if it is known that the sales rep left for the Bermuda vacation, it is more likely than not that the commission came through.
:::

## Comment

Ordinarily, when events occur in stages, the explanatory variable would be the occurrence or non-occurrence of a certain event at the first stage, and the response variable would be the occurrence or non-occurrence of the next event chronologically. In such cases, we would identify the probability of a certain response, given that the explanatory variable took a certain value. However, there are sometimes situations, as in the second example above, where what we know is the ultimate outcome, and what we want to find out is the probability that a certain event occurred previously. Our solution to that example suggests a general formula for solving problems of this form:

$$P(A|B)=\frac{P(A \text{ and } B)}{P(B)} \quad \text{[our expression for a conditional probability]}$$

$$P(A|B)=\frac{P(A)\cdot P(B|A)}{P(B)} \quad \text{[by the General Multiplication Rule]}$$

$$P(A|B)=\frac{P(A)\cdot P(B|A)}{P(A)\cdot P(B|A)+P(\text{not } A)\cdot P(B|\text{not } A)} \quad \text{[by the Law of Total Probability]}$$

The fact that P(A | B) equals the latter expression is known as Bayes' Rule, or Bayes' Theorem.
