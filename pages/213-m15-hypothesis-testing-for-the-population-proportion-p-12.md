# Hypothesis Testing for the Population Proportion p (12 of 13)

```{admonition} Learning Objectives
    - Apply the concepts of: sample size, statistical significance vs. practical importance, and the relationship between hypothesis testing and confidence intervals.
```

## 4. Hypothesis Testing and Confidence Intervals

The last topic we want to discuss is the relationship between hypothesis testing and confidence intervals. Even though the flavor of these two forms of inference is different (confidence intervals estimate a parameter, and hypothesis testing assesses the evidence in the data against one claim and in favor of another), there is a strong link between them.

We will explain this link (using the z-test and confidence interval for the population proportion), and then explain how confidence intervals can be used after a test has been carried out.

Recall that a confidence interval gives us a set of plausible values for the unknown population parameter. We may therefore examine a confidence interval to informally decide if a proposed value of population proportion seems plausible.

For example, if a 95% confidence interval for p, the proportion of all U.S. adults already familiar with Viagra in May 1998, was (.61, .67), then it seems clear that we should be able to reject a claim that only 50% of all U.S. adults were familiar with the drug, since based on the confidence interval, .50 is not one of the plausible values for p.

In fact, the information provided by a confidence interval can be formally related to the information provided by a hypothesis test. (*Comment:* The relationship is more straightforward for two-sided alternatives, and so we will not present results for the one-sided cases.)

Suppose we want to carry out the *two-sided test:*

```{figure} images/image299.gif
:alt: H_0: p = p_0 and H_a: p ≠ p_0

H_0: p = p_0 and H_a: p ≠ p_0
```

using a significance level of .05.

An alternative way to perform this test is to find a 95% *confidence interval* for p and check:

If $p_{0}$ falls*outside* the confidence interval, *reject*H~o~.

If $p_{0}$ falls *inside* the confidence interval, *do not reject*H~o~.

In other words, if $p_{0}$ is not one of the plausible values for p, we reject H~o~.

If $p_{0}$ is a plausible value for p, we cannot reject H~o~.

(*Comment:* Similarly, the results of a test using a significance level of .01 can be related to the 99% confidence interval.)

Let's look at two examples:

```{admonition} Example
    Recall example 3, where we wanted to know whether the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003, when it was .64.

    ```{figure} images/image223.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we want to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat =675/1000 = .675.

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we want to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor. p-hat =675/1000 = .675.
    ```

    We are testing:

    ```{figure} images/image300.gif
    :alt: H_0: p = .64 and H_a: p ≠ .64;

    H_0: p = .64 and H_a: p ≠ .64;
    ```

    and as the figure reminds us, we took a sample of 1,000 U.S. adults, and the data told us that 675 supported the death penalty for convicted murderers (i.e. $\hat{p}=.675$).

    A 95% confidence interval for p, the proportion of *all* U.S. adults who support the death penalty, is:

    $.675\pm2\sqrt{\frac{.675\left(1−.675\right)}{1000}}\approx.675\pm.03=\left(.645, .705\right)$

    Since the 95% confidence interval for p does not include .64 as a plausible value for p, we can reject H~o~ and conclude (as we did before) that the proportion of U.S. adults who support the death penalty for convicted murderers has changed since 2003.

    ```{figure} images/image302.gif
    :alt: A number line illustrating the 95% confidence interval for p. The interval is (.645, .705). In H_0, p = .64, which is outside of this interval, so we can reject H_0: p = .64 .

    A number line illustrating the 95% confidence interval for p. The interval is (.645, .705). In H_0, p = .64, which is outside of this interval, so we can reject H_0: p = .64 .
    ```
```

```{admonition} Example
    You and your roommate are arguing about whose turn it is to clean the apartment. Your roommate suggests that you settle this by tossing a coin and takes one out of a locked box he has on the shelf. Suspecting that the coin might not be fair, you decide to test it first. You toss the coin 80 times, thinking to yourself that if, indeed, the coin is fair, you should get around 40 heads. Instead you get 48 heads. You are puzzled. You are not sure whether getting 48 heads out of 80 is enough evidence to conclude that the coin is unbalanced, or whether this a result that could have happened just by chance when the coin is fair.

    Statistics can help you answer this question.

    Let p be the true proportion (probability) of heads. We want to test whether the coin is fair or not:

    ```{figure} images/image303.gif
    :alt: H_0: p = .5, H_a: p ≠ .5

    H_0: p = .5, H_a: p ≠ .5
    ```

    The data we have are that out of n=80 tosses, we got 48 heads, or that the sample proportion of heads is:$\hat{p}=\frac{48}{80}=.6$

    The 95% confidence interval for p, the true proportion of heads for this coin, is:

    $.6\pm2⋅\sqrt{\frac{.6\left(1−.6\right)}{80}}\approx.6\pm.11=\left(.49, .71\right)$

    Since in this case .5 is one of the plausible values for p, we cannot reject H~o~. In other words, the data do not provide enough evidence to conclude that the coin is not fair.

    ```{figure} images/image306.gif
    :alt: A number line showing the 95% confidence interval for p, which is (.49, .71). H_0 is p = .5, which falls within this interval, so we cannot reject H_0: p = .5 .

    A number line showing the 95% confidence interval for p, which is (.49, .71). H_0 is p = .5, which falls within this interval, so we cannot reject H_0: p = .5 .
    ```
```

##### Did I Get This?

The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. A study was designed in order to examine whether that proportion has changed since. Let p be the proportion of all Internet users who are concerned about credit card fraud. In this study we are therefore testing:

```{figure} images/image390.gif
:alt: H_0: p = .087, H_a: p ≠ .087

H_0: p = .087, H_a: p ≠ .087
```

Based on the collected data, a 95% confidence interval for p was found to be (.08, .14).

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

The UCLA Internet Report (February 2003) estimated that roughly 60.5% of U.S. adults use the Internet at work for personal use. A follow-up study was conducted in order to explore whether that figure has changed since. Let p be the proportion of U.S. adults who use the Internet at work for personal use.

```{figure} images/image391.gif
:alt: H_0: p = .605, H_a: p ≠ .605

H_0: p = .605, H_a: p ≠ .605
```

Based on the collected data, the p-value of the test was found to be .001.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on. If not, then click the link below for some additional practice.

```{note}
    **Sectionnest**

    Hypothesis Testing for the Population Proportion p (extra problems)

    *(Interactive activity — available in the OLI platform)*
```

## Comment

The context of the last example is a good opportunity to bring up an important point that was discussed earlier.

Even though we use .05 as a cutoff to guide our decision about whether the results are significant, we should not treat it as inviolable and we should always add our own judgment. Let's look at the last example again.

It turns out that the p-value of this test is .0734. In other words, it is maybe not extremely unlikely, but it is quite unlikely (probability of .0734) that when you toss a *fair* coin 80 times you'll get a sample proportion of heads of 48/80=.6 (or even more extreme). It is true that using the .05 significance level (cutoff), .0734 is not considered small enough to conclude that the coin is not fair. However, if you really don't want to clean the apartment, the p-value might be small enough for you to ask your roommate to use a different coin, or to provide one yourself!
