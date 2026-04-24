# Exploratory Data Analysis (2 of 2)

Before we jump into exploratory data analysis and really appreciate its importance in the process of statistical analysis, let's step back for a minute and ask:

What do we really mean by *data*?

*Data* are pieces of information about individuals organized into variables. By an *individual*, we mean a particular person or object. By a *variable*, we mean a particular characteristic of the individual.

A *dataset* is a set of data identified with particular circumstances. Datasets are typically displayed in tables, in which rows represent individuals and columns represent variables.

```{admonition} Example: Medical Records
    The following dataset shows medical records from a particular survey:

    ```{figure} images/introduction1.gif
    :alt: A table in which the rows represent patients and each column represents a variable. For example, the third row is for Patient #3, and each cell in the row is in a particular column. The first column is Gender, and Patient #3&apos;s gender is female, so there is an F in the first column of the third row.

    A table in which the rows represent patients and each column represents a variable. For example, the third row is for Patient #3, and each cell in the row is in a particular column. The first column is Gender, and Patient #3&apos;s gender is female, so there is an F in the first column of the third row.
    ```

    In this example, the individuals are patients, and the variables are Gender, Age, Weight, Height, Smoking, and Race. Each row, then, gives us all the information about a particular individual (in this case, patient), and each column gives us information about a particular characteristic of all the patients.
```

Variables can be classified into one of two types: categorical or quantitative.

- *Categorical variables* take category or label values and place an individual into one of several groups. Each observation can be placed in *only* one category, and the categories are mutually exclusive. In our example of medical records, Smoking is a categorical variable, with two groups, since each participant can be categorized only as either a nonsmoker or a smoker. Gender and Race are the two other categorical variables in our medical records example. Notice that the values of the categorical variable Smoking have been coded as the numbers 1 or 2. It is common to code the values of a categorical variable as numbers, but you should remember that these are just codes. They have no arithmetic meaning (i.e., it does not make sense to add, subtract, multiply, divide, or compare the magnitude of such values).
- *Quantitative variables* take numerical values and represent some kind of measurement. In our medical example, Age is an example of a quantitative variable because it can take on multiple numerical values. It also makes sense to think about it in numerical form; that is, a person can be 18 years old or 80 years old. Weight and Height are also examples of quantitative variables.

