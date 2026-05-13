---
purpose: "Provide executable rules for writing and revising economics paper abstracts."
applies_to: "Abstract drafting, abstract revision, and abstract linting."
last_updated: "2026-05-13"
used_by: "paper_skills"
---

# Abstract Rules

Use this file when drafting, compressing, or linting an economics paper abstract.

## 1. Contribution Structure Diagnosis

Before rewriting, classify the paper as one of:

- pure applied causal paper;
- descriptive measurement / stylized-facts paper;
- theory paper;
- mixed theory-empirical paper;
- structural/counterfactual paper;
- policy or method paper.

Then identify:

- main contribution;
- secondary contribution, if any;
- must-preserve mechanism;
- must-preserve empirical magnitude;
- must-preserve data/design feature;
- must-preserve caveat or scope condition.

If the user does not provide this information explicitly, infer it from the existing abstract, introduction, tables, figures, and project notes. Protect these items before cutting words.

## 2. Length Rule

Default target: 100-150 words.

This is a default, not a hard cap, unless the journal explicitly imposes it. For papers with more than one central contribution, mixed theory-empirical papers, structural papers, or papers where the mechanism is part of the contribution, 150-180 words is acceptable if every sentence carries a distinct function.

Retain the old strengths: short, concrete, front-loaded, and non-generic. Do not let a 150-word target delete the mechanism, the second contribution, or the scope condition when those are part of the intellectual claim.

## 3. Compression Rule

Do not remove a claim if it is one of the paper's central contributions. If space is tight, compress the wording, not the contribution.

For mixed theory-empirical papers, preserve at least one sentence or clause for:

- the empirical object or design;
- the main magnitude or fact;
- the economic mechanism;
- the scope/caveat if identification is limited.

For papers with dynamic, theoretical, or mechanism contributions, do not omit the mechanism merely because the empirical finding is easier to summarize.

## 4. Abstract Templates By Paper Type

**Pure applied causal paper**:
Question -> design/variation -> main estimate -> mechanism or heterogeneity -> implication.

**Descriptive measurement / stylized-facts paper**:
Question -> data/measure -> main fact/magnitude -> why the measurement matters -> scope caveat if needed.

**Mixed theory-empirical paper**:
Question -> model mechanism -> data/measure -> main fact/magnitude -> mechanism implication.

**Theory paper**:
Puzzle -> mechanism -> main proposition -> economic implication.

**Structural/counterfactual paper**:
Question -> model/data -> estimated object -> main counterfactual -> implication.

**Policy or method paper**:
Problem -> proposed method/framework -> validation/application -> practical implication.

## 5. Sentence Function Check

Each sentence should do one job:

- question or puzzle;
- data, design, model, or measure;
- main fact, estimate, proposition, or counterfactual;
- mechanism, interpretation, or economic force;
- implication, contribution, or scope.

Delete sentences that only announce importance, novelty, or broad motivation. Keep sentences that protect the contribution structure.

## 6. Drop Check After Rewriting

After rewriting, compare the new abstract with the old abstract or source text. List any substantive claim, mechanism, data source, magnitude, caveat, or contribution that was dropped.

If a dropped item is central or strategically important, restore it in compressed form. The user-facing response may summarize this briefly, but the workflow must perform the comparison before finalizing.

## 7. Original Before/After Example

**Before, over-compressed**:
This paper studies how municipal audits affect local borrowing. Using a staggered rollout, I find that audits reduce new debt issuance by 8 percent.

**Problem**:
The revision preserves the estimate but deletes the secondary contribution: the dynamic mechanism by which audits shift borrowing toward off-budget vehicles.

**After, contribution-preserving**:
This paper studies how municipal audits affect local borrowing. Using a staggered rollout, I find that audits reduce new debt issuance by 8 percent but shift part of financing toward off-budget vehicles. The pattern shows how oversight can discipline visible debt while leaving substitution margins open.
