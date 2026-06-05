# Section Agent Protocol

## Purpose

Use this protocol when a paper task is large enough that each major section needs its own focused pass. The controller remains responsible for the whole paper; section agents work only inside the section contract assigned to them.

This protocol adds section-level specialization without letting chapters drift away from the central argument.

## Controller Duties

Before assigning section agents, the controller must settle:

- `paper_state`;
- one-sentence paper spine;
- contribution hierarchy;
- table/figure placement plan;
- target language and journal style;
- missing facts and `TODO` items.

Then create a section map. No section agent should draft before receiving its section card.

## Section Card

```text
section_id:
section_name:
target_language:
section_purpose:
reader_question:
paper_spine_link:
must_preserve:
must_not_claim:
inputs_to_read:
tables_figures_to_use:
handoff_from_previous_section:
handoff_to_next_section:
child_skill_to_use:
open_todos:
```

## Section Agents

### Abstract Agent

Purpose: compress the paper spine into the shortest complete version.

Must preserve:

- research question;
- main contribution;
- main result or proposition;
- mechanism if it is part of the contribution;
- key data/design feature;
- necessary caveat.

Must not:

- add results not in `paper_state`;
- delete secondary contribution if the controller marks it as strategic;
- turn a mixed theory-empirical paper into a pure measurement paper.

### Introduction Agent

Purpose: make the reader understand the question, why it matters, how the paper answers it, what it finds, and what it contributes.

Must preserve:

- problem tension;
- design or argument path;
- main result and magnitude when available;
- mechanism;
- contribution relative to literature;
- boundary conditions.

Must not:

- bury the main result;
- turn literature review into a citation list;
- let background crowd out the research question.

### Literature Positioning Agent

Purpose: organize close literature by contribution margin.

Must preserve:

- closest literatures;
- what each literature explains;
- what margin this paper adds;
- limits of claim strength when sources are missing.

Must not invent citations or claim "first" unless verified.

### Theory And Mechanism Agent

Purpose: connect economic actors, constraints, behavior, and testable implications.

Must preserve:

- actor;
- constraint or incentive;
- behavior change;
- observable implication;
- link to later main result, mechanism, or heterogeneity evidence.

Must not write abstract concepts without empirical or model anchors.

### Empirical Design Agent

Purpose: explain sample, variables, identification, model, and comparison.

Must preserve:

- data source and period;
- unit of observation;
- treatment or key variable;
- comparison group or model object;
- fixed effects, controls, clustering, and sample restrictions when known;
- identification caveat.

Must not invent estimation details or overstate causality.

### Main Results Agent

Purpose: explain the main table or figure as the answer to the research question.

Must preserve:

- core coefficient, sign, magnitude, or proposition;
- economic interpretation;
- sample comparability;
- design credibility;
- link to mechanism or next section.

Must not do column-by-column narration unless needed for identification.

### Mechanism Agent

Purpose: explain why the main result arises.

Must preserve:

- mechanism promised by the theory or introduction;
- evidence type and strength;
- link between mechanism measure and economic behavior.

Must not claim proof when evidence is only suggestive.

### Heterogeneity Agent

Purpose: show where, for whom, or under what conditions the effect differs.

Must preserve:

- reason for each split;
- link to mechanism, policy target, or scope condition;
- whether the result belongs in main text or appendix.

Must not report every possible split.

### Robustness Agent

Purpose: answer threats to interpretation.

Must preserve:

- the threat each check addresses;
- what changes and what remains stable;
- main text versus appendix placement.

Must not write all checks as "results remain significant".

### Conclusion Agent

Purpose: return to the research question, contribution, scope, and implication.

Must preserve:

- central finding;
- mechanism or theoretical takeaway;
- boundary conditions;
- policy or research implication supported by the paper.

Must not introduce new evidence, new literature, or unsupported policy claims.

## Section Return Format

```text
section_id:
section_agent:
inputs_read:
section_claim:
draft_or_revision:
must_preserve_check:
conflicts_with_paper_state:
handoff_to_next_section:
remaining_todos:
```

## Controller Integration Pass

After section agents return, the controller must check:

- all section claims point to the same paper spine;
- key terms, variables, and mechanisms are stable;
- main contribution and secondary contribution are preserved;
- no section repeats another section's job;
- tables and figures are cited only where they serve the argument;
- caveats remain visible;
- diction passes do not narrow or inflate claims.

If a section fails this check, return it to the relevant section agent with a narrowed revision card.
