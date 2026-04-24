# Overview (4 of 4)

```{admonition} Learning Objectives
    - Explain the logic behind and the process of hypotheses testing. In particular, explain what the p-value is and how it is used to draw conclusions.
```

*Hypothesis testing step 4: Making conclusions.*

Since our conclusion is based on how small the p-value is, or in other words, how surprising our data are when H~o~ is true, it would be nice to have some kind of guideline or cutoff that will help determine how small the p-value must be, or how "rare" (unlikely) our data must be when H~o~ is true, for us to conclude that we have enough evidence to reject H~o~.

This cutoff exists, and because it is so important, it has a special name. It is called the *significance level of the test* and is usually denoted by the Greek letter α. The most commonly used significance level is α = .05 (or 5%). This means that:

- if the p-value < α (usually .05), then the data we got is considered to be "rare
                (or surprising) enough" when H ~o~ is true, and we say that the data provide
                significant evidence against H ~o~ , so we reject H ~o~ and accept
                    H ~a~ .
- if the p-value > α (usually .05), then our data are not considered to be
                "surprising enough" when H ~o~ is true, and we say that our data do not
                provide enough evidence to reject H ~o~ (or, equivalently, that the data do
                not provide enough evidence to accept H ~a~ ).

*Important comment about wording.*

Another common wording (mostly in scientific journals) is:

"The results are statistically significant" - when the p-value < α.

"The results are not statistically significant" - when the p-value > α.

## Comments

1. Although the significance level provides a good guideline for drawing
                            our conclusions, it should not be treated as an incontrovertible
                            truth.
                            There is a lot of room for personal interpretation. What if your p-value
                            is .052? You might want to stick to the rules and say ".052 > .05 and
                            therefore I don't have enough evidence to reject H~o~", but you
                            might decide that .052 is small enough for you to believe that
                                H~o~ should be rejected. It should be noted that
                            scientific journals do consider .05 to be the cutoff point for which any
                            p-value below the cutoff indicates enough evidence against
                            H~o~, and any p-value above it, *or even
                                equal to it*, indicates there is not enough evidence against
                                H~o~.
2. It is important to draw your conclusions *in context*. It is
                                *never enough* to say: *"p-value = ..., and
                                therefore I have enough evidence to reject H~o~ at the .05
                                significance level."*You *should always add:* "... and
                            conclude that ... (what it means in the context of the problem)".
3. Let's go back to the issue of the nature of the two types of conclusions
                            that I can make. *Either*
*I reject H~o~ and accept H~a~ (when
                                the p-value is smaller than the significance level)*
*or*
*I cannot reject H~o~ (when the p-value is
                                larger than the significance level).*

As we mentioned earlier, note that the second conclusion does not imply that I accept H~o~, but just that I don't have enough evidence to reject it. Saying (by mistake) "I don't have enough evidence to reject H~o~ so I accept it" indicates that the data provide evidence that H~o~ is true, which is *not necessarily the case*. Consider the following slightly artificial yet effective example:

```{admonition} Example
    An employer claims to subscribe to an "equal opportunity" policy, not hiring men any more often than women for managerial positions. Is this credible? You're not sure, so you want to test the following *two hypotheses:*

    - *H~o~:* The proportion of male managers hired is
                                    .5
    - *H~a~:* The proportion of male managers hired is
                                    more than .5

    *Data:* You choose at random three of the new managers who were hired in the last 5 years and find that all 3 are men.

    *Assessing Evidence:* If the proportion of male managers hired is really .5 (H~o~ is true), then the probability that the random selection of three managers will yield three males is therefore .5 * .5 * .5 = .125. This is the p-value.

    *Conclusion:* Using .05 as the significance level, you conclude that since the p-value = .125 > .05, the fact that the three randomly selected mangers were all males is not enough evidence to reject H~o~. In other words, you do not have enough evidence to reject the employer's claim of subscribing to an equal opportunity policy.

    However, *the data (all three selected are males) definitely does not provide evidence to accept the employer's claim (H~o~).*
```

## Learn By Doing

The following two hypotheses are tested:

- H~o~: The proportion of U.S. adults who oppose gay marriage is
                            roughly 50%.
- H~a~: The proportion of U.S. adults who oppose gay marriage is
                            above 50% (i.e., the majority oppose).

Suppose a survey was conducted in which a random sample of 1,100 U.S. adults was asked about their opinions about gay marriage, and based on the data, the p-value was found to be .002.

Comment: Throughout this activity use a .05 (5%) significance level (cutoff).

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

The following two hypotheses are tested:

- H~o~: The average number of miles driven per year is 12,000.
- H~a~: The average number of miles driven per year is less than
                            12,000.

In a survey, 1,600 randomly selected drivers were asked the number of miles they drive yearly. Based upon the results, the p-value = .068.

Comment: Throughout this activity use a .05 (5%) significance level.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
