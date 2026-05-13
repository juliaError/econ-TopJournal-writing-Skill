# Corpus Policy / 语料使用政策

This repository uses a locally maintained economics-writing corpus to develop abstract writing, revision, table, figure, and style rules. The public repository does not publish the corpus list, article text, screenshots, full tables, full figure pages, long quotations, or paper-specific extraction logs.

本仓库使用本地整理的经济学写作语料来发展抽象的写作、修稿、表格、图形和风格规则。公开仓库不发布具体论文清单、论文原文、截图、整表、整页图形、长引文或逐篇抽取日志。

## Public Rule Boundary / 公开规则边界

Public skill files may include:

- abstracted writing rules;
- original examples created for revision practice;
- reusable table and figure design principles;
- general corpus coverage categories without paper names or source identifiers;
- ethical and licensing notes.

公开 skill 文件可以包含：

- 抽象后的写作规则；
- 为修稿练习原创的例句；
- 可复用的表格与图形设计原则；
- 不含论文名和来源编号的一般语料覆盖类别；
- 伦理与许可说明。

Public skill files must not include:

- copied article paragraphs or long source sentences;
- paper screenshots, full table images, full figure pages, or extracted page images;
- detailed paper lists with author names and titles;
- paper-specific source identifiers or per-paper audit tables;
- source text that could substitute for reading the original article.

公开 skill 文件不得包含：

- 复制的论文段落或长原句；
- 论文截图、整表图片、整页图形或页面渲染图片；
- 含作者和题名的详细论文清单；
- 逐篇来源编号或逐篇审计表；
- 可能替代阅读原文的来源文本。

## How The Corpus Is Used / 语料如何使用

The corpus is used only as a private learning and audit aid. Rules are released as original abstractions, checklists, workflows, and templates. When a rule depends on broad writing patterns, the public file should describe the pattern by function rather than naming the source articles.

语料只作为本地学习和审计辅助。公开发布的内容应是原创抽象规则、检查清单、工作流和模板。当某条规则来自广泛写作模式时，公开文件应按功能说明模式，而不是列出来源论文。

## Skill Routing / Skill 调用

`econ-writing-workflow` is the public entry skill that routes corpus-informed writing rules to the relevant module:

- English writing and diction rules;
- Chinese top-journal writing and diction rules;
- table and figure design rules;
- argument logic and revision workflow rules.

`econ-writing-workflow` 是公开写作总入口 skill，用于将语料启发的写作规则路由到相应模块：

- 英文写作与遣词规则；
- 中文顶刊写作与遣词规则；
- 表格与图形设计规则；
- 全文逻辑与修稿工作流规则。

## Maintenance Note / 维护说明

Detailed source audits may remain in local task directories for private verification. They should not be copied into public skill references unless converted into abstract, non-source-specific guidance.

详细来源审计可以保留在本地任务目录中用于私人复核。除非已经转换为抽象、非逐篇来源的规则，否则不得复制进公开 skill references。
