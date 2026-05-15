# English Economics Revision Linter

## Principle

Run this linter after drafting or rewriting English economics prose. The goal is not to make prose ornate. The goal is to make claims precise, concrete, and credible.

## Check 1. Vague Aim

- Flag: `aim to investigate`, `try to explore`, `conduct an in-depth study`.
- Fix: replace with the research action and object.
- Check standard: the sentence names X, Y, and setting.
- Original repair: `This paper estimates the effect of [X] on [Y] in [setting].`

## Check 2. Empty Contribution

- Flag: `fills a gap`, `enriches the literature`, `important theoretical and practical significance`.
- Fix: state the exact margin added.
- Check standard: contribution survives without "important" or "novel."
- Original repair: `The paper adds evidence on [mechanism] using [data/design].`

## Check 3. Method Without Identification

- Flag: `uses OLS/DiD/IV to analyze`.
- Fix: state the source of variation or identifying assumption.
- Check standard: reader can see the comparison.
- Original repair: `The design uses [shock/timing/threshold] to compare [units].`

## Check 4. Significant Without Magnitude

- Flag: `significant effect`, `positive impact`, `obvious influence`.
- Fix: add sign, size, and baseline.
- Check standard: result still informs if all significance language is removed.
- Original repair: `[X] increases [Y] by [amount], or [percent] of the pre-treatment mean.`

## Check 5. Overclaiming

- Flag: `prove`, `fully demonstrate`, `reveal the law of`, `confirm the mechanism`.
- Fix: use `estimate`, `show`, `provide evidence`, or `is consistent with`.
- Check standard: claim matches design strength.
- Original repair: `The evidence is consistent with [mechanism], but does not rule out [alternative].`

## Check 6. Passive Filler

- Flag: `it is found that`, `it can be seen that`, `it should be noted that`.
- Fix: put the economic object or result in subject position.
- Check standard: sentence can start with the actor, variable, policy, or estimate.
- Original repair: `[Policy] reduces [outcome] among [group].`

## Check 7. Translationese

- Flag: broad openers such as `with the development of`, `under the background of`, `based on the reality of`.
- Fix: start with the institutional change, friction, or empirical object.
- Check standard: first noun is an economic object, not a broad context.
- Original repair: `[Institutional change] altered [actor]'s cost of [action].`

## Check 8. Template Signposting

- Flag: `the remainder of this paper is organized as follows` when it only lists section numbers.
- Fix: make the roadmap substantive or delete it.
- Check standard: each roadmap clause names a paper-specific landmark.
- Original repair: `Section 2 describes the policy rule that generates the empirical comparison.`

## Check 9. Jargon Without Payoff

- Flag: unnecessary terms that do not sharpen the claim.
- Fix: use simple words unless a technical term is needed.
- Check standard: technical term either names a method, model object, or literature concept.
- Original repair: `firms reduce investment` instead of `economic agents optimize intertemporally` when no model needs the latter.

## Check 10. Unbounded External Validity

- Flag: `the results apply broadly`, `this proves that policy works`.
- Fix: state population, period, and design scope.
- Check standard: reader knows where the result speaks most directly.
- Original repair: `The estimates apply most directly to [population] during [period].`

## Check 11. Author Memo In Manuscript

- Flag: `to satisfy the call for papers`, `for the special issue`, `this draft chooses to`, `for space we move`, `we do not discuss here because`, `the author should add`, `this section is kept/dropped`, `we frame it this way`.
- Fix: move draft-management content to an author memo, or rewrite the economics point as reader-facing scope, identification, contribution, or appendix cross-reference.
- Check standard: a referee can read the sentence without seeing the author-agent conversation.
- Original repair: `Appendix C reports robustness checks using alternative samples, weights, and exposure measures.`
