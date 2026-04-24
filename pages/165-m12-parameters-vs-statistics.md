# Parameters vs. Statistics

```{admonition} Learning Objectives
    - Identify and distinguish between a parameter and a statistic.
    - Explain the concepts of sampling variability and sampling distribution.
```

To better understand the relationship between sample and population, let's consider the two examples that were mentioned in the introduction.

```{admonition} Example: Example #1: Blood Type
    In the probability section, we presented the distribution of blood types in the entire U.S. *population*:

    ```{figure} images/image002.gif
    :alt: A pie chart titled "Blood Types (population)." Type A is 42% of the chart, type O takes up 45% of the chart, type B is 10% of the chart, and type AB is 4%.

    A pie chart titled "Blood Types (population)." Type A is 42% of the chart, type O takes up 45% of the chart, type B is 10% of the chart, and type AB is 4%.
    ```

    Assume now that we take a *sample* of 500 people in the United States, record their blood type, and display the sample results:

    ```{figure} images/image003.gif
    :alt: A pie char titled "Blood Type (sample 1)." Here is the data for each slice on the chart: A: 198, 39.6%; O: 221, 44.2%; B: 59, 11.8%; AB: 22, 4.4%;

    A pie char titled "Blood Type (sample 1)." Here is the data for each slice on the chart: A: 198, 39.6%; O: 221, 44.2%; B: 59, 11.8%; AB: 22, 4.4%;
    ```

    Note that the percentages (or proportions) that we got in our sample are slightly different than the population percentages. This is really not surprising. Since we took a sample of just 500, we cannot expect that our sample will behave exactly like the population, but if the sample is random (as it was), we expect to get results which are not that far from the population (as we did). If we took yet another sample of size 500:

    ```{figure} images/image004.gif
    :alt: A pie char titled "Blood Type (sample 2)." Here is the data for each slice on the chart: A: 216, 43.2%; O: 213, 42.6%; B: 39, 7.8%; AB: 32, 6.4%;

    A pie char titled "Blood Type (sample 2)." Here is the data for each slice on the chart: A: 216, 43.2%; O: 213, 42.6%; B: 39, 7.8%; AB: 32, 6.4%;
    ```

    we again get sample results that are slightly different from the population figures, and also different from what we got in the first sample. This very intuitive idea, that sample results change from sample to sample, is called *sampling variability.*
```

Let's look at another example:

```{admonition} Example: Example #2: Heights of Adult Males
    Heights among the population of all adult males follow a normal distribution with a mean $\mu=69$ inches and a standard deviation

    $\sigma=2.8$ inches. Here is a probability display of this population distribution:

    ```{figure} images/image007.gif
    :alt: A probability histogram, in which the horizontal axis is labeled "Male Height." The axis ranges from 57.6 to 80.0, and the mode of the histogram is at a height of 69. The histogram's shape is very close to a normal bell shape.

    A probability histogram, in which the horizontal axis is labeled "Male Height." The axis ranges from 57.6 to 80.0, and the mode of the histogram is at a height of 69. The histogram's shape is very close to a normal bell shape.
    ```

    A sample of 200 males was chosen, and their heights were recorded. Here are the sample results:

    ```{figure} images/image009.gif
    :alt: A distribution histogram for the sample. The mode for this histogram is at a height of about 70. The bars to the left of the mode are an acceptable approximation of a normal bell curve, but to the right of the mode, the bars drop off too suddenly to approximate a bell curve.

    A distribution histogram for the sample. The mode for this histogram is at a height of about 70. The bars to the left of the mode are an acceptable approximation of a normal bell curve, but to the right of the mode, the bars drop off too suddenly to approximate a bell curve.
    ```

    The sample mean is $\bar{x}=68.7$ inches and the sample standard deviation is s = 2.95 inches.

    Again, note that the sample results are slightly different from the population. The histogram we got resembles the normal distribution, but is not as fine, and also the sample mean and standard deviation are slightly different from the population mean and standard deviation. Let's take another sample of 200 males:

    ```{figure} images/image011.gif
    :alt: A distribution histogram of another sample. The mode is once again at about 70. The bars to the left of the mode approximate a bell curve except for a few which are too low. To the right of the mean we have the same problem as before - the values drop off too fast to model a bell curve.

    A distribution histogram of another sample. The mode is once again at about 70. The bars to the left of the mode approximate a bell curve except for a few which are too low. To the right of the mean we have the same problem as before - the values drop off too fast to model a bell curve.
    ```

    The sample mean is $\bar{x}=69.065$ inches and the sample standard deviation is s = 2.659 inches.

    Again, as in Example 1 we see the idea of *sampling variability.* Again, the sample results are pretty close to the population, and different from the results we got in the first sample.
```

In both the examples, we have numbers that describe the population, and numbers that describe the sample. In Example 1, the number 42% is the population proportion of blood type A, and 39.6% is the sample proportion (in sample 1) of blood type A. In Example 2, 69 and 2.8 are the population mean and standard deviation, and (in sample 1) 68.7 and 2.95 are the sample mean and standard deviation.

```{admonition} Definition: parameter and statistic
    A *parameter* is a number that describes the population; a *statistic* is a number that is computed from the sample.
```

In Example 1: 42% is the parameter and 39.6% is a statistic.

In Example 2: 69 and 2.8 are the parameters and 68.7 and 2.95 are the statistics.

In this course, as in the examples above, we focus on the following parameters and statistics:

- population proportion and sample proportion
- population mean and  sample mean
- population standard deviation and sample standard deviation

The following table summarizes the three pairs, and gives the notation

|  | (Population) Parameter | (Sample) Statistic |
| --- | --- | --- |
| *Proportion* | $p$ | $\hat{p}$ |
| *Mean* | $\mu$ | $\bar{x}$ |
| *Standard Deviation* | $\sigma$ | $s$ |

The only new notation here is p for population proportion (p = .42 for type A in Example 1), and $\hat{p}$ for sample proportion

($\hat{p}$ = .396 for type A in Example 1).

## Comments

1. Parameters are usually unknown, because it is impractical or impossible to know exactly what values a variable takes for every member of the population.

2. Statistics are computed from the sample, and vary from sample to sample due to *sampling variability*.

In the last part of the course, statistical inference, we will learn how to use a statistic to draw conclusions about an unknown parameter, either by estimating it or by deciding whether it is reasonable to conclude that the parameter equals a proposed value. In this module, we'll learn about the behavior of the statistics assuming that we know the parameters. So, for example, if we know that the population proportion of blood type A in the population is .42, and we take a random sample of size 500, what do we expect the sample proportion ($\hat{p}$) to be?

Here are some more examples:

```{admonition} Example
    If students picked numbers completely at random from the numbers 1 to 20, the proportion of times that the number 7 would be picked is .05. When 15 students picked a number "at random" from 1 to 20, 3 of them picked the number 7. Identify the parameter and accompanying statistic in this situation.

    The parameter is the population proportion of random selections resulting in the number 7, which is p = .05. The accompanying statistic is the sample proportion of selections resulting in the number 7, which is $\hat{p}=3/15=0.20$.
```

```{admonition} Example
    The length of human pregnancies has a mean of 266 days and a standard deviation of 16 days. A random sample of 9 pregnant women was observed to have a mean pregnancy length of 270 days, with a standard deviation of 14 days. Identify the parameters and accompanying statistics in this situation.

    The parameters are population mean $\mu=266$ and population standard deviation $\sigma=16$. The accompanying statistics are sample mean $\bar{x}=270$ and sample standard deviation $s=14$.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
