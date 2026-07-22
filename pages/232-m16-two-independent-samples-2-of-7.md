# The Two-Sample t-Test: Stating the Hypotheses

## The Two-Sample t-Test

Here again is the general situation which requires us to use the two-sample t-test: two sub-populations with means $\mu_1$ and $\mu_2$, from which two independent random samples of sizes $n_1$ and $n_2$ are drawn. Our goal is to compare the means $\mu_1$ and $\mu_2$ based on the two independent samples.

## Step 1: Stating the Hypotheses

The hypotheses represent our goal, comparing the means $\mu_1$ and $\mu_2$:

- The null hypothesis has the form $H_0: \mu_1 - \mu_2 = 0$ (which is the same as $H_0: \mu_1 = \mu_2$).
- The alternative hypothesis takes one of the following three forms (depending on the context):
  - $H_a: \mu_1 - \mu_2 < 0$ (which is the same as $H_a: \mu_1 < \mu_2$) (one-sided)
  - $H_a: \mu_1 - \mu_2 > 0$ (which is the same as $H_a: \mu_1 > \mu_2$) (one-sided)
  - $H_a: \mu_1 - \mu_2 \neq 0$ (which is the same as $H_a: \mu_1 \neq \mu_2$) (two-sided)

Note that the null hypothesis claims that there is no difference between the means, which can be represented either as "the difference is 0" or as its (algebraically and conceptually) equivalent, $\mu_1 = \mu_2$ (the means are equal). Either way, conceptually, $H_0$ claims that there is no relationship between the two relevant variables.

The first way of writing the hypotheses (using a difference between the means) will be easier to use when (in the future) we look for a difference that is not 0.

Each one of the three alternatives claims that there is a difference between the means. The two one-sided alternatives specify the nature of the difference: either negative, indicating that $\mu_1$ is smaller than $\mu_2$, or positive, indicating that $\mu_1$ is larger than $\mu_2$. The two-sided alternative, as usual, is more general and simply claims that a difference exists. As before, it should be clear from the context of the problem which of the three alternatives is appropriate.

```{admonition} Comment
:class: important

Note that our parameter of interest in this case (the parameter about which we are making an inference) is the *difference between the means*, $\mu_1 - \mu_2$, and that the null value is 0.
```

:::{admonition} Example: Looks vs. Personality
:class: tip

Recall that the purpose of this survey was to examine whether the opinions of females and males *differ* with respect to the importance of looks vs. personality. The hypotheses in this case are therefore:

- $H_0: \mu_1 - \mu_2 = 0$
- $H_a: \mu_1 - \mu_2 \neq 0$

where $\mu_1$ represents the mean importance score for females and $\mu_2$ represents the mean importance score for males.

It is important to understand that conceptually, the two hypotheses claim:

- $H_0$: score (of looks vs. personality) is *not related* to gender
- $H_a$: score (of looks vs. personality) is *related* to gender
:::

## Check Your Understanding: Hypotheses for Two Means

In order to check the claim that the pregnancy length of women who smoke during pregnancy is shorter, on average, than the pregnancy length of women who do not smoke, a random sample of 35 pregnant women who smoke and a random sample of 35 pregnant women who do not smoke were chosen and their pregnancy lengths were recorded. Here, population 1 is pregnant women who smoke (mean pregnancy length $\mu_1$) and population 2 is pregnant women who do not smoke (mean pregnancy length $\mu_2$).

:::{quiz} What are the appropriate hypotheses for this study?
:hint: The claim being checked is that smokers' pregnancies are SHORTER on average.
:feedback-0: Correct! H₀: μ₁ − μ₂ = 0 (no difference); Hₐ: μ₁ − μ₂ < 0 (smokers' mean length is shorter than non-smokers').
:feedback-1: The claim is directional (shorter), so the two-sided alternative doesn't capture it.
:feedback-2: This says smokers' pregnancies are LONGER—the reverse of the claim.
* *H₀: μ₁ − μ₂ = 0; Hₐ: μ₁ − μ₂ < 0
* H₀: μ₁ − μ₂ = 0; Hₐ: μ₁ − μ₂ ≠ 0
* H₀: μ₁ − μ₂ = 0; Hₐ: μ₁ − μ₂ > 0
:::

:::{quiz} Conceptually, what does the null hypothesis claim in this study?
:hint: Think in terms of the relationship between the two variables.
:feedback-0: Correct! H₀ claims smoking status is not related to pregnancy length—the two population means are equal.
:feedback-1: This is the ALTERNATIVE hypothesis, not the null.
:feedback-2: The null hypothesis concerns the population means, not sample results.
* *Smoking during pregnancy is not related to pregnancy length
* Smoking during pregnancy shortens pregnancy length
* The two sample means will be exactly equal
:::
