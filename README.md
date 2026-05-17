# Economics Writing Workflow Skills / 经济学论文写作 Workflow Skills ✨

This repository is a self-developed Codex skill system for economics paper writing, revision, style adaptation, table/figure design, and workflow routing. It supports English economics prose and top-journal style, Chinese top-journal writing, bilingual table and figure presentation, and auditable full-draft workflows based on user-owned research questions and result packages.

It is a writing workflow system, not a complete empirical pipeline: it does not cover the full process of data cleaning, variable construction, regression estimation, or reproducible empirical execution.

It uses a modular structure: ordinary users can start from the main workflow skill, while advanced users can call specialized sub-skills directly.

这是我开发的一套经济学论文写作 Codex skill 系统，用于论文写作、修改、风格适配、表格图形设计和 workflow 路由。它同时覆盖英文经济学论文写作与英文顶刊风格、中文顶刊写作、中英文通用表图展示，以及基于作者自己研究问题和结果包的可审查完整初稿流程。

它是写作 workflow 系统，不是完整实证流程；不覆盖数据清洗、变量构造、回归估计或可复现实证执行的完整过程。

它采用模块化结构：普通用户可以从总入口 workflow skill 开始，高级用户也可以直接调用专业子 skill。

Important notes: AI writing can only assist the research and drafting process; the key academic judgments still depend on human researchers. This really is not a defensive disclaimer; AI is simply not perfect yet. For serious writing and revision tasks, use the latest and strongest available models when possible, such as GPT-5.5 or Claude 4.6. DeepSeek may be useful for Chinese prose polishing, but it still has limitations in figure and table production.

注意事项：AI 写作只能辅助研究和成文过程，关键学术判断依然离不开人类研究者。这真的不是叠甲，而是 AI 现在确实还达不到完美。进行重要写作和修改任务时，建议尽可能使用当时最新、最强的模型，例如 GPT-5.5 或 Claude 4.6；中文润色也可以使用 DeepSeek，但其在作图和制表方面仍有一定不足。

## What Is Inside / 仓库内容 🧭

### English

| Path | Description |
| --- | --- |
| `skills/econ-writing-workflow/` | Main entry skill that routes economics writing tasks to the relevant English, Chinese, full-draft, or table/figure module, and points empirical work to the empirical workflow. |
| `skills/econ-write/` | General English economics paper writing skill for abstracts, introductions, literature reviews, theory sections, empirical sections, tables, robustness, LaTeX, and revision. |
| `skills/econ-write/references/paper_skills/` | Optional section-specific reference modules loaded by `econ-write` when relevant. Some files are still being developed. |
| `skills/cn-top-econ-writing/` | Chinese top-journal economics writing skill for journals such as 《经济研究》, 《管理世界》, and 《中国工业经济》, including Chinese diction cleanup and argument-logic checks. |
| `skills/econ-table-figure-design/` | Bilingual economics table and figure design skill for regression tables, robustness, heterogeneity, mechanisms, notes, captions, palettes, and export checks. |
| `docs/paper-corpus.md` | Corpus policy for how local writing-learning sources are used without publishing paper lists or source text. |
| `LICENSE` | Layered license overview: original repository content is CC BY-NC 4.0; third-party content keeps its own license. |
| `NOTICE.md` | Third-party copyright and MIT License notice. |
| `ETHICAL_USE.md` | Ethical-use policy for non-commercial academic writing support. |
| `docs/ai-assistance.md` | Notes on AI-assisted development and responsibility. |

### 中文

