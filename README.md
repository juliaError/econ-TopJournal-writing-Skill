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
| `docs/paper-corpus.md` | Paper corpus used as the writing-learning reference set. | 构建和扩展本写作 workflow 时参考、蒸馏的中英文论文清单。 |
| `LICENSE` | MIT License for the original contents of this repository. | 本仓库原创内容采用的 MIT License。 |
| `NOTICE.md` | Third-party copyright and MIT License notice. | 外部来源与 MIT License 声明。 |
| `docs/ai-assistance.md` | Notes on AI-assisted development and responsibility. | 关于 AI 辅助开发、署名和责任边界的说明。 |

## Knowledge Sources / 知识来源 📚

This repository currently has two kinds of sources:

1. **Third-party skill source**: `skills/econ-write/` is based on the open-source [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) project by Lu Han, licensed under the MIT License.
2. **Local paper corpus**: the modular `paper_skills` and table/figure workflows are designed to be expanded from a 43-paper economics writing-learning corpus, including classic English theory/empirical papers and Chinese economics journal papers.

本仓库目前有两类来源：

1. **外部 skill 来源**：`skills/econ-write/` 基于 Lu Han 的开源项目 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill)，许可证为 MIT License。
2. **本地论文语料**：`paper_skills` 与表图设计模块计划从 43 篇经济学论文中提炼写作规则，覆盖英文理论/实证论文和中文经济学期刊论文。

See [`docs/paper-corpus.md`](docs/paper-corpus.md) for the full paper list and what each group teaches.

完整论文清单和学习重点见 [`docs/paper-corpus.md`](docs/paper-corpus.md)。

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
- **2026-05-13 update**: `econ-writing-workflow` is now added as the main writing entry skill that routes ordinary user requests to the relevant specialized module.
- `cn-top-econ-writing` is a standalone Chinese top-journal writing skill.
- `paper_skills` reference files are still being developed. Some files are placeholders until their detailed rule bodies are filled in.
- The long-term goal is to gradually rewrite the workflow into a fully original economics writing skill distilled from the paper corpus and locally developed writing rules.

- `econ-write` 当前可直接使用，并已保留第三方 MIT 声明。
- **2026-05-13 更新**：`econ-write` 已新增 `references/english-diction/` 英文顶刊遣词造句模块，覆盖句子功能、动词搭配、摘要与引言句法、理论/实证 prose 差异，以及 AI 腔/翻译腔修稿检查。
- **2026-05-13 更新**：新增 `econ-table-figure-design` 中英文通用表图设计 skill，覆盖主回归表、稳健性、异质性、机制、表注图注、配色、字体字号和导出检查。
- **2026-05-13 更新**：新增 `econ-writing-workflow` 写作总入口 skill，用于把普通用户请求路由到相应专业模块。
- `cn-top-econ-writing` 是独立的中文顶刊写作 skill。
- `paper_skills` 参考文件仍在开发中，部分文件目前仍是占位。
- 长期目标是逐步基于论文语料和自有写作规则，重写为完全原创的经济学写作 skill。

## Attribution And License / 引用与许可 ⚖️

The `skills/econ-write/` skill is based on [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) by Lu Han, licensed under the MIT License. See [`NOTICE.md`](NOTICE.md) for the preserved third-party copyright and license notice.

`skills/econ-write/` 基于 Lu Han 的 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill)，采用 MIT License。第三方版权与许可声明已保存在 [`NOTICE.md`](NOTICE.md)。

The original contents of this repository are licensed under the MIT License. Third-party materials remain subject to their own notices and attribution, as described in [`NOTICE.md`](NOTICE.md).

本仓库原创内容采用 MIT License；第三方内容仍以其各自的声明和引用要求为准，见 [`NOTICE.md`](NOTICE.md)。

## AI Assistance / AI 辅助说明 🤖

ChatGPT and Codex were used to help organize the repository, draft documentation, review attribution, and prepare Git commits. They are not listed as authors or maintainers because responsibility for the repository, licensing choices, and final content remains with the human maintainer.

本仓库在整理目录、撰写说明、检查引用和准备 Git 提交时使用了 ChatGPT 与 Codex 辅助。它们不列为作者或维护者；仓库内容、许可选择和后续维护责任仍由人类维护者承担。

See [`docs/ai-assistance.md`](docs/ai-assistance.md) for details.
