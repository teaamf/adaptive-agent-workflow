# Validation scope

Updated 18 November 2026 for the 4.4-rc1 experimental candidate. This report concerns the workflow document package, not an executed project or cross-host performance benchmark. Earlier version checks below are retained as history.

The mechanical checker validates master/companion consistency, local file links and a narrow guard against known historical product-name/requirement leakage. That last guard cannot detect all semantic project assumptions; author review is also needed.

The public generality cases G01–G18 were inspected against the rules, not executed as independent agent trials. Core §§2–4 distinguish project scope, assurance and actual capability; §7 supports existing projects and non-software deliverables; §§9–12 distinguish evidence, validity and scoped completion. PROFILES supplies task-specific methods without importing a product catalogue. This is author scenario inspection, not an independent certification.

No project was built, deployed or certified. No user study, controlled multi-project comparison or actual cross-host integration trial was performed. Future trials should use fresh cases, applicable domain expertise and the controls in CONTINUOUS_IMPROVEMENT.md.

The previous MolliKey package is preserved separately; the new package does not load it. Its 24 distributable files were compared byte-for-byte with its existing v3 ZIP and remain unchanged.

## Historical version 4.0 maintenance checks

- At version 4.0, the self-contained master matched its launch file and six canonical modules.
- Active local Markdown links resolve. This does not verify remote availability or every fragment anchor.
- The optional skill passed the Skill Creator frontmatter/discovery validator.
- The document helper ran in a relocated copy from a different working directory without changing the source package.
- A changed module caused a stale-master failure; assembly restored consistency.
- Deliberately introduced historical project-specific content was rejected even after assembly.
- A missing canonical module and a broken local link were each detected; clean checks passed after restoration.
- Ten helper invocations produced the expected exit results. These are document-tool checks, not ten development projects or agent trials.
- All 450 supplied design-advice title entries remain in the optional reference index.

Raw maintenance results are recorded in [research/document-check-results.json](research/document-check-results.json). The initial general draft and first research revision remain available as provenance. No runtime controller or certification service is included.


## Version 4.1 merge checks

The master now embeds seven canonical modules, including PRACTICAL_PLAYBOOKS.md. The updated master/companion and local-link checks passed. The optional skill validator passed. A relocated copy was checked, a modified playbook caused a stale-master failure, and a missing playbook was rejected; clean checks passed after restoration. These checks establish document maintenance behavior, not evidence truth or agent execution.

The two older source folders were compared to the pre-merge hash inventories and remain byte-for-byte unchanged. The pre-merge general package is preserved in its separate snapshot ZIP. No old checker, bytecode cache, synthetic passing report or live run-state fixture is included in the merged distributable.

The old checker was actually run read-only on its synthetic review fixture and returned LOCAL_READINESS with its structural-only caveat. This observed result motivated the new false-evidence example. Cases G19–G21 were inspected against playbooks O3–O4 and the core applicability rules; they were not run as independent agent trials. Their expected rejection is a protocol requirement, not an implemented semantic validator.

## Version 4.2 checks

The master now embeds eight canonical modules, adding AGENT_INTERACTION.md. The pre-edit package was snapshotted as `AdaptiveAgentWorkflow-pre-v4.2.zip` beside the directory. After reassembly, the document checker's consistency, link and leakage checks were rerun. New cases G22–G31 were inspected against the revised rules by the author. They were not run as agent trials. No new rule has comparative evidence in this package; see RESEARCH_AND_CHANGES research cycle 3 for sources and limits.

**Portability pass.** An audit of the operational files found four kinds of problem:

- leftovers from the origin project: a keyboard-specific UI example and a README reference;
- a project-specific guard hard-coded in the helper;
- vendor-specific instruction-file names in core rules;
- only one single-file tier, the 94 KB master, which is too large for small-context models.

Fixes:

- The leftovers were removed.
- The guard patterns moved to the editable `tools/portability_patterns.txt`. They now also cover vendor and model names and machine paths, and every operational file is scanned, not only the master.
- COMPACT_PROMPT.md was added (about 6.9 KB, with a 16 KB budget and required-rule markers checked).
- HOST_ADAPTERS gained loading tiers and a model-capability table.
- Portability cases G32–G36 were added.

Negative controls:

- A vendor name inserted into a module was rejected.
- A compact prompt missing a required rule was rejected.
- The original README leftover was detected before it was fixed.

These are document checks. The workflow has not been run on different models or hosts in this package, so cross-model behavior remains untested.

See [MERGE_DECISIONS.md](MERGE_DECISIONS.md) for accepted/rejected material and [research/merge-check-results.json](research/merge-check-results.json) for completed maintenance results.

## Version 4.3 checks

The pre-edit v4.2 document check passed. Its 26 source files were preserved in [research/AdaptiveAgentWorkflow-pre-v4.3.zip](research/AdaptiveAgentWorkflow-pre-v4.3.zip) before editing. Revision scope and acceptance were recorded in [research/v4.3-plan.md](research/v4.3-plan.md).

The master now embeds ten canonical modules, adding WORKFLOW_CONFIGURATION.md and UI_REVIEW_PLAYBOOK.md. The original checkout passed the updated consistency, local-link, compact-rule/byte-budget and portability checks. The optional skill passed the installed Skill Creator frontmatter validator. The compact tier is 7,791 UTF-8 bytes against a 16,000-byte ceiling; no model-token count was measured.

