# Step 2: Collecting and Summarizing the Data

## Step 2: Collecting and Summarizing the Data (Using a Test Statistic)

After the hypotheses have been stated, the next step is to obtain a *sample* (on which the inference will be based), *collect relevant data*, and *summarize* them.

It is extremely important that our sample is representative of the population about which we want to draw conclusions. This is ensured when the sample is chosen at *random*. Beyond the practical issue of ensuring representativeness, choosing a random sample has theoretical importance that we will mention later.

In the case of hypothesis testing for the population proportion (p), we will collect data on the relevant categorical variable from the individuals in the sample and start by calculating the sample proportion, $\hat{p}$ (the natural quantity to calculate when the parameter of interest is p).

Let's go back to our three examples and add this step to our figures.

::::{admonition} Example 1: Defective Products
:class: tip

```{figure} images/gen/m15-prop-machine-phat.svg
:alt: The population of products produced by the machine after the repair, with question "is p still 0.20 or has it been reduced?" A random sample of 400 products contains 64 defective, so p-hat = $64/400 = 0.16$.
```
::::

::::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

```{figure} images/gen/m15-prop-marijuana-phat.svg
:alt: The population of students at the college, with question "is p 0.157 like the national figure, or higher?" A random sample of 100 students contains 19 marijuana users, so p-hat = $19/100 = 0.19$.
```
::::

::::{admonition} Example 3: Death Penalty Support
:class: tip

```{figure} images/gen/m15-prop-deathpenalty-phat.svg
:alt: The population of U.S. adults, with question "has p changed since 2003, when it was 0.64?" A random sample of 1,000 adults contains 675 in favor, so p-hat = $675/1000 = 0.675$.
```
::::

As we mentioned earlier without going into details, when we summarize the data in hypothesis testing, we go a step beyond calculating the sample statistic and summarize the data with a {term}`test statistic`. Every test has a test statistic, which to some degree captures the essence of the test. In fact, the p-value, which so far we have looked upon as "the king" (in the sense that everything is determined by it), is actually determined by (or derived from) the test statistic. We will now gradually introduce the test statistic.

The test statistic is *a measure* of how far the sample proportion $\hat{p}$ is from the null value $p_0$, the value that the null hypothesis claims is the value of p. In other words, since $\hat{p}$ is what the data estimate p to be, the test statistic can be viewed as a measure of the "distance" between what the data tell us about p and what the null hypothesis claims p to be.

Let's use our examples to understand this:

:::{admonition} Example 1: Defective Products
:class: tip

The parameter of interest is p, the proportion of defective products following the repair.

The data estimate p to be $\hat{p}=0.16$. The null hypothesis claims that $p = 0.20$. The data are therefore 0.04 (or 4 percentage points) below the null hypothesis with respect to what they each tell us about p.

It is hard to evaluate whether this difference of 4 percentage points in defective products is enough evidence to say that the repair was effective, but clearly, the larger the difference, the more evidence it is against the null hypothesis. So if, for example, our sample proportion of defective products had been, say, 0.10 instead of 0.16, then I think you would all agree that cutting the proportion of defective products in half (from 20% to 10%) would be extremely strong evidence that the repair was effective.
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

The parameter of interest is p, the proportion of students in a college who use marijuana.

The data estimate p to be $\hat{p}=0.19$. The null hypothesis claims that $p = 0.157$. The data are therefore 0.033 (or 3.3 percentage points) above the null hypothesis with respect to what they each tell us about p.
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

The parameter of interest is p, the proportion of U.S. adults who support the death penalty for convicted murderers.

The data estimate p to be $\hat{p}=0.675$. The null hypothesis claims that $p = 0.64$. There is a difference of 0.035 (3.5 percentage points) between the data and the null hypothesis with respect to what they each tell us about p.
:::

There is a problem with just looking at the difference between the sample proportion $\hat{p}$ and the null value $p_0$. Examples 2 and 3 illustrate this problem very well.

In example 2 we have a difference of 3.3 percentage points between the data and the null hypothesis, which is approximately the same as the difference in example 3 of 3.5 percentage points. However, the difference in example 3 of 3.5 percentage points is based on a *sample of size 1,000*, and therefore it is much *more impressive* than the difference of 3.3 percentage points in example 2, which was obtained from a sample of size of only 100.

## Check Your Understanding: Why We Standardize the Test Statistic

:::{quiz} Two studies each find a sample proportion 4 percentage points above the null value. Study A used $n = 50$; study B used $n = 2{,}000$. Which study provides stronger evidence against the null hypothesis?
:hint: How much do sample proportions vary from sample to sample when n is small versus large?
:feedback-0: Correct! With $n = 2{,}000$, sample proportions vary little, so a 4-point gap is very surprising under $H_0$. With $n = 50$, such a gap could easily occur by chance.
:feedback-1: With only 50 observations, a 4-point difference could easily arise by random chance—it is weaker evidence.
:feedback-2: The sample size matters a great deal: the same difference is far more surprising when it comes from a large sample.
* *Study B—the same difference from a larger sample is more surprising under the null hypothesis
* Study A—smaller samples give stronger evidence
* Both provide equally strong evidence, since the differences are equal
:::

:::{quiz} Why can't the difference p-hat - $p_0$ serve as the test statistic by itself?
:hint: Think about what the previous question demonstrated.
:feedback-0: Correct! The same raw difference means different things depending on sample-to-sample variability, so we must standardize it—accounting for the sample size—before we can judge how surprising it is.
:feedback-1: The difference can be computed in every study; the problem is interpreting it without a scale.
:feedback-2: The sign of the difference is informative (it shows direction); the issue is that the raw size has no universal scale.
* *Because the same difference is more or less surprising depending on the sample size—it must be standardized
* Because the difference cannot be calculated from sample data
* Because the difference can be negative
:::
