# Mean and Variance of a Random Variable (3 of 5)

```{admonition} Learning Objectives
    - Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

Here is another example:

```{admonition} Example: Life Insurance #1
    Suppose you work for an insurance company, and you sell a $100,000 whole-life insurance policy at an annual premium of $1,200. (This means that the person who bought this policy pays $1,200 per year so that in the event that he or she dies, the policy beneficiaries will get $100,000). Actuarial tables show that the probability of death during the next year for a person of your customer's age, sex, health, etc. is .005. Let the random variable X be the company's gain from such a policy.

    What is the expected or mean gain (amount of money made by the company) for a policy of this type?

    In other words, we need to find $\mu_{X}$ .

    Since this is a whole-life policy, there are two possibilities here; either the customer dies this year (which you are given will happen with probability .005), or the customer does not die this year (which, by the complement rule, must be .995).

    In both cases, the company gets the $1,200 premium. If the customer lives, the company just gains the $1,200, but if the customer dies, the company needs to pay $100,000 to the customer's beneficiaries. Therefore, here is the probability distribution of X:

    ```{figure} images/image029a.gif
    :alt: A two row probability distribution table, in which the rows are labeled "X" and "P(X=x)". Here is the data in column oriented format (X: P(X=x), comment): +1200: .995 (live); 1200-100,000: .005 (die);

    A two row probability distribution table, in which the rows are labeled "X" and "P(X=x)". Here is the data in column oriented format (X: P(X=x), comment): +1200: .995 (live); 1200-100,000: .005 (die);
    ```

    Their average, or expected, gain overall is

    $\mu_{X}$ = 1200(.995) + (1200 - 100,000)(.005) = 700 dollars.
```

```{admonition} Example: Life Insurance #2
    Suppose that five years have passed and your actuarial tables indicate that the probability of death during the next year for a person of your customer's current age has gone up to .0075. Obviously, this change in probability should be reflected in the annual premium (since it is slightly more risky for the insurance company to insure the customer).

    What should the annual premium be (instead of $1,200) if the company wants to keep the same expected gain?

    Now we substitute .0075 for .005, replace 1,200 with an unknown new premium N, and set the mean gain equal to 700, as it was before:

    ```{figure} images/image030a.gif
    :alt: A two-row probability distribution table, in which the rows are labeled "X" and "P(X=x)". Here is the data in column oriented format (X: P(X=x), comment): N: .9925 (live); N-100,000: .0075 (die);

    A two-row probability distribution table, in which the rows are labeled "X" and "P(X=x)". Here is the data in column oriented format (X: P(X=x), comment): N: .9925 (live); N-100,000: .0075 (die);
    ```

    | We need to solve: | 700 | = | (N)(.9925) + (N - 100,000)(.0075) |
    | --- | --- | --- | --- |
    | Using some algebra: | 700 | = | N - 750 |
    | Finally | N | = | 1450 |

    In order to keep the same expected gain of $700, the company should increase that customer's premium to $1,450.
```

The purpose of this next activity is to give you guided practice in solving practical problems whose solution is based on the mean of random variables.

## Learn By Doing

Suppose that you work for an insurance company and you sell a $100,000 fire insurance policy at an annual premium of $1,350. Experience has shown that:

- The probability of total loss (due to fire) to a house in that area and of the size of your customer's house is .002 (in which case the insurance company will pay the full $100,000 to the customer).
- The probability of 50% damage (due to fire) to a house in that area and of the size of your customer's house is .008 (in which case the insurance company will pay only $50,000 to the customer).

For simplicity, we'll ignore any other partial losses.

Let the random variable X be the insurance company's annual gain from such a policy (i.e., the amount of money made by the insurance company from such a policy).

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
