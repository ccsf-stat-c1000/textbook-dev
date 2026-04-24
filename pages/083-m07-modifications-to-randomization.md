# Modifications to Randomization

```{admonition} Learning Objectives
    - Identify the design of a study (controlled experiment vs. observational study) and other features of the study design (randomized, blind etc.).
```

## Modifications to Randomization

In some cases, an experiment's design may be enhanced by relaxing the requirement of total randomization and *blocking* the subjects first, dividing them into groups of individuals who are similar with respect to an outside variable that may be important in the relationship being studied. This can help ensure that the effect of treatments, as well as background variables, are most accurately measured. In blocking, we simply split the sampled subjects into blocks based upon the different values of the background variable, and then randomly allocate treatments within each block. Thus, blocking in the assignment of subjects is analogous to stratification in sampling.

For example, consider again our experiment examining the differences between three versions of software from the last Learn By Doing activity. If we suspected that gender might affect individuals' software preferences, we might choose to allocate subjects to separate blocks, one for males and one for females. Within each block, subjects are randomly assigned to treatments and the treatment proceeds as usual. A diagram of blocking in this situation is below:

```{figure} images/image011.gif
:alt: We have 2 blocks, 3 treatment groups each (by random assignment). From the population we generate a sample. This sample of individuals is then split into two blocks, Males and Females. Each block is then randomly split further into the three treatment groups: "tt1: existing software," "ttt2 new software 1," and "ttt3 new software 2." So, we end up with 6 total groups. Within each group the responses from the treatment groups are compared to each other, generating results separately for each block.

We have 2 blocks, 3 treatment groups each (by random assignment). From the population we generate a sample. This sample of individuals is then split into two blocks, Males and Females. Each block is then randomly split further into the three treatment groups: "tt1: existing software," "ttt2 new software 1," and "ttt3 new software 2." So, we end up with 6 total groups. Within each group the responses from the treatment groups are compared to each other, generating results separately for each block.
```

```{admonition} Example
    Suppose producers of gasoline want to compare which of two types of gas results in better mileage for automobiles. In case the size of the vehicle plays a role in the effectiveness of different types of gasoline, they could first block by vehicle size, then randomly assign some cars within each block to Gasoline A and others to Gasoline B:

    ```{figure} images/image012.gif
    :alt: This example consists of 2 blocks, 2 treatment groups each (by random assignment). From the population we generate a sample, then separate it into two blocks, "Small" and "Large," according to the vehicle size.; Within these blocks we randomly assign vehicles to use either Gasoline A or Gasoline B (So, each block is split into two treatment groups, "ttt1: Gasoline A", and "ttt2: Gasoline B"), resulting in 4 total groups. Then, within each block, we compare the responses, so we obtain results for each block individually.

    This example consists of 2 blocks, 2 treatment groups each (by random assignment). From the population we generate a sample, then separate it into two blocks, "Small" and "Large," according to the vehicle size.; Within these blocks we randomly assign vehicles to use either Gasoline A or Gasoline B (So, each block is split into two treatment groups, "ttt1: Gasoline A", and "ttt2: Gasoline B"), resulting in 4 total groups. Then, within each block, we compare the responses, so we obtain results for each block individually.
    ```
```

In the extreme, researchers may examine a relationship for a sample of blocks of just two individuals who are similar in many important respects, or even the same individual whose responses are compared for two explanatory values.

```{admonition} Example
    For example, researchers could compare the effects of Gasoline A and Gasoline B when both are used on the same car, for a sample of many cars of various sizes and models.

    ```{figure} images/image013.gif
    :alt: In this Matched Pairs Design we have n blocks of individual cars, with 2 treatment groups each, done by random assignment. From the population we generate the sample group. The sample group is then placed into n blocks for each individual car. Each of these blocks is subjected to two treatments by random assignment. These treatments are "ttt1 Gasoline A" and "ttt2 Gasoline B." For each car, the responses to each treatment are compared, resulting in a treatment for each

    In this Matched Pairs Design we have n blocks of individual cars, with 2 treatment groups each, done by random assignment. From the population we generate the sample group. The sample group is then placed into n blocks for each individual car. Each of these blocks is subjected to two treatments by random assignment. These treatments are "ttt1 Gasoline A" and "ttt2 Gasoline B." For each car, the responses to each treatment are compared, resulting in a treatment for each
    ```
```

Such a study design, called *matched pairs*, may enable us to pinpoint the effects of the explanatory variable by comparing responses for the same individual under two explanatory values, or for two individuals who are as similar as possible except that the first gets one treatment, and the second gets another (or serves as the control). Treatments should usually be assigned at random within each pair, or the order of treatments should be randomized for each individual. In our gasoline example, for each car the order of testing (Gasoline A first, or Gasoline B first) should be randomized.

```{admonition} Example
    Suppose researchers want to compare the relative merits of toothpastes with and without tartar control ingredients. In order to make the comparison between individuals who are as similar as possible with respect to background and diet, they could obtain a sample of identical twins. One of each pair would randomly be assigned to brush with the tartar control toothpaste, while the other would brush with regular toothpaste of the same brand. These would be provided in unmarked tubes, so that the subjects would be blind. To make the experiment double-blind, dentists who evaluate the results would not know who used which toothpaste.

    ```{figure} images/image014.gif
    :alt: Paired Design. There are n blocks, each represented by a circle with two identical twins in them. Randomly, the treatment of tartar or regular toothpaste is given to each twin. So, each circle has two twins, two types of toothpaste, and each twin randomly gets assigned one type of toothpaste.

    Paired Design. There are n blocks, each represented by a circle with two identical twins in them. Randomly, the treatment of tartar or regular toothpaste is given to each twin. So, each circle has two twins, two types of toothpaste, and each twin randomly gets assigned one type of toothpaste.
    ```
```

"Before-and-after" studies are another common type of matched pairs design. For each individual, the response variable of interest is measured twice: first before the treatment, then again after the treatment. The categorical explanatory variable is which treatment was applied, or whether a treatment was applied, to that participant.

## Comment

We have explained data production as a two-stage process: first obtain the sample, then evaluate the variables of interest via an appropriate study design. Even though the steps are carried out in this order chronologically, it is generally best for researchers to decide on a study design before they actually obtain the sample. For the toothpaste example above, researchers would first decide to use the matched pairs design, then obtain a sample of identical twins, then carry out the experiment and assess the results.

```{note}
    **Did I Get This?**

    *(Interactive activity — available in the OLI platform)*
```
