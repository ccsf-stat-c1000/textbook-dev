# The Chi-Square Test: Hypotheses and the Big Idea

```{admonition} Learning Objectives
:class: note

- In a given context, carry out the appropriate inferential method for examining relationships and draw the appropriate conclusions.
- Specify the null and alternative hypotheses for comparing relationships.
```

## The Chi-Square Test for Independence

The chi-square test for independence examines our observed data and tells us whether we have enough evidence to conclude beyond a reasonable doubt that two categorical variables are related. Much like the previous part on the ANOVA F-test, we are going to introduce the hypotheses (step 1), and then discuss the idea behind the test, which will naturally lead to the test statistic (step 2). Let's start.

## Step 1: Stating the Hypotheses

Unlike all the previous tests that we presented, the null and alternative hypotheses in the chi-square test are stated in words rather than in terms of population parameters. They are:

- $H_0$: There is no relationship between the two categorical variables. (They are independent.)
- $H_a$: There is a relationship between the two categorical variables. (They are not independent.)

:::{admonition} Example: Drunk Driving and Gender
:class: tip

In our example, the null and alternative hypotheses state:

- $H_0$: There is no relationship between gender and drunk driving.
- $H_a$: There is a relationship between gender and drunk driving.

Or equivalently,

- $H_0$: Drunk driving and gender are independent.
- $H_a$: Drunk driving and gender are not independent.

Hence the name "chi-square test for independence."
:::

```{admonition} Comment
:class: important

Algebraically, independence between gender and driving drunk is equivalent to having equal proportions who drank (or did not drink) for males vs. females. In fact, the null and alternative hypotheses could have been re-formulated as:

- $H_0$: proportion of male drunk drivers = proportion of female drunk drivers
- $H_a$: proportion of male drunk drivers ≠ proportion of female drunk drivers

However, while expressing the hypotheses in terms of proportions works well and is quite intuitive for 2-by-2 tables, the formulation becomes very cumbersome when at least one of the variables has several possible values, not just two. We are therefore going to always stick with the "wordy" form of the hypotheses presented in step 1 above.
```

## The Idea of the Chi-Square Test

The idea behind the chi-square test, much like previous tests that we've introduced, is to measure how far the data are from what is claimed in the null hypothesis. The further the data are from the null hypothesis, the more evidence the data present against it. We'll use our data to develop this idea. Our data are represented by the observed counts:

| Observed | Yes | No | Total |
| --- | --- | --- | --- |
| **Male** | 77 | 404 | 481 |
| **Female** | 16 | 122 | 138 |
| **Total** | 93 | 526 | 619 |

How will we represent the null hypothesis?

In the previous tests we introduced, the null hypothesis was represented by the null value. Here there is not really a null value, but rather a claim that the two categorical variables (drunk driving and gender, in this case) are independent.

To represent the null hypothesis, we will calculate another set of counts—the counts that we would *expect* to see (instead of the observed ones) if drunk driving and gender were really independent (i.e., if $H_0$ were true). For example, we actually observed 77 males who drove drunk; if drunk driving and gender were indeed independent (if $H_0$ were true), how many male drunk drivers would we expect to see instead of 77? Similarly, we can ask the same kind of question about (and calculate) the other three cells in our table.

In other words, we will have two sets of counts:

- the *observed* counts (the data), and
- the *expected* counts (if $H_0$ were true).

We will measure how far the observed counts are from the expected ones. Ultimately, we will base our decision on the size of the discrepancy between what we observed and what we would expect to observe if $H_0$ were true.

How are the expected counts calculated? Once again, we are in need of probability results. Recall from the probability unit that if events A and B are independent, then P(A and B) = P(A) × P(B). We use this rule for calculating expected counts, one cell at a time.

Applying the rule to the first (top left) cell, if driving drunk and gender were independent, then

$$P(\text{drunk and male}) = P(\text{drunk}) \cdot P(\text{male})$$

By dividing the counts in our table, we see that P(drunk) = 93/619 and P(male) = 481/619, and so

$$P(\text{drunk and male}) = \frac{93}{619}\cdot\frac{481}{619}$$

Therefore, since there is a total of 619 drivers, *if drunk driving and gender were independent*, the *count* of drunk male drivers that we would *expect* to see is:

$$619 \cdot P(\text{drunk and male})=619\cdot\frac{93}{619}\cdot\frac{481}{619}=\frac{93\cdot481}{619}\approx72.3$$

Notice that this expression is the product of the column and row totals for that particular cell, divided by the overall table total.

Similarly, if the variables are independent, the expected count of females driving drunk would be

$$\frac{93\cdot138}{619}\approx20.7$$

Again, the expected count equals the product of the corresponding column and row totals, divided by the overall table total. This will always be the case, and will help streamline our calculations:

```{admonition} Expected Count
:class: note

$$\text{Expected count}=\frac{\text{column total}\times\text{row total}}{\text{table total}}$$
```

Here is the complete table of expected counts (compare it with the table of observed counts above):

| Expected | Yes | No | Total |
| --- | --- | --- | --- |
| **Male** | (93 × 481)/619 = 72.3 | (526 × 481)/619 = 408.7 | 481 |
| **Female** | (93 × 138)/619 = 20.7 | (526 × 138)/619 = 117.3 | 138 |
| **Total** | 93 | 526 | 619 |

## Did I Get This?

A study was done on the relationship between gender and piercing among high-school students. A sample of 1,000 students was chosen, then classified according to gender and according to whether or not they had any of their ears pierced. The results of the study are summarized in the following 2-by-2 table:

| | Pierced: Yes | Pierced: No | Total |
| --- | --- | --- | --- |
| **Female** | 576 | 64 | 640 |
| **Male** | 72 | 288 | 360 |
| **Total** | 648 | 352 | 1,000 |

:::{quiz} If gender and ear piercing were independent, what is the expected count of females with pierced ears?
:hint: Expected count = (column total × row total)/table total = (648 × 640)/1000.
:feedback-0: Correct! (648 × 640)/1000 = 414.7.
:feedback-1: 576 is the OBSERVED count, not the expected one.
:feedback-2: Use the column total (648) times the row total (640), divided by the table total (1,000).
* *414.7
* 576
* 640
:::

:::{quiz} The observed count of pierced females (576) is much higher than the expected count under independence (414.7). What does this discrepancy suggest?
:hint: Big gaps between observed and expected counts are evidence about H₀.
:feedback-0: Correct! A large discrepancy between observed and expected counts is evidence against independence—the chi-square statistic will quantify whether it is large enough to be significant.
:feedback-1: The discrepancy points AWAY from independence, not toward it.
:feedback-2: We can't skip the test—the test statistic and p-value determine whether the discrepancy is larger than chance would produce.
* *The data appear far from what independence predicts—evidence against H₀, to be quantified by the test
* The data support the null hypothesis of independence
* We can already conclude a relationship exists, with no test needed
:::

We see that there are differences between the observed and expected counts in the respective cells. We now have to come up with a measure that will quantify these differences. This is the chi-square test statistic.
