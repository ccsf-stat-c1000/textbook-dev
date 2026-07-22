# Blocking and Matched Pairs: Smarter Randomization

## Modifications to Randomization

In some cases, an experiment's design may be enhanced by relaxing the requirement of total randomization and *blocking* the subjects first, dividing them into groups of individuals who are similar with respect to an outside variable that may be important in the relationship being studied. This can help ensure that the effect of treatments, as well as background variables, are most accurately measured. In blocking, we simply split the sampled subjects into blocks based upon the different values of the background variable, and then randomly allocate treatments within each block. Thus, blocking in the assignment of subjects is analogous to stratification in sampling.

For example, consider again our experiment examining the differences between three versions of software. If we suspected that gender might affect individuals' software preferences, we might choose to allocate subjects to separate blocks, one for males and one for females. Within each block, subjects are randomly assigned to treatments and the treatment proceeds as usual. A diagram of blocking in this situation is below:

```{figure} images/gen/m07-blocking-gender.svg
:alt: A diagram of blocking. The sample is split into two blocks, males and females. Within each block, subjects are randomly assigned to one of three treatments: existing software, new software 1, or new software 2, yielding six groups in total. Results are compared within each block separately.
```

:::{admonition} Example: Comparing Gasolines
:class: tip

Suppose producers of gasoline want to compare which of two types of gas results in better mileage for automobiles. In case the size of the vehicle plays a role in the effectiveness of different types of gasoline, they could first block by vehicle size, then randomly assign some cars within each block to Gasoline A and others to Gasoline B:

```{figure} images/gen/m07-blocking-gasoline.svg
:alt: A diagram of blocking by vehicle size. The sample of cars is split into a block of small cars and a block of large cars. Within each block, cars are randomly assigned to Gasoline A or Gasoline B, and mileage is compared within each block separately.
```
:::

In the extreme, researchers may examine a relationship for a sample of blocks of just two individuals who are similar in many important respects, or even the same individual whose responses are compared for two explanatory values.

:::{admonition} Example: Matched Pairs with the Same Car
:class: tip

For example, researchers could compare the effects of Gasoline A and Gasoline B when both are used on the same car, for a sample of many cars of various sizes and models.

```{figure} images/gen/m07-matched-pairs.svg
:alt: A matched pairs diagram in which each car in the sample tries both Gasoline A and Gasoline B, in random order. Within each car, the two mileage responses are compared directly.
```
:::

Such a study design, called *matched pairs*, may enable us to pinpoint the effects of the explanatory variable by comparing responses for the same individual under two explanatory values, or for two individuals who are as similar as possible except that the first gets one treatment, and the second gets another (or serves as the control). Treatments should usually be assigned at random within each pair, or the order of treatments should be randomized for each individual. In our gasoline example, for each car the order of testing (Gasoline A first, or Gasoline B first) should be randomized.

:::{admonition} Example: Twins and Toothpaste
:class: tip

Suppose researchers want to compare the relative merits of toothpastes with and without tartar control ingredients. In order to make the comparison between individuals who are as similar as possible with respect to background and diet, they could obtain a sample of identical twins. One of each pair would randomly be assigned to brush with the tartar control toothpaste, while the other would brush with regular toothpaste of the same brand. These would be provided in unmarked tubes, so that the subjects would be blind. To make the experiment double-blind, dentists who evaluate the results would not know who used which toothpaste.
:::

"Before-and-after" studies are another common type of matched pairs design. For each individual, the response variable of interest is measured twice: first before the treatment, then again after the treatment. The categorical explanatory variable is which treatment was applied, or whether a treatment was applied, to that participant.

```{admonition} Comment
:class: important

We have explained data production as a two-stage process: first obtain the sample, then evaluate the variables of interest via an appropriate study design. Even though the steps are carried out in this order chronologically, it is generally best for researchers to decide on a study design before they actually obtain the sample. For the toothpaste example above, researchers would first decide to use the matched pairs design, then obtain a sample of identical twins, then carry out the experiment and assess the results.
```

## Check Your Understanding: Blocking and Matched Pairs

:::{quiz} Researchers testing a memory supplement suspect that age strongly affects memory performance. They divide their volunteers into "under 40" and "40 and over" groups, then randomly assign supplement or placebo within each group. What design feature is this?
:hint: Subjects were grouped by a background variable before randomization.
:feedback-0: Correct! Grouping subjects by an important background variable (age) and randomizing within groups is blocking.
:feedback-1: Matched pairs would pair up individual subjects (or use the same subject twice), not form two large groups.
:feedback-2: Stratified sampling is the analogous idea in the sampling stage, not the treatment-assignment stage.
* *Blocking by age
* A matched pairs design
* Stratified sampling
:::

:::{quiz} A study measures each participant's typing speed before and after a week-long training course, then compares the two speeds for each person. What design is this?
:hint: Each individual's responses are compared under two conditions.
:feedback-0: Correct! Comparing each individual's before and after measurements is a matched pairs ("before-and-after") design.
:feedback-1: There is only one group here—each person serves as his or her own comparison.
:feedback-2: Blocking would divide subjects into groups by a background variable, then randomize treatments within the groups.
* *A matched pairs (before-and-after) design
* A two-group randomized experiment
* Blocking by typing ability
:::
