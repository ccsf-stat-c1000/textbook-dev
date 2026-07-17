# The Paired t-Test: Stating the Hypotheses

```{admonition} Learning Objectives
:class: note

- Specify the null and alternative hypotheses for comparing groups.
```

## Step 1: Stating the Hypotheses

Recall that in the t-test for a single mean our null hypothesis was $H_0: \mu = \mu_0$ and the alternative was one of $H_a: \mu < \mu_0$, $H_a: \mu > \mu_0$, or $H_a: \mu \neq \mu_0$. Since the paired t-test is a special case of the one-sample t-test, the hypotheses are the same, except that:

- Instead of simply μ, we use the notation $\mu_d$ to denote that the parameter of interest is the mean of the *differences*.
- In this course our null value is always 0 (although technically, it does not have to be).

Therefore, in the paired t-test, the null hypothesis is always

$$H_0: \mu_d = 0$$

and the alternative is one of $H_a: \mu_d < 0$ (one-sided), $H_a: \mu_d > 0$ (one-sided), or $H_a: \mu_d \neq 0$ (two-sided), depending on the context.

Let's go back to our example to see how this works and why it makes sense.

:::{admonition} Example: Drunk Drivers
:class: tip

Recall that in our "Are drivers impaired after drinking two beers?" example, our data were reduced to one sample of differences (one for each driver), so our problem was reduced to inference about the mean of the differences, $\mu_d$.

As we mentioned, the null hypothesis is $H_0: \mu_d = 0$. The null hypothesis claims that the differences in reaction times are centered at (or around) 0, indicating that drinking two beers has no real impact on reaction times. In other words, drivers are not impaired after drinking two beers.

In order to decide which of the alternatives is appropriate here, we have to think about the context of the problem. Recall that we want to check whether drivers are impaired after drinking two beers. Thus, we want to know whether their reaction times are *longer* after the two beers. Since the differences were calculated as (before − after), longer reaction times after the beers would translate into *negative* differences (e.g., 6.25 − 6.85, 2.96 − 4.78, etc.).

Therefore, the appropriate alternative here is $H_a: \mu_d < 0$, indicating that the differences are centered at a negative number.
:::

```{admonition} Comment
:class: important

Some students find it helpful to know that it turns out that $\mu_d = \mu_1 - \mu_2$. In other words, the difference between the means in the two-population representation is the same as the mean of the differences in the one-sample representation. Some students find it easier to first think about the hypotheses in terms of $\mu_1-\mu_2$ (as we did in the two-sample case) and then represent them in terms of $\mu_d$.

In our example, since we want to test whether the reaction times in population 1 (before) are shorter, we are testing $H_0: \mu_1-\mu_2=0$ vs. $H_a: \mu_1-\mu_2<0$, which in the matched pairs design notation is translated to $H_0: \mu_d=0$ vs. $H_a: \mu_d<0$.
```

:::{admonition} Example: Low-Carb Diet
:class: tip

Suppose the effectiveness of a low-carb diet is studied with a matched pairs design, recording each participant's weight before and after dieting. What would be the appropriate hypotheses in this case?

As before, $\mu_d$ is the mean of the differences (weight before diet) − (weight after diet). In this case, if the diet is effective and participants' weight after the diet was indeed lower, we would expect the differences to be *positive*, and therefore the appropriate hypotheses are $H_0: \mu_d=0$ vs. $H_a: \mu_d>0$.
:::

## Did I Get This?

In each of the following cases, decide based on the context what the appropriate set of hypotheses is. In every case, the differences are computed as (first measurement) − (second measurement).

:::{quiz} A study tests whether a memory-training program improves test scores, measuring each participant's score before the program (first) and after the program (second). Which hypotheses are appropriate?
:hint: If training helps, "after" scores are higher, so (before − after) would be negative.
:feedback-0: Correct! Improvement means higher "after" scores, so the differences (before − after) should be centered below 0.
:feedback-1: Positive differences would mean scores DROPPED after training.
:feedback-2: The study specifically tests for improvement, so a directional alternative is appropriate.
* *H₀: μ_d = 0; Hₐ: μ_d < 0
* H₀: μ_d = 0; Hₐ: μ_d > 0
* H₀: μ_d = 0; Hₐ: μ_d ≠ 0
:::

:::{quiz} A study examines whether a blood-pressure medication lowers systolic blood pressure, measuring each patient before treatment (first) and after treatment (second). Which hypotheses are appropriate?
:hint: If the drug works, "after" readings are lower, so (before − after) would be positive.
:feedback-0: Correct! Lower "after" readings make the (before − after) differences positive.
:feedback-1: Negative differences would mean blood pressure ROSE after treatment.
:feedback-2: The research question is directional (lowers), so a one-sided alternative is called for.
* *H₀: μ_d = 0; Hₐ: μ_d > 0
* H₀: μ_d = 0; Hₐ: μ_d < 0
* H₀: μ_d = 0; Hₐ: μ_d ≠ 0
:::

:::{quiz} A study asks whether husbands and wives differ in the number of hours they spend on household chores, with no prior expectation of direction. Each couple provides a pair of measurements (husband first, wife second). Which hypotheses are appropriate?
:hint: No direction is suspected.
:feedback-0: Correct! With no suspected direction, the two-sided alternative Hₐ: μ_d ≠ 0 is appropriate.
:feedback-1: One-sided alternatives require a prior directional expectation, which this study lacks.
* *H₀: μ_d = 0; Hₐ: μ_d ≠ 0
* H₀: μ_d = 0; Hₐ: μ_d > 0
:::
