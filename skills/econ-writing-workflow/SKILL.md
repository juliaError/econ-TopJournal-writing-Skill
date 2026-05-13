---
name: econ-writing-workflow
description: Use as the main entry point for economics writing workflows in English or Chinese, including paper planning, abstract/introduction/results revision, Chinese top-journal adaptation, English and Chinese diction cleanup, AI/translationese removal, table and figure design, notes/captions, formatting checks, and routing to empirical workflow support when data cleaning, regressions, or variable construction are involved.
---

# Economics Writing Workflow

## Role

Use this skill as the user's main entry point for economics writing work. It does not replace the specialized skills; it routes the task to the right writing module, keeps the workflow ordered, and checks that the final output matches the user's target.

This skill is not a full empirical pipeline. For data cleaning, variable construction, regression code, estimation, diagnostics, or reproducibility tasks, pair with `empirical-econ-workflow`.

## First Decision

Before writing or editing, classify the request:

1. **English paper prose**: abstract, introduction, literature review, model/theory prose, empirical/results prose, conclusion, referee response, or English revision.
2. **English diction cleanup**: remove AI-like prose, translationese, vague contribution language, weak verbs, or template signposting.
3. **Chinese top-journal writing**: Chinese paper structure, Chinese abstract, introduction, contribution framing, journal fit, submission style, or top-journal revision.
4. **Chinese diction cleanup**: remove AI 腔, 翻译腔, 作者备忘腔, unnatural collocations, or stiff Chinese academic prose.
5. **Tables and figures**: table/figure admission, main-text versus appendix placement, three-line tables, regression/robustness/heterogeneity/mechanism tables, notes, captions, palettes, fonts, or export quality.
6. **Empirical workflow**: data cleaning, variable construction, sample construction, regression code, estimation, diagnostics, or reproducibility.

If a request spans more than one category, handle them in this order:

1. empirical workflow and sample/design facts;
2. table and figure design;
3. paper structure and section logic;
4. prose and diction cleanup;
5. final formatting/export checks.

## Routing

- For English paper prose, use `econ-write`.
- For English diction cleanup, use `econ-write` and load `references/english-diction/` selectively.
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

## Output Check

Before finalizing a response, confirm that:

- the routed skill matches the user's task;
- any table/figure decision has main-text versus appendix placement;
- any empirical claim is grounded in provided or inspected evidence;
- any prose revision removes vague, inflated, AI-like, or translation-like wording;
- any remaining uncertainty is stated as a concrete limitation or next step.
