# The Big Picture

In a nutshell, what statistics is all about is *converting data into useful information*. Statistics is therefore a process in which we

- Collect data,
- Summarize data, and
- Interpret data.

To really understand how this process works, we need to put it in a context. We will do that by introducing one of the central ideas of this course—the *Big Picture of Statistics*. We will introduce the Big Picture by building it gradually and explaining each step. At the end of the introductory explanation, once you have the full Big Picture in front of you, we will show it again using a concrete example.

The process of statistics starts when we identify what group we want to study or learn something about. We call this group the {term}`population`. Note that the word *population* here (and in the entire course) does not refer only to people; it is used in the broader statistical sense to refer not only to people, but also to animals, objects, and so on. For example, we might be interested in

- The opinions of the population of U.S. adults about the death penalty
- How the population of mice react to a certain chemical
- The average price of the population of all one-bedroom apartments in a certain city

Population, then, is the entire group that is the target of our interest:

```{figure} images/gen/m03-big-picture-1-population.svg
:alt: A large ellipse labeled Population, filled with scattered dots representing individuals.
```

In most cases, the population is so large that, as much as we want to, there is absolutely no way we can study all of it (imagine trying to get the opinions of *all* U.S. adults about the death penalty). A more practical approach would be to examine and collect data only from a subgroup of the population, which we call a {term}`sample`. We call this first step, which involves choosing a sample and collecting data from it, *producing data*.

```{figure} images/gen/m03-big-picture-2-producing-data.svg
:alt: A small circle inside the Population ellipse marks the individuals chosen for the sample. An arrow labeled Step 1, Producing Data, leads from this small circle out to the larger Sample circle, showing that the sample is a subgroup drawn from the population.
```

It should be noted that since, for practical reasons, we need to compromise and examine only a sub-group of the population rather than the whole population, we should make an effort to choose a sample in such a way that it will represent the population well. For example, if we choose a sample from the population of U.S. adults, and ask their opinions about the death penalty, we do not want our sample to consist of only Republicans or only Democrats.

Once the data have been collected, what we have is a long list of answers to questions, or numbers, and in order to explore and make sense of the data, we need to summarize that list in a meaningful way. This second step, which consists of summarizing the collected data, is called {term}`exploratory data analysis`.

```{figure} images/gen/m03-big-picture-3-eda.svg
:alt: A box labeled Step 2, Exploratory Data Analysis, now encloses the Sample circle, showing that exploratory data analysis summarizes the data collected from the sample.
```

Now we've obtained the sample results and summarized them, but we are not done. Remember that our goal is to study the population, so what we want is to be able to draw conclusions about the population based on the sample results. Before we can do so, we need to look at how the sample we're using may differ from the population as a whole, so that we can factor that into our analysis. To examine this difference, we use {term}`probability`.

In essence, probability is the "machinery" that allows us to draw conclusions about the population based on the data collected about the sample.

```{figure} images/gen/m03-big-picture-4-probability.svg
:alt: A dashed arrow leads from the Step 2 Exploratory Data Analysis box into a cloud labeled Step 3, Probability. The cloud represents theory—the machinery that will connect the sample results to conclusions about the population.
```

Finally, we can use what we've discovered about our sample to draw conclusions about our population. We call this final step in the process {term}`inference`.

```{figure} images/gen/m03-big-picture.svg
:alt: The complete Big Picture of statistics. Step 1, Producing Data, leads from a small sample circle inside the Population out to the Sample, showing that the sample is drawn from the population. The Sample sits inside the Step 2, Exploratory Data Analysis box, showing that EDA summarizes the sample data. An arrow passes through the Step 3, Probability cloud—drawn as a cloud to represent theory—back to the Population, which sits inside the Step 4, Inference box, showing that inference draws conclusions about the population.
```

This is the *Big Picture of statistics*.

:::{admonition} Example: Polling on the Death Penalty
:class: tip

At the end of April 2005, a poll was conducted (by ABC News and the *Washington Post*) for the purpose of learning the opinions of U.S. adults about the death penalty.

*1. Producing Data:* A (representative) sample of 1,082 U.S. adults was chosen, and each adult was asked whether he or she favored or opposed the death penalty.

*2. Exploratory Data Analysis (EDA):* The collected data were summarized, and it was found that 65% of the sampled adults favor the death penalty for persons convicted of murder.

*3 and 4. Probability and Inference:* Based on the sample result (of 65% favoring the death penalty) and our knowledge of probability, it was concluded (with 95% confidence) that the percentage of those who favor the death penalty in the population is within 3% of what was obtained in the sample (i.e., between 62% and 68%). The following figure summarizes the example:

```{figure} images/gen/m03-big-picture-example.svg
:alt: The Big Picture applied to the death penalty poll. From the population of all U.S. adults, a sample of 1,082 adults is chosen and asked about the death penalty (Step 1). Exploratory data analysis finds that 65% of the sample favor the death penalty (Step 2). Using probability and inference (Steps 3 and 4, with probability drawn as a cloud to represent theory), we can be 95% confident that between 62% and 68% of all U.S. adults favor the death penalty.
```
:::

## Check Your Understanding: The Big Picture of Statistics

:::{quiz} A nutrition researcher wants to know the average daily caffeine intake of adults in California. She measures the caffeine intake of 500 California adults. In the Big Picture of statistics, what are the 500 adults?
:hint: The whole group of interest is the population; the subgroup actually examined is the sample.
:feedback-0: All California adults are the population—the entire group of interest. The 500 adults are only a subgroup.
:feedback-1: Correct! The 500 adults are the subgroup that was actually examined—the sample.
:feedback-2: The measurements collected from the 500 adults are the data; the adults themselves are the sample.
* The population
* *The sample
* The data
:::

:::{quiz} The researcher summarizes her measurements and finds that the sample's average caffeine intake is 180 mg per day. Which step of the Big Picture is this?
:hint: She is organizing and summarizing the collected data.
:feedback-0: Producing data was choosing the 500 adults and measuring their intake—that step is already done.
:feedback-1: Correct! Summarizing the collected data is exploratory data analysis.
:feedback-2: Inference comes later, when she uses the sample results to draw conclusions about all California adults.
* Producing data
* *Exploratory data analysis
* Inference
:::

## Book Structure

The structure of this entire book is based on the Big Picture. The book has one unit for each of the steps in the Big Picture. As the figure below shows, the units follow the process in order: we start with producing data, continue to EDA, then proceed to probability, so that at the end we'll be able to discuss inference. The following figure summarizes the structure of the book.

% UNIT ORDER: the sentence above assumes Producing Data comes first.
% If the units are switched back to EDA-first, replace it with:
% "As the figure below shows, we start with EDA (even though it is second in
% the process of statistics), continue to discuss producing data, then proceed
% to probability, so that at the end we'll be able to discuss inference."
% Also update the alt text below and pages/images/gen/m03-big-picture-units.svg.

```{figure} images/gen/m03-big-picture-units.svg
:alt: The four steps in process order with the unit that covers each. Producing Data is covered in Unit 1, Exploratory Data Analysis in Unit 2, Probability (drawn as a cloud to represent theory) in Unit 3, and Inference in Unit 4.
```

As you'll see, the Big Picture is the basis upon which the entire book is built, both conceptually and structurally. We will refer to it often, and having it in mind will help you as you go through the units.
