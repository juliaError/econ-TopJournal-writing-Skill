# Input Checklist

Use this file when the user asks for a full paper draft from a research question, regression tables, figures, slides, notes, or a result folder.

## Minimum Inputs

Before drafting, identify whether the user has provided:

- research question;
- target language and target journal or paper style;
- outcome, treatment or main explanatory variable, and key controls;
- sample definition, geography, time window, and unit of observation;
- empirical design or theoretical model logic;
- main regression tables and figure files;
- robustness, heterogeneity, and mechanism results;
- variable definitions and data source descriptions;
- intended contribution and closest literature;
- disclosure constraints, authorship constraints, or forbidden claims.

## Input Audit

Start with a compact audit:

- **Ready**: information that is available and can be used directly.
- **Partial**: information that can support a draft but needs `TODO` markers.
- **Missing**: information that blocks a specific section or claim.
- **Do not infer**: claims that would require new data, new regressions, undisclosed literature, or private author intent.

## Draftability Levels

- **Green**: research question, design, variables, main results, and basic literature position are available. Draft the paper and keep uncertainties narrow.
- **Yellow**: main results and question are available, but literature, mechanism, or data details are incomplete. Draft with explicit `TODO` markers.
- **Red**: tables or figures exist without a research question, variable meaning, or identification logic. Do not write a full paper. Produce an input request and provisional outline only.

## Output Template

```text
Input audit:
- Research question: [ready/partial/missing]
- Evidence package: [ready/partial/missing]
- Identification/model logic: [ready/partial/missing]
- Data and sample: [ready/partial/missing]
- Literature/contribution: [ready/partial/missing]
- Target language/journal: [ready/partial/missing]

Draftability: [green/yellow/red]
Blocked sections: [section names or none]
Required TODO markers: [specific missing items]
```
