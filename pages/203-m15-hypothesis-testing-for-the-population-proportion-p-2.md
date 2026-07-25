# Step 1: Stating the Hypotheses for a Proportion

Recall that there are basically 4 steps in the process of hypothesis testing:

1. State the null and alternative hypotheses.
2. Collect relevant data from a random sample and summarize them (using a test statistic).
3. Find the p-value, the probability of observing data like those observed assuming that $H_0$ is true.
4. Based on the p-value, decide whether we have enough evidence to reject $H_0$ (and accept $H_a$), and draw our conclusions in context.

We are now going to go through these steps as they apply to hypothesis testing for the population proportion p. It should be noted that even though the details will be specific to this particular test, some of the ideas that we will add apply to hypothesis testing in general.

## Step 1: Stating the Hypotheses

Here again are the three sets of hypotheses that are being tested in each of our three examples:

:::{admonition} Example 1: Defective Products
:class: tip

Has the proportion of defective products been reduced as a result of the repair?

- $H_0$: $p = 0.20$ (no change; the repair did not help)
- $H_a$: $p < 0.20$ (the repair was effective)
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

Is the proportion of marijuana users in the college higher than the national figure?

- $H_0$: $p = 0.157$ (same as among all college students in the country)
- $H_a$: $p > 0.157$ (higher than the national figure)
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

Did the proportion of U.S. adults who support the death penalty change between 2003 and a later poll?

- $H_0$: $p = 0.64$ (no change from 2003)
- $H_a$: $p \neq 0.64$ (some change since 2003)
:::

Note that the null hypothesis always takes the form

$$H_0: p = \text{some value}$$

and the alternative hypothesis takes one of the following three forms: $H_a: p <$ that value (as in example 1), $H_a: p >$ that value (as in example 2), or $H_a: p \neq$ that value (as in example 3).

Note that it was quite clear from the context which form of the alternative hypothesis would be appropriate. The value that is specified in the null hypothesis is called the *null value*, and is generally denoted by $p_0$. We can say, therefore, that in general the null hypothesis about the population proportion (p) takes the form:

$$H_0: p = p_0$$

We write $H_0: p = p_0$ to say that we are making the hypothesis that the population proportion has the value of $p_0$. In other words, p is the unknown population proportion and $p_0$ is the number we think p might be for the given situation.

The alternative hypothesis takes one of the following three forms (depending on the context):

- $H_a: p < p_0$ (*one-sided*)
- $H_a: p > p_0$ (*one-sided*)
- $H_a: p \neq p_0$ (*two-sided*)

The first two possible forms of the alternative (where the = sign in $H_0$ is challenged by < or >) are called *one-sided alternatives*, and the third form (where the = sign in $H_0$ is challenged by $\neq )$ is called a *two-sided alternative*. To understand the intuition behind these names, let's go back to our examples.

Example 3 (death penalty) is a case where we have a two-sided alternative:

- $H_0$: $p = 0.64$ (no change from 2003)
- $H_a$: $p \neq 0.64$ (some change since 2003)

In this case, in order to reject $H_0$ and accept $H_a$ we will need to get a sample proportion of death penalty supporters which is very different from 0.64 *in either direction*—either much larger or much smaller than 0.64.

In example 2 (marijuana use) we have a one-sided alternative:

- $H_0$: $p = 0.157$ (same as among all college students in the country)
- $H_a$: $p > 0.157$ (higher than the national figure)

Here, in order to reject $H_0$ and accept $H_a$ we will need to get a sample proportion of marijuana users which is much *higher* than 0.157.

Similarly, in example 1 (defective products), where we are testing

- $H_0$: $p = 0.20$ (no change; the repair did not help)
- $H_a$: $p < 0.20$ (the repair was effective)

in order to reject $H_0$ and accept $H_a$, we will need to get a sample proportion of defective products which is much *smaller* than 0.20.

## Check Your Understanding: Stating Hypotheses

In each of the following examples, a test for the population proportion (p) is called for. You are asked to select the right null and alternative hypotheses.

*Scenario 1:* The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. Has that figure changed since? To test this, a random sample of 100 Internet users was chosen, and when interviewed, 10 said that they were extremely worried about credit card fraud when buying online. Let p be the proportion of all Internet users who are concerned about credit card fraud.

:::{quiz} Which hypotheses are appropriate for scenario 1?
:hint: The question is whether the figure "has changed"—no direction is specified.
:feedback-0: Correct! "Has that figure changed?" calls for a two-sided alternative: $H_0$: $p = 0.087$, $H_a$: $p \neq 0.087$.
:feedback-1: No direction was suspected, so a one-sided "greater than" alternative is not appropriate.
:feedback-2: The null value should be the reported baseline 0.087, not the sample result 0.10.
* *$H_0$: $p = 0.087$; $H_a$: $p \neq 0.087$
* $H_0$: $p = 0.087$; $H_a$: $p > 0.087$
* $H_0$: $p = 0.10$; $H_a$: $p \neq 0.10$
:::

*Scenario 2:* The UCLA Internet Report (February 2003) estimated that a proportion of roughly 0.75 of online homes were still using dial-up access, but claimed that the use of dial-up was declining. Is that really the case? To examine this, a follow-up study was conducted a year later in which, out of a random sample of 1,308 households that had Internet access, 804 were connecting using a dial-up modem. Let p be the proportion of all U.S. Internet-using households that have dial-up access.

