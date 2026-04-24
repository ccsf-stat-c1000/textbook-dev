# Confidence Intervals for the Population Mean (6 of 8)

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
    - Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## Sample Size Calculations

As we just learned, for a given level of confidence, the sample size determines the size of the margin of error and thus the width, or precision, of our interval estimation. This process can be reversed.

In situations where a researcher has some flexibility as to the sample size, the researcher can calculate in advance what the sample size is that he/she needs in order to be able to report a confidence interval with a certain level of confidence and a certain margin of error. Let's look at an example.

```{admonition} Example
    Recall the example about the SAT-M scores of community college students.

    An educational researcher is interested in estimating μ, the mean score on the math part of the SAT (SAT-M) of all community college students in his state. To this end, the researcher has chosen a random sample of 650 community college students from his state, and found that their average SAT-M score is 475. Based on a large body of research that was done on the SAT, it is known that the scores roughly follow a normal distribution, with the standard deviation $\sigma=100$ .

    The 95% confidence interval for μ is $\left(475−2*\frac{100}{\sqrt{650}}, 475+2*\frac{100}{\sqrt{650}}\right)$, which is roughly $475\pm8$, or (467,484). For a sample size of n = 650, our margin of error is 8.

    Now, let's think about this problem in a slightly different way:

    An educational researcher is interested in estimating μ, the mean score on the math part of the SAT (SAT-M) of all community college students in his state with a margin of error of (only) 5, at the 95% confidence level. What is the sample size needed to achieve this? (σ, of course, is still assumed to be 100).

    To solve this, we set:

    $m=2⋅\frac{100}{\sqrt{n}}=5$

    so

    $\sqrt{n}=\frac{2\left(100\right)}{5}$

    and

    $n=\left(\frac{2\left(100\right)}{5}\right)^{2}=1600$

    So, for a sample size of 1,600 community college students, the researcher will be able to estimate μ with a margin of error of 5, at the 95% level. In this example, we can also imagine that the researcher has some flexibility in choosing the sample size, since there is a minimal cost (if any) involved in recording students' SAT-M scores, and there are many more than 1,600 community college students in each state.
```

Rather than take the same steps to isolate n every time we solve such a problem, we may obtain a general expression for the required n for a desired margin of error m and a certain level of confidence.

Since $m=z\times\frac{\sigma}{\sqrt{n}}$ is the formula to determine m for a given n, we can use simple algebra to express n in terms of m (multiply both sides by the square root of n, divide both sides by m, and square both sides) to get

$n=\left(\frac{z^{*}\sigma}{m}\right)^{2}$.

## Comment

Clearly, the sample size n must be an integer. In the previous example we got n = 1,600, but in other situations, the calculation may give us a non-integer result. In these cases, we should always *round up to the next highest integer.*

Using this "conservative approach," we'll achieve an interval at least as narrow as the one desired.

```{admonition} Example
    IQ scores are known to vary normally with a standard deviation of 15. How many students should be sampled if we want to estimate the population mean IQ at 99% confidence with a margin of error equal to 2?

    $n=\left(\frac{z^{*}\sigma}{m}\right)^{2} = \left(\frac{2.576\left(15\right)}{2}\right)^{2} = 373.26$

    Round up to be safe, and take a sample of 374 students.
```

The purpose of the next activity is to give you guided practice in sample size calculations for obtaining confidence intervals with a desired margin of error, at a certain confidence level. Consider the example from the previous Learn By Doing activity:

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

##### Comment

In the preceding activity, you saw that in order to calculate the sample size when planning a study, you needed to know the population standard deviation, sigma (σ). In practice, sigma is usually not known, because it is a parameter. (The rare exceptions are certain variables like IQ score or standardized tests that might be constructed to have a particular known sigma.)

Therefore, when researchers wish to compute the required sample size in preparation for a study, they use an *estimate* of sigma. Usually, sigma is estimated based on the standard deviation obtained in prior studies.

However, in some cases, there might not be any prior studies on the topic. In such instances, a researcher still needs to get a rough estimate of the standard deviation of the (yet-to-be-measured) variable, in order to determine the required sample size for the study. One way to get such a rough estimate is with the "range rule of thumb," which you will practice in the following activity.

The purpose of the next activity is to give you some experience with a method for roughly estimating sigma (σ, the population standard deviation) when no prior studies are available, in order to compute sample size when planning a first study.

##### Learn By Doing

An increasing global population requires more food from crops. With the world’s farmland limited due to overuse and a warming globe, one solution may come from crops that are genetically-engineered to grow in harsh desert soil.

Suppose that an agricultural researcher has just genetically engineered a brand new type of corn, never before tested, which the researcher hopes will yield a sufficient number of kernels of corn when grown in harsh desert soil. In order to test the corn, the researcher will grow a certain number of ears of the new corn in harsh desert soil, and will count and record the number of kernels per ear.

The researcher needs your statistical help in computing the minimum number of ears of the new corn that will be needed to be grown for the study.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

In the formula for the required number (n) of ears of corn the researcher needs in the study, you should have seen that we need to know sigma. Remember that the variable of interest is the number of kernels per ear of corn; so in this case sigma represents the standard deviation of number of kernels (from ear to ear), for the population of all ears of the new genetically engineered corn.

In this case, sigma (the standard deviation of kernels per ear) isn’t known, since the genetically engineered corn is brand new; and since the new corn has never been tested, there are no prior studies to use to estimate sigma.

So the researcher can use the ‘range rule of thumb,’ which says that, to a rough approximation, sigma is no bigger than range/4, where range = max – min. If you have no other estimate for sigma, you can therefore use range/4 as a rough estimate for sigma.

To use range/4 as a rough estimate for sigma, we need to estimate the range of the number of kernels on an ear of the new experimental corn. An ordinary ear of corn has around 800 kernels. We don’t know how few or how many kernels each ear of the experimental corn will have, but at the very minimum it could have zero (if the new corn didn’t produce any kernels at all); and even if the new corn actually over-produces compared to existing corn (despite being grown in harsh conditions), it certainly isn’t going to overproduce by more than twice (since it’s going to be grown in harsh desert soil), so the maximum number of kernels can’t be larger than 1,600.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
