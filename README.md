# Economics Writing Skills / 经济学写作技能

This Codex workflow supports economics writing in English and Chinese: outlines, full drafts, revisions, tables and figures, and manuscript review. It combines writing instructions and reference modules with multi-agent review and an executable Python pipeline for preparing reviews and checking their coverage, citations, and file versions.

**AI can assist research and writing, but key academic judgments remain with human researchers.** You provide the research question, evidence, and intended argument, and decide which changes to accept.

这套 Codex 写作流程支持经济学论文的大纲、全文起草、修改、图表制作和稿件审阅，兼顾中文和英文写作。仓库既有写作规则和分项参考模块，也有多 agent 审阅流程与可执行的 Python 管线，用于准备审阅材料，检查审阅覆盖、引文和文件版本是否一致。

**AI 写作只能辅助研究和成文过程，关键学术判断依然离不开人类研究者。** 研究问题、证据解释和论文主张由作者确定，agent 按要求协助写作，修改结果仍须由作者判断和确认。

## What It Does / 主要功能

### English

- **Outlines and research plans.** Organize paper or book arguments and turn an agreed framework into assignments for collaborators: what to read, what to explain, and which tables or figures to make. Research-proposal guidance also covers feasibility, stages, risks, and expected outputs.
- **English and Chinese writing.** Draft and revise abstracts, introductions, literature reviews, theory, results, conclusions, and referee responses. Review sentence structure, terminology, awkward phrasing, and literal translations.
- **Arguments and interpretation.** Check how the question, contribution, reasoning, and evidence fit together. Distinguish descriptive findings, causal estimates, mechanisms, and heterogeneity; explain the economic size of results using suitable comparisons.
- **Literature and citations.** Work from inspected papers and source notes, check which claims each source supports, and reconcile in-text citations with the literature records and bibliography.
- **Tables and figures.** Use the dedicated `econ-table-figure-design` skill to plan and produce three-line tables, main regressions, robustness, heterogeneity, and mechanism tables, as well as event-study, trend, binscatter, map, distribution, and mechanism figures. It covers main-text versus appendix placement, columns and panels, titles, notes, axes, legends, fonts, palettes, grayscale printing, and export quality. The agent must inspect the rendered output.
- **Journal and document conventions.** Apply the relevant Chinese journal guidance, including submission and anonymity checks, heading structure, references, and appendix placement, with guidance for LaTeX and Word-based work.
- **Long manuscripts and revision control.** Coordinate section and review tasks, preserve the author's intended meaning, track changes to established content, and distinguish draft results, approved versions, and material inserted into the manuscript. Substantive rewriting and manuscript insertion follow the author's approval.

### 中文

- **大纲与研究计划。** 梳理论文或书稿的论证，把已确定的框架整理成合作者可以执行的写作任务，明确读什么、写什么、制作哪些图表。研究建议书另有可行性、阶段安排、风险和预期成果方面的指导。
- **中英文写作。** 起草和修改摘要、引言、文献综述、理论、结果、结论及审稿回复，检查句式、术语、生硬表达和翻译腔。
- **论证与结果解释。** 检查研究问题、贡献、推理和证据能否衔接，区分描述性发现、因果估计、机制和异质性，并选择合适的参照解释结果的经济量级。
- **文献与引用。** 根据实际阅读的论文和资料判断文献能支持哪些主张，核对正文引文、文献记录与最终参考文献表。
- **制表与绘图。** 独立的 `econ-table-figure-design` 子模块指导 agent 设计和制作三线表、主回归表、稳健性表、异质性表、机制表，以及事件研究图、趋势图、分箱散点图、地图、分布图和机制图。它还处理正文与附录的安排、列和分面、标题、注释、坐标轴、图例、字体、配色、黑白打印和导出质量；agent 须检查实际生成的表格或图形。
- **期刊与文档格式。** 按适用的中文期刊要求检查投稿体例、匿名处理、标题层级、参考文献和附录安排，并提供 LaTeX 与 Word 文档处理方面的指导。
- **长文协作与版本管理。** 分配章节写作和审阅任务，检查作者原意是否保留，记录既有内容的增删，并区分候选结果、已确认版本和已经写入稿件的内容。实质改写和稿件整合须遵循作者的授权。

