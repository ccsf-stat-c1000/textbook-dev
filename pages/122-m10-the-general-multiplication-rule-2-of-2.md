# The General Multiplication Rule in Action

```{admonition} Learning Objectives
:class: note

- Use the General Multiplication Rule to find the probability that two events occur (P(A and B)).
```

Here, again, is the General Multiplication Rule:

*For any two events A and B, P(A and B) = P(A) × P(B | A)*

```{admonition} Comments
:class: important

1. Note that although the motivation for this rule was to find P(A and B) when A and B are not independent, this rule is general in the sense that if A and B happen to be *independent*, then P(B | A) = P(B) is true, and we're back to Rule 5—the Multiplication Rule for Independent Events: P(A and B) = P(A) × P(B).

2. The General Multiplication Rule is just the definition of conditional probability in disguise. Recall the definition of conditional probability: *P(B | A) = P(A and B) / P(A)*. Let's isolate P(A and B) by multiplying both sides of the equation by P(A), and we get: *P(A and B) = P(A) × P(B | A)*. That's it ... this is the General Multiplication Rule.

3. The General Multiplication Rule is useful when two events, A and B, occur in stages, first A and then B (like the selection of the two cards in the previous example). Thinking about it this way makes the General Multiplication Rule very intuitive. For both A and B to occur you first need A to occur (which happens with probability P(A)), *and* then you need B to occur, knowing that A has already occurred (which happens with probability P(B | A)).
```

Let's look at another, more realistic example:

:::{admonition} Example: HIV Testing
:class: tip

In a certain region, one in every thousand people (0.001) of all individuals is infected by the HIV virus that causes AIDS. Tests for presence of the virus are fairly accurate but not perfect. If someone actually has HIV, the probability of testing positive is 0.95. Let *H* denote the event of having HIV, and *T* the event of testing positive.

(a) Express the information that is given in the problem in terms of the events H and T.

"one in every thousand people (0.001) of all individuals are infected with HIV" → *P(H) = 0.001*

"If someone actually has HIV, the probability of testing positive is 0.95" → *P(T | H) = 0.95*

(b) Use the General Multiplication Rule to find the probability that someone chosen at random from the population has HIV and tests positive.

*P(H and T)* = P(H) × P(T | H) = 0.001 × 0.95 = 0.00095.

(c) If someone has HIV, what is the probability of testing negative? Here we need to find P(not T | H).

Recall from an activity earlier in this module that the Complement Rule works with conditional probabilities as long as we condition on the same event, therefore: *P(not T | H)* = 1 − P(T | H) = 1 − 0.95 = 0.05.
:::

The purpose of the next activity is to give you guided practice in expressing information in terms of conditional probabilities, and in using the General Multiplication Rule.

## Check Your Understanding: Applying the General Multiplication Rule

An overheating engine can quickly cause serious damage to a car, and therefore a dashboard red warning light is supposed to come on if that happens.

In a certain model car, there is a 3% chance that the engine will overheat (event H).

The probability of the warning light showing up (event W) when it should (i.e., when the engine is really overheating) is 0.98. However, 1% of the time the warning light appears for no apparent reason (i.e., when the engine temperature is normal).

:::{quiz} How should the sentence "the probability of the warning light showing up when the engine is really overheating is 0.98" be written in probability notation?
:hint: The overheating is the given (conditioning) event.
:feedback-0: Correct! Given that the engine overheats (H), the light comes on with probability 0.98: P(W | H) = 0.98.
:feedback-1: P(H | W) would be the probability of overheating given that the light is on—the reverse of what's stated.
:feedback-2: P(W and H) is the probability that both happen, which is not what the sentence describes.
* *P(W | H) = 0.98
* P(H | W) = 0.98
* P(W and H) = 0.98
:::

:::{quiz} How should "1% of the time the warning light appears for no apparent reason (when the engine temperature is normal)" be written?
:hint: The condition here is that the engine is NOT overheating.
:feedback-0: Correct! Given no overheating (not H), the light appears with probability 0.01: P(W | not H) = 0.01.
:feedback-1: P(not H | W) reverses the conditioning.
:feedback-2: P(W) = 0.01 would be the overall probability of the light, ignoring the engine's state.
* *P(W | not H) = 0.01
* P(not H | W) = 0.01
* P(W) = 0.01
:::

:::{quiz} What is the probability that the engine overheats AND the warning light comes on?
:hint: Use the General Multiplication Rule: P(H and W) = P(H) × P(W | H).
:feedback-0: Correct! P(H and W) = 0.03 × 0.98 = 0.0294.
:feedback-1: 0.98 is the conditional probability of the light given overheating, not the joint probability.
:feedback-2: 0.0003 uses the false-alarm rate; the light-given-overheating probability is 0.98.
* *0.0294
* 0.98
* 0.0003
:::

:::{quiz} What is the probability that the engine is fine AND the warning light comes on anyway (a false alarm)?
:hint: P(not H) = 0.97 and P(W | not H) = 0.01.
:feedback-0: Correct! P(not H and W) = 0.97 × 0.01 = 0.0097.
:feedback-1: 0.01 is the conditional false-alarm rate; multiply by P(not H) to get the joint probability.
:feedback-2: 0.03 is P(H); the false alarm involves "not H."
* *0.0097
* 0.01
* 0.03
:::
