# Agent Roles

## Controller

Owns the workflow. Maintains `paper_state`, assigns roles, integrates outputs, resolves conflicts, and decides what the user sees.

The controller must not let specialized agents rewrite the paper's main claim without updating `paper_state` and flagging the change.

## Input Audit Role

Checks whether the provided materials are enough for the requested output.

Focus:

- research question;
- data, sample, variables, design;
- tables and figures;
- literature materials;
- target language and journal;
- missing facts and `TODO` items.

## Argument Logic Role

Checks the paper spine, contribution hierarchy, section order, repetition, emphasis, and whether results serve the main line.

Route to:

- stable workflow `references/argument-logic/` for general logic;
- `cn-top-econ-writing/references/argument-logic/` for Chinese top-journal logic.

## Research Aesthetics Review Role

An optional independent reviewer, enabled only when the user points out a problem with the argument or explicitly requests aesthetics review, for that affected or requested scope. Do not add it just because a task is long or complex, the controller suspects a problem, or a writer loads the aesthetics module. A spelling or layout complaint alone is not an argument-review trigger.

Read the complete shared v0.8 [research-aesthetics module](../../econ-writing-workflow/references/research-aesthetics.md). Reuse its author-calibrated criteria for Chinese or English prose and outlines; do not copy the module, build a new skill or state authority, or start idea training or blind evaluation.

The controller supplies the user's concern, confirmed author objectives and outline or existing paper state, and the relevant text with enough surrounding context. Use a native reviewer that did not draft the material under review. If an independent agent is unavailable, report that the requested independent review was not performed; do not label a same-agent reread independent. Reuse the existing controller-mediated request and return format.

Check the substantive choices, not just wording or isolated qualifications:

- whether the text makes the important economic question visible, rather than letting a subsidiary detail become the main question;
- whether its comparisons address the strongest relevant alternatives supported by the confirmed research, rather than an artificially weak comparison;
- whether the actors' choices, competing economic forces, and central tradeoff explain why the question matters;
- whether the order and allocation of space keep the paragraph, section, or chapter focused on the confirmed main question.

Return specific text locations, the substantive issue and its reasoning, a proposed adjustment of emphasis or order, and any question requiring author choice. Do not assume the user's concern proves a flaw; report when the available text does not substantiate it or the supplied context is insufficient. Do not reduce the review to small caveats or diction edits.

This role returns advice only: it does not edit the manuscript, change shared state, or claim to represent the human author's judgment. Suggestions that change the question, mechanism, comparison, or substantive claim go through the controller for explicit author approval before application. Author approval does not supply missing evidence. This review is not a semantic, literature, evidence, or final-acceptance pass and cannot satisfy or bypass those existing gates.

## Table And Figure Role

Judges main-text versus appendix placement, table/figure function, notes, captions, visual style, palettes, and export quality.

Route to `econ-table-figure-design`.

## Literature Positioning Role

Checks literature grouping, contribution margins, citation grounding, and whether claims are supported by supplied or inspected sources.

Do not invent citations or closest-literature claims.

## Section Drafting Role

Drafts sections only after the controller has settled the paper state, table/figure plan, and argument spine.

For large paper tasks, do not treat this as one generic writer. Use `section_agent_protocol.md` to create section cards for abstract, introduction, literature, theory/mechanism, empirical design, main results, mechanism, heterogeneity, robustness, and conclusion agents.

Route to:

- `econ-write` for English;
- `cn-top-econ-writing` for Chinese.

## Diction And Linter Role

Polishes language after structure is stable.

Route to:

- `econ-write/references/english-diction/` for English;
- `cn-top-econ-writing/references/chinese-diction/` for Chinese.

## Final Consistency Role

Checks terminology, variables, table and figure numbers, magnitudes, caveats, contribution preservation, manuscript voice, and unresolved `TODO` items.

This role should be skeptical and should not rewrite the paper unless the controller asks for a final integrated pass.
