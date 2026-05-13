# Corpus-Informed Palette Templates

These templates summarize reusable visual patterns from economics-paper figures and tables without naming or indexing individual source papers. Use them as starting points for table/figure style decisions, not as mechanical copies of any article's exact colors.

## How To Use

- Match the template to the figure function first: treatment-control, event study, map, distribution, or descriptive trend.
- Prefer print-safe variants when a palette is very light or too close in grayscale.
- Do not use color in tables except light panel shading when the journal template already supports it.
- If the evidence is not visual enough to support the story, move the figure to appendix or remove it.

## Reusable Base Palettes

| Template | Main Colors | Best Use | Avoid |
| --- | --- | --- | --- |
| Table-first monochrome | `#222222`, `#666666`, `#bdbdbd` | Regression tables, descriptive tables, appendix tables | Encoding substantive groups by fill color |
| Single-accent economics | `#1f4e79`, `#8f8f8f`, `#d9eaf7` | One focal estimate, one treatment line, simple trend | More than two substantive groups |
| Treatment-control | `#1f4e79`, `#b45f06`, `#777777`, `#d9d9d9` | DID trends, event study, treatment vs control | Red-green pairings |
| Sequential map | `#f7fbff`, `#c6dbef`, `#6baed6`, `#2171b5`, `#08306b` | Choropleth maps and spatial intensity | Categorical groups |
| Diverging map/effect | `#b2182b`, `#f7f7f7`, `#2166ac` | Positive/negative effects around zero | Variables without meaningful midpoint |

## Template Selection

| Figure Or Table Need | Recommended Template | Caution |
| --- | --- | --- |
| Main regression table | Table-first monochrome | No colored coefficient cells |
| Descriptive or balance table | Table-first monochrome | Use panels instead of shading to organize groups |
| One focal estimate over time | Single-accent economics | Keep comparison series gray or dashed |
| Treatment-control trend | Treatment-control | Use line type or marker shape in addition to color |
| Event-study coefficients | Treatment-control with neutral intervals | Keep zero line and event line visible |
| Spatial intensity map | Sequential map | Make bins ordered and legible in grayscale |
| Positive versus negative effects | Diverging map/effect | Use only when zero is meaningful |
| Mechanism diagram | Single-accent economics | One accent channel only; avoid presentation-slide flowcharts |
| Multiple subgroup lines | Single-accent plus grayscale variants | Do not rely on near-identical pastels |

## Check

A palette is acceptable only if the same result remains legible when printed in grayscale, viewed on a projector, and pasted into Word/PDF without changing font or line weight.
