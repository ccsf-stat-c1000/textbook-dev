# The z-Test for a Proportion: Summary

## Let's Summarize

We have now completed going through the four steps of hypothesis testing, and in particular, we learned how they are applied to the z-test for the population proportion. Let's briefly summarize:

### Step 1

State the null and alternative hypotheses:

$$H_0: p = p_0$$

$$H_a: p < p_0 \quad \text{or} \quad H_a: p > p_0 \quad \text{or} \quad H_a: p \neq p_0$$

where the choice of the appropriate alternative (out of the three) is usually quite clear from the context of the problem.

### Step 2

Obtain data from a sample and:

1. Check whether the data satisfy the conditions which allow you to use this test:

   - Random sample (or at least a sample that can be considered random in context)
   - $np_0 \geq 10$ and $n(1-p_0) \geq 10$

2. Calculate the sample proportion $\hat{p}$, and summarize the data using the test statistic:

   $$z=\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}}$$

   (*Recall:* this standardized test statistic represents how many standard deviations above or below $p_0$ our sample proportion $\hat{p}$ is.)

### Step 3

Find the p-value of the test either by using software or by using the test statistic as follows:

- For $H_a: p < p_0$: p-value = $P(Z \leq z)$
- For $H_a: p > p_0$: p-value = $P(Z \geq z)$
- For $H_a: p \neq p_0$: p-value = $2P(Z \geq |z|)$

### Step 4

Reach a conclusion first regarding the significance of the results, and then determine what it means in the context of the problem. Recall that:

If the p-value is small (in particular, smaller than the significance level, which is usually 0.05), the results are significant (in the sense that there is a significant difference between what was observed in the sample and what was claimed in $H_0$), and so we reject $H_0$. If the p-value is not small, we do not have enough statistical evidence to reject $H_0$, and so we continue to believe that $H_0$ *may* be true. (Remember: in hypothesis testing we never "accept" $H_0$.)

## Check Your Understanding: Carrying Out a Complete Test

A city claims that 30% of its residents bike to work at least once a week. A local advocacy group suspects the true proportion is lower. In a random sample of 500 residents, 130 bike to work at least once a week.

:::{quiz} Carry out step 1: what are the hypotheses?
:hint: The claimed value is 0.30; the group suspects it is lower.
:feedback-0: Correct! $H_0$: $p = 0.30$; $H_a$: $p < 0.30$.
:feedback-1: The suspicion is specifically that the rate is lower, so the alternative is one-sided.
* *$H_0$: $p = 0.30$; $H_a$: $p < 0.30$
* $H_0$: $p = 0.30$; $H_a$: $p \neq 0.30$
:::

:::{quiz} Carry out step 2: are the conditions met, and what is the test statistic?
:hint: p-hat = $130/500 = 0.26$; the standard error is $\sqrt{0.30 \times 0.70/500} \approx 0.0205$.
:feedback-0: Correct! $np_0 = 150$ and n(1 - $p_0) = 350$ are both $\geq 10$, and $z = (0.26 - 0.30)/0.0205 \approx -1.95$.
:feedback-1: Check the standard error: $\sqrt{0.30 \times 0.70/500} \approx 0.0205$, so $z \approx -1.95$, not -0.04.
:feedback-2: The conditions ARE met: $np_0 = 150$ and n(1 - $p_0) = 350$.
* *Conditions met; $z \approx -1.95$
* Conditions met; $z \approx -0.04$
* Conditions are not met
:::

:::{quiz} Steps 3 and 4: the p-value is P(Z $\leq -1.95) \approx 0.026$. Using $\alpha = 0.05$, what is the conclusion?
:hint: Compare 0.026 with 0.05 and state the conclusion in context.
:feedback-0: Correct! Since $0.026 < 0.05$, we reject $H_0$ and conclude that fewer than 30% of residents bike to work weekly.
:feedback-1: 0.026 is smaller than 0.05, so the results ARE significant.
:feedback-2: The conclusion must be in context—about the proportion of residents who bike to work.
* *Reject $H_0$—the data provide significant evidence that fewer than 30% of residents bike to work weekly
* Do not reject $H_0$—the evidence is not strong enough
* Reject $H_0$ (no context needed)
:::

What's next?

Before we move on to the next test, we use the z-test for proportions to bring up and illustrate some very important issues regarding hypothesis testing.
