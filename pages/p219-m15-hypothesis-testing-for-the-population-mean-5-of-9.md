# Tests and Confidence Intervals for a Mean

## Relating Hypothesis Tests and Confidence Intervals

Just as we did for proportions, we may examine a confidence interval to decide whether a proposed value of the population mean is plausible.

Suppose we want to test $H_0: \mu = \mu_0$ vs. $H_a: \mu \neq \mu_0$ using a significance level of $\alpha = 0.05$. An alternative way to perform this test is to find a 95% confidence interval for $\mu$ and make the following conclusions:

- If $\mu_0$ falls *outside* the confidence interval, *reject* $H_0$.
- If $\mu_0$ falls *inside* the confidence interval, *do not reject* $H_0$.

:::{admonition} Example: Concentration of a Chemical in a Drug
:class: tip

We'll use example 2, in which the alternative was two-sided.

Recall that we want to check whether a medication conforms to a target concentration of a chemical ingredient by testing $H_0: \mu = 250$ vs. $H_a: \mu \neq 250$. We assume that $\sigma = 12$, and in a sample of size $n = 100$ we obtained a sample mean of $\bar{x}=247$.

A 95% confidence interval for $\mu$ is:

$$\bar{x}\pm2\frac{\sigma}{\sqrt{n}}=247\pm2\frac{12}{\sqrt{100}}=247\pm2.4=(244.6,\ 249.4)$$

Since the interval does not contain 250, we reject $H_0$ and conclude that the alternative is true: the population mean concentration differs from 250.
:::

## Check Your Understanding: Reading Software Output

One of the following software outputs is internally consistent; the others were edited to be incorrect. All three report the same data summary: $N = 35$, Mean = 260.000, assumed $\sigma = 16$, SE Mean = 2.704, 95% CI (254.699, 265.301).

| Output | Test of $\mu$ = ... vs $\neq$ | Z | P |
| --- | --- | --- | --- |
| A | 264 | -2.22 | 0.047 |
| B | 267 | -2.22 | 0.087 |
| C | 266 | -2.22 | 0.027 |

:::{quiz} Which output is the correct (unedited) one?
:hint: Check each: does $z = (260 - \mu_0)/2.704$ match? Does the p-value agree with the z? Does the test conclusion agree with whether $\mu_0$ is inside the CI?
:feedback-0: Correct! For C: $z = (260 - 266)/2.704 \approx -2.22$ ✓; the two-sided p-value for $z = -2.22$ is about 0.027 ✓; and 266 is outside the CI, consistent with $p < 0.05$ ✓.
:feedback-1: For A, z should be $(260 - 264)/2.704 \approx -1.48$, not -2.22; also 264 lies INSIDE the CI, which contradicts a p-value below 0.05.
:feedback-2: For B, z should be $(260 - 267)/2.704 \approx -2.59$, and 267 lies outside the CI, which contradicts a p-value above 0.05.
* *Output C
* Output A
* Output B
:::

```{admonition} Comment
:class: important

Beyond using the confidence interval as a quick way to carry out the two-sided test, the confidence interval can provide insight into the actual value of the population mean if $H_0$ is rejected. In the concentration level example, $H_0$ was rejected, and all we could conclude about the mean concentration level of the entire shipment, $\mu$, was that it was not 250. The 95% confidence interval for $\mu$, (244.6, 249.4), gives us an idea of what plausible values for $\mu$ would be. In particular, we can conclude that since the confidence interval lies below 250, at least a large portion of the shipment contains medication that is ineffective.
```

## Check Your Understanding: Tests and Intervals for a Mean

A machine fills bottles with a target of 500 ml. A quality check tests $H_0: \mu = 500$ vs. $H_a: \mu \neq 500$ at the 0.05 level, and a 95% confidence interval for $\mu$ from the sample is (500.8, 503.2).

:::{quiz} What is the conclusion of the test, and what extra insight does the interval give?
:hint: Is 500 inside (500.8, 503.2)? Where does the whole interval lie relative to 500?
:feedback-0: Correct! 500 is outside the interval, so we reject $H_0$—and since the interval lies entirely above 500, we learn the machine is overfilling, by roughly 1 to 3 ml.
:feedback-1: 500 is NOT inside the interval (it is below 500.8), so we do reject $H_0$.
:feedback-2: The interval lies above 500, indicating OVERfilling, not underfilling.
* *Reject $H_0$—the machine appears to be overfilling by about 1 to 3 ml
* Do not reject $H_0$—500 is a plausible value
* Reject $H_0$—the machine appears to be underfilling
:::

We are done with the case where the population standard deviation, $\sigma$, is known. We now move on to the more common case where $\sigma$ is unknown.
