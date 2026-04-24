# Hypothesis Testing for the Population Proportion p (3 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 2. Collecting and Summarizing the Data (Using a Test Statistic)

After the hypotheses have been stated, the next step is to obtain a *sample* (on which the inference will be based), *collect relevant data*, and *summarize* them.

It is extremely important that our sample is representative of the population about which we want to draw conclusions. This is ensured when the sample is chosen at *random.* Beyond the practical issue of ensuring representativeness, choosing a random sample has theoretical importance that we will mention later.

In the case of hypothesis testing for the population proportion (p), we will collect data on the relevant categorical variable from the individuals in the sample and start by calculating the sample proportion, $\hat{p}$ (the natural quantity to calculate when the parameter of interest is p).

Let's go back to our three examples and add this step to our figures.

```{admonition} Example: 1
    ```{figure} images/image221.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still .20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still .20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective. p-hat = 64/400 = .16
    ```
```

```{admonition} Example: 2
    ```{figure} images/image222.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana. p-hat = 19/100 = .19
    ```
```

```{admonition} Example: 3
    ```{figure} images/image223.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat = 675/1000 = .675
    ```
```

As we mentioned earlier without going into details, when we summarize the data in hypothesis testing, we go a step beyond calculating the sample statistic and summarize the data with a *test statistic*. Every test has a test statistic, which to some degree captures the essence of the test. In fact, the p-value, which so far we have looked upon as "the king" (in the sense that everything is determined by it), is actually determined by (or derived from) the test statistic. We will now gradually introduce the test statistic.

The test statistic is *a measure* of how far the sample proportion $\hat{p}$ is from the null value $p_{0}$, the value that the null hypothesis claims is the value of p. In other words, since $\hat{p}$ is what the data estimates p to be, the test statistic can be viewed as a measure of the "distance" between what the data tells us about p and what the null hypothesis claims p to be.

Let's use our examples to understand this:

```{admonition} Example: 1
    The parameter of interest is p, the proportion of defective products following the repair.

    The data estimate p to be $\hat{p}=.16$

    The null hypothesis claims that p = .20

    The data are therefore .04 (or 4 percentage points) below the null hypothesis with respect to what they each tell us about p.

    It is hard to evaluate whether this difference of 4% in defective products is enough evidence to say that the repair was effective, but clearly, the larger the difference, the more evidence it is against the null hypothesis. So if, for example, our sample proportion of defective products had been, say, .10 instead of .16, then I think you would all agree that cutting the proportion of defective products in half (from 20% to 10%)would be extremely strong evidence that the repair was effective.
```

```{admonition} Example: 2
    The parameter of interest is p, the proportion of students in a college who use marijuana.

    The data estimate p to be $\hat{p}=.19$.

    The null hypothesis claims that p = .157

    The data are therefore .033 (or 3.3 percentage points) above the null hypothesis with respect to what they each tell us about p.
```

```{admonition} Example: 3
    The parameter of interest is p, the proportion of U.S. adults who support the death penalty for convicted murderers.

    The data estimate p to be $\hat{p}=.675$

    The null hypothesis claims that p = .64.

    There is a difference of .035 (3.5 percentage points) between the data and the null hypothesis with respect to what they each tell us about p.
```

There is a problem with just looking at the difference between the sample proportion $\hat{p}$ and the null value $p_{o}$.

Examples 2 and 3 illustrate this problem very well.

In example 2 we have a difference of 3.3 percentage points between the data and the null hypothesis, which is approximately the same as the difference in example 3 of 3.5 percentage points. However, the difference in example 3 of 3.5 percentage points is based on a *sample of size of 1,000* and therefore it is much *more impressive* than the difference of 3.3 percentage points in example 2, which was obtained from a sample of size of only 100.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
