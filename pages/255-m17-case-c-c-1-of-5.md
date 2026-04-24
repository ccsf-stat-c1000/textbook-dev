# Case C→C (1 of 5)

```{admonition} Learning Objectives
    - Choose the appropriate inferential method for examining the relationship between two variables and justify the choice.
```

## Inference for the Relationships between Two Categorical Variables (Chi-Square
                Test for Independence)

##### Overview

The last three procedures that we studied (two-sample t, paired t, and ANOVA) all involve the relationship between a categorical explanatory variable and a quantitative response variable, corresponding to Case C→Q in the role/type classification table below. Next, we will consider inferences about the relationships between two categorical variables, corresponding to case C→C.

```{figure} images/image182.gif
:alt: It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).

It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).
```

In the Exploratory Data Analysis unit of the course, we summarized the relationship between two categorical variables for a given data set (using a two-way table and conditional percents), without trying to generalize beyond the sample data.

Now we perform statistical inference for two categorical variables, using the sample data to draw conclusions about whether or not we have evidence that the variables are related in the larger population from which the sample was drawn. In other words, we would like to assess whether the relationship between X and Y that we observed in the data is due to a real relationship between X and Y in the population or if it is something that could have happened just by chance due to sampling variability.

```{figure} images/image123.gif
:alt: We have a population of interest and a question about it, which is "Are the two categorical variables X and Y related?" We take an SRS of size n, and summarize that data with a two-way table. Via inference, we can decide if the relationship is strong enough that we can conclude that it is due to a true relationship in the population. This inference step is what this section goes over.

We have a population of interest and a question about it, which is "Are the two categorical variables X and Y related?" We take an SRS of size n, and summarize that data with a two-way table. Via inference, we can decide if the relationship is strong enough that we can conclude that it is due to a true relationship in the population. This inference step is what this section goes over.
```

The statistical test that will answer this question is called the *chi-square test for independence*. Chi is a Greek letter that looks like this: $\chi$, so the test is sometimes referred to as: The $\chi^{2}$ test for independence.

The structure of this section will be very similar to that of the previous ones in this module. We will first present our leading example, and then introduce the chi-square test by going through its 4 steps, illustrating each one using the example. We will conclude by presenting another complete example. As usual, you'll have activities along the way to check your understanding, and to learn how to use software to carry out the test.

Let's start with our leading example.

```{admonition} Example
    In the early 1970s, a young man challenged an Oklahoma state law that prohibited the sale of 3.2% beer to males under age 21 but allowed its sale to females in the same age group. The case (Craig v. Boren, 429 U.S. 190, 1976) was ultimately heard by the U.S. Supreme Court.

    The main justification provided by Oklahoma for the law was traffic safety. One of the 3 main pieces of data presented to the court was the result of a "random roadside survey" that recorded information on gender, and whether or not the driver had been drinking alcohol in the previous two hours. There were a total of 619 drivers under 20 years of age included in the survey.

    Here is what the collected data looked like:

    ```{figure} images/image126.gif
    :alt: A table with two columns, "Gender," and "Drove drunk?." Each row represents one occurrence. The rows in the table (in "Driver #: Gender, Drove Drunk?" format): Driver 1: M, Y; Driver 2: F, N; Driver 3: F, Y; ... Driver 619: M, N;

    A table with two columns, "Gender," and "Drove drunk?." Each row represents one occurrence. The rows in the table (in "Driver #: Gender, Drove Drunk?" format): Driver 1: M, Y; Driver 2: F, N; Driver 3: F, Y; ... Driver 619: M, N;
    ```

    The following two-way table summarizes the observed counts in the roadside survey:

    ```{figure} images/image127.gif
    :alt: A two-way table, in which the columns are labeled "Yes," "No," and "Total." The rows are labeled "Male," "Female," and "Total." Here is the data in the table, given in cell format ("Row, Column: Value"): Male, Yes: 77 Male, No: 404 Male, Total: 481 Female, Yes: 16 Female, No: 122 Female, Total: 138 Total, Yes: 93, Total, No: 526 Total, Total: 619

    A two-way table, in which the columns are labeled "Yes," "No," and "Total." The rows are labeled "Male," "Female," and "Total." Here is the data in the table, given in cell format ("Row, Column: Value"): Male, Yes: 77 Male, No: 404 Male, Total: 481 Female, Yes: 16 Female, No: 122 Female, Total: 138 Total, Yes: 93, Total, No: 526 Total, Total: 619
    ```

    Our task is to assess whether these results provide evidence of a significant ("real") relationship between gender and drunk driving.

    The following figure summarizes this example:

    ```{figure} images/image128.gif
    :alt: The population comprises of all drivers under 20. The question we have about the population is "is drunk driving (Y) related to gender (X)?" To answer this, we create a SRS of size 619 via a roadside survey. The results from this survey are summarized in the two-way table given above. Using Inference, we can figure out if the relationship of the roadside survey strong enough that we can conclude that it is due to a real relationship between drunk driving and gender in population.

    The population comprises of all drivers under 20. The question we have about the population is "is drunk driving (Y) related to gender (X)?" To answer this, we create a SRS of size 619 via a roadside survey. The results from this survey are summarized in the two-way table given above. Using Inference, we can figure out if the relationship of the roadside survey strong enough that we can conclude that it is due to a real relationship between drunk driving and gender in population.
    ```

    Note that as the figure stresses, since we are looking to see whether drunk driving is related to gender, our explanatory variable (X) is gender, and the response variable (Y) is drunk driving. Both variables are two-valued categorical variables, and therefore our two-way table of observed counts is 2-by-2. It should be mentioned that the chi-square procedure that we are going to introduce here is not limited to 2-by-2 situations, but can be applied to any r-by-c situation where r is the number of rows (corresponding to the number of values of one of the variables) and c is the number of columns (corresponding to the number of values of the other variable).

    Before we introduce the chi-square test, let's conduct an exploratory data analysis (that is, look at the data to get an initial feel for it). By doing that, we will also get a better conceptual understanding of the role of the test.

    *Exploratory Analysis*

    Recall that the key to reporting appropriate summaries for a two-way table is deciding which of the two categorical variables plays the role of explanatory variable, and then calculating the conditional percentages — the percentages of the response variable for each value of the explanatory variable — separately. In this case, since the explanatory variable is gender, we would calculate the percentages of drivers who did (and did not) drink alcohol for males and females separately.

    Here is the table of conditional percentages:

    ```{figure} images/image129.gif
    :alt: A two-way table, in which the columns are labeled "Yes," "No," (in response to the Y variable, drank alcohol in the last 2 hours) and "Total." The rows are labeled "Male" and "Female." Here is the data in the table, give in cell format ("Row, Column: Value"): Male, Yes: 77/481 = 16.0% Male, No: 404/481 = 84.0% Male, Total: 100% Female, Yes: 16/138 = 11.6% Female, No: 122/138 = 88.4% Female, Total: 100%

    A two-way table, in which the columns are labeled "Yes," "No," (in response to the Y variable, drank alcohol in the last 2 hours) and "Total." The rows are labeled "Male" and "Female." Here is the data in the table, give in cell format ("Row, Column: Value"): Male, Yes: 77/481 = 16.0% Male, No: 404/481 = 84.0% Male, Total: 100% Female, Yes: 16/138 = 11.6% Female, No: 122/138 = 88.4% Female, Total: 100%
    ```

    For the 619 sampled drivers, a larger percentage of males were found to be drunk than females (16.0% vs. 11.6%). Our data, in other words, provide some evidence that drunk driving is related to gender; however, this in itself is not enough to conclude that such a relationship exists in the larger population of drivers under 20. We need to further investigate the data and decide between the following two points of view:

    - The evidence provided by the roadside survey (16% vs 11.6%) is strong
                                    enough to conclude (beyond a reasonable doubt) that it must be due
                                    to a relationship between drunk driving and gender in the population
                                    of drivers under 20.
    - The evidence provided by the roadside survey (16% vs. 11.6%) is not
                                    strong enough to make that conclusion, and could have happened just
                                    by chance, due to sampling variability, and not necessarily because
                                    a relationship exists in the population.
```

