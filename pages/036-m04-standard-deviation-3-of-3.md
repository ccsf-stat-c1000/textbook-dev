# Putting the Standard Deviation Rule to Work

```{admonition} Learning Objectives
:class: note

- Apply the standard deviation rule to the special case of distributions having the "normal" shape.
```

The following example illustrates how we can apply the Standard Deviation Rule to variables whose distribution is known to be approximately normal.

::::{admonition} Example: Length of Human Pregnancy
:class: tip

The length of the human pregnancy is not fixed. It is known that it varies according to a distribution which is roughly normal, with a mean of 266 days, and a standard deviation of 16 days. (Source: Figures are from Moore and McCabe, *Introduction to the Practice of Statistics*.)

First, let's apply the Standard Deviation Rule to this case by drawing a picture:

```{figure} images/gen/m04-sd-rule-pregnancy.svg
:alt: A normal curve for pregnancy length with the axis marked at 218, 234, 250, 266, 282, 298, and 314 days. Brackets show that about 68% of pregnancies last between 250 and 282 days, about 95% between 234 and 298 days, and about 99.7% between 218 and 314 days.
```
::::

We can now use the information provided by the Standard Deviation Rule about the distribution of the length of human pregnancy, to answer some questions. For example:

:::{admonition} Question & Answer
:class: important

**Question:** How long do the middle 95% of human pregnancies last?

**Answer:** The middle 95% of pregnancies last within 2 standard deviations of the mean, or in this case 234–298 days.

**Question:** What percent of pregnancies last more than 298 days?

**Answer:** Since 95% of the pregnancies last between 234 and 298 days, the remaining 5% of pregnancies last either less than 234 days or more than 298 days. Since the normal distribution is symmetric, these 5% of pregnancies are divided evenly between the two tails, and therefore 2.5% of pregnancies last more than 298 days.

**Question:** How short are the shortest 2.5% of pregnancies?

**Answer:** Using the same reasoning as in the previous question, the shortest 2.5% of human pregnancies last less than 234 days.

**Question:** What percentage of human pregnancies last more than 266 days?

**Answer:** Since 266 days is the mean, approximately 50% of pregnancies last more than 266 days.
:::

In general, the larger the animal, the longer the length of pregnancy (also called *gestation period*). For the horse, for example, the gestation period varies roughly according to a normal distribution with a mean of 336 days and a standard deviation of 3 days (Source: These figures are from Moore and McCabe, *Introduction to the Practice of Statistics*).

Use the Standard Deviation Rule to answer the following questions. This picture of the SD rule applied to this distribution will help:

```{figure} images/gen/m04-sd-rule-horse.svg
:alt: A normal curve for horse gestation with the axis marked at 327, 330, 333, 336, 339, 342, and 345 days. Brackets show that about 68% of gestations last between 333 and 339 days, about 95% between 330 and 342 days, and about 99.7% between 327 and 345 days.
```

## Check Your Understanding: Applying the 68-95-99.7 Rule

:::{quiz} Approximately what percentage of horse pregnancies last between 333 and 339 days?
:hint: 333 and 339 are each 1 SD (3 days) from the mean of 336.
:feedback-0: Correct! 333 to 339 days is within 1 SD of the mean, which covers about 68% of horse pregnancies.
:feedback-1: 95% corresponds to within 2 SDs, i.e., 330 to 342 days.
:feedback-2: 50% is the percentage on one side of the mean, not within 1 SD of it.
* *About 68%
* About 95%
* About 50%
:::

:::{quiz} Approximately what percentage of horse pregnancies last less than 330 days?
:hint: 330 is 2 SDs below the mean. Think about what's left outside the middle 95%, and how it splits between the two tails.
:feedback-0: Correct! About 5% fall outside 330 to 342 days, and half of them, about 2.5%, are below 330.
:feedback-1: 5% is the total in both tails combined; the question asks only about the lower tail.
:feedback-2: 16% would be the answer for less than 333 days (1 SD below the mean), not 330 days.
* *About 2.5%
* About 5%
* About 16%
:::

:::{quiz} A foal is born after 345 days of gestation. How would you describe this pregnancy?
:hint: How many standard deviations above the mean is 345?
:feedback-0: Correct! 345 days is 3 SDs above the mean—only about 0.15% of pregnancies last longer, so this is extremely unusual.
:feedback-1: 345 is not within the middle 68% (333 to 339 days); it is far out in the upper tail.
:feedback-2: Longer than average, yes—but 3 SDs above the mean is not just "slightly" longer; it is extremely unusual.
* *Extremely unusual—about 3 standard deviations above the mean
* Fairly typical—within the middle 68% of pregnancies
* Slightly longer than average, but not unusual
:::

## Let's Summarize

- The standard deviation measures the spread by reporting a typical (average) distance between the data points and their average.
- It is appropriate to use the SD as a measure of spread with the mean as the measure of center.
- Since the mean and standard deviations are highly influenced by extreme observations, they should be used as numerical descriptions of the center and spread only for distributions that are roughly symmetric, and have no outliers.
- For symmetric mound-shaped distributions, the Standard Deviation Rule tells us what percentage of the observations falls within 1, 2, and 3 standard deviations of the mean, and thus provides another way to interpret the standard deviation's value for distributions of this type.
