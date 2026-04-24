# Two Independent Samples (5 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing groups.
```

Let's look at another example, and then you'll do one yourself.

```{admonition} Example
    According to the National Health And Nutrition Examination Survey (NHANES) sponsored by the U.S. government, a random sample of 712 males between 20 and 29 years of age and a random sample of 1,001 males over the age of 75 were chosen, and the weight of each of the males was recorded (in kg). Here is a summary of the results (source: http://www.cdc.gov/nchs/data/ad/ad347.pdf):

    ```{figure} images/image194.gif
    :alt: For males 20-29 years old, n = 712, Y-bar = 83.4, S = 18.7. For males 75+ years old, n = 1001, Y-bar = 78.5, S = 19.0

    For males 20-29 years old, n = 712, Y-bar = 83.4, S = 18.7. For males 75+ years old, n = 1001, Y-bar = 78.5, S = 19.0
    ```

    Do the data provide evidence that the younger male population weighs more (on average) than the older male population? (Note that here the data are given in a summarized form, unlike the previous problem, where the raw data were given.)

    Here is a figure that summarizes this example:

    ```{figure} images/image043.gif
    :alt: We have two populations, from the two categories in the variable Age Group(X). Population 1 is Males 20-29 years old, and Population 2 is Males 75+ years old. Population 1&apos;s Weight (Y) mean is μ_1, and population 2&apos;s weight (Y) mean is μ_2. For population 1, a SRS of size 712 is generated. It has a mean of 83.4 and SD of 18.7 . For population 2, another SRS is generated of size 1001. It has a mean of 78.5 and SD of 19.0 .

    We have two populations, from the two categories in the variable Age Group(X). Population 1 is Males 20-29 years old, and Population 2 is Males 75+ years old. Population 1&apos;s Weight (Y) mean is μ_1, and population 2&apos;s weight (Y) mean is μ_2. For population 1, a SRS of size 712 is generated. It has a mean of 83.4 and SD of 18.7 . For population 2, another SRS is generated of size 1001. It has a mean of 78.5 and SD of 19.0 .
    ```

    Note that we defined the younger age group and the older age group as population 1 and population 2, respectively, and μ~1~ and μ~2~ as the mean weight of population 1 and population 2, respectively.

    *Step 1:*

    Since we want to test whether the older age group (population 2) weighs less on average than the younger age group (population 1), we are testing:

    ```{figure} images/image044.gif
    :alt: H_0: μ_1 - μ_2 = 0, H_a: μ_1 - μ_2 &gt; 0

    H_0: μ_1 - μ_2 = 0, H_a: μ_1 - μ_2 &gt; 0
    ```

    or equivalently,

    ```{figure} images/image045.gif
    :alt: H_0: μ_1 = μ_2, H_a: μ_1 &gt; μ_2

    H_0: μ_1 = μ_2, H_a: μ_1 &gt; μ_2
    ```

    *Step 2:*

    We can safely use the two-sample t-test in this case since:

    1. The samples are independent, since each of the samples was chosen at random.
    2. Both sample sizes are very large (712 and 1,001), and therefore we can proceed regardless of whether the populations are normal or not.

    It is possible from these data to calculate the t-statistic of 5.31 and the p-value of 0.000. The t-value is quite large, and the p-value correspondingly small, indicating that our data are very different from what is claimed in the null hypothesis.

    *Step 3:*

    The p-value is essentially 0, indicating that it would be nearly impossible to observe a difference between the sample mean weights of 4.9 (or more) if the mean weights in the age group populations were the same (i.e., if H~o~ were true).

    *Step 4:*

    A p-value of 0 (or very close to it) indicates that the data provide strong evidence against H~o~, so we reject it and conclude that the mean weight of males 20-29 years old is higher than the mean weight of males 75 years old and older. In other words, males in the younger age group weigh more, on average, than males in the older age group.
```

Now you try one!

```{note}
    **Learn By Doing**

    Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```
