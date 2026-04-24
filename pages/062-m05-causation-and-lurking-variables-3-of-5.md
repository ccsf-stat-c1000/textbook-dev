# Causation and Lurking Variables (3 of 5)

```{admonition} Learning Objectives
    - Recognize the distinction between association and causation, and identify potential lurking variables for explaining an observed relationship.
```

The next example will illustrate another way in which a lurking variable might interfere and prevent us from reaching any causal conclusions.

```{admonition} Example: SAT Test
    For U.S. colleges and universities, a standard entrance examination is the SAT test. The side-by-side boxplots below provide evidence of a relationship between the student's country of origin (the United States or another country) and the student's SAT Math score.

    ```{figure} images/causation4.gif
    :alt: A side-by-side boxplot. The vertical axis is labeled "SAT Math Score", and it ranges from 450 to 800. The horizontal axis is labeled "Country" and has two categories, "Other" and "US".

    A side-by-side boxplot. The vertical axis is labeled "SAT Math Score", and it ranges from 450 to 800. The horizontal axis is labeled "Country" and has two categories, "Other" and "US".
    ```

    The distribution of international students' scores is higher than that of U.S. students. The international students' median score (about 700) exceeds the third quartile of U.S. students' scores. Can we conclude that the country of origin is the *cause* of the difference in SAT Math scores, and that students in the United States are weaker at math than students in other countries?

    No, not necessarily. While it *might* be true that U.S. students differ in math ability from other students—i.e. due to differences in educational systems—we can't conclude that a student's country of origin is the cause of the disparity. One important *lurking variable* that might explain the observed relationship is the educational level of the two populations taking the SAT Math test. In the United States, the SAT is a standard test, and therefore a broad cross-section of all U.S. students (in terms of educational level) take this test. Among all international students, on the other hand, only those who plan on coming to the U.S. to study, which is usually a more selected subgroup, take the test.

    The following figure will help you visualize this explanation:

    ```{figure} images/causation5.gif
    :alt: A flowchart. We have two causes, one of which is "Education level of SAT Takers". This is a "Lurking variable " The other cause is "Nationality (X)". Both of these might be causes of " SAT-Math score (Y)". We have observed an association between "Nationality (X)" and "SAT-Math Score (Y)". Notice that between these two variables is also a suspected cause relationship.

    A flowchart. We have two causes, one of which is "Education level of SAT Takers". This is a "Lurking variable " The other cause is "Nationality (X)". Both of these might be causes of " SAT-Math score (Y)". We have observed an association between "Nationality (X)" and "SAT-Math Score (Y)". Notice that between these two variables is also a suspected cause relationship.
    ```

    Here, the explanatory variable (X) *may* have a causal relationship with the response variable (Y), but the lurking variable might be a contributing factor as well, which makes it very hard to isolate the effect of the explanatory variable and prove that it has a causal link with the response variable. In this case, we say that the lurking variable is *confounded* with the explanatory variable, since their effects on the response variable cannot be distinguished from each other.
```

Note that in each of the above two examples, the lurking variable interacts differently with the variables studied. In example 1, the lurking variable has an effect on both the explanatory and the response variables, creating the illusion that there is a causal link between them. In example two, the lurking variable is confounded with the explanatory variable, making it hard to assess the isolated effect of the explanatory variable on the response variable.

The distinction between these two types of interactions is not as important as the fact that in either case, the observed association can be at least partially explained by the lurking variable. The most important message from these two examples is therefore: *An observed association between two variables is not enough evidence that there is a*

*causal relationship between them.*

In other words ...

```{admonition} Principle
    Association *does not* imply causation!
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Learn By Doing**

    Causation

    *(Interactive activity — available in the OLI platform)*
```
