# Quartiles and the Middle Half of the Data

## Inter-Quartile Range (IQR)

While the range quantifies the variability by looking at the range covered by *ALL* the data, the IQR measures the variability of a distribution by giving us the range covered by the *MIDDLE 50%* of the data.

The following picture illustrates this idea: (Think about the horizontal line as the data ranging from the min to the Max).

```{figure} images/gen/m04-iqr-idea.svg
:alt: A horizontal line representing all of the data from the minimum on the left to the maximum on the right, divided into quarters by Q1, the median M, and Q3. The section from the minimum to Q1 is the bottom 25% of the data, the highlighted section from Q1 to Q3 is the middle 50% of the data, and the section from Q3 to the maximum is the top 25%. A bracket under the middle section is labeled IQR equals Q3 minus Q1.
```

Here is how the IQR is actually found:

1. Arrange the data in increasing order, and find the median M. Recall that the median divides the data, so that 50% of the data points are below the median, and 50% of the data points are above the median.
2. Find the median of the lower 50% of the data. This is called the first quartile of the distribution, and the point is denoted by Q1. Note from the picture that Q1 divides the lower 50% of the data into two halves, containing 25% of the data points in each half. Q1 is called the first quartile, since one quarter of the data points fall below it.
3. Repeat this again for the top 50% of the data. Find the median of the top 50% of the data. This point is called the third quartile of the distribution, and is denoted by Q3. Note from the picture that Q3 divides the top 50% of the data into two halves, with 25% of the data points in each. Q3 is called the third quartile, since three quarters of the data points fall below it.
4. The middle 50% of the data falls between Q1 and Q3, and therefore: IQR = Q3 - Q1

::::{admonition} Comments
:class: important

1. The last picture shows that Q1, M, and Q3 divide the data into four quarters with 25% of the data points in each, where the median is essentially the second quartile. The use of IQR = Q3 - Q1 as a measure of spread is therefore particularly appropriate when the median M is used as a measure of center.

2. We can define a bit more precisely what is considered the bottom or top 50% of the data. The bottom (top) 50% of the data is all the observations whose position in the ordered list is to the left (right) of the location of the overall median M. The following picture visually illustrates this for the simple cases of $n = 7$ and $n = 8$.

   ```{figure} images/gen/m04-quartile-halves.svg
   :alt: Two rows of ordered dots. For n equals 7, the middle dot is the median and is excluded, leaving a bottom half of three dots and a top half of three dots. For n equals 8, the data split naturally into a bottom half of four dots and a top half of four dots.
   ```

   Note that when n is odd (as in $n = 7$ above), the median is *not* included in either the bottom or top half of the data; when n is even (as in $n = 8$ above), the data are naturally divided into two halves.
::::
