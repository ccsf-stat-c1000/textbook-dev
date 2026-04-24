# Hypothesis Testing for the Population Proportion p (2 of 13)

```{admonition} Learning Objectives
    - In a given context, specify the null and alternative hypotheses for the population proportion and mean.
```

Recall that there are basically 4 steps in the process of hypothesis testing:

1. State the null and alternative hypotheses.

2. Collect relevant data from a random sample and summarize them (using a test statistic).

3. Find the p-value, the probability of observing data like those observed assuming that H~o~ is true.

4. Based on the p-value, decide whether we have enough evidence to reject H~o~ (and accept H~a~), and draw our conclusions in context.

We are now going to go through these steps as they apply to the hypothesis testing for the population proportion p. It should be noted that even though the details will be specific to this particular test, some of the ideas that we will add apply to hypothesis testing in general.

## 1. Stating the Hypotheses

Here again are the three set of hypotheses that are being tested in each of our three examples:

```{admonition} Example: 1
    Has the proportion of defective products been reduced as a result of the repair?

    *H*~*o*~*:* p = .20 (No change; the repair did not help).

    *H*~*a*~*:* p < .20 (The repair was effective).
```

```{admonition} Example: 2
    Is the proportion of marijuana users in the college higher than the national figure?

    *H*~*o*~*:* p = .157 (Same as among all college students in the country).

    *H*~*a*~*:* p > .157 (Higher than the national figure).
```

```{admonition} Example: 3
    Did the proportion of U.S. adults who support the death penalty changebetween 2003 and a later poll?

    *H*~*o*~*:* p =.64 (No change from 2003).

    *H*~*a*~*:* p ≠.64 (Some change since 2003).
```

Note that the null hypothesis always takes the form:

H~o~: p = some value

and the alternative hypothesis takes one of the following three forms:

H~a~: p < that value (like in example 1) *or*

H~a~: p > that value (like in example 2) *or*

H~a~: p ≠ that value (like in example 3).

Note that it was quite clear from the context which form of the alternative hypothesis would be appropriate. The value that is specified in the null hypothesis is called the *null value*, and is generally denoted by p~o~. We can say, therefore, that in general the null hypothesis about the population proportion (p) would take the form:

H~o~: p = p~o~

We write H~o~: p = p~o~ to say that we are making the hypothesis that the population proportion has the value of p~o~. In other words, p is the unknown population proportion and p~o~ is the number we think p might be for the given situation.

The alternative hypothesis takes one of the following three forms (depending on the context):

H~a~: p < p~o~*(one-sided)*

H~a~: p > p~o~*(one-sided)*

H~a~: p ≠ p~o~*(two-sided)*

The first two possible forms of the alternatives (where the = sign in H~o~ is challenged by < or >) are called *one-sided alternatives*, and the third form of alternative (where the = sign in H~o~ is challenged by ≠) is called a*two-sided alternative.* To understand the intuition behind these names let's go back to our examples.

Example 3 (death penalty) is a case where we have a two-sided alternative:

*H*~*o*~*:* p =.64 (No change from 2003).

*H*~*a*~*:* p ≠.64 (Some change since 2003).

In this case, in order to reject H~o~ and accept H~a~ we will need to get a sample proportion of death penalty supporters which is very different from .64 *in either direction,* either much larger or much smaller than .64.

In example 2 (marijuana use) we have a one-sided alternative:

*H*~*o*~*:* p = .157 (Same as among all college students in the country).

*H*~*a*~*:* p > .157 (Higher than the national figure).

Here, in order to reject H~o~ and accept H~a~ we will need to get a sample proportion of marijuana users which is much *higher* than .157.

Similarly, in example 1 (defective products), where we are testing:

*H*~*o*~*:* p = .20 (No change; the repair did not help).

*H*~*a*~*:* p < .20 (The repair was effective).

in order to reject H~o~ and accept H~a~, we will need to get a sample proportion of defective products which is much *smaller* than .20.

##### Learn By Doing

In each of the following examples, a test for the population proportion (p) is called for. You are asked to select the right null and alternative hypotheses.

*Scenario 1:*The UCLA Internet Report (February 2003) estimated that roughly 8.7% of Internet users are extremely concerned about credit card fraud when buying online. Has that figure changed since? To test this, a random sample of 100 Internet users was chosen, and when interviewed, 10 said that they were extremely worried about credit card fraud when buying online. Let p be the proportion of all Internet users who are concerned about credit card fraud.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 2:*The UCLA Internet Report (February 2003) estimated that a proportion of roughly .75 of online homes are still using dial-up access, but claimed that the use of dial-up is declining. Is that really the case? To examine this, a follow-up study was conducted a year later in which out of a random sample of 1,308 households that had Internet access, 804 were connecting using a dial-up modem. Let p be the proportion of all U.S. Internet-using households that have dial-up access.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 3:*According to the UCLA Internet Report (February 2003) the use of the Internet at home is growing steadily and it is estimated that roughly 59.3% of households in the United States have Internet access at home. Has that trend continued since the report was released? To study this, a random sample of 1,200 households from a big metropolitan area was chosen for a more recent study, and it was found that 972 had an Internet connection. Let p be the proportion of U.S. households that have internet access.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

##### Did I Get This?

In each of the following examples, a test for the population proportion (p) is called for. You are asked to select the right null and alternative hypotheses.

*Scenario 1:* When shirts are made, there can occasionally be defects (such as improper stitching). But too many such defective shirts can be a sign of substandard manufacturing.

Suppose, in the past, your favorite department store has had only one defective shirt per 200 shirts (a prior defective rate of only .005). But you suspect that the store has recently switched to a substandard manufacturer. So you decide to test to see if their overall proportion of defective shirts today is higher.

Suppose that, in a random sample of 200 shirts from the store, you find that 27 of them are defective, for a sample proportion of defective shirts of .135. You want to test whether this is evidence that the store is "guilty" of substandard manufacturing, compared to their prior rate of defective shirts.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 2:* It is a known medical fact that just slightly fewer females than males are born (although the reasons are not completely understood); the known "proper" baseline female birthrate is about 49% females.

In some cultures, male children are traditionally looked on more favorably than female children, and there is concern that the increasing availability of ultrasound may lead to pregnant mothers deciding to abort the fetus if it’s not the culturally "desired" gender. If this is happening, then the proportion of females in those nations would be significantly lower than the proper baseline rate.

To test whether the proportion of females born in India is lower than the proper baseline female birthrate, a study investigates a random sample of 6,500 births from hospital files in India, and finds 44.8% females born among the sample.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

*Scenario 3:* A properly-balanced 6-sided game die should give a 1 in exactly 1/6 (16.7%) of all rolls. A casino wants to test its game die. If the die is not properly balanced one way or another, it could give either too many 1’s or too few 1’s, either of which could be bad.

The casino wants to use the proportion of 1’s to test whether the die is out of balance. So the casino test-rolls the die 60 times and gets a 1 in 9 of the rolls (15%).

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
