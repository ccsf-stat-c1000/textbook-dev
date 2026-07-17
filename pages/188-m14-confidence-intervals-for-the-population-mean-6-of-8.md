# Choosing a Sample Size for a Desired Margin of Error

```{admonition} Learning Objectives
:class: note

- Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
- Find confidence intervals for the population mean and the population proportion (when certain conditions are met), and perform sample size calculations.
```

## Sample Size Calculations

As we just learned, for a given level of confidence, the sample size determines the size of the margin of error and thus the width, or precision, of our interval estimation. This process can be reversed.

In situations where a researcher has some flexibility as to the sample size, the researcher can calculate in advance what sample size he/she needs in order to be able to report a confidence interval with a certain level of confidence and a certain margin of error. Let's look at an example.

:::{admonition} Example: Planning the SAT-M Study
:class: tip

Recall the example about the SAT-M scores of community college students, where scores follow a normal distribution with standard deviation $\sigma=100$. With a sample of n = 650, the 95% confidence interval had margin of error 8.

Now, let's think about this problem in a slightly different way:

An educational researcher is interested in estimating μ, the mean SAT-M score of all community college students in his state, with a margin of error of (only) 5, at the 95% confidence level. What is the sample size needed to achieve this? (σ, of course, is still assumed to be 100.)

To solve this, we set:

$$m=2\cdot\frac{100}{\sqrt{n}}=5$$

so

$$\sqrt{n}=\frac{2(100)}{5} \quad\text{and}\quad n=\left(\frac{2(100)}{5}\right)^{2}=1600$$

So, for a sample size of 1,600 community college students, the researcher will be able to estimate μ with a margin of error of 5, at the 95% level. In this example, we can also imagine that the researcher has some flexibility in choosing the sample size, since there is a minimal cost (if any) involved in recording students' SAT-M scores, and there are many more than 1,600 community college students in each state.
:::

Rather than take the same steps to isolate n every time we solve such a problem, we may obtain a general expression for the required n for a desired margin of error m and a certain level of confidence.

Since $m=z^{*}\cdot\frac{\sigma}{\sqrt{n}}$ is the formula to determine m for a given n, we can use simple algebra to express n in terms of m (multiply both sides by the square root of n, divide both sides by m, and square both sides) to get

$$n=\left(\frac{z^{*}\sigma}{m}\right)^{2}$$

## Comment

Clearly, the sample size n must be an integer. In the previous example we got n = 1,600, but in other situations, the calculation may give us a non-integer result. In these cases, we should always *round up to the next highest integer.* Using this "conservative approach," we'll achieve an interval at least as narrow as the one desired.

:::{admonition} Example: Sample Size for IQ
:class: tip

IQ scores are known to vary normally with a standard deviation of 15. How many students should be sampled if we want to estimate the population mean IQ at 99% confidence with a margin of error equal to 2?

$$n=\left(\frac{z^{*}\sigma}{m}\right)^{2} = \left(\frac{2.576(15)}{2}\right)^{2} = 373.26$$

Round up to be safe, and take a sample of 374 students.
:::

## Learn By Doing

:::{quiz} A researcher wants to estimate the mean pregnancy length of women who smoke (σ = 16 days) with 95% confidence and a margin of error of 2 days. What sample size is required?
:hint: n = (z*σ/m)² = (2 × 16/2)².
:feedback-0: Correct! n = (32/2)² = 16² = 256 women.
:feedback-1: 64 comes from forgetting to square; the formula squares the whole quantity.
:feedback-2: Use z* = 2 for 95% confidence, giving (2 × 16/2)² = 256.
* *256
* 64
* 683
:::

## Comment

In the preceding activity, you saw that in order to calculate the sample size when planning a study, you needed to know the population standard deviation, sigma (σ). In practice, sigma is usually not known, because it is a parameter. (The rare exceptions are certain variables like IQ score or standardized tests that might be constructed to have a particular known sigma.)

Therefore, when researchers wish to compute the required sample size in preparation for a study, they use an *estimate* of sigma. Usually, sigma is estimated based on the standard deviation obtained in prior studies.

However, in some cases, there might not be any prior studies on the topic. In such instances, a researcher still needs to get a rough estimate of the standard deviation of the (yet-to-be-measured) variable, in order to determine the required sample size for the study. One way to get such a rough estimate is with the "range rule of thumb."

## Learn By Doing

An increasing global population requires more food from crops. With the world's farmland limited due to overuse and a warming globe, one solution may come from crops that are genetically engineered to grow in harsh desert soil.

Suppose that an agricultural researcher has just genetically engineered a brand new type of corn, never before tested, which the researcher hopes will yield a sufficient number of kernels of corn when grown in harsh desert soil. In order to test the corn, the researcher will grow a certain number of ears of the new corn in harsh desert soil, and will count and record the number of kernels per ear. The researcher needs your statistical help in computing the minimum number of ears of the new corn that will be needed for the study.

In the formula for the required number (n) of ears of corn, we need to know sigma—here, the standard deviation of the number of kernels per ear for the population of all ears of the new corn. Since the corn is brand new, there are no prior studies to estimate sigma from.

So the researcher can use the "range rule of thumb," which says that, to a rough approximation, sigma is no bigger than range/4, where range = max − min. If you have no other estimate for sigma, you can therefore use range/4 as a rough estimate.

To use range/4, we need to estimate the range of the number of kernels on an ear of the new experimental corn. An ordinary ear of corn has around 800 kernels. We don't know how few or how many kernels each ear of the experimental corn will have, but at the very minimum it could have zero (if the new corn didn't produce any kernels at all); and even if the new corn actually over-produces compared to existing corn (despite being grown in harsh conditions), it certainly isn't going to overproduce by more than twice, so the maximum number of kernels can't be larger than 1,600.

:::{quiz} Using the range rule of thumb, what is the rough estimate for sigma?
:hint: Range = 1,600 − 0; sigma ≈ range/4.
:feedback-0: Correct! σ ≈ (1600 − 0)/4 = 400 kernels.
:feedback-1: 800 is the typical number of kernels, not the range divided by 4.
:feedback-2: Divide the range by 4, not by 2.
* *400
* 800
* 200
:::

:::{quiz} Using σ ≈ 400, how many ears of corn must be grown to estimate the mean number of kernels with 95% confidence and a margin of error of 50 kernels?
:hint: n = (2 × 400/50)².
:feedback-0: Correct! n = (800/50)² = 16² = 256 ears of corn.
:feedback-1: Don't forget to square the quantity: (16)² = 256.
:feedback-2: Use z* = 2 for 95% confidence.
* *256
* 16
* 1,024
:::