| 路径 | 说明 |
| --- | --- |
| `skills/econ-writing-workflow/` | 普通用户主要调用的写作总入口 skill，负责把经济学写作任务路由到英文、中文、完整初稿或表图模块；涉及实证工作时提示搭配实证 workflow。 |
| `skills/econ-write/` | 通用英文经济学论文写作 skill，覆盖摘要、引言、文献、理论、实证、表图、稳健性、LaTeX 和修改审查。 |
| `skills/econ-write/references/paper_skills/` | `econ-write` 按需加载的分 section 参考规则；部分文件仍在开发中。 |
| `skills/cn-top-econ-writing/` | 面向《经济研究》《管理世界》《中国工业经济》等中文顶刊的写作、审查和修稿 skill，包含中文遣词造句清理和论证逻辑检查。 |
| `skills/econ-table-figure-design/` | 中英文通用经济学表格与图形设计 skill，覆盖三线表、主回归、稳健性、异质性、机制、表注图注、配色和导出检查。 |
| `docs/paper-corpus.md` | 语料使用政策，说明如何使用本地写作学习来源，同时不公开论文清单或来源文本。 |
| `LICENSE` | 分层许可说明：本仓库原创内容采用 CC BY-NC 4.0；第三方内容保留原许可。 |
| `NOTICE.md` | 外部来源与 MIT License 声明。 |
| `ETHICAL_USE.md` | 非商用学术写作辅助的伦理使用说明。 |
| `docs/ai-assistance.md` | 关于 AI 辅助开发、署名和责任边界的说明。 |

## Knowledge Sources / 知识来源 📚

### English

This repository currently has two kinds of sources:

1. **Third-party skill source**: `skills/econ-write/` is based on the open-source [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) project by Lu Han, licensed under the MIT License.
2. **Corpus-informed rules**: the modular writing and table/figure workflows are informed by Econ Top 5 papers (AER, QJE, JPE, Econometrica, REStud) and Chinese top-journal papers, including papers published in *Economic Research Journal*, *Management World*, and *China Industrial Economics*. Because some paper authors may object to their articles being publicly labeled as distilled sources, the full paper list is not published for now.

See [`docs/paper-corpus.md`](docs/paper-corpus.md) for the corpus-use policy.

### 中文

本仓库目前有两类来源：

1. **外部 skill 来源**：`skills/econ-write/` 基于 Lu Han 的开源项目 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill)，许可证为 MIT License。
2. **语料启发规则**：模块化写作和表图 workflow 来自 Econ Top 5 论文（AER、QJE、JPE、Econometrica、REStud）和中文顶刊论文，包括发表于《经济研究》《管理世界》《中国工业经济》的论文。由于担心各论文作者可能不愿意自己的文章被公开标注为蒸馏来源，短期内不公布完整论文清单。

语料使用政策见 [`docs/paper-corpus.md`](docs/paper-corpus.md)。

## Install Locally / 本地安装 🚀

### English

#### Method 1 (Recommended): Ask an AI agent to install

Copy the repository URL and ask an AI agent to download and install the skills for you.

```text
Please help me download and install the Codex skills from this repository:
https://github.com/juliaError/econ-TopJournal-writing-Skill

Copy `skills/econ-writing-workflow`, `skills/econ-write`, `skills/cn-top-econ-writing`, and `skills/econ-table-figure-design` into `~/.codex/skills/`, then tell me whether I still need to refresh or restart Codex.
```

#### Method 2: Manual copy

Clone or download this repository, then copy the skill directories into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-writing-workflow ~/.codex/skills/econ-writing-workflow
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
cp -R skills/econ-table-figure-design ~/.codex/skills/econ-table-figure-design
```

After either method, restart or refresh Codex so the skills list is reloaded.

### 中文

#### 方法 1（推荐）：让 AI agent 帮你安装

复制这个仓库链接，让 AI agent 帮你下载并安装 skills。

```text
请帮我下载并安装这个仓库里的 Codex skills：
https://github.com/juliaError/econ-TopJournal-writing-Skill

把 `skills/econ-writing-workflow`、`skills/econ-write`、`skills/cn-top-econ-writing` 和 `skills/econ-table-figure-design` 复制到 `~/.codex/skills/`，然后告诉我是否还需要刷新或重启 Codex。
```

#### 方法 2：手动复制

克隆或下载本仓库，然后把 skill 目录复制到 Codex skills 文件夹：

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-writing-workflow ~/.codex/skills/econ-writing-workflow
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
cp -R skills/econ-table-figure-design ~/.codex/skills/econ-table-figure-design
```

