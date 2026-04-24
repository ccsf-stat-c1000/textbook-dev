# Two Independent Samples (1 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Comparing Two Means—Two Independent Samples (The Two-Sample t-Test)

##### Overview

As we mentioned in the summary of the introduction to Case C→Q, the first case that we will deal with is comparing two means when the two samples are independent:

```{figure} images/image014.gif
:alt: Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. From Sub-population 1 we take an SRS of size n_1, and from Sub-population 2 we take an SRS of size n_2. Both of these samples are independent.

Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. From Sub-population 1 we take an SRS of size n_1, and from Sub-population 2 we take an SRS of size n_2. Both of these samples are independent.
```

Recall that here we are interested in the effect of a two-valued (k = 2) categorical variable (X) on a quantitative response (Y). Samples are drawn independently from the two sub-populations (defined by the two categories of X), and we need to evaluate whether or not the data provide enough evidence for us to believe that the two sub-population means are different.

In other words, our goal is to test whether the means μ~1~ and μ~2~ (which are the means of the variable of interest in the two sub-populations) are equal or not, and in order to do that we have two samples, one from each sub-population, which were chosen independently of each other. As the title of this part suggests, the test that we will learn here is commonly known as the *two-sample t-test*. As the name suggests, this is a t-test, which as we know means that the p-values for this test are calculated under some t distribution. Here is how this part is organized.

We first introduce our leading example, and then go in detail through the four steps of the two-sample t-test, illustrating each step using our example.

```{note}
:class: note
    Up until now, we have been dividing our population into *sub-populations*, then sampling from these sub-populations.

    From now on, instead of calling them sub-populations, we will usually call the groups we wish to compare *population 1, population 2,*and so on. These two descriptions of the groups we are comparing can be used interchangeably.
```

```{admonition} Example
    What is more important to you — personality or looks?

    This question was asked of a random sample of 239 college students, who were to answer on a scale of 1 to 25. An answer of 1 means personality has maximum importance and looks no importance at all, whereas an answer of 25 means looks have maximum importance and personality no importance at all. The purpose of this survey was to examine whether males and females differ with respect to the importance of looks vs. personality.

    R InstructionsStatCrunch InstructionsMinitab InstructionsExcel 2007 InstructionsExcel 2003 InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. To open R with the dataset preloaded, right-click [here](../../webcontent/r/looks.RData) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in R.The data have been loaded into the variable "looks." Enter the command `looks` to see the data.To open this file in StatCrunch you must first right-click [here](../../webcontent/excel/looks.xls) and choose "Save Target As" to download the file to your computer. Next click [here](http://www.statcrunch.com/)to open StatCrunch in a separate window and login using your username and password.Click on the link “Open StatCrunch” at the top of the My StatCrunch page. To open the data set select the “My computer” link under Load a data set from box on the left side of the page.Select the "Browse" or “Choose File” (depending on which browser you're using and select the data set you downloadedScroll to the bottom of the page and click on “Load File”To open Minitab with the data in the worksheet, right-click [here](../../webcontent/minitab/looks.mtw) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Minitab. Note: a dialog box will likely appear that says "A copy of the content of this file will be added to the current project"—just click "OK."To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/looks.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel.To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/looks.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel.To open a group of lists with the data loaded, right-click [here](../../webcontent/ti/looks.8xg) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and send it to your calculator. For instructions on how to connect your calculator to your computer and transfer a file, click here.L1: Score (Y) (-9999 represents missing data) L2: Gender (X) (1 = Female, 2 = Male) L3: Score (Y) for females (-9999 represents missing data) L4: Score (Y) for males (-9999 represents missing data) NOTE: For the TI, categorical data such as gender must be coded with numbers. To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/looks.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens, you may have to enable editing.To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/looks.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens, you may have to enable editing.

    Note that the data have the following format:

    | Score (Y) | Gender (X) |
    | --- | --- |
    | 15 | Male |
    | 13 | Female |
    | 10 | Female |
    | 12 | Male |
    | 14 | Female |
    | 14 | Male |
    | 6 | Male |
    | 17 | Male |
    | etc. |  |

    The format of the data reminds us that we are essentially examining the relationship between the two-valued categorical variable, gender, and the quantitative response, score. The two values of the categorical explanatory variable define the two populations that we are comparing — males and females. The comparison is with respect to the response variable score. Here is a figure that summarizes the example:

    ```{figure} images/image018.gif
    :alt: We have two populations, Females and Males. This is our Gender (X) Variable. For each of these populations, there is a Score (Y) mean, μ_1 for Females and μ_2 for Males. For the Female population we generate an SRS of size 150. For Males, we generate a SRS of size 85.

    We have two populations, Females and Males. This is our Gender (X) Variable. For each of these populations, there is a Score (Y) mean, μ_1 for Females and μ_2 for Males. For the Female population we generate an SRS of size 150. For Males, we generate a SRS of size 85.
    ```

    *Comments:*

    1. Note that this figure emphasizes how the fact that our explanatory is a two-valued categorical variable means that in practice we are comparing two populations (defined by these two values) with respect to our response Y.
    2. Note that even though the problem description just says that we had 239 students, the figure tells us that there were 85 males in the sample, and 150 females.
    3. Following up on comment 2, note that 85 + 150 = 235 and not 239. In these data (which are real) there are four "missing observations"—4 students for which we do not have the value of the response variable, "importance." This could be due to a number of reasons, such as recording error or nonresponse. The bottom line is that even though data were collected from 239 students, effectively we have data from only 235. (Recommended: Go through the data file and note that there are 4 cases of missing observations: students 34, 138, 179, and 183).
```

```{note}
    **Many Students Wonder**

    Two Independent Samples

    *(Interactive activity — available in the OLI platform)*
```

We will now introduce the two-sample t-test by going through its four steps.
