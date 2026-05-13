# Paper-Specific Palette Templates

These templates summarize audit signals from the planned English and Chinese economics-paper corpus. Use them as starting points for table/figure style decisions, not as mechanical copies of any paper's exact colors.

## How To Use

- Match the template to the figure function first: treatment-control, event study, map, distribution, or descriptive trend.
- Prefer print-safe variants when a detected palette is very light or too close in grayscale.
- Do not use color in tables except light panel shading when the journal template already supports it.
- If a source is missing or downgraded, use the default monochrome or single-accent template and record the limitation.

## Reusable Base Palettes

| Template | Main Colors | Best Use | Avoid |
| --- | --- | --- | --- |
| Table-first monochrome | `#222222`, `#666666`, `#bdbdbd` | Regression tables, descriptive tables, appendix tables | Encoding substantive groups by fill color |
| Single-accent economics | `#1f4e79`, `#8f8f8f`, `#d9eaf7` | One focal estimate, one treatment line, simple trend | More than two substantive groups |
| Treatment-control | `#1f4e79`, `#b45f06`, `#777777`, `#d9d9d9` | DID trends, event study, treatment vs control | Red-green pairings |
| Sequential map | `#f7fbff`, `#c6dbef`, `#6baed6`, `#2171b5`, `#08306b` | Choropleth maps and spatial intensity | Categorical groups |
| Diverging map/effect | `#b2182b`, `#f7f7f7`, `#2166ac` | Positive/negative effects around zero | Variables without meaningful midpoint |

## Source-Specific Starting Points

| Source | Audit Template | Suggested Public Template | Recommended Use | Caution |
| --- | --- | --- | --- | --- |
| E01 | Multi-accent with red/cyan/gray signals | Treatment-control or restrained multi-accent | Mechanism or model illustration with few groups | Convert very light fills to print-safe tones |
| E02 | Table-first monochrome | Table-first monochrome | Theory or model tables | Keep figures simple unless needed for intuition |
| E03 | Missing main text | Table-first monochrome | Not audited | Do not infer palette from appendix-only material |
| E04 | Monochrome/grayscale | Single-accent economics | Theory figures and tables | Use line type if more than one curve appears |
| E05 | Monochrome/grayscale | Single-accent economics | Mechanism and comparative-statics figures | Avoid decorative gradients |
| E06 | Downgraded text quality | Table-first monochrome | Source list only unless manually checked | Do not make source-specific visual claims |
| E07 | Downgraded text quality | Table-first monochrome | Source list only unless manually checked | Do not make source-specific visual claims |
| E08 | Monochrome/grayscale | Single-accent economics | Model, implication, and calibration figures | Keep labels close to plotted objects |
| E09 | Monochrome/grayscale | Single-accent economics | Theory implication figures | Use direct labels when legends crowd the plot |
| E10 | Table-first monochrome | Table-first monochrome | Theory/model tables | Keep table width conservative |
| E11 | Monochrome/grayscale | Single-accent economics | Main empirical result figures | Use gray CI bands or capped intervals |
| E12 | Dark multi-accent signal | Treatment-control | Policy or historical contrast figures | Use solid/dashed lines, not color alone |
| E13 | Pastel multi-accent signal | Treatment-control, print-safe | Local-labor-market trends and maps | Darken pastels before publication |
| E14 | Cool multi-accent signal | Sequential map or treatment-control | Spatial RD, map, and distance-gradient figures | Keep map legend readable in grayscale |
| E15 | Table-first monochrome | Table-first monochrome | Historical development tables | Use figures only when they show the central fact |
| E16 | Light green sequential signal | Sequential map | Environmental/spatial intensity figures | Convert green-only palettes for colorblind safety |
| E17 | Monochrome/grayscale | Single-accent economics | Culture or historical-mechanism figures | Avoid crowded legends |
| E18 | Monochrome/grayscale | Treatment-control | Household balance-sheet trends | Separate levels from growth rates |
| E19 | Monochrome/grayscale | Single-accent economics | Mobility maps and distribution figures | Maps need clear bins and legend titles |
| E20 | Monochrome/grayscale | Treatment-control | RCT and firm-productivity figures | Put confidence intervals in neutral gray |
| C01 | Monochrome/grayscale | Table-first monochrome | Chinese theory or framework papers | Use Chinese labels consistently |
| C02 | Table-first monochrome | Table-first monochrome | New structural economics framework text | Do not over-visualize conceptual claims |
| C03 | Monochrome/grayscale | Single-accent economics | Development strategy and distribution figures | Keep captions bilingual only when required |
| C04 | Table-first monochrome | Table-first monochrome | Political-economy institutional tables | Avoid workflow notes in table notes |
| C05 | Monochrome/grayscale | Single-accent economics | Governance framework figures | Keep mechanism diagrams sparse |
| C06 | Table-first monochrome | Table-first monochrome | Decentralization reform tables | Use panels for province/period splits |
| C07 | Table-first monochrome | Table-first monochrome | Fiscal decentralization regressions | Put FE/control rows below coefficients |
| C08 | Blue multi-accent signal | Single-accent economics | Market segmentation figures | Use darker blue for focal series |
| C09 | Monochrome/grayscale | Single-accent economics | Measurement and decomposition figures | State units in axis titles |
| C10 | Missing/restricted text in audit | Table-first monochrome | Not audited in first pass | Do not infer table structure until source is available |
| C11 | Monochrome/grayscale | Single-accent economics | Trade liberalization and productivity figures | Do not mix firm-level and aggregate scales |
| C12 | Monochrome/grayscale | Table-first monochrome | Processing trade tables | Keep robustness in appendix unless central |
| C13 | Monochrome/grayscale | Table-first monochrome | Export participation tables | Limit heterogeneity columns |
| C14 | Missing main document | Table-first monochrome | Not included in first pass | Await source before source-specific claims |
| C15 | Downgraded text quality | Table-first monochrome | Source list only unless manually checked | Use only high-level design signals |
| C16 | Table-first monochrome | Table-first monochrome | Minimum wage and export tables | State sample and clustering clearly |
| C17 | Monochrome/grayscale | Single-accent economics | Spatial equilibrium and urbanization figures | Use maps or trends only when visually decisive |
| C18 | Downgraded text quality | Table-first monochrome | Source list only unless manually checked | Use only high-level design signals |
| N01 | Monochrome/grayscale | Single-accent economics | Industry-structure figures | Keep category order meaningful |
| N02 | Table-first monochrome | Table-first monochrome | External-shock regression tables | Put shock definition in note or text |
| N03 | Table-first monochrome | Table-first monochrome | Automation-capital regressions | Use panels for mechanism/heterogeneity splits |
| N04 | Monochrome/grayscale | Single-accent economics | Fiscal-rule trends and event figures | Mark policy timing explicitly |
| N05 | Monochrome/grayscale | Single-accent economics | Added Chinese journal figure examples | Treat as supplementary style source |

## Check

A palette is acceptable only if the same result remains legible when printed in grayscale, viewed on a projector, and pasted into Word/PDF without changing font or line weight.
