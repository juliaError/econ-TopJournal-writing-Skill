# Three-Line Tables

## Rule

Use three-line tables as the default for economics papers in both English and Chinese. In LaTeX this means `booktabs`; in Word this means real table borders, not only a style name.

## Required Structure

- Top rule above the header.
- Mid rule below the header.
- Bottom rule after the final statistics block.
- No vertical rules, full grid, background shading, or decorative fills.
- Coefficients and parenthesized standard errors appear on adjacent rows.
- Numeric columns are right-aligned and preferably decimal-aligned.

## What To Avoid

- Raw `esttab`, `outreg2`, spreadsheet, or markdown tables in the final paper.
- `.082` without leading zero; use `0.082`.
- Standalone p-value rows in main-text tables unless substantively necessary.
- Tiny font or aggressive `resizebox` as the first solution to a wide table.

## Language Mode

- English table titles use `Table 1. Main Estimates`.
- Chinese table titles use `表1 基准回归结果`.
- English notes use `Notes:`.
- Chinese notes use `注：`.

## Check

A reader should understand the dependent variable, focal coefficient, sample, controls/fixed effects, standard error convention, and significance notation without opening the code.
