# Matched Pairs (1 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

## Comparing Two Means—Matched Pairs (Paired t-Test)

##### Overview

We are still in Case C→Q of inference about relationships, where the explanatory variable is categorical and the response variable is quantitative. As we mentioned in the introduction, we introduce three inferential procedures in this case.

So far we have introduced the first procedure—the two-sample t-test that is used when we are comparing two means and the samples are independent. We now move on to the second procedure, where we also compare two means, but the samples are paired or matched. Every observation in one sample is linked with an observation in the other sample. In this case, the samples are *dependent*.

```{figure} images/image051.gif
:alt: The X variable is a two-valued categorical explanatory variable. Using the categories we split the population into Population 1 and population 2. Each has its own Y mean, μ_1 and μ_2. For each population we generate a matched pair SRS of size n.

The X variable is a two-valued categorical explanatory variable. Using the categories we split the population into Population 1 and population 2. Each has its own Y mean, μ_1 and μ_2. For each population we generate a matched pair SRS of size n.
```

One of the most common cases where dependent samples occur is when both samples have the same subjects and they are "*paired by subject*." In other words, each subject is measured twice on the response variable, typically before and then after some kind of treatment/intervention in order to assess its effectiveness.

```{admonition} Example: SAT Prep Class
    Suppose you want to assess the effectiveness of an SAT prep class. It would make sense to use the matched pairs design and record each sampled student's SAT score before and after the SAT prep classes are attended:

    ```{figure} images/image052.gif
    :alt: The X variable is whether a student has gone to prep class (Yes/No). From this we split the population into two populations: Population 1 which has Students with no SAT prep class, and Population 2, which has students that take the SAT prep class. Each population has its own SAT Score (Y) Mean, which is μ_1 for population 1 and μ_2 for population 2. We use the same subjects in both samples, but when we generate the SRS for population 1, we do it before the students take the prep class, and after they take the prep class we generate the SRS for population 2.

    The X variable is whether a student has gone to prep class (Yes/No). From this we split the population into two populations: Population 1 which has Students with no SAT prep class, and Population 2, which has students that take the SAT prep class. Each population has its own SAT Score (Y) Mean, which is μ_1 for population 1 and μ_2 for population 2. We use the same subjects in both samples, but when we generate the SRS for population 1, we do it before the students take the prep class, and after they take the prep class we generate the SRS for population 2.
    ```

    Recall that the two populations represent the two values of the explanatory variable. In this situation, those two values come from *a single set of subjects*. In other words, both populations really have the *same students*. However, each population has a different value of the explanatory variable. Those values are: no prep class, prep class.
```

This, however, is not the only case where the paired design is used. Other cases are when the pairs are "natural pairs," such as siblings, twins, or couples. We will present two examples in this part. The first one will be of the type where each subject is measured twice, and the second one will be a study involving twins.

This section on matched pairs design will be organized very much like the previous section on two independent samples. We will first introduce our leading example, and then present the paired t-test illustrating each step using our example. We will then look at another example, and finally talk about estimation using a confidence interval. As usual, you'll be able to check your understanding along the way, and will learn how to use software to carry out this test.

```{admonition} Example: Drunk Drivers
    Drunk driving is one the main causes of car accidents. Interviews with drunk drivers who were involved in accidents and survived revealed that one of the main problems is that drivers do not realize that they are impaired, thinking "I only had 1-2 drinks ... I am OK to drive." A sample of 20 drivers was chosen, and their reaction times in an obstacle course were measured before and after drinking two beers. The purpose of this study was to check whether drivers are impaired after drinking two beers. Here is a figure summarizing this study:

    ```{figure} images/image053.gif
    :alt: The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.

    The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.
    ```
```

## Comments

1. Note that the categorical explanatory variable here is "drinking 2 beers (Yes/No)", and the quantitative response variable is the reaction time.
2. Note that by using the matched pairs design in this study (i.e., by measuring each driver twice), the researchers isolated the effect of the two beers on the drivers and eliminated any other confounding factors that might influence the reaction times (such as the driver's experience, age, etc.).
3. For each driver, the two measurements are the total reaction time before drinking two beers, and after. You can see the data by following these instructions:

R InstructionsStatCrunch InstructionsMinitab InstructionsExcel 2007 InstructionsExcel 2003 InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. To open R with the dataset preloaded, right-click [here](../../webcontent/r/beers.RData) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in R. The data have been loaded into the variable "beers." Enter the command `beers` to see the data.To open this file in StatCrunch you must first right-click [here](../../webcontent/excel/beers.xls) and choose "Save Target As" to download the file to your computer. Next click [here](http://www.statcrunch.com/)to open StatCrunch in a separate window and login using your username and password.Click on the link “Open StatCrunch” at the top of the My StatCrunch page. To open the data set select the “My computer” link under Load a data set from box on the left side of the page.Select the "Browse" or “Choose File” (depending on which browser you're using and select the data set you downloadedScroll to the bottom of the page and click on “Load File”To open Minitab with the data in the worksheet, right-click [here](../../webcontent/minitab/beers.mtw) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Minitab. Note: you will likely see a dialog box appear that says "A copy of the content of this file will be added to the current project"—just click "OK." To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/beers.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. To open Excel with the data in the worksheet, right-click [here](../../webcontent/excel/beers.xls) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. To open a group of lists with the beer data loaded, right-click [here](../../webcontent/ti/beers.8xg) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and send it to your calculator. For instructions on how to connect your calculator to your computer and transfer a file, click here.L1 contains "Before drinking" data and L2 contains "After drinking" data. Choose STAT/EDIT/1:Edit to see the data.To open Excel with the data in the worksheet, click [here](../../webcontent/excel/beers.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens, you may have to enable editing.To open Excel with the data in the worksheet, click [here](../../webcontent/excel/beers.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens, you may have to enable editing.
