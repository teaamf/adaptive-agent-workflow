# Architectural decision records for 4.4-rc1

Version 4.4-rc1 research record. Every decision here is a **candidate** decision: it is implemented in rc1 so that it can be evaluated, not accepted. Full rationale, rejected alternatives and cited evidence for ADR-01 to ADR-10 are in `EVIDENCE_BASE.md`; this file records what rc1 actually implemented, where it deviates from the evidence base, and how each decision is checked. Hypothesis IDs (H1–H16) refer to `EVIDENCE_BASE.md` and are carried into `EXPERIMENT_CONTRACT.md`.

Each decision is classed by the kind of support it can get:

- **Mechanical:** a logically necessary property that `tools/documents.py check` or `research/run_rc1_checks.py` verifies. Under CONTINUOUS_IMPROVEMENT C4 this can support at most VERIFIED_DOCUMENT_OR_TOOL_FIX.
- **Empirical:** a behavioural claim that only the frozen experiment can support.

| ADR | Decision as implemented | Where | Deviation from the evidence base | Support |
|---|---|---|---|---|
| ADR-01 | One glossary placing every existing noun in one of eight categories, one defining section per term; other methods' roles map onto existing responsibilities | GLOSSARY.md | The brief's "fundamental entities and responsibilities" are listed as two categories (Entity, Responsibility) plus a separate Invariant category, giving ten labels in the table; the eight-category meaning is preserved | Mechanical: every term resolves to an existing section, no term defined twice (H1) |
| ADR-02 | Three new settings only: participation (per stage), cadence and format, scaffolding. Planning depth and topology are derived and requestable but clamped. Assurance, domain profiles and tier stay as in 4.3. Each workflow preset sets one dimension | COMPOSITION.md K1–K5, K8 | Added `action_log` (rules C-04, C-05) and `attended` keys. A requested lighter plan is clamped up to the class minimum. After review: presets reduced to one dimension each; `minimal` never changes the path | Mechanical: single-dimension presets and resolver independence (a helper property only; H2 itself is not established); token cost empirical (H3) |
| ADR-03 | One precedence list of eight ranks, with the assurance floor above the contract; any layer may be stricter; model capability never lowers assurance; owner override caps status, never assurance | COMPOSITION K6, INV-07, INV-11 | After review: floor moved above the contract; owner-override rule added | Floor clamping and preset/explicit override illustrated mechanically (H4); contract, permission and standing-preference layers are not modelled by the helper |
| ADR-04 | Requested, effective and observed configuration; notice only on material difference or consequential work; eleven reason codes; required-but-unavailable shown as "required: blocked" | WORKFLOW §2, COMPOSITION K6, PRACTICAL_PLAYBOOKS O3 | None | Examples 1 and 3 mechanical; behaviour empirical (H5) |
| ADR-05 | One truth axis with *inconclusive within budget*; consequence, decision, remediation, applicability and acceptance tracked separately; delivery status and report buckets are views; acceptance is recorded, never inferred | WORKFLOW §9, MIGRATION.md mapping | After review: acceptance axis added; decision values act / defer / accept risk | Re-inspection of G11, G19, G21, G25, G27 recorded in VALIDATION.md (H6); compact vocabulary errors empirical (H7, expanded) |
| ADR-06 | Seven verification dimensions; naming the applicable ones and evidencing each is required, methods are typical; criteria are properties of results; valid alternatives pass; results resting on prohibited, out-of-scope or unsupported mechanisms are not accepted, while a wrong explanation is corrected and re-assessed; isolation reported on five axes; same-family agreement counts once | WORKFLOW §6, §10, INV-09 | After review: methods by level made typical rather than mandatory; INV-09 reworded | Empirical (H8 false acceptance, H9 false rejection) |
| ADR-07 | Per-stage participation on five levels; five presets; authorship invariants; tutoring and co-creation behaviour rules; unattended runs defer gated actions; `propose` at the decide stage covers only consequential and owner-kept decisions | AGENT_INTERACTION A3, A8; COMPOSITION K1 | Tutoring sets execute to `assist`. Compatibility rules C-01 to C-14 replace the evidence base's prose list | Resolver independence only (H10 not established); learning behaviour needs human participants (H11, not in pilot) |
| ADR-08 | Scaffolding as a policy chosen from six inputs; capability can lighten procedure, never assurance; escalate within a task, reduce between tasks only on recorded evidence; smallest eligible team with recorded rationale | WORKFLOW §5, COMPOSITION K4, HOST_ADAPTERS | None | Empirical (H12 via ablation A4, H13) |
| ADR-09 | Nine failure classes with default actions; stagnation window; default total ceiling of twelve attempts on one problem; two-sided stopping; logged escalation | WORKFLOW §11, AGENT_INTERACTION A6, COMPOSITION K5 | Numbers kept as labelled defaults, held once in K5 and quoted by §11. After review: external dependency and unknown classes added; finite default ceiling | Quoting mechanical; behaviour empirical (H14) |
| ADR-10 | Consolidations: one consequence classification; one claims-within-evidence invariant; compact parity by invariant ID; "profile" disambiguated; unified lifecycle; one glossary; judgment and coordination tables moved to PRACTICAL_PLAYBOOKS O6, with short summaries kept in Tier 1; helper evidence fixed | WORKFLOW §0, §3; INV-06; COMPACT_PROMPT; O6; tools | After review: every dropped 4.3 safeguard restored; removals of restatements listed in MIGRATION.md | Mechanical (H15: Tier 1 39,478 ≤ 39,480 bytes; compact 10,239 ≤ 10,500 bytes with all IDs); adherence empirical (H16) |
| ADR-11 | Twelve numbered mandatory invariants at the top of the core, carried by ID in every tier | WORKFLOW "Mandatory invariants", COMPACT_PROMPT §1 | Added during implementation to make ADR-10's compact parity checkable | Mechanical: exact set INV-01..INV-12 pinned in the tool; each ID present in compact and master; wording equivalence not checked |
| ADR-12 | COMPOSITION.md tables are the single source for presets, defaults, compatibility rules and reason codes; the optional `tools/composition.py` reads them rather than holding its own copy | COMPOSITION K6–K9, tools/composition.py | Added during implementation to avoid a competing definition between prose and helper | Mechanical: table consistency, example re-derivation, mutation controls |
| ADR-13 | The self-test helper writes run-stamped results outside the tested tree, records actual time and manifest hashes, keeps failed records, and fails on a missing or empty pattern file | research/run_rc1_checks.py, tools/documents.py | Implements defects K1–K5 from the evidence base. Results are then copied into research/validation/ and bound by FREEZE.md | Mechanical: 19 controls, 41 records |

## Decisions deliberately not taken

- No new ontology file, role roster or orchestration runtime (MERGE_DECISIONS.md already rejected fixed roles).
- No machine-readable schema version: configuration stays readable `key: value` text.
- No automatic de-escalation of approvals or assurance after success streaks (rejected in 4.2, not reopened).
- No funnel resource policy in the core (M29 requires further evidence).
- No time-based evidence expiry by default; evidence is invalidated on change, plus revalidation before consequential action on a moving subject.
- No generated compact prompt; parity checking is the smaller step.

## Mandatory core versus optional composition

| Part | Mandatory in rc1 | Optional |
|---|---|---|
| INV-01 to INV-12 | Yes, every tier | — |
| Consequence class and assurance floor | Yes | Stricter assurance on request |
| Fast path | Yes, for routine work | — |
| Configuration notice | Only when requested and effective differ materially or work is consequential | — |
| Participation, cadence, format, scaffolding | Defaults apply silently | Presets and per-key overrides |
| COMPOSITION.md, GLOSSARY.md, PRACTICAL_PLAYBOOKS O6 | No (on demand) | Loaded when relevant |
| tools/*.py | No | Maintenance helpers |
