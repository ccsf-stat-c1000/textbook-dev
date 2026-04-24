# Matched Pairs (2 of 8)

```{admonition} Learning Objectives
    - In a given context, carry out the inferential method for comparing groups and draw the appropriate conclusions.
```

So far, we have discussed and illustrated cases in which the matched pairs design comes up, and we are now ready to discuss how to carry out the test in this case. We will first present the idea behind the paired t-test, and then go through the four steps in the testing process.

## The Paired t-test

##### Idea

The idea behind the paired t-test is to reduce this two-sample situation, where we are comparing two means, to a single sample situation where we are doing inference on a single mean, and then use a simple t-test that we introduced in the previous module. We will first illustrate this idea using our example, and then more generally.

```{note} Video
[Matched Pairs](https://www.youtube.com/watch?v=URPrSH0Lg_M)
```

In other words, by reducing the two samples to one sample of differences, we are essentially reducing the problem from a problem where we're comparing two means (i.e., doing inference on $\mu_{1}−\mu_{2}$):

```{figure} images/image054.gif
:alt: The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.

The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.
```

to a problem where we are making an inference about a single mean — the mean of the differences:

```{figure} images/image055.gif
:alt: The population of drivers is represented by a large circle. We are interested in μ for this population, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). We generate a sample of size n = 20, and get 20 differences.

The population of drivers is represented by a large circle. We are interested in μ for this population, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). We generate a sample of size n = 20, and get 20 differences.
```

In general, in every matched pairs problem, our data consist of 2 samples which are organized in n pairs:

```{figure} images/image056.gif
:alt: A set of matched pairs, numbered 1 through n. The first element in each pair is sample 1 and the second element in each pair is sample 2. The data is presented in a table which has 3 rows, labeled "Pairs," "Sample 1," and "Sample 2."

A set of matched pairs, numbered 1 through n. The first element in each pair is sample 1 and the second element in each pair is sample 2. The data is presented in a table which has 3 rows, labeled "Pairs," "Sample 1," and "Sample 2."
```

We reduce the two samples to only one by calculating for each pair the difference between the two observations (in the figure we used $d_{1},d_{2},d_{3},...,d_{n}$ to denote the differences).

```{figure} images/image058.gif
:alt: Each pair is reduced to a difference, by calculating sample1 - sample2. This is shown on the table by adding an extra row labeled " differences" and for each column, adding a value in the differences row describing the pair represented by the column.

Each pair is reduced to a difference, by calculating sample1 - sample2. This is shown on the table by adding an extra row labeled " differences" and for each column, adding a value in the differences row describing the pair represented by the column.
```

The paired t-test is based on this one sample of n differences,

```{figure} images/image059.gif
:alt: We can now ignore the sample 1 and sample 2 data in each pair and instead just focus on the differences.

We can now ignore the sample 1 and sample 2 data in each pair and instead just focus on the differences.
```

and it uses those differences as data for a simple t-test on a single mean — the mean of the differences.

This is the general idea behind the paired t-test; it is nothing more than a regular one-sample t-test for the mean of the differences. We will now go through the 4-step process of the paired t-test.
