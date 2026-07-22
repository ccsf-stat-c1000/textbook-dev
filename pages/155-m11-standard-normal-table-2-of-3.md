# Finding Probabilities from the Table

:::{admonition} Example: Reading the Table
:class: tip

*(a)* What is the probability of a normal random variable taking a value less than 2.8 standard deviations above its mean? According to the table, P(Z < 2.8) = 0.9974 or 99.74%.

| z | 0.00 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 | 0.07 | 0.08 | 0.09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.5 | 0.9938 | 0.9940 | 0.9941 | 0.9943 | 0.9945 | 0.9946 | 0.9948 | 0.9949 | 0.9951 | 0.9952 |
| 2.6 | 0.9953 | 0.9955 | 0.9956 | 0.9957 | 0.9959 | 0.9960 | 0.9961 | 0.9962 | 0.9963 | 0.9964 |
| 2.7 | 0.9965 | 0.9966 | 0.9967 | 0.9968 | 0.9969 | 0.9970 | 0.9971 | 0.9972 | 0.9973 | 0.9974 |
| 2.8 | 0.9974 | 0.9975 | 0.9976 | 0.9977 | 0.9977 | 0.9978 | 0.9979 | 0.9979 | 0.9980 | 0.9981 |
| 2.9 | 0.9981 | 0.9982 | 0.9982 | 0.9983 | 0.9984 | 0.9984 | 0.9985 | 0.9985 | 0.9986 | 0.9986 |
| 3.0 | 0.9987 | 0.9987 | 0.9987 | 0.9988 | 0.9988 | 0.9989 | 0.9989 | 0.9989 | 0.9990 | 0.9990 |

*(b)* What is the probability of a normal random variable taking a value lower than 1.47 standard deviations below its mean? P(Z < −1.47) = 0.0708, or 7.08%.

| z | 0.00 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 | 0.06 | 0.07 | 0.08 | 0.09 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| −1.5 | 0.0668 | 0.0655 | 0.0643 | 0.0630 | 0.0618 | 0.0606 | 0.0594 | 0.0582 | 0.0571 | 0.0559 |
| −1.4 | 0.0808 | 0.0793 | 0.0778 | 0.0764 | 0.0749 | 0.0735 | 0.0721 | 0.0708 | 0.0694 | 0.0681 |
| −1.3 | 0.0968 | 0.0951 | 0.0934 | 0.0918 | 0.0901 | 0.0885 | 0.0869 | 0.0853 | 0.0838 | 0.0823 |
| −1.2 | 0.1151 | 0.1131 | 0.1112 | 0.1093 | 0.1075 | 0.1056 | 0.1038 | 0.1020 | 0.1003 | 0.0985 |

*(c)* What is the probability of a normal random variable taking a value *more* than 0.75 standard deviations above its mean?

The fact that the problem involves the word *more* rather than *less* should not be overlooked! Our normal table, like most, provides left-tail probabilities, and adjustments must be made for any other type of problem.

*Method 1:* By symmetry of the z curve centered on 0, P(Z > +0.75) = P(Z < −0.75) = 0.2266.

*Method 2:* Because the total area under the normal curve is 1, P(Z > +0.75) = 1 − P(Z < +0.75) = 1 − 0.7734 = 0.2266.

*Note:* Most students prefer to use Method 1, which does not require subtracting 4-digit probabilities from 1.

*(d)* What is the probability of a normal random variable taking a value between 1 standard deviation below and 1 standard deviation above its mean?

To find probabilities between two values, we must put them in terms of "less than" probabilities. A sketch is especially helpful here:

P(−1 < Z < +1) = P(Z < +1) − P(Z < −1) = 0.8413 − 0.1587 = 0.6826.

(Note that this confirms the "68%" of the Standard Deviation Rule, now with more precision.)
:::

## Check Your Understanding: Greater-Than and Between Probabilities

:::{quiz} What is P(Z > −1.35)? (From the table, P(Z < −1.35) = 0.0885.)
:hint: "Greater than" is the complement of the left-tail probability.
:feedback-0: Correct! P(Z > −1.35) = 1 − 0.0885 = 0.9115.
:feedback-1: 0.0885 is the probability of being LESS than −1.35.
:feedback-2: By symmetry P(Z > −1.35) = P(Z < 1.35), which is far more than half.
* *0.9115
* 0.0885
* 0.5
:::

:::{quiz} What is P(−1.47 < Z < 2.8)? (Use the values found in the example: P(Z < 2.8) = 0.9974 and P(Z < −1.47) = 0.0708.)
:hint: Subtract the smaller left-tail area from the larger.
:feedback-0: Correct! 0.9974 − 0.0708 = 0.9266.
:feedback-1: Adding the two left-tail probabilities doesn't correspond to any area between the two values.
:feedback-2: 0.9974 is the entire area to the left of 2.8; you must remove the part below −1.47.
* *0.9266
* 1.0682
* 0.9974
:::
