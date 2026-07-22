# When Lurking Variables Deepen (Rather Than Reverse) the Story

It is *not* always the case that including a lurking variable makes us rethink the direction of the association. In the next example we will see how including a lurking variable just helps us gain a deeper understanding of the observed relationship.

:::{admonition} Example: College Entrance Exams
:class: tip

As discussed earlier, in the United States, the SAT is a widely used college entrance examination, required by the most prestigious schools. In some states, a different college entrance examination is prevalent, the ACT. A scatterplot of states' average SAT scores against the percentage of students taking the SAT reveals two distinct clusters: states where most students take the SAT (with lower average scores) and states where few students take it (with higher average scores, since only a select group of students—often those applying to out-of-state schools—take the SAT there). Including the lurking variable "percentage of students taking the exam" doesn't reverse any association, but it explains the clusters and deepens our understanding of the relationship.

```{note} Video

[Including a Lurking Variable](https://www.youtube.com/watch?v=Nnj1YlqzkX4)
```
:::

The last two examples showed us that including a lurking variable in our exploration may

- Lead us to rethink the direction of an association (as in the Hospital/Death Rate example).
- Help us to gain a deeper understanding of the relationship between variables (as in the SAT/ACT example).

## Check Your Understanding: Simpson's Paradox

:::{quiz} A university finds that overall, program X admits a higher percentage of applicants than program Y. But when applicants are separated by intended major, program Y admits a higher percentage in every single major. What phenomenon is this?
:hint: Including the lurking variable (major) reversed the direction of the association.
:feedback-0: Correct! When accounting for a lurking variable reverses the direction of an association, we have Simpson's paradox.
:feedback-1: Extrapolation refers to predicting beyond the range of the data in regression.
:feedback-2: A negative correlation describes two quantitative variables; this is about a reversal of an association after conditioning on a third variable.
* *Simpson's paradox
* Extrapolation
* Negative correlation
:::

:::{quiz} In the hospital example, why did Hospital A have the higher overall death rate even though its death rate was lower within both severity groups?
:hint: Compare the mix of patients each hospital admitted.
:feedback-0: Correct! Hospital A treated a far higher proportion of severely ill patients (1,500 of 2,100), and severely ill patients die at higher rates no matter where they are treated—this weighting drove up A's overall rate.
:feedback-1: The arithmetic is correct in both analyses; the difference comes from the patient mix, not an error.
:feedback-2: Sample size alone doesn't explain the reversal—the key is the proportion of severe cases at each hospital.
* *Hospital A admitted a much larger proportion of severely ill patients, who have higher death rates everywhere
* The overall percentages were computed incorrectly
* Hospital B's sample was too small to compute death rates
:::

## Let's Summarize

- A *lurking variable* is a variable that was not included in your analysis, but that could substantially change your interpretation of the data if it were included.
- Because of the possibility of lurking variables, we adhere to the principle that *association does not imply causation*.
- Including a lurking variable in our exploration may
  - Help us to gain a deeper understanding of the relationship between variables.
  - Lead us to rethink the direction of an association.
- Whenever including a lurking variable causes us to rethink the direction of an association, this is an instance of *Simpson's paradox*.
