# Agent Roles

## Controller

Owns the workflow. Maintains `paper_state`, the artifact contract, conservation ledger, and cumulative dashboard; assigns roles, integrates outputs, resolves conflicts, and decides what the user sees.

The controller must not let specialized agents rewrite the paper's main claim without updating `paper_state` and flagging the change.

## Input Audit Role

Checks whether the provided materials are enough for the requested output.

Focus:

- research question;
- data, sample, variables, design;
- tables and figures;
- literature materials;
- accepted baseline, project artifact constraints, and available main-text measurements;
- target language and journal;
- missing facts and `TODO` items.

## Argument Logic Role

Checks the paper spine, contribution hierarchy, section order, repetition, emphasis, and whether results serve the main line.

Route to:

- stable workflow `references/argument-logic/` for general logic;
- `cn-top-econ-writing/references/argument-logic/` for Chinese top-journal logic.

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

## Main-Text Sufficiency And Conservation Role

Audit the integrated candidate against the accepted baseline, artifact contract, cumulative dashboard, and conservation ledger. Keep this role independent from drafting and diction.

Report:

- missing main-text functions and unjustified appendix dependencies;
- cumulative main-text word and page changes;
- source blocks without a ledger disposition;
- whole sections or core labels that disappeared or crossed the appendix boundary;
- sections below their approved budget or minimum-depth questions;
- deterministic audit status and unresolved approval triggers.

Do not polish prose, silently restore text, or change the artifact contract. Block diction and finalization when status is `fail`, `metric_unavailable`, or unapproved `approval_required`; return the recovery or approval decision to the controller and user.

## Final Consistency Role

Checks terminology, variables, table and figure numbers, magnitudes, caveats, contribution preservation, manuscript voice, and unresolved `TODO` items after the sufficiency and conservation gate passes.

This role should be skeptical and should not rewrite the paper unless the controller asks for a final integrated pass.
