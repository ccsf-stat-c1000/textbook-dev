# Applications (1 of 2)

```{admonition} Learning Objectives
    - Find probabilities associated with the normal distribution.
```

## Working with Non-standard Normal Values

In a much earlier example, we wondered,

"How likely or unlikely is a male foot length of more than 13 inches?" We were unable to solve the problem, because 13 inches didn't happen to be one of the values featured in the Standard Deviation Rule. Subsequently, we learned how to standardize a normal value (tell how many standard deviations below or above the mean it is) and how to use the normal table to find the probability of falling in an interval a certain number of standard deviations below or above the mean. By combining these two skills, we will now be able to answer questions like the one above.

```{admonition} Example: Male Foot Length
    1. Male foot lengths have a normal distribution, with $\mu=11,\sigma=1.5$ inches. What is the probability of a foot length of more than 13
                            inches? First, we standardize: $z=\frac{x-\mu}{\sigma}=\frac{13-11}{1.5}=+1.33$; the probability that we seek, P(X > 13), is the same as the
                            probability P(Z > +1.33) that a normal variable takes a value greater than 1.33 standard deviations above its mean. This can be solved with the normal table, after applying the property of symmetry: P(Z > +1.33) = P(Z < -1.33) = .0918. A male foot length of more than 13 inches is on the
                            long side, but not too unusual: its probability is about 9%. *Comment:* We can streamline the solution in terms of probability notation. Since the standardized value
                                    for 13 is (13 - 11) / 1.5 = +1.33, we can write $P(X>13)=P(Z>1.33)=P(Z<-1.33)=0.0918$. The first equality above holds because we subtracted the mean from a normal variable X and
                            divided by its standard deviation, transforming it to a standardized normal
                            variable that we call "Z." The second equality above holds by the symmetry of the standard normal curve around zero. The last equality above was obtained from the normal table.
    2. What is the probability of a male foot length between 10 and 12 inches? The standardized values of 10 and 12 are, respectively, $\frac{10-11}{1.5}=-0.67$ and $\frac{12-11}{1.5}=0.67$. P(-.67 < Z < +.67) = P(Z < +.67) - P(Z < -.67) = .7486 - .2514 = .4972. Or, if you prefer the
                            streamlined
                            notation, $P(10<X<12)=P(-0.67<Z<+0.67)=P(Z<+0.67)-P(Z<-0.67)=0.7486-0.2514=0.4972$.
```

## Comment

By solving the above example, we inadvertently discovered the quartiles of a normal distribution! P(Z < -.67) = .2514 tells us that roughly 25%, or one quarter, of a normal variable's values are less than .67 standard deviations below the mean. P(Z < +.67) = .7486 tells us that roughly 75%, or three quarters, are less than .67 standard deviations above the mean. And of course the median is equal to the mean, since the distribution is symmetric, the median is 0 standard deviations away from the mean.

```{figure} images/image160.gif
:alt: A normal probability distribution curve which has a horizontal axis in z-score units. The first quartile is at Z=-.67 . To the left of this, under the curve, is an area of .25 . The second quartile, is at Z=0, the median. To the left of this is an area of .50 under the curve. The third quartile is Z=.67, and to the left is .75 area. To the right of the third quartile is the remaining .25 of area.

A normal probability distribution curve which has a horizontal axis in z-score units. The first quartile is at Z=-.67 . To the left of this, under the curve, is an area of .25 . The second quartile, is at Z=0, the median. To the left of this is an area of .50 under the curve. The third quartile is Z=.67, and to the left is .75 area. To the right of the third quartile is the remaining .25 of area.
```

```{admonition} Example: Length of a Human Pregnancy
    Length (in days) of a randomly chosen human pregnancy is a normal random variable with $\mu=266,\sigma=16$

    1. Find Q1, the median, and Q3. Q1 = 266 - .67(16) = 255; median = mean = 266; Q3 = 266 + .67(16) = 277. Thus, the probability is 1/4 that a pregnancy will last less than 255 days; 1/2 that it will last less than 266 days; 
        3/4 that it will last less than 277 days.
    2. What is the probability that a randomly chosen pregnancy will last less than 246 days? Since (246 - 266) / 16 = -1.25, we write $P(X<246)=P(Z<-1.25)=0.1056$
    3. What is the probability that a randomly chosen pregnancy will last longer than 240 days? Since (240 - 266) / 16 = -1.63, we write $P(X>240)=P(Z>-1.63)=P(Z<+1.63)=0.9484$ Since the mean is 266 and the standard deviation is 16, most pregnancies last longer than 240 days.
    4. What is the probability that a randomly chosen pregnancy will last longer than 500 days? *Method 1:* Common sense tells us that this would be impossible. *Method 2:* The standardized value of 500 is (500 - 266) / 16 = +14.625. $P(X>500)=P(Z>14.625)=0$.
    5. Suppose a pregnant woman's husband has scheduled his business trips so that he will
                            be in town between the 235th and 295th days. What is the probability that
                            the birth will take place during that time? The standardized values are (235
                            - 266) / 16) = -1.94 and (295 - 266) / 16 = +1.81. $P(235<X<295)=P(-1.94<Z<+1.81)=P(Z<+1.81)-P(Z<-1.94)=0.9649-0.0262=0.9387$ There is close to a 94% chance that the husband will be in town for the birth.
```

The purpose of the next activity is to give you guided practice at solving word problems that involve normal random variables. In particular, we'll solve problems like the examples you just went over, in which you are asked to find the probability that a normal random variable falls within a certain interval.

##### Learn By Doing

According to the College Board website, the scores on the math part of the SAT (SAT-M) in a certain year had a mean of 507 and standard deviation of 111. Assume that SAT scores follow a normal distribution.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
