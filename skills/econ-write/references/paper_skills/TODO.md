---
purpose: "List weak, incomplete, or non-actionable parts of paper_skills found during review."
applies_to: "paper_skills maintenance, rule completion, and future content integration."
last_updated: "2026-05-13"
used_by: "paper_skills"
---

# To Do

## Critical

- Fill the rule bodies for the remaining placeholder files. Current placeholder content is not usable for Codex beyond routing and file discovery.
- Extend `11_revision_linter.md` after the remaining substantive files are filled so it explicitly checks the applicable rules from:
  - `00_project_brief.md`
  - `02_house_style_english.md`
  - `05_related_literature_rules.md`
  - `06_theory_section_rules.md`
  - `07_empirical_section_rules.md`
  - `08_tables_figures_rules.md`
  - `09_robustness_appendix_rules.md`
  - `10_latex_word_format_rules.md`
  - `12_forbidden_phrases.md`
  - `13_journal_specific/jde.md`
  - `13_journal_specific/research_policy.md`

## Weak or Incomplete Files

- `00_project_brief.md`: missing actual project brief fields such as paper type, target journal, central contribution, evidence/model, audience, current draft state, and open decisions.
- `02_house_style_english.md`: missing enforceable English style rules and examples.
- `03_abstract_rules.md`: now contains contribution-preserving abstract rules; later expansion could add journal-specific variants and more examples.
- `04_introduction_rules.md`: now contains contribution-preserving introduction rules; later expansion could add more field-specific opening patterns.
- `05_related_literature_rules.md`: missing citation grouping, contribution positioning, and avoid-list rules.
- `06_theory_section_rules.md`: missing model setup, assumptions, propositions, intuition, proof placement, and prediction mapping rules.
- `07_empirical_section_rules.md`: missing data, identification, estimation, sample audit, coefficient interpretation, and causal language rules.
- `08_tables_figures_rules.md`: missing table/figure admission criteria, notes, labels, column structure, and caption rules.
- `09_robustness_appendix_rules.md`: missing robustness hierarchy, appendix organization, and specification audit rules.
- `10_latex_word_format_rules.md`: missing LaTeX/Word formatting standards, table formatting rules, citation style, and export checks.
- `11_revision_linter.md`: now contains contribution-preservation checks; later expansion should connect to remaining substantive files after their bodies are filled.
- `12_forbidden_phrases.md`: missing phrase list, rationale, and preferred replacements.
- `13_journal_specific/jde.md`: missing JDE-specific framing, evidence, and robustness expectations.
- `13_journal_specific/research_policy.md`: missing Research Policy-specific innovation framing, contribution style, and evidence expectations.

## Duplicated Content

- No duplicated substantive rule content is currently present. The former repeated placeholder sentence has been replaced with file-specific pending-content notes.

## Cross-Reference Gaps

- `README.md` references all expected files and the references are consistent with file names.
- `11_revision_linter.md` now references the active abstract and introduction rules. It should be extended after the remaining placeholder files are filled.
- After rule bodies are added, all internal references should use exact file names, including the `13_journal_specific/` prefix for journal files.

## Vagueness Risks

- Remaining placeholder files are too vague for Codex to apply because they contain no executable rules, examples, checks, or decision criteria.
- When filling files, each rule should specify: applicable scenario, action rule, positive example or template, negative pattern, and check standard.

## Formulaic AI-Style Prose Risks

- The new abstract and introduction rules use paper-type templates, but they explicitly require contribution diagnosis, concrete magnitudes, and a drop check to avoid boilerplate.
- When content is added, watch for rules that overuse fixed paragraph formulas, generic transition sentences, or reusable boilerplate that could make papers sound templated.

## Metadata Check

- Every Markdown file currently has `purpose` and `applies_to`.
- The fields are clear enough for routing, but many files still need body content to make those fields operational.
