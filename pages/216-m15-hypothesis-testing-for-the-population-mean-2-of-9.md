# Hypothesis Testing for the Population Mean (2 of 9)

```{admonition} Learning Objectives
    - In a given context, specify the null and alternative hypotheses for the population proportion and mean.
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 1. Stating the Hypotheses

The null and alternative hypotheses for the z-test for the population mean (μ) have exactly the same structure as the hypotheses for z-test for the population proportion (p):

* The null hypothesis has the form:

$H_{0}:\mu=\mu_{0}$

(where $\mu_{0}$ is the null value).

* The alternative hypothesis takes one of the following three forms (depending on the context):

$H_{a}:\mu<\mu_{0}$ (one-sided)

$H_{a}:\mu>\mu_{0}$ (one-sided)

$H_{a}:\mu\neq\mu_{0}$ (two-sided)

```{admonition} Example: 1
    In our example 1, based on a sample of 4 students from Ross College, we were testing whether the mean SAT-M of all of Ross College students is higher than the national mean (which, by construction, is 500).

    Here is the figure that summarizes example 1:

    ```{figure} images/image311.gif
    :alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. The question we want to answer is &quot;is the mean SAT-M 500 (national mean) or is it higher? (Assume: SD = 100).&quot; We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550.

    A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. The question we want to answer is &quot;is the mean SAT-M 500 (national mean) or is it higher? (Assume: SD = 100).&quot; We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550.
    ```
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{admonition} Example: 2
    Here we want to test whether the mean concentration of a certain chemical in a large shipment of a certain prescription drug is the required 250 ppm:

    ```{figure} images/image314.gif
    :alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. The question we want to answer is &quot;is the mean concentration the required 250ppm or not? (Assume: SD = 12).&quot; Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247.

    A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. The question we want to answer is &quot;is the mean concentration the required 250ppm or not? (Assume: SD = 12).&quot; Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247.
    ```

    The null and alternative hypotheses in this case are therefore:

    ```{figure} images/image320.gif
    :alt: H_0: μ = 250, H_a: μ ≠ 250

    H_0: μ = 250, H_a: μ ≠ 250
    ```
```

## 2. Collecting Data and Summarizing Them

Since our parameter of interest is the population mean (μ), once we collect the data, we find the sample mean ($\bar{x}$).

However, we already know that in hypothesis testing we go a step beyond calculating the relevant sample statistic and summarize the data with a test statistic.

Recall that in the z-test for the proportion, the test statistic is the z-score (standardized value) of the sample proportion, assuming that H~o~ is true. It should not be very surprising that in the z-test for the population mean, we do exactly the same thing.

The test statistic is the z-score (standardized value) of the sample mean ($\bar{x}$) assuming that H~o~ is true (in other words, assuming that $\mu=\mu_{0}$).

We rely once again on probability results—in this case, we refer to results about the sampling distribution of the sample mean ($\bar{X}$):

When we discussed probability models based on sampling distributions, we concluded that sample means behave as follows:

- Center: The mean of the sample means is µ, the population mean.
- Spread: The standard deviation of the sample means is $\frac{\sigma}{\sqrt{n}}$.
- Shape: The sample means are normally distributed if the variable is normally distributed in the population or the sample size is large enough to guarantee approximate normality. Recall that this last statement is the Central Limit Theorem. As a general guideline, we said that if n > 30, the Central Limit Theorem applies and we can use a normal curve as a probability model.

Based on this description of the sampling distribution of $\bar{X}$, we can define a test statistic that measures the distance between the hypothesized value of µ (denoted µ~o~) and the sample mean (determined by the data) in standard deviation units.

The test statistic is: $z=\frac{\bar{x}&minus;\mu_{0}}{\frac{&sigma;}{\sqrt{n}}}$ .

## Comments

1. Note that our test statistic (because it is a z-score), tells us how far $\bar{x}$ is from the null value $\mu_{0}$ measured in standard deviations. Since $\bar{x}$ represents the data and $\mu_{0}$ represents the null hypothesis, the test statistic is a measure of how different our data are from what is claimed in the null hypothesis. The larger the test statistic, the more evidence we have against H~o~, since what we saw in our data is very different from what H~o~ claims. This is an idea that we mentioned in the previous test as well.

2. As we established earlier, all inference procedures are based on probability. We are trying to determine if our sample results are likely or unlikely based on our assumptions about the population. This requires that we have a probability model that describes the long-term behavior of sample results that are randomly collected from a population that fits our hypothesis. For this reason, the Central Limit Theorem gives us criteria for deciding if the z-test for the population mean can be used. We need to verify:

(i) The sample is random (or at least can be considered as random in context).

(ii) We are in one of the three situations marked with a green check mark in the following table:

```{figure} images/image325.gif
:alt: A table with two columns and two rows, titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size.&quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;

