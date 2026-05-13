---
purpose: "Provide executable rules for writing and revising economics paper introductions."
applies_to: "Introduction structure, motivation, contribution framing, and results preview."
last_updated: "2026-05-13"
used_by: "paper_skills"
---

# Introduction Rules

Use this file when drafting, restructuring, compressing, or linting an economics paper introduction.

## 1. First Diagnosis

Before rewriting an introduction, classify the paper as one of:

- pure applied causal paper;
- descriptive measurement / stylized-facts paper;
- theory paper;
- mixed theory-empirical paper;
- structural/counterfactual paper;
- policy or method paper.

Then mark the introduction's protected content:

- main contribution;
- secondary contribution, if any;
- must-preserve mechanism;
- must-preserve empirical magnitude;
- must-preserve data/design feature;
- must-preserve caveat or scope condition.

If these are not explicit, infer them from the current text and preserve them unless the user asks to reframe the paper.

## 2. Speed Without Strategic Loss

The introduction should get to the point quickly, but speed must not come at the cost of erasing the paper's contribution structure.

For papers with both empirical and theoretical contributions, the first 1-2 pages should make both visible:

- what is measured or estimated;
- what the main fact/result is;
- what mechanism explains it;
- why this mechanism matters beyond the immediate data exercise.

If the paper is mixed theory-empirical, do not rewrite it as a pure measurement paper unless the user explicitly requests that reframing.

## 3. Default Introduction Path

Use this order unless the paper type calls for a different emphasis:

1. Hook: the economic puzzle, fact, or tension.
2. Question: what the paper asks.
3. Design or model: how the paper can answer the question.
4. Main result: concrete magnitude, proposition, or counterfactual.
5. Mechanism: why the result arises or what economic force explains it.
6. Contribution: what prior work did not settle and what this paper adds.
7. Scope: the key population, setting, model boundary, or identification caveat.
8. Roadmap: brief and customized.

## 4. Paper-Type Branches

**Pure applied causal paper**:
Move quickly from question to variation and magnitude. Mechanisms and heterogeneity can be shorter unless they are part of the contribution.

**Descriptive measurement / stylized-facts paper**:
Make the data object and measurement contribution visible early. Do not overstate causal interpretation.

**Mixed theory-empirical paper**:
State the mechanism before the reader treats the paper as only a measurement exercise. Map the empirical fact to the economic mechanism.

**Theory paper**:
Start with the puzzle and mechanism, not the literature gap. State the main proposition in plain English before details.

**Structural/counterfactual paper**:
State the object being estimated, why the model is needed, and the main counterfactual result. Do not hide the counterfactual until late in the introduction.

**Policy or method paper**:
State the practical problem, the proposed method or framework, the validation/application, and the usable implication.

## 5. Contribution Preservation Rule

Do not remove a claim if it is one of the paper's central contributions. If space is tight, compress the wording, not the contribution.

When cutting:

- delete generic motivation before deleting the mechanism;
- merge literature sentences before deleting the second contribution;
- shorten data description before deleting the identifying design feature;
- compress caveats into one clause rather than erasing necessary scope limits.

## 6. Drop Check After Rewriting

After rewriting, compare the new introduction with the old one. List any substantive claim, mechanism, data source, magnitude, caveat, or contribution that was dropped.

If a dropped item is central or strategically important, restore it in compressed form. Do this check even if the final answer only briefly says that no central contribution was dropped.

## 7. Original Before/After Example

**Before, over-compressed**:
This paper studies how export shocks affect firm investment. I use customs records and firm balance sheets to show that exposed firms invest less after demand falls.

**Problem**:
The rewrite is concise, but it erases the paper's dynamic mechanism: firms reduce long-term investment because collateral values fall, not only because sales fall.

**After, contribution-preserving**:
This paper studies how export shocks affect firm investment. Linking customs records to firm balance sheets, I show that exposed firms cut investment after foreign demand falls, with the decline concentrated among firms whose collateral values also fall. The result points to a dynamic financing channel rather than a short-run sales response alone.
