# No Author Memo In Manuscript

## Scope: Manuscript Prose Versus Outlines And Proposals

The manuscript-only prohibitions below apply to prose intended for the paper's
reader. For outlines and research-team staffing briefs, first apply Audience
And Intended Use in `../../SKILL.md` and the recipient-necessity checks in
`../outlines/01_argument_and_writing_task_outlines.md`. Exclude internal
editorial deliberation from circulated documents, but preserve useful reading
assignments, argument steps, sources and figure/table instructions in a task
outline. Words such as “写”, “制作” or “完成” do not by themselves indicate
internal leakage. A complete proposal still needs its substantive research
rationale, evidence status, methods, feasibility, risks and necessary stages;
apply its own genre requirements rather than mechanically banning future work.

## Core Rule

Separate three output channels before writing or revising:

- **Manuscript Text**: text that a journal reader should see in the paper, table note, figure note, appendix, or footnote.
- **Author Memo**: advice to the author about why to move, delete, shorten, or reframe content.
- **Task Log**: workflow record for README files, implementation notes, or revision history.

Only `Manuscript Text` may enter the paper. `Author Memo` and `Task Log` belong in the response, task README, revision memo, or author-facing checklist.

## Unclear Manuscript Facts

If a manuscript fact or author choice is unclear, do not fill it in by guessing. Apply the author-intent gate and return `clarification_required` without drafting the affected text when the uncertainty concerns:

- research question, theory channel, mechanism, or contribution;
- variable definition, sample construction, estimation choice, identification assumption, or coefficient interpretation;
- table/figure meaning, main-text versus appendix placement, target-journal requirement, or whether to keep/delete a substantive claim.

These are semantic choices: do not replace the author's decision with a
`TODO`, a tentative sentence, or silent omission. A concrete author-facing
`TODO` is allowed only for a missing factual, citation, or verification detail
that does not change a frozen-current proposition or its evidence boundary.
Do not turn uncertainty into manuscript prose such as `本文可能`, `可理解为`,
`可以认为`, or a confident claim not supported by the provided draft/results.

## Author-Facing Diagnostic Labels

Labels such as `一句话主线`, `主线功能`, `表图对主线的支撑`, `它支撑了主线的哪一环`, `是否需要进入正文`, `是否可移入附录`, `next revision step`, and `argument spine` are diagnostic labels for author memos, review reports, task READMEs, or checklists. They must not appear in manuscript text, table notes, figure notes, appendix notes, or footnotes.

When moving from diagnosis to manuscript prose, replace these labels with the concrete reader-facing object:

- say `表4检验替换核心解释变量口径后，基准结果是否保持稳定`, not `表4支撑主线`;
- say `该异质性结果表明政策效应主要集中在高司法保护地区`, not `该结果服务于论文主线`;
- say `附录C报告替换样本门槛后的估计结果`, not `该表可移入附录`.

## Paragraph-Level Linter

Run this linter after each paragraph or note, not only at the end:

1. Is the sentence explaining the economic object, model, identification, result, data limit, or interpretation to the reader?
2. Or is it explaining what the author/agent chose to do, why something was moved, why a draft is shaped a certain way, or how to satisfy a call for papers?
3. Would the sentence still make sense if read by an anonymous referee with no access to the author-agent conversation?
4. Does the sentence mention drafting, writing strategy, submission positioning, appendix management, deleted material, or future author work?
5. Does the sentence contain an author-facing diagnostic label such as `主线功能`, `支撑主线`, `服务主线`, `是否进入正文`, `是否移入附录`, `argument spine`, or `revision step`?

If the answer to 2, 4, or 5 is yes, move it out of the manuscript or rewrite it as reader-facing scope/interpretation.

## Main-Text Pointer Rule

When the main text points to an appendix, table, figure, or online appendix, the pointer sentence should answer only:

1. **what** the reader can find there;
2. **where** it is located;
3. only if needed, the appendix item's **substantive role** for the current claim, such as robustness, variable construction, sample scope, background fact, derivation, or extended result.

Do not satisfy the third item with meta-language such as `this is related to the main text`, `therefore it is relevant`, `因此与正文有关`, `所以和正文有关`, or `与正文相关`. Either name the substantive role or omit the clause.

