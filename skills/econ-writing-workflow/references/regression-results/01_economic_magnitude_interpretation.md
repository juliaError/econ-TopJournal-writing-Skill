# Economic Magnitude Interpretation for Regression Results

## When To Use

Use this module before drafting or revising main regression results, important mechanism results, heterogeneity results, robustness results that enter the main text, abstracts, introductions, conclusions, or referee responses that discuss coefficient size.

The goal is to translate estimates into a reader-facing economic magnitude. Do not stop at sign, stars, or "economically significant" language.

## Core Rule

For every main result and every important mechanism or robustness result that will be discussed in the paper, write:

```text
direction -> magnitude -> benchmark -> interpretation
```

Choose at least one appropriate benchmark. Do not mechanically report mean, standard deviation, and percentile comparisons for every result. The benchmark must match the variable, model, identification source, and paper audience.

## Magnitude Selector

| Situation | Preferred benchmark | Use when | Guardrail |
|---|---|---|---|
| Natural units are intuitive | Units, dollars, hours, people, percentage points | Outcomes are levels, rates, probabilities, employment, income, costs, or counts | Distinguish percentage points from percent |
| Log outcome or log treatment | Percent or semi-elasticity | `ln(Y)`, `ln(X)`, log index, growth interpretation | For large coefficients, use exact `exp(beta)-1` instead of only the small-coefficient approximation |
| Policy or treatment has a real change size | Actual policy change, treatment intensity, or sample-period change | Tariffs, minimum wages, procurement, subsidies, experiment take-up, intervention dosage | Avoid unrealistic "0 to 1" changes unless the variable is truly binary |
| Variable is an index or abstract construct | One standard deviation change | Management index, digital finance index, institutional quality, culture, standardized factor | State the standardization sample or put it in table notes; add a concrete interpretation when possible |
| Exposure is skewed or distributional | P75-P25, P90-P10, top-bottom group, or rank change | Regional exposure, income ranks, firm size, productivity, inequality, mobility | State which sample defines the percentiles |
| Outcome mean is meaningful | Effect relative to mean | Participation rates, market shares, sales, debt, productivity, baseline levels | Avoid this as the only benchmark when the mean is near zero or heavily skewed |
| Interactions or nonlinear models | Net effect, marginal effect, or fitted contrast at meaningful values | DID/DDD, interaction terms, Probit/Logit, nonlinear specifications, heterogeneity | Do not interpret only the sign of the interaction term |
| Welfare or mechanism result | Back-of-envelope cost, benefit, fiscal burden, GDP share, ROI, or deadweight loss | Policy implications, fiscal effects, welfare channels, mechanism size | State data sources and assumptions clearly |
| Treatment is categorical | Difference between named categories | High/medium/low treatment, disaster intensity, erosion levels, policy groups | Define categories before interpreting magnitude |

## Writing Workflow

1. Identify units for `Y` and `X`: level, rate, percentage point, log, index, probability, binary variable, or interaction.
2. Choose the most reader-relevant benchmark. Prefer natural units and real policy changes over purely statistical benchmarks when they are available.
3. If the natural unit is not intuitive, add one statistical benchmark: standard deviation, percentile spread, or mean comparison.
4. For interactions, nonlinear models, and probability models, calculate net effects or marginal effects before drafting prose.
5. Put only the main magnitude in the text. Move auxiliary calculations to notes, appendix, or author memo unless the reader needs them immediately.
6. If descriptive statistics, percentiles, or standard deviations are missing, ask for them, compute them from the estimation sample, or mark a concrete `TODO`. Never invent them.

## Language-Specific Defaults

For English economics prose, it is natural to use standard deviations, interquartile ranges, policy benchmarks, and back-of-envelope calculations more explicitly. Write compactly and state the unit clearly.

For Chinese economics prose, prefer natural units, policy-relevant changes, percentage points, percent conversions, marginal effects, and net effects. Use standard deviations or percentile spreads when the variable is an index, the distribution is central to the argument, or no natural unit is intuitive. Do not turn the paragraph into a statistical checklist.

## Required Checks

- Do not write only "significant", "positive", "negative", "large", "obvious", or "economically meaningful" without a numerical benchmark.
- Distinguish `percent` from `percentage points`.
- State whether an elasticity, semi-elasticity, or marginal effect is evaluated at the mean, median, baseline, treatment group, control group, or another meaningful point.
- For log outcomes, use exact conversion when coefficients are large or when precision matters.
- For standardized variables, make the standardization sample visible in the table note, variable definition, or prose.
- For percentile comparisons, name the comparison: P75-P25, P90-P10, top versus bottom quartile, or another defined contrast.
- For mean comparisons, specify the denominator: estimation sample, pre-treatment sample, control group, baseline year, full sample, or target population.
- If identification comes from within-unit changes, do not rely only on full-sample mean or full-sample standard deviation when a within-sample, pre-treatment, treatment-intensity, or policy-relevant benchmark is more appropriate.
- For interaction terms, calculate the net effect at substantively meaningful values or groups before writing the interpretation.
- For null results, say whether the confidence interval rules out economically meaningful effects. A non-significant coefficient is not automatically zero.

## Manuscript-Safe Patterns

Use patterns like these after filling in actual numbers:

- "A one percentage point increase in X is associated with a Y percentage point change in Z."
- "A 10 percent increase in X implies an approximately Y percent change in Z."
- "Moving from the 25th to the 75th percentile of X corresponds to a Y-unit difference in Z."
- "Relative to the pre-treatment mean of Z, the estimate equals about Y percent."
- "At the sample mean, the marginal effect implies that X raises the probability of Z by Y percentage points."
- "For group A, the net effect is beta1 + beta3 x value, implying a Y change in Z."

Do not write author-facing calculation instructions in the manuscript, such as "we should compare this to the mean" or "this needs a magnitude check." Keep those in task notes or revision memos.
