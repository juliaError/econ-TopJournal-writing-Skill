# Paper State Protocol

## Purpose

Use `paper_state` as the single source of truth for a large economics writing project. Every agent or staged role must read it before working and must report any proposed change to it.

## When To Create

Create or update `paper_state` when the task involves:

- a full paper draft;
- many tables or figures;
- multiple sections;
- a major revision;
- bilingual writing;
- referee comments;
- long context that may exceed what one agent can reliably track.

For small polishing tasks, do not create a full paper state unless the user asks.

## Required Fields

```text
project_title:
target_language:
target_journal_or_style:
research_question:
main_contribution:
secondary_contributions:
theory_or_mechanism:
data_sources:
sample_scope:
period:
unit_of_observation:
key_variables:
identification_or_model:
main_tables:
main_figures:
main_results_and_magnitudes:
mechanism_results:
heterogeneity_results:
robustness_results:
literature_positioning:
scope_conditions_and_caveats:
cannot_invent:
open_todos:
last_updated_by:
```

## Authority Rules

- If `paper_state` conflicts with a draft paragraph, table note, or agent output, pause and flag the conflict.
- If an agent infers a fact from supplied materials, label it as `inferred` until confirmed.
- If a needed fact is missing, write a concrete `TODO` rather than smoothing over the gap.
- If user instructions update the paper facts, update `paper_state` before editing prose.
- Do not use `paper_state` to store long source excerpts, paper PDFs, or copyrighted text.

## Minimal Paper State

If inputs are sparse, use this reduced form:

```text
research_question:
main_contribution:
data_or_model:
main_results:
mechanism:
tables_figures_available:
missing_information:
do_not_invent:
```
