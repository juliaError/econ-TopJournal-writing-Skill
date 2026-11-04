---
name: econ-writing-workflow
description: Use as the main entry point for economics writing workflows in English or Chinese, including paper and research-proposal planning, monograph outlines, chapter drafting and integration, argument outlines, collaborator-facing writing-task outlines and research-team staffing briefs, scope and claim convergence, full paper drafting from research questions and result packages, major revision, document-level translation or compression, exhaustive semantic QA and final audits, abstract/introduction/results revision, Chinese top-journal adaptation, English and Chinese diction cleanup, AI/translationese removal, table and figure design, notes/captions, formatting checks, and routing to empirical workflow support when data cleaning, regressions, or variable construction are involved.
---

# Economics Writing Workflow

## Role

Use this skill as the user's main entry point for economics writing work. It does not replace the specialized skills; it routes the task to the right writing module, keeps the workflow ordered, and checks that the final output matches the user's target.

This skill is not a full empirical pipeline. For data cleaning, variable construction, regression code, estimation, diagnostics, or reproducibility tasks, pair with `empirical-econ-workflow`.

## Deliverable Type

Identify the requested deliverable separately from the work stage: discussion
or argument outline, research proposal, collaborator-facing writing-task
outline, research-team staffing brief, or manuscript prose. A writing-task outline is meant to contain
reading assignments, argument steps and figure/table production instructions;
do not strip them out using manuscript-only voice rules. Keep internal edit
history and agent bookkeeping out of the handed-off outline.

For paper/book or proposal outlines, writing-task outlines, or research-team
staffing briefs, load
`references/outlines/01_argument_and_writing_task_outlines.md`. Preserve the
accepted framework and use the outline's purpose to choose its level of detail.
An outline alone does not trigger complete-paper drafting or exhaustive
complete-manuscript QA requirements. Existing author-intent, source, empirical
and write-authorization rules still apply where relevant. For an actual
research proposal, continue to use the proposal-specific module rather than
substituting the task-outline template.

When planning a monograph, drafting a chapter or bringing separately written
sections together, consult the same paper-writing references listed under
Routing for the work at hand: argument logic, literature and evidence, or
tables and figures. Use them when setting assignments as well as when reading
drafts. For chapter roles, writing order and editorial handoff, use
`references/outlines/01_argument_and_writing_task_outlines.md`. An empirical
design, regression or journal-style contribution statement belongs in a book
only when the chapter actually calls for it.

A proposal skeleton is still an outline, not a complete proposal. For
outline-only requests, check argument and display specifications; do not
require produced figures, rendered-label checks, or a complete-proposal QA
report when those artifacts are not being delivered. Apply the corresponding
production and acceptance checks when the actual artifacts are requested.

## Audience And Intended Use

Before drafting a book outline, paper plan, proposal, writing-task outline or
research-team staffing brief, establish who will read it and what they need
to do with it. Read the user's existing instructions first. If unclear, ask:
“这份文件主要供你自己推敲，还是发给老师、同学或合作者？如果发给别人，
是请对方讨论判断，还是据此执行任务？” Wait for the answer before drafting
content whose inclusion depends on it; independent context reading can continue.
Reuse an explicit audience and purpose without asking again on each edit or
resumption. Reassess when the intended recipient or use changes.

Self-use permits useful alternatives, edit reasons and discussion notes; it
does not require adding them. For a document handed to others, retain content
that helps the recipient understand the research, make the requested decision,
or carry out confirmed work. Keep author-agent deliberation, allocation
history and agent bookkeeping outside it. Personal availability, workload,
existing task burdens and personal accommodation arrangements belong only in
the user's private deliberation or records. Exclude them from documents handed
to anyone else, whether for discussion or execution; apparent usefulness to
the recipient's decision is not an exception. Retain relevant expertise only
when the user permits its disclosure and it is necessary for that recipient's
current decision.
Research reasoning, necessary sources, evidence status, methods, feasibility,
risks, and substantive questions requiring the recipient's decision are not
internal chatter. Writing and figure/table instructions belong in a task
outline even though they would not belong in manuscript prose.

Apply this distinction while drafting, when converting a self-use document
for circulation, and before final delivery. For outlines and staffing briefs,
use the recipient-necessity and assignment checks in
`references/outlines/01_argument_and_writing_task_outlines.md`; for complete
proposals also preserve the proposal-specific requirements. Keep internal
notes in the conversation or existing authorized records. Do not automatically
create internal/external versions, extra files, or printed audit checklists.
Audience selection does not authorize sending the document to anyone.

## Project-Level Skill Pinning

For multi-step economics writing, table, figure, journal-submission, or paper-formatting workflows, check whether the nearest project-level `AGENTS.md` or `CLAUDE.md` already contains an economics-writing skill routing rule.

If no such rule exists, ask the user once whether to add a persistent local rule. Do not edit `AGENTS.md` or `CLAUDE.md` without explicit user approval, and do not ask for tiny one-off requests.

Recommended rule text:

