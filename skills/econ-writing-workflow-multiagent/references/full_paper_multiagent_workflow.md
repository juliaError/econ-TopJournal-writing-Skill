# Full Paper Multiagent Workflow

## Purpose

Use this workflow when the user asks for a complete draft or major rewrite from a research question, result package, tables, figures, and design notes.

This workflow supports author-responsible drafting only. It must not be used for paid paper-writing services, undisclosed ghostwriting, fabricated research, or automatic submission.

## Workflow

### Step 1. Input Audit

Use the input audit role to determine draftability:

- enough to draft;
- enough to outline but not draft;
- enough to revise selected sections only;
- insufficient without user clarification.

Output missing facts as `TODO`.

### Step 2. Paper State

Create or update `paper_state` before any section drafting.

Do not proceed to full drafting if research question, main result, data/sample, or identification/model information is missing. Produce an outline with `TODO` items instead.

### Step 3. Table/Figure Plan

Route to `econ-table-figure-design`.

Decide:

- main text tables;
- appendix tables;
- main text figures;
- appendix figures;
- table/figure notes and captions;
- whether any item is confusing, redundant, or unsupported.

This is the first table/figure pass. Later section agents may request targeted table/figure review through `cross_agent_collaboration_protocol.md` if their section claim needs more specific evidence placement or note/caption decisions.

### Step 4. Argument Spine

Use the argument logic role to produce:

- one-sentence paper spine;
- contribution hierarchy;
- section order;
- mechanism position;
- robustness and heterogeneity role;
- repeated or misplaced material.

### Step 5. Section Drafting

Before drafting, load `section_agent_protocol.md` and have the controller create a section map. Each section agent must receive a section card before writing.

When a section agent identifies a missing table/figure, argument-logic, literature, diction, or empirical decision, pause drafting and use `cross_agent_collaboration_protocol.md`. The controller updates the section card before the section agent continues.

Draft in this order:

1. results and table/figure narration;
2. empirical design or model;
3. mechanism, heterogeneity, and robustness;
4. literature positioning;
5. introduction;
6. abstract;
7. conclusion.

Route English prose to `econ-write`; route Chinese prose to `cn-top-econ-writing`.

After each section agent returns, the controller checks whether the section claim still follows the paper spine before sending the text to diction or final consistency.

### Step 6. Diction And Linter

Run the language-specific diction role only after section logic is stable.

- English: `econ-write/references/english-diction/`.
- Chinese: `cn-top-econ-writing/references/chinese-diction/`.

### Step 7. Final Consistency

Check:

- paper state versus draft;
- table/figure references;
- variable names;
- magnitudes;
- caveats;
- contribution preservation;
- manuscript voice;
- unresolved `TODO` items.

## Final Deliverable

Return the draft or revision with:

```text
Input audit:
Paper spine:
Table/figure placement:
Drafted sections:
Preserved claims:
Remaining TODOs:
Risks:
Next pass:
```