A copy in an explicitly writable artifacts directory was checked from a different working directory. Fifteen recorded checks passed:

- clean relocated package;
- rejection of a stale master, a broken local link, provider-name leakage and a lost compact safeguard;
- rejection when either new canonical module was absent;
- a clean pass after restoring each of those six negative controls;
- valid skill frontmatter in the deployment folder and a folder name matching its declared name.

The initial default temporary directory denied a nested write before any control ran. The test was moved to the permitted artifacts directory; this setup failure is retained in the report. The relocated copy was removed after verification. Negative controls changed only the temporary copy, not the delivered package.

Raw outputs, expected/actual exit codes and sizes are in [research/v4.3-check-results.json](research/v4.3-check-results.json). `research/run_v4_3_checks.py` (preserved in the 4.3 baseline; superseded in 4.4-rc1 by `research/run_rc1_checks.py`) reproduces these maintenance controls given an authorized temporary root and a skill-validator path. It is a research helper, not a runtime prerequisite.

The author inspected G37–G50 against the new procedures and checked the core/compact/skill routing for consistency. These are public scenario inspections, not independent agent executions. No live UI was refined, no model council ran, and no human usability study, independent review or multi-host/model/language trial was performed. This revision establishes a consistent, inspectable procedure; reduced cost, higher visual quality and improved transfer remain hypotheses for a controlled evaluation.

## Version 4.4-rc1 checks

18 November 2026. 4.4-rc1 is an experimental candidate; nothing here is evidence that it works better than 4.3. Statements fall into four kinds, kept apart as the owner's brief requires.

**Mechanically validated (document and tool properties only).**

- `tools/documents.py check` passes on the frozen tree. It checks: the master against eleven modules and LAUNCH.md; the invariant set exactly INV-01 to INV-12 and every ID in the compact tier; the 14 compact markers; the compact ceiling of 10,500 bytes (actual 10,239); the Tier 1 ceiling of 39,480 bytes (actual 39,478); version declarations; local links; glossary sections; and, through `tools/composition.py`, table consistency, single-dimension presets, WORKFLOW §11 quoting the K5 defaults, resolver independence and twelve re-derived example configurations.
- `research/run_rc1_checks.py` ran 19 mutation controls on an isolated copy. Each control had to make the check fail with a specific message and then pass again once restored. Together with the clean relocated run, the frontmatter check and the exact-restore check, that gives 41 records, all passed. The run-stamped JSON is in `research/validation/`, together with the manifest of the tree it tested. That manifest is of the tree before the results were added; `FREEZE.md` records the final tree.
- `research/build_ablations.py` built all five arm packages (A1–A5) under one packaging rule. Each edited tree passed its own document check, and each ablation's residual-text patterns found nothing. The summary is `research/validation/arms.json`; the hashes are in `FREEZE.md`.
- The 4.3 baseline still matches its manifest (`releases/4.3-baseline/SHA256SUMS`, digest `2059d8b7…3c55`).

These support at most VERIFIED_DOCUMENT_OR_TOOL_FIX for the defects they address (CONTINUOUS_IMPROVEMENT C4).

**Author re-inspection, not agent execution.** G11, G19, G21, G25 and G27 were re-read against the rc1 rules (hypothesis H6). Each reaches the same verdict as under 4.3, in the unified vocabulary:

| Case | 4.3 verdict | rc1 rule and state |
|---|---|---|
| G11 unchanged candidate, new session | Revalidate; do not discard for session identity | §9 "Correctly bound evidence survives a new session after revalidation"; truth stays *supported within scope* after revalidation |
| G19 placeholder bundle, "tests passed" only | Insufficient for acceptance | §9 evidence fields, §10 "A green suite is evidence only about what it exercises", INV-06; truth *evidence pending*; acceptance *not accepted* |
| G21 one hashed log for many claims | Digest reuse is not coverage | §9 "A digest proves identity, not that the right behavior was evaluated"; each claim keeps its own truth state |
| G25 progress note says F3 passes | Recheck reality; downgrade without end-to-end evidence | A4 resume routine; §13 ledger "passes only on end-to-end evidence"; F3 becomes *evidence pending* |
| G27 intermittent test passes on the third rerun | Not green; unresolved nondeterminism | §11 "Never rerun unchanged conditions until lucky success", pause trigger "intermittent results", Unreliable oracle class; truth *inconclusive within budget* |

G51–G71 were written for rc1 and inspected by their author only. The re-inspector shares a model family with the author of the rules and the fresh-context reviewer; this is cooperative evidence.

**Proposed behaviour.** Everything the documents instruct an agent to do, including configuration notices, participation, scaffolding, stopping, and attribution and scope checks at acceptance, has not been observed in any agent run.

**Empirical findings.** None. The pilot in `research/EXPERIMENT_CONTRACT.md` is frozen and has not been run.

**Review.** A fresh-context review (same model family, cooperative separation) found 28 defects, and all were reconciled (`research/REVIEW_RECONCILIATION.md`). A second fresh-context review, again in the same family with cooperative separation, verified the reconciliation and found ten new defects (one major). All ten were fixed before the current freeze and were not re-reviewed (`research/REVIEW_RECONCILIATION.md` "Verification review"; both review texts are in `research/reviews/`).
