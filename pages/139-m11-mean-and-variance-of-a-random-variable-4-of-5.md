# Mean and Variance of a Random Variable (4 of 5)

```{admonition} Learning Objectives
    - Find the mean and variance of a discrete random variable, and apply these concepts to solve real-world problems.
```

## Variance and Standard Deviation of a Discrete Random Variable

In Exploratory Data Analysis, we used the mean of a sample of quantitative values (their arithmetic average, $\bar{x}$) to tell the center of their distribution, and the standard deviation (s) to tell the typical distance of sample values from their mean. We described the center of a probability distribution for a random variable by reporting its mean $\mu_{X}$, and now we would like to establish an accompanying measure of spread. Our measure of spread will still report the typical distance of values from their means, but in order to distinguish the spread of a population of all of a random variable's values from the spread (s) of sample values, we will denote the standard deviation of the random variable X with the Greek lower case "sigma," and use a subscript to remind us what is the variable of interest (there may be more than one in later problems):

## Notation:σX

We will also focus more frequently than before on the squared standard deviation, called the *variance*, because some important rules we need to invoke are in terms of variance $\sigma_{X}^{2}$ rather than standard deviation $\sigma_{X}$.

```{admonition} Example: Xavier's Production Line
    Recall that the number of defective parts produced each hour by Xavier's production line is a random variable X with the following probability distribution:

    ```{figure} images/image012.gif
    :alt: A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;

    A probability distribution table with two rows, labeled "X" and "P(X=x)." The data in column format (X: P(X=x)): 0: .15; 1: .30; 2: .25; 3: .20; 4: .10;
    ```

    We found the mean number of defective parts produced per hour to be $\mu_{X}$ = 1.8. Obviously, there is variation about this mean: some hours as few as 0 defective parts are produced, whereas in other hours as many as 4 are produced. Typically, how far does the number of defective parts fall from the mean of 1.8? As we did for the spread of sample values, we measure the spread of a random variable by calculating the square root of the average squared deviation from the mean. Now "average" is a weighted average, where more probable values of the random variable are accordingly given more weight. Let's begin with the variance, or average squared deviation from the mean, and then take its square root to find the standard deviation:

    ```{figure} images/image033.gif
    :alt: A table describing for several characteristics of of possible values of X. For X=0, Dev. from mean = (0-1.8), Sq. deviation = (0-1.8)², and P(X=0) = .15 . For X=1, Dev. from mean = (1-1.8), Sq. deviation = (1-1.8)², and P(X=1) = .30. For X=2, Dev. from mean = (2-1.8), Sq. deviations = (2-1.8)², and P(X=2) = .25 . For X=3, Dev. from mean = (3-1.8), Sq. deviations = (3-1.8)², and P(X=3) = .20 . For X=4, Dev. from mean = (4-1.8), Sq. deviations = (4-1.8)², and P(X=4) = .10 .

    A table describing for several characteristics of of possible values of X. For X=0, Dev. from mean = (0-1.8), Sq. deviation = (0-1.8)², and P(X=0) = .15 . For X=1, Dev. from mean = (1-1.8), Sq. deviation = (1-1.8)², and P(X=1) = .30. For X=2, Dev. from mean = (2-1.8), Sq. deviations = (2-1.8)², and P(X=2) = .25 . For X=3, Dev. from mean = (3-1.8), Sq. deviations = (3-1.8)², and P(X=3) = .20 . For X=4, Dev. from mean = (4-1.8), Sq. deviations = (4-1.8)², and P(X=4) = .10 .
    ```

    $Variance=\sigma_{X}^{2}=(0-1.8)^{2}(0.15)+(1-1.8)^{2}(0.30)+(2-1.8)^{2}(0.25)+(3-1.8)^{2}(0.20)+(4-1.8)^{2}(0.1)=1.46$

    $standard deviation=\sigma_{X}=\sqrt{1.46}=1.21$
```

How do we interpret the standard deviation of X?

Xavier's production line produces an average of 1.80 defective parts per hour. The number of defective parts varies from hour to hour; typically (or, on average), it is about 1.21 away from 1.80.

Here is the formal definition:

```{admonition} Definition: standard deviation of a discrete random variable
    For any discrete random variable X with
                                    a
                                    probability
                                    distribution
                                    of

    the *variance* of X is defined to
                                    be

    $\sigma_{X}^{2}=(x_{1}-\mu_{X})^{2}p_{1}+(x_{2}-\mu_{X})^{2}p_{2}+...+(x_{n}-\mu_{X})^{2}p_{n}$
    $=\sum_{i=1}^{n}(x_{i}-\mu_{X})^{2}p_{i}$

    and the *standard deviation* is

    $\sigma_{X}=\sqrt{\sigma_{X}^{2}}$
```

```{figure} images/image011.gif
:alt: white space

white space
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

The purpose of the next activity is to give you better intuition about the mean and standard deviation of a random variable.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
