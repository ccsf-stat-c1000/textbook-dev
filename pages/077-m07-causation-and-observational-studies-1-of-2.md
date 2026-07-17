# Why Observational Studies Struggle to Prove Causation

```{admonition} Learning Objectives
:class: note

- Explain how the study design impacts the types of conclusions that can be drawn.
```

## Causation and Observational Studies

Suppose the *observational study* described on the previous page were carried out, and researchers determined that the percentage succeeding with the combination drug/therapy method was highest, while the percentage succeeding with neither therapy nor drugs was lowest. In other words, suppose there is clear evidence of an association between method used and success rate. Could they then conclude that the combination drug/therapy method causes success more than using neither therapy nor a drug?

```{figure} images/gen/m07-method-response.svg
:alt: A diagram with the explanatory variable, method, connected by an arrow labeled causes with a question mark to the response variable, success or failure.
```

It is at precisely this point that we confront the underlying weakness of most observational studies: some members of the sample have opted for certain values of the explanatory variable (method of quitting), while others have opted for other values. It could be that those individuals may be different in additional ways that would also play a role in the response of interest. For instance, suppose women are more likely to choose certain methods to quit, and suppose women in general tend to quit more successfully than men. The data would make it appear that the method itself were responsible for success, whereas in truth it may just be that being female is the reason for success. We can express this scenario in terms of the key variables involved. In addition to the explanatory variable (method) and the response variable (success or failure), a third, *lurking* variable (gender) is tied in (or *confounded*) with the explanatory variable's values, and may itself cause the response to be success or failure. The following diagram illustrates this situation.

```{figure} images/gen/m07-lurking-gender.svg
:alt: The method-to-response diagram with a lurking variable, gender, added below. A dashed line labeled confounded connects gender to the method, and a solid arrow labeled may affect points from gender to the response, success or failure.
```

Since the difficulty arises because of the lurking variable's values being tied in with those of the explanatory variable, one way to attempt to unravel the true nature of the relationship between explanatory and response variables is to separate out the effects of the lurking variable. In general, we *control* for the effects of a lurking variable by separately studying groups that are similar with respect to this variable.

We could control for the lurking variable "gender" by studying women and men separately. Then, if both women and men who chose one method have higher success rates than those opting for another method, we would be closer to producing evidence of causation.

```{figure} images/gen/m07-control-gender.svg
:alt: Two separate diagrams, one for women only and one for men only. In each, method points to success or failure, showing that the relationship is now studied separately within each gender.
```

The diagram above demonstrates how straightforward it is to control for the lurking variable gender.

Notice that we did not claim that controlling for gender would allow us to make a definite claim of causation, only that we would be closer to establishing a causal connection. This is due to the fact that other lurking variables may also be involved, such as the level of the participants' desire to quit. Specifically, those who have chosen to use the drug/therapy method may already be the ones who are most determined to succeed, while those who have chosen to quit without investing in drugs or therapy may, from the outset, be less committed to quitting. The following diagram illustrates this scenario.

```{figure} images/gen/m07-lurking-desire.svg
:alt: The method-to-response diagram with a different lurking variable, desire to quit. A dashed line notes that the most determined smokers choose drugs or therapy, confounding desire with method, and a solid arrow shows that desire to quit may also affect success or failure.
```

To attempt to control for this lurking variable, we could interview the individuals at the outset in order to rate their desire to quit on a scale of 1 (weakest) to 5 (strongest), and study the relationship between method and success separately for each of the five groups. But desire to quit is obviously a very subjective thing, difficult to assign a specific number to. Realistically, we may be unable to effectively control for the lurking variable "desire to quit."

Furthermore, who's to say that gender and/or desire to quit are the only lurking variables involved? There may be other subtle differences among individuals who choose one of the four various methods that researchers fail to imagine as they attempt to control for possible lurking variables. For example, smokers who opt to quit using neither therapy nor drugs may tend to be in a lower income bracket than those who opt for (and can afford) drugs and/or therapy. Perhaps smokers in a lower income bracket also tend to be less successful in quitting because more of their family members and co-workers smoke. Thus, socioeconomic status is yet another possible lurking variable in the relationship between cessation method and success rate.

It is because of the existence of a virtually unlimited number of potential lurking variables that we can never be 100% certain of a claim of causation based on an observational study. On the other hand, observational studies are an extremely common tool used by researchers to attempt to draw conclusions about causal connections. If great care is taken to control for the most likely lurking variables (and to avoid other pitfalls which we will discuss presently), and if common sense indicates that there is good reason for one variable to cause changes in the other, then researchers may assert that an observational study provides good evidence of causation.