无论使用哪种方法，安装后都需要重启或刷新 Codex，让 skills 列表重新加载。

## Usage / 使用方式 🛠️

### English

For most users, call `econ-writing-workflow` first. It will route the writing task to the right module.

```text
Use econ-writing-workflow to revise this paper's introduction, tables, and Chinese abstract.
```

It can also help draft an auditable full paper from your own research question, regression tables, figures, and design notes. Missing facts should remain as explicit `TODO` items rather than invented claims.

```text
Use econ-writing-workflow to draft a Chinese economics paper from this result folder, research question, variable notes, and figures. First audit the inputs, decide which tables and figures enter the main text, then draft the paper with TODO markers for missing literature or design details.
```

Advanced users may call specialized skills directly:

- Use `econ-write` for general English economics paper writing.
- Use `cn-top-econ-writing` for Chinese top-journal submissions.
- Use `econ-table-figure-design` when the task is about tables, figures, notes, palettes, or main-text versus appendix placement.

Examples:

```text
Use econ-write to revise this introduction.
```

```text
Use econ-table-figure-design to decide which regression tables and figures should enter the main text, how many columns each table should have, and what the notes should include.
```

For empirical coding, data cleaning, or regressions, pair these writing skills with a separate empirical workflow skill.

### 中文

普通用户日常优先调用 `econ-writing-workflow`。它会根据写作任务类型自动转向合适的模块。

```text
用 econ-writing-workflow 检查这篇经济学论文的引言、主回归表和中文表达。
```

如果你已经有自己的研究问题、回归表、图和识别/变量说明，也可以让它生成一版可审查的完整初稿。缺失信息应保留为明确的 `TODO`，不能编造。

```text
用 econ-writing-workflow 根据这个结果文件夹、研究问题、变量说明和图表，生成一版中文经济学论文初稿。先审查输入，再判断正文/附录表图，最后起草全文；缺失的文献和识别细节用 TODO 标出。
```

高级用户也可以直接调用专业子 skill：

- 一般英文经济学论文写作可以使用 `econ-write`。
- 中文顶刊投稿、修改和预审可以使用 `cn-top-econ-writing`。
- 涉及表格、图形、表注、图注、配色、正文/附录取舍时，可以使用 `econ-table-figure-design`。

示例：

```text
用 cn-top-econ-writing 审查这篇中文经济学论文的引言和贡献表述。
```

```text
用 econ-table-figure-design 检查这组主回归、稳健性、机制和异质性表，并给出正文表、附录表和配色方案。
```

如果任务涉及数据清洗、变量构造或回归代码，应搭配单独的实证工作流 skill，而不是只靠写作 skill。

## Current Status / 当前状态 🌱

### English

- **2026-05-16 update**:
  1. Added manuscript-safety guardrails that keep author-facing diagnostic labels out of paper prose, table notes, figure notes, appendix notes, and footnotes. When paper facts, variable definitions, samples, identification choices, table/figure meanings, target-journal requirements, or substantive keep/delete decisions are unclear, agents must ask the user or leave a concrete `TODO` instead of guessing.
  2. `econ-writing-workflow` now includes active mid-task routing, so long workflows re-check whether the current phase should use `econ-table-figure-design`, `cn-top-econ-writing`, `econ-write`, or `empirical-econ-workflow`.
  3. `econ-table-figure-design` now requires final rendered artifact inspection for drawn, edited, or regenerated figures and maps; agents must check that text, legends, colorbars, insets, axes, and map/figure content do not overlap or obscure useful information.
- **2026-05-15 update**:
  1. `econ-writing-workflow` now includes a project-level skill routing prompt for multi-step economics writing, table, figure, journal-submission, and formatting workflows.
  2. When no economics-writing routing rule exists in the nearest `AGENTS.md` or `CLAUDE.md`, the skill asks the user once whether to add a persistent local rule before editing either file.
  3. `cn-top-econ-writing` and `econ-table-figure-design` now point long-running tasks back to `econ-writing-workflow` for this persistent routing setup, so specialized skills are less likely to be forgotten during extended work.
