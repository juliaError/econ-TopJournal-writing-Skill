# Table Notes

## Required Contents

For regression tables, notes should normally state:

- sample and unit of observation;
- estimator or model family when not obvious;
- standard error convention;
- clustering level;
- fixed effects;
- control variables or where they are listed;
- significance stars;
- special sample restrictions or variable definitions needed to read the table.

## What Not To Put In Notes

- The author's workflow, such as why a column was dropped or which draft changed.
- Submission strategy, author-agent discussion, or text such as `for space we moved this`, `为了节省篇幅`, `作者需要补充`, or `为满足专题要求`.
- Defensive language about significance.
- Long variable construction paragraphs that belong in the data section or appendix.
- Repeated details already stated clearly in the first relevant table note.

## Main-Text Pointers Versus Table Notes

Do not let main-text cross-references explain table construction. A main-text pointer should only say what to see and where to see it. Only when needed, add the table's substantive role for the current claim, such as robustness, variable construction, sample scope, background fact, derivation, or extended result. Do not write empty relevance language such as `therefore it is related to the main text` or `因此与正文有关`.

- Good main-text pointer: `AI适配度前10和后10城市及其人均GDP见在线附录C3。`
- Bad main-text pointer: `在线附录C3左边列示前十城市，右边列示后十城市，中间分开排版。`

If layout guidance is genuinely necessary for reading a dense appendix table, put it in the appendix table title, table note, or short appendix paragraph, not in the main text. Use neutral reader-facing language rather than production language:

- acceptable note: `注：本表左、右两组分别报告AI适配度最高和最低的10个城市。`
- avoid production note: `注：本表为了排版采用左右分栏并调整列宽。`

## English Template

`Notes: The table reports [estimator] estimates for [sample/unit]. Standard errors clustered at the [level] level are in parentheses. All columns include [fixed effects/controls]. *, **, and *** denote significance at the 10, 5, and 1 percent levels.`

## Chinese Template

`注：本表报告 [样本/单位] 的 [估计方法] 结果。括号内为按 [层级] 聚类的标准误。各列控制 [固定效应/控制变量]。*、**、*** 分别表示在 10%、5%、1% 水平上显著。`

## Check

After reading the note, the reader should not need to guess how standard errors, fixed effects, controls, or samples differ across columns.
