---
purpose: "Explain how to use the paper_skills modular economics writing workflow."
applies_to: "Human and AI users applying the paper_skills rule system."
last_updated: "2026-05-12"
used_by: "paper_skills"
---

# Paper Skills

`paper_skills/` is a modular rule system for economics journal writing. Each file should contain one compact, actionable rule set. Load only the files relevant to the current writing task.

## Use Order

1. Read `00_project_brief.md` first to understand the paper, target audience, contribution, data/model, and current workflow.
2. Read the section-specific rule file for the task: abstract, introduction, literature, theory, empirical section, tables and figures, robustness, formatting, or revision.
3. Read `02_house_style_english.md` when writing or revising English prose.
4. Read `12_forbidden_phrases.md` during prose polishing and final cleanup.
5. Read files in `13_journal_specific/` only when targeting that journal.
6. Check `CONFLICTS.md` before applying rules if multiple files are relevant.

## File Map

- `00_project_brief.md`: project objective, target journal, central contribution, paper type, workflow state.
- `02_house_style_english.md`: English prose style and house conventions.
- `03_abstract_rules.md`: abstract structure and revision rules.
- `04_introduction_rules.md`: introduction structure, hook, contribution, and results preview.
- `05_related_literature_rules.md`: literature positioning and contribution mapping.
- `06_theory_section_rules.md`: model, assumptions, propositions, intuition, and predictions.
- `07_empirical_section_rules.md`: data, identification, estimation, results, and interpretation.
- `08_tables_figures_rules.md`: table and figure admission, design, notes, and presentation.
- `09_robustness_appendix_rules.md`: robustness design, appendix organization, and audits.
- `10_latex_word_format_rules.md`: LaTeX and Word manuscript formatting.
- `11_revision_linter.md`: manuscript-level revision checks.
- `12_forbidden_phrases.md`: discouraged phrases and preferred replacements.
- `13_journal_specific/jde.md`: Journal of Development Economics guidance.
- `13_journal_specific/research_policy.md`: Research Policy guidance.
- `CONFLICTS.md`: conflict log for incompatible rules.
- `TODO.md`: maintenance list for weak or incomplete files.
- `CHANGELOG.md`: concise record of low-risk maintenance edits.

## Metadata Convention

Every file begins with a YAML-like metadata block:

```yaml
---
purpose: "What this file is for."
applies_to: "When to load this file."
last_updated: "YYYY-MM-DD"
used_by: "paper_skills"
---
```

When updating a file, keep the metadata block at the top and update `last_updated`.

## Heading Convention

Use one H1 heading per file, matching the file's role. Use sentence-style H2/H3 headings inside the file. Do not bury executable rules under decorative headings.

## Conflict Handling

Do not silently resolve contradictions between files. If two files prescribe incompatible behavior, record the issue in `CONFLICTS.md` with:

- files involved
- conflicting rules
- why the conflict matters
- recommended resolution, if clear
- status: open or resolved

## Pending Content

The rule bodies are placeholders until the user provides the Markdown contents. Once content is provided, save it under the metadata block, normalize headings, and record any contradictions in `CONFLICTS.md`.
