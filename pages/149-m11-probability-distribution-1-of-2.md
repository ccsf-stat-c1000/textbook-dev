# Probability Distribution (1 of 2)

```{admonition} Learning Objectives
    - Explain how a density function is used to find probabilities involving continuous random variables.
```

## The Probability Distribution of a Continuous Random Variable

In order to shift our focus from discrete to continuous random variables, let us first consider the probability histogram below for the shoe size of adult males. Let X represent these shoe sizes. Thus, X is a discrete random variable, since shoe sizes can only take whole and half number values, nothing in between.

```{figure} images/image100.gif
:alt: A histogram for male shoe sizes. The vertical axis is labeled "Probability" and the horizontal axis is labeled "Male shoe size". Moving from left to right across the horizontal axis, we start at size=6.5, where the probability is very low, below .02 . From there, the probabilities grow until size=11, where probability is at about .20 . Then, as sizes increase, probability decreases. The axis ends at size = 15.5 . The histogram makes a typical normal shape.

A histogram for male shoe sizes. The vertical axis is labeled "Probability" and the horizontal axis is labeled "Male shoe size". Moving from left to right across the horizontal axis, we start at size=6.5, where the probability is very low, below .02 . From there, the probabilities grow until size=11, where probability is at about .20 . Then, as sizes increase, probability decreases. The axis ends at size = 15.5 . The histogram makes a typical normal shape.
```

Recall that in all of the previous probability histograms we've seen, the X-values were whole numbers. Thus, the width of each bar was 1. The height of each bar was the same as the probability for its corresponding X-value. Due to the principle that states the sum of probabilities of all possible outcomes in the sample space must be 1, the *heights* of all the rectangles in the histogram must sum to 1. This meant that the area was also 1.

This histogram uses half-sizes. We wish to keep the area = 1, but we still want the horizontal scale to represent half-sizes. Therefore, we must adjust the vertical scale of the histogram. As is, the total area of the histogram rectangles would be .50 times the sum of the probabilities, since the width of each bar is .50. Thus, the area is .50(1) = .50. If we double the vertical scale, the area will double and be 1, just like we want. This means we are changing the vertical scale from "Probability" to "Probability per half size." The shape and the horizontal scale remain unchanged.

```{figure} images/image101.gif
:alt: The same histogram as the previous one, except that the vertical axis has been changed. It is now labeled "Probability per half size", and now the units are half as large, so that at size = 11, probability is .40 . We also see that the area for all of the bars using this new vertical axis is 1.

The same histogram as the previous one, except that the vertical axis has been changed. It is now labeled "Probability per half size", and now the units are half as large, so that at size = 11, probability is .40 . We also see that the area for all of the bars using this new vertical axis is 1.
```

Now we can tell the probability of shoe size taking a value in any interval, just by finding the area of the rectangles over that interval. For instance, the area of the rectangles up to and including 9 shows the probability of having a shoe size less than or equal to 9.

```{figure} images/image102.gif
:alt: The same histogram as the previous one, but the bars for sizes 6.5 to 9 have been shaded. The area of the shading is the Probability of shoe size less than or equal to 9.

The same histogram as the previous one, but the bars for sizes 6.5 to 9 have been shaded. The area of the shading is the Probability of shoe size less than or equal to 9.
```

Recall that for a discrete random variable like shoe size, the probability is affected by whether we want strict inequality or not. For example, the area—and corresponding probability—is reduced if we only consider shoe sizes strictly less than 9:

```{figure} images/image103.gif
:alt: The histogram now only has the bars for shoe sizes 6.5 though 8.5 shaded. The shaded area is the Probability of shoe size < 9.

The histogram now only has the bars for shoe sizes 6.5 though 8.5 shaded. The shaded area is the Probability of shoe size < 9.
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Transition to Continuous Random Variables

Now we are going to be making the transition from *discrete* to *continuous* random variables. Recall that continuous random variables represent measurements and can take on any value within an interval.

For our shoe size example, this would mean measuring shoe sizes in smaller units, such as tenths, or hundredths. As the number of intervals increases, the width of the bars becomes narrower and narrower, and the graph approaches a smooth curve.

To illustrate this, the following graphs represent two steps in this process of narrowing the widths of the intervals. Specifically, the interval widths are .25 and .10.

We'll use these smooth curves to represent the probability distributions of continuous random variables. This idea will be discussed in more detail on the next page.
