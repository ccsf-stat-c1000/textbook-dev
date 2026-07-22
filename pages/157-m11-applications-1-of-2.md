# Normal Applications: From Values to Probabilities

## Working with Non-standard Normal Values

In a much earlier example, we wondered, "How likely or unlikely is a male foot length of more than 13 inches?" We were unable to solve the problem, because 13 inches didn't happen to be one of the values featured in the Standard Deviation Rule. Subsequently, we learned how to standardize a normal value (tell how many standard deviations below or above the mean it is) and how to use the normal table to find the probability of falling in an interval a certain number of standard deviations below or above the mean. By combining these two skills, we will now be able to answer questions like the one above.

:::{admonition} Example: Male Foot Length
:class: tip

1. Male foot lengths have a normal distribution, with $\mu=11, \sigma=1.5$ inches. What is the probability of a foot length of more than 13 inches?

   First, we standardize: $z=\frac{x-\mu}{\sigma}=\frac{13-11}{1.5}=+1.33$. The probability that we seek, P(X > 13), is the same as the probability P(Z > +1.33) that a normal variable takes a value greater than 1.33 standard deviations above its mean. This can be solved with the normal table, after applying the property of symmetry: P(Z > +1.33) = P(Z < −1.33) = 0.0918. A male foot length of more than 13 inches is on the long side, but not too unusual: its probability is about 9%.

   *Comment:* We can streamline the solution in terms of probability notation:

   $$P(X>13)=P(Z>1.33)=P(Z<-1.33)=0.0918$$

   The first equality holds because we subtracted the mean from a normal variable X and divided by its standard deviation, transforming it to a standardized normal variable that we call "Z." The second equality holds by the symmetry of the standard normal curve around zero. The last equality was obtained from the normal table.

2. What is the probability of a male foot length between 10 and 12 inches?

   The standardized values of 10 and 12 are, respectively, $\frac{10-11}{1.5}=-0.67$ and $\frac{12-11}{1.5}=+0.67$.

   $$P(10<X<12)=P(-0.67<Z<+0.67)=P(Z<+0.67)-P(Z<-0.67)=0.7486-0.2514=0.4972$$
:::

```{admonition} Comment
:class: important

By solving the above example, we inadvertently discovered the quartiles of a normal distribution! P(Z < −0.67) = 0.2514 tells us that roughly 25%, or one quarter, of a normal variable's values are less than 0.67 standard deviations below the mean. P(Z < +0.67) = 0.7486 tells us that roughly 75%, or three quarters, are less than 0.67 standard deviations above the mean. And of course the median is equal to the mean, since the distribution is symmetric: the median is 0 standard deviations away from the mean.
```

:::{admonition} Example: Length of a Human Pregnancy
:class: tip

Length (in days) of a randomly chosen human pregnancy is a normal random variable with $\mu=266, \sigma=16$.

1. Find Q1, the median, and Q3. Q1 = 266 − 0.67(16) ≈ 255; median = mean = 266; Q3 = 266 + 0.67(16) ≈ 277. Thus, the probability is 1/4 that a pregnancy will last less than 255 days; 1/2 that it will last less than 266 days; 3/4 that it will last less than 277 days.

2. What is the probability that a randomly chosen pregnancy will last less than 246 days? Since (246 − 266)/16 = −1.25, we write $P(X<246)=P(Z<-1.25)=0.1056$.

3. What is the probability that a randomly chosen pregnancy will last longer than 240 days? Since (240 − 266)/16 = −1.63, we write $P(X>240)=P(Z>-1.63)=P(Z<+1.63)=0.9484$. Since the mean is 266 and the standard deviation is 16, most pregnancies last longer than 240 days.

4. What is the probability that a randomly chosen pregnancy will last longer than 500 days? *Method 1:* Common sense tells us that this would be impossible. *Method 2:* The standardized value of 500 is (500 − 266)/16 = +14.625, and $P(X>500)=P(Z>14.625)=0$ (approx.).

5. Suppose a pregnant woman's husband has scheduled his business trips so that he will be in town between the 235th and 295th days. What is the probability that the birth will take place during that time? The standardized values are (235 − 266)/16 = −1.94 and (295 − 266)/16 = +1.81.

   $$P(235<X<295)=P(-1.94<Z<+1.81)=P(Z<+1.81)-P(Z<-1.94)=0.9649-0.0262=0.9387$$

   There is close to a 94% chance that the husband will be in town for the birth.
:::

The purpose of the next activity is to give you guided practice at solving word problems that involve normal random variables. In particular, we'll solve problems like the examples you just went over, in which you are asked to find the probability that a normal random variable falls within a certain interval.

## Check Your Understanding: Finding Normal Probabilities

According to the College Board website, the scores on the math part of the SAT (SAT-M) in a certain year had a mean of 507 and standard deviation of 111. Assume that SAT scores follow a normal distribution.

:::{quiz} What is the probability that a randomly chosen test taker scored above 700 on the SAT-M?
:hint: Standardize first: z = (700 − 507)/111 ≈ 1.74, then find the upper-tail probability.
:feedback-0: Correct! P(X > 700) = P(Z > 1.74) = P(Z < −1.74) = 0.0409—about a 4% chance.
:feedback-1: 0.9591 is P(Z < 1.74), the probability of scoring BELOW 700.
:feedback-2: 1.74 is the z-score, not the probability.
* *About 0.04
* About 0.96
* 1.74
:::

:::{quiz} What is the probability that a randomly chosen test taker scored between 400 and 600?
:hint: Standardize both: z = (400 − 507)/111 ≈ −0.96 and z = (600 − 507)/111 ≈ 0.84; then subtract left-tail areas (0.7995 − 0.1685).
:feedback-0: Correct! P(400 < X < 600) = P(Z < 0.84) − P(Z < −0.96) = 0.7995 − 0.1685 = 0.631.
:feedback-1: 0.80 is only P(Z < 0.84); you must remove the area below 400.
:feedback-2: Adding the two left-tail areas has no probability meaning here—subtract them.
* *About 0.63
* About 0.80
* About 0.97
:::
