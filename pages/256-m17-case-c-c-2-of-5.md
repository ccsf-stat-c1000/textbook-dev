# Case C→C (2 of 5)

```{admonition} Learning Objectives
    - In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing relationships.
```

## The Chi-Square Test for Independence

The chi-square test for independence examines our observed data and tells us whether we have enough evidence to conclude beyond a reasonable doubt that two categorical variables are related. Much like the previous part on the ANOVA F-test, we are going to introduce the hypotheses (step 1), and then discuss the idea behind the test, which will naturally lead to the test statistic (step 2). Let's start.

## Step 1: Stating the hypotheses

Unlike all the previous tests that we presented, the null and alternative hypotheses in the chi-square test are stated in words rather than in terms of population parameters. They are:

*H*~*o*~: There is no relationship between the two categorical variables. (They are independent.)

*H*~*a*~: There is a relationship between the two categorical variables. (They are not independent.)

```{admonition} Example: Title
    In our example, the null and alternative hypotheses would then state:

    *H*~*o*~: There is no relationship between gender and drunk driving.

    *H*~*a*~: There is a relationship between gender and drunk driving.

    Or equivalently,

    *H*~*o*~: Drunk driving and gender are independent

    *H*~*a*~: Drunk driving and gender are not independent

    and hence the name "chi-square test for independence."
```

## Comment

Algebraically, independence between gender and driving drunk is equivalent to having equal proportions who drank (or did not drink) for males vs. females. In fact, the null and alternative hypotheses could have been re-formulated as

*H*~*o*~*:* proportion of male drunk drivers = proportion of female drunk drivers

*H*~*a*~*:*proportion of male drunk drivers ≠ proportion of female drunk drivers

However, expressing the hypotheses in terms of proportions works well and is quite intuitive for two-by-two tables, but the formulation becomes very cumbersome when at least one of the variables has several possible values, not just two. We are therefore going to always stick with the "wordy" form of the hypotheses presented in step 1 above.

## The Idea of the Chi-Square Test

The idea behind the chi-square test, much like previous tests that we've introduced, is to measure how far the data are from what is claimed in the null hypothesis. The further the data are from the null hypothesis, the more evidence the data presents against it. We'll use our data to develop this idea. Our data are represented by the observed counts:

```{figure} images/image131.gif
:alt: The two-way table with counts. The cells which are not in a Total row or column are the observed counts. Full description: A two-way table, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619; The observed counts are Male, Yes; Male, No; Female, Yes; Female, No;

The two-way table with counts. The cells which are not in a Total row or column are the observed counts. Full description: A two-way table, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619; The observed counts are Male, Yes; Male, No; Female, Yes; Female, No;
```

How will we represent the null hypothesis?

In the previous tests we introduced, the null hypothesis was represented by the null value. Here there is not really a null value, but rather a claim that the two categorical variables (drunk driving and gender, in this case) are independent.

To represent the null hypothesis, we will calculate another set of counts — the counts that we would expect to see (instead of the observed ones) if drunk driving and gender were really independent (i.e., if H~o~ were true). For example, we actually observed 77 males who drove drunk; if drunk driving and gender were indeed independent (if H~o~ were true), how many male drunk drivers would we expect to see instead of 77? Similarly, we can ask the same kind of question about (and calculate) the other three cells in our table.

In other words, we will have two sets of counts:

- the observed counts (the data)
- the expected counts (if H~o~ were true)

We will measure how far the observed counts are from the expected ones. Ultimately, we will base our decision on the size of the discrepancy between what we observed and what we would expect to observe if H~o~ were true.

How are the expected counts calculated? Once again, we are in need of probability results. Recall from the probability section that if events A and B are independent, then P(A and B) = P(A) * P(B). We use this rule for calculating expected counts, one cell at a time.

Here again are the observed counts:

```{figure} images/image132.gif
:alt: A two-way table, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;

A two-way table, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;
```

Applying the rule to the first (top left) cell, if driving drunk and gender were independent then:

P(drunk and male) = P(drunk) * P(male)

By dividing the counts in our table, we see that:

P(Drunk) = 93 / 619 and

P(Male) = 481 / 619,

and so,

P(Drunk and Male) = (93 / 619) (481 / 619)

