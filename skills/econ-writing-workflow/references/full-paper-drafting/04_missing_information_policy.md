# Missing Information Policy

Use this file whenever a full draft request lacks information needed for credible academic prose.

## Never Invent

Do not invent:

- citations, author names, journal names, or literature claims;
- literature-based data, theory, variable, mechanism, classification, specification, or policy judgments that have not been inspected in the relevant source or confirmed by the user;
- data sources, sample windows, sample restrictions, or observation counts;
- variable definitions, transformations, or units;
- identifying assumptions, instruments, discontinuities, shocks, or treatment timing;
- coefficient signs, magnitudes, standard errors, significance, or robustness results;
- mechanism evidence, heterogeneity patterns, or placebo outcomes;
- policy implications that do not follow from the evidence;
- journal-specific requirements not provided or inspected.

## TODO Format

Use concrete markers:

```text
TODO[data]: Add the sample window and unit of observation.
TODO[variable]: Define the treatment variable and its unit.
TODO[result]: Insert the coefficient, standard error, and economic magnitude from Table X.
TODO[literature]: Add verified citations for the closest papers on this mechanism.
TODO[judgment]: Confirm whether reference papers support using X as the mechanism/variable/specification.
TODO[identification]: State the identifying assumption and the main threat.
```

Each `TODO` must name the missing object and where it affects the draft.

## Allowed Provisional Language

Use provisional wording only when it is visibly conditional:

- "The draft can state this claim after the author verifies ..."
- "This paragraph assumes the table shows ..."
- "If the identifying variation is ..., the empirical strategy section should ..."

Do not convert provisional notes into paper-facing claims.

## Ethical Boundary

If the request appears to be paid ghostwriting, undisclosed authorship, fabricated evidence, or evasion of journal or university rules, do not provide a full manuscript. Offer an ethical alternative such as an outline, revision checklist, or teaching-oriented explanation.

## Insufficient Inputs

When key inputs are missing, produce:

1. what can be drafted now;
2. what must remain as `TODO`;
3. what cannot be drafted responsibly;
4. the smallest set of additional files or facts needed to proceed.
