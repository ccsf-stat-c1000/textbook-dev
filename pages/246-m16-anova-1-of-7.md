# ANOVA (1 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Comparing More Than Two Means—ANOVA

##### Overview

In this part, we continue to handle situations involving one categorical explanatory variable and one quantitative response variable, which is case C→Q in our role/type classification table:

```{figure} images/image093.gif
:alt: It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).

It is possible for any type of explanatory variable to be paired with any type of response variable. The possible pairings are: Categorical Explanatory → Categorical Response (C→C), Categorical Explanatory → Quantitative Response (C→Q), Quantitative Explanatory → Categorical Response (Q→C), and Quantitative Explanatory → Quantitative Response (Q→Q).
```

So far we have discussed the two samples and matched pairs designs, in which the categorical explanatory variable is two-valued. As we saw, in these cases, examining the relationship between the explanatory and the response variables amounts to comparing the mean of the response variable (Y) in two populations, which are defined by the two values of the explanatory variable (X). The difference between the two samples and matched pairs designs is that in the former, the two samples are independent, and in the latter, the samples are dependent.

We are now moving on to cases in which the categorical explanatory variable takes more than two values. Here, as in the two-valued case, making inferences about the relationship between the explanatory (X) and the response (Y) variables amounts to comparing the means of the response variable in the populations defined by the values of the explanatory variable, where the number of means we are comparing depends, of course, on the number of values of X. Unlike the two-valued case, where we looked at two sub-cases (1) when the samples are independent (two samples design) and (2) when the samples are dependent (matched pairs design, here, we are just going to discuss the case where the samples are independent. In other words, we are just going to extend the two samples design to more than two independent samples.

```{figure} images/image094.gif
:alt: The Explanatory (X): has k values. This means we have k populations, and for each population a Y mean μ. Each of these populations also has a sample, each with its own size. We end up with k independent samples.

The Explanatory (X): has k values. This means we have k populations, and for each population a Y mean μ. Each of these populations also has a sample, each with its own size. We end up with k independent samples.
```

##### Comment

The extension of the matched pairs design to more than two dependent samples is called "Repeated Measures" and is beyond the scope of this course.

The inferential method for comparing more than two means that we will introduce in this part is called Analysis Of Variance (abbreviated as ANOVA), and the test associated with this method is called the ANOVA F-test. The structure of this part will be very similar to that of the previous two. We will first present our leading example, and then introduce the ANOVA F-test by going through its 4 steps, illustrating each one using the example. (It will become clear as we explain the idea behind the test where the name "Analysis of Variance" comes from.) We will then present another complete example, and conclude with some comments about possible follow-ups to the test. As usual, you'll have activities along the way to check your understanding, and learn how to use software to carry out the test.

Let's start by introducing our leading example.

```{admonition} Example
    Is "academic frustration" related to major?

    A college dean believes that students with different majors may experience different levels of academic frustration. Random samples of size 35 of Business, English, Mathematics, and Psychology majors are asked to rate their level of academic frustration on a scale of 1 (lowest) to 20 (highest).

    ```{figure} images/image095.gif
    :alt: The X variable is major, and it has four categories, which are Business, English, Mathematics, and Psychology. We have four populations, one for each of these categories. We are interested in the level of frustration (Y) mean for each population, so we have 4 μ, one for each population. For each population we take a sample of size 35, resulting in 4 separate samples.

    The X variable is major, and it has four categories, which are Business, English, Mathematics, and Psychology. We have four populations, one for each of these categories. We are interested in the level of frustration (Y) mean for each population, so we have 4 μ, one for each population. For each population we take a sample of size 35, resulting in 4 separate samples.
    ```

    The figure highlights what we have already mentioned: examining the relationship between major (X) and frustration level (Y) amounts to comparing the mean frustration levels ($\mu_{1},\mu_{2},\mu_{3},\mu_{4}$ ) among the four majors defined by X. Also, the figure reminds us that we are dealing with a case where the samples are independent.
```

##### Comment

There are two ways to record data in the ANOVA setting:

- Unstacked: One column for each of the four majors, with each column listing the frustration levels reported by all sampled students in that major: BusinessEnglishMathPsychology11119116916196141113etc.
- Stacked: one column for all the frustration levels, and next to it a column to keep track of which major a student is in: Frustration(Y)Major(X)9Business2Business9Business10English11Psychology13English13Psychology12Mathetc.

The "unstacked" format helps us to look at the four groups separately, while the "stacked" format helps us remember that there are, in fact, two variables involved: frustration level (the quantitative response variable) and major (the categorical explanatory variable).

StatCrunch InstructionsExcel 2007 InstructionsMinitab InstructionsR InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. To open this file in StatCrunch you must first right-click [here](../../webcontent/excel/frustration.xls) and choose "Save Target As" to download the file to your computer. Next click [here](http://www.statcrunch.com/)to open StatCrunch in a separate window and login using your username and password.Click on the link “Open StatCrunch” at the top of the My StatCrunch page. To open the data set select the “My computer” link under Load a data set from box on the left side of the page.Select the "Browse" or “Choose File” (depending on which browser you're using and select the data set you downloadedScroll to the bottom of the page and click on “Load File”Note that in the first 4 columns, the data are in unstacked format, and in the next two columns the data are stacked.To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/frustration.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. Note that in the first 4 columns (A-D), the data are in unstacked format, and in the next two columns (E-F) the data are stacked.To open Minitab with the data in the worksheet, right-click [here](../../webcontent/minitab/frustration.mtw) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Minitab. Note: you will likely see a dialog box appear that says "A copy of the content of this file will be added to the current project"—just click "OK." Note that in the first 4 columns (c1-c4), the data are in unstacked format, and in the next two columns (c5-c6) the data are stacked.To open R with the dataset preloaded, right-click [here](../../webcontent/r/frustration.RData) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in R. The data have been loaded into the variable "frustration." Enter the command `frustration` to see the data.Note that in the first 4 columns, the data are in unstacked format, and in the next two columns the data are stacked.To open a group of lists with the data, right-click [here](../../webcontent/ti/frustration.8xg) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and send it to your calculator. For instructions on how to connect your calculator to your computer and transfer a file, click here.UNGROUP frustration.8xgL1 frustration (for Business) L2 frustration (for English) L3 frustration (for Mathematics) L4 frustration (for Psychology) L5 Frustration (Y) L6 Major (X) (1=Business, 2=English, 3=Mathematics, 4=Psychology). Note that in the first 4 lists (L1-L4), the data are in unstacked format: L1 (Business), L2 (English) , L3 (Mathematics), L4 (Psychology); and in the next two lists (L5-L6) the data are stacked: L5 (Frustration(Y)), L6 (Major(X) with 1=Business, 2=English, 3=Mathematics, 4=Psychology).To open Excel with the data in the worksheet, click [here](../../webcontent/excel/frustration.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing.Note that in the first 4 columns (A-D), the data are in unstacked format, and in the next two columns (E-F) the data are stacked.To open Excel with the data in the worksheet, click [here](../../webcontent/excel/frustration.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing.Note that in the first 4 columns (A-D), the data are in unstacked format, and in the next two columns (E-F) the data are stacked.
