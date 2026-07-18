---
name: econ-writing-workflow-multiagent
description: Experimental beta entry point for large economics writing projects that need multi-agent or staged-agent coordination, including full paper drafting from result packages, many tables and figures, major revisions, mature-manuscript restructuring, bilingual writing, long context management, shared paper_state and artifact-conservation protocols, role handoffs, conflict resolution, and integration across econ-write, cn-top-econ-writing, econ-table-figure-design, and empirical-econ-workflow. Use for complex projects, not short one-off polishing.
---

# Economics Writing Workflow Multiagent

## Role

This is an experimental coordination skill for large economics writing projects. It does not replace or rewrite the stable `econ-writing-workflow`; it sits beside it as a beta workflow.

Use this skill only as the controller for multi-agent or staged-agent work. It should coordinate specialized skills, maintain a shared paper state, manage context budget, and integrate outputs. It should not duplicate the substantive rules already maintained in:

- `econ-write`
- `cn-top-econ-writing`
- `econ-table-figure-design`
- `empirical-econ-workflow`

If the environment supports true sub-agents, delegate narrow tasks with explicit handoff templates. If not, simulate the same roles sequentially in one agent while keeping the same paper-state and handoff discipline.

## When To Use

Use this beta workflow for:

- full paper drafting from a research question, result package, tables, figures, variable notes, and design notes;
- long revision projects with many sections, tables, figures, appendix items, or referee comments;
- projects where English and Chinese writing modules both matter;
- tasks where a single-agent context is likely to lose track of contributions, variables, magnitudes, caveats, or table/figure placement;
- comparisons between the stable workflow and a multi-agent-aware workflow.

Do not use it for:

- one paragraph of polishing;
- a single abstract rewrite;
- one table note or one figure caption;
- simple translation;
- pure data cleaning, regressions, estimation, or code execution without a writing integration task.

For small tasks, use the stable `econ-writing-workflow` or the relevant child skill directly.

## Core Rule

Before splitting work across agents or roles, create or update a shared paper state. The paper state is the single source of truth. No agent may invent or silently alter:

- research question;
- contributions;
- data, sample, period, or variable definitions;
- identification or model assumptions;
- coefficient values, magnitudes, mechanisms, robustness results, or caveats;
- literature claims or citations.

Missing information must remain as a concrete `TODO`.

Context compression governs handoffs and duplicated input, not the reader-facing manuscript. Preserve the accepted artifact budget and substantive main-text coverage unless the user, project rules, or verified format requirements authorize a shorter output.

For an accepted mature manuscript, default to `patch_existing` or `reorder_existing_blocks`. Do not use clean-slate section redrafting unless the user authorizes `full_redraft` or the controller records why the existing section is unusable.

## Routing

Load the relevant reference file before starting each phase:

- Before any multi-agent task, load `references/controller_startup_checklist.md`.
- For shared facts and the `paper_state` schema, load `references/paper_state_protocol.md`.
- For full drafting, mature-manuscript revision, restructuring, shortening, or appendix relocation, load `references/artifact_conservation_and_depth_gates.md` before setting the paper spine or assigning roles.
- For role definitions and when to use true sub-agents versus staged roles, load `references/agent_roles.md`.
- For structured delegation and return formats, load `references/handoff_templates.md`.
- For deciding whether to split work, load `references/context_budget_rules.md`.
- For merging outputs and resolving disagreements, load `references/integration_and_conflict_resolution.md`.
- For controller-led section agents, section cards, and section-level integration, load `references/section_agent_protocol.md`.
- For controller-mediated collaboration between section agents and functional agents, load `references/cross_agent_collaboration_protocol.md`.
- For complete result-package-to-paper workflows, load `references/full_paper_multiagent_workflow.md`.

Then route substantive work to child skills:

- English writing and revision: `econ-write`.
- English diction cleanup: `econ-write` with `references/english-diction/`.
- Chinese top-journal writing: `cn-top-econ-writing`.
- Chinese diction cleanup: `cn-top-econ-writing` with `references/chinese-diction/`.
- Chinese argument logic: `cn-top-econ-writing` with `references/argument-logic/`.
- Tables, figures, notes, captions, palettes, and main-text versus appendix placement: `econ-table-figure-design`.
- Data cleaning, variable construction, regression estimation, and reproducibility: `empirical-econ-workflow`.

## Default Workflow

For complex paper tasks, proceed in this order:

1. Run the controller startup checklist.
2. Classify the request and decide whether multi-agent coordination is justified.
3. Build or update `paper_state` and, when applicable, its artifact contract, baseline measurements, and conservation ledger.
4. Audit inputs and mark missing facts or unavailable artifact metrics as `TODO`.
5. Settle the paper spine and create section cards with rewrite modes and artifact budgets when section-level work is needed.
6. Assign narrow roles or staged passes using the handoff template.
7. Use controller-mediated cross-agent loops when a section needs table/figure, argument-logic, literature, diction, empirical, or conservation review.
8. Route each substantive pass to the relevant child skill.
9. Integrate outputs against `paper_state`, the artifact contract, and the conservation ledger, not against memory.
10. Run deterministic conservation checks and the independent main-text sufficiency review before diction or final consistency.
11. Run conflict checks, drop checks, and final consistency checks.
12. Return a concise result plus unresolved `TODO` and approval items.

## Output Check

Before finalizing, confirm:

- the stable workflow and existing child skills were not modified as part of this beta workflow;
- the controller startup checklist was run before delegation;
- every delegated or staged pass used `paper_state` as the authority;
- every section agent worked from a controller-approved section card when section-level drafting was used;
- every section-functional collaboration went through the controller and updated the section card when needed;
- disagreements were resolved explicitly or left as user-facing `TODO`;
- table/figure decisions were integrated into the argument spine;
- prose edits did not delete central contributions, mechanisms, magnitudes, caveats, or design features;
- any mature-draft revision followed its recorded rewrite mode and mapped every substantive source block to a conservation-ledger disposition;
- context or handoff limits were not used as manuscript-length instructions;
- the integrated manuscript satisfies the artifact contract, cumulative compression permission, and main-text self-containment gate;
- deterministic audit status is `pass`; if it first returned `approval_required`, any scoped approval was recorded and the audit was rerun to `pass`;
- no fabricated data, citations, results, or policy implications entered the output.
