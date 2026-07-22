# Lurking Variables in Action: The SAT Score Gap

The next example will illustrate another way in which a lurking variable might interfere and prevent us from reaching any causal conclusions.

::::{admonition} Example: SAT Test
:class: tip

For U.S. colleges and universities, a standard entrance examination is the SAT test. The side-by-side boxplots below provide evidence of a relationship between the student's country of origin (the United States or another country) and the student's SAT Math score.

```{figure} images/gen/m05-sat-boxplots.svg
:alt: Side-by-side vertical boxplots of SAT Math scores for U.S. students and students from other countries. The international students' boxplot sits noticeably higher: its median, about 700, exceeds the third quartile of the U.S. students' scores.
```

The distribution of international students' scores is higher than that of U.S. students. The international students' median score (about 700) exceeds the third quartile of U.S. students' scores. Can we conclude that the country of origin is the *cause* of the difference in SAT Math scores, and that students in the United States are weaker at math than students in other countries?

No, not necessarily. While it *might* be true that U.S. students differ in math ability from other students—i.e. due to differences in educational systems—we can't conclude that a student's country of origin is the cause of the disparity. One important *lurking variable* that might explain the observed relationship is the educational level of the two populations taking the SAT Math test. In the United States, the SAT is a standard test, and therefore a broad cross-section of all U.S. students (in terms of educational level) take this test. Among all international students, on the other hand, only those who plan on coming to the U.S. to study, which is usually a more selected subgroup, take the test.

The following figure will help you visualize this explanation:

```{figure} images/gen/m05-confounding-diagram.svg
:alt: A diagram in which both X, nationality, and the lurking variable, education level of SAT takers, have arrows labeled possible cause pointing to Y, the SAT Math score. A dashed red line labeled confounded connects nationality and the lurking variable, indicating that their effects on the response cannot be separated.
```

Here, the explanatory variable (X) *may* have a causal relationship with the response variable (Y), but the lurking variable might be a contributing factor as well, which makes it very hard to isolate the effect of the explanatory variable and prove that it has a causal link with the response variable. In this case, we say that the lurking variable is *confounded* with the explanatory variable, since their effects on the response variable cannot be distinguished from each other.
::::

Note that in each of the above two examples, the lurking variable interacts differently with the variables studied. In the first example, the lurking variable has an effect on both the explanatory and the response variables, creating the illusion that there is a causal link between them. In the second example, the lurking variable is confounded with the explanatory variable, making it hard to assess the isolated effect of the explanatory variable on the response variable.

The distinction between these two types of interactions is not as important as the fact that in either case, the observed association can be at least partially explained by the lurking variable. The most important message from these two examples is therefore: *An observed association between two variables is not enough evidence that there is a causal relationship between them.*

In other words ...

```{admonition} Principle
:class: note

Association *does not* imply causation!
```

## Check Your Understanding: Correlation and Causation

:::{quiz} A study finds a strong positive correlation between ice cream sales and the number of drownings, month by month. What is the most reasonable explanation?
:hint: What third variable rises and falls with both ice cream sales and swimming activity?
:feedback-0: It's very unlikely that eating ice cream causes drowning—look for a variable affecting both.
:feedback-1: Correct! Warm summer weather is a lurking variable: it increases both ice cream sales and swimming (and therefore drownings).
:feedback-2: Reverse causation is equally implausible here; a lurking variable explains the association.
* Eating ice cream causes drowning
* *A lurking variable—warm weather—increases both ice cream sales and swimming activity
* Drownings cause people to buy ice cream
:::

:::{quiz} Children who sleep with a night-light on are more likely to become nearsighted. Before concluding that night-lights cause nearsightedness, which lurking variable should be considered?
:hint: Nearsightedness is strongly hereditary—and who chooses to put a night-light in the child's room?
:feedback-0: Correct! Nearsighted parents (who pass on nearsightedness genetically) are also more likely to use night-lights, confounding the relationship.
:feedback-1: The child's age was the same at the time of the study; it doesn't explain the association.
:feedback-2: The brightness of the light is part of the explanatory variable, not a separate lurking variable.
* *The parents' nearsightedness—nearsighted parents may both pass on the trait and prefer night-lights
* The child's age
* The brightness of the night-light
:::

:::{quiz} A newspaper reports: "Students who take music lessons have higher GPAs, so music lessons improve grades." What is the best critique of this conclusion?
:hint: Association does not imply causation—what else might differ between families whose children take music lessons and those who don't?
:feedback-0: Correct! Lurking variables such as family income, parental involvement, or study habits could explain both music lessons and higher GPAs; the observed association alone doesn't establish causation.
:feedback-1: The direction of the association is not the issue—the causal claim is.
:feedback-2: A larger sample would not fix the problem; the issue is the causal interpretation of an observed association.
* *The association could be explained by lurking variables such as family income or parental involvement
* The correlation is probably negative rather than positive
* The study simply needs a larger sample size
:::
