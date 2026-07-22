# Conditions for the z-Test for a Proportion

```{admonition} Comments
:class: important

1. It should now be clear why this test is commonly known as *the z-test for the population proportion*. The name comes from the fact that it is based on a test statistic that is a *z-score*.

2. Recall fact 1 that we used for constructing the z-test statistic: when we take a *random* sample of size n from a population with population proportion p, the possible values of the sample proportion ($\hat{p}$), *when certain conditions are met*, have approximately a normal distribution. This result provides the theoretical justification for constructing the test statistic the way we did, and therefore the assumptions under which this result holds are the conditions that our data need to satisfy so that we can use this test. These two conditions are:

   1. The sample has to be random.
   2. The conditions under which the sampling distribution of $\hat{p}$ is normal are met; in other words, $np_0\geq10$ and $n(1-p_0)\geq10$.
```

Here we will pause to say more about the first condition, the need for a random sample. In the Producing Data unit we discussed sampling plans based on probability (such as a simple random sample, cluster sampling, or stratified sampling) that produce a non-biased sample, which can be safely used in order to make inferences about a population. We also noted that, in practice, other (non-random) sampling techniques are sometimes used when random sampling is not feasible. It is important, though, when these techniques are used, to be aware of the type of bias that they introduce, and thus the limitations of the conclusions that can be drawn from them.

For our purpose here, we will focus on one such practice: the situation in which a sample is not really chosen randomly, but in the context of the categorical variable that is being studied, the sample is regarded as random. For example, say that you are interested in the proportion of students at a certain college who suffer from seasonal allergies. For that purpose, the students in a large engineering class could be considered as a random sample, since there is nothing about being in an engineering class that makes you more or less likely to suffer from seasonal allergies. Technically, the engineering class is a convenience sample, but it is treated as a random sample in the context of this categorical variable. On the other hand, if you are interested in the proportion of students in the college who have math anxiety, then the class of engineering students clearly could not be viewed as a random sample, since engineering students probably have a much lower incidence of math anxiety than the college population overall.

## Check Your Understanding: Valid Samples for Testing

We are conducting a survey to determine if an upcoming bond measure will receive a majority vote in the county. The null hypothesis claims that p = 0.50, where p is the proportion of registered voters in the county who say they support the bond measure.

:::{quiz} Which sample would be valid for testing this hypothesis?
:hint: The sample must be representative of registered voters in the county with respect to opinions about the bond measure.
:feedback-0: Correct! A random sample of registered voters in the county is exactly the population the hypothesis is about.
:feedback-1: People attending a school board meeting likely have systematically different opinions about a school bond—this convenience sample is biased for this variable.
:feedback-2: Voters in a single neighborhood may not represent the whole county.
* *A random sample of 500 registered voters drawn from the county's voter roll
* The first 500 people leaving a school board meeting
* 500 registered voters from one neighborhood
:::

In 2007, a Gallup poll estimated that 45% of U.S. adults rated their financial situation as "good." Is the proportion different for this year? We want to test the null hypothesis p = 0.45.

:::{quiz} A large statistics class at a public university is surveyed, and the proportion rating their financial situation as "good" is computed. Is this sample valid for testing the hypothesis about U.S. adults?
:hint: Is there anything about being a college student that is related to one's financial situation?
:feedback-0: Correct! Students' financial situations differ systematically from U.S. adults in general, so this convenience sample cannot be treated as random for this variable.
:feedback-1: The relevant issue isn't the sample size—it's that students are not representative of U.S. adults with respect to financial situation.
* *Not valid—college students' financial situations are not representative of all U.S. adults
* Valid—as long as the class has more than 30 students
:::

We plan to poll 200 students enrolled in statistics at your college by distributing surveys during class.

:::{quiz} Which hypothesis could be validly tested with this survey?
:hint: For which variable can statistics students be treated as a random sample of the college's students?
:feedback-0: Correct! There is no reason to think enrollment in statistics is related to blood type, so the class can be treated as random for this variable.
:feedback-1: Statistics students are mostly students who need quantitative courses—their majors are not representative of the college.
:feedback-2: Math attitudes are directly related to taking a statistics course, so the sample is biased for this variable.
* *H₀: the proportion of students at the college with type O blood is 0.45
* H₀: the proportion of students at the college majoring in the humanities is 0.30
* H₀: the proportion of students at the college who enjoy math is 0.50
:::

Let's check the conditions in our three examples.

:::{admonition} Example 1: Defective Products
:class: tip

1. The 400 products were chosen at random.
2. n = 400 and $p_0=0.20$, so $np_0 = 400(0.20) = 80 \geq 10$ and $n(1-p_0) = 400(0.80) = 320 \geq 10$.

Both conditions are met.
:::

:::{admonition} Example 2: Marijuana Use at a Liberal Arts College
:class: tip

1. The 100 students were chosen at random.
2. n = 100 and $p_0=0.157$, so $np_0 = 100(0.157) = 15.7 \geq 10$ and $n(1-p_0) = 100(0.843) = 84.3 \geq 10$.

