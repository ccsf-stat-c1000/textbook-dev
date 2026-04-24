# Matched Pairs (6 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing groups.
```

The "driving after having 2 beers" example is a case in which observations are paired by subject. In other words, both samples have the same subject, so that each subject is measured twice. Typically, as in our example, one of the measurements occurs before a treatment/intervention (2 beers in our case), and the other measurement after the treatment/intervention. Our next example is another typical type of study where the matched pairs design is used—it is a study involving twins.

```{admonition} Example
    Researchers have long been interested in the extent to which intelligence, as measured by IQ score, is affected by "nurture" as opposed to "nature": that is, are people's IQ scores mainly a result of their upbringing and environment, or are they mainly an inherited trait? A study was designed to measure the effect of home environment on intelligence, or more specifically, the study was designed to address the question: "Are there significant differences in IQ scores between people who were raised by their birth parents, and those who were raised by someone else?"

    In order to be able to answer this question, the researchers needed to get two groups of subjects (one from the population of people who were raised by their birth parents, and one from the population of people who were raised by someone else) who are as similar as possible in all other respects. In particular, since genetic differences may also affect intelligence, the researchers wanted to control for this confounding factor.

    We know from our discussion on study design (in the Producing Data unit of the course) that one way to (at least theoretically) control for all confounding factors is randomization—randomizing subjects to the different treatment groups. In this case, however, this is not possible. This is an observational study; you cannot randomize children to either be raised by their birth parents or to be raised by someone else. How else can we eliminate the genetics factor? We can conduct a "twin study."

    Because identical twins are genetically the same, a good design for obtaining information to answer this question would be to compare IQ scores for identical twins, one of whom is raised by birth parents and the other by someone else. Such a design (matched pairs) is an excellent way of making a comparison between individuals who only differ with respect to the explanatory variable of interest (upbringing) but are as alike as they can possibly be in all other important aspects (inborn intelligence). Identical twins raised apart were studied by Susan Farber, who published her studies in the book "Identical Twins Reared Apart" (1981, Basic Books). In this problem, we are going to use the data that appear in Farber's book in table E6, of the IQ scores of 32 pairs of identical twins who were reared apart.

    Here is a figure that will help you understand this study:

    ```{figure} images/image083.gif
    :alt: The variable X takes on two categories: Upbringing by birth parents or someone else. These two categories form population 1 and population 2. For each population, we have a IQ (Y) mean, μ_1 for population 1 and μ_2 for population 2. We generate the samples in matched pairs by using the relationship of twins separated at birth. So, we generate an SRS of size 32 for population 1 and also one of size 32 for population 2 using this relationship, paired by twins.

    The variable X takes on two categories: Upbringing by birth parents or someone else. These two categories form population 1 and population 2. For each population, we have a IQ (Y) mean, μ_1 for population 1 and μ_2 for population 2. We generate the samples in matched pairs by using the relationship of twins separated at birth. So, we generate an SRS of size 32 for population 1 and also one of size 32 for population 2 using this relationship, paired by twins.
    ```

    Here are the important things to note in the figure:

    1. We are essentially comparing the mean IQ scores in two populations that are defined by our (two-valued categorical) explanatory variable — upbringing (X), whose two values are: raised by birth parents, raised by someone else.
    2. This is a matched pairs design (as opposed to a two independent samples design), since each observation in one sample is linked (matched) with an observation in the second sample. The observations are paired by twins.

    To look at the data set, follow these instructions:

    R InstructionsStatCrunch InstructionsMinitab InstructionsExcel 2007 InstructionsExcel 2003 InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. To open R with the dataset preloaded, right-click [here](../../webcontent/r/twins.RData) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in R. The data have been loaded into the variable "twins." Enter the command `twins` to see the data.To open this file in StatCrunch you must first right-click [here](../../webcontent/excel/twins.xls) and choose "Save Target As" to download the file to your computer. Next click [here](http://www.statcrunch.com/)to open StatCrunch in a separate window and login using your username and password.Click on the link “Open StatCrunch” at the top of the My StatCrunch page. To open the data set select the “My computer” link under Load a data set from box on the left side of the page.Select the "Browse" or “Choose File” (depending on which browser you're using and select the data set you downloadedScroll to the bottom of the page and click on “Load File”To open Minitab with the data in the worksheet, right-click [here](../../webcontent/minitab/twins.mtw) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Minitab. Note: you will likely see a dialog box appear that says "A copy of the content of this file will be added to the current project"—just click "OK." To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/twins.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/twins.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. To open a group of lists with the twins data loaded, right-click [here](../../webcontent/ti/twins.8xg) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and send it to your calculator. For instructions on how to connect your calculator to your computer and transfer a file, click here.The data have been loaded into L1 (Twin 1) and L2 (Twin 2). Choose STAT/EDIT/1:Edit to see the data.To open Excel with the data in the worksheet, click [here](../../webcontent/excel/twins.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing.To open Excel with the data in the worksheet, click [here](../../webcontent/excel/twins.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing.

    Each of the 32 rows represents one pair of twins. Keeping the notation that we used above, twin 1 is the twin that was raised by his/her birth parents, and twin 2 is the twin that was raised by someone else. Let's carry out the analysis.

    1. *Stating the hypotheses.* Recall that in matched pairs, we reduce the data from two samples to one sample of differences: and we state our hypotheses in terms of the mean of the differences, $\mu_{d}$. Since we would like to test whether there are differences in IQ scores between people who were raised by their birth parents and those who weren't, we are carrying out the two-sided test: *Comment:* Again, some students find it easier to first think about the hypotheses in terms of μ~1~ and μ~2~, and then write them in terms of $\mu_{d}$. In this case, since we are testing for differences between the two populations, the hypotheses will be: and since $\mu_{d}=\mu_{1}−\mu_{2}$ we get back to the hypotheses above.
    2. *Checking conditions and summarizing the data with a test statistic.* Is it safe to use the paired t-test in this case? The data don't reveal anything that we should be worried about (like very extreme skewness or outliers), so we can safely proceed. Looking at the histogram, we note that most of the differences are negative, indicating that in most of the 32 pairs of twins, twin 2 (raised by someone else) has a higher IQ. From this point we rely on statistical software, and find that: Our test statistic is -1.85. Our data (represented by the average of the differences) are 1.85 standard errors below the null hypothesis (represented by the null value 0).
      1. Clearly, the samples of twins are not random samples from the two populations. However, in this context, they can be considered as random, assuming that there is nothing special about the IQ of a person just because he/she has an identical twin.
      2. The sample size here is n = 32. Even though it's the case that if we use the n > 30 rule of thumb our sample can be considered large, it is sort of a borderline case, so just to be on the safe side, we should look at the histogram of the differences just to make sure that we do not see anything extreme. (Comment: Looking at the histogram of differences in every case is useful even if the sample is very large, just in order to get a sense of the data. Recall: "Always look at the data.")
      - t-value = -1.85
      - p-value = 0.074
    3. *Finding the p-value.* The p-value is 0.074, indicating that there is a 7.4% chance of obtaining data like those observed (or even more extreme) assuming that H~o~ is true (i.e., assuming that there are no significant differences in IQ scores between people who were raised by their natural parents and those who weren't).
    4. *Making conclusions.* Using the conventional significance level (cut-off probability) of .05, our p-value is not small enough, and we therefore cannot reject H~o~. In other words, our data do not provide enough evidence to conclude that whether a person was raised by his/her natural parents has an impact on the person's intelligence (as measured by IQ scores).
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

## Comment:

This means that if, based on prior knowledge, prior research, or just a hunch, we had wanted to test the hypothesis that the IQ level of people raised by their birth parents is lower, on average, than the IQ level of people who were raised by someone else, we would have rejected H~o~ and accepted that hypothesis (at the .05 significance level, since .037 < .05).

It should be stressed, though, that one should set the hypotheses before looking at the data. It would be ethically wrong to look at the histogram of differences, note that most of the differences are negative, and then decide to carry out the one-sided test that the data seem to support. This is known as "data snooping," and is considered to be a very bad statistical practice.

```{note}
    **Learn By Doing**

    Matched Pairs

    *(Interactive activity — available in the OLI platform)*
```
