# Black-White And Print Compatibility

Economics papers are often read as PDFs, printed copies, referee packets, and Word drafts. Every table and figure must survive without color.

## Required Checks

- Convert the figure to grayscale and confirm all substantive groups remain distinguishable.
- Use line type, marker shape, or direct labels in addition to color for multi-series figures.
- Avoid red-green contrasts as the only distinction.
- Make confidence intervals visible against both white and light-gray backgrounds.
- Ensure map bins remain ordered in grayscale.
- Confirm table rules, notes, and stars remain sharp after Word/PDF export.

## Figure Patterns

| Figure Type | Print-Safe Encoding |
| --- | --- |
| Treatment-control trend | Focal solid line, control dashed line, neutral gray CI |
| Event study | Point estimate markers, capped CI bars, vertical event line, horizontal zero line |
| Binscatter | Hollow or filled markers plus fitted line; no color-only grouping |
| Map | Ordered sequential bins; clear legend title; avoid too many categories |
| Distribution | Solid focal density, dashed comparison density, labels outside crowded regions |
| Mechanism diagram | Black/gray arrows, one accent only for focal channel |

## Table Patterns

- Do not rely on shading to define panels; use panel labels and horizontal rules.
- Use bold sparingly for panel headings, not for significance emphasis.
- Keep notes readable after scaling to one page.
- If a landscape table is necessary, make the orientation choice explicit in the production file rather than shrinking fonts below readability.

## Export Checks

- Prefer vector output for LaTeX/PDF workflows.
- For Word workflows, use high-resolution PNG/TIFF only when vector insertion is unstable.
- Inspect the final rendered artifact after insertion into the manuscript.
- Re-export if labels blur, lines thicken unevenly, or panel titles shift.

## Check

If a printed black-white copy cannot show which estimate, group, or period is focal, the figure is not publication-ready.
