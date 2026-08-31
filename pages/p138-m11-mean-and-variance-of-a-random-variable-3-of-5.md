---
enumerator: "123."
---
# Expected Value in the Real World: Games, Insurance, and Decisions

Here is another example:

:::{admonition} Example: Life Insurance #1
:class: tip

Suppose you work for an insurance company, and you sell a \$100,000 whole-life insurance policy at an annual premium of \$1,200. (This means that the person who bought this policy pays \$1,200 per year so that in the event that he or she dies, the policy beneficiaries will get \$100,000.) Actuarial tables show that the probability of death during the next year for a person of your customer's age, sex, health, etc. is 0.005. Let the random variable X be the company's gain from such a policy.

What is the expected or mean gain (amount of money made by the company) for a policy of this type?

In other words, we need to find $\mu_{X}$.

Since this is a whole-life policy, there are two possibilities here; either the customer dies this year (which you are given will happen with probability 0.005), or the customer does not die this year (which, by the complement rule, must be 0.995).

In both cases, the company gets the \$1,200 premium. If the customer lives, the company just gains the \$1,200, but if the customer dies, the company needs to pay \$100,000 to the customer's beneficiaries. Therefore, here is the probability distribution of X:

| x | +1200 (lives) | $1200 - 100{,}000$ (dies) |
| --- | --- | --- |
| P(X = x) | 0.995 | 0.005 |

Their average, or expected, gain overall is

$$\mu_{X} = 1200(0.995) + (1200 - 100{,}000)(0.005) = 700 \text{ dollars}$$
:::

:::{admonition} Example: Life Insurance #2
:class: tip

Suppose that five years have passed and your actuarial tables indicate that the probability of death during the next year for a person of your customer's current age has gone up to 0.0075. Obviously, this change in probability should be reflected in the annual premium (since it is slightly more risky for the insurance company to insure the customer).

What should the annual premium be (instead of \$1,200) if the company wants to keep the same expected gain?

Now we substitute 0.0075 for 0.005, replace 1,200 with an unknown new premium N, and set the mean gain equal to 700, as it was before:

| x | N (lives) | $N - 100{,}000$ (dies) |
| --- | --- | --- |
| P(X = x) | 0.9925 | 0.0075 |

We need to solve: 700 = (N)(0.9925) + (N - 100,000)(0.0075)

Using some algebra: $700 = N - 750$

Finally: $N = 1450$

In order to keep the same expected gain of \$700, the company should increase that customer's premium to \$1,450.
:::

The purpose of this next activity is to give you guided practice in solving practical problems whose solution is based on the mean of random variables.

## Check Your Understanding: Expected Value in Applications

Suppose that you work for an insurance company and you sell a \$100,000 fire insurance policy at an annual premium of \$1,350. Experience has shown that:

- The probability of total loss (due to fire) to a house in that area and of the size of your customer's house is 0.002 (in which case the insurance company will pay the full \$100,000 to the customer).
- The probability of 50% damage (due to fire) to a house in that area and of the size of your customer's house is 0.008 (in which case the insurance company will pay only \$50,000 to the customer).

For simplicity, we'll ignore any other partial losses.

Let the random variable X be the insurance company's annual gain from such a policy (i.e., the amount of money made by the insurance company from such a policy).

:::{quiz} What are the possible values of X and their probabilities?
:hint: The company always collects the \$1,350 premium, and pays out \$100,000, \$50,000, or nothing.
:feedback-0: Correct! Total loss: $1350 - 100{,}000 = -98{,}650$ (prob 0.002); 50% damage: $1350 - 50{,}000 = -48{,}650$ (prob 0.008); no fire: +1350 (prob 0.990).
:feedback-1: Don't forget that the company keeps the premium in every case—subtract payouts from 1350.
:feedback-2: The no-fire probability is $1 - 0.002 - 0.008 = 0.990$.
* *-98,650 (0.002); -48,650 (0.008); +1,350 (0.990)
* -100,000 (0.002); -50,000 (0.008); +1,350 (0.990)
* -98,650 (0.002); -48,650 (0.008); +1,350 (0.980)
:::

:::{quiz} What is the company's expected annual gain from this policy?
:hint: $\mu(X) = (-98{,}650)(0.002) + (-48{,}650)(0.008) + (1{,}350)(0.990)$.
:feedback-0: Correct! $\mu(X) = -197.30 - 389.20 + 1{,}336.50$ = \$750.
:feedback-1: \$1,350 ignores the fire payouts, which lower the long-run average.
:feedback-2: Check the arithmetic: the three weighted terms are -197.30, -389.20, and +1,336.50.
* *\$750
* \$1,350
* \$550
:::

:::{quiz} Which is the best interpretation of this expected gain?
:hint: Expected value describes a long-run average.
:feedback-0: Correct! Over many, many policies of this kind, the company gains an average of \$750 per policy per year—even though on any single policy it either gains \$1,350 or takes a large loss.
:feedback-1: On any single policy the gain is never exactly \$750; the mean describes the long-run average.
:feedback-2: The company can absolutely lose money on an individual policy (when a fire occurs)—just not on average across many policies.
* *In the long run, the company averages a gain of \$750 per policy per year
* The company earns exactly \$750 from this customer each year
* The company can never lose money on this policy
:::
