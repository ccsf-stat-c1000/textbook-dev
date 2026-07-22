# Null and Alternative Hypotheses

## More Details and Terminology

Now that we understand the general idea of how statistical hypothesis testing works, let's go back to each of the steps and delve slightly deeper, getting more details and learning some terminology.

### Hypothesis Testing Step 1: Stating the Claims

In all three examples, our aim is to decide between two opposing points of view, claim 1 and claim 2. In hypothesis testing, *claim 1* is called the *null hypothesis* (denoted $H_0$), and *claim 2* plays the role of the *alternative hypothesis* (denoted $H_a$). As we saw in the three examples, the null hypothesis suggests nothing special is going on; in other words, there is no change from the status quo, no difference from the traditional state of affairs, no relationship. In contrast, the alternative hypothesis disagrees with this, stating that something is going on, or there is a change from the status quo, or there is a difference from the traditional state of affairs. The alternative hypothesis, $H_a$, usually represents what we want to check or what we suspect is really going on.

Let's go back to our three examples and apply the new notation:

*In example 1 (smoking at Goodheart University):*

- $H_0$: The proportion of smokers at Goodheart is 0.20.
- $H_a$: The proportion of smokers at Goodheart is less than 0.20.

*In example 2 (concentration of a chemical in a drug):*

- $H_0$: The mean concentration in the shipment is the required 245 ppm.
- $H_a$: The mean concentration in the shipment is not the required 245 ppm.

*In example 3 (SAT scores and gender):*

- $H_0$: Performance on the SAT is not related to gender (males and females score the same).
- $H_a$: Performance on the SAT is related to gender—males score higher.

## Check Your Understanding: Identifying Null and Alternative Hypotheses

According to the Centers for Disease Control and Prevention, the proportion of U.S. adults age 25 or older who smoke is 0.22. A researcher suspects that the rate is lower among U.S. adults 25 or older who have a bachelor's degree or higher education level.

:::{quiz} What are the appropriate hypotheses for this study?
:hint: The null hypothesis says "nothing special is going on" among college graduates; the alternative captures the researcher's suspicion.
:feedback-0: Correct! H₀ says the rate among college graduates is the same as the overall rate (0.22); Hₐ says it is lower, as the researcher suspects.
:feedback-1: This reverses the roles—the researcher's suspicion belongs in the alternative hypothesis, not the null.
:feedback-2: The alternative should be directional ("lower") because the researcher specifically suspects a lower rate.
* *H₀: the proportion of college-graduate smokers is 0.22; Hₐ: the proportion is less than 0.22
* H₀: the proportion is less than 0.22; Hₐ: the proportion is 0.22
* H₀: the proportion is 0.22; Hₐ: the proportion is not 0.22
:::

A study investigated whether there are differences between the mean IQ level of people who were reared by their biological parents and those who were reared by someone else.

:::{quiz} What are the appropriate hypotheses for this study?
:hint: No direction is suspected here—the study simply asks whether there is a difference.
:feedback-0: Correct! H₀ says there is no difference between the two means; Hₐ says the means differ (in either direction), since no particular direction was suspected.
:feedback-1: The study did not suspect a particular direction, so the alternative should be two-sided.
:feedback-2: The null hypothesis is always the "no difference / nothing special" claim.
* *H₀: the two groups have the same mean IQ; Hₐ: the two groups have different mean IQs
* H₀: the two groups have the same mean IQ; Hₐ: those reared by biological parents have a higher mean IQ
* H₀: the two groups have different mean IQs; Hₐ: the two groups have the same mean IQ
:::

## Check Your Understanding: Hypotheses in Context

Data were collected in order to determine whether there is a relationship between a person's level of education and whether or not the person is a smoker.

:::{quiz} What are the appropriate hypotheses for this study?
:hint: The null hypothesis is the "no relationship" claim.
:feedback-0: Correct! H₀: there is no relationship between level of education and smoking; Hₐ: there is a relationship.
:feedback-1: This reverses the roles of the null and alternative hypotheses.
:feedback-2: No direction was specified in the research question, and hypotheses about relationships between two categorical variables are stated in terms of relationship/no relationship.
* *H₀: there is no relationship between education level and smoking; Hₐ: there is a relationship
* H₀: there is a relationship between education level and smoking; Hₐ: there is no relationship
* H₀: more-educated people smoke less; Hₐ: more-educated people smoke more
:::

### Hypothesis Testing Step 2: Choosing a Sample and Collecting Data

This step is pretty obvious. This is what inference is all about. You look at sampled data in order to draw conclusions about the entire population. In the case of hypothesis testing, based on the data, you draw conclusions about whether or not there is enough evidence to reject $H_0$.

There is, however, one detail that we would like to add here. In this step we collect data and *summarize* them. Go back and look at the second step in our three examples. Note that in order to summarize the data we used simple sample statistics such as the sample proportion ($\hat{p}$), sample mean ($\bar{x}$) and the sample standard deviation (s).

In practice, you go a step further and use these sample statistics to summarize the data with what's called a *test statistic*. We are not going to go into any details right now, but we will discuss test statistics when we go through the specific tests.

### Hypothesis Testing Step 3: Assessing the Evidence

As we saw, this is the step where we calculate how likely it is to get data like that observed when $H_0$ is true. In a sense, this is the heart of the process, since we draw our conclusions based on this probability. If this probability is very small (see example 2), then that means that it would be very surprising to get data like that observed if $H_0$ were true. The fact that we *did* observe such data is therefore evidence against $H_0$, and we should reject it. On the other hand, if this probability is not very small (see example 3), this means that observing data like that observed is not very surprising if $H_0$ were true, so the fact that we observed such data does not provide evidence against $H_0$. This crucial probability, therefore, has a special name. It is called the *p-value* of the test.

In our three examples, the p-values were given to you (and you were reassured that you didn't need to worry about how these were derived):

- Example 1: p-value = 0.106
- Example 2: p-value = 0.0007
- Example 3: p-value = 0.29

Obviously, the smaller the p-value, the more surprising it is to get data like ours when $H_0$ is true, and therefore, the stronger the evidence the data provide against $H_0$. Looking at the three p-values of our three examples, we see that the data that we observed in example 2 provide the strongest evidence against the null hypothesis, followed by example 1, while the data in example 3 provide the least evidence against $H_0$.

```{admonition} Comments
:class: important

1. Right now we will not go into specific details about p-value calculations, but just mention that since the p-value is the probability of getting *data* like those observed when $H_0$ is true, it would make sense that the calculation of the p-value will be based on the data summary, which, as we mentioned, is the test statistic. Indeed, this is the case. In practice, we will mostly use software to provide the p-value for us.

2. It should be noted that in the past, before statistical software was such an integral part of introductory statistics courses, it was common to use critical values (rather than p-values) in order to assess the evidence provided by the data. While this course focuses on p-values, the critical values approach leads to the same conclusions.
```