Therefore, since there are total of 619 drivers, *if drunk driving and gender were independent*, the *count*of drunk male drivers that I would *expect* to see is:

$619*P\left(Drunk and Male\right)=619\left(\frac{93}{619}\right)\left(\frac{481}{619}\right)=\frac{93*481}{619}$

Notice that this expression is the product of the column and row totals for that particular cell, divided by the overall table total.

```{figure} images/image133.gif
:alt: P(Drunk and Male) is calculated using 3 cells from the two-way table. These are the row total (Male, Total) cell, the column total (Total, Yes) cell, and table total (Total, Total) cell. P(Drunk and Male) = (column total * row total)/(table total)

P(Drunk and Male) is calculated using 3 cells from the two-way table. These are the row total (Male, Total) cell, the column total (Total, Yes) cell, and table total (Total, Total) cell. P(Drunk and Male) = (column total * row total)/(table total)
```

Similarly, if the variables are independent,

P(Drunk and Female) = P(Drunk) * P(Female) = (93 / 619) (138 / 619)

and the expected count of females driving drunk would be

$\left(\frac{93}{619}\right)\left(\frac{138}{619}\right)=\frac{93*138}{619}$

Again, the expected count equals the product of the corresponding column and row totals, divided by the overall table total:

```{figure} images/image134.gif
:alt: P(Drunk and Female) is calculated using 3 cells from the two-way table. These are the row total (Female, Total) cell, the column total (Total, Yes) cell, and table total (Total, Total) cell. P(Drunk and Female) = (column total * row total)/(table total)

P(Drunk and Female) is calculated using 3 cells from the two-way table. These are the row total (Female, Total) cell, the column total (Total, Yes) cell, and table total (Total, Total) cell. P(Drunk and Female) = (column total * row total)/(table total)
```

This will always be the case, and will help streamline our calculations:

$Expected Count=\frac{Column Total*Row Total}{Table Total}$

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

Here is the complete table of expected counts, followed by the table of observed counts:

```{figure} images/image136.gif
:alt: A two-way table for expected counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: (93 * 481)/619 = 72.3; Male, No: (526 * 481)/619 = 408.7; Male, Total: 481; Female, Yes: (93 * 138)/619 = 20.7; Female, No: (526 * 138)/619 = 117.3; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;

A two-way table for expected counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: (93 * 481)/619 = 72.3; Male, No: (526 * 481)/619 = 408.7; Male, Total: 481; Female, Yes: (93 * 138)/619 = 20.7; Female, No: (526 * 138)/619 = 117.3; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;
```

```{figure} images/image137.gif
:alt: A two-way table for observed counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;

A two-way table for observed counts, in which the columns are labeled &quot;Yes,&quot; &quot;No,&quot; and &quot;Total.&quot; The rows are labeled &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Male, Yes: 77; Male, No: 404; Male, Total: 481; Female, Yes: 16; Female, No: 122; Female, Total: 138; Total, Yes: 93; Total, No: 526; Total, Total: 619;
```

## Did I Get This?

A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to gender and according to whether or not they had any of their ears pierced. The results of the study are summarized in the following 2-by-2 table:

```{figure} images/image425.gif
:alt: A two way table with &quot;Yes Piercing,&quot; &quot;No Pierceing,&quot; and &quot;Total&quot; columns. The rows are &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Female, Yes: 576; Female, No: 64; Female, Total: 640; Male, Yes: 72; Male, No: 288; Male, Total: 360; Total, Yes: 648; Total, No: 352; Total, Total: 1000

A two way table with &quot;Yes Piercing,&quot; &quot;No Pierceing,&quot; and &quot;Total&quot; columns. The rows are &quot;Male,&quot; &quot;Female,&quot; and &quot;Total.&quot; Here is the data in the table, given in cell format (&quot;Row, Column: Value&quot;): Female, Yes: 576; Female, No: 64; Female, Total: 640; Male, Yes: 72; Male, No: 288; Male, Total: 360; Total, Yes: 648; Total, No: 352; Total, Total: 1000
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

We see that there are differences between the observed and expected counts in the respective cells. We now have to come up with a measure that will quantify these differences. This is the chi-square test statistic.
