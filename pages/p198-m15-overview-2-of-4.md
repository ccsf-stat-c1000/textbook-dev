# The Four Steps of a Hypothesis Test

:::{admonition} Example: Concentration of a Chemical in a Drug
:class: tip

A certain prescription allergy medicine is supposed to contain an average of 245 parts per million (ppm) of a certain chemical. If the concentration is higher than 245 ppm, the drug will likely cause unpleasant side effects, and if the concentration is below 245 ppm, the drug may be ineffective. The manufacturer wants to check whether the mean concentration in a large shipment is the required 245 ppm or not. To this end, a random sample of 64 portions from the large shipment is tested, and it is found that the sample mean concentration is 250 ppm with a sample standard deviation of 12 ppm. Let's analyze this example according to the four steps of hypothesis testing we outlined on the previous page:

1. *Stating the claims:* Note that again, claim 1 basically says: "There is nothing unusual about this shipment; the mean concentration is the required 245 ppm." This claim is challenged by the manufacturer, who wants to check whether that is, indeed, the case or not.

   - *Claim 1:* The mean concentration in the shipment is the required 245 ppm.
   - *Claim 2:* The mean concentration in the shipment is not the required 245 ppm.

2. *Choosing a sample and collecting data:* A sample of $n = 64$ portions is chosen, and after summarizing the data it is found that the sample mean concentration is $\bar{x}=250$ and the sample standard deviation is $s = 12$. Is the fact that $\bar{x}=250$ is different from 245 strong enough evidence to reject claim 1 and conclude that the mean concentration in the whole shipment is not the required 245? In other words, do the data provide strong enough evidence to reject claim 1?

3. *Assessing the evidence:* In order to assess whether the data provide strong enough evidence against claim 1, we need to ask ourselves the following question: If the mean concentration in the whole shipment were really the required 245 ppm (i.e., if claim 1 were true), how surprising would it be to observe a sample of 64 portions where the sample mean concentration is off by 5 ppm or more (as we did)? It turns out that it would be extremely unlikely to get such a result if the mean concentration were really the required 245. There is only a probability of 0.0014 (i.e., about 14 in 10,000) of that happening. (Do not worry about how this was calculated at this point.)

4. *Making conclusions:* Here, it is pretty clear that a sample like the one we observed is extremely rare (or extremely unlikely) if the mean concentration in the shipment were really the required 245 ppm. The fact that we *did* observe such a sample therefore provides strong evidence against claim 1, so we reject it and conclude with very little doubt that the mean concentration in the shipment is not the required 245 ppm.
:::

Do you think that you're getting it? Let's make sure, and look at another example.

:::{admonition} Example: SAT Scores and Gender
:class: tip

Is there a relationship between gender and combined scores (Math + Verbal) on the SAT exam?

Following a report showing that in 2003, males scored generally higher than females on the SAT exam, an educational researcher wanted to check whether this was also the case in her school district. The researcher chose random samples of 150 males and 150 females from her school district, collected data on their SAT performance and found the following:

| Group | n | Mean | Standard deviation |
| --- | --- | --- | --- |
| Males | 150 | 1,025 | 212 |
| Females | 150 | 1,010 | 206 |

Again, let's see how the process of hypothesis testing works for this example:

1. *Stating the claims:* Note that again, claim 1 basically says: "There is nothing going on between the variables SAT and gender." Claim 2 represents what the researcher wants to check, or suspects might actually be the case.

   - *Claim 1:* Performance on the SAT is not related to gender (males and females score the same).
   - *Claim 2:* Performance on the SAT is related to gender—males score higher.

2. *Choosing a sample and collecting data:* Data were collected and summarized as given above. Is the fact that the sample mean score of males (1,025) is higher than the sample mean score of females (1,010) by 15 points strong enough information to reject claim 1 and conclude that in this researcher's school district, males score higher on the SAT than females?

3. *Assessment of evidence:* In order to assess whether the data provide strong enough evidence against claim 1, we need to ask ourselves: If SAT scores are in fact not related to gender (claim 1 is true), how likely is it to get data like the data we observed, in which the difference between the males' average and females' average score is as high as 15 points or higher? It turns out that the probability of observing such a sample result if SAT score is not related to gender is approximately 0.29. (Again, do not worry about how this was calculated at this point.)

4. *Conclusion:* Here, we have an example where observing a sample like the one we observed is definitely not surprising (roughly 30% chance) if claim 1 were true (i.e., if indeed there is no difference in SAT scores between males and females). We therefore conclude that our data do not provide enough evidence for rejecting claim 1.
:::

::::{admonition} Comment
:class: important

Go back and read the conclusion sections of the three examples, and pay attention to the wording. Note that there are two types of conclusions:

