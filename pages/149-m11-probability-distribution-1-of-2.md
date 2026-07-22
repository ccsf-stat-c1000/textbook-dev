# From Histogram to Density Curve

## The Probability Distribution of a Continuous Random Variable

In order to shift our focus from discrete to continuous random variables, let us first consider the probability histogram below for the shoe size of adult males. Let X represent these shoe sizes. Thus, X is a discrete random variable, since shoe sizes can only take whole and half number values, nothing in between.

Recall that in all of the previous probability histograms we've seen, the X-values were whole numbers. Thus, the width of each bar was 1. The height of each bar was the same as the probability for its corresponding X-value. Due to the principle that states the sum of probabilities of all possible outcomes in the sample space must be 1, the *heights* of all the rectangles in the histogram must sum to 1. This meant that the area was also 1.

This histogram uses half-sizes. We wish to keep the area = 1, but we still want the horizontal scale to represent half-sizes. Therefore, we must adjust the vertical scale of the histogram. As is, the total area of the histogram rectangles would be 0.50 times the sum of the probabilities, since the width of each bar is 0.50. Thus, the area is 0.50(1) = 0.50. If we double the vertical scale, the area will double and be 1, just like we want. This means we are changing the vertical scale from "Probability" to "Probability per half size." The shape and the horizontal scale remain unchanged:

```{figure} images/gen/m11-shoesize-hist.svg
:alt: A probability histogram of male shoe sizes from 6.5 to 15.5 in half-size steps, with the vertical axis labeled probability per half size. The bars rise to a peak at size 11 and fall away, forming a roughly normal shape. With this vertical scale, the total area of the bars is 1.
```

Now we can tell the probability of shoe size taking a value in any interval, just by finding the area of the rectangles over that interval. For instance, the area of the rectangles up to and including 9 shows the probability of having a shoe size less than or equal to 9:

```{figure} images/gen/m11-shoesize-shaded.svg
:alt: The same shoe-size histogram with the bars for sizes 6.5 through 9 shaded orange. The shaded area equals the probability that the shoe size is at most 9.
```

Recall that for a discrete random variable like shoe size, the probability is affected by whether we want strict inequality or not. For example, the area—and corresponding probability—is reduced if we only consider shoe sizes strictly less than 9, since we then remove the bar over 9 itself.

## Check Your Understanding: From Histograms to Density Curves

:::{quiz} In the rescaled shoe-size histogram (vertical axis: probability per half size), how is P(9.5 ≤ X ≤ 10.5) represented?
:hint: Probabilities are now represented by areas.
:feedback-0: Correct! With this scaling, probability equals the area of the bars over the interval—here the three bars at 9.5, 10, and 10.5.
:feedback-1: With the "probability per half size" scale, the heights alone no longer give probabilities—each bar's area (height × 0.5) does.
:feedback-2: The single tallest bar is the mode, not the probability of the whole interval.
* *By the total area of the bars over 9.5, 10, and 10.5
* By the sum of the heights of those bars
* By the height of the tallest bar
:::

## Transition to Continuous Random Variables

Now we are going to be making the transition from *discrete* to *continuous* random variables. Recall that continuous random variables represent measurements and can take on any value within an interval.

For our shoe size example, this would mean measuring shoe sizes in smaller units, such as tenths, or hundredths. As the number of intervals increases, the width of the bars becomes narrower and narrower, and the graph approaches a smooth curve:

```{figure} images/gen/m11-hist-to-curve.svg
:alt: Three panels showing the same bell-shaped distribution with progressively narrower histogram bars: first with interval width 0.25, then 0.10, and finally as a smooth density curve. As the bars narrow, the histogram approaches the smooth curve.
```

We'll use these smooth curves to represent the probability distributions of continuous random variables. This idea will be discussed in more detail on the next page.
