# The 68-95-99.7 Rule for Normal Variables

## The Standard Deviation Rule for Normal Random Variables

We began to get a feel for normal distributions in the Exploratory Data Analysis (EDA) section, when we introduced the Standard Deviation Rule (or the *68-95-99.7* rule) for how values in a normally-shaped *sample data set* behave relative to their mean ($\bar{x}$) and standard deviation (s). This is the same rule that dictates how the distribution of a normal {term}`random variable` behaves relative to its mean $\mu$ and standard deviation $\sigma$. Now we use probability language and notation to describe the random variable's behavior. For example, in the EDA section, we would have said "68% of pregnancies in our data set fall within 1 standard deviation (s) of their mean ($\bar{x}$)." The analogous statement now would be "If X, the length of a randomly chosen pregnancy, is normal with mean ($\mu$) and standard deviation ($\sigma$), then $0.68=P(\mu-\sigma<X<\mu+\sigma)$."

In general, if X is a normal random variable, then the probability is:

- 68% that X falls within 1 $\sigma$ of $\mu$, that is, in the interval $\mu\pm\sigma$
- 95% that X falls within 2 $\sigma$ of $\mu$, that is, in the interval $\mu\pm2\sigma$
- 99.7% that X falls within 3 $\sigma$ of $\mu$, that is, in the interval $\mu\pm3\sigma$

Using probability notation, we may write

$$0.68=P(\mu-\sigma<X<\mu+\sigma)$$

$$0.95=P(\mu-2\sigma<X<\mu+2\sigma)$$

$$0.997=P(\mu-3\sigma<X<\mu+3\sigma)$$

```{figure} images/gen/m04-sd-rule.svg
:alt: A normal curve with the axis marked at 1, 2, and 3 standard deviations on either side of the mean, and brackets showing the 68 percent, 95 percent, and 99.7 percent regions.
```

::::{admonition} Comment
:class: important

Notice that the information from the rule can be interpreted from the perspective of the tails of the normal curve: since 0.68 is the probability of being within 1 standard deviation of the mean, $(1 - 0.68)/2 = 0.16$ is the probability of being further than 1 standard deviation below the mean (or further than 1 standard deviation above the mean). Likewise, $(1 - 0.95)/2 = 0.025$ is the probability of being more than 2 standard deviations below (or above) the mean; $(1 - 0.997)/2 = 0.0015$ is the probability of being more than 3 standard deviations below (or above) the mean. The figure below illustrates this:

```{figure} images/gen/m11-normal-tails.svg
:alt: A normal curve in which the middle region within one standard deviation of the mean holds probability 0.68, and each shaded tail beyond one standard deviation holds probability 0.16. The caption notes that 0.025 lies beyond two standard deviations on each side, and 0.0015 beyond three.
```
::::

::::{admonition} Example: Foot Length
:class: tip

Suppose that foot length of a randomly chosen adult male is a normal random variable with mean $\mu=11$ and standard deviation $\sigma=1.5$. Then the Standard Deviation Rule lets us sketch the probability distribution of X as follows:

```{figure} images/gen/m11-sd-rule-foot.svg
:alt: A normal curve for foot length with the axis marked at 6.5, 8, 9.5, 11, 12.5, 14, and 15.5 inches. Brackets show that 68% of foot lengths fall between 9.5 and 12.5 inches, 95% between 8 and 14 inches, and 99.7% between 6.5 and 15.5 inches.
```

*(a)* What is the probability that a randomly chosen adult male will have a foot length between 8 and 14 inches? 0.95, or 95%.

*(b)* An adult male is almost guaranteed (0.997 probability) to have a foot length between what two values? 6.5 and 15.5 inches.

*(c)* The probability is only 2.5% that an adult male will have a foot length greater than how many inches? 14. (Since 95% of foot lengths fall between 8 and 14, the remaining 5% is split evenly between the two tails.)
::::

Now you should try a few. (Use the figure in the example to help you.)

:::{quiz} (d) What is the probability that a randomly chosen adult male will have a foot length between 9.5 and 12.5 inches?
:hint: 9.5 and 12.5 are each 1 standard deviation from the mean of 11.
:feedback-0: Correct! This is the within-$1\sigma$ interval, so the probability is 0.68.
:feedback-1: 0.95 corresponds to within 2 standard deviations (8 to 14 inches).
:feedback-2: 0.16 is the probability in ONE tail beyond 1 standard deviation.
* *0.68
* 0.95
* 0.16
:::

:::{quiz} (e) What is the probability that a randomly chosen adult male will have a foot length of less than 8 inches?
:hint: 8 is 2 standard deviations below the mean.
:feedback-0: Correct! $(1 - 0.95)/2 = 0.025$.
:feedback-1: 0.05 is the total probability in both tails beyond 2 standard deviations; the question asks about only the lower tail.
:feedback-2: 0.16 is the probability of being more than 1 (not 2) standard deviation below the mean.
* *0.025
* 0.05
* 0.16
:::

:::{quiz} (f) The probability is 16% that an adult male will have a foot length greater than how many inches?
:hint: 16% is the upper tail beyond 1 standard deviation above the mean.
:feedback-0: Correct! 0.16 is the probability of exceeding $\mu + \sigma = 11 + 1.5 = 12.5$ inches.
:feedback-1: 14 corresponds to the upper 2.5% tail, not 16%.
:feedback-2: 11 is the mean; 50% of foot lengths exceed it.
* *12.5
* 14
* 11
:::

```{admonition} Comment
:class: important

Notice that there are two types of problems we may want to solve: those like *(a)*, *(d)* and *(e)*, in which a particular interval of values of a normal random variable is given, and we are asked to find a probability, and those like *(b)*, *(c)* and *(f)*, in which a probability is given and we are asked to identify what the normal random variable's values would be.
```
