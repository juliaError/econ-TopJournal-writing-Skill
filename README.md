# Economics Top-Journal Writing Skills / 经济学顶刊写作 Skills ✨

This repository collects Codex skills for economics paper writing, revision, and top-journal style checking.

本仓库用于整理经济学论文写作、修改、投稿前审查和中文顶刊风格适配的 Codex skills。它目前采用“总入口 workflow skill + 可独立调用的专业子 skill”的结构。

## What Is Inside / 仓库内容 🧭

| Path | English | 中文说明 |
| --- | --- | --- |
| `skills/econ-writing-workflow/` | Main entry skill that routes economics writing tasks to the relevant English, Chinese, or table/figure module, and points empirical work to the empirical workflow. | 普通用户主要调用的写作总入口 skill，负责把经济学写作任务路由到英文、中文或表图模块；涉及实证工作时提示搭配实证 workflow。 |
| `skills/econ-write/` | General economics paper writing skill for abstracts, introductions, literature reviews, theory sections, empirical sections, tables, robustness, LaTeX, and revision. | 通用英文经济学论文写作 skill，覆盖摘要、引言、文献、理论、实证、表图、稳健性、LaTeX 和修改审查。 |
| `skills/econ-write/references/paper_skills/` | Optional section-specific reference modules loaded by `econ-write` when relevant. | 后续用于细分写作规则的模块化参考文件，目前部分内容仍是占位。 |
| `skills/cn-top-econ-writing/` | Chinese top-journal economics writing skill for journals such as 《经济研究》, 《管理世界》, and 《中国工业经济》. | 面向《经济研究》《管理世界》《中国工业经济》等中文顶刊的写作、审查和修稿 skill。 |
| `skills/econ-table-figure-design/` | Bilingual economics table and figure design skill for regression tables, robustness, heterogeneity, mechanisms, notes, captions, palettes, and export checks. | 中英文通用经济学表格与图形设计 skill，覆盖三线表、主回归、稳健性、异质性、机制、表注图注、配色和导出检查。 |
| `docs/paper-corpus.md` | Corpus policy for how local writing-learning sources are used without publishing paper lists or source text. | 语料使用政策，说明如何使用本地写作学习来源，同时不公开论文清单或来源文本。 |
| `LICENSE` | Layered license overview: original repository content is CC BY-NC 4.0; third-party content keeps its own license. | 分层许可说明：本仓库原创内容采用 CC BY-NC 4.0；第三方内容保留原许可。 |
| `NOTICE.md` | Third-party copyright and MIT License notice. | 外部来源与 MIT License 声明。 |
| `ETHICAL_USE.md` | Ethical-use policy for non-commercial academic writing support. | 非商用学术写作辅助的伦理使用说明。 |
| `docs/ai-assistance.md` | Notes on AI-assisted development and responsibility. | 关于 AI 辅助开发、署名和责任边界的说明。 |

## Knowledge Sources / 知识来源 📚

This repository currently has two kinds of sources:

1. **Third-party skill source**: `skills/econ-write/` is based on the open-source [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) project by Lu Han, licensed under the MIT License.
2. **Curated local corpus**: the modular writing and table/figure workflows are informed by a private, locally maintained economics writing-learning corpus. Public files contain only abstracted rules, original examples, and reusable workflows.

本仓库目前有两类来源：

1. **外部 skill 来源**：`skills/econ-write/` 基于 Lu Han 的开源项目 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill)，许可证为 MIT License。
2. **本地整理语料**：模块化写作和表图 workflow 由私人、本地维护的经济学写作学习语料启发。公开文件只包含抽象规则、原创例句和可复用工作流。

See [`docs/paper-corpus.md`](docs/paper-corpus.md) for the corpus-use policy.

语料使用政策见 [`docs/paper-corpus.md`](docs/paper-corpus.md)。

## Install Locally / 本地安装 🚀

Copy the skill directories into your Codex skills folder:

将本仓库中的全部 skill 目录复制到 Codex skills 文件夹：

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-writing-workflow ~/.codex/skills/econ-writing-workflow
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
cp -R skills/econ-table-figure-design ~/.codex/skills/econ-table-figure-design
```

Restart or refresh Codex after installation so the skills list is reloaded.

安装后重启或刷新 Codex，让 skills 列表重新加载。

You can also copy the repository webpage URL and ask an AI agent to help download and set up the skills for you.

你也可以直接复制这个仓库网页链接，让 AI agent 帮你下载并完成安装设置。

Short prompt for an AI agent:

给 AI agent 的简短 prompt：

```text
Please help me download and install the Codex skills from this repository:
https://github.com/juliaError/econ-TopJournal-writing-Skill

Copy `skills/econ-writing-workflow`, `skills/econ-write`, `skills/cn-top-econ-writing`, and `skills/econ-table-figure-design` into `~/.codex/skills/`, then tell me whether I still need to refresh or restart Codex.
```

```text
请帮我下载并安装这个仓库里的 Codex skills：
https://github.com/juliaError/econ-TopJournal-writing-Skill