Actually, these two opposing points of view constitute the null and alternative hypotheses of the chi-square test for independence, so now that we understand our example and what we still need to find out, let's introduce the four-step process of this test.

## Learn By Doing

The purpose of this activity is to introduce you to the example that you are going to work through in this section, and for you to get a feeling for the data by conducting exploratory analysis.

Background: Alcoholism Risk in 9/11 Responders

Among firefighters and other "first responders" to the World Trade Center on September 11, 2001, there have been reports of increased alcohol-related difficulties (e.g., DUI). A survey of 9/11 first responders (On the Front Line: The Work of First Responders in a Post-9/11 World) conducted by Cornell researcher Samuel Bacharach was released in 2004. To see the report, click [here](../../webcontent/FirefighterStress.pdf). Based on the research, we can construct the following two-way table of observed counts:

```{figure} images/image422.gif
:alt: A two-way table titled "Firefighters(*) vs. Alcohol Risk, Based on a 2004 Study of NY Firefighters." The columns are "No risk for alcohol problems**," "Moderate to Severe risk for alcohol problems**," and "Total". The rows are "Participated in 911 rescue," "Did Not Participate in 911 rescue," and "total." Here is the data in the table, given in cell format ("Row, Column: Value"): Participated, No risk: 783; Participated, Moderate to severe risk: 309; Participated, Total: 1102; Did Not, No risk: 441; Did Not, Moderate to severe risk: 110 Did Not, Total: 551; Total, No Risk: 1234; Total, Moderate to Severe risk: 419; Total, Total: 1653. (*): does not include officers (**): as defined by the DSM criteria (also used by the National Institute on Alcohol Abuse) and determined by survey results.

A two-way table titled "Firefighters(*) vs. Alcohol Risk, Based on a 2004 Study of NY Firefighters." The columns are "No risk for alcohol problems**," "Moderate to Severe risk for alcohol problems**," and "Total". The rows are "Participated in 911 rescue," "Did Not Participate in 911 rescue," and "total." Here is the data in the table, given in cell format ("Row, Column: Value"): Participated, No risk: 783; Participated, Moderate to severe risk: 309; Participated, Total: 1102; Did Not, No risk: 441; Did Not, Moderate to severe risk: 110 Did Not, Total: 551; Total, No Risk: 1234; Total, Moderate to Severe risk: 419; Total, Total: 1653. (*): does not include officers (**): as defined by the DSM criteria (also used by the National Institute on Alcohol Abuse) and determined by survey results.
```

Using the data from this research, we would like to investigate whether alcohol risk among New York firefighters is significantly related to participation in the 9/11 rescue.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
