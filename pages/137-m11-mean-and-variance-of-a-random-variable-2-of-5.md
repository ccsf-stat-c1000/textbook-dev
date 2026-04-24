# Mean and Variance of a Random Variable (2 of 5)

```{admonition} Learning Objectives
    - Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

## Applications of the Mean

Means of random variables are useful for telling us about long-run gains in sales, or for insurance companies.

Here are two examples:

```{admonition} Example: Pizza Delivery #1
    Your favorite pizza place delivers only one kind of pizza, which is sold for $10, and costs the pizza place $6 to make. The pizza place has the following policy regarding delivery: if the pizza takes longer than half an hour to arrive, there is no charge. Let the random variable X be the pizza place's gain for any one pizza.

    Experience has shown that delivery takes longer than half an hour only 10 percent of the time.

    Find the mean gain per pizza, $\mu_{X}$.

    In order to find the mean of X, we first need to establish its probability distribution—the possible values and their probabilities.

    The random variable X has two possible values: either the pizza costs them $6 to make and they sell it for $10, in which case X takes the value $10 - $6 = $4, or it costs them $6 to make and they give it away, in which case X takes the value $0 - $6 = -$6. The probability of the latter case is given to be 10 percent, or .1, so using complements, the former has probability .9. Here, then is the probability distribution of X:

    ```{figure} images/image024a.gif
    :alt: A probability distribution table with two rows, labeled "X" "P(X=x)." Here is the data in columns (X: P(X=x)): +4: .9; -6: .1; In other words, when pizza delivery is not longer than half an hour, X = +4, and P(X = +4) = .9 . When pizza delivery takes longer than half an hour, X=-6, and P(X = -6) = .1 .

    A probability distribution table with two rows, labeled "X" "P(X=x)." Here is the data in columns (X: P(X=x)): +4: .9; -6: .1; In other words, when pizza delivery is not longer than half an hour, X = +4, and P(X = +4) = .9 . When pizza delivery takes longer than half an hour, X=-6, and P(X = -6) = .1 .
    ```

    Therefore,

    $\mu_{X}=(+4)(.9)+(-6)(.1)=+3$.

    In the long run, the pizza place gains an average of $3 per pizza delivered.
```

```{admonition} Example: Pizza Delivery #2
    If the pizza place wants to increase its mean gain per pizza to $3.90, how much should it raise the price from $10? We need to replace the original cost of 10 with an as-yet-to-be-determined new cost N, resulting in this probability distribution table:

    ```{figure} images/image026a.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." Here is the data in columns (X: P(X=x)): N-6: .9; -6: .1; In other words, when pizza delivery is not longer than half an hour, X = N-6, and P(X = N-6) = .9 . When pizza delivery takes longer than half an hour, X=-6, and P(X = -6) = .1 .

    A probability distribution table with two rows, labeled "X" and "P(X=x)." Here is the data in columns (X: P(X=x)): N-6: .9; -6: .1; In other words, when pizza delivery is not longer than half an hour, X = N-6, and P(X = N-6) = .9 . When pizza delivery takes longer than half an hour, X=-6, and P(X = -6) = .1 .
    ```

    Next, setting $\mu_{X}$ equal to +3.90 instead of +3, we solve

    $3.9=(N-6)(.9)+(-6)(.1)=.9N-6$ or

    $.9N=9.9$

    Therefore, the new price must be 11 dollars.
```

## Learn By Doing

We are going to look at a variation of the pizza delivery example. Here is the scenario.

The Acme Shipping Company has learned from experience that it costs $14.80 to deliver a small package overnight. The company charges $20 for such a shipment, but guarantees that they will refund the $20 charge if it does not arrive within 24 hours.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example: Raffle
    In order to raise money, a charity decides to raffle off some prizes. The charity sells 2,000 raffle tickets for $5 each. The prizes are:

    - 10 movie packages (two tickets plus popcorn) worth $25 each
    - 5 dinners for two worth $50 each
    - 2 smart phones worth $200 each
    - 1
                        flat-screen
                        TV worth
                        $1,500

    What is the expected gain or loss if you buy a single raffle ticket? The expected value can be written as E(X).

    There are 5 possible outcomes when you buy a ticket: win movie package, win dinner for two, win smart phone, win TV, win nothing.

    | prize | net gain or loss | probability |
    | --- | --- | --- |
    | movie package | 25 - 5 | 10 / 2000 |
    | dinner for two | 50 - 5 | 5 / 2000 |
    | smart phone | 200 - 5 | 2 / 2000 |
    | TV | 1500 - 5 | 1 / 2000 |
    | nothing | 0 - 5 | (2000 - 10 - 5 - 2 - 1) / 2000 |

    The previous information is summarized below in a probability distribution:

    ```{figure} images/image_raffle.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." Here is the data in column oriented format (X: P(X=x), comment): 20: 10/20000 (movie package); 45: 5/2000 (dinner for two); 195: 2/2000 (smart phone); 1495: 1/2000 (TV); -5: 1982/2000 (Nothing);

    A probability distribution table with two rows, labeled "X" and "P(X=x)." Here is the data in column oriented format (X: P(X=x), comment): 20: 10/20000 (movie package); 45: 5/2000 (dinner for two); 195: 2/2000 (smart phone); 1495: 1/2000 (TV); -5: 1982/2000 (Nothing);
    ```

    $\mu_{X}=E(X)=20(\frac{10}{2000})+45(\frac{5}{2000})+195(\frac{2}{2000})+1495(\frac{1}{2000})+(-5)(\frac{1982}{2000})$

    $E(X)=\frac{-7600}{2000}=-3.80$

    Since we got a negative number, we have an expected loss of $3.80 for each raffle ticket purchased. Recall that this is based upon a long-run average.

    Each raffle ticket has only 5 possible outcomes:

    - $20 net gain if you win the movie package
    - $45 net gain if you win the dinner for two
    - $195 net gain if you win the smart phone
    - $1,495 net
                            gain if you win the TV
    - $5 net loss if you do not win a prize

    It should not be surprising that you have an expected loss. After all, the charity's goal is to raise money. If you have an expected loss of $3.80 per ticket, they will have an expected gain of $3.80 per ticket. Each ticket gives the charity +5 (it was -5 for you). The prizes are reversed, too. For example, the movie package is -20 + 5 for the charity (it was 20 - 5 for you).
```