:::{quiz} Which hypotheses are appropriate for scenario 2?
:hint: The claim being examined is that dial-up use is DECLINING.
:feedback-0: Correct! The claim of decline calls for a one-sided alternative: $H_0$: $p = 0.75$, $H_a$: $p < 0.75$.
:feedback-1: The report specifically claims a decline, so the alternative should be one-sided (less than).
:feedback-2: The null value is the earlier baseline 0.75, not the follow-up sample proportion $804/1308 \approx 0.615$.
* *$H_0$: $p = 0.75$; $H_a$: $p < 0.75$
* $H_0$: $p = 0.75$; $H_a$: $p \neq 0.75$
* $H_0$: $p = 0.615$; $H_a$: $p < 0.615$
:::

*Scenario 3:* According to the UCLA Internet Report (February 2003), the use of the Internet at home was growing steadily, and it was estimated that roughly 59.3% of households in the United States had Internet access at home. Has that trend continued since the report was released? To study this, a random sample of 1,200 households was chosen for a more recent study, and it was found that 972 had an Internet connection. Let p be the proportion of U.S. households that have Internet access.

:::{quiz} Which hypotheses are appropriate for scenario 3?
:hint: The report describes a GROWING trend—has it continued?
:feedback-0: Correct! Checking whether the growing trend continued calls for $H_0$: $p = 0.593$, $H_a$: $p > 0.593$.
:feedback-1: The context (a growing trend) suggests a one-sided "greater than" alternative.
:feedback-2: The null value is the reported baseline 0.593, not the sample proportion $972/1200 = 0.81$.
* *$H_0$: $p = 0.593$; $H_a$: $p > 0.593$
* $H_0$: $p = 0.593$; $H_a$: $p \neq 0.593$
* $H_0$: $p = 0.81$; $H_a$: $p > 0.81$
:::

## Check Your Understanding: Stating Hypotheses in Context

In each of the following examples, a test for the population proportion (p) is called for. You are asked to select the right null and alternative hypotheses.

*Scenario 1:* When shirts are made, there can occasionally be defects (such as improper stitching). But too many defective shirts can be a sign of substandard manufacturing. Suppose, in the past, your favorite department store has had only one defective shirt per 200 shirts (a prior defective rate of only 0.005). But you suspect that the store has recently switched to a substandard manufacturer, so you decide to test whether their overall proportion of defective shirts today is higher. Suppose that, in a random sample of 200 shirts from the store, you find that 27 of them are defective, for a sample proportion of 0.135.

:::{quiz} Which hypotheses are appropriate for the defective shirts scenario?
:hint: The prior rate is 0.005, and you suspect the rate is now HIGHER.
:feedback-0: Correct! $H_0$: $p = 0.005$ (the prior rate); $H_a$: $p > 0.005$ (substandard manufacturing).
:feedback-1: The suspicion is specifically that the rate is higher, so a one-sided alternative is appropriate.
:feedback-2: The null value is the historical rate 0.005, not the sample result 0.135.
* *$H_0$: $p = 0.005$; $H_a$: $p > 0.005$
* $H_0$: $p = 0.005$; $H_a$: $p \neq 0.005$
* $H_0$: $p = 0.135$; $H_a$: $p > 0.135$
:::

*Scenario 2:* It is a known medical fact that slightly fewer females than males are born; the known baseline female birthrate is about 49% females. In some cultures, male children are traditionally looked on more favorably than female children, and there is concern that the increasing availability of ultrasound may lead to sex-selective abortion. If this is happening, then the proportion of females born would be significantly lower than the baseline rate. To test whether the proportion of females born in India is lower than the baseline female birthrate, a study investigates a random sample of 6,500 births from hospital files in India, and finds 44.8% females born among the sample.

:::{quiz} Which hypotheses are appropriate for the birthrate scenario?
:hint: The baseline is 0.49, and the concern is a LOWER proportion of female births.
:feedback-0: Correct! $H_0$: $p = 0.49$ (the baseline rate); $H_a$: $p < 0.49$ (lower, as the concern suggests).
:feedback-1: The study specifically tests for a LOWER rate, so the alternative should be one-sided (less than).
:feedback-2: The null value is the baseline 0.49, not the sample result 0.448.
* *$H_0$: $p = 0.49$; $H_a$: $p < 0.49$
* $H_0$: $p = 0.49$; $H_a$: $p \neq 0.49$
* $H_0$: $p = 0.448$; $H_a$: $p < 0.448$
:::

*Scenario 3:* A properly balanced 6-sided game die should give a 1 in exactly 1/6 (16.7%) of all rolls. A casino wants to test its game die. If the die is not properly balanced one way or another, it could give either too many 1's or too few 1's, either of which could be bad. The casino wants to use the proportion of 1's to test whether the die is out of balance, so it test-rolls the die 60 times and gets a 1 in 9 of the rolls (15%).

:::{quiz} Which hypotheses are appropriate for the game die scenario?
:hint: Too many 1's OR too few 1's would both be bad—no direction is specified.
:feedback-0: Correct! Since an imbalance in either direction matters, the alternative is two-sided: $H_0$: $p = 1/6$, $H_a$: $p \neq 1/6$.
:feedback-1: The casino cares about imbalance in EITHER direction, so a one-sided alternative is not appropriate.
:feedback-2: The null value is the fair-die probability $1/6 \approx 0.167$, not the sample result 0.15.
* *$H_0$: $p = 1/6$; $H_a$: $p \neq 1/6$
* $H_0$: $p = 1/6$; $H_a$: $p < 1/6$
* $H_0$: $p = 0.15$; $H_a$: $p \neq 0.15$
:::