## Python Pipeline And Review / Python 管线与审阅

### English

For a full paper, a complete proposal, a document-level translation or compression, or a major revision, the workflow combines agent review with Python checks:

1. The author confirms the intended argument and the scope of the work; the agent drafts or revises from the supplied evidence.
2. `prepare_manuscript_qa.py` reads the manuscript, enumerates the text to review, and builds review packets with context and file hashes.
3. Independent agents review meaning, evidence, definitions, and economic reasoning. They return structured findings for the coordinating agent to address.
4. Python validators check whether the required reviews are complete, refer to the current files, and agree with the recorded decisions. Citation, content-preservation, literature-review, and figure-label checks cover their respective parts.
5. The agent revises the affected passages and obtains the required re-review. The author reviews the resulting manuscript and unresolved decisions.

The repository contains six Python programs and six accompanying test files. The Python code handles reproducible checks; agents assess meaning and evidence, and the author makes the academic decisions. The manuscript preparation and conservation tools accept UTF-8 `.tex`, `.md`, and `.txt` sources. Figure labels and rendered-output reviews have their own records.

The multi-agent component, `econ-writing-workflow-multiagent`, requires an agent environment that supports independent reviewers. Short polishing tasks and outline-only requests use lighter checks rather than the complete-manuscript process.

### 中文

完整论文、完整研究建议书、整篇翻译或压缩，以及重大修改，会结合 agent 审阅和 Python 程序检查：

1. 作者确认论文要表达的内容和本次任务范围，agent 根据已有证据起草或修改。
2. `prepare_manuscript_qa.py` 读取稿件，列出需要审阅的文字，生成包含上下文和文件校验值的审阅包。
3. 独立的 agent 分别检查原意、证据、定义和经济推理，返回明确的问题记录，由负责整合的 agent 处理。
4. Python 验证程序检查审阅是否覆盖应审内容、是否对应当前文件、是否与已记录的决定一致。引文、原有内容保留、文献审阅和图表标签另有相应检查。
5. agent 修改受影响的文字并完成必要的复审，再将稿件和待决定的问题交给作者。

仓库包含六个 Python 程序和六个配套测试文件。Python 负责可以重复核验的项目，agent 负责理解文字和判断证据，作者负责学术决定。稿件准备和内容保留检查支持 UTF-8 编码的 `.tex`、`.md` 和 `.txt` 文件；图表标签及最终画面的审查使用单独的记录。

多 agent 模块 `econ-writing-workflow-multiagent` 需要运行环境支持独立审阅 agent。短段落润色和只交付大纲的任务使用相应的轻量检查，不套用完整稿件流程。

### Programs / 程序清单

| Program / 程序 | What it checks / 作用 |
| --- | --- |
| [`prepare_manuscript_qa.py`](skills/econ-writing-workflow-multiagent/scripts/prepare_manuscript_qa.py) | Builds the manuscript inventory and review packets / 生成稿件清单和审阅包。 |
| [`validate_manuscript_qa.py`](skills/econ-writing-workflow-multiagent/scripts/validate_manuscript_qa.py) | Checks review coverage, current file versions, findings, and required re-reviews / 核对审阅覆盖、文件版本、问题处理和复审记录。 |
| [`audit_manuscript_conservation.py`](skills/econ-writing-workflow-multiagent/scripts/audit_manuscript_conservation.py) | Measures length and tracked content changes against the agreed revision limits / 按已约定的修改范围检查篇幅和内容变化。 |
| [`audit_citation_integrity.py`](skills/econ-writing-workflow-multiagent/scripts/audit_citation_integrity.py) | Reconciles citations, literature records, and bibliography / 核对引文、文献记录和参考文献表。 |
| [`validate_literature_audit.py`](skills/econ-writing-workflow-multiagent/scripts/validate_literature_audit.py) | Validates the independent literature-review assignment and result / 验证独立文献审阅的任务与结果记录。 |
| [`audit_reader_facing_labels.py`](skills/econ-table-figure-design/scripts/audit_reader_facing_labels.py) | Checks label coverage, numeric preservation, bilingual pairing, and semantic/render-review records / 检查图表标签覆盖、数值保留、中英对应及语义和画面审查记录。 |

## Model Choice / 模型选择

### English

