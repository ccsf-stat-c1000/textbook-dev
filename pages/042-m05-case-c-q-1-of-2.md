# Comparing Groups on a Quantitative Response (Case C→Q)

## Case C→Q: Categorical Explanatory Variable and Quantitative Response Variable

Recall the role-type classification table for framing our discussion about the relationship between two variables:

```{figure} images/gen/m05-role-type-cq.svg
:alt: The role-type classification table with the C to Q cell highlighted, indicating that this part covers a categorical explanatory variable paired with a quantitative response variable.
```

We are now ready to start with Case C→Q, exploring the relationship between two variables where the explanatory variable is categorical, and the response variable is quantitative. As you'll discover, exploring relationships of this type is something we've already discussed in this course, but we didn't frame the discussion this way.

::::{admonition} Example: Hot Dogs
:class: tip

*Background:* People who are concerned about their health may prefer hot dogs that are low in calories. A study was conducted by a concerned health group in which 54 major hot dog brands were examined, and their calorie contents recorded. In addition, each brand was classified by type: beef, poultry, and meat (mostly pork and beef, but up to 15% poultry meat). The purpose of the study was to examine whether the *number of calories* a hot dog has is related to (or affected by) its *type*. (Reference: Moore, David S., and George P. McCabe (1989). *Introduction to the Practice of Statistics*. Original source: *Consumer Reports*, June 1986, pp. 366-367.)

Answering this question requires us to examine the relationship between the categorical variable Type and the quantitative variable Calories. Because the question of interest is whether the type of hot dog affects calorie content,

- the *explanatory* variable is *Type*, and
- the *response* variable is *Calories*.

Here is what the raw data look like:

| Brand | Type | Calories |
| --- | --- | --- |
| Brand 1 | Beef | 186 |
| Brand 2 | Poultry | 129 |
| Brand 3 | Beef | 181 |
| Brand 4 | Meat | 183 |
| ... | ... | ... |
| Brand 54 | Poultry | 144 |

The raw data are a list of types and calorie contents, and are not very useful in that form. To explore how the number of calories is related to the type of hot dog, we need an informative visual display of the data that will compare the three types of hot dogs with respect to their calorie content.

The visual display that we'll use is *side-by-side boxplots* (which we've seen before). The side-by-side boxplots will allow us to *compare the distribution* of calorie counts within each category of the explanatory variable, hot dog type:

```{figure} images/gen/m05-hotdog-boxplots.svg
:alt: Side-by-side vertical boxplots of calories for beef, meat, and poultry hot dogs. The beef and meat boxplots sit high and nearly overlap, with medians around 152 to 153 calories. The poultry boxplot sits distinctly lower, with a median of 113 calories, below even the first quartiles of the other two types.
```

As before, we supplement the side-by-side boxplots with the descriptive statistics of the calorie content (response) for each type of hot dog separately (i.e., for each level of the explanatory variable separately):

| Statistic | Beef | Meat | Poultry |
| --- | --- | --- | --- |
| min | 111 | 107 | 86 |
| Q1 | 139.5 | 138.5 | 100.5 |
| Median | 152.5 | 153 | 113 |
| Q3 | 179.75 | 180.5 | 142.5 |
| Max | 190 | 195 | 152 |

Let's summarize the results we got and interpret them in the context of the question we posed:

By examining the three side-by-side boxplots and the numerical summaries, we see at once that poultry hot dogs, as a group, contain fewer calories than those made of beef or meat. The median number of calories in poultry hot dogs (113) is less than the median (and even the first quartile) of either of the other two distributions (medians 152.5 and 153). The spread of the three distributions is about the same, if IQR is considered (all slightly above 40), but the (full) ranges vary slightly more (beef: 79, meat: 88, poultry: 66). The general recommendation to the health-conscious consumer is to eat poultry hot dogs. It should be noted, though, that since each of the three types of hot dogs shows quite a large spread among brands, simply buying a poultry hot dog does not guarantee a low-calorie food.
::::

What we learn from this example is that when exploring the relationship between a categorical explanatory variable and a quantitative response (Case C→Q), we essentially *compare the distributions of the quantitative response for each category of the explanatory variable* using side-by-side boxplots supplemented by descriptive statistics. Recall that we have actually done this before when we talked about the boxplot and argued that boxplots are most useful when presented side by side for comparing distributions of two or more groups. This is exactly what we are doing here!
