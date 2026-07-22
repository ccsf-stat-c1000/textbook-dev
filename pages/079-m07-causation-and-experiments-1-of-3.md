# Experiments: Taking Control of the Explanatory Variable

## Causation and Experiments

Recall that in an experiment, it is the researchers who assign values of the explanatory variable to the participants. The key to ensuring that individuals differ only with respect to explanatory values—which is also the key to establishing causation—lies in the way this assignment is carried out. Let's return to the smoking cessation study as a context to explore the essential ingredients of experimental design.

:::{admonition} Example: Quitting Smoking (continued)
:class: tip

In our discussion of the distinction between observational studies and experiments, we described the following experiment: collect a representative sample of 1,000 individuals from the population of smokers who are just now trying to quit. We divide the sample into 4 groups of 250 and instruct each group to use a different method to quit. One year later, we contact the same 1,000 individuals and determine whose attempts succeeded while using our designated method.

This was an experiment, because the researchers themselves determined the values of the explanatory variable of interest for the individuals studied, rather than letting them choose.
:::

We will begin by using the context of this smoking cessation example to illustrate the specialized vocabulary of experiments. First of all, the explanatory variable, or *factor*, in this case is the method used to quit. The different imposed values of the explanatory variable, or {term}`treatments <treatment>`, consist of the four possible quitting methods. The groups receiving different treatments are called *treatment groups*. The group that tries to quit without drugs or therapy could be called the {term}`control group`—those individuals on whom no specific treatment was imposed. Ideally, the *subjects* (human participants in an experiment) in each treatment group differ from those in the other treatment groups only with respect to the treatment (quitting method). As mentioned in our discussion of why lurking variables prevent us from establishing causation in observational studies, eliminating all other differences among treatment groups will be the key to asserting causation via an experiment. How can this be accomplished?

## Randomized Controlled Experiments

Your intuition may already tell you, correctly, that *random assignment to treatments* is the best way to prevent treatment groups of individuals from differing from each other in ways other than the treatment assigned. Either computer software or tables can be utilized to accomplish the random assignment. The resulting design is called a *randomized controlled experiment*, because researchers control values of the explanatory variable with a randomization procedure. Under random assignment, the groups should not differ significantly with respect to any potential lurking variable. Then, if we see a relationship between the explanatory and response variables, we have evidence that it is a causal one.

```{figure} images/gen/m07-randomized-experiment.svg
:alt: A diagram of a randomized controlled experiment. From the population, a random sample of 1,000 is selected, and the participants are then randomly assigned to four groups: three treatment groups (drugs, therapy, both) and a control group (neither). Random assignment makes the four groups alike except for the treatment.
```

```{admonition} Comment
:class: important

Note that in a randomized controlled experiment, a randomization procedure may be used in two phases. First, a sample of subjects is collected. Ideally it would be a *random sample* so that it would be perfectly representative of the entire population. (*Comment:* often researchers have no choice but to recruit volunteers. Using volunteers may help to offset one of the drawbacks to experimentation which will be discussed later, namely the problem of noncompliance.) Second, we *assign individuals randomly* to the treatment groups to ensure that the only difference between them will be due to the treatment and we can get evidence of causation. At this stage, randomization is vital.
```

Let's discuss some other issues related to experimentation.

## Inclusion of a Control Group

A common misconception is that an experiment must include a control group of individuals receiving no treatment. There may be situations where a complete lack of treatment is not an option, or where including a control group is ethically questionable, or where researchers explore the effects of a treatment without making a comparison. Here are a few examples:

:::{admonition} Example: Comparing Two Drugs
:class: tip

If doctors want to conduct an experiment to determine whether Prograf or Cyclosporin is more effective as an immunosuppressant, they could randomly assign transplant patients to take one or the other of the drugs. It would, of course, be unethical to include a control group of patients not receiving any immunosuppressants.
:::

:::{admonition} Example: Sham Surgery
:class: tip

Recently, experiments have been conducted in which the treatment is a highly invasive brain surgery. The only way to have a legitimate control group in this case is to randomly assign half of the subjects to undergo the entire surgery except for the actual treatment component (inserting stem cells into the brain). This, of course, is also ethically problematic (but, believe it or not, is being done).
:::

:::{admonition} Example: A Single Treatment
:class: tip

There may even be an experiment designed with only a single treatment. For example, makers of a new hair product may ask a sample of individuals to treat their hair with that product over a period of several weeks, then assess how manageable their hair has become. Such a design is clearly flawed because of the absence of a comparison group, but it is still an experiment because use of the product has been imposed by its manufacturers, rather than chosen naturally by the individuals. A flawed experiment is nevertheless an experiment.
:::

```{admonition} Comment
:class: important

The word *control* is used in at least three different senses. In the context of observational studies, we *control for a confounding variable* by separating it out. Referring to an experiment as a *controlled experiment* stresses that the values of the experiment's explanatory variables (factors) have been assigned by researchers, as opposed to having occurred naturally. In the context of experiments, the {term}`control group` consists of subjects who do not receive a treatment, but who are otherwise handled identically to those who do receive the treatment.
```

## Check Your Understanding: Randomized Controlled Experiments

:::{quiz} In a randomized controlled experiment testing a new fertilizer, why does randomly assigning plots of land to fertilizer or no-fertilizer groups allow a causal conclusion?
:hint: What does random assignment do to potential lurking variables like soil quality or sunlight?
:feedback-0: Correct! Random assignment spreads lurking variables (soil, drainage, sun) roughly evenly across the groups, so a difference in yield can be attributed to the fertilizer itself.
:feedback-1: Random assignment doesn't eliminate variability—it balances it across the treatment groups.
:feedback-2: Random assignment concerns the internal validity (causation), not the representativeness of the plots.
* *It balances lurking variables across the groups, so the groups differ only in the treatment
* It removes all variability in the response variable
* It guarantees the plots represent all farmland in the country
:::

:::{quiz} In the smoking study, the group assigned to quit "cold turkey" (no drugs, no therapy) is best described as the:
:hint: Which group receives no active treatment but is otherwise handled identically?
:feedback-0: The factor is the explanatory variable itself (quitting method).
:feedback-1: Correct! The group receiving no specific treatment, handled identically otherwise, is the control group.
:feedback-2: A treatment group receives one of the imposed active treatments.
* Factor
* *Control group
* Treatment group
:::
