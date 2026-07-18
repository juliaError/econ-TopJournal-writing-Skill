# Artifact Conservation And Depth Gates

## Contents

- Core invariants
- Authority and task classification
- Artifact contract
- Safe defaults and approval gates
- Main-text sufficiency
- Conservation ledger
- Section budgets
- Two-pass restructuring
- Deterministic audit and recovery

## Core Invariants

- Treat context and handoff compression as coordination tools, not permission to shorten the reader-facing manuscript.
- For an accepted mature manuscript, default to `patch_existing` or `reorder_existing_blocks`. Use `full_redraft` only when the user authorizes it or the controller records why the existing section is unusable.
- Preserve substantive main-text coverage and the accepted artifact budget unless a higher-priority constraint authorizes a shorter output.
- Treat word and page counts as guardrails, not measures of writing quality. Do not pad a manuscript to satisfy a threshold.

## Authority And Task Classification

Apply artifact constraints in this order:

1. explicit user instruction;
2. the nearest project instructions;
3. verified journal or format requirements;
4. the user-accepted baseline manuscript;
5. conditional skill defaults.

Classify `task_mode` as `full_draft`, `major_revision`, `restructure`, `shorten`, or `local_edit`. Treat a manuscript as mature when it has a user-accepted multi-section draft whose content and architecture are revision inputs rather than disposable notes. Record ambiguity as `metric_status: ambiguous` and pause before destructive restructuring.

## Artifact Contract

Keep the authoritative contract in `paper_state` or a durable project artifact. Use this schema and omit only fields that are genuinely inapplicable:

```text
artifact_contract:
  task_mode: full_draft | major_revision | restructure | shorten | local_edit
  rewrite_mode: patch_existing | reorder_existing_blocks | full_redraft
  mature_baseline: true | false | unknown
  target_journal_or_style:
  inherited_project_constraints:
  baseline_artifact:
    path:
    version_or_hash:
    accepted_by:
  measurement_contract:
    appendix_boundary:
    source_word_method:
    include_resolution_mode:
    pdf_main_page_method:
  baseline_main_source_words:
  baseline_main_pdf_pages:
  target_main_source_word_range:
  target_main_pdf_page_range:
  hard_main_text_floor:
    source_words:
    pdf_pages:
  max_unapproved_main_reduction_pct:
  must_remain_main:
  allowed_appendix_moves:
  user_approved_compression: true | false
  appendix_dependency_tolerance:
  target_basis: user | project_rule | verified_journal | accepted_baseline | default
  approval_record:
    approved_by:
    approved_scope:
    approved_at:
  metric_status: measured | unavailable | ambiguous
```

Do not silently change the baseline or measurement method during a revision. Do not treat an unavailable baseline as zero or as automatic approval.

For deterministic audits, express `must_remain_main` entries as a section title, a label, or `{type: section | label, value: ...}`. Express `allowed_appendix_moves` as approved section titles or labels. Keep `approval_record.approved_scope` narrow, using entries such as `compression`, `move_appendix:<title-or-label>`, `delete:<title>`, or `full_redraft`; do not use `all` unless the user explicitly authorizes that entire scope.

## Safe Defaults And Approval Gates

For a mature baseline with `task_mode` equal to `major_revision` or `restructure`, and no explicit shorter target:

- default to `rewrite_mode: patch_existing`;
- allow `reorder_existing_blocks` during an architecture pass;
- set `max_unapproved_main_reduction_pct` to `0.15`;
- require approval before `full_redraft`;
- require approval before deleting a substantive section or moving central data construction, sample audit, identification/model environment, main results, or core robustness discussion to the appendix.

Treat the 15 percent value as an approval trigger for cumulative net main-text reduction, not a universal target or quality rule. Apply section-deletion and core-object gates even when the total reduction remains below 15 percent.

When the user requests a short paper, note, letter, or verified capped format, record the shorter target and approval scope in the contract. Let that explicit contract override the conditional 15 percent default. Never impose a universal 30-page floor; inherit a page floor only from the user, project, or verified format requirement.

## Main-Text Sufficiency

Require the main text to let a reader answer, without reconstructing the paper from the appendix:

1. What are the research question and contribution?
2. What data, sample, or model environment is used?
3. How is the central object measured or defined?
4. What comparison, accounting map, identification, or mechanism produces the result?
5. What are the main magnitude and benchmark?
6. What are the central threats, robustness results, and sample limitations?
7. Which claims are descriptive, causal, calibrated, conditional, or scenarios?

Allow proofs, supplementary derivations, secondary definitions, extended robustness, and validation detail in the appendix when the main text retains the assumptions, mechanism, proposition interpretation, evidence function, and limitations needed for those answers.

## Conservation Ledger

Maintain the complete ledger outside agent prompts. Give each role only the slice it needs.

```text
source_block_id:
source_function:
disposition: unchanged | revised | reordered | merged | moved_appendix | deleted
destination:
main_text_replacement_or_summary:
reason:
approval_required:
approval_status:
```

Assign stable block IDs before restructuring. Map every old substantive block to a disposition. Do not accept “still exists in the appendix” unless the ledger identifies what explanation remains in the main text. Require controller approval for merges or renames that prevent deterministic title matching.

## Section Budgets

Add these fields to every mature-draft section card:

```text
baseline_words:
target_word_range:
maximum_reduction_pct:
minimum_depth_questions:
must_remain_main:
allowed_appendix_moves:
rewrite_mode:
ledger_slice:
```

Use ranges and substantive questions rather than mechanical quotas. Return large deviations to the controller before integration. Do not assume another section preserves an omitted object without a verified destination in the section map and ledger.

## Two-Pass Restructuring

For major restructuring:

1. Run an architecture pass that reorders the complete accepted material and edits only transitions, duplicated signposting, and changes needed to make moved blocks coherent.
2. Measure and audit the complete reordered manuscript.
3. Run a separate compression pass that removes genuine duplication within the artifact contract.

Do not combine clean-slate rewriting, block relocation, table/figure migration, and diction compression in one pass.

## Deterministic Audit And Recovery

Run `scripts/audit_manuscript_conservation.py` after architecture integration, after compression integration, and before finalization. Interpret its statuses as follows:

```bash
python scripts/audit_manuscript_conservation.py \
  --baseline baseline.tex \
  --candidate candidate.tex \
  --project-root /path/to/project \
  --contract artifact_contract.json \
  --report conservation_audit.json
```

Use `--baseline-main-pdf-pages` and `--candidate-main-pdf-pages` only for page counts measured with an explicit appendix boundary. Never substitute total PDF pages. Use `--appendix-marker`, `--word-metric`, `--max-main-reduction`, and hard-floor flags only when they agree with the recorded measurement contract. Require exactly one uncommented appendix marker in each expanded source; otherwise treat the metric as unavailable.

- `pass`: deterministic gates are satisfied; still run the semantic sufficiency role.
- `approval_required`: preserve or restore material, or obtain and record user approval before continuing.
- `fail`: restore missing or under-floor material before diction or finalization.
- `metric_unavailable`: repair the baseline, appendix boundary, include graph, or page measurement; do not treat the result as a pass.

Treat exit codes `0`, `1`, `2`, and `3` as `pass`, `fail`, `approval_required`, and `metric_unavailable`, respectively. Read the JSON report rather than inferring status from console wording.

Keep private manuscripts and copyrighted fixtures local. Commit only synthetic tests. If a candidate fails, restore baseline blocks or revise the contract through the authority order; never change the baseline merely to make the audit pass.
