# Hypothesis Testing for the Population Proportion p (5 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## Comments

1. It should now be clear why this test is commonly known as *the z-test for the population proportion*. The name comes from the fact that it is based on a test statistic that is a *z-score.*
2. Recall fact 1 that we used for constructing the z-test statistic. Here is part of it again: When we take a *random* sample of size n from a population with population proportion p, the possible values of the sample proportion ($\hat{p}$) (*when certain conditions are met*) have approximately a normal distribution with a mean of ... and a standard deviation of .... This result provides the theoretical justification for constructing the test statistic the way we did, and therefore the assumptions under which this result holds (in bold, above) are the conditions that our data need to satisfy so that we can use this test. These two conditions are:
  1. The sample has to be random.
  2. The conditions under which the sampling distribution of $\hat{p}$ is normal are met. In other words:
3. Here we will pause to say more about condition (i.) above, the need for a random sample. In the Probability Unit we discussed sampling plans based on probability (such as a simple random sample, cluster, or stratified sampling) that produce a non-biased sample, which can be safely used in order to make inferences about a population. We noted in the Probability Unit that, in practice, other (non-random) sampling techniques are sometimes used when random sampling is not feasible. It is important though, when these techniques are used, to be aware of the type of bias that they introduce, and thus the limitations of the conclusions that can be drawn from them. For our purpose here, we will focus on one such practice, the situation in which a sample is not really chosen randomly, but in the context of the categorical variable that is being studied, the sample is regarded as random. For example, say that you are interested in the proportion of students at a certain college who suffer from seasonal allergies. For that purpose, the students in a large engineering class could be considered as a random sample, since there is nothing about being in an engineering class that makes you more or less likely to suffer from seasonal allergies. Technically, the engineering class is a convenience sample, but it is treated as a random sample in the context of this categorical variable. On the other hand, if you are interested in the proportion of students in the college who have math anxiety, then the class of engineering students clearly could not be viewed as a random sample, since engineering students probably have a much lower incidence of math anxiety than the college population overall.

##### Learn By Doing

We are conducting a survey to determine if an upcoming bond measure will receive a majority vote in the county. The null hypothesis claims that p = 0.50, where p is the proportion of registered voters in the county who say they support the bond measure.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

In 2007, a Gallup poll estimated that 45% of U.S. adults rated their financial situation as “good.” Is the proportion different for this year? Which of the following samples could be used to test the null hypothesis p = 0.45? Mark each as valid (OK to use to test the hypothesis) or not valid (should not be used to test the hypothesis).

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

We plan to poll 200 students enrolled in statistics at your college by distributing surveys during class. Which of the following hypotheses could be tested with the survey results? Mark each as valid (OK to use to test the hypothesis) or not valid (should not be used to test the hypothesis.)

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Let's check the conditions in our three examples.

```{admonition} Example: 1
    1. The 400 products were chosen at random.
    2. n = 400, $p_{0}=.2$, and therefore:

    ```{figure} images/image250.gif
    :alt: * n × p_0 = 80 ≥ 10 * n × (1 - p_0) = 320 ≥ 10

    * n × p_0 = 80 ≥ 10 * n × (1 - p_0) = 320 ≥ 10
    ```
```

```{admonition} Example: 2
    1. The 100 students were chosen at random.
    2. n = 100, $p_{0}=.157$, and therefore:

    ```{figure} images/image252.gif
    :alt: * n × p_0 = 15.7 ≥ 10 * n × (1 - p_0) = 84.3 ≥ 10

    * n × p_0 = 15.7 ≥ 10 * n × (1 - p_0) = 84.3 ≥ 10
    ```
```

```{admonition} Example: 3
    1. The 1,000 U.S. adults were chosen at random.
    2. n = 1,000, $p_{0}=.64$, and therefore:

    ```{figure} images/image254.gif
    :alt: * n × p_0 = 640 ≥ 10 * n × (1 - p_0) = 360 ≥ 10

    * n × p_0 = 640 ≥ 10 * n × (1 - p_0) = 360 ≥ 10
    ```
```

## Learn By Doing

In each of the following scenarios, you need to decide whether it is appropriate to use the z-test for the population proportion p, and if not, which condition is violated.

*Scenario 1:*The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. Has that figure changed since? To test this, a random sample of 100 Internet users was chosen. When interviewed, 10 said that they were extremely worried about credit card fraud when buying online. Let p be the proportion of all Internet users who are concerned about credit card fraud.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 2:*The UCLA Internet Report (February 2003) estimated that a proportion of roughly .75 of Internet-using homes are still using dial-up access, but claimed that the use of dial-up is declining. Is that really the case? To examine this, a follow-up study was conducted a year later in which out of a random sample of 1,308 households that had an Internet connection, 804 were connecting using a dial-up modem. Let p be the proportion of all U.S. Internet-using households that have dial-up access.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 3:*According to the UCLA Internet Report (February 2003) the use of the Internet at home is growing steadily. The report estimated that roughly 59.3% of households in the Unites States have Internet access at home. Has that trend continued since the report was released? To study this, a random sample of 1,200 households from a big metropolitan area was chosen, and it was found that 972 had an Internet connection. Let p be the proportion of U.S. households that have Internet access.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 4:*A superintendent of a large school district claims that 80% of elementary school children in her district read at or above grade level (which is much higher than the national figure). To test the superintendent’s claim, a random sample of 40 elementary school children from the school district is chosen, and it found that only 27 of read at or above grade level. Let p be the proportion of all school children in the school district who read at or above grade level.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

Checking that our data satisfy the conditions under which the test can be reliably used is a very important part of the hypothesis testing process. So far we haven't explicitly included it in the 4-step process of hypothesis testing, but now that we are discussing a specific test, you can see how it fits into the process. We are therefore now going to amend our 4-step process of hypothesis testing to include this extremely important part of the process.

## The Four Steps in Hypothesis Testing

1. State the appropriate null and alternative hypotheses, H~o~ and H~a~.
2. Obtain a random sample, collect relevant data, and *check whether the data meet the conditions under which the test can be used*. If the conditions are met, summarize the data using a test statistic.
3. Find the p-value of the test.
4. Based on the p-value, decide whether or not the results are significant and *draw your conclusions in context.*

With respect to the z-test, the population proportion that we are currently discussing:

Step 1: Completed

Step 2: Completed

Step 3: This is what we will work on next.