Do not mix main-text pointers with table-layout or file-construction explanations. Layout details such as `left panel`, `right panel`, `split columns`, `two-column layout`, `column width`, `page break`, `continued table`, `repeated header`, `left half`, `right half`, `分栏`, `左半部分`, `右半部分`, `列宽`, `跨页`, `续表`, `表头复写`, `中间分开`, or `排版` belong in an appendix paragraph, table title, table note, or production memo, not in the main text.

Acceptable main-text pointer:

- `拥堵指数最高和最低的十条运输线路见在线附录C3。`
- `Appendix Table C3 reports the ten routes with the highest and lowest congestion scores.`

Not acceptable as main-text prose:

- `在线附录C3左边列示拥堵指数最高的十条线路，右边列示最低的十条线路，中间分开排版。`
- `Appendix Table C3 uses a split-column layout with the highest-congestion routes on the left and the lowest-congestion routes on the right.`

If the reader truly needs layout guidance to read a dense appendix table, put it in the appendix table note or the short appendix text immediately before the table.

## Hard-Reject Patterns

Do not put these in manuscript text, table notes, or figure notes:

- explicit workflow: `本段这样写`, `这样写的目的`, `本文采取……写法`, `为了把文章写成`, `避免把文章写成`, `包装成`, `保留这部分`, `删去/删除这部分`, `调整为`, `修改为`;
- author-agent conversation: `作者需要补充`, `后续可以补充`, `我们先不写`, `这里先放着`, `待后续完善`, `TODO`;
- submission strategy: `为了满足征稿要求`, `为了贴合专题期刊`, `为了回应编辑偏好`, `AI专题要求`, `专题而言` when it only justifies journal fit rather than states a research contribution;
- appendix/workflow movement: `为节省篇幅移入附录`, `这部分放在附录`, `正文不再展开是因为`, `表格已移到附录`, unless rewritten as a reader-facing appendix cross-reference;
- defensive draft talk: `这一定位并不降低文章价值`, `这样处理更符合投稿要求`, `这不是作者想做的重点`, `本文不打算做`;
- table/figure workflow: `这一列被删掉`, `这张图换成`, `为了美观调整`, `这里没有展示是因为结果不好`.
- author-facing diagnostic labels: `主线功能`, `支撑主线`, `服务主线`, `表图对主线的支撑`, `是否需要进入正文`, `是否可移入附录`, `下一步改写顺序`, `argument spine`, `revision step`.

## Context-Dependent Patterns

These phrases are not automatically forbidden. Use them only when they introduce substantive information the reader needs:

- `需要说明的是`: acceptable for a real definition, sample boundary, identifying assumption, or interpretation limit. Avoid it when it introduces drafting strategy.
- `本文不再赘述` / `不再展开`: acceptable only for genuinely standard derivations or previously established definitions, and usually better as a concise cross-reference.
- `完整结果见附录`: acceptable when it names the concrete appendix/table/figure and the appendix contains reader-relevant robustness or derivation. Avoid vague appendix dumping.
- `不是……而是……`: acceptable for a necessary conceptual distinction, model scope, or interpretation boundary after affirmative wording has stated what the object is. Avoid using it to defend a writing choice or to introduce a new object only so the sentence can deny it.
- `本文不把……解释为因果效应`: acceptable only when a concrete causal misreading remains after accurate verbs, claim type, and affirmative scope wording. Bind it to the exact result and use a stand-alone negative sentence only as a last resort.

“可接受”只描述语义候选，不授予写入权限。若上述精确否定命题未由作者确认并冻结，返回 `clarification_required`，提交正面解释与拟保留对照供作者裁决，不得由 AI 自行写入或保留。

## Caveat Placement Discipline

Reader-facing evidence boundaries are not author memos, but repetitive
defensive prose still weakens the manuscript. Prefer an accurate verb, claim
type, and local scope condition. Add a separate limitation only when the
reader could otherwise materially misread the evidence.

