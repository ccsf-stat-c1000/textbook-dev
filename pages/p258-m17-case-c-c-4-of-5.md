---
enumerator: "237."
---
# The Chi-Square Test: P-value and Conclusion

## Step 3: Finding the P-value

The p-value for the chi-square test for independence is the probability of getting counts like those observed, assuming that the two variables are not related (which is what is claimed by the null hypothesis). The smaller the p-value, the more surprising it would be to get counts like we did if the null hypothesis were true.

Technically, the p-value is the probability of observing a $\chi^2$ statistic at least as large as the one observed. Using statistical software, we find that the p-value for the drunk driving test is 0.201.

## Step 4: Stating the Conclusion in Context

As usual, we use the magnitude of the p-value to draw our conclusions. A small p-value indicates that the evidence provided by the data is strong enough to reject $H_0$ and conclude (beyond a reasonable doubt) that the two variables are related. In particular, if a significance level of 0.05 is used, we reject $H_0$ if the p-value is less than 0.05.

:::{admonition} Example: Drunk Driving and Gender
:class: tip

A p-value of 0.201 is not small at all. There is no compelling statistical evidence to reject $H_0$, and so we will continue to assume it may be true. Gender and drunk driving may be independent, and so the data suggest that a law that forbids sale of 3.2% beer to males and permits it to females is unwarranted. In fact, the Supreme Court, by a 7-2 majority, struck down the Oklahoma law as discriminatory and unjustified. In the majority opinion, Justice Brennan wrote:

"Clearly, the protection of public health and safety represents an important function of state and local governments. However, appellees' statistics in our view cannot support the conclusion that the gender-based distinction closely serves to achieve that objective and therefore the distinction cannot under [prior case law] withstand equal protection challenge."
:::

## Check Your Understanding: Drawing a Conclusion from the Chi-Square Test

Let's draw our conclusion regarding the relationship between participation in the 9/11 rescue and risk of alcohol problems among New York firefighters. For those data, software gives a chi-square statistic of about 12.7 and a p-value of about 0.0004.

:::{quiz} Using a 0.05 significance level, what is the correct conclusion for the firefighter study?
:hint: Compare 0.0004 with 0.05 and state the conclusion in context.
:feedback-0: Correct! The tiny p-value provides strong evidence against independence, so we conclude that alcohol risk is related to participation in the 9/11 rescue: participants show a higher risk (28% vs. 20%).
:feedback-1: 0.0004 is far below 0.05, so we DO reject $H_0$.
:feedback-2: Since this is an observational study, we can conclude association, but the direction of the observed difference (participants at higher risk) is part of a complete conclusion.
* *Reject $H_0$—alcohol risk among firefighters is related to 9/11 rescue participation, with participants at higher risk
* Do not reject $H_0$—the evidence is insufficient
* Reject $H_0$ and conclude that 9/11 participation causes alcoholism
:::

```{admonition} Comment: The Effect of Sample Size
:class: important

This is a good opportunity to illustrate an important idea that was discussed earlier in this unit: the larger the sample the results are based on, the more evidence they carry. Let's take the drunk driving example and simply multiply each of the counts by 3:

| | Yes | No | Total |
| --- | --- | --- | --- |
| **Male** | 231 | 1,212 | 1,443 |
| **Female** | 48 | 366 | 414 |
| **Total** | 279 | 1,578 | 1,857 |

Obviously, the conditional percents remain the same (males: $231/1443 = 16.0\%$ drank; females: $48/414 = 11.6\%$ drank). In other words, the sample provides the "same" results, but this time they are based on a much larger sample (1,857 instead of 619). This is reflected by the chi-square test. In this case, software gives us a chi-square statistic of 4.91 and a p-value of 0.027.

When done with software, the original chi-square statistic was 1.637 (software doesn't round as much as we did by hand). Since the observed counts are triple what they were before, the expected counts are also tripled, and the chi-square statistic is $3 \times 1.637 = 4.91$ (which now is in the "large" range for a 2-by-2 table). Therefore, the p-value is smaller and is now 0.027.

Now we *do* reject $H_0$, and we conclude that gender and drunk driving are related. In this case, the largest contribution to the chi-square statistic comes from the fact that so few females drove drunk (48) compared to the number that would be expected $(62.2 = 414 \times 279/1857)$ if gender and drunk driving were not related. This contribution is $\frac{(48-62.2)^{2}}{62.2}=3.242$.
```

## Check Your Understanding: Sample Size and the Chi-Square Test

:::{quiz} The same conditional percentages (16.0% vs. 11.6%) led to "do not reject" with $n = 619$ but "reject" with $n = 1{,}857$. What is the lesson?
:hint: This mirrors what we saw for tests about means and proportions.
:feedback-0: Correct! The same observed difference carries more weight when based on more data—larger samples make the same relationship easier to detect (and can make even weak relationships statistically significant).
:feedback-1: The percentages were identical—only the amount of data changed.
:feedback-2: Neither analysis was wrong; the strength of evidence legitimately depends on the sample size.
* *Evidence depends on sample size—the same observed relationship becomes significant with enough data
* The percentages must have changed when the counts were tripled
* One of the two analyses must have been performed incorrectly
:::
