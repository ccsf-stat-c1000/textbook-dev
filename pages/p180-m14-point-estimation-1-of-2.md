# Point Estimation: Estimating with a Single Number

Point estimation is the form of statistical inference in which, based on the sample data, we estimate the unknown parameter of interest using a *single* value (hence the name *point* estimation). As the following two examples illustrate, this form of inference is quite intuitive.

:::{admonition} Example: IQ at Smart University
:class: tip

Suppose that we are interested in studying the IQ levels of students at Smart University (SU). In particular (since IQ level is a quantitative variable), we are interested in estimating $\mu$, the mean IQ level of all the students at SU.

A random sample of 100 SU students was chosen, and their (sample) mean IQ level was found to be $\bar{x}=115$.

If we wanted to estimate $\mu$, the population mean IQ level, by a single number based on the sample, it would make intuitive sense to use the corresponding quantity in the sample, the sample mean $\bar{x}=115$. We say that 115 is the {term}`point estimate` for $\mu$, and in general, we'll always use $\bar{x}$ as the *point estimator* for $\mu$. (Note that when we talk about the *specific value* (115), we use the term *estimate*, and when we talk in general about the {term}`statistic` $\bar{x}$, we use the term *estimator*.)
:::

Here is another example.

:::{admonition} Example: Legalizing Marijuana
:class: tip

Suppose that we are interested in the opinions of U.S. adults regarding legalizing the use of marijuana. In particular, we are interested in the parameter p, the proportion of U.S. adults who believe marijuana should be legalized.

Suppose a poll of 1,000 U.S. adults finds that 560 of them believe marijuana should be legalized. If we wanted to estimate p, the population proportion, using a single number based on the sample, it would make intuitive sense to use the corresponding quantity in the sample, the sample proportion $\hat{p}=\frac{560}{1000}=0.56$. We say in this case that 0.56 is the {term}`point estimate` for p, and in general, we'll always use $\hat{p}$ as the *point estimator* for p.
:::

## Check Your Understanding: Computing Point Estimates

A study on exercise habits used a random sample of 2,540 college students (1,220 females and 1,320 males).

The study found the following:

- 818 of the females in the sample exercise on a regular basis.
- 924 of the males in the sample exercise on a regular basis.
- The average time that the 1,742 students who exercise on a regular basis $(818 + 924)$ spend exercising per week is 4.2 hours.

:::{quiz} What is the point estimate for the proportion of all female college students who exercise on a regular basis?
:hint: Use the corresponding sample quantity: 818 out of 1,220 females.
:feedback-0: Correct! p-hat = $818/1220 \approx 0.67$.
:feedback-1: 818/2540 uses the whole sample as the denominator, but the parameter concerns females only.
:feedback-2: 0.70 is the estimate for males (924/1320).
* *$818/1220 \approx 0.67$
* $818/2540 \approx 0.32$
* $924/1320 \approx 0.70$
:::

:::{quiz} What is the point estimate for the mean weekly exercise time of college students who exercise regularly?
:hint: Which sample statistic corresponds to this population mean?
:feedback-0: Correct! The sample mean, 4.2 hours, is the point estimate for $\mu$.
:feedback-1: 1,742 is the number of regular exercisers in the sample, not a mean.
:feedback-2: 0.69 is the overall proportion of exercisers, which estimates a proportion, not a mean.
* *4.2 hours
* 1,742
* 0.69
:::

## Check Your Understanding: Point Estimates in Context

A psychology researcher was conducting a study about newlywed heterosexual couples during the first two years of their marriage. 513 newlywed couples were randomly chosen for the study. One of the questions that the researcher was interested in was "During a typical week, how many times do you have sex?" The 513 responses had an average of 2.35 and standard deviation of 1.2. Another question that was asked is "During a typical week, how many evenings do you go out?" 171 of the couples answered that they go out more than twice a week.

:::{quiz} What is the point estimate for $\mu$, the mean number of times per week that newlywed couples have sex?
:hint: Use the sample mean.
:feedback-0: Correct! The sample mean, 2.35, is the point estimate for $\mu$.
:feedback-1: 1.2 is the sample standard deviation, which estimates $\sigma$.
:feedback-2: 171/513 estimates a proportion, not this mean.
* *2.35
* 1.2
* 0.33
:::

:::{quiz} What is the point estimate for p, the proportion of newlywed couples who go out more than twice a week?
:hint: 171 of the 513 couples said yes.
:feedback-0: Correct! p-hat = $171/513 \approx 0.33$.
:feedback-1: 2.35 estimates the mean of the other variable.
:feedback-2: 171 is the raw count; divide by the sample size 513.
* *$171/513 \approx 0.33$
* 2.35
* 171
:::
