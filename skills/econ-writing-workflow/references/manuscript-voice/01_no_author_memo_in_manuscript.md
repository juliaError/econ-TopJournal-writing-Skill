# No Author Memo In Manuscript

## Core Rule

Separate three output channels before writing or revising:

- **Manuscript Text**: text that a journal reader should see in the paper, table note, figure note, appendix, or footnote.
- **Author Memo**: advice to the author about why to move, delete, shorten, or reframe content.
- **Task Log**: workflow record for README files, implementation notes, or revision history.

Only `Manuscript Text` may enter the paper. `Author Memo` and `Task Log` belong in the response, task README, revision memo, or author-facing checklist.

## Paragraph-Level Linter

Run this linter after each paragraph or note, not only at the end:

1. Is the sentence explaining the economic object, model, identification, result, data limit, or interpretation to the reader?
2. Or is it explaining what the author/agent chose to do, why something was moved, why a draft is shaped a certain way, or how to satisfy a call for papers?
3. Would the sentence still make sense if read by an anonymous referee with no access to the author-agent conversation?
4. Does the sentence mention drafting, writing strategy, submission positioning, appendix management, deleted material, or future author work?

If the answer to 2 or 4 is yes, move it out of the manuscript or rewrite it as reader-facing scope/interpretation.

## Main-Text Pointer Rule

When the main text points to an appendix, table, figure, or online appendix, the pointer sentence should answer only:

1. **what** the reader can find there;
2. **where** it is located;
3. only if needed, the appendix item's **substantive role** for the current claim, such as robustness, variable construction, sample scope, background fact, derivation, or extended result.

Do not satisfy the third item with meta-language such as `this is related to the main text`, `therefore it is relevant`, `因此与正文有关`, `所以和正文有关`, or `与正文相关`. Either name the substantive role or omit the clause.

Do not mix main-text pointers with table-layout or file-construction explanations. Layout details such as `left panel`, `right panel`, `split columns`, `two-column layout`, `column width`, `page break`, `continued table`, `repeated header`, `left half`, `right half`, `分栏`, `左半部分`, `右半部分`, `列宽`, `跨页`, `续表`, `表头复写`, `中间分开`, or `排版` belong in an appendix paragraph, table title, table note, or production memo, not in the main text.

Acceptable main-text pointer:

- `AI适配度前10和后10城市及其人均GDP见在线附录C3。`
- `Appendix Table C3 reports the ten cities with the highest and lowest AI-fit scores and their GDP per capita.`

Not acceptable as main-text prose:

- `在线附录C3左边列示前十城市，右边列示后十城市，中间分开排版。`
- `Appendix Table C3 uses a split-column layout with the top ten on the left and the bottom ten on the right.`

If the reader truly needs layout guidance to read a dense appendix table, put it in the appendix table note or the short appendix text immediately before the table.

## Hard-Reject Patterns

Do not put these in manuscript text, table notes, or figure notes:

- explicit workflow: `本段这样写`, `这样写的目的`, `本文采取……写法`, `为了把文章写成`, `避免把文章写成`, `包装成`, `保留这部分`, `删去/删除这部分`, `调整为`, `修改为`;
- author-agent conversation: `作者需要补充`, `后续可以补充`, `我们先不写`, `这里先放着`, `待后续完善`, `TODO`;
- submission strategy: `为了满足征稿要求`, `为了贴合专题期刊`, `为了回应编辑偏好`, `AI专题要求`, `专题而言` when it only justifies journal fit rather than states a research contribution;
- appendix/workflow movement: `为节省篇幅移入附录`, `这部分放在附录`, `正文不再展开是因为`, `表格已移到附录`, unless rewritten as a reader-facing appendix cross-reference;
- defensive draft talk: `这一定位并不降低文章价值`, `这样处理更符合投稿要求`, `这不是作者想做的重点`, `本文不打算做`;
- table/figure workflow: `这一列被删掉`, `这张图换成`, `为了美观调整`, `这里没有展示是因为结果不好`.

## Context-Dependent Patterns

These phrases are not automatically forbidden. Use them only when they introduce substantive information the reader needs:

- `需要说明的是`: acceptable for a real definition, sample boundary, identifying assumption, or interpretation limit. Avoid it when it introduces drafting strategy.
- `本文不再赘述` / `不再展开`: acceptable only for genuinely standard derivations or previously established definitions, and usually better as a concise cross-reference.
- `完整结果见附录`: acceptable when it names the concrete appendix/table/figure and the appendix contains reader-relevant robustness or derivation. Avoid vague appendix dumping.
- `不是……而是……`: acceptable for conceptual distinction, model scope, or interpretation boundary. Avoid using it to defend a writing choice.
- `本文不把……解释为因果效应`: acceptable when it clarifies identification scope. Keep the object specific.

## Rewrite Rules

Turn author-facing draft talk into reader-facing economics prose:

- Instead of saying the paper uses a certain "writing style," state the research design's scope: `本文提供任务结构与AI技术方向匹配的测度和反事实核算，不估计AI对城市GDP、工资或就业的总效应。`
- Instead of saying content was moved for length, state the appendix object: `附录C报告替换指标、调整样本门槛和改变权重口径后的完整稳健性结果。`
- Instead of saying a section satisfies a call for papers, state the substantive fit: `本文把AI能力的任务方向与城市新增劳动需求结构连接起来，刻画通用技术在空间上的潜在收益差异。`
- Instead of saying the author will later supplement a point, either write the missing fact as `TODO` in an author memo or omit it from manuscript text.

## Final Delivery Check

Before finalizing manuscript text, scan for:

- `写法`, `定位`, `包装`, `专题`, `征稿`, `篇幅`, `移入附录`, `放入附录`, `不再赘述`, `暂不展开`, `后续补充`, `作者需要`, `TODO`, `修改`, `删除`, `保留`;
- pointer leakage in sentences containing `见附录`, `见在线附录`, `见表`, `见图`, `报告于`, `列示于`, `参见`, `see Appendix`, `see Table`, or `see Figure`: layout language such as `分栏`, `左半部分`, `右半部分`, `左边`, `右边`, `列宽`, `跨页`, `续表`, `表头复写`, `中间分开`, `排版`, `split columns`, `left panel`, `right panel`, `page break`, `continued table`, `repeated header`; or empty relevance language such as `与正文有关`, `和正文有关`, `与正文相关`, `related to the main text`, `relevant to the current text`;
- English equivalents: `to satisfy the call`, `for the special issue`, `we do not discuss here`, `for space`, `moved to the appendix`, `the author should`, `this draft`, `we choose to write`.

For each hit, decide:

- **Keep** if it is a reader-facing definition, scope condition, cross-reference, or identification caveat.
- **Rewrite** if the economics point is valid but phrased as a drafting choice.
- **Move** if it belongs in an author memo or task log.
