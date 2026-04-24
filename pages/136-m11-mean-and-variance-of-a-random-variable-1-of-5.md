# Mean and Variance of a Random Variable (1 of 5)

```{admonition} Learning Objectives
    - Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

In the Exploratory Data Analysis (EDA) section, we displayed the distribution of one quantitative variable with a histogram, and supplemented it with numerical measures of center and spread. We are doing the same thing here. We display the probability distribution of a discrete random variable with a table, formula or histogram, and supplement it with numerical measures of the center and spread of the probability distribution. These measures are the *mean and standard deviation of the random variable.*

This section will be devoted to introducing these measures. As before, we'll start with the numerical measure of center, the mean. Let's begin by revisiting an example we saw in EDA.

## World Cup Soccer

Recall that we used the following data from 3 World Cup tournaments (a total of 192 games) to introduce the idea of a *weighted average*.

We've added a third column to our table that gives us relative frequencies.

| total # goals/game | frequency | relative frequency |
| --- | --- | --- |
| 0 | 17 | 17 / 192 = .089 |
| 1 | 45 | 45 / 192 = .234 |
| 2 | 51 | 51 / 192 = .266 |
| 3 | 37 | 37 / 192 = .193 |
| 4 | 25 | 25 / 192 = .130 |
| 5 | 11 | 11 / 192 = .057 |
| 6 | 3 | 3 / 192 = .016 |
| 7 | 2 | 2 / 192 = .010 |
| 8 | 1 | 1 / 192 = .005 |

| the mean for this data | = | $\frac{0(17)+1(45)+2(51)+3(37)+4(25)+5(11)+6(3)+7(2)+8(1)}{192}$ |
| --- | --- | --- |
| distributing the division by 192 we get: | = | $0(\frac{17}{192})+1(\frac{45}{192})+2(\frac{51}{192})+3(\frac{37}{192})+4(\frac{25}{192})+5(\frac{11}{192})+6(\frac{3}{192})+7(\frac{2}{192})+8(\frac{1}{192})$ |

Notice that the mean is each number of goals per game multiplied by its relative frequency. Since we usually write the relative frequencies as decimals, we can see that:

| mean number of goals per game | = | 0(.089) + 1(.234) + 2(.266) + 3(.193) + 4(.130) + 5(.057)                             + 6(.016) + 7(.010) + 8(.005) |
| --- | --- | --- |
|  | = | 2.36, rounded to two decimal places |

## Mean of a Random Variable

In Exploratory Data Analysis, we used the mean of a sample of quantitative values—their arithmetic average—to tell the center of their distribution. We also saw how a weighted mean was used when we had a frequency table. These frequencies can be changed to relative frequencies. So we are essentially using the relative frequency approach to find probabilities. We can use this to find the mean, or center, of a probability distribution for a random variable by reporting its mean, which will be a weighted average of its values; the more probable a value is, the more weight it gets. As always, it is important to distinguish between a concrete sample of observed values for a variable versus an abstract population of all values taken by a random variable in the long run.

Whereas we denoted the mean of a sample as $\bar{x}$, we now denote the mean of a random variable as $\mu_{X}$. Let's see how this is done by looking at a specific example.

```{admonition} Example: Xavier's Production Line
    Xavier's production line produces a variable number of defective parts in an hour, with probabilities shown in this table:

    ```{figure} images/image012.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;

    A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;
    ```

    How many defective parts are typically produced in an hour on Xavier's production line? If we sum up the possible values of X, each weighted with its probability, we have

    $\mu_{X}=0(0.15)+1(0.30)+2(0.25)+3(0.20)+4(0.10)=1.8$
```

Here is the general definition of the mean of a discrete random variable:

```{admonition} Definition: mean of a discrete random variable
    In general, for any discrete random variable X with probability
                                    distribution

                                the *mean* of X is defined to be

                                    $\mu_{X}=x_{1}p_{1}+x_{2}p_{2}+...+x_{n}p_{n}=\sum_{i=1}^{n}x_{i}p_{i}$
```

```{figure} images/image011.gif
:alt: white space

white space
```

In general, the mean of a random variable tells us its "long-run" average value. It is sometimes referred to as the *expected value* of the random variable. But this expression may be somewhat misleading, because in many cases it is impossible for a random variable to actually equal its expected value. For example, the mean number of goals for a World Cup soccer game is 2.36. But we can never expect any single game to result in 2.36 goals, since it is not possible to score a fraction of a goal. Rather, 2.36 is the long-run average of all World Cup soccer games. In the case of Xavier's production line, the mean number of defective parts produced in an hour is 1.8. But the actual number of defective parts produced in any given hour can never equal 1.8, since it must take whole number values.

To get a better feel for the mean of a random variable, let's extend the defective parts example:

```{admonition} Example: Xavier's and Yves' Production Lines
    Recall the probability distribution of the random variable X, representing the number of defective parts in an hour produced by Xavier's production line.

    ```{figure} images/image012.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;

    A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in columns (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;
    ```

    The number of defective parts produced each hour by Yves' production line is a random variable Y with the following probability distribution:

    ```{figure} images/image022.gif
    :alt: A probability distribution table with two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .05; 1: .05; 2: .10; 3: .75; 4: .05;

    A probability distribution table with two rows, labeled "Y" and "P(Y=y)." The data in column format (Y: P(Y=y)): 0: .05; 1: .05; 2: .10; 3: .75; 4: .05;
    ```

    Look at both probability distributions. Both X and Y take the same possible values (0, 1, 2, 3, 4).

    However, they are very different in the way the probability is distributed among these values.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
