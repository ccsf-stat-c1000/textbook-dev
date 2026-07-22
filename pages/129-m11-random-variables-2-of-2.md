# Discrete or Continuous? Classifying Random Variables

```{admonition} Learning Objectives
:class: note

- Distinguish between discrete and continuous random variables.
```

Before we go any further, a few observations about the nature of discrete and continuous random variables should be mentioned.

```{admonition} Comments
:class: important

1. Sometimes, continuous random variables are "rounded" and are therefore "in a discrete disguise." For example:

   - time spent watching TV in a week, rounded to the nearest hour (or minute)
   - outside temperature, to the nearest degree
   - a person's weight, to the nearest pound

   Even though they "look like" discrete variables, these are still continuous random variables, and we will in most cases treat them as such.

2. On the other hand, there are some variables which are discrete in nature, but take so many distinct possible values that it will be much easier to treat them as continuous rather than discrete:

   - the IQ of a randomly chosen person
   - the SAT score of a randomly chosen student
   - the annual salary of a randomly chosen CEO, whether rounded to the nearest dollar or the nearest cent

3. Sometimes we have a discrete random variable but do not know the extent of its possible values. For example: How many accidents will occur in a particular intersection this month? We may know from previously collected data that this number is from 0–5. But 6, 7, or more accidents could be possible.

4. A good rule of thumb is that *discrete* random variables are things we *count*, while *continuous* random variables are things we *measure*:

   - We counted the number of tails and the number of ears with earrings. These were discrete random variables.
   - We measured the weight of the lightweight boxer. This was a continuous random variable.
```

Often we can have a subject matter for which we can collect data that could involve a discrete or a continuous random variable, depending on the information we wish to know.

:::{admonition} Example: Soft Drinks
:class: tip

Suppose we want to know *how many days per week you drink a soft drink*. The sample space would be S = { 0, 1, 2, 3, 4, 5, 6, 7 }. There are a finite number of values for this variable. This would be a discrete random variable.

Instead, suppose we want to know *how many ounces of soft drinks you consume per week*. Even if we round to the nearest ounce, the answer is a measurement. Thus, this would be a continuous random variable.
:::

:::{admonition} Example: x-bar
:class: tip

Suppose we are interested in the weights of all males. We take a random sample and get the mean for that sample, namely $\bar{x}$. We then take another random sample (with the same sample size) and get another $\bar{x}$.

We would expect the values of the $\bar{x}$s from these two samples to be different, but pretty close in value.

Each time we take a sample we'll get a different $\bar{x}$. We will take lots of samples and thus get many $\bar{x}$s.

The value of $\bar{x}$ from these repeated samples is a random variable. Since it can take on any value within an interval of possible male weights, it is a continuous random variable.
:::

## Check Your Understanding: Discrete and Continuous Random Variables

:::{quiz} Classify each random variable: X = the number of text messages a student sends in a day, and Y = the length of time (in minutes) a student spends on the phone in a day.
:hint: Count vs. measure.
:feedback-0: Correct! Messages are counted (discrete); time is measured (continuous), even if we round to the nearest minute.
:feedback-1: The number of messages is a count with listable values—discrete.
:feedback-2: Time spent is a measurement that can take any value in an interval—continuous.
* *X is discrete; Y is continuous
* Both are continuous
* Both are discrete
:::

:::{quiz} A hospital records the birth weight of each newborn, rounded to the nearest gram. How should this variable be treated?
:hint: Rounding puts a continuous variable "in a discrete disguise."
:feedback-0: Correct! Weight is a measurement—a continuous random variable—even though rounding makes it look discrete.
:feedback-1: The rounded values look discrete, but the underlying quantity is a measurement, and we treat it as continuous.
* *As a continuous random variable in a "discrete disguise"
* As a discrete random variable, since only whole grams are recorded
:::

We devote a great deal of attention to random variables, since random variables and the probabilities that are associated with them play a vital role in the theory behind statistical inference, our ultimate goal in this course.

This module is organized in two parts; one on discrete random variables, and one on continuous. We'll start with discrete.
