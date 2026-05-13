---
purpose: "Record contradictions found across paper_skills rules without silently resolving them."
applies_to: "All paper_skills rule integration and revision passes."
last_updated: "2026-05-13"
used_by: "paper_skills"
---

# Conflicts

## Audit Date

2026-05-13

## Scope

Reviewed all Markdown files under `paper_skills/`, including `13_journal_specific/`.

## Confirmed Conflicts

No confirmed substantive contradictions were found.

Reason: the newly filled abstract, introduction, and revision-linter rules all use the same standard: concise by default, but preserve central contributions, strategically important secondary contributions, mechanisms, key magnitudes, design/data features, and necessary caveats. Remaining placeholder files still contain no substantive rules that could conflict.

## Potential Conflict Areas To Recheck After Content Is Added

- `03_abstract_rules.md` vs. `04_introduction_rules.md`: currently aligned on contribution preservation; recheck when more section-specific content is added.
- `04_introduction_rules.md` vs. `05_related_literature_rules.md`: ensure literature review placement is consistent.
- `07_empirical_section_rules.md` vs. `08_tables_figures_rules.md`: ensure table admission, coefficient reporting, sample notes, and interpretation rules agree.
- `07_empirical_section_rules.md` vs. `09_robustness_appendix_rules.md`: ensure robustness checks are not both required in main text and relegated to appendix under incompatible criteria.
- `10_latex_word_format_rules.md` vs. `08_tables_figures_rules.md`: ensure table/figure formatting conventions agree.
- `11_revision_linter.md` vs. all rule files: ensure the linter checks the same rule set rather than introducing stricter or conflicting requirements.
- `13_journal_specific/jde.md` and `13_journal_specific/research_policy.md` vs. general rules: ensure journal-specific exceptions are explicit and do not silently override general workflow rules.

## Structural Findings That Are Not Conflicts

- `11_revision_linter.md` now references the active abstract and introduction rules. It still needs extension after remaining placeholder files are filled.
- No duplicated substantive guidance was found. The previous repeated placeholder sentence has been replaced with file-specific pending-content notes.
- The active abstract and introduction templates are paper-type branches rather than boilerplate paragraphs. Recheck formulaic-prose risk as more rule bodies are filled.
