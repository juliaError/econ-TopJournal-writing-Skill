---
name: econ-writing-workflow
description: Use as the main entry point for economics writing workflows in English or Chinese, including paper planning, full paper drafting from research questions and result packages, abstract/introduction/results revision, Chinese top-journal adaptation, English and Chinese diction cleanup, AI/translationese removal, table and figure design, notes/captions, formatting checks, and routing to empirical workflow support when data cleaning, regressions, or variable construction are involved.
---

# Economics Writing Workflow

## Role

Use this skill as the user's main entry point for economics writing work. It does not replace the specialized skills; it routes the task to the right writing module, keeps the workflow ordered, and checks that the final output matches the user's target.

This skill is not a full empirical pipeline. For data cleaning, variable construction, regression code, estimation, diagnostics, or reproducibility tasks, pair with `empirical-econ-workflow`.

## Project-Level Skill Pinning

For multi-step economics writing, table, figure, journal-submission, or paper-formatting workflows, check whether the nearest project-level `AGENTS.md` or `CLAUDE.md` already contains an economics-writing skill routing rule.

If no such rule exists, ask the user once whether to add a persistent local rule. Do not edit `AGENTS.md` or `CLAUDE.md` without explicit user approval, and do not ask for tiny one-off requests.

Recommended rule text:

```markdown
## Economics Writing Skill Routing

For economics paper writing, journal adaptation, tables, figures, captions, notes, Word/PDF formatting, and submission checks, first route through `econ-writing-workflow`.

Use `cn-top-econ-writing` for Chinese top-journal prose and journal-specific submission style. Use `econ-table-figure-design` for tables, figures, maps, captions, notes, and export quality. Use `empirical-econ-workflow` when data cleaning, variable construction, regressions, sample audits, or estimation code are involved.

Keep the relevant skill active throughout the task unless the user explicitly opts out. Do not treat skill use as a one-time setup step: at the start of each substantive phase, and whenever the work crosses from prose into tables, figures, maps, journal formatting, data facts, or empirical code, reclassify the current subtask and load the relevant specialized skill or reference file.

During manuscript drafting or revision, separate paper-facing text from author memos and task logs before writing each paragraph, table note, figure note, appendix note, or footnote. Only reader-facing manuscript text may enter the paper. Author workflow notes, submission-positioning discussion, reasons for moving/deleting material, and author-agent internal decisions must stay in the response, task README, revision memo, or checklist.

When paper facts, variable definitions, sample construction, identification choices, target-journal requirements, table/figure meanings, or the user's intended claim are unclear, ask the user or mark a concrete `TODO`. Do not guess, invent, silently choose among substantive alternatives, or write around the uncertainty as if it were known.

When producing tables, figures, maps, or edited images, verify the final rendered artifact itself before treating the task as complete. Check that text, legends, colorbars, inset maps, axes, notes, and substantive visual content do not overlap, obscure, or cover useful information.
```

After adding the rule, include a clear marker heading so future agents can detect it and avoid asking again.

## First Decision

Before writing or editing, classify the request:

1. **English paper prose**: abstract, introduction, literature review, model/theory prose, empirical/results prose, conclusion, referee response, or English revision.
2. **English diction cleanup**: remove AI-like prose, translationese, vague contribution language, weak verbs, or template signposting.
3. **Argument logic**: full-paper logic, argument spine, repeated material, misplaced sections, emphasis, ordering, or whether tables and figures serve the main line.
4. **Full-paper drafting from a result package**: draft a complete paper from a research question, regression tables, figures, result folders, slides, variable notes, or design notes.
5. **Chinese top-journal writing**: Chinese paper structure, Chinese abstract, introduction, contribution framing, journal fit, submission style, or top-journal revision.
6. **Chinese diction cleanup**: remove AI 腔, 翻译腔, 作者备忘腔, unnatural collocations, or stiff Chinese academic prose.
7. **Journal submission style**: target-journal formatting, submission requirements, anonymous PDF checks, accepted-version Word formatting, title hierarchy, references, JEL codes, appendices, or journal-specific body/appendix placement.
8. **Tables and figures**: table/figure admission, main-text versus appendix placement, three-line tables, regression/robustness/heterogeneity/mechanism tables, notes, captions, palettes, fonts, or export quality.
9. **Empirical workflow**: data cleaning, variable construction, sample construction, regression code, estimation, diagnostics, or reproducibility.

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
- For manuscript-facing versus author-facing voice, internal memo leakage, or requests to remove author workflow notes from paper prose, load `references/manuscript-voice/01_no_author_memo_in_manuscript.md` before finalizing text.
- For full-paper drafting from research questions, regression tables, figures, or result folders, load `references/full-paper-drafting/` first, then route table/figure decisions to `econ-table-figure-design` and language-specific prose to `econ-write` or `cn-top-econ-writing`.
- For Chinese top-journal writing, use `cn-top-econ-writing`.
- For target-journal submission style, anonymous manuscript checks, accepted-version formatting, references, appendices, or requests such as “按《经济学（季刊）》投稿要求调整”, use `cn-top-econ-writing` and its `references/journal-styles/` module. For 《经济学（季刊）》, load `references/journal-styles/00_journal_submission_workflow.md`, `references/journal-styles/economics_quarterly.md`, and when table/figure/appendix issues appear, `references/journal-styles/common_chinese_journal_rules.md`.
- For Chinese diction cleanup, use `cn-top-econ-writing` and load `references/chinese-diction/` selectively.
- For tables, figures, notes, captions, palettes, typography, and export checks, use `econ-table-figure-design`.
- For data cleaning, regression code, variable construction, or estimation, pair with `empirical-econ-workflow`. Do not let this writing workflow invent or run empirical results by itself.

