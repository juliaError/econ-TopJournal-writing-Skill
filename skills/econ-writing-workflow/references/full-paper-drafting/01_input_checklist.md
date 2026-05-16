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
- local literature materials: PDFs, notes, extracted text, `.bib` files, source ledgers, or reference-paper folders;
- literature-dependent objects that the paper uses or adapts: data, theory, variables, mechanisms, classifications, specifications, controls, fixed effects, heterogeneity choices, or robustness designs;
- disclosure constraints, authorship constraints, or forbidden claims.

## Input Audit

Start with a compact audit:

- **Ready**: information that is available and can be used directly.
- **Partial**: information that can support a draft but needs `TODO` markers.
- **Missing**: information that blocks a specific section or claim.
- **Do not infer**: claims that would require new data, new regressions, undisclosed literature, or private author intent.

If the literature materials are missing or thin, ask whether the user considers them sufficient and whether the agent should help search for publicly available papers. If important Chinese or paywalled papers cannot be inspected locally, continue only with explicit TODOs or user confirmation for affected literature and judgment claims.

## Draftability Levels

- **Green**: research question, design, variables, main results, and basic literature position are available. Draft the paper and keep uncertainties narrow.
- **Yellow**: main results and question are available, but literature, mechanism, or data details are incomplete. Draft with explicit `TODO` markers.
- **Red**: tables or figures exist without a research question, variable meaning, or identification logic. Do not write a full paper. Produce an input request and provisional outline only.

Green requires more than a reference list: when the paper relies on literature-based data, theories, variables, mechanisms, classifications, or empirical choices, the relevant source material must be available or summarized well enough to align terminology, construction, scope, and claim strength.

## Output Template

```text
Input audit:
- Research question: [ready/partial/missing]
- Evidence package: [ready/partial/missing]
- Identification/model logic: [ready/partial/missing]
- Data and sample: [ready/partial/missing]
- Literature/contribution: [ready/partial/missing]
- Literature grounding: [source materials sufficient? judgment alignment needed?]
- Target language/journal: [ready/partial/missing]

Draftability: [green/yellow/red]
Blocked sections: [section names or none]
Required TODO markers: [specific missing items]
```
