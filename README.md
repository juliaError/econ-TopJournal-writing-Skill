# Economics Top-Journal Writing Skills

This repository contains Codex skills for economics paper writing workflows.

## Contents

- `skills/econ-write/`: general economics paper writing skill for abstracts, introductions, literature reviews, theory sections, empirical sections, tables, robustness, LaTeX, and revision.
- `skills/econ-write/references/paper_skills/`: optional section-specific reference modules used by `econ-write` when relevant.
- `skills/cn-top-econ-writing/`: Chinese top-journal economics writing skill for journals such as 《经济研究》, 《管理世界》, and 《中国工业经济》.

## Install Locally

Copy the skill directories into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
cp -R skills/econ-write ~/.codex/skills/econ-write
cp -R skills/cn-top-econ-writing ~/.codex/skills/cn-top-econ-writing
```

Restart or refresh Codex after installation so the skills list is reloaded.

## Usage

Use `econ-write` for general economics papers:

```text
Use econ-write to revise this introduction.
```

Use `cn-top-econ-writing` for Chinese top-journal submissions:

```text
用 cn-top-econ-writing 审查这篇中文经济学论文的引言和贡献表述。
```

## Notes

- `econ-write` selectively loads `references/paper_skills/` files only when the task needs them.
- Some `paper_skills` reference files are placeholders until their Markdown rule bodies are filled in.
- No license is included yet. Add one before public reuse if you want to define redistribution and modification rights.
