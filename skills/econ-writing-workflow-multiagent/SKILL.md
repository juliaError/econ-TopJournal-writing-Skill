---
name: econ-writing-workflow-multiagent
description: Experimental beta entry point for large economics writing projects that need multi-agent or staged-agent coordination, including full paper drafting from result packages, many tables and figures, major revisions, bilingual writing, long context management, shared paper_state protocols, role handoffs, conflict resolution, and integration across econ-write, cn-top-econ-writing, econ-table-figure-design, and empirical-econ-workflow. Use for complex projects, not short one-off polishing.
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

## Routing

Load the relevant reference file before starting each phase:

- For shared facts and the `paper_state` schema, load `references/paper_state_protocol.md`.
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

1. Classify the request and decide whether multi-agent coordination is justified.
2. Build or update `paper_state`.
3. Audit inputs and mark missing facts as `TODO`.
4. Settle the paper spine and create section cards when section-level work is needed.
5. Assign narrow roles or staged passes using the handoff template.
6. Use controller-mediated cross-agent loops when a section needs table/figure, argument-logic, literature, diction, or empirical review.
7. Route each substantive pass to the relevant child skill.
8. Integrate outputs against `paper_state`, not against memory.
9. Run conflict checks, drop checks, and final consistency checks.
10. Return a concise result plus unresolved `TODO` items.

## Output Check

Before finalizing, confirm:

- the stable workflow and existing child skills were not modified as part of this beta workflow;
- every delegated or staged pass used `paper_state` as the authority;
- every section agent worked from a controller-approved section card when section-level drafting was used;
- every section-functional collaboration went through the controller and updated the section card when needed;
- disagreements were resolved explicitly or left as user-facing `TODO`;
- table/figure decisions were integrated into the argument spine;
- prose edits did not delete central contributions, mechanisms, magnitudes, caveats, or design features;
- no fabricated data, citations, results, or policy implications entered the output.
