# Full Paper Multiagent Workflow

## Contents

- Purpose
- Baseline artifact audit
- Input, state, and evidence planning
- Architecture and section drafting
- Conservation, diction, and final consistency
- Final deliverable

## Purpose

Use this workflow when the user asks for a complete draft or major rewrite from a research question, result package, tables, figures, and design notes.

This workflow supports author-responsible drafting only. It must not be used for paid paper-writing services, undisclosed ghostwriting, fabricated research, or automatic submission.

## Workflow

### Step 0. Baseline Artifact Audit And Contract

For a mature revision, restructuring, shortening, or appendix relocation, load `artifact_conservation_and_depth_gates.md` before assigning roles.

- identify the user-accepted baseline by path and hash;
- classify `task_mode` and `rewrite_mode`;
- measure the main text with a fixed appendix boundary and measurement method;
- record target ranges, hard floors, cumulative reduction permission, `must_remain_main`, and allowed appendix moves;
- assign stable source-block IDs and initialize the conservation ledger.

Stop if required metrics are unavailable or the proposed scope implies material shortening without a target or approval.

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

For a mature `major_revision` or `restructure`, split this step into two passes:

1. **Architecture pass:** apply patches and reorder the complete accepted blocks; edit only transitions and duplicated signposting needed for coherence.
2. **Compression pass:** begin only after the full reordered manuscript exists, the ledger is complete, and the artifact budget has been measured. Remove genuine duplication within the recorded approval scope.

Update the conservation ledger and cumulative dashboard after every section return. Do not combine clean-slate rewriting, block movement, appendix relocation, and diction compression in one pass.

### Step 6. Main-Text Sufficiency And Conservation

Run `scripts/audit_manuscript_conservation.py` after architecture integration and again after any compression pass. Then route the baseline, candidate, artifact contract, ledger, and deterministic report to the Main-Text Sufficiency and Conservation Role.

- On `pass`, continue to diction.
- On `approval_required`, restore or preserve material unless the user gives a scoped approval that is recorded in the contract.
- On `fail`, restore missing or under-floor material and rerun the gate.
- On `metric_unavailable`, repair the measurement or require a bounded manual audit; never treat it as a pass.

### Step 7. Diction And Linter

Run the language-specific diction role only after section logic is stable.

- English: `econ-write/references/english-diction/`.
- Chinese: `cn-top-econ-writing/references/chinese-diction/`.

### Step 8. Final Consistency

Check:

- paper state versus draft;
- table/figure references;
- variable names;
- magnitudes;
- caveats;
- contribution preservation;
- manuscript voice;
- unresolved `TODO` items.

Do not enter this step while the artifact contract or main-text sufficiency gate is failing.

## Final Deliverable

Return the draft or revision with:

```text
Input audit:
Paper spine:
Table/figure placement:
Drafted sections:
Preserved claims:
Artifact-contract status:
Conservation-ledger status:
Remaining TODOs:
Risks:
Next pass:
```
