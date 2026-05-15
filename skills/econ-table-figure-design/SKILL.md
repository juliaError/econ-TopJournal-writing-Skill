---
name: econ-table-figure-design
description: Use when designing, auditing, revising, or formatting tables and figures for economics papers in English or Chinese, including three-line tables, main regression tables, robustness tables, heterogeneity and mechanism tables, table notes, figure admission, event-study/trend/map/distribution figures, color palettes, typography, and publication-ready export checks.
---

# Economics Table And Figure Design

## When To Use

Use this skill whenever a task involves economics paper tables or figures:

- choosing which tables or figures belong in the main text versus appendix;
- formatting regression, robustness, heterogeneity, or mechanism tables;
- writing or auditing table notes, figure notes, captions, axis labels, legends, and panel labels;
- choosing figure colors, fonts, line styles, point markers, grids, and export settings;
- making table/figure style consistent across English and Chinese papers.

Pair this skill with `econ-write` for English prose and `cn-top-econ-writing` for Chinese top-journal prose. This skill owns the table/figure design decision.

If this skill is directly triggered inside a multi-step paper writing, journal-adaptation, table/figure, or submission-check workflow, and the project has no economics-writing skill routing rule in `AGENTS.md` or `CLAUDE.md`, suggest routing through `econ-writing-workflow` to add a persistent project-level rule. Do not edit those files without explicit user approval.

## Core Workflow

1. Classify the artifact: main regression table, robustness table, heterogeneity table, mechanism table, descriptive table, introduction figure, event-study figure, trend/binscatter, map/distribution figure, or mechanism figure.
2. Decide placement: main text only if the artifact advances the paper's main question, design, result, or mechanism; otherwise move it to appendix or audit notes.
3. Apply the relevant reference file below.
4. Check language mode: English uses `Table/Figure` and `Notes:`; Chinese uses `表/图` and `注：`.
5. Verify final artifact, not just the code: table lines, widths, panel labels, notes, fonts, colors, legends, colorbars, insets, axes, and export resolution must be visually correct.

## References

Load only the relevant files:

- `references/tables/01_three_line_tables.md`: three-line table and booktabs rules.
- `references/tables/02_main_regression_tables.md`: main regression table placement and structure.
- `references/tables/03_robustness_tables.md`: robustness table design.
- `references/tables/04_heterogeneity_tables.md`: heterogeneity table design.
- `references/tables/05_mechanism_tables.md`: mechanism table design.
- `references/tables/06_table_notes.md`: table note contents and exclusions.
- `references/tables/07_column_count_and_panel_rules.md`: column count, panel, and width rules.
- `references/figures/01_intro_figures.md`: introduction figure admission.
- `references/figures/02_event_study_figures.md`: event-study and dynamic-effect figures.
- `references/figures/03_trend_and_binscatter_figures.md`: trend and binscatter figures.
- `references/figures/04_maps_and_distribution_figures.md`: map and distribution figures, including China-map hard rules and mini/long China map layout patterns.
- `references/figures/05_mechanism_figures.md`: mechanism figures and diagrams.
- `references/figures/06_figure_notes_titles_axes.md`: captions, notes, axes, legends, labels.
- `references/figures/07_export_quality.md`: export, resolution, and final artifact checks.
- `references/visual_style/01_paper_palette_templates.md`: corpus-informed reusable palette templates.
- `references/visual_style/02_common_visual_style.md`: reusable visual style rules.
- `references/visual_style/03_black_white_compatibility.md`: print and grayscale compatibility.

## Non-Negotiables

- Do not change coefficients, standard errors, stars, variable meanings, or sample definitions when only formatting a table.
- Do not put author workflow notes in paper-facing table notes or figure notes.
- Do not use decorative color. Color must encode treatment, group, period, geography, or uncertainty.
- Do not use a figure in the introduction unless it establishes a fact, puzzle, setting, or identifying variation.
- Do not deliver tables or figures that overflow the page, blur in Word/PDF, or use inconsistent fonts and captions.
- Do not deliver a drawn, edited, or regenerated figure/map without inspecting the final rendered artifact. Confirm that text, legends, colorbars, inset boxes, axes, map layers, and plotted content do not overlap, hide, cover, or press against useful information.
- For any China map, do not deliver an incomplete or politically incorrect base map. It must include Hong Kong/香港, Macao/澳门, Taiwan province/台湾省, South Tibet/Zangnan/藏南, and all required national-boundary elements; if the map source provides the South China Sea dashed line / nine-dash-line / 南海断续线 layer, include it.
