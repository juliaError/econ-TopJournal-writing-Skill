# Literature And Judgment Grounding

Use this file before drafting or revising material that depends on prior literature, including introductions, literature reviews, theory and mechanism sections, variable definitions, data descriptions, identification choices, heterogeneity choices, robustness choices, contribution claims, and policy implications.

The goal is not to add citations after the prose is written. The goal is to make local literature materials discipline the paper's substantive judgments before and during writing.

## 1. Start With A Literature Grounding Check

Before drafting or revising a paper-level claim, check whether the project already has local literature materials:

- folders such as `references/`, `literature/`, `papers/`, `sources/`, `文献/`, `参考文献/`;
- PDFs, extracted text files, notes, Zotero/Mendeley exports, `.bib` files, or source ledgers;
- target-journal sample papers that the user has explicitly provided as style examples.

Then ask the user, when the answer is not obvious:

- whether the available literature is sufficient for the current writing task;
- whether the agent should help search for publicly available papers or working papers;
- whether missing Chinese papers should be left as user-supplied items.

If a Chinese paper, database-licensed paper, or paywalled source cannot be obtained locally, tell the user plainly. It is acceptable to continue without it, but the affected literature positioning, theory, mechanism, variable alignment, or citation judgment must remain more author-supervised and should carry a concrete `TODO` when needed.

## 2. Build A Source Ledger Before Writing From Literature

When literature files are available, do not rely on memory, titles, abstracts alone, or generic field knowledge. First create or update a compact source ledger from the local documents. For each important paper, record:

- bibliographic identity: author, year, title, journal/working-paper status when available;
- research question and setting;
- data source, sample, unit, time window, and key measurement choices;
- theoretical object, mechanism, or conceptual framework;
- variable definitions and proxies that may be reused or adapted;
- identification strategy or model structure;
- central findings and limits;
- how the paper is similar to, different from, or useful for the user's paper;
- claims the current paper may use, and claims it must not over-extend.

Keep the ledger concise. It should support writing decisions; it is not a full paper summary.

## 3. Add A Judgment Ledger

For similar or important judgments, create a separate judgment ledger. A judgment is any decision that shapes what the paper may responsibly claim, not just a citation slot.

Track at least these judgment types when relevant:

- research positioning and contribution boundary;
- theory or mechanism selection;
- data source and measurement alignment;
- variable name, proxy, construction, and unit;
- control variables, fixed effects, clustering, sample restrictions, or model specification;
- heterogeneity, robustness, placebo, or mechanism-test selection;
- main-text versus appendix placement;
- result strength, caveats, and policy implications.

Use this compact format:

```text
Judgment type:
Current paper decision:
Relevant sources:
What the sources support:
Alignment required:
Support strength: strong / moderate / weak
Allowed manuscript use:
Do not claim:
Need user confirmation:
```

## 4. Align Before Reusing Literature Objects

If the paper uses data, theory, variables, mechanisms, classifications, institutional facts, model objects, or empirical choices that come from or closely resemble the reference literature, read the relevant source passage before writing. Then align the manuscript with the literature as far as the user's design allows.

Alignment means:

- use the same concept name when the same concept is meant;
- explain any renamed or adapted variable instead of silently changing it;
- preserve the source's unit, sample, time window, and construction logic when they are part of the claim;
- distinguish a literature concept from the user's measurable proxy;
- state when the user's paper extends the source to a new setting, mechanism, data object, or identification design;
- avoid inventing a new theoretical label, variable interpretation, or mechanism when a local reference already provides the relevant wording or boundary.

If the user's paper intentionally departs from the literature, say so as a design choice in author-facing notes or reader-facing prose when needed. Do not hide the departure by writing as if the concepts are identical.

## 5. Use Literature To Calibrate Claim Strength

Use the source and judgment ledgers to avoid both over-conservatism and over-claiming:

- If multiple close sources support a mechanism or variable choice, do not weaken every sentence into `may`, `might`, or `to some extent`.
- If the sources only motivate a hypothesis or interpretation, do not write that the current paper proves the mechanism.
- If the sources use a variable as a proxy, do not call it the underlying concept without explaining the proxy relationship.
- If the sources study a different population, period, country, institution, or level of aggregation, mark the boundary before using the claim.
- If the sources disagree, present the tension rather than choosing one side silently.

## 6. Write With Source-Grounded Retrieval

During drafting, follow this loop:

1. Identify the paragraph's function: literature position, theory, mechanism, data, variables, identification, results interpretation, robustness, heterogeneity, or policy implication.
2. Search the source ledger and judgment ledger for that function.
3. If the ledger is enough, draft with citations and boundaries.
4. If the ledger is not enough, inspect the relevant PDF/text passage before writing.
5. If the source is missing, ask the user or insert a concrete `TODO[literature]`, `TODO[variable]`, `TODO[mechanism]`, or `TODO[identification]`.

Never fill the gap with invented author-year citations, guessed findings, generic field claims, or unsupported "common sense" mechanisms.

## 7. Final Literature-Grounding Audit

Before finalizing literature-dependent text, check:

- every cited paper appears in the source ledger or was otherwise inspected;
- every data, theory, variable, mechanism, specification, or policy judgment borrowed from literature is aligned with the relevant source;
- every contribution claim is relative to concrete literature, not a vague `现有研究较少`;
- every strong claim has adequate support strength;
- every unsupported or unavailable source is marked with a concrete TODO or user question;
- no author-facing source notes, extraction notes, or judgment labels entered the manuscript.
