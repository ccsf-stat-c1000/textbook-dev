# Case Q→Q (2 of 3)

```{admonition} Learning Objectives
    - In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing relationships.
```

Let's introduce our leading example, which was actually our leading example in the Exploratory Data Analysis unit as well.

```{admonition} Example
    In a study of the legibility and visibility of highway signs, a Pennsylvania research firm determined the maximum distance at which each of 30 drivers could read a newly designed sign. The 30 participants in the study ranged in age from 18 to 82 years old. The government agency that funded the research hoped to improve highway safety for older drivers and wanted to examine the relationship between age and sign legibility distance. (Data adopted with permission from Utts and Heckard, Mind on Statistics).

    Let's go through the entire process (outlined on the previous page) for this example.

    *Starting point*: The researchers wanted to examine the relationship between age and sign legibility distance in the population of drivers. The researchers collected data from a random sample of 30 drivers:

    ```{figure} images/image179.gif
    :alt: A two column table, with column headers &quot;Age&quot; and &quot;Distance.&quot; Here is the data in the table, by row (in &quot;Age: Distance&quot; format): 18: 510; 20: 590; 22: 560; 23: 510; 23: 460; 25: 490; 27: 560; ... ... 77: 360; 79: 310; 82: 360;

    A two column table, with column headers &quot;Age&quot; and &quot;Distance.&quot; Here is the data in the table, by row (in &quot;Age: Distance&quot; format): 18: 510; 20: 590; 22: 560; 23: 510; 23: 460; 25: 490; 27: 560; ... ... 77: 360; 79: 310; 82: 360;
    ```

    *Exploratory Analysis:*

    The researchers display the data on a scatterplot:

    ```{figure} images/image147.gif
    :alt: A scatterplot of Distance vs. Age. Distance is on the vertical axis, and age is on the horizontal axis. The histogram has a negative relationship, and it seems like it could be reasonably linear.

    A scatterplot of Distance vs. Age. Distance is on the vertical axis, and age is on the horizontal axis. The histogram has a negative relationship, and it seems like it could be reasonably linear.
    ```

    and observe a negative linear relationship in the data. In order to quantify the strength of that linear relationship, the researchers supplement the scatterplot with a numerical measure—the correlation coefficient (r), which turns out to be r = -.801, confirming the researchers' visual assessment of a negative, fairly strong linear relationship between age and legibility distance.
```

```{note}
    **Learn By Doing**

    Case Q→Q

    *(Interactive activity — available in the OLI platform)*
```

*Inference:*

The researchers would now like to see whether the observed linear relationship between age and legibility distance can be generalized to the entire population of drivers. In other words, the researchers want to check whether the observed linearity is due to true linearity in the population, or a pattern that could have happened just by chance.

The test that the researchers are going to carry out is a t-test (most commonly known as the "t-test for the slope" for reasons that we are not going to get into) which is testing the following two hypotheses (step 1):

*H**~o~**:* There is no linear relationship between age and distance.

*H**~a~**:* There is a linear relationship between age and distance.

and in general,

*H**~o~**:* There is no linear relationship between X and Y.

*H**~a~**:* There is a linear relationship between X and Y.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

## Comments

1. As we mentioned earlier, we are going to keep this discussion on the qualitative side and in particular we will not go very deeply into *step 2*of the hypothesis test. As for the*test-statistic* in this case, we'll just say that the test is a t-test, which, as we know, means that the null distribution of its test statistic (under which the p-values are calculated) is some tdistribution.

2. We are also going to focus on only some of the *conditions* that allow us to safely use this t-test. They are:

- the observed data indeed look linear (otherwise it would not make sense to try and generalize them)
- the observations are independent
- there are no extreme outliers in the data
- the sample size is fairly large

Note that in our example all these conditions are met; the data definitely look linear, the observations (drivers) are independent of each other (since they were randomly chosen), there are no extreme observations in the data, and a sample size of n=30 is fairly large.

For *step 3,* the researchers use statistical software to find a test statistic value of -7.09, and a p-value that is so small that it is essentially 0. This means that it would be extremely unlikely (actually, quite impossible) to get data like those observed if age and legibility distance were not linearly related. In other words, it would be extremely unlikely to get data like those observed just by chance.

The researchers conclude (*step 4*) that since the p-value is so small, the data provide extremely strong evidence to reject H~o~ and conclude that age and legibility distance are linearly related.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    Case Q→Q

    *(Interactive activity — available in the OLI platform)*
```

*Note:* It is important to distinguish between the information provided by r and by the p-value. The correlation coefficient *r informs us about the strength of the linear relationship in the data*: close to +1 or -1 for a strong linear relationship, close to 0 for a weak linear relationship. In contrast, the regression *p-value informs us about the strength of evidence* that there is a linear relationship in the population from which the data were obtained.

In our example, since the p-value is 0.000 and r = -.801, we would say that we have extremely strong evidence of a fairly strong relationship between age and distance in the population of drivers.

## Did I Get This?

In our cry count of newborns and IQ at age three example, we have found the following:

- The correlation coefficient of our observed data is r=0.4.
- The p-value of the test: is p=0.012.
  - H~o~: There is no linear relationship between cry count and IQ.
  - H~a~: There is a significant linear relationship between cry count and IQ.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