```markdown
## Economics Writing Skill Routing

For economics paper writing, journal adaptation, tables, figures, captions, notes, Word/PDF formatting, and submission checks, first route through `econ-writing-workflow`.

Use `cn-top-econ-writing` for Chinese top-journal prose and journal-specific submission style. Use `econ-table-figure-design` for tables, figures, maps, captions, notes, and export quality. Use `empirical-econ-workflow` when data cleaning, variable construction, regressions, sample audits, or estimation code are involved.

Keep the relevant skill active throughout the task unless the user explicitly opts out. Do not treat skill use as a one-time setup step: at the start of each substantive phase, and whenever the work crosses from prose into tables, figures, maps, journal formatting, data facts, or empirical code, reclassify the current subtask and load the relevant specialized skill or reference file.

During manuscript drafting or revision, separate paper-facing text from author memos and task logs before writing each paragraph, table note, figure note, appendix note, or footnote. Only reader-facing manuscript text may enter the paper. Author workflow notes, submission-positioning discussion, reasons for moving/deleting material, and author-agent internal decisions must stay in the response, task README, revision memo, or checklist.

Before drafting claim-bearing prose, determine whether the author has explicitly fixed the intended meaning for the requested scope. If not, inspect the available context, ask the smallest grouped set of material questions, restate the intended meaning for confirmation, and wait. Do not draft the affected prose or use a `TODO` to bypass unresolved author intent. A `TODO` may represent a missing factual detail only when it does not change the already confirmed meaning.

Before drafting each paper-facing paragraph, apply draft-time argument clarity: ground abstract concepts in observable/model objects, state the comparison for relative or causal claims, keep design language separate from findings, distinguish mechanisms from plain heterogeneity, position close literature by the margin advanced, and keep terminology stable.

Before drafting literature-dependent claims, check whether the project has local reference papers, literature notes, `.bib` files, or source ledgers. Ask whether the literature is sufficient and whether the user wants help finding publicly available papers. If a Chinese or paywalled source cannot be obtained locally, tell the user and continue only with unaffected content. A non-semantic citation or verification detail may remain as an author-facing `TODO`; if the missing source affects literature positioning, theory, mechanism, variable meaning, identification, contribution, policy implication, or claim strength, return `evidence_conflict` and leave the affected manuscript text unwritten. When the paper uses literature-based data, theories, variables, mechanisms, or empirical choices, read the relevant source material and align with it instead of inventing a new framing.

Preserve evidence boundaries without turning them into defensive disclaimers. Prefer an accurate claim type, calibrated verb, and the minimum scope qualifier needed for the reader. Before adding even the first or only stand-alone negative caveat, state affirmatively what the result, estimate, threshold, scenario, or model object represents and what interpretation it supports. This is explanatory wording, not favorable spin. Admit a separate negative sentence only when it blocks a concrete material misreading not already excluded by the calibrated wording; bind it to the exact claim or number and use it as a last resort. Repeat it only when the identification, sample, period, geography, extrapolation target, or evidence grade changes, or when a stand-alone abstract, caption, note, journal rule, or referee request requires self-contained wording. Do not impose a mechanical per-section caveat quota.

Do not let the model or a reviewer self-authorize that last resort. Unless the exact negative proposition is already confirmed and frozen by the author, withhold it from manuscript prose and return `clarification_required` with the affirmative alternative and proposed contrast.

When writing regression results, main findings, mechanisms, heterogeneity, robustness, abstracts, introductions, or conclusions that mention coefficient size, translate estimates into economic magnitude using at least one appropriate benchmark. Prefer natural units or real policy changes when available; use means, standard deviations, or percentile spreads only when they fit the variable and identification source. Never invent descriptive statistics.

When producing tables, figures, maps, or edited images, load `econ-table-figure-design/references/labels/01_reader_facing_labels.md` and apply its reader-facing label gate before treating the task as complete. Verify the final rendered artifact itself: text, legends, colorbars, inset maps, axes, notes, and substantive visual content must be intelligible and must not overlap, obscure, or cover useful information.
```

After adding the rule, include a clear marker heading so future agents can detect it and avoid asking again.

## Paper Plan And Artifact Lifecycle

For multi-step paper work or a major paper section, first locate the project's
single authoritative current-plan store and current-plan document. If none
exists, ask the author whether to establish it before substantive production.
Do not create parallel current-plan files.

Read the authoritative current plan before each substantive phase. Keep only
the latest accepted objective and claim sequence, admitted evidence and paper
role, main-text or appendix placement, reader-facing terminology, unresolved
decisions, current non-goals, and authorization boundaries. When the author
approves, rejects, narrows, or replaces a plan, update the current plan in
place during the same task. Keep historical process in task logs, manifests,
or audit packages rather than competing current-plan documents.

Develop exploratory and candidate tables, figures, maps, measures,
specifications, model outputs, and other research objects outside the
centralized current-artifact store. Track two dimensions separately:

- `artifact_state`: `exploratory`, `candidate`, `author-confirmed`,
  `frozen-current`, `rejected`, or `superseded`;
- `manuscript_state`: `not-integrated` or `manuscript-integrated`.

Never infer a later state or approval from an earlier one. An object may remain
`frozen-current` while also being `manuscript-integrated`; a revision that
replaces it may become `superseded` while an older manuscript still cites that
revision.

Before moving to a new substantive phase, update the authoritative current
plan and check whether an `author-confirmed` object still lacks an explicit
freeze decision. If so, ask whether to freeze it as the sole current revision.
Do not repeatedly ask after the project record contains the decision, and do
not freeze a merely plausible, validated, or polished candidate.