## Active Routing During Work

Do not route only once at the beginning of a long task. At the start of each substantive phase, and whenever the work crosses from prose into tables, figures, maps, journal formatting, data facts, or empirical code, reclassify the current subtask and load the relevant specialized skill or reference file.

Route immediately when these boundaries appear:

- tables, figures, maps, image edits, captions, legends, colorbars, fonts, export quality, or main-text versus appendix placement: use `econ-table-figure-design`;
- target-journal style, anonymous submission, title hierarchy, references, JEL codes, appendices, Word/PDF submission format, or 《经济学（季刊）》 rules: use `cn-top-econ-writing` and its `references/journal-styles/` module;
- data cleaning, variable construction, regression code, estimation, sample changes, or post-estimation sample audit: pair with `empirical-econ-workflow`;
- English prose or English diction: use `econ-write`;
- Chinese top-journal prose, Chinese diction, Chinese abstract, or Chinese contribution framing: use `cn-top-econ-writing`.

After a specialized skill settles its part, return to this workflow to integrate the decision into the paper-level order and final output check.

## Operating Rules

- Read available manuscript context before giving paper-level prose advice. If only an excerpt is available, state that the advice is excerpt-level.
- Do not rewrite tables or figures as prose problems. Table selection, sample comparability, notes, and visual design are part of the research presentation.
- Do not put author workflow notes in paper-facing text, table notes, or figure notes.
- Before delivering or inserting manuscript text, classify each sentence as paper-facing text, author memo, or task log. Only paper-facing text may enter the manuscript.
- If the manuscript context is unclear on research question, variables, sample, identification, table/figure meaning, target journal, or whether the author wants to keep/delete a substantive claim, ask the user or leave a concrete `TODO`; do not guess.
- When writing main-text pointers to appendices, tables, figures, or online appendices, keep them as pure pointers: state what to see and where to see it; only when needed, name the substantive role for the current claim, such as robustness, variable construction, sample scope, background fact, or extended result. Do not write meta-language such as `this is related to the main text` or `因此与正文有关`. Do not include layout or production language such as split columns, left/right halves, column width, page breaks, continued tables, repeated headers, or appendix-table formatting in the main text; put necessary reading guidance in the appendix text, table title, or note.
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

## Manuscript-Voice References

Load when drafting, revising, polishing, or auditing prose that will enter the manuscript:

- `references/manuscript-voice/01_no_author_memo_in_manuscript.md`: separates manuscript text from author memos and task logs; includes forbidden and context-dependent author-memo patterns.

## Output Check

Before finalizing a response, confirm that:

- the routed skill still matches the current subtask, not just the original request;
- any table/figure decision has main-text versus appendix placement;
- any empirical claim is grounded in provided or inspected evidence;
- any full-draft output has an input audit, argument spine, table/figure placement plan, and unresolved `TODO` list when needed;
- any prose revision removes vague, inflated, AI-like, or translation-like wording;
- no paper-facing paragraph, table note, or figure note contains author-facing workflow notes, draft-management explanations, or internal discussion with the author;
- any remaining uncertainty is stated as a concrete limitation or next step.
