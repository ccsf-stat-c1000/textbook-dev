# Boxplot (2 of 3)

```{admonition} Learning Objectives
    - Generate and interpret several different graphical displays of the distribution of a quantitative variable (histogram, stemplot, boxplot).
```

Now that you understand what each of the five numbers means, you can appreciate how much information about the distribution is packed into the five-number summary. All this information can also be represented visually by using the boxplot.

## The Boxplot

The boxplot graphically represents the distribution of a quantitative variable by visually displaying the five-number summary and any observation that was classified as a suspected outlier using the 1.5(IQR) criterion.

There are several ways to plot the whiskers on a boxplot. One convention is to plot whiskers down to the minimum and up to the maximum value. We use the 1.5(IQR criterion), also known as the Tukey method for plotting whiskers. First, calculate the IQR, the difference between the 75th and 25th percentiles (or Q3 – Q1). Multiply the IQR by 1.5. Add this value to the 75th percentile. If the value is greater than (or equal to) the maximum value in the dataset, draw the upper whisker to the maximum value. Otherwise, stop the whisker at the largest value that is less than 75th percentile + 1.5 * IQR. Plot any values that are greater than this as individual points that are outliers. Similarly, subtract 1.5 * IQR from the 25th percentile. If this value is smaller than the minimum value in the dataset, draw the lower whisker to the minimum value. Otherwise, stop the whisker at the lowest value that is greater than 25th percentile – 1.5 * IQR. Plot any values that are smaller than this as individual points that are outliers.

Using the Best Actress dataset, here is how we determine where to draw the whiskers:

- Q3 = 42
- Q1 = 30.5
- IQR: 42 – 30.5 = 11.5
- 1.5 * IQR = 1.5 * 11.5 = 17.25
- Q3 + 1.5 * IQR = 42 + 17.25 = 59.25

The largest observation that is less than or equal to 59.25 is 49 so we draw the upper whisker up to 49. All points above 49 are considered outliers (61, 61, 62, 74, 80).

Q1 – 1.5 * IQR = 30.5 – 17.25 = 13.25

The smallest observation that is greater than or equal to 13.5 is 21 so we draw the lower whisker down to 21, which is also the minimum. There are no outliers.

Here is how a boxplot is constructed: (this is for the "Best Actress" dataset—to see the dataset, click here.)

```{note} Video
[Constructing a Boxplot](https://www.youtube.com/watch?v=S50-WYpOm4I)
```

##### 

The boxplot below displays the ages of Best Actor Oscar winners (1970-2013). Here is how a boxplot is constructed: (this is for the "Best Actress" dataset, to see the dataset click here.)

```{admonition} Example: Best Actor Oscar Winners
    The boxplot below displays the ages of Best Actor Oscar winners (1970-2013). Click here for the data. In the last activity, you found numerical measures for this distribution.

    Label the different numerical measures as they are depicted in the boxplot.

    ```{note}
        **Learn By Doing**

        *(Interactive activity — available in the OLI platform)*
    ```
```

GeoGebra Group offers a simulation activity where you can practice calculating the median, Q1, Q3, IQR, and outliers and drawing a boxplot. Note that you can edit the data in the chart to see different results.

To view this interactive simulation in a separate window click [here](http://ggbtu.be/m11008).

[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) by [GeoGebra Group](http://www.geogebra.org/)

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

*Did You Get It?* If so, then go ahead and move on to the next page. If not, then click the link below for some additional practice.

```{note}
    **Did I Get This?**

    Boxplot: Extra Problems

    *(Interactive activity — available in the OLI platform)*
```
