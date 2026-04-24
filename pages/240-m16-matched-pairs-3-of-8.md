# Matched Pairs (3 of 8)

```{admonition} Learning Objectives
    - Specify the null and alternative hypotheses for comparing groups.
```

## Step 1: Stating the hypotheses.

Recall that in the t-test for a single mean our null hypothesis was:	$H_{o}:\mu=\mu_{o}$ and the alternative was one of	$H_{a}:\mu<or>or\neq\mu_{0}$ . Since the paired t-test is a special case of the one-sample t-test, the hypotheses are the same except that:

- Instead of simply	μ
we use the	notation $\mu_{d}$
to denote that the parameter of interest is the mean of the differences.
- In this course our null value	$\mu_{0}$
is always 0 (although technically, it does not have to be).

Therefore, in the paired t-test:

The null hypothesis is always:

$H_{o}:\mu_{d}=0$

and the alternative is one of :

```{figure} images/image065.gif
:alt: H_a: μ_d < 0 (one-sided), H_a: μ_d > 0 (one-sided), H_a: μ_d ≠ 0 (two-sided)

H_a: μ_d < 0 (one-sided), H_a: μ_d > 0 (one-sided), H_a: μ_d ≠ 0 (two-sided)
```

depending on the context.

Let's go back to our example to see how this works and why it makes sense.

```{admonition} Example: Drunk Driving
    Recall that in our "Are drivers impaired after drinking two beers?" example, our data was reduced to one sample of differences (one for each driver),

    ```{figure} images/image066.gif
    :alt: A table with the rows "Driver," "Sample 1 (before)," "Sample 2 (after)," and "Differences (before - after)." We only care about the Driver and Differences row.

    A table with the rows "Driver," "Sample 1 (before)," "Sample 2 (after)," and "Differences (before - after)." We only care about the Driver and Differences row.
    ```

    so our problem was reduced to inference about the mean of the differences	$\mu_{d}$	.

    ```{figure} images/image067.gif
    :alt: For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.

    For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.
    ```

    As we mentioned, the null hypothesis is:

    $H_{o}:\mu_{d}=0$ .

    The null hypothesis claims that the differences in reaction times are centered at (or around) 0, indicating that drinking two beers has no real impact on reaction times. In other words, drivers are not impaired after drinking two beers.

    In order to decide which of the alternatives is appropriate here we have to think about the context of the problem. Recall that we want to check whether drivers are impaired after drinking two beers. Thus, we want to know whether their reaction times are longer after the two beers. Since the differences were calculated before-after, longer reaction times after the beers would translate into negative differences. These differences are: 6.25 - 6.85, 2.96 - 4.78, etc.

    Therefore, the appropriate alternative here is:

    $H_{a}:\mu_{d}<0$

    indicating that the differences are centered at a negative number.
```

```{note}
    **Many Students Wonder**

    Matched Pairs

    *(Interactive activity — available in the OLI platform)*
```

## Comment

Recall that originally, the following figure represented our problem:

```{figure} images/image054.gif
:alt: The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.

The X variable is whether the driver had 2 beers or no beers. We have two populations, population 1 of sober drivers and population 2 of drivers who had two beers. For each population we have the Reaction Time (Y) mean, μ_1 for population 1 and μ_2 for population 2. We use the same drivers to generate the samples for both populations. The SRS of size 20 is created for population 1 before the drivers have had 2 beers, and using the same drivers, we generate the SRS of size 20 for population 2 after giving them 2 beers.
```

Later, we reduced the problem to inference about a single mean, the mean of the differences:

```{figure} images/image067.gif
:alt: For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.

For the population of all drivers, we are trying to find μ_d, which represents the mean of the difference in total reaction time (before 2 beers - after 2 beers). To do this, we generate a sample from the population. The sample consists of 20 differences.
```

Some students find it helpful to know that it turns out that	$\mu_{d}=\mu_{1}−\mu_{2}$. In other words, the difference between the means $\mu_{1}−\mu_{2}$ in the first representation is the same as the mean of the differences, $\mu_{d}$,in the second one. Some students find it easier to first think about the hypotheses in terms of	$\mu_{1}−\mu_{2}$	(as we did in the two-sample case) and then represent it in terms of	$\mu_{d}$.

In our example, since we want to test whether the reaction times in population 1 are shorter, we are testing $H_{o}:\mu_{1}−\mu_{2}=0 vs. H_{a}:\mu_{1}−\mu_{2}<0 $, which in the matched pairs design notation is translated to	$H_{o}:\mu_{d}=0 vs. H_{a}:\mu_{d}<0 $ .

Here is another example:

```{admonition} Example
    Suppose the effectiveness of a low-carb diet is studied with a matched pairs design, recording each participant's weight before and after dieting. What would be the appropriate hypotheses in this case?

    As before,	$\mu_{d}$ is the mean of the differences (weight before diet)-(weight after diet). In this case, if the diet is effective and participants' weight after the diet was indeed lower, we would expect the differences to be positive, and therefore the appropriate hypotheses in this case are:	$H_{o}:\mu_{d}=0 vs. H_{a}:\mu_{d}>0 $ .
```

## Did I Get This?

In each of the following cases, decide based on the context what the appropriate set of hypotheses is.

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
