# Two-Way Tables: Relationships Between Categories (Case $C \to C)$

## Case $C \to C$: Two Categorical Variables

Recall the role-type classification table for framing our discussion about the relationship between two variables:

```{figure} images/gen/m05-role-type-cc.svg
:alt: The role-type classification table with the C to C cell highlighted, indicating that this part covers a categorical explanatory variable paired with a categorical response variable.
```

We are done with case $C \to Q$, and will now move on to case $C \to C$, where we examine the relationship between two categorical variables.

Earlier in the course (when we discussed the distribution of a *single* categorical variable) we examined the data obtained when a random sample of 1,200 U.S. college students were asked about their body image (underweight, overweight, or about right). We are now returning to this example, to address the following question:

If we had separated our sample of 1,200 U.S. college students by gender and looked at *males and females separately*, would we have found a similar distribution across body-image categories? More specifically, are men and women just as likely to think their weight is about right? Among those students who do not think their weight is about right, is there a difference between the genders in feelings about body image?

Answering these questions requires us to *examine the relationship between two categorical variables*, gender and body image. Because the question of interest is whether there is a gender effect on body image,

- the *explanatory* variable is *gender*, and
- the *response* variable is *body image*.

Here is what the raw data look like when we include the gender of each student:

| Student | Gender | Body Image |
| --- | --- | --- |
| ... | ... | ... |
| student 25 | M | overweight |
| student 26 | M | about right |
| student 27 | F | underweight |
| student 28 | F | about right |
| student 29 | M | about right |
| ... | ... | ... |

Once again the raw data is a long list of 1,200 genders and responses, and thus not very useful in that form. To start our exploration of how body image is related to gender, we need an informative display that summarizes the data. In order to summarize the relationship between two categorical variables, we create a display called a {term}`two-way table`.

Here is the two-way table for our example:

| Gender | About right | Overweight | Underweight | Total |
| --- | --- | --- | --- | --- |
| Female | 560 | 163 | 37 | 760 |
| Male | 295 | 72 | 73 | 440 |
| **Total** | **855** | **235** | **110** | **1200** |

The table has the possible genders in the rows, and the possible responses regarding body image in the columns. At each intersection between row and column, we put the counts for how many times that combination of gender and body image occurred in the data. We sum across the rows to fill in the Total column, and we sum across the columns to fill in the Total row.

## Check Your Understanding: Reading a Two-Way Table

:::{quiz} Using the two-way table, how many of the sampled students are males who feel their weight is about right?
:hint: Find the cell where the Male row meets the About right column.
:feedback-0: 560 is the count of females who feel about right.
:feedback-1: Correct! The Male row and About right column intersect at 295.
:feedback-2: 440 is the total number of males in the sample, across all body-image categories.
* 560
* *295
* 440
:::

:::{quiz} How many students in the sample are female?
:hint: Look at the Total column for the Female row.
:feedback-0: Correct! Summing across the Female row: $560 + 163 + 37 = 760$.
:feedback-1: 855 is the total number of students (of both genders) who feel about right.
:feedback-2: 1200 is the total number of students in the entire sample.
* *760
* 855
* 1200
:::

```{admonition} Comment
:class: important

Note that from the way the two-way table is constructed, the Total row or column is a summary of one of the two categorical variables, ignoring the other. In our example:

- The Total row gives the summary of the categorical variable body image, ignoring gender: 855 about right, 235 overweight, 110 underweight. (These are the same counts we got earlier in the course when we looked at the single categorical variable body image, and did not consider gender.)
- The Total column gives the summary of the categorical variable gender, ignoring body image: 760 females and 440 males.
```
