# Controller Startup Checklist

## Purpose

Run this checklist before any multi-agent or staged-agent economics writing task. It prevents the controller from jumping directly into drafting before the shared state, section boundaries, and cross-agent rules are active.

## Startup Steps

1. Confirm this task is large enough for `econ-writing-workflow-multiagent`.
   - If it is a short polish, one abstract, one table note, or one caption, route to the stable workflow or a child skill instead.

2. Activate the controller role.
   - The controller owns `paper_state`, section cards, cross-agent requests, integration, conflict resolution, and final user-facing output.

3. Read the nearest project instructions and classify the artifact task.
   - Record `task_mode`, whether an accepted mature baseline exists, and the default `rewrite_mode`.
   - Do not infer permission to shorten from a request to improve structure or prose.

4. Create the artifact contract when the task is a full draft, mature revision, restructuring, shortening, or appendix relocation.
   - Load `artifact_conservation_and_depth_gates.md`.
   - Fix the accepted baseline path and hash, measurement method, target basis, approval triggers, and `must_remain_main` objects.
   - Measure the baseline before delegation. Record unavailable or ambiguous metrics instead of substituting zero.

5. Load or create `paper_state`.
   - Use `paper_state_protocol.md`.
   - Mark missing facts as concrete `TODO` items.
   - Do not invent data, citations, results, mechanisms, or sample details.

6. Decide which coordination mode is needed.
   - Functional-only: table/figure, literature, argument logic, diction, empirical review.
   - Section-agent mode: abstract, introduction, literature, theory/mechanism, empirical design, main results, mechanism, heterogeneity, robustness, conclusion.
   - Full workflow: result package to paper draft or major revision.

7. Create section cards when section agents are needed.
   - Use `section_agent_protocol.md`.
   - No section agent drafts before receiving a controller-approved section card.
   - For mature drafts, include rewrite mode, baseline/target range, `must_remain_main`, allowed appendix moves, and a ledger slice.

8. Use controller-mediated cross-agent collaboration when needed.
   - Use `cross_agent_collaboration_protocol.md`.
   - Section agents may request functional review, but only the controller updates `paper_state`, table/figure placement, or section cards.

## Startup Output

Before delegating, produce or internally maintain:

```text
coordination_mode:
paper_state_status:
artifact_contract_status:
baseline_main_length:
target_main_length:
rewrite_mode:
compression_permission:
must_remain_main:
approval_triggers:
section_agents_needed:
functional_agents_needed:
first_handoff:
blocking_todos:
```

## Stop Conditions

Pause and ask the user or return a bounded plan if:

- research question, main result, data/sample, or identification/model facts are missing for a requested full draft;
- a requested claim depends on unavailable literature or uninspected sources;
- a mature-manuscript restructuring may materially shorten the main text but has no accepted baseline, target, or approval scope;
- the baseline, appendix boundary, or required page metric is unavailable or ambiguous and the proposed edit would cross an artifact gate;
- the task appears to be paid ghostwriting, fabricated research, or academic misconduct;
- the user requests empirical estimates that have not been produced.
