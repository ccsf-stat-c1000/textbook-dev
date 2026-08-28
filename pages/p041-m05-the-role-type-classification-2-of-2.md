# The Role-Type Classification: A Roadmap for Relationships

If we further classify each of the two relevant variables according to *type* (categorical or quantitative), we get the following four possibilities for *role-type classification*:

1. Categorical explanatory and quantitative response
2. Categorical explanatory and categorical response
3. Quantitative explanatory and quantitative response
4. Quantitative explanatory and categorical response

This role-type classification can be summarized and easily visualized in the following table (note that the explanatory variable is always listed first):

```{figure} images/gen/m05-role-type-table.svg
:alt: A two-by-two table of the role-type classification. The rows give the type of the explanatory variable and the columns the type of the response variable. A categorical explanatory with a categorical response is case C to C; categorical explanatory with quantitative response is case C to Q; quantitative explanatory with categorical response is case Q to C; and quantitative explanatory with quantitative response is case Q to Q.
```

This role-type classification serves as the infrastructure for this entire section. In each of the four cases, different statistical tools (displays and numerical measures) should be used to explore the relationship between the two variables. This suggests the following important principle:

```{admonition} Principle
:class: note

When confronted with a research question that involves exploring the relationship between two variables, the first and most crucial step is to determine which of the four cases represents the data structure of the problem. In other words, the first step should be classifying the two relevant variables according to their role and type, and only then can we determine what statistical tools should be used to analyze them.
```

Now let's go back to our eight examples and determine which of the four cases represents the data structure of each:

:::{admonition} Example: 1
:class: tip

- *Gender* is the *explanatory* variable, and it is *categorical*.
- *Test score* is the *response* variable, and it is *quantitative*.
- Therefore, this is an example of *case $C \to Q$*.
:::

:::{admonition} Example: 3
:class: tip

- *Light Type* is the *explanatory* variable, and it is *categorical*.
- *Nearsightedness* is the *response* variable, and it is *categorical*.
- Therefore, this is an example of *case $C \to C$*.
:::

:::{admonition} Example: 5
:class: tip

- *SAT Score* is the *explanatory* variable, and it is *quantitative*.
- *GPA of Freshman Year* is the *response* variable, and it is *quantitative*.
- Therefore, this is an example of *case $Q \to Q$*.
:::

:::{admonition} Example: 7
:class: tip

- *Time* is the *explanatory* variable, and it is *quantitative*.
- *Driving Test Outcome* is the *response* variable, and it is *categorical*.
- Therefore, this is an example of *case $Q \to C$*.
:::

## Check Your Understanding: Classifying Relationships by Role and Type

Now you classify the rest. In each of the following problems, determine which of the four cases represents the data structure of the study.

:::{quiz} Example 2: How is the number of calories in a hot dog related to the type of hot dog (beef, meat, or poultry)?
:hint: Type of hot dog explains calories. Classify each variable as categorical or quantitative.
:feedback-0: Correct! Type of hot dog (categorical) is the explanatory variable, and calories (quantitative) is the response: case $C \to Q$.
:feedback-1: Calories is quantitative, not categorical—so the response is quantitative.
:feedback-2: Type of hot dog is categorical, not quantitative—so the explanatory variable is categorical.
* *$C \to Q$
* $C \to C$
* $Q \to Q$
:::

:::{quiz} Example 4: Are the smoking habits of a person (yes, no) related to the person's gender?
:hint: Both variables place people into categories.
:feedback-0: Both variables here are categorical—neither is a numerical measurement.
:feedback-1: Correct! Gender (categorical) is the explanatory variable and smoking (categorical, yes/no) is the response: case $C \to C$.
:feedback-2: Neither variable is quantitative in this study.
* $C \to Q$
* *$C \to C$
* $Q \to C$
:::

:::{quiz} Example 6: What is the relationship between a driver's age and the maximum distance at which the driver can read a road sign?
:hint: Both variables are numerical measurements.
:feedback-0: Age is a quantitative variable, so the explanatory variable is not categorical.
:feedback-1: Distance is a quantitative variable, so the response is not categorical.
:feedback-2: Correct! Age (quantitative) explains sign legibility distance (quantitative): case $Q \to Q$.
* $C \to Q$
* $Q \to C$
* *$Q \to Q$
:::

:::{quiz} Example 8: Can you predict a person's favorite type of music (classical, rock, jazz) on the basis of his or her IQ level?
:hint: The predictor is numerical; the outcome is a category.
:feedback-0: Correct! IQ (quantitative) is the explanatory variable and favorite music type (categorical) is the response: case $Q \to C$.
:feedback-1: The explanatory variable, IQ, is quantitative, not categorical.
:feedback-2: The response, favorite music type, is categorical, not quantitative.
* *$Q \to C$
* $C \to C$
* $Q \to Q$
:::

The remainder of this section on exploring relationships is guided by this role-type classification. In the next three parts, we elaborate on cases $C \to Q$, $C \to C$, and $Q \to Q$. More specifically, we will learn the appropriate statistical tools (visual display and numerical summaries) that will allow us to explore the relationship between the two variables in each of the cases. Case $Q \to C$ is *not* discussed in this course and is typically covered in more advanced courses. The section concludes with a discussion on causal relationships.
