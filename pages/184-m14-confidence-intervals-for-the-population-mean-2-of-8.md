# Building the 95% Confidence Interval for a Mean

## The General Case

Let's generalize the IQ example. Suppose that we are interested in estimating the unknown population mean $(\mu)$ based on a random sample of size n. Further, we assume that the population standard deviation $(\sigma)$ is known.

The values of $\bar{x}$ follow a normal distribution with (unknown) mean $\mu$ and standard deviation $\frac{\sigma}{\sqrt{n}}$ (known, since both $\sigma$ and n are known). By the (second part of the) Standard Deviation Rule, this means that:

There is a 95% chance that our sample mean ($\bar{x}$) will fall within $2\cdot\frac{\sigma}{\sqrt{n}}$ of $\mu$,

which means that:

We are 95% confident that $\mu$ falls within $2\cdot\frac{\sigma}{\sqrt{n}}$ of our sample mean ($\bar{x}$).

Or, in other words, a 95% confidence interval for the population mean $\mu$ is:

$$\left(\bar{x}-2\cdot\frac{\sigma}{\sqrt{n}},\ \bar{x}+2\cdot\frac{\sigma}{\sqrt{n}}\right)$$

Here, then, is the *general result:*

```{admonition} 95% Confidence Interval for $\mu (\sigma$ known)
:class: note

Suppose a random sample of size n is taken from a normal population of values for a quantitative variable whose mean $(\mu)$ is unknown, when the standard deviation $(\sigma)$ is given. A 95% confidence interval (CI) for $\mu$ is:

$$\bar{x}\pm2\cdot\frac{\sigma}{\sqrt{n}}$$
```

```{admonition} Comment
:class: important

Note that for now we require the population standard deviation $(\sigma)$ to be known. Practically, $\sigma$ is rarely known, but for some cases, especially when a lot of research has been done on the quantitative variable whose mean we are estimating (such as IQ, height, weight, scores on standardized tests), it is reasonable to assume that $\sigma$ is known. Eventually, we will see how to proceed when $\sigma$ is unknown, and must be estimated with the sample standard deviation (s).
```

Let's look at another example.

:::{admonition} Example: SAT-M Scores
:class: tip

An educational researcher was interested in estimating $\mu$, the mean score on the math part of the SAT (SAT-M) of all community college students in his state. To this end, the researcher chose a random sample of 650 community college students from his state, and found that their average SAT-M score is 475. Based on a large body of research that was done on the SAT, it is known that the scores roughly follow a normal distribution with standard deviation $\sigma=100$.

Based on this information, let's estimate $\mu$ with a 95% confidence interval.

Using the formula we developed before, a 95% confidence interval for $\mu$ is:

$$475\pm2\cdot\frac{100}{\sqrt{650}} = 475 \pm 7.8 = (467.2,\ 482.8)$$

In this case, it makes sense to round, since SAT scores can be only whole numbers, and say that the 95% confidence interval is (467, 483).

We are not done yet. An equally important part is to *interpret what this means in the context of the problem.*

We are 95% confident that the mean SAT-M score of all community college students in the researcher's state is covered by the interval (467, 483). Note that the confidence interval was obtained by taking $475\pm8$ (rounded). This means that we are 95% confident that by using the sample mean ($\bar{x}=475$) to estimate $\mu$, our error is no more than 8 points.
:::

## Check Your Understanding: Constructing a Confidence Interval for a Mean

A study was done on pregnant women who smoked during their pregnancies. In particular, the researchers wanted to study the effect that smoking has on pregnancy length. A sample of 114 pregnant women who were smokers participated in the study and were followed until the birth of their child. At the end of the study, the collected data were analyzed and it was found that the average pregnancy length of the 114 women was 260 days. From a large body of research, it is known that length of human pregnancy has a standard deviation of 16 days.

:::{quiz} Find a 95% confidence interval for $\mu$, the mean pregnancy length of women who smoke during pregnancy.
:hint: $260 \pm 2(16/\sqrt{114})$; note $16/\sqrt{114} \approx 1.5$.
:feedback-0: Correct! $260 \pm 2(1.5) = 260 \pm 3 = (257$, 263).
:feedback-1: (244, 276) uses $\pm 16$, the population standard deviation—you must divide by $\sqrt{n}$ first.
:feedback-2: (258.5, 261.5) uses only 1 standard deviation of the sample mean; the 95% interval uses 2.
* *(257, 263)
* (244, 276)
* (258.5, 261.5)
:::

:::{quiz} It is known that the mean pregnancy length among all women (smokers and non-smokers) is 266 days. Based on your interval (257, 263), what can the researchers conclude?
:hint: Is 266 inside the interval of plausible values?
:feedback-0: Correct! 266 lies above the entire interval, so it is not a plausible value for the mean among smokers—the data provide evidence that smoking is associated with shorter pregnancies.
:feedback-1: 266 falls OUTSIDE (257, 263), so it is not plausible for this population.
:feedback-2: The interval is about the mean pregnancy length of smokers; comparing it with 266 is precisely how it's used.
* *Since 266 is outside the interval, the mean pregnancy length of smokers appears to be shorter than 266 days
* Since 266 is inside the interval, there is no evidence of a difference
* The interval cannot be used to address this question
:::

You just gained practice computing and interpreting a confidence interval for a population mean. Note that the way a confidence interval is used is that we hope the interval contains the population mean $\mu$. This is why we call it an "interval *for the population mean*."

We just saw that one interpretation of a 95% confidence interval is that we are 95% confident that the population mean $(\mu)$ is contained in the interval. Another useful interpretation in practice is that, given the data, the confidence interval represents the set of plausible values for the population mean $\mu$.

:::{admonition} Example: Using the Interval
:class: tip

As an illustration, let's return to the example of mean SAT-Math score of community college students. Recall that we had constructed the confidence interval (467, 483) for the unknown mean SAT-M score for all community college students.

Here is a way that we can use the confidence interval:

Do the results of this study provide evidence that $\mu$, the mean SAT-M score of community college students, is lower than the mean SAT-M score in the general population of college students in that state (which is 480)?

The 95% confidence interval for $\mu$ was found to be (467, 483). Note that 480, the mean SAT-M score in the general population of college students in that state, falls inside the interval, which means that it is one of the plausible values for $\mu$.

This means that $\mu$ could be 480 (or even higher, up to 483), and therefore we cannot conclude that the mean SAT-M score among community college students in the state is lower than the mean in the general population of college students in that state. (Note that the fact that most of the plausible values for $\mu$ fall below 480 is not a consideration here.)
:::

```{admonition} Comment
:class: important

Recall that in the formula for the 95% confidence interval for $\mu$, $\bar{x}\pm2\cdot\frac{\sigma}{\sqrt{n}}$, the 2 comes from the Standard Deviation Rule, which says that any normal random variable (in our case $\bar{X}$) has a 95% chance (or probability of 0.95) of taking a value that is within 2 standard deviations of its mean.

As you recall from the discussion about the normal random variable, this is only an approximation, and to be more accurate, there is a 95% chance that a normal random variable will take a value within 1.96 standard deviations of its mean. Therefore, a more accurate formula for the 95% confidence interval for $\mu$ is $\bar{x}\pm1.96\cdot\frac{\sigma}{\sqrt{n}}$, which you'll find in most introductory statistics books. In this course, we'll use 2 (and not 1.96), which is close enough for our purposes.
```
