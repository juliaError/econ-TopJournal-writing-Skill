# English Diction Source Coverage

## Principle

This file records the source coverage behind `english-diction`. Use it to avoid treating one paper's style as a universal rule. Public skill files include abstracted rules and original examples only; they do not store long source text.

## Audit Status

- Use when: checking whether an English prose rule is broadly supported.
- Recommended: rely on rules supported by several readable theory and empirical papers.
- Avoid: copying source sentences or treating restricted/mis-extracted PDFs as sentence-level evidence.
- Check: source coverage should distinguish included, downgraded, and missing papers.

Automatic audit result:

| Category | Count | Notes |
| --- | ---: | --- |
| Planned English papers | 20 | E01-E20 in the corpus list |
| Included sources | 16 | readable extraction, used for function-level distillation |
| Downgraded sources | 3 | E06, E07, E12 extraction quality too weak for core sentence rules |
| Missing/restricted sources | 1 | E03 main article not available as open local PDF |

## Included Sources

Theory and model prose: E01, E02, E04, E05, E08, E09, E10.

Empirical and measurement prose: E11, E13, E14, E15, E16, E17, E18, E19, E20.

## Downgraded And Missing Sources

E06 and E07 are classic theory sources, but the local PDFs do not provide usable extracted text for automatic sentence-level distillation. They should remain in the corpus list but should not support specific diction rules until manually reviewed.

E12 is substantively important, but the local extraction contains heavy encoding noise. It should not support core sentence-level rules unless a cleaner text source is supplied.

E03 has a public AEA article page and DOI metadata, but the main article requires member or institutional access. Metadata pages from Princeton and LSE do not provide full text, and the AEA web appendix is not a substitute for the article.

## Function Coverage

| Function | Main Supporting Sources | Use |
| --- | --- | --- |
| Research question and setup | E19, E20, E01, E14, E15, E10 | abstract openings, introduction question paragraphs |
| Model setup | E04, E01, E08, E09, E20, E10 | theory environments, players, timing, information |
| Assumption and equilibrium | E01, E05, E09, E10, E02, E13 | assumptions, equilibrium definitions, propositions |
| Mechanism and intuition | E01, E19, E08, E04, E18, E20 | intuition paragraphs and mechanism interpretation |
| Identification and variation | E20, E19, E13, E18, E17, E16 | empirical strategy and design summaries |
| Data and measurement | E19, E20, E18, E14, E13, E17 | data sections and constructed variables |
| Results and magnitude | E19, E13, E18, E11, E16, E14 | table discussion and abstract findings |
| Literature and contribution | E01, E19, E18, E13, E20, E10 | contribution paragraphs and related literature |
| Limitation and scope | E19, E16, E13, E01, E10, E02 | external validity, caveats, interpretation boundaries |
| Table and figure narration | E19, E13, E14, E18, E16, E17 | table notes, figure discussion, appendix references |

## Use Check

Before applying a rule, ask:

1. Is this a theory sentence, empirical sentence, or general prose sentence?
2. Does the rule come from multiple included sources?
3. Is the rewrite an original sentence rather than source imitation?
4. Does the final sentence make a narrower, clearer, and more credible claim?
