# Interval Estimation

```{admonition} Learning Objectives
    - Explain what a confidence interval represents and determine how changes in sample size and confidence level affect the precision of the confidence interval.
```

Point estimation is simple and intuitive, but also a bit problematic. Here is why:

When we estimate, say, μ by the sample mean $\bar{x}$, we are almost guaranteed to make some kind of error. Even though we know that the values of $\bar{x}$ fall around μ, it is very unlikely that the value of $\bar{x}$ will fall exactly at μ .

Given that such errors are a fact of life for point estimates (by the mere fact that we are basing our estimate on one sample that is a small fraction of the population), these estimates are in themselves of limited usefulness, unless we are able to quantify the extent of the estimation error. Interval estimation addresses this issue. The idea behind *interval estimation* is, therefore, to enhance the simple point estimates by supplying information about the size of the error attached.

In this introduction, we'll provide examples that will give you a solid intuition about the basic idea behind interval estimation.

```{admonition} Example
    Consider the example that we discussed in the point estimation section:

    Suppose that we are interested in studying the IQ levels of students in a Smart University (SU). In particular (since IQ level is a quantitative variable), we are interested in estimating μ, the mean IQ level of all the students in SU. A random sample of 100 SU students was chosen, and their (sample) mean IQ level was found to be $\bar{x}=115$.

    .

    In point estimation we used $\bar{x}=115$ as the point estimate for μ. However, we had no idea of what the estimation error involved in such an estimation might be. Interval estimation takes point estimation a step further and says something like:

    "I am 95% confident that by using the point estimate $\bar{x}=115$ to estimate μ, I am off by no more than 3 IQ points. In other words, I am 95% confident that μ is within 3 of 115, or between 112 (115 - 3) and 118 (115 + 3)."

    Yet another way to say the same thing is: I am 95% confident that μ is somewhere in (or covered by) the interval (112,118). (*Comment:* At this point you should not worry about, or try to figure out, how we got these numbers. We'll do that later. All we want to do here is make sure you understand the idea.)

    Note that while point estimation provided just one number as an estimate for μ (115), interval estimation provides a whole interval of "plausible values" for μ (between 112 and 118), and also attaches the level of our confidence that this interval indeed includes the value of μ to our estimation (in our example, 95% confidence). The interval (112,118) is therefore called "a 95% confidence interval for μ."
```

Let's look at another example:

```{admonition} Example
    Let's consider the second example from the point estimation section.

    Suppose that we are interested in the opinions of U.S. adults regarding legalizing the use of marijuana. In particular, we are interested in the parameter p, the proportion of U.S. adults who believe marijuana should be legalized.

    Suppose a poll of 1,000 U.S. adults finds that 560 of them believe marijuana should be legalized.

    ```{figure} images/image030.gif
    :alt: A large circle represents the population of all US Adults. We are interested in the parameter p, the proportion who believe marijuana should be legalized. From this population we create a sample of size n=1000, represented by a smaller circle. In this sample, we find that p hat is .56 .

    A large circle represents the population of all US Adults. We are interested in the parameter p, the proportion who believe marijuana should be legalized. From this population we create a sample of size n=1000, represented by a smaller circle. In this sample, we find that p hat is .56 .
    ```

    If we wanted to estimate p, the population proportion, by a single number based on the sample, it would make intuitive sense to use the corresponding quantity in the sample, the sample proportion $\hat{p}=\frac{560}{1000}=.56$.

    Interval estimation would take this a step further and say something like:

    "I am 90% sure that by using .56 to estimate the true population proportion, p, I am off by (or, I have an error of) no more than .03 (or 3 percentage points). In other words, I am 90% confident that the actual value of p is somewhere between .53 (.56 - .03) and .59 (.56 + .03)."

    Yet another way of saying this is: "I am 90% confident that p is covered by the interval (.53, .59)."

    In this example, (.53, .59) is a 90% confidence interval for p.
```

## Let's summarize

The two examples showed us that the idea behind interval estimation is, instead of providing just one number for estimating an unknown parameter of interest, to provide an interval of plausible values of the parameter plus a level of confidence that the value of the parameter is covered by this interval.

We are now going to go into more detail and learn how these confidence intervals are created. As you'll see, the ideas that were developed in the "Sampling Distributions" module of the Probability unit will, again, be very important (as they were in point estimation).

We'll start by discussing confidence intervals for the population mean μ, and later discuss confidence intervals for the population proportion p.
