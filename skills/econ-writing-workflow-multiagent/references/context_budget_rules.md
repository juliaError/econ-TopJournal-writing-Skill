# Context Budget Rules

## Default Decision

Do not split small tasks. Multi-agent coordination has overhead and can make short edits worse.

Use the stable workflow or a child skill directly for:

- one paragraph;
- one abstract;
- one table note;
- one figure caption;
- a short translation;
- a narrow style cleanup.

## Split Work When

Use multi-agent or staged-agent coordination when at least one is true:

- the task spans multiple paper sections;
- there are many tables or figures;
- the user asks for a full draft;
- the manuscript and result package cannot fit comfortably in one working context;
- both Chinese and English writing decisions matter;
- literature, empirical design, table/figure placement, and prose all interact;
- revision involves many referee comments or many moving parts.

## Suggested Splits

- **Full paper draft**: input audit, table/figure, argument logic, section drafting, diction, final consistency.
- **Major revision**: referee issue map, table/figure changes, argument restructuring, prose rewrite, response audit.
- **Large result package**: table/figure admission first, then argument spine, then prose.
- **Bilingual work**: settle paper facts once, then run separate language-specific diction passes.

## Keep Context Small

- Pass only the fields needed for each role.
- Summarize long tables, but preserve coefficient values, samples, notes, and caveats needed for interpretation.
- Do not pass full papers or long source excerpts to every role.
- Keep role outputs structured and short enough for the controller to integrate.

## Escalation Rule

If a role cannot answer because information is missing, it should return `Missing information` and stop at a bounded recommendation. It should not infer beyond the provided evidence.