For important writing and substantial revisions, choose the latest, most advanced models, such as [GPT-6.1 Sol or GPT-6 Astra](https://developers.openai.com/api/docs/models) and [Claude Opus 5.5 or Claude Fable 5.1](https://platform.claude.com/docs/en/models/overview).

For Chinese wording and sentence-level revision, you can also try DeepSeek or Kimi, then compare the revision with the original to check that the meaning is intact. Use each model in a service that supports it. Current model lineups are listed by [OpenAI](https://developers.openai.com/api/docs/models) and [Anthropic](https://platform.claude.com/docs/en/models/overview).

### 中文

重要写作和较大幅度的修改，建议使用最新、最先进的模型，例如 [GPT-6.1 Sol、GPT-6 Astra](https://developers.openai.com/api/docs/models)、[Claude Opus 5.5 或 Claude Fable 5.1](https://platform.claude.com/docs/en/models/overview)。

中文措辞和句式润色，也可以使用 DeepSeek 或 Kimi，再对照原文检查含义是否保留。请在支持相应模型的平台上使用。当前型号可查阅 [OpenAI](https://developers.openai.com/api/docs/models) 和 [Anthropic](https://platform.claude.com/docs/en/models/overview) 的官方列表。

## Install Locally / 本地安装

### English

#### Ask the agent to install

Send this request in a Codex conversation:

```text
Please download and install the writing skills from this repository:
https://github.com/juliaError/econ-TopJournal-writing-Skill

Install these five folders: skills/econ-writing-workflow, skills/econ-write,
skills/cn-top-econ-writing, skills/econ-table-figure-design, and
skills/econ-writing-workflow-multiagent (including its references and scripts).
First check which skills directory my version of Codex reads. If skills with
the same names are already installed, compare the versions and ask before
replacing them. After installation, check that Codex can find the skills and
tell me whether I need to restart it.
```

The agent downloads the files, checks the installation path, and copies the skills. You do not need to run the commands below if the agent completes the installation.

#### Install manually

If your Codex installation reads skills from `~/.codex/skills/`, clone or download the repository, open a terminal in its root directory, and run the following commands. These commands are for a first installation; if the destination folders already exist, compare them before copying. If your Codex version uses a different directory, use the installation request above to have the agent check it.

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-writing-workflow ~/.codex/skills/econ-writing-workflow
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
cp -R skills/econ-table-figure-design ~/.codex/skills/econ-table-figure-design
cp -R skills/econ-writing-workflow-multiagent ~/.codex/skills/econ-writing-workflow-multiagent
```

The audit scripts require Python 3 and use its standard library. The multi-agent skill is used for complete-manuscript review; install its reference files and scripts together. The agent runs the relevant checks as part of the writing task.

If the skills do not appear after installation, restart Codex and ask it to check again.

### 中文

#### 让 agent 安装

在 Codex 对话中发送下面这段话：

```text
请下载并安装这个仓库中的写作技能：
https://github.com/juliaError/econ-TopJournal-writing-Skill

需要安装五个目录：skills/econ-writing-workflow、skills/econ-write、
skills/cn-top-econ-writing、skills/econ-table-figure-design，以及
skills/econ-writing-workflow-multiagent（连同其 references 和 scripts）。
请先确认当前 Codex 版本读取哪个技能目录。如果已经安装同名技能，先比较版本，
征得我同意后再替换。安装后，检查 Codex 能否找到这些技能，并告诉我是否需要重启。
```

下载文件、核对安装路径和复制技能由 agent 完成。它安装成功后，你不需要再执行下面的命令。

#### 手动安装

如果你的 Codex 从 `~/.codex/skills/` 读取技能，可以先克隆或下载仓库，在仓库根目录打开终端，再执行以下命令。这组命令适用于首次安装；目标目录已经存在时，应先比较内容再复制。如果当前版本使用其他目录，可以用上面的安装请求让 agent 核对。

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-writing-workflow ~/.codex/skills/econ-writing-workflow
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
cp -R skills/econ-table-figure-design ~/.codex/skills/econ-table-figure-design
cp -R skills/econ-writing-workflow-multiagent ~/.codex/skills/econ-writing-workflow-multiagent
```

检查脚本需要 Python 3，使用 Python 标准库。多 agent 技能用于完整稿件审阅，安装时应保留其中的参考文件和脚本，由 agent 在写作任务中调用相应检查。

安装后如果仍未显示这些技能，请重启 Codex，再让 agent 检查。

## Usage / 如何使用

### English

After installation, describe your writing task in a Codex conversation and ask the agent to use `econ-writing-workflow`. For example:

```text
Please use econ-writing-workflow to revise this paper's introduction.
Focus on whether the research question and contribution are clear.
```

The agent reads the workflow instructions and selects the English-writing, Chinese-writing, or table-and-figure skill needed for your task. You do not need to select each of these skills yourself. Codex can also choose a skill from the task description; naming it explicitly tells the agent to use this collection. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills).

Give the agent the relevant draft, tables, figures, or source materials, along with the parts you want changed and the parts you want preserved. Here are two further examples.

**Prepare an outline for collaborators**

```text
Please use econ-writing-workflow to turn this agreed book outline into
writing assignments for my collaborators. Keep the headings and structure.
For each section, explain what to read, which argument to develop, and which
tables or figures we have agreed to make. Prepare the outline only, not the
chapters or figures. Ask me about any substantive choices that remain open.
```

**Draft from completed research**

```text
Please use econ-writing-workflow to help draft a Chinese economics paper
from these research notes, results, and figures. First read the materials and
confirm with me what the paper should argue. Then draft within that scope.
List missing information separately. If a gap affects the meaning or support
for a claim, ask me before writing that part.
```

For a specific task, you can name a specialized skill directly: `econ-write` for English prose, `cn-top-econ-writing` for Chinese prose, or `econ-table-figure-design` for tables and figures. For example: “Use econ-table-figure-design to check the column layout and notes in these regression tables.”

These are writing skills. Data cleaning, variable construction, regression estimation, and reproducible empirical execution require a separate empirical workflow.

### 中文

安装完成后，在 Codex 对话中说明你的写作任务，并指定使用 `econ-writing-workflow`。例如：

```text
请使用 econ-writing-workflow，帮我修改这篇论文的引言，
重点检查研究问题和贡献是否说清楚。
```

agent 收到请求后，会读取技能说明，再根据任务使用英文写作、中文写作或表图技能。你不需要逐个选择和调用这些技能。不写技能名时，Codex 也可以根据任务自动选择；明确点名，是为了指定使用本仓库的这套写作流程。调用方式见 [Codex 官方文档](https://learn.chatgpt.com/docs/build-skills#how-chatgpt-and-codex-use-skills)。

请同时提供相关稿件、表格、图形或参考材料，并说明哪些地方要改、哪些内容要保留。下面是另外两种常见用法。

**给合作者整理写作任务**

```text
请使用 econ-writing-workflow，把这份已确定的书稿大纲整理成合作者可以
照着写的任务安排。保留现有标题和结构，逐节说明读什么材料、展开哪些论证，
以及制作哪些已经约定的图表。本次只整理大纲，不写章节正文，也不制作图表。
尚未确定的实质问题，请先问我。
```

**根据已有研究起草论文**

```text
请使用 econ-writing-workflow，根据这些研究说明、结果和图表，协助起草
一篇中文经济学论文。先阅读材料，与我确认论文要表达的主要观点，再按确认的
范围写作。缺少的信息单独列出；如果缺口影响论点的含义或依据，先问我再写。
```

任务比较具体时，也可以直接点名：英文修改用 `econ-write`，中文修改用 `cn-top-econ-writing`，表格和图形检查用 `econ-table-figure-design`。例如：“请使用 econ-table-figure-design，检查这些回归表的列安排和表注。”

这套技能负责写作。数据清洗、变量构造、回归估计和可复现实证执行，需要另外使用实证工作流。

## Sources / 内容来源

### English

`econ-write` includes work based on Lu Han's [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill), which is licensed under MIT. The original copyright and license notice is preserved in [`NOTICE.md`](NOTICE.md).

Other writing and table-and-figure guidance draws on a locally maintained collection of papers from AER, QJE, JPE, Econometrica, REStud, and Chinese journals including *Economic Research Journal*, *Management World*, and *China Industrial Economics*. The public files describe general writing practices rather than reproduce the papers. The article list is not published, out of concern that authors may not wish their papers to be identified as sources for these rules. See the [corpus policy](docs/paper-corpus.md).

### 中文

`econ-write` 包含基于 Lu Han 的开源项目 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) 的内容。原项目采用 MIT 许可，版权和许可声明保存在 [`NOTICE.md`](NOTICE.md)。

其他写作和表图规则参考了本地整理的经济学论文，包括 AER、QJE、JPE、Econometrica、REStud，以及《经济研究》《管理世界》《中国工业经济》等中文期刊。公开文件总结写作方法，不转载论文内容。考虑到论文作者可能不愿被列为这些规则的提炼来源，目前不公开具体论文清单。详见[语料使用政策](docs/paper-corpus.md)。

## Current Status / 当前状态

### English

The repository includes four writing/design skills and the `econ-writing-workflow-multiagent` module. Some files in `paper_skills` remain placeholders. Further development will replace inherited writing guidance with original rules while preserving the required attribution for retained third-party material.

<details>
<summary>Update history</summary>

- **2026-10-09** — Added argument outlines and writing assignments for collaborators. The agent preserves agreed headings, gives each claim a main location, and specifies the reading, reasoning, and agreed table or figure work for each section. An outline or proposal skeleton is checked as an outline; full-draft review and rendered-figure checks apply when those finished outputs are requested.
- **2026-07-18** — Added three research-planning references covering scope and claims, theory and empirical support, and proposal feasibility and revision decisions. The agent selects checks for the task at hand rather than turning exploration or a local edit into a full-paper audit. The references distinguish preliminary from established findings, check model and measurement definitions, connect theory to data, examine the conditions behind policy recommendations, and ask when a revision is finished. Suggested paragraph counts, result counts, and model complexity vary with the paper; working checklists stay outside the manuscript. Removed unsupported `argument-hint` and `user-invocable` fields from `econ-write` without changing its instructions or invocation behavior; source and installed copies passed validation.
- **2026-05-17** — Added guidance for explaining the economic size of estimates in English and Chinese. It covers coefficients, marginal effects, interactions, log conversions, and comparisons with relevant means, standard deviations, percentiles, or policy changes. The agent chooses a meaningful comparison rather than applying every benchmark, and must not invent descriptive statistics.
- **2026-05-16** — Added checks to keep editing notes and internal labels out of paper text, notes, appendices, and footnotes. Unclear research facts or substantive choices must be raised with the author rather than guessed. The workflow now rechecks which skill is needed as a task changes. Drawn or edited figures and maps require inspection of the final output for obscured content, overlapping text, and unreadable labels.
- **2026-05-15** — Added an optional project-level reminder to use the relevant writing skills throughout a longer task. Before adding it to local `AGENTS.md` or `CLAUDE.md` files, the agent asks for permission. The Chinese-writing and table-and-figure skills also refer longer tasks back to this setup.
- **2026-05-14** — Added Chinese argument-review guidance for the paper's central argument, contribution, section order, theory, results, supporting analyses, and use of tables and figures. It draws on economic reasoning without copying English syntax. The agent checks structure and retained content before polishing Chinese wording.
- **2026-05-13** — Added English prose guidance for sentence purpose, verbs, abstracts, introductions, theory and empirical writing, and awkward or formulaic phrasing. Added the bilingual table-and-figure skill, whole-paper argument review, and a process for drafting from the author's research materials. That process checks the inputs, places tables and figures, and separates missing information from supported claims.

</details>

### 中文

仓库包含四个写作与表图技能，以及 `econ-writing-workflow-multiagent` 模块；`paper_skills` 中部分参考文件仍是占位内容。后续会继续用原创规则替换借鉴的写作指导，保留仍在使用的第三方内容所需的署名和许可声明。

<details>
<summary>查看更新记录</summary>

- **2026-10-09** — 新增论证大纲和面向合作者的写作任务安排。agent 保留已确定的标题，为各项主张安排主要论述位置，并逐节说明阅读材料、推理步骤和已约定的图表任务。大纲和研究建议书骨架按大纲检查；要求交付完整稿件或实际图形时，再做相应验收。
- **2026-07-18** — 新增三个研究规划参考文件，分别处理研究范围与主张、理论和实证依据，以及研究建议书的可行性和修改安排。agent 按当前任务选择检查内容，不把探索或局部修改扩大为全文审查。规则区分初步结果与已有结论，检查模型和测量定义、理论与数据的对应关系、政策建议成立的条件，以及何时可以结束修改。段数、结果数量和模型复杂度建议随论文类型调整，工作清单不写进正文。同时删除 `econ-write` 中不受支持的 `argument-hint`、`user-invocable` 字段，技能正文和调用方式未变，源文件与安装副本均通过校验。
- **2026-05-17** — 新增中英文共用的经济量级解释指导，涵盖系数、边际效应、交互项、对数换算，以及与均值、标准差、分位差或政策变化的比较。agent 应选择有经济含义的参照，不机械套用所有指标，也不编造描述统计。
- **2026-05-16** — 新增检查，避免把修改备忘和内部标签写进正文、表注、图注、附录或脚注。研究事实或实质选择不清楚时，应向作者提出，而不是猜测。写作任务转入其他环节时，agent 会重新判断应使用的技能；绘制或修改图形、地图后，须检查实际输出，确认内容没有被遮挡、文字没有重叠、标签可以辨认。
- **2026-05-15** — 新增可选的项目级提醒，让 agent 在长任务中持续使用相关写作技能。写入本地 `AGENTS.md` 或 `CLAUDE.md` 前，agent 必须取得许可。中文写作和表图技能也会在长任务中提示使用这项设置。
- **2026-05-14** — 新增中文论证检查，涵盖全文主线、贡献、章节顺序、理论、结果、补充分析和表图安排。参考经济学论证方法，不照搬英文句法。agent 先检查结构和必要内容是否保留，再修改中文表达。
- **2026-05-13** — 新增英文表达指导，处理句子作用、动词搭配、摘要、引言、理论和实证写作，以及生硬或套路化表达。同时加入中英文表图技能、全文论证检查，以及根据作者研究材料起草论文的步骤，包括检查输入、安排正文与附录表图、区分缺失信息和已有依据。

</details>

## What Is Inside / 仓库内容

### English

The five skill directories include the entry point, three specialist writing/design skills, and a multi-agent coordinator. Reference files hold the detailed guidance; `scripts/` directories hold the executable Python checks and their tests.

| Path | Contents |
| --- | --- |
| [`skills/econ-writing-workflow/`](skills/econ-writing-workflow/) | Main entry point; argument and task outlines, author-intent preservation, full drafting, literature use, research planning, economic-magnitude interpretation, and version/approval procedures. |
| [`skills/econ-write/`](skills/econ-write/) | English economics writing and revision, diction, section guidance, identification discussion, LaTeX tips, and review checklists. |
| [`skills/econ-write/references/paper_skills/`](skills/econ-write/references/paper_skills/) | Section-specific references; some remain under development. |
| [`skills/cn-top-econ-writing/`](skills/cn-top-econ-writing/) | Chinese economics prose, argument review, wording, and journal conventions. |
| [`skills/econ-table-figure-design/`](skills/econ-table-figure-design/) | Table and figure design, labels, visual style, and export checks. |
| [`skills/econ-table-figure-design/scripts/`](skills/econ-table-figure-design/scripts/) | Python label-audit program and its tests. |
| [`skills/econ-writing-workflow-multiagent/`](skills/econ-writing-workflow-multiagent/) | Coordination of long writing tasks, independent reviewers, shared research facts, handoffs, and revisions. |
| [`skills/econ-writing-workflow-multiagent/scripts/`](skills/econ-writing-workflow-multiagent/scripts/) | Five Python preparation/validation programs for manuscript, citation, and literature review, plus their tests. |
| [`docs/paper-corpus.md`](docs/paper-corpus.md) | Policy for using the local paper collection without publishing source texts or article lists. |
| [`LICENSE`](LICENSE) | License for original repository content. |
| [`NOTICE.md`](NOTICE.md) | Third-party copyright and license notices. |
| [`ETHICAL_USE.md`](ETHICAL_USE.md) | Academic and non-commercial use requirements. |
| [`docs/ai-assistance.md`](docs/ai-assistance.md) | How AI assisted development and who is responsible for the repository. |

### 中文

五个技能目录分别是写作总入口、三个专业写作与表图技能，以及多 agent 协作模块。具体规则放在参考文件中；`scripts/` 目录存放可执行的 Python 检查程序及测试。

| 路径 | 内容 |
| --- | --- |
| [`skills/econ-writing-workflow/`](skills/econ-writing-workflow/) | 写作总入口，包含论证与任务大纲、作者原意保留、全文起草、文献使用、研究规划、经济量级解释，以及版本和授权安排。 |
| [`skills/econ-write/`](skills/econ-write/) | 英文经济学写作与修改、遣词造句、章节指导、识别策略讨论、LaTeX 提示和审阅清单。 |
| [`skills/econ-write/references/paper_skills/`](skills/econ-write/references/paper_skills/) | 分章节参考规则；部分仍在开发。 |
| [`skills/cn-top-econ-writing/`](skills/cn-top-econ-writing/) | 中文经济学论文表达、论证检查、遣词造句和期刊体例。 |
| [`skills/econ-table-figure-design/`](skills/econ-table-figure-design/) | 表格与图形设计、标签、视觉样式和导出检查。 |
| [`skills/econ-table-figure-design/scripts/`](skills/econ-table-figure-design/scripts/) | 图表标签 Python 检查程序及测试。 |
| [`skills/econ-writing-workflow-multiagent/`](skills/econ-writing-workflow-multiagent/) | 长文写作、独立审阅、共享研究事实、任务交接和修改整合的多 agent 模块。 |
| [`skills/econ-writing-workflow-multiagent/scripts/`](skills/econ-writing-workflow-multiagent/scripts/) | 稿件、引文和文献审阅所用的五个 Python 准备与验证程序，以及配套测试。 |
| [`docs/paper-corpus.md`](docs/paper-corpus.md) | 本地论文语料的使用政策，说明为何不公开原文和具体论文清单。 |
| [`LICENSE`](LICENSE) | 仓库原创内容的许可说明。 |
| [`NOTICE.md`](NOTICE.md) | 第三方版权与许可声明。 |
| [`ETHICAL_USE.md`](ETHICAL_USE.md) | 学术使用和非商用要求。 |
| [`docs/ai-assistance.md`](docs/ai-assistance.md) | AI 参与开发的方式，以及仓库责任归属。 |

## License And Use / 许可与使用要求

### English

Unless otherwise stated, original repository content is licensed under **CC BY-NC 4.0**. Commercial use requires separate written permission. Third-party material keeps its own license, including the MIT-licensed material used in `econ-write`; it is not relicensed as non-commercial-only content. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).

The skills are intended for non-commercial academic writing, teaching, and revision. Do not use them for paid paper-writing, undisclosed ghostwriting, academic misconduct, fabricated research, or an automatic paper-writing or submission service. Authors remain responsible for accuracy, citations, disclosure, and compliance with their institution's or journal's rules. See [`ETHICAL_USE.md`](ETHICAL_USE.md).

Because the original content has a non-commercial restriction, this repository is not an OSI-approved open-source project.

### 中文

除另有说明外，本仓库原创内容采用 **CC BY-NC 4.0** 许可，商业使用须另行取得书面许可。第三方内容保留原许可；例如 `econ-write` 使用的 MIT 许可内容，不因收入本仓库而变为仅限非商用。详见 [`LICENSE`](LICENSE) 和 [`NOTICE.md`](NOTICE.md)。

这些技能用于非商用学术写作、教学和修稿，不得用于付费论文代写、隐瞒实际作者身份的代写、学术不端、伪造研究，或自动论文代写和投稿服务。作者负责核对内容、引用和披露要求，并遵守所在机构及期刊的规定。详见 [`ETHICAL_USE.md`](ETHICAL_USE.md)。

由于原创内容有非商用限制，本仓库不属于 OSI 认可的开源项目。

## AI Assistance / AI 辅助说明

ChatGPT and Codex assisted with repository organization, documentation, attribution checks, and Git operations. They are not authors or maintainers; the human maintainer is responsible for the content, licensing decisions, and maintenance. See [`docs/ai-assistance.md`](docs/ai-assistance.md).

本仓库使用 ChatGPT 和 Codex 协助整理目录、撰写说明、检查来源署名和执行 Git 操作。它们不列为作者或维护者；内容、许可决定和后续维护由维护者负责。详见 [AI 辅助说明](docs/ai-assistance.md)。
