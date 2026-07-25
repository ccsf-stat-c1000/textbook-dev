# Mean vs. Median: How Shape and Outliers Decide

## Comparing the Mean and the Median

As we have seen, the mean and the median, two of the common measures of center, each describe the center of a distribution of values in a different way. The mean describes the center as an average value, in which the *actual values* of the data points play an important role. The median, on the other hand, locates the middle value as the center, and the *order* of the data is the key to finding it.

To get a deeper understanding of the differences between these two measures of center, consider the following example.

Here are two datasets:

| | |
| --- | --- |
| Dataset A | 64 65 66 68 70 71 **73** |
| Dataset B | 64 65 66 68 70 71 **730** |

For dataset A, the mean is 68.1, and the median is 68. Looking at dataset B, notice that all of the observations except the last one are close together. The observation 730 is very large, and is certainly an outlier. In this case, the median is still 68, but the mean will be influenced by the high outlier, and shifted up to 162. The message that we should take from this example is:

*The mean is very sensitive to outliers (because it factors in their magnitude), while the median is resistant to outliers.*

Therefore:

- For symmetric distributions with no outliers: $\bar{x}$ is approximately equal to M.

```{figure} images/gen/m04-center-symmetric.svg
:alt: A symmetric, single-peaked density curve. A single dashed line at the center marks both the mean and the median, which coincide.
```

- For skewed right distributions and/or datasets with high outliers: $\bar{x} > M$

```{figure} images/gen/m04-center-skewed-right.svg
:alt: A right-skewed density curve with a long right tail. The median is marked near the peak, and the mean is marked to the right of the median, pulled toward the long tail.
```

- For skewed left distributions and/or datasets with low outliers: $\bar{x} < M$

```{figure} images/gen/m04-center-skewed-left.svg
:alt: A left-skewed density curve with a long left tail. The median is marked near the peak, and the mean is marked to the left of the median, pulled toward the long tail.
```

We will therefore use $\bar{x}$ as a measure of center for symmetric distributions with no outliers. Otherwise, the median will be a more appropriate measure of the center of our data.

## Check Your Understanding: Choosing a Measure of Center

:::{quiz} A real estate agent lists the prices of 15 homes sold last month in a neighborhood. Fourteen sold for between \$350,000 and \$500,000, and one mansion sold for \$3.2 million. Which statement is correct?
:hint: Which measure factors in the actual magnitude of the mansion's price?
:feedback-0: Correct! The mansion is a high outlier; it pulls the mean up substantially but barely affects the median.
:feedback-1: It's the reverse—the median only depends on the order of the values, so the outlier hardly moves it.
:feedback-2: The two measures respond very differently to the outlier, so they will not be approximately equal.
* *The mean will be much larger than the median
* The median will be much larger than the mean
* The mean and median will be approximately equal
:::

:::{quiz} A histogram of scores is clearly skewed left. What is the expected relationship between the mean and the median?
:hint: The mean gets pulled toward the long tail.
:feedback-0: In a skewed-left distribution the long tail is on the low side, pulling the mean down, not up.
:feedback-1: Correct! The long left tail pulls the mean below the median.
:feedback-2: Mean and median are approximately equal only for symmetric distributions.
* Mean > Median
* *Mean < Median
* Mean $\approx$ Median
:::

:::{quiz} For the ages of the Best Actress Oscar winners, the mean is 38.3 and the median is 34.5. What does this comparison suggest about the shape of the distribution?
:hint: Which direction is the mean pulled relative to the median?
:feedback-0: Correct! The mean is noticeably larger than the median, consistent with a right-skewed distribution (a few unusually old winners pull the mean up).
:feedback-1: If the distribution were skewed left, the mean would be below the median.
:feedback-2: In a symmetric distribution the two measures would be approximately equal, but here they differ by almost 4 years.
* *The distribution is skewed right
* The distribution is skewed left
* The distribution is symmetric
:::

:::{quiz} A journalist wants to report the "typical" household income in a city, where the income distribution is strongly skewed right. Which measure of center is more appropriate?
:hint: Which measure resists the influence of a few extremely high incomes?
:feedback-0: The mean is inflated by the few very high incomes and overstates what a typical household earns.
:feedback-1: Correct! The median is resistant to the high outliers and better represents a typical household.
:feedback-2: The mode can be unstable for income data and ignores the center of the distribution.
* The mean
* *The median
* The mode
:::

## Let's Summarize

- The three main numerical measures for the center of a distribution are the mode, mean ($\bar{x}$), and the median (M). The mode is the most frequently occurring value. The mean is the average value, while the median is the middle value.
- The mean is very sensitive to outliers (as it factors in their magnitude), while the median is resistant to outliers.
- The mean is an appropriate measure of center only for symmetric distributions with no outliers. In all other cases, the median should be used to describe the center of the distribution.