This test applies to the first or only caveat as well as later repetitions.
First state affirmatively what the result, estimate, threshold, scenario, or
model object represents and what it helps the reader interpret. This is not
positive spin: the wording must preserve the same evidence strength. A
stand-alone negative caveat is admitted only if it identifies the exact claim
it limits and blocks a concrete stronger reading that the affirmative wording
does not already exclude. If it introduces a new outcome or estimand only to
deny that the paper estimates it, delete it unless that confusion is materially
plausible; when it is plausible, integrate the distinction into the result
interpretation and leave a separate negative sentence as the last resort.

That last resort still requires author authority. If its exact negative
proposition is not already frozen, withhold it and return
`clarification_required`; a reviewer finding or polished rationale cannot
authorize manuscript insertion.

State the same limitation once when it first matters. Repeat it only when the
identification, sample, period, geography, extrapolation target, or evidence
grade changes; when the text actually discusses long-run, welfare, or
external-validity conclusions; when a stand-alone abstract, caption, table or
figure note must be self-contained; or when a journal or referee requires it.
Do not create a mechanical per-section quota, and do not add `not causal`,
`cannot be extrapolated`, or `cannot identify long-run effects` merely because
a new table or figure appears.

Removing a later repetition is a redundancy edit, not a change in author
intent, when the retained wording still conveys the full boundary for the
affected claims. If the evidence boundary has actually changed, state the new
specific condition rather than copying a generic disclaimer.

## Rewrite Rules

Turn author-facing draft talk into reader-facing economics prose:

- Instead of saying the paper uses a certain "writing style," state affirmatively what the design measures: `本文的模型比较刻画给定固定成本下的均衡进入率及其对需求弹性的敏感性。`
- Instead of saying content was moved for length, state the appendix object: `附录C报告替换指标、调整样本门槛和改变权重口径后的完整稳健性结果。`
- Instead of saying a section satisfies a call for papers, state the substantive fit: `本文把运输网络的拥堵暴露与企业路线选择连接起来，刻画固定容量下的均衡等待时间差异。`
- Instead of saying the author will later supplement a point, put a genuinely non-semantic missing fact in an author-facing `TODO`. Do not omit a frozen `must_express` proposition; if the missing item changes its meaning or support, return `clarification_required` or `evidence_conflict` and leave the affected manuscript text unwritten.

## Final Delivery Check

Before finalizing manuscript text, scan for:

- `写法`, `定位`, `包装`, `专题`, `征稿`, `篇幅`, `移入附录`, `放入附录`, `不再赘述`, `暂不展开`, `后续补充`, `作者需要`, `TODO`, `修改`, `删除`, `保留`;
- author-facing diagnostics: `主线功能`, `支撑主线`, `服务主线`, `表图对主线的支撑`, `是否需要进入正文`, `是否可移入附录`, `下一步改写顺序`, `argument spine`, `revision step`;
- pointer leakage in sentences containing `见附录`, `见在线附录`, `见表`, `见图`, `报告于`, `列示于`, `参见`, `see Appendix`, `see Table`, or `see Figure`: layout language such as `分栏`, `左半部分`, `右半部分`, `左边`, `右边`, `列宽`, `跨页`, `续表`, `表头复写`, `中间分开`, `排版`, `split columns`, `left panel`, `right panel`, `page break`, `continued table`, `repeated header`; or empty relevance language such as `与正文有关`, `和正文有关`, `与正文相关`, `related to the main text`, `relevant to the current text`;
- English equivalents: `to satisfy the call`, `for the special issue`, `we do not discuss here`, `for space`, `moved to the appendix`, `the author should`, `this draft`, `we choose to write`.

For each hit, decide:

- **Keep** if it is a reader-facing definition, scope condition, cross-reference, or identification caveat and, for a stand-alone negative caveat, its exact proposition is already frozen by the author.
- **Rewrite** if the economics point is valid but phrased as a drafting choice.
- **Move** if it belongs in an author memo or task log.

For every stand-alone negative caveat, including its first occurrence, record
the exact claim it limits, the concrete stronger misreading it blocks, whether
calibrated wording already blocks that reading, whether the sentence introduces
a new object only to deny it, and whether affirmative interpretation can carry
the needed meaning. For repeated hits, also compare identification, sample,
period, geography, extrapolation target, and evidence grade with the first
adequate statement. Keep a negative sentence only when it adds material
interpretive information or the object must stand alone, and only with the
exact frozen author-intent authority required above. Otherwise return
`clarification_required`.
