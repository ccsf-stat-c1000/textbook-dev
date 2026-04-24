# Probability Trees (2 of 3)

```{admonition} Learning Objectives
    - Use probability trees as a tool for finding probabilities.
```

Now that we understand how to construct the probability tree, let's use the tree to answer some questions:

```{admonition} Example
    What is the overall probability that the sales rep will take the Bermuda vacation?

    Notice that a V branch can be reached by either a C or a not C branch: either the sales rep gets the commission and takes the vacation, or he does not get the commission and he takes the vacation. Symbolically, V = (C and V) or (not C and V). Thus, the overall probability of taking the vacation is

    P(V) = P( (C and V) or (not C and V) ).

    Applying the Addition Rule for Disjoint Events, we have

    P(V) = P(C and V) + P(not C and V).

    Applying the General Multiplication Rule to each term, we have

    P(V) = P(C) * P(V | C) + P(not C) * P(V | not C) = .4 * .9 + .6 * .3 = .36 + .18 = .54.

    The overall probability that the sales rep will take the Bermuda vacation is .54. The tree diagram below shows the probabilities obtained via the general multiplication rule, and then the addition rule.

    ```{figure} images/image011.gif
    :alt: A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Each branch-off represents the path we take when we need to take a branch, and the probability for taking that branch is provided. {C: .4; V: .9}; {C: .4; not V: .1}; {not C: .6; V: .3}; {not C: .6; not V: .7}; Now, focus on the {C: .4, V: .9} branch. From this branch we can conclude that P(C and V) = P(C) * P(V|C) = .4 * .9 = .36 . Also, the other branch {not C: .6, V: .3} branch shows that P(not C and V) = P(not C) * P(V | not C) = .6 * .3 = .18 . From these two, we can obtain P(V) = P(C and V) + P(not C and V) = .36 + .18 = .54 .

    A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Each branch-off represents the path we take when we need to take a branch, and the probability for taking that branch is provided. {C: .4; V: .9}; {C: .4; not V: .1}; {not C: .6; V: .3}; {not C: .6; not V: .7}; Now, focus on the {C: .4, V: .9} branch. From this branch we can conclude that P(C and V) = P(C) * P(V|C) = .4 * .9 = .36 . Also, the other branch {not C: .6, V: .3} branch shows that P(not C and V) = P(not C) * P(V | not C) = .6 * .3 = .18 . From these two, we can obtain P(V) = P(C and V) + P(not C and V) = .36 + .18 = .54 .
    ```
```

## Comment

Following one branch to a connected branch, such as C then V, represents the occurrence of one event and then another, which requires multiplication of probabilities. Including outcomes reached via either of two end-branches represents the occurrence of one event or another, which requires addition of probabilities.

In order to illustrate the background situation of either getting the commission or not—which together make up the whole sample space S—along with the follow-up circumstance of either taking the vacation or not, we can draw a different sort of Venn diagram:

```{figure} images/image012.gif
:alt: The entire sample space is represented by a large rectangle. This rectangle is divided into two pieces. One side is for C and the other side is for not C. In the middle of the rectangle is a circle, which has one part in C and the other in not C. The circle represents V, and the part of the circle in C represents C and V, and the other part (in not C) represents not C and V.

The entire sample space is represented by a large rectangle. This rectangle is divided into two pieces. One side is for C and the other side is for not C. In the middle of the rectangle is a circle, which has one part in C and the other in not C. The circle represents V, and the part of the circle in C represents C and V, and the other part (in not C) represents not C and V.
```

The diagram shows that V = (C and V) or (not C and V), where (C and V) and (not C and V) are disjoint. Applying first the Addition Rule for Disjoint Events and then the General Multiplication Rule, we have P(V) = P(C and V) + P(not C and V) = P(C) * P(V | C) + P(not C) * P(V | not C), just as we saw in our tree diagram.

We can generalize our solution to obtain an expression for the probability of any event B, based on how B is impacted by the occurrence or non-occurrence of some other event A. We call this the *Law of Total Probability:*P(B) = P(A) * P(B | A) + P(not A) * P(B | not A).

```{admonition} Example
    Suppose the friend finds out that the sales rep has left for Bermuda. Is it likely that the commission came through? Find the probability that the commission came through, given that the sales rep went to Bermuda.

    Here, we are asked to find the probability that the commission came through, given that the sales rep took his Bermuda vacation, P(C | V). Using the definition of conditional probability,

    P(C | V) = P(C and V) / P(V)

    and now, using the tree, and our result from part (a) (P(V) = .54)), we get that:

    P(C | V) = P(C and V) / P(V) = .36/.54 = .67

    Thus, if it is known that the sales rep left for the Bermuda vacation, it is more likely than not that the commission came through.

    ```{figure} images/image013.gif
    :alt: A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Each branch-off represents the path we take when we need to take a branch, and the probability for taking that branch is provided. {C: .4; V: .9}; {C: .4; not V: .1}; {not C: .6; V: .3}; {not C: .6; not V: .7}; From this tree, we observe that the branch {C: .4, V: .9} represents P(C and V) = P(C) and P(V|C) = .4 * .9 = .36. We also observe that the branch {not C: .6, V: .3} represents P(not C and V) = P(not C) and P(V|not C) = .6 * .3 = .18 . From these two we calculate P(V) = P(C and V) or P(not C and V) = .36 + .18 = .54. We also know that P(C|V) = P(C and V)/P(V) = .36/.54 = .67, giving us our answer.

    A probability tree. We will be naming paths through the tree with the notation "{first branch-off: probability of branch-off; second branch-off: probability of branch-off; ...}". Each branch-off represents the path we take when we need to take a branch, and the probability for taking that branch is provided. {C: .4; V: .9}; {C: .4; not V: .1}; {not C: .6; V: .3}; {not C: .6; not V: .7}; From this tree, we observe that the branch {C: .4, V: .9} represents P(C and V) = P(C) and P(V|C) = .4 * .9 = .36. We also observe that the branch {not C: .6, V: .3} represents P(not C and V) = P(not C) and P(V|not C) = .6 * .3 = .18 . From these two we calculate P(V) = P(C and V) or P(not C and V) = .36 + .18 = .54. We also know that P(C|V) = P(C and V)/P(V) = .36/.54 = .67, giving us our answer.
    ```
```

## Comment

Ordinarily, when events occur in stages, the explanatory variable would be the occurrence or non-occurrence of a certain event at the first stage, and the response variable would be the occurrence or non-occurrence of the next event chronologically. In such cases, we would identify the probability of a certain response, given that the explanatory variable took a certain value. However, there are sometimes situations, as in the second example above, where what we know is the ultimate outcome, and what we want to find out is the probability that a certain event occurred previously. Our solution to that example suggests a general formula for solving problems of this form:

$P\left(A|B\right)=\frac{P\left(A and B\right)}{P\left(B\right)}$ *[our expression for a conditional probability]*

$P\left(A|B\right)=\frac{P\left(A\right)⋅P\left(B|A\right)}{P\left(B\right)}$ *[by the General Multiplication Rule]*

$P\left(A|B\right)=\frac{P\left(A\right)⋅P\left(B|A\right)}{P\left(A\right)⋅P\left(B|A\right)+P\left(not A\right)⋅P\left(B|not A\right)}$ *[by the Law of Total Probability]*

The fact that P(A | B) equals the latter expression is known as Bayes' Rule, or Bayes' Theorem.
