# Remaining questions and unresolved hypotheses

Version 4.4-rc1 research record, after review reconciliation. Everything here is open. **Pilot** items are addressed by `EXPERIMENT_CONTRACT.md`; **expanded** items only by the larger experiment; **outside** items need evidence the contract cannot produce.

## Hypotheses carried into the experiment

| ID | Hypothesis | Where tested |
|---|---|---|
| H3 | rc1's routine-task cost stays within 1.25 × 4.3's (median tokens and latency) at equal assurance, despite larger compact and full tiers | Pilot (routine cost gate 1.25 × A1) |
| H5 | The requested/effective notice lowers false acceptance on misrepresented capability fallback | Pilot (F8, F10) |
| H7 | The unified status vocabulary removes compact-tier status errors | Expanded (compact arms fixed by amendment before it starts) |
| H8 | rc1 lowers false acceptance on wrong-mechanism, out-of-scope and correlated-reviewer tasks | Pilot (F2, F3), expanded (F7) |
| H9 | The attribution and scope requirements do not raise false rejection of valid alternatives | Pilot (all valid controls; escalation counts as false rejection) |
| H12 | Adaptive scaffolding is no worse than fixed standard scaffolding at lower or equal cost | Pilot (A4 subset), expanded |
| H13 | rc1 does not fan out on sequential tasks and records a rationale when it does | Pilot transcripts |
| H14 | The stagnation rule stops unproductive loops without stopping productive long investigations | Pilot (F9) |
| H16 | Moving O6 detail out of Tier 1 (keeping short summaries) does not lower adherence | Expanded |
| H17 | Restored 4.3 rules (upward reclassification, exact-action authorization, end-to-end default) behave as in 4.3 | Pilot (R1, R2) |
| H11 | The tutoring preset protects learning | Outside: needs human participants |

Hypotheses H1, H4, H6 and H15 concern document or helper properties. Their record is in `VALIDATION.md` "Version 4.4-rc1 checks" (mechanical checks and author re-inspection). H2 and H10 (independence of the settings) are **not** established: the helper shows only that its own resolver keeps them apart and that each preset sets one dimension. Whether agents treat the settings as independent is part of the pilot transcripts and is otherwise unknown.

## Design questions

1. **Five levels per stage.** Will real owners use per-stage levels, or only presets? If only presets, the per-stage overrides could leave the documented surface.
2. **Stagnation window.** Is two attempts without new evidence too eager for slow but valid investigations? The default is a hypothesis.
3. **Default attempt ceiling.** Twelve attempts on one problem is a guess that bounds runs without a budget. Is it too low for hard debugging or too high for cheap tasks?
4. **Planning clamp.** A requested lighter plan is raised to the class minimum. Is that too strict for experienced owners who plan outside the agent?
5. **Full-tier growth.** COMPOSITION.md adds about 19 KB to the master. Should the master embed only a condensed summary? That would create a second definition, which this candidate otherwise avoids.
6. **Compact tier size (review finding R-17).** 10,239 bytes is 31.4% above 4.3 and above the reviewer's ≈9.5 KB target. The author accepted it provisionally: most of the remainder is the invariants and restored 4.3 lines, and the rest is new rc1 content judged protective (the configuration line, the failure classes, the verification dimensions). Reaching the target would mean dropping some of that. The owner may overturn this. Hypothesis H3's cost gate and the expanded experiment's compact arms will show whether the extra size costs adherence or tokens.
7. **Isolation axes.** Will five axes be reported faithfully, or collapse back into a label?
8. **Same-family agreement counts once.** What counts as the same family for hosts that do not disclose the model?
9. **Revalidation before action.** How should a text-only or offline host revalidate a moving external subject?
10. **Compatibility rules.** Fourteen rules came from the literature, design reasoning and review, not from observed misconfiguration. Which, if any, will matter in practice?
11. **Owner override.** The status cap lets an owner ship without a required check while keeping the record honest. Is a cap enough, or should some gates (security, INV-03) refuse the override outright? Every invariant still binds; the override waives only the check.

## Evidence gaps (from EVIDENCE_BASE.md)

- The OpenAI Linux security post was not fetchable (HTTP 403); its figures rest on secondary coverage. Stage costs, failed-attempt costs, "give up after an hour" and the GPT-6 Cyber system-card figures were not found in any fetched source and were not used.
- No study compares named human–AI collaboration presets for agents, isolates the benefit of planning for coding agents, or establishes retry, stagnation or ceiling thresholds.
- The RS-WF-1 project-local adaptation referred to by one report was not located.
- No token counts exist for any tier, only byte counts.

## Process limits of this candidate

- The rc1 author, the fresh-context reviewer and the re-inspector share a model family, and separation was cooperative. The verification review's ten fixes were not re-reviewed.
- No withheld acceptance cases exist yet. They must be written after the freeze, by someone other than the designer, to count as withheld.
- No agent trial of 4.3 or rc1 has been run; every behavioural statement is a design claim.