For every freeze, replacement, rejection, or manuscript integration, load and
follow `references/artifact-lifecycle/01_artifact_state_and_freeze_protocol.md`.
That protocol requires a machine-readable registry, a complete freeze
manifest, SHA-256 coverage for code, inputs, outputs, and validation records,
and a verified immutable audit bundle before any current revision is replaced.
Do not report a freeze complete while a required manifest, checksum, approval,
or recovery artifact is missing.

Keep the centralized current-artifact store current-state only. Build and
validate replacement candidates outside it. Before updating stable current
paths, preserve and verify the old frozen revision in the superseded audit
store; then switch the replacement into the stable paths and update the
registry. Do not accumulate competing current names such as `v2`, `final2`,
`new`, or `latest`, and do not treat current-state cleanup as permission to
delete audit history or original inputs.

Treat substantive approval, freeze approval, replacement approval, and
manuscript-integration approval as separate decisions. Freezing never
authorizes Word/LaTeX edits, caption or note changes, figure redesign,
manuscript insertion, or submission export. Before integration, verify the
proposed object and placement against the authoritative current plan and the
current-artifact registry, obtain separate manuscript authorization, and
record the exact manuscript version and location.

This research-object lifecycle registry is distinct from the multiagent
manuscript `artifact_contract`, which protects accepted manuscript content,
length, and main-text sufficiency. When both apply, maintain both records; do
not use either as a substitute for the other. Follow stricter project-level
repository, terminology-firewall, manuscript-conservation, or authorization
rules first.

## Author Intent And Semantic Fidelity

Before new claim-bearing prose, substantive rewriting, translation that may
change meaning, or section restructuring, load and follow
`references/author-intent/01_author_intent_contract_and_semantic_fidelity.md`.
Do this even for a local passage; a local scope exception from paper-wide
convergence does not authorize the agent to infer the author's meaning.

Inspect the manuscript, current plan, evidence, and prior author decisions
before asking. If an existing frozen author-intent contract covers the exact
scope, reuse it without repeated confirmation. If the author has already stated
one uniquely determined meaning and requested writing from it, record that
instruction as the frozen-current contract. Otherwise, ask the smallest grouped
set of questions that would change the text and teach back the proposed meaning.
The author's explicit confirmation normally freezes that meaning for the stated
drafting scope in the same act; do not ask for a redundant second approval. Keep
it unfrozen only when the author explicitly reserves approval, a material
question remains unresolved, or an evidence conflict blocks the intended claim.

Treat the author as the authority over what the paper is intended to say and
the inspected evidence as the authority over what the paper can support.
Return `clarification_required` when intended meaning remains ambiguous or
internally inconsistent. Return `evidence_conflict` when the intended claim
exceeds the evidence. In either state, do not write around the problem, insert
the disputed claim with a `TODO`, or silently substitute the agent's preferred
interpretation.

Once the contract is frozen, preserve every `must_express`, `must_not_claim`,
`must_not_imply`, required qualifier, evidence boundary, and terminology rule.
The agent may improve syntax, order, transitions, and concision only within the
recorded `allowed_discretion`. Put alternative interpretations or stronger
frames in an author-facing memo and obtain approval before they enter the
manuscript. If intent changes, supersede only the affected contract entry and
recheck its downstream prose; never allow silent semantic drift.

Freeze the semantic content and necessary coverage of a qualifier, not a
requirement to repeat the same disclaimer after every result, table, or figure.
After a candidate exists, an optional derived `caveat_placement_registry` may
map a required boundary to its first adequate location and the concrete events
that permit repetition; before drafting, keep only the frozen placement policy
and a pending pointer, not invented unit IDs. Precise claim type, calibrated
verbs, and a nearby scope condition can satisfy the boundary without a separate
defensive sentence. Before accepting even the first or only stand-alone
negative caveat, prefer an integrated affirmative explanation of what the
estimate, threshold, scenario, or model object is and what it shows. A sentence
that introduces a new outcome or estimand only to deny that the paper estimates
it adds no information unless a concrete material misreading would otherwise
remain. If a negative contrast is still necessary, bind it to the exact
preceding claim or number and use it as a last resort. Do not infer permission
to add or retain that contrast from the model's own caution: unless the exact
negative proposition is already frozen in author intent, return
`clarification_required` and ask the author. Removing a unique
no-information caveat, or a later repetition, is not semantic weakening when
the surrounding calibrated wording still covers the same claims and scope.

After drafting, run the semantic-fidelity audit from the reference. Do not
deliver or integrate text that omits a required proposition, adds an
unapproved claim, strengthens association into causality, upgrades
heterogeneity into mechanism evidence, broadens scope, drops a qualifier, or
reintroduces a forbidden implication.

For a complete paper or proposal, a document-level translation or compression,
or a major manuscript revision, route the accepted draft through
`econ-writing-workflow-multiagent` and its
`econ-writing-workflow-multiagent/references/exhaustive_semantic_qa_protocol.md`
reference before delivery. This is a
mandatory heavy-QA route, not an invitation to reopen the frozen author intent
or shorten the manuscript. It covers every reader-visible sentence in the body
and appendix, including sentences inside footnotes, captions, and table or
figure notes. The
multiagent controller must use native independent reviewers and deterministic
coverage/hash validation; a missing reviewer or unavailable independent-agent
environment returns `audit_incomplete`, never a simulated pass.

