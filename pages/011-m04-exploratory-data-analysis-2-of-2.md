# Exploratory Data Analysis (2 of 2)

Before we jump into exploratory data analysis and really appreciate its importance in the process of statistical analysis, let's step back for a minute and ask:

What do we really mean by *data*?

*Data* are pieces of information about individuals organized into variables. By an *individual*, we mean a particular person or object. By a *variable*, we mean a particular characteristic of the individual.

A *dataset* is a set of data identified with particular circumstances. Datasets are typically displayed in tables, in which rows represent individuals and columns represent variables.

## Example: Medical Records
The following dataset shows medical records from a particular survey:

```{figure} images/introduction1.gif
:alt: A table in which the rows represent patients and each column represents a variable. For example, the third row is for Patient #3, and each cell in the row is in a particular column. The first column is Gender, and Patient #3&apos;s gender is female, so there is an F in the first column of the third row.
```

In this example, the individuals are patients, and the variables are Gender, Age, Weight, Height, Smoking, and Race. Each row, then, gives us all the information about a particular individual (in this case, patient), and each column gives us information about a particular characteristic of all the patients.

Variables can be classified into one of two types: categorical or quantitative.

- *Categorical variables* take category or label values and place an individual into one of several groups. Each observation can be placed in *only* one category, and the categories are mutually exclusive. In our example of medical records, Smoking is a categorical variable, with two groups, since each participant can be categorized only as either a nonsmoker or a smoker. Gender and Race are the two other categorical variables in our medical records example. Notice that the values of the categorical variable Smoking have been coded as the numbers 1 or 2. It is common to code the values of a categorical variable as numbers, but you should remember that these are just codes. They have no arithmetic meaning (i.e., it does not make sense to add, subtract, multiply, divide, or compare the magnitude of such values).
- *Quantitative variables* take numerical values and represent some kind of measurement. In our medical example, Age is an example of a quantitative variable because it can take on multiple numerical values. It also makes sense to think about it in numerical form; that is, a person can be 18 years old or 80 years old. Weight and Height are also examples of quantitative variables.

```{note}
Categorical variables are sometimes called *qualitative* variables, but in this course we use the term categorical.
```

## Concept Check
We took a random sample from the 2000 U.S. Census. Here is part of the dataset:

```{figure} images/eda_intro_lbd.png
```

:::{quiz} Who are the individuals described by this data?
:hint: Individuals are the people or objects described by the data.
:explanation: The U.S. Census is completed by people living in the United States.
* States
* People with families in the year 2000
* *People living in the United States in the year 2000
:::

:::{quiz} What type of variable is zipcode?
:hint: A categorical variable puts individuals into categories. A quantitative variable is a numerical measurement that can be averaged.
:explanation: Zipcode is a categorical variable because it categorizes individuals by geographic location.
* Quantitative
* *Categorical
:::

:::{quiz} What type of variable is Family_Size?
:hint: A categorical variable puts individuals into categories. A quantitative variable is a numerical measurement that can be averaged.
:explanation: Family_Size is a variable with numerical values that can be averaged.
* *Quantitative
* Categorical
:::

:::{quiz} What type of variable is Annual_income?
:hint: A categorical variable puts individuals into categories. A quantitative variable is a numerical measurement that can be averaged.
:explanation: Annual_income is a variable with numerical values that can be averaged.
* *Quantitative
* Categorical
:::