# Two Independent Samples (2 of 7)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
    - Specify the null and alternative hypotheses for comparing groups.
```

## The Two-Sample t-Test

Here again is the general situation which requires us to use the two-sample t-test:

```{figure} images/image014.gif
:alt: Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. From Sub-population 1 we take an SRS of size n_1, and from Sub-population 2 we take an SRS of size n_2. Both of these samples are independent.

Sub-Population 1 has a Y Mean of μ_1, and Sub-Population 2 has a Y Mean of μ_2. From Sub-population 1 we take an SRS of size n_1, and from Sub-population 2 we take an SRS of size n_2. Both of these samples are independent.
```

Our goal is to compare the means μ~1~ and μ~2~ based on the two independent samples.

## Step 1: Stating the Hypotheses

The hypotheses represent our goal, comparing the means: μ~1~ and μ~2~ .

- The null hypothesis has the form:
  - $H_{o}:\mu_{1}−\mu_{2}=0$
			(which is the same as
			$H_{o}:\mu_{1}=\mu_{2}$
			)
- The alternative hypothesis takes one of the following three forms (depending on the context):
  - $H_{a}:\mu_{1}−\mu_{2}<0$
			(which is the same as
			$H_{a}:\mu_{1}<\mu_{2}$
			) (one-sided)
  - $H_{a}:\mu_{1}−\mu_{2}>0$
			(which is the same as
			$H_{a}:\mu_{1}>\mu_{2}$
			) (one-sided)
  - $H_{a}:\mu_{1}−\mu_{2}\neq0$
			(which is the same as
			$H_{a}:\mu_{1}\neq\mu_{2}$
			) (two-sided)

Note that the null hypothesis claims that there is no difference between the means, which can either represented as the difference is 0 (no difference), or as its (algebraically and conceptually) equivalent, $\mu_{1}=\mu_{2}$ (the means are equal). Either way, conceptually, H~o~ claims that there is no relationship between the two relevant variables.

The first way of writing the hypotheses (using a difference between the means) will be easier to use when (in the future) we look for a difference that is not 0.

Each one of the three alternatives claims that there is a difference between the means. The two one-sided alternatives specify the nature of the difference; either negative, indicating that μ~1~ is smaller than μ~2~, or positive, indicating that μ~1~ is larger than μ~2~. The two-sided alternative, as usual, is more general and simply claims that a difference exists. As before, it should be clear from the context of the problem which of the three alternatives is appropriate.

## Comment

Note that our parameter of interest in this case (the parameter about which we are making an inference) is the difference between the means $\mu_{1}−\mu_{2}$ , and that the null value is 0.

```{admonition} Example
    Recall that the purpose of this survey was to examine whether the opinions of females and males *differ*with respect to the importance of looks vs. personality. The hypotheses in this case are therefore:

    ```{figure} images/image030.gif
    :alt: H_0: μ_1 - μ_2 = 0, H_a: μ_1 - μ_2 ≠ 0

    H_0: μ_1 - μ_2 = 0, H_a: μ_1 - μ_2 ≠ 0
    ```

    where μ~1~ represents the mean importance for females and μ~2~ represents the mean importance for males.

    It is important to understand that conceptually, the two hypotheses claim:

    H~o~: Score (of looks vs. personality) is not related to gender

    H~a~: Score (of looks vs. personality) is related to gender
```

##### Did I Get This?

In order to check the claim that the pregnancy length of women who smoke during pregnancy is shorter, on average, than the pregnancy length of women who do not smoke, a random sample of 35 pregnant women who smoke and a random sample of 35 pregnant women who do not smoke were chosen and their pregnancy lengths were recorded. Here is a figure of this example:

```{figure} images/image156.gif
:alt: The Smoking (X) variable gives us our two populations. These are Population 1: Pregnant women who smoke, and Pop 2: Pregnant Women who don't smoke. For each of these populations we have the variable Length (Y) and its mean. For smokers we have μ_1, and for non-smokers we have μ_2. From the population of smokers, we create an SRS of size 35, and from the population of non-smokers we create an SRS of 35.

The Smoking (X) variable gives us our two populations. These are Population 1: Pregnant women who smoke, and Pop 2: Pregnant Women who don't smoke. For each of these populations we have the variable Length (Y) and its mean. For smokers we have μ_1, and for non-smokers we have μ_2. From the population of smokers, we create an SRS of size 35, and from the population of non-smokers we create an SRS of 35.
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