A table with two columns and two rows, titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size.&quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;
```

3. If the conditions are met, then $\bar{X}$ values vary normally, or at least close enough to normally to use a normal model to calculate probabilities. When $\bar{X}$ values are normal, then the z-scores will be normally distributed with a mean of 0 and a standard deviation of 1.

Let's go back to our examples.

```{admonition} Example: 1
    Here is a summary of example 1:

    ```{figure} images/image327.gif
    :alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550.

    A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550.
    ```

    Let's start by checking the conditions:

    (i) The sample is random.

    (ii) The variable of interest, SAT-M scores, is assumed to vary normally in the population, so the fact that the sample size is small (n = 4) is not a problem. Sample means will be normally distributed and we can use a normal probability model based on z-scores to determine probabilities.

    ```{figure} images/image328.gif
    :alt: The same table as before. The &quot;Variable varies normally in the population, Small sample size&quot; case is what this example is. As a recap, the table has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK, (this is the case this example is); Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;

    The same table as before. The &quot;Variable varies normally in the population, Small sample size&quot; case is what this example is. As a recap, the table has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK, (this is the case this example is); Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK;
    ```

    The sample mean is $\bar{x}=550$, and so the test statistic is:

    $z=\frac{550−500}{\frac{100}{\sqrt{4}}}=1$

    This means that our data (represented by the sample mean) are only 1 standard deviation above the null value (500). Clearly, this provides some evidence against H~o~, but is this strong enough evidence to reject it? Probably not. This will be confirmed when we find the p-value. Here is an updated figure:

    ```{figure} images/image331.gif
    :alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550, and with our conditions met, we can find that z = 1.

    A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample from the population of size n = 4, represented by a smaller circle. For this sample, x-bar = 550, and with our conditions met, we can find that z = 1.
    ```
```

```{admonition} Example: 2
    ```{figure} images/image332.gif
    :alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247.

    A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247.
    ```

    In this case, the conditions that allow us to carry out the z-test are met since:

    (i) The sample is random.

    (ii) The sample size (n = 100) is large enough for the Central Limit Theorem to apply (note that in this case the large sample is essential since the concentration level is not known to vary normally).

    ```{figure} images/image333.gif
    :alt: The same table as before. The &quot;Variable doesn&apos;t vary normally in the population, Large sample size&quot; case is what this example is. As a recap, the table has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK, (this is the case this example is);

    The same table as before. The &quot;Variable doesn&apos;t vary normally in the population, Large sample size&quot; case is what this example is. As a recap, the table has two columns and two rows, and is titled &quot;Conditions: z-test for a population mean.&quot; The column headings are: &quot;Small Sample Size&quot; and &quot;Large Sample Size. &quot; The row headings are &quot;Variable varies normally in the population&quot; and &quot;Variable doesn&apos;t vary normally in the population.&quot; Here is the data in the table by cell in &quot;Row, Column: Value&quot; format: Variable varies normally in the population, Small sample size: OK; Variable varies normally in the population, Large sample size: OK; Variable doesn&apos;t vary normally in the population, Small sample size: NOT OK; Variable doesn&apos;t vary normally in the population, Large sample size: OK, (this is the case this example is);
    ```

    The z-statistic in this case is: $z=\frac{247−250}{\frac{12}{\sqrt{100}}}=−2.5$

    Our data (represented by the sample mean concentration level—247) are 2.5 standard deviations below the null value. A difference of 2.5 standard deviations is considered quite strong evidence against H~o~. (Essentially any difference that is above 2 standard deviations is considered quite large.) This will be confirmed when we find the p-value of the test. Here is an updated figure that represents the hypothesis testing process for this problem so far:

    ```{figure} images/image335.gif
    :alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that z = -2.5

    A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that z = -2.5
    ```
```

```{note} Video
[Test for Mean](https://www.youtube.com/watch?v=9WT3tK3o3mY)
```

```{note}
    **Learn By Doing**

    Hypothesis Testing for the Population Mean

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

Use the following histogram to answer the question below.

```{figure} images/_u5_m1_dig24a_01.gif
:alt: A histogram titled &quot;Histogram 1&quot;, and the vertical axis is labeled &quot;Frequency.&quot; Here is the data shown on the histogram, given in &quot;Horizontal axis value, vertical axis value&quot; format: 7: 1 8: 3 9: 3 10: 1 11: 4 12: 1 13: 1 14: 1

A histogram titled &quot;Histogram 1&quot;, and the vertical axis is labeled &quot;Frequency.&quot; Here is the data shown on the histogram, given in &quot;Horizontal axis value, vertical axis value&quot; format: 7: 1 8: 3 9: 3 10: 1 11: 4 12: 1 13: 1 14: 1
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Normal body temperature for healthy, at-rest human beings has always been said to be 98.6°F. A doctor has seen a lot of patients who had a lower or higher body temperature when they were not ill. He has read research that says it is actually lower. So, he collected 50 randomly selected temperatures that had a mean of 98.4°F. The standard deviation is known to be .35°F.

H~o~: μ = 98.6

H~a~: μ ≠ 98.6

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Each histogram in the questions below represents a random sample. We do not know if the variable is distributed normally in the population, but we want to be reasonably sure that the distribution of sample means will be normal so that we can use the z-test for testing claims about the population mean.

For each histogram, choose the option that best describes how to proceed with a hypothesis test for a population mean.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
