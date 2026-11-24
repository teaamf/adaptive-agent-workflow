# Candidate-versus-baseline change summary

Version 4.4-rc1 research record, 18 November 2026, after reconciliation of the fresh-context review. Baseline: 4.3 as preserved in `releases/4.3-baseline/` (manifest digest `2059d8b7…3c55`). Candidate identity: `FREEZE.md`. This summary separates three kinds of statement, as the brief requires:

- **Mechanically validated:** checked by `tools/documents.py check`, the 19 mutation controls of `research/run_rc1_checks.py` (41 records, results in `research/validation/`), and the arm build of `research/build_ablations.py`.
- **Proposed behaviour:** what the documents instruct; not observed in any agent run.
- **Empirical findings:** none yet. The comparison in `EXPERIMENT_CONTRACT.md` has not been run.

## What changed

| Area | Change | Kind |
|---|---|---|
| Mandatory core | Twelve numbered invariants INV-01–INV-12 at the top of WORKFLOW.md; carried by ID in every tier | Exact set and compact presence mechanically validated; wording equivalence reviewed, not proven; behaviour proposed |
| Consequence | One classification (routine, material, consequential) sets the fast path and the assurance floor; reclassify upward when new risk appears, never downward | Proposed |
| Configuration | COMPOSITION.md: participation per stage, cadence/format, scaffolding as new settings; planning and topology derived and clamped; eight-rank precedence with the assurance floor above the contract; owner override caps status, never assurance; 13 compatibility rules; 11 reason codes; five single-dimension workflow presets and five participation presets | Table consistency, single-dimension presets, quoted defaults and 12 resolved examples mechanically validated; agent behaviour proposed |
| Requested/effective/observed | Short notice only on material difference, warning or consequential work; "required: blocked" for unavailable required capability | Resolution mechanically illustrated; behaviour proposed |
| Claim lifecycle | One truth axis plus *inconclusive within budget*; consequence, decision, remediation, applicability and acceptance as separate axes; acceptance recorded, never inferred | Proposed; mapping table in MIGRATION.md |
| Evidence | Oracle identity added; revalidate before irreversible or external action on a moving subject; dedup by root cause | Proposed |
| Verification | Seven dimensions; naming the applicable ones and evidencing each is required, methods are typical; alternatives pass; INV-09 corrects a wrong explanation rather than rejecting an authorized result | Proposed |
| Independence | Five isolation axes; same-family agreement counts once | Proposed |
| Failure and stopping | Nine failure classes with default actions; stagnation window; default ceiling of twelve attempts on one problem; two-sided stopping | Defaults quoted consistently (mechanical); behaviour proposed |
| Human interaction | AGENT_INTERACTION A8 participation and authorship; default works end to end; plan approval covers only exactly named actions; unattended runs defer gated actions | Proposed |
| Compact tier | Rewritten: fixes the seven 4.3 divergences, carries every invariant, restores the 4.3 compact lines the reviews identified | 14 markers and 12 IDs mechanically validated; semantic fidelity reviewed, not proven |
| Terminology | "Profile" now means domain profile only; assurance level, accessibility target | Proposed; aliases in MIGRATION.md |
| Moved detail | Bias table, multi-agent cluster table and practice bullets to PRACTICAL_PLAYBOOKS O6, with a six-line bias list and a one-line cluster summary kept in Tier 1; full metric definitions to PROFILES P3, with one line kept in §10 | Proposed; adherence effect is hypothesis H16 |
| New modules | COMPOSITION.md, GLOSSARY.md (not embedded in the master), MIGRATION.md, examples/CONFIGURATIONS.md | Glossary resolution mechanically validated |
| Tools | documents.py: pinned invariant set, Tier 1 and compact ceilings, version declarations, glossary, composition, fail on missing/empty patterns, scoped link scan. composition.py: new optional helper. run_rc1_checks.py replaces run_v4_3_checks.py and fixes its evidence defects. build_ablations.py builds all arms under one packaging rule with residual checks | Mechanically validated by mutation controls |
| Scenarios | G51–G71 added (public development cases) | Not executed |
| Experiment | Frozen contract: 22-task, 234-trial pilot; expansion | Not run |

## Size

| Measure | 4.3 | 4.4-rc1 | Change |
|---|---:|---:|---:|
| Tier 1 core (WORKFLOW + AGENT_INTERACTION + PROJECT_TEMPLATE) | 39,480 | 39,478 | −2 (−0.0%) |
| WORKFLOW.md | 29,564 | 30,104 | +540 |
| AGENT_INTERACTION.md | 7,791 | 6,992 | −799 |
| Compact tier | 7,791 | 10,239 | +2,448 (+31.4%) |
| Full tier (MASTER_PROMPT.md) | 112,623 | 138,838 | +26,215 (+23.3%) |
| On-demand modules added | — | COMPOSITION 19,063; GLOSSARY 5,691 (not in the master) | — |

Bytes, not tokens; no tokenizer was run. **The mandatory modular core did not grow; the compact and full tiers did.** Growth in the compact tier comes from the invariant list and from restoring the 4.3 compact lines the reviews identified. It fell from 12,427 bytes in the reviewed draft to 10,150, then rose to 10,239 when the verification review's fixes were applied. The reviewer's ≈9.5 KB target (R-17) was not met: the remainder is the invariants, restored 4.3 lines and new rc1 content judged protective (configuration, failure classes, verification dimensions). The size was accepted as a provisional decision, recorded in REVIEW_RECONCILIATION.md, which the owner may overturn. Growth in the full tier is mostly COMPOSITION.md, which a full-tier user loads whether or not they configure anything. Whether that overhead is worth it is part of hypothesis H3 and the routine-task cost gate in the experiment contract.

## Defects in 4.3 addressed (from EVIDENCE_BASE.md)

C1–C7 compact divergences; P1 stale version header (annotated; the record is historical); P2 master contents list in GUIDE.md; P3 "16 KB" stated as 16,000 bytes; P4 overloaded "profile"; P5 overlapping consequence classifiers; K1–K3 self-test evidence defects; K4 silent pass on a missing pattern file; K5 link-scan scope and missing version check. Each is a logically necessary correction, checked mechanically or by inspection: VERIFIED_DOCUMENT_OR_TOOL_FIX at most, never a measured improvement.

## What did not change

Assurance levels and the ratchet; domain profiles P1–P7; UI design protocol and review playbook (version line and a term or sentence only); loading tiers; the improvement protocol's method; delivery statuses; oracle-integrity rules; the security boundary; Markdown-only operation; every 4.3 safeguard and ceremony limit the two reviews identified (restored; removals of pure restatements are listed in MIGRATION.md). No complete sentence-by-sentence comparison has been made.
