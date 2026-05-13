# Full Draft Workflow

Use this file when the user asks for a complete paper draft from a result package.

## Workflow

1. **Ethical check**: confirm the request is for the user's own legitimate research, teaching, revision, or noncommercial academic support.
2. **Input audit**: apply `01_input_checklist.md` and assign green, yellow, or red draftability.
3. **Evidence ledger**: apply `02_from_results_to_outline.md` to summarize tables and figures without overstating them.
4. **Table and figure design**: use `econ-table-figure-design` for main-text placement, appendix placement, notes, captions, and visual consistency.
5. **Argument spine**: use `references/argument-logic/` to remove repeated material and order the paper around the central chain.
6. **Section drafting**: apply `03_section_drafting_order.md` and route prose through the relevant English or Chinese writing skill.
7. **Missing information pass**: apply `04_missing_information_policy.md` and replace unsupported claims with concrete `TODO` markers.
8. **Diction and linter pass**: use the relevant English or Chinese diction module to remove AI-like prose, translationese, inflated contribution language, and author-memo language.
9. **Final package**: return the draft, a table/figure placement plan, and a `TODO` list.

## One-Sentence Prompt Handling

If the user gives a short request such as "use these tables and my research question to write the paper," do not stop at a generic question. First inspect available files or pasted material, then produce an input audit. If enough information exists, draft. If not, produce a structured outline and the smallest concrete missing-information list.

## Final Output Structure

For full draft tasks, return:

```text
1. Input audit
2. Argument spine
3. Table and figure placement plan
4. Full draft or section draft
5. TODO list
6. Verification notes
```

The draft may be incomplete, but it must be honest: no fabricated data, citations, estimates, or mechanisms.

## Quality Bar

A successful full draft:

- reads as a paper, not as a work log;
- keeps the central question visible throughout;
- discusses only results supported by the provided tables, figures, or notes;
- marks missing facts with precise `TODO` items;
- separates main findings from robustness, heterogeneity, and mechanism evidence;
- uses language appropriate to the target language and journal style;
- leaves the author responsible for verification, citations, disclosure, and final submission choices.
