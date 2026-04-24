# Case C→C (3 of 5)

```{admonition} Learning Objectives
    - In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
```

## Step 2: Checking the Conditions and Calculating the Test Statistic

Given our discussion on the previous page, it would be natural to present the test statistic, and then come back to the conditions that allow us to safely use the chi-square test, although in practice this is done the other way around.

The single number that summarizes the overall difference between observed and expected counts is the chi-square statistic $\chi^{2}$ , which tells us in a standardized way how far what we observed (data) is from what would be expected if H~o~ were true.

Here it is:

$\chi^{2}=\sum_{all cells}\frac{\left(Observed Count−ExpectedCount\right)^{2}}{Expected Count}$

## Comment

As we expected, $\chi^{2}$ is based on each of the differences: observed count - expected count (one such difference for each cell), but why is it squared? Why do we divide each square difference by the expected count? The reason we do that is so that the null distribution of $\chi^{2}$ will have a known null distribution (under which p-values can be easily calculated). The details are really beyond the scope of this course, but we will just say that the null distribution of $\chi^{2}$ is called chi-square (which is not very surprising given that the test is called the chi-square test), and like the t-distributions there are many chi-square distributions distinguished by the number of degrees of freedom associated with them.

## Conditions under Which the Chi-Square Test Can Safely Be Used

1. The sample should be random.
2. In general, the larger the sample, the more accurate and reliable the test results are. There are different versions of what the conditions are that will ensure reliable use of the test, all of which involve the expected counts. One version of the conditions says that all expected counts need to be greater than 1, and at least 80% of expected counts need to be greater than 5. A more conservative version requires that all expected counts are larger than 5.

```{admonition} Example
    Here, again, are the observed and expected counts.

    ```{figure} images/image141.gif
    :alt: A two-way table for observed and expected counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: observed: 77 expected: 72.3 Male, No: observed: 404 expected: 408.7 Male, Total: 481 Female, Yes: observed: 16, expected: 20.7 Female, No: observed: 122, expected: 117.3 Female, Total: 138 Total, Yes: 93, Total, No: 526 Total, Total: 619

    A two-way table for observed and expected counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: observed: 77 expected: 72.3 Male, No: observed: 404 expected: 408.7 Male, Total: 481 Female, Yes: observed: 16, expected: 20.7 Female, No: observed: 122, expected: 117.3 Female, Total: 138 Total, Yes: 93, Total, No: 526 Total, Total: 619
    ```

    Checking the conditions:

    1. The roadside survey is known to have been random.
    2. All the expected counts are above 5. We can therefore safely proceed with the chi-square test, and the chi-square test statistic is: $\frac{\left(77−72.3\right)^{2}}{72.3}+\frac{\left(404−408.7\right)^{2}}{408.7}+\frac{\left(16−20.7\right)^{2}}{20.7}+\frac{\left(122−117.3\right)^{2}}{117.3}=.306+.054+1.067+.188=1.62$
```

## Did I Get This?

RStatCrunchMinitabExcelTI CalculatorExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. A study was done on the relationship between gender and ear piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following information is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, and then classified according to both gender and whether or not they had either of their ears pierced. The following (edited) StatCrunch output is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following (edited) Minitab is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following information is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following information is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following information is available:A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to both gender and whether or not they had either of their ears pierced. The following information is available:

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

Once the chi-square statistic has been calculated, we can get a feel for its size: is there a relatively large difference between what we observed and what the null hypothesis claims, or a relatively small one? It turns out that for a 2-by-2 case like ours, we are inclined to call the chi-square statistic "large" if it is larger than 3.84. Therefore, our test statistic is not large, indicating that the data are not different enough from the null hypothesis for us to reject it (we will also see that in the p-value not being small). For other cases (other than 2-by-2) there are different cut-offs for what is considered large, which are determined by the null distribution in that case. We are therefore going to rely only on the p-value to draw our conclusions. Even though we cannot really use the chi-square statistic, it was important to learn about it, since it encompasses the idea behind the test.

## Did I Get This?

The purpose of this activity is to continue to explore whether the risk of alcohol problems among New York firefighters and first responders is related to participation in the 911 rescue. In particular, in this activity, we will state the hypotheses that are being tested, learn how to carry out the chi-square test for independence using statistical software, and check whether the conditions under which this test can be safely used are met.

