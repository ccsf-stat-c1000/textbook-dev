# Probability Rules (7 of 11)

```{admonition} Learning Objectives
    - Apply probability rules in order to find the likelihood of an event.
```

As you've seen, the last three rules that we've introduced (the Complement Rule, the Addition Rule for Disjoint Events, and the Multiplication Rule for Independent Events) are frequently used in solving problems. Before we move on to our next rule, here are two comments that will help you use these rules in broader types of problems and more effectively.

## Comment

As we mentioned before, the Addition Rule can be extended to more than two disjoint events. Likewise, the Multiplication Rule can be extended to more than two independent events. So if A, B and C are three independent events, for example, then P(A and B and C) = P(A) * P(B) * P(C). These extensions are quite straightforward, as long as you remember that "or" requires us to add, while "and" requires us to multiply.

An example of a situation where more than two independent events naturally occur is when a random sample of more than two individuals is chosen from a large population.

Here is an example:

```{admonition} Example
    Three people are chosen at random from a large population. What is the probability that all three have blood type B? We'll use the usual notation of B1, B2 and B3 for the events that persons 1, 2 and 3 have blood type B, respectively. We need to find P(B1 and B2 and B3). Let's solve this one together:

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

Here is another example that might be quite surprising.

```{admonition} Example
    A fair coin is tossed 10 times. Which of the following two outcomes is more likely?

    (a) HHHHHHHHHH

    (b) HTTHHTHTTH

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```

    In fact, they are equally likely. The 10 tosses are independent, so we'll use the Multiplication Rule for Independent Events:

    P(HHHHHHHHHH) = P(H) * P(H) * ... *P(H) = 1/2 * 1/2 *... * 1/2 = (1/2)^10^

    P(HTTHHTHTTH) = P(H) * P(T) * ... * P(H) = 1/2 * 1/2 *... * 1/2 = (1/2)^10^

    Here is the idea:

    My random experiment here is tossing a coin 10 times. You can imagine how huge the sample space is.

    There are actually 1,024 possible outcomes to this experiment, all of which are equally likely. Therefore, while it is true that it is more likely to get an outcome that has 5 heads and 5 tails than an outcome that has only heads (since there is only one possible outcome of the latter kind, and many possible outcomes of the former), if I am comparing 2 *specific outcomes* as I do here, they are equally likely.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
