# Handoff Templates

## Delegation Template

Use this when assigning work to a sub-agent or staged role.

```text
Role:
Task:
Inputs to read:
Paper_state fields to respect:
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