|  | No risk for alchohol problems | Moderate to Servere risk for alcohol problems | Total |
| --- | --- | --- | --- |
| Participated in 911 rescue | 793 | 309 | *1102* |
| Did Not Participate in 911 rescue | 441 | 110 | *551* |
| Total | *1234* | *419* | *1653* |

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

In this activity, we check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you'll need to first launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").

```{note}
    R InstructionsMinitab InstructionsExcel 2013 and 2016 Instructions InstructionsStatCrunch InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To enter the actual (observed) counts into R, open R. Then, use the following command:  
    `data=data.frame(no.risk=c(793,441),moderate.to.severe.risk=c(309,110),row.names=``c("participated","did.not.participate"));data`Then use this command to calculate the expected counts:  
    `chisq.test(data)$expected`Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To enter the actual (observed) counts into Minitab, open Minitab. Then, use the following command:  
    Enter the observed counts as they appear in the table above (not including the totals) into columns C1 and C2.Name C1 "No Risk" and C2 "M to S Risk."Choose Stat → Tables → Chi-Square Test (Table in Worksheet).Under "Columns containing the table," enter C1 and C2.Click OK.Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To use Excel to calculate the expected counts:  
    Open Excel and create a table for expected counts with the same row and column headings as in the above observed data table.Use the formula `Expected Count = (Column Total * Row Total)/Table Total` in each cell to complete the table of expected counts.Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To enter the actual (observed) counts into StatCrunch, open StatCrunch and complete the following steps:  
    Enter Yes and No in column var1Enter the observed counts as they appear in the table above (not including the totals) into columns var2 and var3Rename var1 as “911,” var2 as “No Risk,” and var3 as “M to S Risk” Choose Stat → Tables → Contingency → with summarySelect the columns “No Risk” and “M to S Risk”Select Row labels in “911”Press “Next”Check “Expected Count” and “Chi-Square”Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To enter the actual (observed) counts into your TI Calculator, use the following steps:*Chi-square test for independence*  
    Enter the data in Matrix A: Press `MATRIX (2ND/x^-1^` on TI 84; `MATRIX` button on old TI83) You should see: Press the right arrow twice to choose `EDIT`. Choose 1:[A]. You should see: NOTE: Your screen may be different if another matrix was previously entered in [A]. You need to enter: number of rows X number of columns. The rows entry will be highlighted. Enter the number of categories for the explanatory variable. Use the right arrow (or `ENTER`) to move to the columns entry. Note that the correct number of rows is now displayed. Enter the number of categories for the response variable. Use the down arrow (or `ENTER`) to move to the entry for the first row, first column. Note that the correct number of columns is now displayed. Enter counts (no totals) from your two-way table. You should see: Choose `STAT/TESTS/C: X^2^-Test`. Enter the correct matrix for the observed values (the values you just entered from the two-way table) and any matrix for the expected values calculated by the TI. Note:You can always use the default values of [A] for observed and [B] for expected. To use matrices other than [A] or [B], position the cursor to the right of observed: (or expected) and press `MATRIX/NAMES/` choose a matrix name. You should see: Choose `Calculate`, then `ENTER`. You should see: Note: degrees of freedom df = (number of rows - 1)(number of columns - 1)To see the expected values calculated by your TI: Choose `MATRIX (2ND/x^-1^` on TI 84; `MATRIX` button on old TI83) You should see: Press the right arrow twice to choose `EDIT`. Choose 2:[B]. Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To use Excel to calculate the expected counts:  
    Open Excel and create a table for expected counts with the same row and column headings as in the above observed data table.Use the formula *Expected Count = (Column Total * Row Total)/Table Total* in each cell to complete the table of expected counts.Now you will check whether the conditions under which the chi-square test can be safely used are met. In order to do this, you will need to do the following two things:  
    Launch the actual [research report](../../webcontent/FirefighterStress.pdf) and read the last paragraph on page iii of the introduction (starting with "The study was fully funded...").Use the observed data from the above table to calculate the expected counts.To use Excel to calculate the expected counts:  
    Open Excel and create a table for expected counts with the same row and column headings as in the above observed data table.Use the formula *Expected Count = (Column Total * Row Total)/Table Total* in each cell to complete the table of expected counts.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```
