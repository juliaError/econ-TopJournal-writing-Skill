# Handoff Templates

## Contents

- Delegation and return
- Drafting and table/figure handoffs
- Section-functional collaboration
- Conservation audit
- Conflict handoff

## Delegation Template

Use this when assigning work to a sub-agent or staged role.

```text
Role:
Task:
Inputs to read:
Paper_state fields to respect:
Artifact contract and ledger slice:
Allowed changes:
Forbidden changes:
Questions to answer:
Expected output format:
Maximum scope:
```

## Return Template

Every role should return structured output, not a loose essay.

```text
Role:
Inputs read:
Claims used:
Findings:
Recommended changes:
Must preserve:
Words before/after:
Blocks revised, reordered, merged, moved, or omitted:
Conservation-ledger updates:
Main-text self-containment check:
Approval needed:
Conflicts with paper_state:
Missing information:
Output for next role:
```

## Drafting Handoff

Use this before drafting a section.

```text
Section:
Target language:
Reader-facing purpose:
Paper_state facts to use:
Tables/figures to cite:
Claims to preserve:
Caveats to preserve:
Rewrite mode:
Baseline and target length:
Must remain in main text:
Permitted appendix moves:
Cumulative main-text reduction before this task:
Ledger slice:
Do not mention:
TODO items to leave visible:
```

## Table/Figure Handoff

Use this for result packages.

```text
Table/Figure item:
Proposed function:
Main text or appendix:
Evidence for main claim:
Needed note/caption elements:
Risks or ambiguity:
Follow-up needed:
```

## Section-To-Functional Handoff

Use this when a section agent needs a functional agent review.

```text
Requesting section:
Section claim:
Functional role needed:
Question:
Evidence or text to review:
Decision needed:
Current section card fields:
```

## Functional-To-Section Return

Use this when a functional agent returns a bounded decision.

```text
Functional role:
Inputs read:
Answer:
Recommended section card update:
Recommended paper_state update:
Risks:
Needs user confirmation:
```

## Conservation Audit Handoff

Use this after integration and before diction or final consistency.

```text
Accepted baseline:
Candidate manuscript:
Artifact contract:
Measurement contract:
Cumulative dashboard:
Conservation ledger:
Deterministic report:
Questions for semantic sufficiency review:
```

Require this return:

```text
Deterministic status:
Missing main-text functions:
Unjustified appendix dependencies:
Unmapped source blocks:
Sections below budget:
Cumulative reduction:
Recovery required:
Approval required:
Gate decision: pass | approval_required | fail | metric_unavailable
```

## Conflict Handoff

Use this when roles disagree.

```text
Conflict:
Agent/role outputs involved:
Paper_state authority:
Evidence inspected:
Recommended resolution:
Needs user decision:
```
