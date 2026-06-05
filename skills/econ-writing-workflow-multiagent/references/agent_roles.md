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
