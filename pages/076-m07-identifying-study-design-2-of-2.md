# Identifying Study Design (2 of 2)

```{admonition} Learning Objectives
:class: note

- Identify the design of a study (controlled experiment vs. observational study) and other features of the study design (randomized, blind etc.).
```

## Experiments vs. Observational Studies

Before assessing the effectiveness of observational studies and experiments for producing evidence of a causal relationship between two variables, we will illustrate the essential differences between these two designs.

:::{admonition} Example: Quitting Smoking
:class: tip

Every day, a huge number of people are engaged in a struggle whose outcome could literally affect the length and quality of their life: they are trying to quit smoking. Just the array of techniques, products, and promises available shows that quitting is not easy, nor is its success guaranteed. Researchers would like to determine which of the following is the best method:

1. Drugs that alleviate nicotine addiction.
2. Therapy that trains smokers to quit.
3. A combination of drugs and therapy.
4. Neither form of intervention (quitting "cold turkey").

The explanatory variable is the method (1, 2, 3 or 4), while the response variable is eventual success or failure in quitting. In an observational study, values of the explanatory variable occur naturally. In this case, this means that the participants themselves choose a method of trying to quit smoking. In an experiment, researchers assign the values of the explanatory variable. In other words, they tell people what method to use. Let us consider how we might compare the four techniques, via either an observational study or an experiment.

1. An *observational study* of the relationship between these two variables requires us to collect a representative sample from the population of smokers who are beginning to try to quit. We can imagine that a substantial proportion of that population is trying one of the four above methods. In order to obtain a representative sample, we might use a nationwide telephone survey to identify 1,000 smokers who are just beginning to quit smoking. We record which of the four methods the smokers use. One year later, we contact the same 1,000 individuals and determine whether they succeeded.

2. In an *experiment*, we again collect a representative sample from the population of smokers who are just now trying to quit, using a nationwide telephone survey of 1,000 individuals. This time, however, we divide the sample into 4 groups of 250 and *assign* each group to use one of the four methods to quit. One year later, we contact the same 1,000 individuals and determine whose attempts succeeded while using our designated method.
:::

The following figures illustrate the two study designs:

```{figure} images/gen/m07-observational-design.svg
:alt: A diagram of the observational study. From the population of quitting smokers, a random sample of 1,000 is selected. The sample then divides itself into four groups of uneven sizes, one for each quitting method, because participants choose their own method.
```

```{figure} images/gen/m07-experiment-design.svg
:alt: A diagram of the experiment. From the population of quitting smokers, a random sample of 1,000 is selected. The researchers then assign the participants to four equal groups of 250, one for each quitting method.
```

Both the observational study and the experiment begin with a random sample from the population of smokers just now beginning to quit. In both cases, the individuals in the sample can be divided into categories based on the values of the explanatory variable: method used to quit. The response variable is success or failure after one year. Finally, in both cases, we would assess the relationship between the variables by comparing the proportions of success of the individuals using each method, using a two-way table and conditional percentages.

The only difference between the two methods is the way the sample is divided into categories for the explanatory variable (method). In the observational study, individuals are divided based upon the method by which they *choose* to quit smoking. The researcher does not assign the values of the explanatory variable, but rather records them as they naturally occur. In the experiment, the researcher *deliberately assigns* one of the four methods to each individual in the sample. The researcher intervenes by controlling the explanatory variable, and then assesses its relationship with the response variable.

Now that we have outlined two possible study designs, let's return to the original question: which of the four methods for quitting smoking is most successful? Suppose the study's results indicate that individuals who try to quit with the combination drug/therapy method have the highest rate of success, and those who try to quit with neither form of intervention have the lowest rate of success, as illustrated in the hypothetical two-way table below:

| Method | Quit | Didn't Quit | Total | % Who Quit |
| --- | --- | --- | --- | --- |
| Neither ("cold turkey") | 12 | 238 | 250 | 5% |
| Drugs only | 60 | 190 | 250 | 24% |
| Therapy only | 59 | 191 | 250 | 24% |
| Drugs & therapy | 83 | 167 | 250 | 33% |

Can we conclude that using the combination drugs and therapy method caused the smokers to quit most successfully? Which type of design was implemented will play an important role in the answer to this question.

## Concept Check

:::{quiz} In the observational version of the quitting-smoking study, why can't we safely conclude that the drug-plus-therapy method causes the highest success rate?
:hint: Who ended up in the drug-plus-therapy group, and how did they get there?
:feedback-0: Correct! Participants chose their own method, so the groups may differ in important ways (motivation, income, addiction severity)—lurking variables that could explain the differences in success.
:feedback-1: Sample size is not the core problem; even a very large observational study would have self-selected groups.
:feedback-2: A two-way table is an appropriate summary; the issue is how the groups were formed.
* *Participants chose their own method, so the groups may differ in ways that affect success (lurking variables)
* The sample of 1,000 is too small to draw any conclusion
* Two-way tables cannot be used to compare success rates
:::