For a bounded local polish, audit only the changed sentences, their full
paragraphs, adjacent context needed to interpret them, and any definitions or
cross-section statements that depend on the change. Escalate to the heavy route
when the edit changes the paper spine, claim type or strength, mechanism,
definition, evidence boundary, scope, or material placement. A small context
window limits reviewer input, not the length or substantive completeness of the
manuscript.

Pure spelling, punctuation, citation-format, layout, or grammar-only edits do
not require the full intent-elicitation protocol when the author explicitly
requires meaning preservation or the requested operation has one unambiguously
mechanical, meaning-preserving correction. Use the source wording and the
narrow requested operation as the baseline. Verify the correction itself,
including subject-verb agreement, pronoun antecedent and number, tense,
negation, modifier attachment, and punctuation or citation consistency. Stop
and ask only if the edit exposes a material ambiguity or requires choosing
among substantively different meanings.

## First Decision

Before writing or editing, classify the task stage as `exploration`, `proposal`,
`full drafting`, `document translation`, `compression`, `major revision`,
`major restructuring`, `local edit`, `local polish`, or `final audit`. Do not
load paper-wide convergence or final-audit checks for a bounded local edit
unless a substantive contradiction blocks the requested change.

When handing a task to deterministic multiagent QA, map those human-facing
labels exactly: `proposal -> proposal_draft`, `full drafting -> full_draft`,
`document translation -> document_translation`, `compression ->
document_compression`, `major revision -> major_revision`, `major
restructuring -> major_restructure`, `local edit -> local_edit`, `local polish
-> local_polish`, and `final audit -> final_audit`. Do not invent another
machine stage or use a generic final-audit label to hide the underlying
artifact mode.

Task-stage classification never overrides the author-intent gate. A local
substantive rewrite still requires confirmed meaning; only an explicitly or
unambiguously meaning-preserving mechanical edit receives the narrow exception
above.

Then classify the request:

1. **English paper prose**: abstract, introduction, literature review, model/theory prose, empirical/results prose, conclusion, referee response, or English revision.
2. **English diction cleanup**: remove AI-like prose, translationese, vague contribution language, weak verbs, or template signposting.
3. **Argument logic and draft-time clarity**: full-paper logic, argument spine, paragraph-level clarity, concept grounding, comparison clarity, design/results separation, mechanism-versus-heterogeneity, contribution positioning, repeated material, misplaced sections, emphasis, ordering, or whether tables and figures serve the main line.
4. **Regression results and economic magnitude**: main regression interpretation, coefficient size, economic magnitude, marginal effects, interaction net effects, or result prose that needs means, standard deviations, percentiles, policy benchmarks, or log-to-percent conversions.
5. **Literature and judgment grounding**: local reference papers, literature search/download decisions, source ledgers, citation grounding, theory/mechanism/variable alignment, contribution boundaries, or literature-based judgment calibration.
6. **Full-paper drafting from a result package**: draft a complete paper from a research question, regression tables, figures, result folders, slides, variable notes, or design notes.
7. **Chinese top-journal writing**: Chinese paper structure, Chinese abstract, introduction, contribution framing, journal fit, submission style, or top-journal revision.
8. **Chinese diction cleanup**: remove AI 腔, 翻译腔, 作者备忘腔, unnatural collocations, or stiff Chinese academic prose.
9. **Journal submission style**: target-journal formatting, submission requirements, anonymous PDF checks, accepted-version Word formatting, title hierarchy, references, JEL codes, appendices, or journal-specific body/appendix placement.
10. **Tables and figures**: table/figure admission, main-text versus appendix placement, three-line tables, regression/robustness/heterogeneity/mechanism tables, notes, captions, palettes, fonts, or export quality.
11. **Empirical workflow**: data cleaning, variable construction, sample construction, regression code, estimation, diagnostics, or reproducibility.
12. **Research convergence and proposal feasibility**: scope freezing, one-sentence research question, contribution hierarchy, current non-goals, model or identification closure, theory-to-measure mapping, proposal execution plans, cross-section consistency, or stopping a mature revision cycle.
13. **Document transformation and exhaustive QA**: a complete manuscript or proposal, document-level translation or compression, major revision, deterministic sentence/unit coverage, independent semantic review, or final acceptance gating.

If a request spans more than one category, handle them in this order:

1. empirical workflow and sample/design facts;
2. literature and judgment grounding;
3. applicable research-convergence gates;
4. table and figure design;
5. paper structure and section logic;
6. full-paper drafting plan;
7. prose and diction cleanup;
8. exhaustive semantic QA, post-diction semantic re-review, and final conservation when required;
9. final formatting/export checks.

## Routing