Both conditions are met.
:::

:::{admonition} Example 3: Death Penalty Support
:class: tip

1. The 1,000 U.S. adults were chosen at random.
2. n = 1,000 and $p_0=0.64$, so $np_0 = 1000(0.64) = 640 \geq 10$ and $n(1-p_0) = 1000(0.36) = 360 \geq 10$.

Both conditions are met.
:::

## Check Your Understanding: When Is the z-Test Appropriate?

In each of the following scenarios, decide whether it is appropriate to use the z-test for the population proportion p, and if not, which condition is violated.

*Scenario 1:* The UCLA Internet Report estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. To test whether that figure has changed, a random sample of 100 Internet users was chosen; 10 said they were extremely worried about credit card fraud. Here p is the proportion of all Internet users concerned about credit card fraud, and $H_0: p = 0.087$.

:::{quiz} Is it appropriate to use the z-test in scenario 1?
:hint: Check np₀ = 100(0.087) and n(1 − p₀) = 100(0.913).
:feedback-0: Correct! np₀ = 8.7, which is below 10, so the sampling distribution of p-hat cannot be assumed normal—the z-test should not be used.
:feedback-1: The sample IS random; the problem is that np₀ = 8.7 < 10.
:feedback-2: Check the products np₀ and n(1 − p₀): one of them fails.
* *No—np₀ = 8.7 is less than 10
* No—the sample was not random
* Yes—all conditions are met
:::

*Scenario 2:* Out of a random sample of 1,308 households with Internet access, 804 were connecting using dial-up. Here $H_0: p = 0.75$ and $H_a: p < 0.75$.

:::{quiz} Is it appropriate to use the z-test in scenario 2?
:hint: np₀ = 1308(0.75) and n(1 − p₀) = 1308(0.25).
:feedback-0: Correct! The sample is random, np₀ = 981 ≥ 10 and n(1 − p₀) = 327 ≥ 10.
:feedback-1: Both products are far above 10—check: 1308(0.75) = 981 and 1308(0.25) = 327.
* *Yes—the sample is random and both np₀ = 981 and n(1 − p₀) = 327 are at least 10
* No—the conditions on np₀ and n(1 − p₀) fail
:::

*Scenario 3:* To study whether Internet access at home (59.3% nationally) has continued growing, a random sample of 1,200 households *from one big metropolitan area* was chosen; 972 had an Internet connection. Here p is the proportion of all U.S. households with Internet access.

:::{quiz} Is it appropriate to use the z-test in scenario 3?
:hint: The population of interest is ALL U.S. households. Where did the sample come from?
:feedback-0: Correct! Households in one metropolitan area are not representative of all U.S. households with respect to Internet access (urban access rates differ from rural ones), so the sample cannot be treated as random for this population.
:feedback-1: The sample size conditions are fine (712 and 488); the problem is the sampling.
:feedback-2: The sample fails to represent the population of interest, so the test's conclusions would not apply to all U.S. households.
* *No—a sample from one metropolitan area is not a random sample of all U.S. households
* No—np₀ or n(1 − p₀) is below 10
* Yes—all conditions are met
:::

*Scenario 4:* A superintendent of a large school district claims that 80% of elementary school children in her district read at or above grade level. To test the claim, a random sample of 40 elementary school children from the district is chosen, and 27 read at or above grade level.

:::{quiz} Is it appropriate to use the z-test in scenario 4?
:hint: np₀ = 40(0.80) = 32, and n(1 − p₀) = 40(0.20) = 8.
:feedback-0: Correct! n(1 − p₀) = 8 falls below 10, so the normality condition fails and the z-test should not be used.
:feedback-1: np₀ = 32 is fine, but BOTH conditions must hold—n(1 − p₀) = 8 fails.
:feedback-2: The sample is random; the problem is the sample size condition.
* *No—n(1 − p₀) = 8 is less than 10
* Yes—np₀ = 32 is at least 10
* No—the sample was not random
:::

Checking that our data satisfy the conditions under which the test can be reliably used is a very important part of the hypothesis testing process. So far we haven't explicitly included it in the 4-step process of hypothesis testing, but now that we are discussing a specific test, you can see how it fits into the process. We are therefore now going to amend our 4-step process of hypothesis testing to include this extremely important part of the process.

```{admonition} The Four Steps in Hypothesis Testing
:class: note

1. State the appropriate null and alternative hypotheses, $H_0$ and $H_a$.
2. Obtain a random sample, collect relevant data, and *check whether the data meet the conditions under which the test can be used*. If the conditions are met, summarize the data using a test statistic.
3. Find the p-value of the test.
4. Based on the p-value, decide whether or not the results are significant and *draw your conclusions in context*.
```

With respect to the z-test for the population proportion that we are currently discussing: step 1 is completed, step 2 is completed, and step 3 is what we will work on next.
