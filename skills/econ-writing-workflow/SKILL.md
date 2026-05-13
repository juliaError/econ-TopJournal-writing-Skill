---
name: econ-writing-workflow
description: Use as the main entry point for economics writing workflows in English or Chinese, including paper planning, full paper drafting from research questions and result packages, abstract/introduction/results revision, Chinese top-journal adaptation, English and Chinese diction cleanup, AI/translationese removal, table and figure design, notes/captions, formatting checks, and routing to empirical workflow support when data cleaning, regressions, or variable construction are involved.
---

# Economics Writing Workflow

## Role

Use this skill as the user's main entry point for economics writing work. It does not replace the specialized skills; it routes the task to the right writing module, keeps the workflow ordered, and checks that the final output matches the user's target.

This skill is not a full empirical pipeline. For data cleaning, variable construction, regression code, estimation, diagnostics, or reproducibility tasks, pair with `empirical-econ-workflow`.

## First Decision

Before writing or editing, classify the request:

1. **English paper prose**: abstract, introduction, literature review, model/theory prose, empirical/results prose, conclusion, referee response, or English revision.
2. **English diction cleanup**: remove AI-like prose, translationese, vague contribution language, weak verbs, or template signposting.
3. **Argument logic**: full-paper logic, argument spine, repeated material, misplaced sections, emphasis, ordering, or whether tables and figures serve the main line.
4. **Full-paper drafting from a result package**: draft a complete paper from a research question, regression tables, figures, result folders, slides, variable notes, or design notes.
5. **Chinese top-journal writing**: Chinese paper structure, Chinese abstract, introduction, contribution framing, journal fit, submission style, or top-journal revision.
6. **Chinese diction cleanup**: remove AI 腔, 翻译腔, 作者备忘腔, unnatural collocations, or stiff Chinese academic prose.
7. **Tables and figures**: table/figure admission, main-text versus appendix placement, three-line tables, regression/robustness/heterogeneity/mechanism tables, notes, captions, palettes, fonts, or export quality.
8. **Empirical workflow**: data cleaning, variable construction, sample construction, regression code, estimation, diagnostics, or reproducibility.

If a request spans more than one category, handle them in this order:

1. empirical workflow and sample/design facts;
2. table and figure design;
3. paper structure and section logic;
4. full-paper drafting plan;
5. prose and diction cleanup;
6. final formatting/export checks.

## Routing

- For English paper prose, use `econ-write`.
- For English diction cleanup, use `econ-write` and load `references/english-diction/` selectively.
- For full-paper logic, repeated material, emphasis, section ordering, and argument-spine audits, load `references/argument-logic/` selectively before polishing prose.
- For full-paper drafting from research questions, regression tables, figures, or result folders, load `references/full-paper-drafting/` first, then route table/figure decisions to `econ-table-figure-design` and language-specific prose to `econ-write` or `cn-top-econ-writing`.
- For Chinese top-journal writing, use `cn-top-econ-writing`.
- For Chinese diction cleanup, use `cn-top-econ-writing` and load `references/chinese-diction/` selectively.
- For tables, figures, notes, captions, palettes, typography, and export checks, use `econ-table-figure-design`.
- For data cleaning, regression code, variable construction, or estimation, pair with `empirical-econ-workflow`. Do not let this writing workflow invent or run empirical results by itself.

## Operating Rules

- Read available manuscript context before giving paper-level prose advice. If only an excerpt is available, state that the advice is excerpt-level.
- Do not rewrite tables or figures as prose problems. Table selection, sample comparability, notes, and visual design are part of the research presentation.
- Do not put author workflow notes in paper-facing text, table notes, or figure notes.
- Do not merge all specialized rules into the response. Load only the relevant child skill or reference files needed for the task.
- Preserve the user's language target: English manuscript tasks should output English unless asked otherwise; Chinese top-journal tasks should output Chinese unless asked otherwise.
- For full draft requests, never invent citations, data, variable definitions, identification claims, coefficient values, mechanisms, robustness results, or policy implications. Mark missing facts as concrete `TODO` items.
- Do not provide full manuscript drafting for paid paper-writing services, undisclosed ghostwriting, fabricated research, or academic misconduct. Offer an ethical outline, checklist, or teaching-oriented alternative instead.

## Argument-Logic References

Load only the relevant files:

- `references/argument-logic/01_argument_spine.md`: one-chain paper logic and missing-link audit.
- `references/argument-logic/02_redundancy_linter.md`: repeated, appendix, and delete/merge material.
- `references/argument-logic/03_emphasis_and_ordering.md`: what to foreground, delay, or de-emphasize.
- `references/argument-logic/04_table_figure_logic.md`: whether tables and figures serve the main line.
- `references/argument-logic/05_revision_workflow.md`: full-paper logic revision workflow.

## Full-Paper Drafting References

Load only the relevant files:

- `references/full-paper-drafting/01_input_checklist.md`: input audit and draftability levels.
- `references/full-paper-drafting/02_from_results_to_outline.md`: result ledger, argument spine, and table/figure placement logic.
- `references/full-paper-drafting/03_section_drafting_order.md`: section order and language-specific routing.
- `references/full-paper-drafting/04_missing_information_policy.md`: anti-fabrication rules and `TODO` format.
- `references/full-paper-drafting/05_full_draft_workflow.md`: full result-package-to-paper workflow.

## Output Check

Before finalizing a response, confirm that:

- the routed skill matches the user's task;
- any table/figure decision has main-text versus appendix placement;
- any empirical claim is grounded in provided or inspected evidence;
- any full-draft output has an input audit, argument spine, table/figure placement plan, and unresolved `TODO` list when needed;
- any prose revision removes vague, inflated, AI-like, or translation-like wording;
- any remaining uncertainty is stated as a concrete limitation or next step.