- For discussion/argument outlines, book or proposal outlines, writing-task outlines, or research-team staffing briefs, apply Audience And Intended Use and load `references/outlines/01_argument_and_writing_task_outlines.md`; distinguish the deliverable from a research proposal or manuscript before applying the remaining routes.
- For new claim-bearing prose, substantive rewriting, meaning-sensitive translation, section restructuring, or uncertainty about what the author wants to say or not say, first load `references/author-intent/01_author_intent_contract_and_semantic_fidelity.md`.
- For a complete paper or proposal, document-level translation or compression, major revision, or exhaustive pre-delivery semantic audit, route to `econ-writing-workflow-multiagent` and load `econ-writing-workflow-multiagent/references/exhaustive_semantic_qa_protocol.md`. Do not use a sequential same-agent simulation as evidence that the independent-review gate passed.
- For English paper prose, use `econ-write`.
- For English diction cleanup, use `econ-write` and load `econ-write/references/english-diction/` selectively.
- For full-paper logic, repeated material, emphasis, section ordering, and argument-spine audits, load `references/argument-logic/` selectively before polishing prose. Before drafting or revising abstracts, introductions, literature positioning, design, results, mechanisms, heterogeneity, contributions, or conclusions, load `references/argument-logic/06_draft_time_argument_clarity.md` so clarity is handled during generation, not only in the final audit.
- For regression results, main findings, economic magnitude, coefficient interpretation, marginal effects, interaction net effects, log-to-percent conversions, or benchmark choices using means, standard deviations, percentiles, policy changes, or natural units, load `references/regression-results/01_economic_magnitude_interpretation.md` before drafting the relevant prose.
- For literature-dependent drafting, closest-literature positioning, literature search/download decisions, source ledgers, citation grounding, theory/mechanism/variable alignment, or calibration of similar judgments from prior papers, load `references/literature-grounding/01_literature_and_judgment_grounding.md` before drafting the relevant prose. For a full paper or proposal, substantive literature revision, project-specific coverage target, citation-library reconciliation, or final audit with references, also load `references/literature-grounding/02_literature_coverage_and_citation_integrity.md`.
- For manuscript-facing versus author-facing voice, internal memo leakage, or requests to remove author workflow notes from paper prose, load `references/manuscript-voice/01_no_author_memo_in_manuscript.md` before finalizing text.
- For full-paper drafting from research questions, regression tables, figures, or result folders, load `references/full-paper-drafting/` first, then route table/figure decisions to `econ-table-figure-design` and language-specific prose to `econ-write` or `cn-top-econ-writing`.
- For full-paper or proposal scoping, major restructuring, contribution drift, terminology drift, or repeated expansion beyond the current question, load `references/research-convergence/01_scope_and_claim_contract.md`.
- For theory/model closure, assumption roles, theory-to-measure mapping, identification capacity, evidence-status calibration, welfare claims, or normative policy recommendations, load only the applicable sections of `references/research-convergence/02_theory_empirical_closure_gates.md`.
- For a general research proposal, executable research plan, paper-wide ordered revision, final consistency audit, or mature-draft stopping decision, load only the applicable sections of `references/research-convergence/03_proposal_revision_stop_gates.md`.
- Do not load all research-convergence modules for local diction cleanup, a bounded paragraph rewrite, citation formatting, or a narrow table/figure note edit. Keep the requested scope unless a high-impact substantive contradiction prevents a responsible local answer.
- For Chinese top-journal writing, use `cn-top-econ-writing`.
- For target-journal submission style, anonymous manuscript checks, accepted-version formatting, references, appendices, or requests such as “按《经济学（季刊）》投稿要求调整”, use `cn-top-econ-writing` and its `cn-top-econ-writing/references/journal-styles/` module. For 《经济学（季刊）》, load `cn-top-econ-writing/references/journal-styles/00_journal_submission_workflow.md`, `cn-top-econ-writing/references/journal-styles/economics_quarterly.md`, and when table/figure/appendix issues appear, `cn-top-econ-writing/references/journal-styles/common_chinese_journal_rules.md`.
- For Chinese diction cleanup, use `cn-top-econ-writing` and load `cn-top-econ-writing/references/chinese-diction/` selectively.
- For tables, figures, notes, captions, palettes, typography, and export checks, use `econ-table-figure-design`.
- For data cleaning, regression code, variable construction, or estimation, pair with `empirical-econ-workflow`. Do not let this writing workflow invent or run empirical results by itself.

## Active Routing During Work

Do not route only once at the beginning of a long task. At the start of each substantive phase, and whenever the work crosses from prose into tables, figures, maps, journal formatting, data facts, or empirical code, reclassify the current subtask and load the relevant specialized skill or reference file.

Route immediately when these boundaries appear:

- new claim-bearing prose, substantive rewriting, meaning-sensitive translation, section restructuring, or possible drift in claim meaning, strength, qualifiers, implications, or emphasis: load `references/author-intent/01_author_intent_contract_and_semantic_fidelity.md` before the language-specific writing skill;
- complete-paper or complete-proposal drafting, document-level translation or compression, major revision, or final semantic acceptance: route to `econ-writing-workflow-multiagent` for deterministic manifest coverage plus independent semantic review; bounded local polish remains local unless it changes a substantive dependency;
- tables, figures, maps, image edits, titles, row or column names, captions, notes, legends, colorbars, fonts, export quality, or main-text versus appendix placement: use `econ-table-figure-design` and its mandatory reader-facing-label reference; code-generated paper-facing artifacts and delivery candidates require its deterministic label audit as well as semantic and rendered-artifact review;
- abstracts, introductions, literature positioning, research design, results, mechanisms, heterogeneity, contributions, or conclusions where the wording depends on observable objects, comparison groups, design/results separation, mechanism evidence, contribution margins, or terminology stability: load `references/argument-logic/06_draft_time_argument_clarity.md`;
- main regression results, mechanism or heterogeneity estimates, coefficient size, economic magnitude, marginal effects, interaction net effects, log-to-percent conversions, mean/SD/percentile comparisons, or policy benchmark interpretation: load `references/regression-results/01_economic_magnitude_interpretation.md`;
- local reference papers, PDFs, `.bib` files, literature search/download, closest-literature positioning, data/theory/variable/mechanism alignment with prior papers, contribution boundaries, or claim-strength calibration: load `references/literature-grounding/01_literature_and_judgment_grounding.md`; add `references/literature-grounding/02_literature_coverage_and_citation_integrity.md` for paper-level coverage, registry, bibliography, or final citation-integrity work;
- full drafting, proposal development, major restructuring, scope or terminology drift, theory/model closure, theory-to-measure mapping, normative policy claims, paper-wide revision, or final-audit stopping decisions: load only the matching `references/research-convergence/` file and section;
- target-journal style, anonymous submission, title hierarchy, references, JEL codes, appendices, Word/PDF submission format, or 《经济学（季刊）》 rules: use `cn-top-econ-writing` and its `cn-top-econ-writing/references/journal-styles/` module;
- data cleaning, variable construction, regression code, estimation, sample changes, or post-estimation sample audit: pair with `empirical-econ-workflow`;
- English prose or English diction: use `econ-write`;
- Chinese top-journal prose, Chinese diction, Chinese abstract, or Chinese contribution framing: use `cn-top-econ-writing`.

After a specialized skill settles its part, return to this workflow to integrate the decision into the paper-level order and final output check.

## Operating Rules

- Apply research-convergence rules by task stage, paper type, requested scope, and claim type. Do not turn a local prose edit into an unsolicited paper-wide audit, and do not force an exploration-stage idea into premature closure.
- Keep one central question visible while preserving legitimate secondary theory, data, measurement, structural, or policy contributions that materially change the intellectual claim. Treat fixed paragraph counts, result counts, and minimal-model advice as defaults with paper-type exceptions, not universal vetoes.
- Distinguish model results, numerical exercises, causal estimates, descriptive facts, suggestive interpretations, and planned tests. The abstract, introduction, conclusion, and policy discussion must not state a stronger or more complete result than the body supports.
- Keep scope contracts, non-goal lists, consistency matrices, revision-pass labels, and stopping decisions in author-facing logs or memos. Never insert them into manuscript prose, table notes, figure notes, appendix notes, or footnotes.
- Read available manuscript context before giving paper-level prose advice. If only an excerpt is available, state that the advice is excerpt-level.
- Before drafting each paper-facing paragraph, apply the author-intent gate and then the draft-time clarity gate. Identify the intended proposition, object, observable or model anchor, claim type, comparison, qualifiers, forbidden implications, and section function. If an unknown item would change meaning, return `clarification_required`; use a `TODO` only for a missing non-semantic fact inside an already confirmed proposition.
- Do not rewrite tables or figures as prose problems. Table selection, sample comparability, notes, and visual design are part of the research presentation.
- Do not put author workflow notes in paper-facing text, table notes, or figure notes.
- Before delivering or inserting manuscript text, classify each sentence as paper-facing text, author memo, or task log. Only paper-facing text may enter the manuscript.
- If the manuscript context is unclear on research question, variables, sample, identification, table/figure meaning, target journal, or whether the author wants to keep, delete, strengthen, weaken, or reframe a substantive claim, ask the user and stop the affected drafting scope; do not guess or use a `TODO` as semantic authorization.
- When discussing regression results in the manuscript, translate the coefficient into at least one suitable economic magnitude benchmark. Do not invent means, standard deviations, percentiles, policy changes, or marginal effects; compute them from supplied materials or ask for them. If the missing benchmark is recorded as an author-facing `TODO`, keep the unsupported magnitude out of paper-facing prose.
- Before writing literature-dependent claims, check local literature materials and ask whether they are sufficient when that is unclear. If the user wants help finding literature, only rely on papers that can be inspected or that the user supplies. If important Chinese or paywalled papers are unavailable, say so; use an author-facing `TODO` only for non-semantic citation or verification details, and return `evidence_conflict` with affected prose withheld when the missing support changes the claim.
- For a full paper, proposal, substantive literature revision, or final audit with references, define the applicable literature coverage clusters and reconcile the reference-library manifest, literature registry, manuscript citekeys, evidence ledger, and final visible bibliography. Do not infer a universal source-count floor from this skill. A project-specific minimum or target range is enforceable only when its provenance is recorded as an author requirement, journal rule, or reproducible comparable-paper sample.
- Preserve necessary evidence boundaries, but do not append generic statements such as `this is not causal`, `cannot be extrapolated`, or `cannot identify long-run effects` after a table, figure, or result paragraph. First state affirmatively what the result or numerical object represents and what interpretation it supports; this is explanatory precision, not favorable spin. Even a first or unique stand-alone negative caveat must block a concrete material misreading not already excluded by accurate verbs, claim type, and scope wording. If it introduces a new outcome or estimand only to deny it, delete it or integrate the necessary distinction into the affirmative interpretation unless a documented material misreading makes the precise contrast a last-resort necessity. Bind any retained negative sentence to the exact claim or number, and repeat it only after a relevant scope or evidence change or in a genuinely stand-alone reader-visible object. There is no per-section minimum or maximum count.
- A model or reviewer cannot self-authorize a stand-alone negative caveat. If its exact proposition is not already frozen by the author, withhold that sentence and return `clarification_required`; only the author may approve the exceptional `keep`.
- When the paper uses or adapts data, theory, concepts, variables, mechanisms, classifications, model objects, controls, fixed effects, heterogeneity dimensions, robustness checks, or policy interpretations from reference papers, inspect the relevant source material first and align terminology, construction, sample scope, and claim strength with those sources. Do not invent a new framing when a local reference already provides the relevant concept or boundary.
- When writing main-text pointers to appendices, tables, figures, or online appendices, keep them as pure pointers: state what to see and where to see it; only when needed, name the substantive role for the current claim, such as robustness, variable construction, sample scope, background fact, or extended result. Do not write meta-language such as `this is related to the main text` or `因此与正文有关`. Do not include layout or production language such as split columns, left/right halves, column width, page breaks, continued tables, repeated headers, or appendix-table formatting in the main text; put necessary reading guidance in the appendix text, table title, or note.
- Do not merge all specialized rules into the response. Load only the relevant child skill or reference files needed for the task.
- Preserve the user's language target: English manuscript tasks should output English unless asked otherwise; Chinese top-journal tasks should output Chinese unless asked otherwise.
- For full draft requests, never invent citations, data, variable definitions, identification claims, coefficient values, mechanisms, robustness results, or policy implications. Record only non-semantic missing facts as author-facing `TODO` items; mark a missing item `BLOCKED` and withhold the affected prose when it changes meaning or evidentiary support.
- Do not provide full manuscript drafting for paid paper-writing services, undisclosed ghostwriting, fabricated research, or academic misconduct. Offer an ethical outline, checklist, or teaching-oriented alternative instead.

