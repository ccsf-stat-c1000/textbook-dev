# Hypothesis Testing for the Population Mean (3 of 9)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 3. Finding the p-value of the test

The p-value — the probability of getting data (summarized with the test statistic) as extreme as those observed or even more extreme (in the direction of the alternative hypothesis) when H~o~ is true — for the z-test for the population mean is found exactly like the p-value in the z-test for the population proportion. We've already learned that the p-value is found under the null distribution of the test statistic, and since for both means (with σ known) and proportions the null distribution of the test statistic is N(0,1), the p-value is calculated as follows:

##### Less Than

```{figure} images/image336.gif
:alt: H_a: μ &lt; μ_0 ⇒ p-value = P(Z ≤ z)

H_a: μ &lt; μ_0 ⇒ p-value = P(Z ≤ z)
```

```{figure} images/image259.gif
:alt: A N(0,1) curve for which the horizontal axis has been marked with two z-scores, z and 0, where z is the observed test statistic. z is to the left of 0, and the area to the left of z under the curve is the p-value.

A N(0,1) curve for which the horizontal axis has been marked with two z-scores, z and 0, where z is the observed test statistic. z is to the left of 0, and the area to the left of z under the curve is the p-value.
```

##### Greater Than

```{figure} images/image337.gif
:alt: H_a: μ &gt; μ_0 ⇒ p-value = P(Z ≥ z)

H_a: μ &gt; μ_0 ⇒ p-value = P(Z ≥ z)
```

```{figure} images/image261.gif
:alt: A N(0,1) curve for which the horizontal axis has been marked with two z-scores, z and 0, where z is the observed test statstic. z is to the right of 0, and the area to the right of z under the curve is the p-value.

A N(0,1) curve for which the horizontal axis has been marked with two z-scores, z and 0, where z is the observed test statstic. z is to the right of 0, and the area to the right of z under the curve is the p-value.
```

##### Not Equal To

```{figure} images/image338.gif
:alt: H_a: μ ≠ μ_0 ⇒ p-value = P(Z ≤ -|z|) + P(Z ≥ |z|) = 2P(Z ≥ |z|)

H_a: μ ≠ μ_0 ⇒ p-value = P(Z ≤ -|z|) + P(Z ≥ |z|) = 2P(Z ≥ |z|)
```

```{figure} images/image263.gif
:alt: A N(0,1) curve for which the horizontal axis has been marked with three z-scores, -|z|, 0, and |z|, where z is the test statistic. -|z| is to the left of 0, and |z| is to the right of 0. The p-value is the sum of the area to the right of |z| under the curve and the area to the left of -|z| under the curve.

A N(0,1) curve for which the horizontal axis has been marked with three z-scores, -|z|, 0, and |z|, where z is the test statistic. -|z| is to the left of 0, and |z| is to the right of 0. The p-value is the sum of the area to the right of |z| under the curve and the area to the left of -|z| under the curve.
```

```{admonition} Example: 1
    In the example about the SAT-M scores of students at Ross College, the test statistic was found to be z = 1. The p-value is therefore P(Z > 1):

    ```{figure} images/image339.gif
    :alt: A N(0,1) curve, with a horizontal axis marked with z-scores of 0 and 1. The area to the right of z-score 1 is the area we care about, because it is the p-value.

    A N(0,1) curve, with a horizontal axis marked with z-scores of 0 and 1. The area to the right of z-score 1 is the area we care about, because it is the p-value.
    ```

    To find the p-value, we can either:

    - use the (68% part of the) Standard Deviation Rule for the normal distribution, which tells us that the p-value is approximately 0.16 (since P(-1 < Z < 1) = 0.68), or
    - use the normal table, or
    - carry out the test using statistical software. In this case, we get a p-value of 0.159.

    ```{figure} images/image340.gif
    :alt: A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample of size n = 4 from the population, represented by a smaller circle. For this sample, x-bar = 550, and since our conditions are met, we can calculate that z = 1. We also calculate that the p-value = .159

    A large circle represents all of the Students at Ross College. We are interested in finding μ, or the mean of the SAT-M scores, which has a normal distribution. Our hypotheses are H_0: μ = 500 and H_a: μ &gt; 500, assuming SD = 100. We take a sample of size n = 4 from the population, represented by a smaller circle. For this sample, x-bar = 550, and since our conditions are met, we can calculate that z = 1. We also calculate that the p-value = .159
    ```
```

```{admonition} Example: 2
    In the concentration level example, the test statistic was found to be -2.5. Since this is the two-sided test, the p-value is the combination of the two shaded areas in the following figure.

    ```{figure} images/image341.gif
    :alt: A N(0,1) curve, with a horizontal axis marked with z-scores of -2.5, 0, and 2.5. The P-value is the area to the under the curve to the left of -2.5, and the area under the curve to the right of 2.5 .

    A N(0,1) curve, with a horizontal axis marked with z-scores of -2.5, 0, and 2.5. The P-value is the area to the under the curve to the left of -2.5, and the area under the curve to the right of 2.5 .
    ```

    The p-value is therefore twice P(Z > 2.5). We can either use the table, or carry out the test using statistical software. In this case, we get a p-value of 0.012.

    ```{figure} images/image342.gif
    :alt: A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that z = -2.5, and that the p-value = .012

    A large circle represents the population, which is the shipment. μ represents the concentration of the chemical. Our hypotheses are H_0:mean = 250, and H_a: mean is not 250. We assume that SD = 12). Selected from the population is a sample of size n=100, represented by a smaller circle. x-bar for this sample is 247, and because our conditions are met, we can calculate that z = -2.5, and that the p-value = .012
    ```
```
