# Step 3: Finding the P-value for a Mean

```{admonition} Learning Objectives
:class: note

- Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Step 3: Finding the P-value of the Test

The p-value—the probability of getting data (summarized with the test statistic) as extreme as those observed or even more extreme (in the direction of the alternative hypothesis) when $H_0$ is true—for the z-test for the population mean is found exactly like the p-value in the z-test for the population proportion. We've already learned that the p-value is found under the null distribution of the test statistic, and since for both means (with σ known) and proportions the null distribution of the test statistic is N(0,1), the p-value is calculated as follows:

### Less Than

For $H_a: \mu < \mu_0$, the p-value is $P(Z \leq z)$—the area under the standard normal curve to the left of the observed test statistic (a left-tailed test).

```{figure} images/gen/m15-pvalue-left.svg
:alt: A standard normal curve with z-scores 0 and z marked on the horizontal axis, where z is to the left of 0. The p-value is the shaded area to the left of z under the curve.
```

### Greater Than

For $H_a: \mu > \mu_0$, the p-value is $P(Z \geq z)$—the area under the standard normal curve to the right of the observed test statistic (a right-tailed test).

```{figure} images/gen/m15-pvalue-right.svg
:alt: A standard normal curve with z-scores 0 and z marked on the horizontal axis, where z is to the right of 0. The p-value is the shaded area to the right of z under the curve.
```

### Not Equal To

For $H_a: \mu \neq \mu_0$, the p-value is $P(Z \leq -|z|) + P(Z \geq |z|) = 2P(Z \geq |z|)$—the combined area in both tails (a two-tailed test).

```{figure} images/gen/m15-pvalue-two.svg
:alt: A standard normal curve with z-scores negative absolute z, 0, and positive absolute z marked on the horizontal axis. The p-value is the sum of the shaded areas in both tails.
```

:::{admonition} Example 1: SAT-M Scores at Ross College
:class: tip

In the example about the SAT-M scores of students at Ross College, the test statistic was found to be z = 1. Since the alternative is $H_a: \mu > 500$, the p-value is P(Z > 1)—the area to the right of 1 under the standard normal curve.

To find the p-value, we can either:

- use the (68% part of the) Standard Deviation Rule for the normal distribution, which tells us that the p-value is approximately 0.16 (since P(−1 < Z < 1) = 0.68, each tail beyond 1 standard deviation holds about 0.16), or
- use a normal table, or
- carry out the test using statistical software. In this case, we get a p-value of 0.159.
:::

:::{admonition} Example 2: Concentration of a Chemical in a Drug
:class: tip

In the concentration level example, the test statistic was found to be z = −2.5. Since this is a two-sided test ($H_a: \mu \neq 250$), the p-value is the combination of the two tail areas: the area to the left of −2.5 plus the area to the right of 2.5.

The p-value is therefore 2 × P(Z > 2.5). We can either use a table or carry out the test using statistical software. In this case, we get a p-value of 0.012.
:::

## Check Your Understanding: Finding the P-value for a Mean

:::{quiz} A z-test for μ with alternative Hₐ: μ < μ₀ produces z = −1.5. Which expression gives the p-value?
:hint: A "less than" alternative is left-tailed.
:feedback-0: Correct! For a left-tailed test, the p-value is the area to the left of the observed test statistic: P(Z ≤ −1.5) ≈ 0.067.
:feedback-1: The area to the right of −1.5 (≈ 0.933) would essentially measure agreement with H₀.
:feedback-2: Doubling is only for two-sided alternatives.
* *P(Z ≤ −1.5)
* P(Z ≥ −1.5)
* 2P(Z ≤ −1.5)
:::

:::{quiz} In example 2, the p-value was 0.012. Which is the correct interpretation?
:hint: Condition on H₀ (μ = 250) being true, and remember the two-sided alternative.
:feedback-0: Correct! If the mean concentration really were 250 ppm, there would be only a 0.012 probability of getting a sample mean at least 2.5 standard deviations away from 250 (in either direction).
:feedback-1: The p-value is not the probability that H₀ is true.
:feedback-2: Since the alternative is two-sided, "as extreme" includes both directions, not just below.
* *If μ were 250 ppm, the probability of a sample mean as far from 250 as 247 is (in either direction) would be 0.012
* There is a 1.2% chance that the mean concentration is 250 ppm
* If μ were 250 ppm, the probability of a sample mean of 247 or lower would be 0.012
:::
