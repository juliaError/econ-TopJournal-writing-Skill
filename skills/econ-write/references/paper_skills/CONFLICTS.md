---
purpose: "Record contradictions found across paper_skills rules without silently resolving them."
applies_to: "All paper_skills rule integration and revision passes."
last_updated: "2026-05-12"
used_by: "paper_skills"
---

# Conflicts

## Audit Date

2026-05-12

## Scope

Reviewed all Markdown files under `paper_skills/`, including `13_journal_specific/`.

## Confirmed Conflicts

No confirmed substantive contradictions were found.

Reason: the section-specific rule files are still placeholders and contain no substantive rules beyond metadata, H1 headings, and file-specific pending-content notes.

## Potential Conflict Areas To Recheck After Content Is Added

- `03_abstract_rules.md` vs. `04_introduction_rules.md`: ensure both agree on when results, contribution, and methods should be stated.
- `04_introduction_rules.md` vs. `05_related_literature_rules.md`: ensure literature review placement is consistent.
- `07_empirical_section_rules.md` vs. `08_tables_figures_rules.md`: ensure table admission, coefficient reporting, sample notes, and interpretation rules agree.
- `07_empirical_section_rules.md` vs. `09_robustness_appendix_rules.md`: ensure robustness checks are not both required in main text and relegated to appendix under incompatible criteria.
- `10_latex_word_format_rules.md` vs. `08_tables_figures_rules.md`: ensure table/figure formatting conventions agree.
- `11_revision_linter.md` vs. all rule files: ensure the linter checks the same rule set rather than introducing stricter or conflicting requirements.
- `13_journal_specific/jde.md` and `13_journal_specific/research_policy.md` vs. general rules: ensure journal-specific exceptions are explicit and do not silently override general workflow rules.

## Structural Findings That Are Not Conflicts

- `11_revision_linter.md` does not yet reference the other rule files. This is incomplete, but not a contradiction.
- No duplicated substantive guidance was found. The previous repeated placeholder sentence has been replaced with file-specific pending-content notes.
- No file currently encourages formulaic AI-style prose; however, this cannot be fully assessed until rule bodies are added.
