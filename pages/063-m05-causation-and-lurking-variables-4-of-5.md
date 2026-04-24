# Causation and Lurking Variables (4 of 5)

```{admonition} Learning Objectives
    - Recognize the distinction between association and causation, and identify potential lurking variables for explaining an observed relationship.
    - Recognize and explain the phenomenon of Simpson's Paradox as it relates to interpreting the relationship between two variables.
```

So far, we have:

- discussed what lurking variables are,
- demonstrated different ways in which the lurking variables can interact with the two
                studied variables, and
- understood that the existence of a possible lurking variable is the main reason why
                we say that association does not imply causation.

As you recall, a lurking variable, by definition, is a variable that was not included in the study, but could have a substantial effect on our understanding of the relationship between the two studied variables.

What if we *did* include a lurking variable in our study? What kind of effect could that have on our understanding of the relationship? These are the questions we are going to discuss next.

Let's start with an example:

```{admonition} Example: Hospital Death Rates
    *Background:* A government study collected data on the death rates in nearly 6,000 hospitals in the United States. These results were then challenged by researchers, who said that the federal analyses failed to take into account the variation among hospitals in the severity of patients' illnesses when they were hospitalized. As a result, said the researchers, some hospitals were treated unfairly in the findings, which named hospitals with higher-than-expected death rates. What the researchers meant is that when the federal government explored the relationship between the two variables—hospital and death rate—*it also should have included in the study (or taken into account) the lurking variable—severity of illness.*

    We will use a simplified version of this study to illustrate the researchers' claim, and see what the possible effect could be of including a lurking variable in a study. (Reference: Moore and McCabe (2003). *Introduction to the Practice of Statistics*.)

    Consider the following two-way table, which summarizes the data about the status of patients who were admitted to two hospitals in a certain city (Hospital A and Hospital B). Note that since the purpose of the study is to examine whether there is a "hospital effect" on patients' status, "Hospital is the explanatory variable, and "Patient's Status" is the response variable.

    When we supplement the two-way table with the conditional percents within each hospital:

    we find that Hospital A has a higher death rate (3%) than Hospital B (2%). Should we jump to the conclusion that a sick patient admitted to Hospital A is 50% more likely to die than if he/she were admitted to Hospital B? *Not so fast ...*

    Maybe Hospital A gets most of the severe cases, and that explains why it has a higher death rate. In order to explore this, we need to *include (or account for) the lurking variable "severity of illness" in our analysis.* To do this, we go back to the two-way table and split it up to look separately at patents who are severely ill, and patients who are not.

    As we can see, Hospital A *did* admit many more severely ill patients than Hospital B (1,500 vs. 200). In fact, from the way the totals were split, we see that in Hospital A, severely ill patients were a much higher proportion of the patients—1,500 out of a total of 2,100 patients. In contrast, only 200 out of 800 patients at Hospital B were severely ill. To better see the effect of including the lurking variable, we need to supplement each of the two new two-way tables with its conditional percentages:

    Note that despite our earlier finding that overall Hospital A has a higher death rate (3% vs. 2%), when we take into account the lurking variable, we find that actually it is Hospital B that has the higher death rate both among the severely ill patients (4% vs. 3.8%) and among the not severely ill patients (1.3% vs. 1%). *Thus, we see that adding a lurking variable can change the direction of an association.*

    Whenever including a lurking variable causes us to rethink the direction of an association, this is called *Simpson's paradox.*

    The possibility that a lurking variable can have such a dramatic effect is another reason we must adhere to the principle:
```

```{admonition} Principle
    Association *does not* imply causation!
```
