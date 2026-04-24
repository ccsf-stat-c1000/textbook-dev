# Case C→C (4 of 5)

```{admonition} Learning Objectives
    - In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
```

## Step 3: Finding the p-value

The p-value for the chi-square test for independence is the probability of getting counts like those observed, assuming that the two variables are not related (which is what is claimed by the null hypothesis). The smaller the p-value, the more surprising it would be to get counts like we did, if the null hypothesis were true.

Technically, the p-value is the probability of observing $\chi^{2}$ at least as large as the one observed. Using statistical software, we find that the p-value for this test is 0.201.

## Step 4: Stating the conclusion in context

As usual, we use the magnitude of the p-value to draw our conclusions. A small p-value indicates that the evidence provided by the data is strong enough to reject H~o~ and conclude (beyond a reasonable doubt) that the two variables are related. In particular, if a significance level of .05 is used, we will reject H~o~ if the p-value is less than .05.

```{admonition} Example
    A p-value of .201 is not small at all. There is no compelling statistical evidence to reject H~o~, and so we will continue to assume it may be true. Gender and drunk driving may be independent, and so the data suggest that a law that forbids sale of 3.2% beer to males and permits it to females is unwarranted. In fact, the Supreme Court, by a 7-2 majority, struck down the Oklahoma law as discriminatory and unjustified. In the majority opinion Justice Brennan wrote (http://www.law.umkc.edu/faculty/projects/ftrials/conlaw/craig.html):

    "Clearly, the protection of public health and safety represents an important function of state and local governments. However, appellees' statistics in our view cannot support the conclusion that the gender-based distinction closely serves to achieve that objective and therefore the distinction cannot under [prior case law] withstand equal protection challenge."
```

The purpose of this activity is to draw our conclusion regarding the relationship between participation in the 9/11 rescue and risk of alcohol problems among New York firefighters and first responders.

```{note}
    R InstructionsStatCrunch InstructionsMinitab InstructionsExcel 2013 and 2016 Instructions InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. In the previous activity, we entered observed counts into R and calculated expected counts. This time we enter the same observed counts and conduct a chi-squared test for association on the data.Use the following command to create a data frame of the actual counts into R:  
    `data = data.frame(no.risk=c(793,441), moderate.to.severe.risk=c(309,110), row.names=c("participated","did.not.participate"))``data`Then use this command to calculate the test statistic and p-value for the chi-square test for association (independence):  
    `chisq.test(data)`In the previous activity, we carried out the chi-square test using StatCrunch and obtained the following output:*Contingency table results:*Rows: 911Columns: NoneIn the previous activity, we carried out the chi-square test using Minitab and obtained the following output:In the previous activity, we created a table of expected counts to go along with our table of observed counts. In this activity, we will use both of these tables to conduct a chi-square test on the data.To do this in Excel, we first need to re-create both the table of observed counts and table of expected counts from the last exercise. Here are the data again for your convenience:Now use the `CHITEST` function in Excel to calculate the p-value given the data in our tables. To do this, pick an empty cell and type `=CHITEST([actual range], [expected range])` where [actual range] is the range of observed data in our table (without row/column headers or totals) and [expected range] is the range of expected data in our table (again without row/column headers or totals). For example, assuming that the top left cell in the table above is A1, the formula would be `=CHITEST(B3:C4, B8:C9)`.In the previous activity, we carried out the chi-square test and obtained the following output:In the previous activity, we created a table of expected counts to go along with our table of observed counts. In this activity, we will use both tables to conduct a chi-square test on the data.To do this in Excel, we first need to re-create both the table of observed counts and table of expected counts from the last exercise. Here are the data again for your convenience: Now use the function *CHITEST* in Excel to calculate the p-value given the data in our tables. To do this, pick an empty cell and type *=CHITEST(actual range, expected range)*where*actual range* is the range of observed data in our table (without row/column headers or totals) and *expected range* is the range of expected data in our table (again without row/column headers or totals). For example, assuming that the top left cell in the table above is A1, the formula would be *=CHITEST(B3:C4, B8:C9)*.In the previous activity, we created a table of expected counts to go along with our table of observed counts. In this activity, we will use both tables to conduct a chi-square test on the data.To do this in Excel, we first need to re-create both the table of observed counts and table of expected counts from the last exercise. Here are the data again for your convenience: Now use the function *CHITEST* in Excel to calculate the p-value given the data in our tables. To do this, pick an empty cell and type *=CHITEST(actual range, expected range)*where*actual range* is the range of observed data in our table (without row/column headers or totals) and *expected range* is the range of expected data in our table (again without row/column headers or totals). For example, assuming that the top left cell in the table above is A1, the formula would be *=CHITEST(B3:C4, B8:C9)*.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

## Comment

This is a good opportunity to illustrate an important idea that was discussed earlier in this unit: The larger the sample the results are based on, the more evidence they carry. Let's take the previous example and simply multiply each of the counts by 3:

```{figure} images/image144.gif
:alt: A two-way table for observed counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; (categories of Drank Alcohol in the last 2 hours?) and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 231; Male, No: 1212; Male, Total: 1443; Female, Yes: 48; Female, No: 366; Female, Total: 414; Total, Yes: 279; Total, No: 1578; Total, Total: 1875;

A two-way table for observed counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; (categories of Drank Alcohol in the last 2 hours?) and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 231; Male, No: 1212; Male, Total: 1443; Female, Yes: 48; Female, No: 366; Female, Total: 414; Total, Yes: 279; Total, No: 1578; Total, Total: 1875;
```

and see what would have happened if these were the original data. Obviously, the conditional counts would remain the same:

```{figure} images/image145.gif
:alt: A two-way table for conditional counts, in which the columns are labeled &quot;Yes&quot; and &quot;No&quot; (categories of Drank Alcohol in the last 2 hours?). The rows are labeled &quot;Male&quot; and &quot;Female.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 231/1443 = 16.0% Male, No: 1212/1443 = 84.0% Female, Yes: 48/414 = 11.6% Female, No: 366/414 = 88.4%

A two-way table for conditional counts, in which the columns are labeled &quot;Yes&quot; and &quot;No&quot; (categories of Drank Alcohol in the last 2 hours?). The rows are labeled &quot;Male&quot; and &quot;Female.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 231/1443 = 16.0% Male, No: 1212/1443 = 84.0% Female, Yes: 48/414 = 11.6% Female, No: 366/414 = 88.4%
```

In other words, the sample provides the "same" results, but this time they are based on a much larger sample (1857 instead of 619). This is reflected by the chi-square test. In this case, software gives us a chi-square statistic of 4.910 and a p-value of 0.027.

As before, H~o~ states that gender and drunk driving are not related; H~a~ states that they are related. Since the observed counts are triple what they were before, the expected counts are also tripled. When done with software the original chi-square statistic was 1.637 since software doesn't round as much. The chi-square statistic when we tripled the data is 3 times 1.637, or 4.91 (which now is in the "large" range). Therefore, the p-value is smaller and is now .027.

Now, we do reject H~o~, and we conclude that gender and drunk driving are related. In this case, the "largest contribution to chi-square" is large enough to provide evidence of a relationship. This is due to the fact that so few females drove drunk (48) compared to the number that would be expected (62.2, which is 414 * 279 / 1857) if the variables gender and drunk driving were not related. This contribution is $\frac{\left(48−62.2\right)^{2}}{62.2}=3.242$.
