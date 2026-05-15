# Maps And Distribution Figures

## Maps

- Use maps when geography is part of the research design, exposure, or substantive mechanism.
- Use a sequential palette for intensity and a diverging palette only when values have a meaningful midpoint.
- Include a legend with units and bins.
- Make missing or excluded regions visually distinct.
- Avoid decorative base-map detail that competes with the economic variable.

## China Maps

Treat China maps as a compliance-sensitive figure type. This rule applies to all uses of this skill, not only Chinese journals.

### Non-Negotiable Boundary Completeness

- A China map must be a complete China map. It must include the mainland, Hainan, Hong Kong/香港, Macao/澳门, Taiwan province/台湾省, South Tibet/Zangnan/藏南, and other required national-boundary regions.
- Do not use or deliver a China base map that omits Hong Kong/香港, Macao/澳门, Taiwan province/台湾省, South Tibet/Zangnan/藏南, Aksai Chin, the South China Sea islands, Diaoyu Dao and affiliated islands, or required national-boundary linework.
- If the map package provides a South China Sea dashed line / nine-dash-line / 南海断续线 layer, include it. If the package does not provide it, prefer an official or approved base map that does; otherwise add a compliant South China Sea inset or line layer before delivery.
- Do not crop, mask, label over, or place annotations in a way that hides important islands, national-boundary linework, South China Sea inset content, or the dashed line.
- Hong Kong, Macao, and Taiwan province must not disappear merely because the dataset lacks observations for them. Show them as no data / not in sample when necessary, but keep the geography visible.

### Source And Legal-Safety Rules

- Prefer authoritative standard-map sources, especially the Ministry of Natural Resources standard map service or a map that has a valid review number when the output will be public-facing.
- Record the base-map source in the figure note or workflow notes. If a review number is available, retain it.
- Do not rely blindly on default `sf`, `geopandas`, `echarts`, `plotly`, online tile, or public shapefile boundaries; many packages omit or simplify sensitive boundary elements.
- If the map is for publication, media, public presentation, or online release, check whether map review or an approved standard map is required before treating the artifact as final.

### Layout Pattern For Publication Figures

- Use one clean main map with thin administrative boundaries, a restrained fill palette, and no decorative background.
- Use a South China Sea inset when the main frame cannot show the South China Sea islands and dashed line clearly.
- Keep the inset visible, legible, and inside the figure boundary; do not reduce it to an unreadable stamp.
- Keep aspect ratio and projection stable; do not stretch the map to fit a panel.
- Use a clear legend with variable name, units, bins, and missing/no-data category.
- If Hong Kong, Macao, Taiwan province, or South China Sea regions are not part of the analytical sample, mark them explicitly as no data / not in sample rather than deleting them.
- Use Chinese labels for Chinese-language outputs: `香港`, `澳门`, `台湾省`, `南海诸岛`, `藏南` when labels are needed. Do not over-label if labels crowd the map.
- Add a concise note when helpful: base-map source, data year, unit of observation, classification method, and whether missing regions are outside the sample.

### Python Mini/Long Layout Pattern

When adapting the common Python `geopandas` + `matplotlib` style for China maps, keep the technical layout but verify or replace the base map with a complete, compliant China map.

- Use `geopandas` for vector data and `matplotlib` for drawing. Reproject every boundary, point, raster-derived point, and polygon layer to one fixed China projection before plotting; a common choice is an Albers equal-area projection centered on China.
- Keep map geometry at equal aspect ratio. After plotting, set `ax.set_aspect("equal")`, preserve the calculated x/y limits, and adjust figure width/height to the map bounds instead of stretching the map into an arbitrary rectangle.
- Draw the map in stable layers: base administrative polygons, data fill or points, national/coastline/boundary linework, South China Sea inset or small-map linework, province labels only if legible, then scale bar, north arrow, legend, title, and note.
- If the boundary file has line classes such as `九段线`, `海岸线`, `小地图框格`, or `省份`, filter and draw those classes explicitly. Do not let the dashed line or small-map frame disappear because it is stored in a separate line shapefile.
- For the mini-map layout, treat the South China Sea small map as part of the national map, not as decoration. If points or raster/polygon observations fall inside the small-map bounding box, transform those geometries into the inset by translating to the inset origin, scaling, and translating to the displayed frame; then merge the transformed geometries back with the main layer.
- For the long-map layout, use a portrait figure and keep the full long boundary line layer, especially `九段线` and `海岸线`. A long map that lacks the South China Sea small-map frame still must show complete national-boundary elements through the long boundary data.
- For yearly province/city/county maps, use the boundary file for the same administrative year as the data whenever the historical boundary matters. Keep projection, extent, legend bins, missing-data color, label policy, and export size stable across years unless the figure is explicitly exploratory.
- For choropleths, merge data by stable administrative codes before falling back to names. Keep regions with no observations as `no data` / `not in sample`; never drop them from the base layer.
- For point or raster-derived maps, reproject longitude/latitude points before plotting. If using raster data, aggregate or polygonize deliberately, clip to the complete China map only after the full boundary is loaded, and retain the inset or dashed-line layer afterward.
- Export publication figures as vector PDF/SVG when the map contains mostly vector geometry; also export a high-resolution PNG when Word or preview workflows need it. For raster-heavy maps, use at least 400 dpi and visually inspect the final artifact, not only the script output.

### Rejection Checklist

Reject or revise the figure if any item is true:

- Taiwan province, Hong Kong, Macao, Hainan, South China Sea islands, South Tibet/Zangnan, or Aksai Chin is absent from a national China map.
- The South China Sea dashed line / nine-dash-line layer exists in the map package but is not drawn.
- Taiwan or Hainan is shown with a style implying it is outside China when the map is a China map.
- The boundary is visibly cropped, distorted, or hidden by labels, legends, arrows, or annotation boxes.
- The map package source is unknown and the boundary cannot be checked.
- The figure uses color as decoration rather than to encode a geographic variable.
- A mini-map or long-map script draws only the filled polygons and forgets the separate line layer containing `九段线`, `海岸线`, `小地图框格`, or national-boundary linework.

## Distribution Figures

- Use histograms, density plots, or quantile plots to show exposure, outcome dispersion, or sample comparability.
- Use identical bins or bandwidths when comparing groups.
- Use transparency sparingly; overlapping filled distributions often become muddy in print.
- Consider faceting instead of overlaying many distributions.

## Color Rules

- Sequential maps: light-to-dark single hue.
- Diverging maps: two restrained hues with a neutral midpoint.
- Distribution comparison: focal color plus neutral gray, or two print-safe contrasting line styles.

## Check

A reader should know what variable is mapped or distributed, what unit it uses, and why this visual belongs in the paper.
