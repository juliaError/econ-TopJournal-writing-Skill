---
purpose: "Provide a checklist-style linter for revising economics paper prose and structure."
applies_to: "Revision passes, section audits, manuscript linting, and final pre-submission checks."
last_updated: "2026-05-13"
used_by: "paper_skills"
---

# Revision Linter

Use this checklist after rewriting an abstract, introduction, conclusion, or manuscript section. Load it with the relevant section file, especially `03_abstract_rules.md` and `04_introduction_rules.md`.

## 1. Contribution Preservation Check

Before accepting a rewrite, answer:

- Did the rewrite preserve the main contribution?
- Did it preserve any secondary contribution that the old version clearly emphasized?
- Did it preserve the paper's mechanism?
- Did it preserve key magnitudes?
- Did it preserve necessary data/design features?
- Did it preserve necessary caveats about causality, scope, or interpretation?
- Did concision improve clarity without narrowing the paper's intellectual claim?

If any answer is no, revise again. Compress wording, not the contribution.

## 2. Paper-Type Check

Confirm the rewrite still matches the paper type:

- pure applied causal paper;
- descriptive measurement / stylized-facts paper;
- theory paper;
- mixed theory-empirical paper;
- structural/counterfactual paper;
- policy or method paper.

Flag a rewrite if it turns a mixed theory-empirical paper into a pure measurement paper, a measurement paper into an overclaimed causal paper, or a structural paper into a reduced-form summary.

## 3. Drop Check

After rewriting, compare the new version with the old version. List any dropped:

- substantive claim;
- mechanism;
- data source or data object;
- magnitude or economic significance;
- identification or design feature;
- caveat or scope condition;
- contribution sentence.

Restore dropped items that are central or strategically important. Items may be restored as clauses rather than full sentences.

## 4. Concision Check

The rewrite should still be concise:

- no vague motivation;
- no empty contribution language;
- no generic roadmap;
- no passive filler;
- no overclaiming;
- concrete magnitudes early when available;
- reader-first / newspaper order.

Concise does not mean strategically incomplete.

## 5. Abstract-Specific Linter

- Default target is 100-150 words, not a hard cap unless the journal imposes it.
- 150-180 words is acceptable for multi-contribution, mixed theory-empirical, structural, or mechanism-centered papers if every sentence has a distinct function.
- The abstract states the question, design/model/measure, main finding, and contribution.
- Mechanism, counterfactual, or secondary contribution is preserved when it is part of the claim.

## 6. Introduction-Specific Linter

- The first 1-2 pages reveal the paper's contribution structure.
- Main result and magnitude appear early.
- Empirical object/design and mechanism are both visible for mixed theory-empirical papers.
- Literature positioning does not crowd out the main result or mechanism.
- Roadmap is customized and short.

## 7. Conclusion-Specific Linter

- The conclusion restates the finding in new language.
- It preserves necessary scope, causality, or interpretation caveats without adding a formulaic limitations section.
- It does not add new results, unsupported implications, or generic future-work filler.

## 8. Minimal User-Facing Summary

When reporting a rewrite, briefly state:

- what was compressed;
- what protected contribution or mechanism was preserved;
- whether any old claim was dropped and why.

Do not expose a long internal audit unless the user asks for it.