## Argument-Logic References

Load only the relevant files:

- `references/argument-logic/01_argument_spine.md`: one-chain paper logic and missing-link audit.
- `references/argument-logic/02_redundancy_linter.md`: repeated, appendix, and delete/merge material.
- `references/argument-logic/03_emphasis_and_ordering.md`: what to foreground, delay, or de-emphasize.
- `references/argument-logic/04_table_figure_logic.md`: whether tables and figures serve the main line.
- `references/argument-logic/05_revision_workflow.md`: full-paper logic revision workflow.
- `references/argument-logic/06_draft_time_argument_clarity.md`: draft-time concept grounding, comparison clarity, design/results separation, mechanism-versus-heterogeneity, literature-margin positioning, and terminology stability.

## Research-Convergence References

Load only the matching module and relevant section:

- `references/research-convergence/01_scope_and_claim_contract.md`: task-stage classification, scope contract, paper-type argument spine, must-preserve/current-non-goal lists, terminology ledger, and reopening conditions.
- `references/research-convergence/02_theory_empirical_closure_gates.md`: evidence-status calibration, model closure, friction and assumption roles, economic-result qualification, concept-to-measure mapping, identification capacity, and normative policy conditions.
- `references/research-convergence/03_proposal_revision_stop_gates.md`: proposal status and executable plans, ordered major-revision passes, author-facing consistency matrix, and stop/reopen criteria.

## Author-Intent Reference

Load before claim-bearing drafting or substantive rewriting:

- `references/author-intent/01_author_intent_contract_and_semantic_fidelity.md`:
  defines the author-intent contract, teach-back confirmation, narrow mechanical
  exception, frozen-current meaning record, evidence-conflict handling, change
  control, and post-draft semantic-fidelity audit.

## Artifact-Lifecycle Reference

Load for multi-step projects that create, approve, freeze, replace, reject, or
insert tables, figures, maps, measures, specifications, model outputs, or other
research objects:

- `references/artifact-lifecycle/01_artifact_state_and_freeze_protocol.md`:
  separates artifact lifecycle from manuscript integration; defines allowed
  transitions, mandatory registry and SHA-256 fields, immutable superseded
  audit bundles, and safe current-path replacement.

## Full-Paper Drafting References

Load only the relevant files:

- `references/full-paper-drafting/01_input_checklist.md`: input audit and draftability levels.
- `references/full-paper-drafting/02_from_results_to_outline.md`: result ledger, argument spine, and table/figure placement logic.
- `references/full-paper-drafting/03_section_drafting_order.md`: section order and language-specific routing.
- `references/full-paper-drafting/04_missing_information_policy.md`: anti-fabrication rules and `TODO` format.
- `references/full-paper-drafting/05_full_draft_workflow.md`: full result-package-to-paper workflow.

## Literature-Grounding References

Load before drafting or revising literature-dependent sections or judgments:

- `references/literature-grounding/01_literature_and_judgment_grounding.md`: checks local references, asks whether literature is sufficient, builds source and judgment ledgers, aligns reused data/theory/variables/mechanisms with sources, and audits claim strength.
- `references/literature-grounding/02_literature_coverage_and_citation_integrity.md`: defines `literature-coverage-contract/1.0`, `reference-library-manifest/1.0`, `literature-registry/1.0`, their relationship to the existing `text_to_evidence_ledger`, project-specific coverage targets, and final manuscript-to-bibliography closure.

