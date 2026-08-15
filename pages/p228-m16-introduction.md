# Introduction

In the previous two modules we performed inference for one variable. More specifically, we learned about inference for the population proportion p (when the variable of interest is categorical) and inference for the population mean $\mu$ (when the variable of interest is quantitative). In those modules we were also exposed to the following three forms of inference, which will continue to be central as we move forward in the course:

- *Point estimation*—estimating an unknown parameter with a single value that is computed from the sample.
- *Interval estimation*—estimating an unknown parameter by an interval of plausible values. To each such interval we attach a level of confidence that the interval indeed captures the value of the unknown parameter, hence the name confidence intervals.
- {term}`Hypothesis testing <hypothesis testing>`—a four-step process in which we are assessing evidence provided by the data in favor of or against some claim about the population parameter.

Our next (and final) goal for this course is to perform inference about relationships between two variables in a population, based on an observed relationship between variables in a sample. Here is what the process looks like:

```{figure} images/gen/m16-inference-relationship.svg
:alt: A large circle represents the population of interest, where we ask whether X and Y are related. A smaller circle represents a simple random sample of size n, from which we collect data on both variables. Based on the observed data, we infer whether there is significant evidence that X and Y are related in the population.
```

We are interested in studying whether a relationship exists between the variables X and Y in a population of interest. We choose a random sample and collect data on both variables from the subjects. Our goal is to determine whether these data provide strong enough evidence for us to generalize the observed relationship in the sample and conclude (with some acceptable and agreed-upon level of uncertainty) that a relationship between X and Y exists in the entire population.

The primary inference form that we will use in this module, then, is hypothesis testing. Conceptually, across all the inferential methods that we will learn, we'll test some form of:

- $H_0$: There is no relationship between X and Y.
- $H_a$: There is a significant relationship between X and Y.

(We will also discuss point and interval estimation, but our discussion about these forms of inference will be framed around the test.)

Recall that in the module about examining the relationship between two variables in the Exploratory Data Analysis unit, our discussion was framed around the role-type classification table. This part of the course will be structured in exactly the same way.

In other words, we will go through 3 sections corresponding to cases $C \to Q$, $C \to C$, and $Q \to Q$ in the table below.

```{figure} images/gen/m05-role-type-table.svg
:alt: The role-type classification table. Any type of explanatory variable can be paired with any type of response variable, giving four cases: categorical explanatory with quantitative response (C to Q), categorical with categorical (C to C), quantitative with categorical (Q to C), and quantitative with quantitative (Q to Q).
```

(Recall that case $Q \to C$ is not discussed in this course.)

In total, we will introduce 5 inferential methods: three in case $C \to Q$ (corresponding to a division of this case into 3 sub-cases) and one in each of the cases $C \to C$ and $Q \to Q$.

Unlike the previous part of the course on Inference for One Variable, where we discussed in some detail the theory behind the machinery of the test (such as the null distribution of the test statistic, under which the p-values are calculated), in the 5 inferential procedures that we will introduce in Inference for Relationships, we will discuss much less of that kind of detail. The principles are the same, but the details behind the null distribution of the test statistic become more complicated and require knowledge of theoretical results that are definitely beyond the scope of this course.

Instead, within each of the five inferential methods we will focus on:

- When the inferential method is appropriate for use.
- Under what conditions the procedure can safely be used.
- The conceptual idea behind the test (as it is usually captured by the test statistic).
- How to use software to carry out the procedure in order to get the p-value of the test.
- Interpreting the results in the context of the problem.

Also, we will continue to introduce each test according to the four-step process of hypothesis testing. We are now ready to start with case $C \to Q$.
