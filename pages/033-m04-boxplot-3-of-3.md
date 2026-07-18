# Side-by-Side Boxplots: Comparing Groups at a Glance

```{admonition} Learning Objectives
:class: note

- Compare and contrast distributions (of quantitative data) from two or more groups, and produce a brief summary, interpreting your findings in context.
```

## Side-By-Side (Comparative) Boxplots

As we learned in the beginning of this module, the distribution of a quantitative variable is best represented graphically by a histogram. Boxplots are most useful when presented side-by-side for comparing and contrasting distributions from two or more groups.

::::{admonition} Example: Best Actor/Actress Oscar Winners
:class: tip

So far we have examined the age distributions of Oscar winners for males and females separately.

It will be interesting to *compare* the age distributions of actors and actresses who won best acting Oscars. To do that we will look at side-by-side boxplots of the age distributions by gender, supplemented by the five-number summary of each distribution (calculated using statistical software):

| Statistic | Actors | Actresses |
| --- | --- | --- |
| min | 31 | 21 |
| Q1 | 38 | 30.5 |
| Median | 43.5 | 34.5 |
| Q3 | 50.5 | 42 |
| Max | 76 | 80 |

```{figure} images/gen/m04-actor-actress-boxplots.svg
:alt: Side-by-side horizontal boxplots of winners' ages for actors and actresses on a shared axis from 20 to 80. The actors' box sits noticeably to the right of the actresses' box, with a median of 43.5 versus 34.5. The actors' plot has one high outlier at 76; the actresses' plot has outliers at 61, 61, 62, 74, and 80.
```

Based on the graph and numerical measures, we can make the following comparison between the two distributions:

*Center:* The graph reveals that the age distribution of the males is higher than the females' age distribution. This is supported by the numerical measures. The median age for females (34.5) is lower than for the males (43.5). Actually, it should be noted that even the third quartile of the females' distribution (42) is lower than the median age for males. We therefore conclude that in general, actresses win the Best Actress Oscar at a younger age than actors do.

*Spread:* Judging by the range of the data, there is much more variability in the females' distribution (range = 59) than there is in the males' distribution (range = 45). On the other hand, if we look at the IQR, which measures the variability only among the middle 50% of the distribution, we see slightly more spread in the ages of males (IQR = 12.5) than females (IQR = 11.5). We conclude that among all the winners, the actors' ages are more alike than the actresses' ages. However, the middle 50% of the age distribution of actresses is more homogeneous than the actors' age distribution.

*Outliers:* We see that we have outliers in both distributions. There is only one high outlier in the actors' distribution (76, Henry Fonda, *On Golden Pond*), compared with five high outliers in the actresses' distribution.
::::

::::{admonition} Example: Temperature of Pittsburgh vs. San Francisco
:class: tip

In order to compare the average high temperatures of Pittsburgh to those in San Francisco we will look at the following side-by-side boxplots, and supplement the graph with the descriptive statistics of each of the two distributions.

```{figure} images/gen/m04-temps-boxplots.svg
:alt: Side-by-side vertical boxplots of average monthly high temperatures. The San Francisco boxplot is short and compact, entirely between about 56 and 69 degrees. The Pittsburgh boxplot stretches from about 34 to 83 degrees with a very tall box. The two medians are similar, around 61 to 63 degrees.
```

| Statistic | San Francisco | Pittsburgh |
| --- | --- | --- |
| min | 56.3 | 33.7 |
| Q1 | 60.2 | 41.2 |
| Median | 62.7 | 61.4 |
| Q3 | 65.35 | 77.75 |
| Max | 68.7 | 82.6 |

When looking at the graph, the similarities and differences between the two distributions are striking. Both distributions have roughly the same center (medians are 61.4 for Pittsburgh, and 62.7 for San Francisco). However, the temperatures in Pittsburgh have a much larger variability than the temperatures in San Francisco (Range: 49 vs. 12. IQR: 36.5 vs. 5).

The practical interpretation of the results we got is that the weather in San Francisco is much more consistent than the weather in Pittsburgh, which varies a lot during the year. Also, because the temperatures in San Francisco vary so little during the year, knowing that the median temperature is around 63 is actually very informative. On the other hand, knowing that the median temperature in Pittsburgh is around 61 is practically useless, since temperatures vary so much during the year, and can get much warmer or much colder.

Note that this example provides more intuition about variability by interpreting small variability as consistency, and large variability as lack of consistency. Also, through this example we learned that the center of the distribution is more meaningful as a typical value for the distribution when there is little variability (or, as statisticians say, little "noise") around it. When there is large variability, the center loses its practical meaning as a typical value.
::::

## Check Your Understanding: Comparing Groups with Boxplots

:::{quiz} Two bus routes both have a median travel time of 30 minutes. Route A's IQR is 4 minutes; Route B's IQR is 22 minutes. Which statement gives the best practical interpretation?
:hint: Think of the San Francisco vs. Pittsburgh temperature example—small variability means consistency.
:feedback-0: Correct! With small variability, Route A's typical time of 30 minutes is dependable; Route B's identical median tells you much less because times vary widely.
:feedback-1: The medians are equal, so on a typical day the routes take about the same time—the difference is in consistency, not center.
:feedback-2: A larger IQR means less consistency, not more.
* *Route A is more consistent, so its median is a more meaningful "typical" travel time
* Route A is usually much faster than Route B
* Route B is more reliable because its IQR is larger
:::

:::{quiz} Using the side-by-side boxplots of Oscar winners' ages, which comparison is supported by the display?
:hint: Compare the positions of the two boxes and medians.
:feedback-0: Correct! The actresses' entire box (up to Q3 = 42) lies below the actors' median (43.5), showing that actresses tend to win at younger ages.
:feedback-1: The actors' median (43.5) is well above the actresses' median (34.5).
:feedback-2: The full range is larger for actresses (59 years) than for actors (45 years).
* *Actresses tend to win at younger ages than actors
* The median age of actors is lower than that of actresses
* The actors' ages cover a wider overall range than the actresses' ages
:::

## Let's Summarize

- The five-number summary of a distribution consists of the median (M), the two quartiles (Q1, Q3) and the extremes (min, Max).
- The five-number summary provides a complete numerical description of a distribution. The median describes the center, and the extremes (which give the range) and the quartiles (which give the IQR) describe the spread.
- The boxplot graphically represents the distribution of a quantitative variable by visually displaying the five-number summary and any observation that was classified as a suspected outlier using the 1.5(IQR) criterion.
- Boxplots are most useful when presented side-by-side to compare and contrast distributions from two or more groups.
