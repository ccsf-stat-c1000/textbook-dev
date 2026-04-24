# Hypothesis Testing for the Population Proportion p (11 of 13)

```{admonition} Learning Objectives
    - Carry out hypothesis testing for the population proportion and mean (when appropriate), and draw conclusions in context.
```

## 3. One-Sided Alternative vs. Two-Sided Alternative

Recall that earlier we noticed (only visually) that for a given value of the test statistic z, the p-value of the two-sided test is twice as large as the p-value of the one-sided test. We will now further discuss this issue. In particular, we will use our example 2 (marijuana users at a certain college) to gain better intuition about this fact.

For illustration purposes, we are actually going to use example 2* (where out of a *sample of size 400*, 76 were marijuana users). Let's recall example 2*, but this time give two versions of it; the original version, and a slightly changed version, which we'll call example 2**. The differences are highlighted.

```{admonition} Example: 2*
    *There are rumors that students at a certain liberal arts college are more inclined to use drugs than U.S. college students in general.* Suppose that in a simple random sample of 400 students from the college, 76 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is .157? (This number is reported by the Harvard School of Public Health.)
```

```{admonition} Example: 2**
    *The dean of students in a certain liberal arts college was interested in whether the proportion of students who use drugs in her college is different than the proportion among U.S. college students in general.* Suppose that in a simple random sample of 400 students from the college, 76 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) *differs* from the national proportion, which is .157? (This number is reported by the Harvard School of Public Health.)
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

Indeed, in example 2* we suspect from the outset (based on the rumors) that the overall proportion (p) of marijuana smokers at the college is *higher* than the reported national proportion of .157, and therefore the appropriate alternative is H~o~:p>.157. In example 2**, as a result of the change of wording (which eliminated the part about the rumors), we simply wonder if p is *different* (in either direction) from the reported national proportion of .157, and therefore the appropriate alternative is the two-sided test: $H_{a}:p\neqp_{0}$. Would switching to the two-sided alternative have an effect on our results?

Let's explore that.

```{admonition} Example: 2*
    We already carried out the test for this example, and the results are summarized in the following figure:

    ```{figure} images/image293.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana. Conditions are met to use our method, so p-hat = 76/400 = .19, z = 1.81, and p-value = .035 . The p-value is low enough to let us conclude that we can reject H_0

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The hypotheses are H_0: p = .157 and H_a: p &gt; .157 . We take a sample of 400 students, represented by a smaller circle, and find that 76 use marijuana. Conditions are met to use our method, so p-hat = 76/400 = .19, z = 1.81, and p-value = .035 . The p-value is low enough to let us conclude that we can reject H_0
    ```

    The following figure reminds you how the p-value was found (using the test statistic):

    ```{figure} images/image294.gif
    :alt: A N(0,1) curve with z-scores of 0 and 1.81 marked on the horizontal axis. The area to the right of 1.81 under the curve is the p-value = .035

    A N(0,1) curve with z-scores of 0 and 1.81 marked on the horizontal axis. The area to the right of 1.81 under the curve is the p-value = .035
    ```
```

```{admonition} Example: 2**
    I. Here we are testing:

    ```{figure} images/image295.gif
    :alt: H_0: p = 1.57 H_a: p ≠ 1.57

    H_0: p = 1.57 H_a: p ≠ 1.57
    ```

    II. Since we have the same data as in example 2* (76 marijuana users out of 400), we have the same sample proportion and the same test statistic:

    ```{figure} images/image296.gif
    :alt: p-hat = .19 z = 1.81

    p-hat = .19 z = 1.81
    ```

    III. Since the calculation of the p-value depends on the type of alternative we have, here is where things start to be different. Statistical software tells us that the p-value for example 2** is 0.070. Here is a figure that reminds us how the p-value was calculated (based on the test statistic):

    ```{figure} images/image297.gif
    :alt: A N(0,1) curve with z-scores of -1.81, 0, and 1.81 marked on the horizontal axis. The area to the right of 1.81 under the curve is the .035 . The area to the left of 1.81 is also .035 . The p-value is the sum of these two areas, which is .07

    A N(0,1) curve with z-scores of -1.81, 0, and 1.81 marked on the horizontal axis. The area to the right of 1.81 under the curve is the .035 . The area to the left of 1.81 is also .035 . The p-value is the sum of these two areas, which is .07
    ```

    IV. If we use the .05 level of significance, the p-value we got is not small enough (.07>.05), and therefore we cannot reject H~o~. In other words, the data do not provide enough evidence to conclude that the proportion of marijuana smokers in the college is different from the national proportion (.157).
```

What happened here?

It should be pretty clear what happened here numerically. The p-value of the one-sided test (example 2*) is .035, suggesting the results are significant at the .05 significant level. However, the p-value of the two sided-test (example 2**) is twice the p-value of the one-sided test, and is therefore 2*.035=.07, suggesting that the results are not significant at the .05 significance level.

Here is a more conceptual explanation:

The idea is that in Example 2*, we began our hypothesis test with a piece of information (in the form of a rumor) about unknown population proportion p, which gave us a sort of head-start towards the goal of rejecting the null hypothesis. We foundthat the evidence that the data provided were then enough to cross the finish line and reject H~o~. In Example 2**, we had no prior information to go on, and the data alone were not enough evidence to cross the finish line and reject H~o~. The following figure illustrates this idea:

```{figure} images/image298.gif
:alt: Two &apos;races&apos; which illustrate why in the two-sided example we could not eliminate H_0. In the first race, H_0: p = .157, H_a: p &gt; .157 . This is a one-sided hypothesis, so we get a head start on the race. The data gets us more progress along the race track, enough that we cross the &apos;finish-line&apos; (being less than the significance level of .05), so we have enough evidence to reject H_0. In the two-sided problem where H_0: p = .157, H_a: p ≠ .157, we do not have a head start, since we are not given the information of which side. So, we only have the data to give us progress on the race, which isn&apos;t enough progress to cross the &apos;finish-line.&apos;

Two &apos;races&apos; which illustrate why in the two-sided example we could not eliminate H_0. In the first race, H_0: p = .157, H_a: p &gt; .157 . This is a one-sided hypothesis, so we get a head start on the race. The data gets us more progress along the race track, enough that we cross the &apos;finish-line&apos; (being less than the significance level of .05), so we have enough evidence to reject H_0. In the two-sided problem where H_0: p = .157, H_a: p ≠ .157, we do not have a head start, since we are not given the information of which side. So, we only have the data to give us progress on the race, which isn&apos;t enough progress to cross the &apos;finish-line.&apos;
```

We can summarize and say that in general it is harder to reject H~o~ against a two-sided H~a~ because the p-value is twice as large. Intuitively, a one-sided alternative gives us a head-start, and on top of that we have the evidence provided by the data. When our alternative is the two-sided test, we get no head-start and all we have are the data, and therefore it is harder to cross the finish line and reject H~o~.

##### Did I Get This?

Consider the following two hypothesis testing scenarios for the population proportion (p) and corresponding studies:

*I.* The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. A study was designed in order to examine whether that proportion has changed since.

*II.*The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. In light of the increasing problem of spyware, a study was designed in order to examine whether that proportion has increased since.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