- **2026-05-14 update**:
  1. `cn-top-econ-writing` now includes `references/argument-logic/`, a Chinese argument-logic module for transferring cross-language economics writing structure into Chinese top-journal writing without importing English diction, wording, or sentence order.
  2. The module covers argument spine, contribution preservation, abstract/introduction logic, theory and mechanism writing, main-result narration, mechanism/heterogeneity/robustness placement, table/figure argument fit, and post-rewrite drop checks.
  3. `chinese-diction` now explicitly runs after argument-logic when a task involves structure, contribution, section order, result organization, or table/figure placement.
- **2026-05-13 update**:
  1. `econ-write` now includes `references/english-diction/`, an English top-journal prose module for sentence functions, verbs/collocations, abstract and introduction patterns, theory-versus-empirical prose, and AI/translationese revision checks.
  2. `econ-table-figure-design` is now added as a bilingual table/figure design skill for main regression tables, robustness, heterogeneity, mechanisms, notes, captions, palettes, typography, and export checks.
  3. `econ-writing-workflow` now includes `references/argument-logic/` for full-paper logic, repeated material, emphasis, ordering, and table/figure fit.
  4. `econ-writing-workflow` now includes `references/full-paper-drafting/` for drafting an auditable paper from a user-owned result package, with input audits, table/figure placement, anti-fabrication `TODO` rules, and language-specific routing.
- `econ-write` is usable now and keeps its third-party MIT notice.
- `cn-top-econ-writing` is a standalone Chinese top-journal writing skill.
- `paper_skills` reference files are still being developed. Some files are placeholders until their detailed rule bodies are filled in.
- The long-term goal is to gradually rewrite the workflow into fully original economics writing skills based on local writing rules and non-source-specific abstractions.

### 中文

- **2026-05-16 更新**：
  1. 新增稿件安全护栏：作者诊断标签（如“主线功能”“支撑主线”“是否进入正文”）不得进入正文、表注、图注、附录说明或脚注；当研究事实、变量口径、样本构造、识别设定、表图含义、目标期刊要求或实质取舍不清楚时，agent 必须询问用户或留下具体 `TODO`，不能自行猜测。
  2. `econ-writing-workflow` 已新增任务过程中的主动重路由规则，长任务中会反复检查当前阶段是否应切换到 `econ-table-figure-design`、`cn-top-econ-writing`、`econ-write` 或 `empirical-econ-workflow`。
  3. `econ-table-figure-design` 现在要求对绘制、修改或重新生成后的图形和地图进行最终渲染结果检查，必须确认文字、图例、色带、小图框、坐标轴和地图/图形内容没有重叠、遮挡或压住有效信息。
- **2026-05-15 更新**：
  1. `econ-writing-workflow` 已新增项目级 skill 路由提示，适用于多步骤论文写作、制表、绘图、投稿体例和格式检查任务。
  2. 当最近的 `AGENTS.md` 或 `CLAUDE.md` 中尚无 economics-writing routing 规则时，skill 会先询问用户是否添加持久本地规则；未获明确授权前不会修改这些文件。
  3. `cn-top-econ-writing` 和 `econ-table-figure-design` 现在会在长任务中提示回到 `econ-writing-workflow` 统一设置持久路由，降低 agent 做着做着忘记调用相关 skill 的风险。
- **2026-05-14 更新**：
  1. `cn-top-econ-writing` 已新增 `references/argument-logic/` 中文论证逻辑模块，把经济学论文可跨语言迁移的写作结构转化为中文顶刊规则，但不迁移英文句式、表达或语序。
  2. 该模块覆盖全文主线、贡献保护、摘要/引言逻辑、理论与机制写作、主结果叙述、机制/异质性/稳健性取舍、表图是否服务主线，以及改写后的 drop check。
  3. `chinese-diction` 现在明确在涉及结构、贡献、章节顺序、结果组织或表图取舍时，先走论证逻辑判断，再做中文遣词造句和 AI 腔/翻译腔清理。