## Manuscript-Voice References

Load when drafting, revising, polishing, or auditing prose that will enter the manuscript:

- `references/manuscript-voice/01_no_author_memo_in_manuscript.md`: separates manuscript text from author memos and task logs; includes forbidden and context-dependent author-memo patterns.

## Regression-Results References

Load before drafting or revising main result prose, abstracts, introductions, conclusions, or referee responses that discuss coefficient size:

- `references/regression-results/01_economic_magnitude_interpretation.md`: chooses natural units, policy changes, means, standard deviations, percentile spreads, marginal effects, interaction net effects, and log-to-percent conversions for reader-facing economic magnitude.

## Output Check

Before finalizing a response, confirm that:

- the routed skill still matches the current subtask, not just the original request;
- for an outline, proposal or staffing brief, the audience and intended use are established; every delivered paragraph has been read for its value to that recipient, internal deliberation is excluded from circulated documents, and necessary research content and confirmed task instructions remain intact;
- a staffing brief distinguishes confirmed assignments for execution from explicitly requested proposals for discussion; proposed owners and responsibilities are marked pending confirmation, not treated as formal assignments or execution authorization; output and handoff instructions remain within the requested scope, and agent-generated coordination ideas have not silently become extra assignments;
- a writing-task outline makes the required reading, argument steps and outputs recoverable at each relevant unit, distinguishes production from prose instructions, and has been actually read within the claimed audit scope;
- any claim-bearing draft is covered by a frozen-current author-intent contract for the requested scope, or qualifies for the explicit meaning-preserving mechanical exception;
- the semantic-fidelity audit maps every required intent to the draft and finds no unapproved addition, claim-strength escalation, lost qualifier, forbidden implication, or evidence conflict;
- any complete paper or proposal, or document-level translation, compression, or major revision of such a manuscript, has a current exhaustive-QA report tied to the candidate and contract hashes; all reader-visible text is captured, every sentence/heading review target has the required roles, high-risk targets meet the contract's explicit independent-review minimum, and the final status is `pass` rather than `clarification_required`, `evidence_conflict`, `audit_incomplete`, `approval_required`, `fail`, or `metric_unavailable`; outline-only deliverables, including proposal skeletons, receive the outline review defined above rather than complete-manuscript acceptance;
- any bounded local polish rechecks the changed sentences, their paragraph and necessary adjacent context, and affected definition or cross-section dependencies rather than claiming a paper-wide pass;
- any table/figure decision specifies its intended placement and passes the applicable specification and source-recoverability checks; actual delivered tables/figures also pass the applicable basic-identity, full-recoverability, language, and rendered-label checks; outline-only production instructions do not require a produced or rendered artifact;
- any empirical claim is grounded in provided or inspected evidence;
- any main regression or important mechanism/robustness result has an economic magnitude benchmark, or the missing benchmark is kept out of paper-facing prose and recorded as a concrete author-facing `TODO`;
- any literature-dependent claim, theory, mechanism, variable, data source, empirical choice, contribution boundary, or policy implication is grounded in inspected local sources; unavailable non-semantic metadata is recorded as an author-facing `TODO`, while a material support gap returns `evidence_conflict` and keeps the affected prose unwritten;
- any applicable literature-coverage contract has no unresolved functional cluster, every manuscript citekey resolves through the authoritative library and admitted registry, every cited claim is linked to its evidence where required, and the final visible bibliography is derived from manuscript citekeys plus explicitly authorized `nocite` entries rather than from all unused library inventory;
- every necessary qualifier retains its meaning at an adequate reader-visible location, while a first, unique, or repeated defensive caveat with no new scope or evidence information is rewritten as affirmative interpretation or removed; absence of a generic disclaimer is not a failure when calibrated wording already preserves the evidence boundary, and any retained negative sentence is bound to a concrete claim and material misreading;
- every retained stand-alone negative caveat is covered by an exact frozen author-intent proposition rather than by an agent's own prudential preference;
- any full-draft output has an input audit, argument spine, table/figure placement plan, and an unresolved non-semantic `TODO` list when needed; semantic or evidence gaps retain `clarification_required` or `evidence_conflict` and keep the affected prose unwritten;
- any applicable convergence module was loaded selectively rather than imposed on an unrelated local edit;
- any proposal distinguishes completed, preliminary, planned, and expected results and supplies executable stages, risks, fallbacks, and deliverables when required;
- any theory-to-empirical claim has a recoverable concept-to-measure link, and any normative policy claim states the relevant social-private wedge and implementation conditions;
- any final consistency matrix, scope contract, or stop decision remains author-facing and does not leak into the manuscript;
- any prose revision removes vague, inflated, AI-like, or translation-like wording;
- any drafted or revised paragraph grounds abstract concepts, states needed comparisons, keeps design separate from findings, explains mechanism links rather than relabeling heterogeneity, and uses stable terminology;
- no paper-facing paragraph, table note, or figure note contains author-facing workflow notes, draft-management explanations, or internal discussion with the author;
- any remaining material uncertainty is handled at its first genuinely necessary reader-facing location or in an author-facing next-step record, without mechanically repeating the same limitation throughout the manuscript.
