# Reading the Standard Normal Table

```{admonition} Learning Objectives
:class: note

- Find probabilities associated with the normal distribution.
```

## Finding Probabilities with the Normal Table

Now that you have learned to assess the relative value of any normal value by standardizing, the next step is to evaluate probabilities. As mentioned before, we will first take the conventional approach of referring to a *normal table*, which tells the probability of a normal variable taking a value *less than* any standardized score z. (A complete standard normal table appears in most statistics references, and your instructor can provide one; statistical software and calculators give these probabilities directly.)

Since normal curves are symmetric about their mean, it follows that the curve of z scores must be symmetric about 0. Since the total area under any normal curve is 1, it follows that the areas on either side of z = 0 are both 0.5. Also, according to the Standard Deviation Rule, most of the area under the standardized curve falls between z = −3 and z = +3.

The normal table outlines the precise behavior of the standard normal random variable Z, the number of standard deviations a normal value x is below or above its mean. The normal table provides probabilities that a standardized normal random variable Z would take a value less than or equal to a particular value z*.

These particular values are listed in the form *.* in rows along the left margins of the table, specifying the ones and tenths. The columns fine-tune these values to hundredths, allowing us to look up the probability of being below any standardized value z of the form *.**. Here is part of the table.

| z | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -3.4 | .0003 | .0003 | .0003 | .0003 | .0003 | .0003 | .0003 | .0003 | .0003 | .0002 |
| -3.3 | .0005 | .0005 | .0005 | .0004 | .0004 | .0004 | .0004 | .0004 | .0004 | .0003 |
| -3.2 | .0007 | .0007 | .0006 | .0006 | .0006 | .0006 | .0006 | .0005 | .0005 | .0005 |
| -3.1 | .0010 | .0009 | .0009 | .0009 | .0008 | .0008 | .0008 | .0008 | .0007 | .0007 |
| -3.0 | .0013 | .0013 | .0013 | .0012 | .0012 | .0011 | .0011 | .0011 | .0010 | .0010 |
| -2.9 | .0019 | .0018 | .0018 | .0017 | .0016 | .0016 | .0015 | .0015 | .0014 | .0014 |
| -2.8 | .0026 | .0025 | .0024 | .0023 | .0023 | .0022 | .0021 | .0021 | .0020 | .0019 |
| -2.7 | .0035 | .0034 | .0033 | .0032 | .0031 | .0030 | .0029 | .0028 | .0027 | .0026 |
| -2.6 | .0047 | .0045 | .0044 | .0043 | .0041 | .0040 | .0039 | .0038 | .0037 | .0036 |
| -2.5 | .0062 | .0060 | .0059 | .0057 | .0055 | .0054 | .0052 | .0051 | .0049 | .0048 |
| -2.4 | .0082 | .0080 | .0078 | .0075 | .0073 | .0071 | .0069 | .0068 | .0066 | .0064 |
| -2.3 | .0107 | .0104 | .0102 | .0099 | .0096 | .0094 | .0091 | .0089 | .0087 | .0084 |
| -2.2 | .0139 | .0136 | .0132 | .0129 | .0125 | .0122 | .0119 | .0116 | .0113 | .0110 |
| -2.1 | .0179 | .0174 | .0170 | .0166 | .0162 | .0158 | .0154 | .0150 | .0146 | .0143 |

By construction, the probability P(Z < z*) equals the area under the z curve to the left of that particular value z*.

```{figure} images/gen/m11-z-left-shaded.svg
:alt: A standard normal curve with a value z-star marked on the axis and the entire area under the curve to the left of z-star shaded. The shaded area equals the probability that Z is less than z-star.
```

A quick sketch is often the key to solving normal problems easily and correctly.

## Concept Check

:::{quiz} Using the excerpt of the normal table above, what is P(Z < −2.25)?
:hint: Find the row for −2.2 and the column for .05.
:feedback-0: Correct! The −2.2 row and .05 column give 0.0122.
:feedback-1: 0.0139 is P(Z < −2.20); the extra hundredths matter—use the .05 column.
:feedback-2: 0.9878 would be P(Z > −2.25), the complement.
* *0.0122
* 0.0139
* 0.9878
:::
