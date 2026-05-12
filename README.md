# Economics Top-Journal Writing Skills / 经济学顶刊写作 Skills ✨

This repository collects Codex skills for economics paper writing, revision, and top-journal style checking.

本仓库用于整理经济学论文写作、修改、投稿前审查和中文顶刊风格适配的 Codex skills。它目前采用“可用的外部英文 skill + 自有中文顶刊 skill + 后续可扩展论文语料模块”的结构。

## What Is Inside / 仓库内容 🧭

| Path | English | 中文说明 |
| --- | --- | --- |
| `skills/econ-write/` | General economics paper writing skill for abstracts, introductions, literature reviews, theory sections, empirical sections, tables, robustness, LaTeX, and revision. | 通用英文经济学论文写作 skill，覆盖摘要、引言、文献、理论、实证、表图、稳健性、LaTeX 和修改审查。 |
| `skills/econ-write/references/paper_skills/` | Optional section-specific reference modules loaded by `econ-write` when relevant. | 后续用于细分写作规则的模块化参考文件，目前部分内容仍是占位。 |
| `skills/cn-top-econ-writing/` | Chinese top-journal economics writing skill for journals such as 《经济研究》, 《管理世界》, and 《中国工业经济》. | 面向《经济研究》《管理世界》《中国工业经济》等中文顶刊的写作、审查和修稿 skill。 |
| `docs/paper-corpus.md` | Paper corpus used as the writing-learning reference set. | 构建和扩展本写作 workflow 时参考、蒸馏的中英文论文清单。 |
| `LICENSE` | MIT License for the original contents of this repository. | 本仓库原创内容采用的 MIT License。 |
| `NOTICE.md` | Third-party copyright and MIT License notice. | 外部来源与 MIT License 声明。 |
| `docs/ai-assistance.md` | Notes on AI-assisted development and responsibility. | 关于 AI 辅助开发、署名和责任边界的说明。 |

## Knowledge Sources / 知识来源 📚

This repository currently has two kinds of sources:

1. **Third-party skill source**: `skills/econ-write/` is based on the open-source [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill) project by Lu Han, licensed under the MIT License.
2. **Local paper corpus**: the modular `paper_skills` workflow is designed to be expanded from a 38-paper economics writing-learning corpus, including classic English theory/empirical papers and Chinese economics journal papers.

本仓库目前有两类来源：

1. **外部 skill 来源**：`skills/econ-write/` 基于 Lu Han 的开源项目 [`hanlulong/econ-writing-skill`](https://github.com/hanlulong/econ-writing-skill)，许可证为 MIT License。
2. **本地论文语料**：`paper_skills` 模块计划从 38 篇经济学论文中提炼写作规则，覆盖英文理论/实证论文和中文经济学期刊论文。

See [`docs/paper-corpus.md`](docs/paper-corpus.md) for the full paper list and what each group teaches.

完整论文清单和学习重点见 [`docs/paper-corpus.md`](docs/paper-corpus.md)。

## Install Locally / 本地安装 🚀

Copy the skill directories into your Codex skills folder:

将 skill 目录复制到 Codex skills 文件夹：

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
```

Restart or refresh Codex after installation so the skills list is reloaded.

安装后重启或刷新 Codex，让 skills 列表重新加载。

## Usage / 使用方式 🛠️

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

For empirical coding, data cleaning, or regressions, pair these writing skills with a separate empirical workflow skill.

如果任务涉及数据清洗、变量构造或回归代码，应搭配单独的实证工作流 skill，而不是只靠写作 skill。

## Current Status / 当前状态 🌱

- `econ-write` is usable now and keeps its third-party MIT notice.
- `cn-top-econ-writing` is a standalone Chinese top-journal writing skill.
- `paper_skills` reference files are still being developed. Some files are placeholders until their detailed rule bodies are filled in.
- The long-term goal is to gradually rewrite the workflow into a fully original economics writing skill distilled from the paper corpus and locally developed writing rules.

- `econ-write` 当前可直接使用，并已保留第三方 MIT 声明。
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
