# The Sample Proportion: Center, Spread, and Shape

```{admonition} Learning Objectives
:class: note

- Apply the sampling distribution of the sample proportion (when appropriate). In particular, be able to identify unusual samples from a given population.
```

The first step to drawing conclusions about parameters based on the accompanying statistics is to understand how sample statistics behave relative to the parameter that summarizes the entire population. We begin with the behavior of sample proportion relative to population proportion (when the variable of interest is categorical). After that, we will explore the behavior of sample mean relative to population mean (when the variable of interest is quantitative).

## Behavior of Sample Proportion (p-hat)

:::{admonition} Example: Part-Time College Students
:class: tip

Approximately 60% of all part-time college students in the United States are female. (In other words, the population proportion of females among part-time college students is p = 0.6.) What would you expect to see in terms of the behavior of the sample proportion of females ($\hat{p}$) if random samples of size 100 were taken from the population of all part-time college students?

As we saw before, due to sampling variability, sample proportion in random samples of size 100 will take numerical values which vary according to the laws of chance: in other words, sample proportion is a *random variable*. To summarize the behavior of any random variable, we focus on three features of its distribution: the center, the spread, and the shape.

Based only on our intuition, we would expect the following:

*Center*: Some sample proportions will be on the low side—say, 0.55 or 0.58—while others will be on the high side—say, 0.61 or 0.66. It is reasonable to expect all the sample proportions in repeated random samples to average out to the underlying population proportion, 0.6. In other words, the mean of the distribution of $\hat{p}$ should be p.

*Spread*: For samples of 100, we would expect sample proportions of females not to stray too far from the population proportion 0.6. Sample proportions lower than 0.5 or higher than 0.7 would be rather surprising. On the other hand, if we were only taking samples of size 10, we would not be at all surprised by a sample proportion of females even as low as 4/10 = 0.4, or as high as 8/10 = 0.8. Thus, sample size plays a role in the spread of the distribution of sample proportion: there should be less spread for larger samples, more spread for smaller samples.

*Shape*: Sample proportions closest to 0.6 would be most common, and sample proportions far from 0.6 in either direction would be progressively less likely. In other words, the shape of the distribution of sample proportion should bulge in the middle and taper at the ends: it should be somewhat *normal.*
:::

## Comment

The *distribution* of the values of the sample proportions ($\hat{p}$) in repeated *samples* is called the *sampling distribution of* $\hat{p}$.

The following video uses simulation to check whether our intuition about the center, spread and shape of the sampling distribution of $\hat{p}$ was right:

```{note} Video

[Behavior of Sample Proportion 1](https://www.youtube.com/watch?v=2bIC4EmejkQ)
```

## Concept Check

:::{quiz} Suppose p = 0.6 and we repeatedly take random samples of size 100, recording the sample proportion each time. Around what value will the sample proportions center?
:hint: The mean of the sampling distribution of p-hat is p.
:feedback-0: Correct! The sample proportions average out to the population proportion, 0.6.
:feedback-1: 0.5 has no special role here; the center follows the population proportion.
:feedback-2: The sample proportions cluster around a predictable center: the parameter p.
* *0.6
* 0.5
* There is no predictable center
:::

:::{quiz} Two students each draw many random samples: one uses samples of size 25, the other of size 2,500. How will their sampling distributions of p-hat differ?
:hint: Larger samples approximate the population better.
:feedback-0: Correct! Both are centered at p, but the larger samples produce sample proportions that cluster much more tightly around p—less spread.
:feedback-1: The centers are the same (p); it's the spread that differs.
:feedback-2: Larger samples give LESS variability, not more.
* *Both center at p, but the size-2,500 samples have much less spread
* The size-2,500 samples center closer to p, with the same spread
* The size-2,500 samples have more spread
:::

At this point, we have a good sense of what happens as we take random samples from a population. Our simulation suggests that our initial intuition about the shape and center of the sampling distribution is correct. If the population has a proportion of p, then random samples of the same size drawn from the population will have sample proportions close to p. More specifically, the distribution of sample proportions will have a mean of p. We also observed that for this situation, the sample proportions are approximately normal. We will see later that this is not always the case. But if sample proportions are normally distributed, then the distribution is centered at p. Now we want to think more about the variability we expect to see in the sample proportions. Our intuition tells us that larger samples will better approximate the population, so we might expect less variability in large samples. The next video uses simulations to investigate this idea. After that, we will tie these ideas to more formal theory.

```{note} Video

[Behavior of Sample Proportion 2](https://www.youtube.com/watch?v=tUvXeJ3A3_s)
```
