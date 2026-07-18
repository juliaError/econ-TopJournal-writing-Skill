# Integration And Conflict Resolution

## Integration Order

The controller integrates in this order:

1. user instructions;
2. `paper_state`, including its artifact contract and recorded approvals;
3. the accepted baseline and conservation ledger;
4. inspected tables, figures, data notes, manuscript text, and source materials;
5. specialized role findings;
6. prose preferences and style compression.

If a prose suggestion conflicts with a paper fact, the paper fact wins.

## Common Conflicts

- Contribution conflict: one role narrows or expands the claim.
- Result conflict: prose differs from table values or notes.
- Mechanism conflict: mechanism prose is not supported by theory or result evidence.
- Placement conflict: table/figure role moves an item that drafting role relies on.
- Language conflict: diction role smooths away a caveat or secondary contribution.
- Literature conflict: contribution claim is stronger than inspected literature supports.
- Artifact-budget conflict: the integrated candidate falls below a target, hard floor, or unapproved cumulative-reduction threshold.
- Main-versus-appendix sufficiency conflict: material still exists but the main text can no longer explain a central data, model, design, result, or limitation without the appendix.

## Resolution Rules

- Resolve contribution conflicts by returning to `main_contribution`, `secondary_contributions`, and `scope_conditions_and_caveats`.
- Resolve result conflicts by inspecting the table, figure, variable definition, and sample note.
- Resolve mechanism conflicts by checking the mechanism chain and whether evidence is direct, indirect, or only suggestive.
- Resolve placement conflicts by asking whether the item supports the argument spine or only documents robustness.
- Resolve language conflicts by restoring the substantive claim in compressed form.
- Resolve literature conflicts by weakening the claim or marking a `TODO` for source verification.
- Resolve artifact-budget conflicts by restoring accepted material, narrowing the proposed compression, or obtaining a scoped user approval. Do not change the baseline to clear the gate.
- Resolve main-versus-appendix conflicts by restoring a sufficient main-text explanation or reversing the move. Appendix existence alone does not resolve the conflict.

Do not send a failing candidate to diction or final consistency. Run the deterministic audit and Main-Text Sufficiency and Conservation Role after integration. Treat `metric_unavailable` as a stop condition, not a pass.

## Final Integration Output

For large tasks, return:

```text
Integrated decision:
What changed:
What was preserved:
Artifact-gate status:
Conservation-ledger status:
Conflicts resolved:
Remaining TODOs:
Next recommended pass:
```

Do not expose long internal role transcripts unless the user asks. Summarize what matters for the paper.