- **2026-05-13 更新**：
  1. `econ-write` 已新增 `references/english-diction/` 英文顶刊遣词造句模块，覆盖句子功能、动词搭配、摘要与引言句法、理论/实证 prose 差异，以及 AI 腔/翻译腔修稿检查。
  2. 新增 `econ-table-figure-design` 中英文通用表图设计 skill，覆盖主回归表、稳健性、异质性、机制、表注图注、配色、字体字号和导出检查。
  3. `econ-writing-workflow` 已新增 `references/argument-logic/`，用于全文逻辑、重复删除、重点排序和表图是否服务主线的审查。
  4. `econ-writing-workflow` 已新增 `references/full-paper-drafting/`，用于基于作者自己的研究问题、结果包和图表生成可审查初稿，并通过输入审查、正文/附录表图安排、禁止编造的 `TODO` 规则和中英文写作路由保证边界清楚。
- `econ-write` 当前可直接使用，并已保留第三方 MIT 声明。
- `cn-top-econ-writing` 是独立的中文顶刊写作 skill。
- `paper_skills` 参考文件仍在开发中，部分文件目前仍是占位。
- 长期目标是逐步基于本地写作规则和非逐篇来源的抽象规则，重写为完全原创的经济学写作 skills。

## Attribution, License, And Ethical Use / 引用、许可与伦理使用 ⚖️

### English

The `skills/econ-write/` skill includes content based on [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) by Lu Han, licensed under the MIT License. See [`NOTICE.md`](NOTICE.md) for the preserved third-party copyright and license notice.

Original repository content is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0), unless otherwise stated. Commercial use of original repository content requires separate written permission. Third-party materials remain subject to their own notices and licenses, as described in [`NOTICE.md`](NOTICE.md).

This repository is intended for non-commercial academic writing support. Do not use it for paid paper-writing services, ghostwriting, academic misconduct services, or fabricated research materials. See [`ETHICAL_USE.md`](ETHICAL_USE.md).

Full-draft workflows are for author-responsible drafting and revision of legitimate research. They must not be used as an automatic paper-writing or submission service.

Because the original repository content uses a NonCommercial license, this repository is not distributed as an OSI-approved open-source project.

### 中文

`skills/econ-write/` 包含基于 Lu Han 的 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) 的内容，原项目采用 MIT License。第三方版权与许可声明已保存在 [`NOTICE.md`](NOTICE.md)。

除非另有说明，本仓库原创内容采用 Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)。原创内容的商业使用需要另行取得书面许可。第三方内容仍以其各自声明和许可为准，见 [`NOTICE.md`](NOTICE.md)。

本仓库用于非商用学术写作辅助。不得用于付费论文代写、ghostwriting、学术不端服务或伪造研究材料。见 [`ETHICAL_USE.md`](ETHICAL_USE.md)。

完整初稿 workflow 只用于作者负责的合法研究写作与修稿，不得作为自动论文代写或自动投稿服务使用。

由于原创内容采用 NonCommercial 许可，本仓库不以 OSI 认可的开源项目形式发布。

## AI Assistance / AI 辅助说明 🤖

### English

ChatGPT and Codex were used to help organize the repository, draft documentation, review attribution, and prepare Git commits. They are not listed as authors or maintainers because responsibility for the repository, licensing choices, and final content remains with the human maintainer.

See [`docs/ai-assistance.md`](docs/ai-assistance.md) for details.

### 中文

本仓库在整理目录、撰写说明、检查引用和准备 Git 提交时使用了 ChatGPT 与 Codex 辅助。它们不列为作者或维护者；仓库内容、许可选择和后续维护责任仍由人类维护者承担。

详情见 [`docs/ai-assistance.md`](docs/ai-assistance.md)。