- "The data provide enough evidence to reject claim 1 and accept claim 2"; or
- "The data do not provide enough evidence to reject claim 1."

In particular, note that in the second type of conclusion *we did not say:* "*I accept claim 1*," but only "*I don't have enough evidence to reject claim 1*." We will come back to this issue later, but this is a good place to make you aware of this subtle difference.

Hopefully by now, you understand the logic behind the statistical hypothesis testing process. Here is a summary:

```{figure} images/gen/m15-logic-flow.svg
:alt: A flow chart describing the process. First, we state Claim 1 and Claim 2. Claim 1 says "nothing special is going on" and is challenged by Claim 2. Second, we collect relevant data and summarize them. Third, we assess how surprising it would be to observe data like that observed if Claim 1 were true. Fourth, we draw conclusions in context.
```
::::

## Check Your Understanding: Assessing the Evidence

For many years "working full-time" has meant 40 hours per week. Nowadays it seems that corporate employers expect their employees to work more than this amount. A researcher decides to investigate this hypothesis.

- *Claim 1:* The average time full-time corporate employees work per week is 40 hours.
- *Claim 2:* The average time full-time corporate employees work per week is more than 40 hours.

To substantiate his claim, the researcher randomly selects 250 corporate employees and finds that they work an average of 47 hours per week with a standard deviation of 3.2 hours.

:::{quiz} In step 3 of the hypothesis test, which question must the researcher answer in order to assess the evidence?
:hint: Step 3 always asks how surprising the observed data would be IF claim 1 were true.
:feedback-0: Correct! We assess how likely a sample mean of 47 hours or more would be in a sample of 250 employees if the population average were really 40 hours.
:feedback-1: This gets it backward—we assume claim 1 is true and ask how surprising the data are, not the other way around.
:feedback-2: The probability that claim 1 is true is not what the assessment step (or the p-value) measures.
* *How likely is a sample average of 47 hours or more, assuming the population average is really 40 hours?
* How likely is it that the population average is 40 hours, given that the sample average was 47?
* What is the probability that claim 1 is true?
:::

According to the Centers for Disease Control and Prevention (CDC), roughly 21.5% of all high-school seniors in the United States have used marijuana. (*Comment:* the figure represents those who reported use during the month prior to the survey, so the actual figure might be higher.) A sociologist suspects that the rate among African-American high school seniors is lower, and wants to check that. In this case, then,

- *Claim 1:* The rate of African-American high-school seniors who have used marijuana is 21.5% (same as the overall rate of seniors).
- *Claim 2:* The rate of African-American high-school seniors who have used marijuana is lower than 21.5%.

To check his claim, the sociologist chooses a random sample of 375 African-American high school seniors, and finds that 16.5% of them have used marijuana.

:::{quiz} Which probability would provide the appropriate assessment of the evidence in this study?
:hint: The evidence is a sample proportion of 16.5%. Claim 2 says the rate is LOWER, so results as low as, or lower than, the observed one count against claim 1.
:feedback-0: Correct! We ask how likely a sample proportion as low as 16.5% (or lower) would be in a random sample of 375 if the true rate were 21.5%.
:feedback-1: We must condition on claim 1 being true—not on claim 2.
:feedback-2: We need the probability of results as extreme as (or more extreme than) the observed one, not of exactly 16.5%.
* *The probability of a sample proportion of 16.5% or lower, if the true rate were 21.5%
* The probability of a sample proportion of 16.5% or lower, if the true rate were lower than 21.5%
* The probability of getting a sample proportion of exactly 16.5%
:::

## Check Your Understanding: Evidence and the Alternative

The most commonly accepted tradition is that college students will study 2 hours outside of class for every hour in class. This means 30 hours/week for a full-time student taking 15 units (hours of class). An educator suspects that this figure is different now than in the past.

- *Claim 1:* The average time full-time college students study outside of class per week is 30 hours.
- *Claim 2:* The average time full-time college students study outside of class per week is not 30 hours.

To substantiate her claim, the educator randomly selects 1,500 college students and finds that they study an average of 27 hours per week with a standard deviation of 1.7 hours.

:::{quiz} Notice that claim 2 here says the average is "not 30 hours" (rather than specifically more or less). Which sample results would count as evidence against claim 1?
:hint: Compare this claim 2 with the one-directional claims in the previous two studies.
:feedback-0: Correct! Since claim 2 is two-sided, sample averages far from 30 in EITHER direction (like the observed 27) count against claim 1.
:feedback-1: That would be appropriate if claim 2 said the average is LESS than 30, but it says "not 30."
:feedback-2: Sample averages near 30 support claim 1; they are not evidence against it.
* *Sample averages much lower OR much higher than 30
* Only sample averages much lower than 30
* Sample averages close to 30
:::
