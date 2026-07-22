# Step 4: Drawing Conclusions for a Mean

So far, we've discussed the first three steps in the hypothesis testing process of the z-test for the population mean (μ). The last step is to draw conclusions.

## Step 4: Drawing Conclusions

Here we assess the significance of the results (based on the p-value compared with some significance level of choice), and state our conclusions in context.

:::{admonition} Example 1: SAT-M Scores at Ross College
:class: tip

Here the p-value is quite large (0.159), which means that it is not very surprising to get data like those observed when $H_0$ is true. The results are therefore not significant, and so we do not have enough evidence to reject $H_0$ and conclude that the mean SAT-M of all Ross College students is higher than the national mean (500).

Note that even though the average SAT-M in our sample was 550 (which is substantially larger than 500), since this result was based on a sample of only 4 students, it does not provide enough evidence to conclude that the mean SAT-M is higher than 500.

The complete story of this example: $H_0: \mu = 500$ vs. $H_a: \mu > 500$; n = 4; $\bar{x} = 550$; z = 1; p-value = 0.159; since the p-value is large, we cannot reject $H_0$.
:::

:::{admonition} Example 2: Concentration of a Chemical in a Drug
:class: tip

In this example, the p-value is quite small (0.012). In particular, for a significance level of 0.05, the p-value indicates that the results are significant.

The data provide enough evidence for us to reject $H_0$ and conclude that the mean concentration level in the shipment is not the required 250 ppm.

The complete story of this example: $H_0: \mu = 250$ vs. $H_a: \mu \neq 250$; n = 100; $\bar{x} = 247$; z = −2.5; p-value = 0.012; since the p-value is small, we reject $H_0$.
:::

## Check Your Understanding: Sample Size and Conclusions

Let's revisit example 1 and see what a larger sample would have done. Suppose the dean had sampled 25 students (instead of 4) and again found a sample mean SAT-M of 550.

:::{quiz} With n = 25 and the same sample mean of 550, what is the test statistic?
:hint: z = (550 − 500)/(100/√25).
:feedback-0: Correct! The standard error shrinks to 100/√25 = 20, so z = 50/20 = 2.5.
:feedback-1: z = 1 was the value for n = 4; with n = 25 the standard error is smaller, so z is larger.
:feedback-2: Remember to divide σ by √n: 100/√25 = 20.
* *z = 2.5
* z = 1
* z = 0.5
:::

:::{quiz} The p-value for z = 2.5 (one-sided) is about 0.006. What do we conclude now, and what is the lesson?
:hint: Compare with the n = 4 case, where the same sample mean gave a p-value of 0.159.
:feedback-0: Correct! With 0.006 < 0.05 we now reject H₀. The same sample mean carries far more weight when it comes from a larger sample.
:feedback-1: 0.006 is much smaller than 0.05, so the results ARE significant.
:feedback-2: The data did not change in direction—the increased sample size is what strengthened the evidence.
* *Reject H₀—the same sample mean of 550 becomes convincing evidence when based on 25 students instead of 4
* Do not reject H₀—the results are still not significant
* The conclusion is unrelated to the sample size
:::