```{note}
    Categorical variables are sometimes called *qualitative* variables, but in this course we use the term categorical.
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

## Let's Explore a Dataset

In this activity we

- Learn how to open and examine a dataset.
- Practice classifying variables by their type: quantitative or categorical.
- Learn how to handle categorical variables whose values are numerically coded.

##### Background to Dataset

Clinical depression is the most common mental illness in the United States, affecting 19 million adults each year (Source: NIMH, 1999). Nearly 50% of individuals who experience a major episode will have a recurrence within 2 to 3 years. Researchers are interested in comparing therapeutic solutions that could delay or reduce the incidence of recurrence.

In a study conducted by the National Institutes of Health, 109 clinically depressed patients were separated into three groups, and each group was given one of two active drugs (imipramine or lithium) or no drug at all. For each patient, the dataset contains the treatment used, the outcome of the treatment, and several other interesting characteristics.

Here is a summary of the variables in our dataset:

- *Hospt:*The patient's hospital, represented by a code for each of the 5 hospitals (1, 2, 3, 5, or 6)
- *Treat:* The treatment received by the patient (Lithium, Imipramine, or Placebo)
- *Outcome:*Whether or not a recurrence occurred during the patient's treatment (Recurrence or No Recurrence)
- *Time:* Either the time in days till the first recurrence, or if a recurrence did not occur, the length in days of the patient's participation in the study
- *AcuteT:* The time in days that the patient was depressed prior to the study
- *Age:* The age of the patient in years, when the patient entered the study
- *Gender:* The patient's gender (1 = Female, 2 = Male)

```{note}
    R InstructionsStatCrunch InstructionsMinitab InstructionsExcel 2013 and 2016 InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. To open R (a free software environment for statistical computing and graphics) with the data preloaded, right-click [here](../webcontent/r/depression.RData) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in R.The data have been loaded into the variable "depression." Enter the command `depression` to see the data.*Note: Using R—*Throughout the Learn By Doing activities in this course, you will be given commands to execute in R. You can use the following steps to avoid having to type all of these commands in by hand:  
    Highlight the command with your mouse.On the browser menu, click "Edit," then "Copy."Click on the R command window, then at the top of the R window, click "Edit," then "Paste."You may have to press <Enter> to execute the command.When you enter the command `depression` into R, you will see a large data table. Each row of this table contains the values of the variables associated with a single individual, and the different variables are separated into columns. The columns are labeled with the variable names.If we simply wanted to observe only Age information we can extract that specific variable from the data frame by connecting the data frame name to the column name using the $ symbol, such as in the following command: `depression$Age`To open this file in StatCrunch, you must first right-click [here](../webcontent/excel/depression.xls) and choose "Save Target As" to download the file to your computer. Next, click [here](http://www.statcrunch.com/) to open StatCrunch in a separate window and log in using your username and password.  
    Click on the link "Open StatCrunch" at the top of the My StatCrunch page.To open the dataset, choose `Data → Load → From file → on my computer`.Select "Browse" or "Choose File" (depending on which browser you're using) and select the dataset you downloaded.Scroll to the bottom of the page and click on "Load File."The data is displayed in tabular form. Each row contains the values of the variables associated with a single individual, and the different variables are separated in columns. Rows are referred to by number 1, 2, 3, etc. Columns are labeled by default as var1, var2, etc. It is helpful if the columns are labeled with the variable names, as in our case.Often, it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do this in StatCrunch:  
    Choose `Data → Compute → Expression`. This will bring up the Compute Expression window.In the Expression input field, enter `ifelse(Gender = 1,Female,Male)`, then press Compute!Notice that a new column is created at the right with the desired recoding.Finally, we will want to delete the original `Gender` column and give this name to the new column. To delete the original Gender column:  
    Choose `Edit → Columns → Delete` to bring up the Delete Columns window.Under the `Select Columns` heading, select `Gender`. Then press Compute!To rename the new column, double-click on the current name and press the Delete key. Then type in the new name.To open Minitab with the data in the worksheet, click [here](../webcontent/minitab/depression.mtw) (in some browsers, right-click and choose "Save Target As" to download the file to your computer. Then find the downloaded file and double-click it to open it in Minitab.) Note: a dialog box will likely appear that says "A copy of the content of this file will be added to the current project"—just click "OK."In Minitab, the dataset is displayed in tabular form in the bottom part of the screen called "worksheet." Each row contains the values of the variables associated with a single individual, and the different variables are separated in columns. Rows are referred to by R1, R2, etc. Columns can be referred to by column names or by C1, C2, etc. It is helpful if the columns are labeled with the variable names, as in our case. To open the dataset, click [here](../webcontent/excel/depression.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing. To open a group of lists with the depression data loaded, right-click [here](../webcontent/ti/depression.8xg) and choose "Save Target As" to download the file to your computer. Then find the downloaded file and send it to your calculator. For instructions on how to connect your calculator to your computer and transfer a file, click here.On the TI calculator, the dataset is displayed in lists L1-L6, and an extra list named GEND.   
    L1: Hospt L2: Treat (0=Lithium, 1=Imipramine, or 2=Placebo) L3: Outcome (1=Recurrence/Failure or 0=No Recurrence/Success) L4: Time L5: AcuteT L6: Age GEND: Gender (1 = Female, 2 = Male) Use these directions to look over the data in the various lists:  
    To access one of the built-in lists (L1-L6), press `2ND` and then the number of the list, followed by `ENTER`. For example, to access L1, you would press `2ND/1/ENTER`.To access a non-built-in list, use the `LIST` menu (`2nd/STAT`). Press `LIST/NAMES` and then scroll down to the desired list and press `ENTER` and then `ENTER` again.Use the right and left arrows to scroll through the list.You can also choose `Stat/Edit/1:Edit` to see L1-L6 in table form. You can scroll through the table using the arrow keys.Note that in order to see the GEND list in the table, you have to add it. To do so:  
    Choose `STAT/EDIT/1:Edit`Use the up arrow and the right arrow keys to position the cursor on the name of the last list in the table (for most cases, this will be L6). Now press the right arrow key once. This will create a new list.Name the new list `GEND` and you will see the data for that list show up in the table.Each row in the table contains the values of the variables associated with a single individual, and the different variables are represented by the lists. Rows are referred to by (1), (2), etc. To open the dataset, click [here](../webcontent/excel/depression.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing. To open the dataset, click [here](../webcontent/excel/depression.xls) to download the file to your computer. Then find the downloaded file and double-click it to open it in Excel. When Excel opens you may have to enable editing.
```

```{note}
    StatCrunch InstructionsR InstructionsMinitab InstructionsExcel 2013 and 2016 InstructionsTI InstructionsExcel 2019 PCExcel 2019 MacTip: Alternative versions are available, click the arrow to switch. Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do this in StatCrunch:  
    Choose `Data → Transform data →` This will bring up the Transform data window.In the Expression input field enter: `ifelse(Gender = 1,Female,Male)` then press `Compute`Notice that a new column is created at the right with the desired recoding.Finally, we will want to delete the original Gender column and give this name to the new column.To delete the original Gender column:  
    Choose `Edit → Columns → Delete`In the Columns Delete Window, Select `Gender and press Delete`To rename the new column click on the current name and press the Delete key. Then type in the new namesOften it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." Copy the entire following command into R:`depression$Gender = replace(depression$Gender,depression$Gender==1,'Female'); depression$Gender = replace(depression$Gender,depression$Gender==2,'Male'); depression$Gender`Remember, you may have to press <Enter> to execute the command.Notice that the column Gender now contains the meaningful labels "Female" and "Male" where before it contained "1" and "2" codes.*Note: Using R -*To learn more about any command you see in these notes, enter `help` (command) into R or check out the resources listed under the Help menu.Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do that in Minitab:  
    Choose Data → Code → Numeric to text... This will bring up the Code—Numeric to Text dialog box.To fill in "Code data from columns":   
    Double click on the variable you wish to recode in the left panel. We will choose Gender.To fill in "Store coded data in columns":   
    Double click on the column in which you wish to place the recoded variable. We will choose Gender again, to replace the existing variable.To fill in "Original values" and "New":   
    Enter 1 and "Female" in the first row of boxesEnter 2 and "Male" in the second row of boxesClick OK. Notice that the column Gender now contains the meaningful labels "Female" and "Male" where before it contained "1" and "2" codes.Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do that in Excel:  
    Click on the column header above the `Gender` column. In this case, Gender is in column G, so click on the column header labeled `G`. This will select the entire column of gender values.Choose `Find & Select → Replace` from the `Editing` group in the `Home` tab to bring up the Find and Replace window.In the first textbox labeled `Find what:`, enter "1".In the second textbox labeled `Replace with`, enter "Female".Now click the button labeled `Replace All`. This will replace all of the "1" values in our selected column with the word "Female".Now do the same thing for males:In the first textbox labeled `Find what:`, enter "2".In the second textbox labeled `Replace with`, enter "Male"Click the `Replace All` button, and then click the `Close` button.Notice that the column Gender now contains the meaningful labels "Female" and "Male" where before it contained "1" and "2" codes.Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. However, the TI can only handle categorical data with each category represented by a number. Look at the data in row 1 for L1-L6 and GEND. Interpret what this data represents for the first individual (row 1 in each list). Then check your answers in this table: Note: Under L4, in the first row you probably see 36.143. In order to see all the decimal places, highlight the 36.143, then look at the bottom of the screen. You should see L4(1)=36.14300156.Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do that in Excel:  
    Click on the column header above the *Gender*column. In this case, Gender is in column G, so click on the column header labeled *G*. This will select the entire column of gender values.In the *Home*tab under the *Editing* group, choose *Find & Select → Replace* to bring up the Find and Replace window.In the first textbox labeled *Find what:*, enter "1".In the second textbox labeled *Replace with*, enter "Female".Now click the button labeled *Replace All*. This will replace all of the "1" values in our selected column with the word "Female". Press *OK* to close the dialog box that was launched.Now do the same thing for males:In the first textbox labeled *Find what:*, enter "2".In the second textbox labeled *Replace with*, enter "Male"Click the *Replace All* button and press *OK*to close the dialog box. Then click the *Close*button.Notice that the column Gender now contains the meaningful labels "Female" and "Male" where before it contained "1" and "2" codes.Often it is easier to use labels for categorical variables that are as close as possible to the meanings of the categories. Now we will recode the variable gender with the labels "Male" and "Female." To do that in Excel:  
    Click on the column header above the *Gender*column. In this case, Gender is in column G, so click on the column header labeled *G*. This will select the entire column of gender values.In the *Home*tab, choose *Find & Select → Replace* to bring up the Replace window.In the first textbox labeled *Find what:*, enter "1".In the second textbox labeled *Replace with*, enter "Female".Now click the button labeled *Replace All*. This will replace all of the "1" values in our selected column with the word "Female". Press *OK* to close the dialog box that was launched.Now do the same thing for males:In the first textbox labeled *Find what:*, enter "2".In the second textbox labeled *Replace with*, enter "Male"Click the *Replace All* button and press *OK*to close the dialog box. Then click the *Close*button.Notice that the column Gender now contains the meaningful labels "Female" and "Male" where before it contained "1" and "2" codes.
```

## Did I Get This?

- *Hospt:* The patient’s hospital, represented by a code for each of the five hospitals (1, 2, 3, 5, and 6)
- *Treat:* The treatment received by the patient (Lithium, Imipramine, or Placebo)
- *Outcome:* Whether a recurrence occurred during the patient’s treatment (Recurrence or No Recurrence)
- *Time:* Either the time in days until the first recurrence or, if a recurrence did not occur, the length in days of the patient’s participation in the study
- *AcuteT:* The time in days that the patient was depressed prior to the study
- *Age:* The age of the patient in years when the patient entered the study
- *Gender:* The patient’s gender (1 = Female; 2 = Male)

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

```{note}
    **Learnmore**

    Scales of Measurement / Types of Variables

    *(Interactive activity — available in the OLI platform)*
```
