# Hypothesis Testing for the Population Proportion p (1 of 13)

```{admonition} Learning Objectives
    - In a given context, specify the null and alternative hypotheses for the population proportion and mean.
```

## Overview

Now that we understand the process we go through in hypothesis testing and the logic behind it, we are ready to start learning about specific statistical tests (also known as significance tests).

The first test we are going to learn is the test about the population proportion (p). This is test is widely known as the *z-test for the population proportion (p).* (We will understand later where the "z-test" part comes from.)

When we conduct a test about a population proportion, we are working with a categorical variable. Later in the course, after we have learned a variety of hypothesis tests, we will need to be able to identify which test is appropriate for which situation. Identifying the variable as categorical or quantitative is an important component of choosing an appropriate hypothesis test.

```{note}
    **Learn By Doing**

    *(Interactive activity — available in the OLI platform)*
```

Our discussion of hypothesis testing for the population proportion p follows the four steps of hypotheses testing that we introduced in our general discussion on hypothesis testing, but this time we go into more details. More specifically, we learn how the test statistic and p-value are calculated and interpreted.

Once we learn how to carry out the test for the population proportion p, we discuss some general topics that are related to hypotheses testing. More specifically, we see what role the sample size plays and understand how hypothesis testing and interval estimation (confidence intervals) are related.

Let's start by introducing the three examples, which will be the leading examples in our discussion. Each example is followed by a figure illustrating the information provided, as well as the question of interest.

```{admonition} Example: 1
    A machine is known to produce 20% defective products, and is therefore sent for repair. After the machine is repaired, 400 products produced by the machine are chosen at random and 64 of them are found to be defective. Do the data provide enough evidence that the proportion of defective products produced by the machine (p) has been *reduced* as a result of the repair?

    The following figure displays the information, as well as the question of interest:

    ```{figure} images/image212.gif
    :alt: A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still .20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective.

    A large circle represents the population of products produced by the machine (following the repair). We want to know p about this population, or what is the proportion of defective products. The question we wish to answer is &quot;is p still .20 or has it been reduced?&quot; We take a sample of 400 products, represented by a smaller circle. We find that 64 of these are defective.
    ```

    The question of interest helps us formulate the null and alternative hypotheses in terms of p, the proportion of defective products produced by the machine following the repair:

    *H*~*o*~*:* p = .20 (No change; the repair did not help).

    *H*~*a*~*:* p < .20 (The repair was effective).
```

```{admonition} Example: 2
    There are rumors that students at a certain liberal arts college are more inclined to use drugs than U.S. college students in general. Suppose that in a simple random sample of 100 students from the college, 19 admitted to marijuana use. Do the data provide enough evidence to conclude that the proportion of marijuana users among the students in the college (p) is *higher* than the national proportion, which is .157? (This number is reported by the Harvard School of Public Health.)

    Again, the following figure displays the information as well as the question of interest:

    ```{figure} images/image213.gif
    :alt: A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana.

    A large circle represents the population Students at the college. We want to know p about this population, or what is the population proportion of students using marijuana. The question we wish to answer is &quot;is p .157 (like the national figure) or higher?&quot; We take a sample of 100 students, represented by a smaller circle. We find that 19 use marijuana.
    ```

    As before, we can formulate the null and alternative hypotheses in terms of p, the proportion of students in the college who use marijuana:

    *H*~*o*~*:* p = .157 (same as among all college students in the country).

    *H*~*a*~*:* p > .157 (higher than the national figure).
```

```{admonition} Example: 3
    Polls on certain topics are conducted routinely in order to monitor changes in the public's opinions over time. One such topic is the death penalty. In 2003 a poll estimated that 64% of U.S. adults support the death penalty for a person convicted of murder. In a more recent poll, 675 out of 1,000 U.S. adults chosen at random were in favor of the death penalty for convicted murderers. Do the results of this poll provide evidence that the proportion of U.S. adults who support the death penalty for convicted murderers (p)*changed*between 2003 and the later poll?

    Here is a figure that displays the information, as well as the question of interest:

    ```{figure} images/image214.gif
    :alt: A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor.

    A large circle represents the population US Adults. We want to know p about this population, which is population proportion which support the death penalty. The question we wish to answer is &quot;has p changed since 2003 (when it was .64)?&quot; We take a sample of 1000 US Adults, represented by a smaller circle. We find that 675 are in favor.
    ```

    Again, we can formulate the null and alternative hypotheses in term of p, the proportion of U.S. adults who support the death penalty for convicted murderers.

    *H*~*o*~*:* p =.64 (No change from 2003).

    *H*~*a*~*:* p ≠.64 (Some change since 2003).
```

## Learn By Doing

According to the American Association of Community Colleges, 23% of community college students receive federal grants. The California Community College Chancellor’s Office anticipates that the percentage is smaller for California community college students. They collect a sample of 1,000 community college students in California and find that 210 received federal grants.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

## Did I Get This?

Using data from 2008, the American Association of Community Colleges (AACC) reports that community college students constitute 46% of all U.S. undergraduates. Given the downturn in the U.S. economy, the AACC anticipates an increase in this percentage for 2010. A poll of 500 randomly chosen undergraduates taken in 2010 indicates that 52% are attending a community college.

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```

```{note}
    **Sectionnest**

    *(Interactive activity — available in the OLI platform)*
```
