# Overview (3 of 4)

```{admonition} Learning Objectives
    - Explain the logic behind and the process of hypotheses testing. In particular, explain what the p-value is and how it is used to draw conclusions.
```

## More Details and Terminology

Now that we understand the general idea of how statistical hypothesis testing works, let's go back to each of the steps and delve slightly deeper, getting more details and learning some terminology.

*Hypothesis testing step 1: Stating the claims.*

In all three examples, our aim is to decide between two opposing points of view, Claim 1 and Claim 2. In hypothesis testing, *Claim 1* is called the *null hypothesis* (denoted "*H~0~*"), and *Claim 2* plays the role of the *alternative hypothesis* (denoted "*H~a~*"). As we saw in the three examples, the null hypothesis suggests nothing special is going on; in other words, there is no change from the status quo, no difference from the traditional state of affairs, no relationship. In contrast, the alternative hypothesis disagrees with this, stating that something is going on, or there is a change from the status quo, or there is a difference from the traditional state of affairs. The alternative hypothesis, H~a~, usually represents what we want to check or what we suspect is really going on.

Let's go back to our three examples and apply the new notation:

*In example 1:*

- *H~0~:* The proportion of smokers at Goodheart is
                            .20.
- *H~a~:* The proportion of smokers at Goodheart is less
                            than .20.

*In example 2:*

- *H~0~:* The mean concentration in the shipment is the
                            required 245 ppm.
- *H~a~:* The mean concentration in the shipment is not
                            the required 245 ppm.

*In example 3:*

- *H~0~:* Performance on the SAT is not related to gender
                            (males and females score the same).
- *H~a~:* Performance on the SAT is related to gender -
                            males score higher.

##### Learn By Doing

According to the Centers for Disease Control and Prevention, the proportion of U.S. adults age 25 or older who smoke is .22. A researcher suspects that the rate is lower among U.S. adults 25 or older who have a bachelor's degree or higher education level.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

A study investigated whether there are differences between the mean IQ level of people who were reared by their biological parents and those who were reared by someone else.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### Did I Get This?

Data were collected in order to determine whether there is a relationship between a person's level of education and whether or not the person is a smoker.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Hypothesis testing step 2: Choosing a sample and collecting data*.

This step is pretty obvious. This is what inference is all about. You look at sampled data in order to draw conclusions about the entire population. In the case of hypothesis testing, based on the data, you draw conclusions about whether or not there is enough evidence to reject H~o~.

There is, however, one detail that we would like to add here. In this step we collect data and *summarize* it. Go back and look at the second step in our three examples. Note that in order to summarize the data we used simple sample statistics such as the sample proportion ($\hat{p}$), sample mean ($\bar{x}$) and the sample standard deviation (s).

In practice, you go a step further and use these sample statistics to summarize the data with what's called a *test statistic*. We are not going to go into any details right now, but we will discuss test statistics when we go through the specific tests.

*Hypothesis testing step 3: Assessing the evidence.*

As we saw, this is the step where we calculate how likely is it to get data like that observed when H~o~ true. In a sense, this is the heart of the process, since we draw our conclusions based on this probability. If this probability is very small (see example 2), then that means that it would be very surprising to get data like that observed if H~0~ were true. The fact that we *did* observe such data is therefore evidence against H~0~, and we should reject it. On the other hand, if this probability is not very small (see example 3) this means that observing data like that observed is not very surprising if H~0~ were true, so the fact that we observed such data does not provide evidence against H~o~. This crucial probability, therefore, has a special name. It is called the *p-value* of the test.

In our three examples, the p-values were given to you (and you were reassured that you didn't need to worry about how these were derived):

- Example 1: p-value = .106
- Example 2: p-value = .0007
- Example 3: p-value = .29

Obviously, the smaller the p-value, the more surprising it is to get data like ours when H~0~ is true, and therefore, the stronger the evidence the data provide against H~0~. Looking at the three p-values of our three examples, we see that the data that we observed in example 2 provide the strongest evidence against the null hypothesis, followed by example 1, while the data in example 3 provides the least evidence against H~0~.

##### Comments:

Right now we will not go into specific details about p-value calculations, but just mention that since the p-value is the probability of getting *data* like those observed when H~0~ is true, it would make sense that the calculation of the p-value will be based on the data summary, which, as we mentioned, is the test statistic. Indeed, this is the case. In practice, we will mostly use software to provide the p-value for us.

It should be noted that in the past, before statistical software was such an integral part of intro stats courses it was common to use critical values (rather than p-values) in order to assess the evidence provided by the data. While this courses focuses on p-values, we will provide some details about the critical values approach later in this module for those students who are interested in learning more about it.