把 `skills/econ-writing-workflow`、`skills/econ-write`、`skills/cn-top-econ-writing` 和 `skills/econ-table-figure-design` 复制到 `~/.codex/skills/`，然后告诉我是否还需要刷新或重启 Codex。
```

## Usage / 使用方式 🛠️

For most users, call `econ-writing-workflow` first. It will route the writing task to the right module:

普通用户日常优先调用 `econ-writing-workflow`。它会根据写作任务类型自动转向合适的模块：

```text
Use econ-writing-workflow to revise this paper's introduction, tables, and Chinese abstract.
```

```text
用 econ-writing-workflow 检查这篇经济学论文的引言、主回归表和中文表达。
```

Advanced users may call specialized skills directly:

高级用户也可以直接调用专业子 skill：

Use `econ-write` for general English economics paper writing:

一般英文经济学论文写作可以使用 `econ-write`：

```text
Use econ-write to revise this introduction.
```

Use `cn-top-econ-writing` for Chinese top-journal submissions:

中文顶刊投稿、修改和预审可以使用 `cn-top-econ-writing`：

```text
用 cn-top-econ-writing 审查这篇中文经济学论文的引言和贡献表述。
```

Use `econ-table-figure-design` when the task is about tables, figures, notes, palettes, or main-text versus appendix placement:

涉及表格、图形、表注、图注、配色、正文/附录取舍时，可以使用 `econ-table-figure-design`：

```text
Use econ-table-figure-design to decide which regression tables and figures should enter the main text, how many columns each table should have, and what the notes should include.
```

```text
用 econ-table-figure-design 检查这组主回归、稳健性、机制和异质性表，并给出正文表、附录表和配色方案。
```

For empirical coding, data cleaning, or regressions, pair these writing skills with a separate empirical workflow skill.

如果任务涉及数据清洗、变量构造或回归代码，应搭配单独的实证工作流 skill，而不是只靠写作 skill。

## Current Status / 当前状态 🌱

- `econ-write` is usable now and keeps its third-party MIT notice.
- **2026-05-13 update**: `econ-write` now includes `references/english-diction/`, an English top-journal prose module for sentence functions, verbs/collocations, abstract and introduction patterns, theory-versus-empirical prose, and AI/translationese revision checks.
- **2026-05-13 update**: `econ-table-figure-design` is now added as a bilingual table/figure design skill for main regression tables, robustness, heterogeneity, mechanisms, notes, captions, palettes, typography, and export checks.
- **2026-05-13 update**: `econ-writing-workflow` now includes `references/argument-logic/` for full-paper logic, repeated material, emphasis, ordering, and table/figure fit.
- `cn-top-econ-writing` is a standalone Chinese top-journal writing skill.
- `paper_skills` reference files are still being developed. Some files are placeholders until their detailed rule bodies are filled in.
- The long-term goal is to gradually rewrite the workflow into fully original economics writing skills based on local writing rules and non-source-specific abstractions.

- `econ-write` 当前可直接使用，并已保留第三方 MIT 声明。
- **2026-05-13 更新**：`econ-write` 已新增 `references/english-diction/` 英文顶刊遣词造句模块，覆盖句子功能、动词搭配、摘要与引言句法、理论/实证 prose 差异，以及 AI 腔/翻译腔修稿检查。
- **2026-05-13 更新**：新增 `econ-table-figure-design` 中英文通用表图设计 skill，覆盖主回归表、稳健性、异质性、机制、表注图注、配色、字体字号和导出检查。
- **2026-05-13 更新**：`econ-writing-workflow` 已新增 `references/argument-logic/`，用于全文逻辑、重复删除、重点排序和表图是否服务主线的审查。
- `cn-top-econ-writing` 是独立的中文顶刊写作 skill。
- `paper_skills` 参考文件仍在开发中，部分文件目前仍是占位。
- 长期目标是逐步基于本地写作规则和非逐篇来源的抽象规则，重写为完全原创的经济学写作 skills。

## Attribution, License, And Ethical Use / 引用、许可与伦理使用 ⚖️

The `skills/econ-write/` skill includes content based on [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) by Lu Han, licensed under the MIT License. See [`NOTICE.md`](NOTICE.md) for the preserved third-party copyright and license notice.

`skills/econ-write/` 包含基于 Lu Han 的 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) 的内容，原项目采用 MIT License。第三方版权与许可声明已保存在 [`NOTICE.md`](NOTICE.md)。

Original repository content is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0), unless otherwise stated. Commercial use of original repository content requires separate written permission. Third-party materials remain subject to their own notices and licenses, as described in [`NOTICE.md`](NOTICE.md).

除非另有说明，本仓库原创内容采用 Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)。原创内容的商业使用需要另行取得书面许可。第三方内容仍以其各自声明和许可为准，见 [`NOTICE.md`](NOTICE.md)。

This repository is intended for non-commercial academic writing support. Do not use it for paid paper-writing services, ghostwriting, academic misconduct services, or fabricated research materials. See [`ETHICAL_USE.md`](ETHICAL_USE.md).

本仓库用于非商用学术写作辅助。不得用于付费论文代写、ghostwriting、学术不端服务或伪造研究材料。见 [`ETHICAL_USE.md`](ETHICAL_USE.md)。

Because the original repository content uses a NonCommercial license, this repository is not distributed as an OSI-approved open-source project.

由于原创内容采用 NonCommercial 许可，本仓库不以 OSI 认可的开源项目形式发布。

## AI Assistance / AI 辅助说明 🤖

ChatGPT and Codex were used to help organize the repository, draft documentation, review attribution, and prepare Git commits. They are not listed as authors or maintainers because responsibility for the repository, licensing choices, and final content remains with the human maintainer.

本仓库在整理目录、撰写说明、检查引用和准备 Git 提交时使用了 ChatGPT 与 Codex 辅助。它们不列为作者或维护者；仓库内容、许可选择和后续维护责任仍由人类维护者承担。

See [`docs/ai-assistance.md`](docs/ai-assistance.md) for details.
