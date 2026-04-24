# Standard Normal Table (3 of 3)

```{admonition} Learning Objectives
    - Find probabilities associated with the normal distribution.
```

## Comment

So far, we have used the normal table to find a probability, given the number (z) of standard deviations below or above the mean. The solution process involved first locating the given z value of the form *.** in the margins, then finding the corresponding probability of the form .**** inside the table as our answer. Now, in Example 2, a probability will be given and we will be asked to find a z value. The solution process involves first locating the given probability of the form .**** inside the table, then finding the corresponding z value of the form *.** as our answer.

```{admonition} Example
    (a) The probability is .01 that a standardized normal variable takes a value below what particular value of z?

    The closest we can come to a probability of .01 inside the table is .0099, in the z = -2.3 row and .03 column: z = -2.33. In other words, the probability is .01 that the value of a normal variable is lower than 2.33 standard deviations below its mean.

    | z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | -2.5 | .0062 | .0060 | .0059 | .0057 | .0055 | .0054 | .0052 | .0051 | .0049 | .0048 |
    | -2.4 | .0082 | .0080 | .0078 | .0075 | .0073 | .0071 | .0069 | .0068 | .0066 | .0064 |
    | -2.3 | .0107 | .0104 | .0102 | .0099 | .0096 | .0094 | .0091 | .0089 | .0087 | .0084 |
    | -2.2 | .0139 | .0136 | .0132 | .0129 | .0125 | .0122 | .0119 | .0116 | .0113 | .0110 |
    | -2.1 | .0179 | .0174 | .0170 | .0166 | .0162 | .0158 | .0154 | .0150 | .0146 | .0143 |

    ```{figure} images/image145.gif
    :alt: A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis is a z-scores of -2.33 . The area under the curve to the left of -2.33 is .01.

    A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis is a z-scores of -2.33 . The area under the curve to the left of -2.33 is .01.
    ```

    (b) The probability is .15 that a standardized normal variable takes a value *above* what particular value of z?

    Remember that the table only provides probabilities of being *below* a certain value, not above. Once again, we must rely on one of the properties of the normal curve to make an adjustment.

    *Method 1:* According to the table, .15 (actually .1492) is the probability of being *below* -1.04. By symmetry, .15 must also be the probability of being *above* +1.04.

    | z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | -1.2 | .1151 | .1131 | .1112 | .1093 | .1075 | .1056 | .1038 | .1020 | .1003 | .0985 |
    | -1.1 | .1357 | .1335 | .1314 | .1292 | .1271 | .1251 | .1230 | .1210 | .1190 | .1170 |
    | -1.0 | .1587 | .1562 | .1539 | .1515 | .1492 | .1469 | .1446 | .1423 | .1401 | .1379 |
    | -0.9 | .1841 | .1814 | .1788 | .1762 | .1736 | .1711 | .1685 | .1660 | .1635 | .1611 |
    | -0.8 | .2119 | .2090 | .2061 | .2033 | .2005 | .1977 | .1949 | .1922 | .1894 | .1867 |

    ```{figure} images/image147.gif
    :alt: A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis are z-scores of -1.04 and 1.04 . The area under the curve to the left of -1.04 is .15, and since the curve is symmetric, the area under the curve to the right of 1.04 is also .15.

    A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis are z-scores of -1.04 and 1.04 . The area under the curve to the left of -1.04 is .15, and since the curve is symmetric, the area under the curve to the right of 1.04 is also .15.
    ```

    *Method 2:* If .15 is the probability of being above the value we seek, then 1 - .15 = .85 must be the probability of being below the value we seek. According to the table, .85 (actually .8508) is the probability of being below +1.04.

    ```{figure} images/image148.gif
    :alt: A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis is a z-score of 1.04. The area under the curve to the right of 1.04 is .15. Knowing this we can calculate the area to the left of 1.04, which is 1-.15 = .85 .

    A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis is a z-score of 1.04. The area under the curve to the right of 1.04 is .15. Knowing this we can calculate the area to the left of 1.04, which is 1-.15 = .85 .
    ```

    In other words, we have found .15 to be the probability that a normal variable takes a value more than 1.04 standard deviations above its mean.

    (c) The probability is .95 that a normal variable takes a value within how many standard deviations of its mean?

    A symmetric area of .95 centered at 0 extends to values -z* and +z* such that the remaining (1 - .95) / 2 = .025 is below -z* and also .025 above +z*. The probability is .025 that a standardized normal variable is below -1.96. Thus, the probability is .95 that a normal variable takes a value within 1.96 standard deviations of its mean. Once again, the Standard Deviation Rule is shown to be just roughly accurate, since it states that the probability is .95 that a normal variable takes a value within 2 standard deviations of its mean.

    ```{figure} images/image149.gif
    :alt: A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis are z-scores of 1.96 and -1.96 . The area under the curve between these two z-scores is .95 . Since the curve is symmetric, we can calculate the area to the left of -1.96 , which is (1-.95/2 = .025 . The area to the right of 1.96 is the same.

    A normal probability distribution curve with its horizontal axis representing z-scores . Marked on the axis are z-scores of 1.96 and -1.96 . The area under the curve between these two z-scores is .95 . Since the curve is symmetric, we can calculate the area to the left of -1.96 , which is (1-.95/2 = .025 . The area to the right of 1.96 is the same.
    ```
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

Our standard normal table, like most, only provides probabilities for z values between -3.49 and +3.49. The following example demonstrates how to handle cases where z exceeds 3.49 in absolute value.

```{admonition} Example
    *(a)* What is the probability of a normal variable being lower than 5.2 standard deviations below its mean?

    There is no need to panic about going "off the edge" of the normal table. We already know from the Standard Deviation Rule that the probability is only about (1 - .997) / 2 = .0015 that a normal value would be more than 3 standard deviations away from its mean in one direction or the other. The table provides information for z values as extreme as plus or minus 3.49: the probability is only .0002 that a normal variable would be lower than 3.49 standard deviations below its mean. Any more standard deviations than that, and we generally say the probability is approximately zero.

    In this case, we would say the probability of being lower than 5.2 standard deviations below the mean is approximately zero:

    P(Z < -5.2) = 0 (approx.)

    *(b)* What is the probability of the value of a normal variable being higher than 6 standard deviations below its mean?

    Since the probability of being lower than 6 standard deviations below the mean is approximately zero, the probability of being higher than 6 standard deviations below the mean must be approximately 1. P(Z > -6) = 1 (approx.)

    *(c)* What is the probability of a normal variable being less than 8 standard deviations above the mean? Approximately 1. P(Z < +8) = 1 (approx.)

    *(d)* What is the probability of a normal variable being greater than 3.5 standard deviations above the mean? Approximately 0. P(Z > +3.5) = 0 (approx.)
```
