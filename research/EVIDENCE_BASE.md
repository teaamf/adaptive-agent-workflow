# Build 4.4 on what 4.3 already does

**Adaptive Agent Workflow 4.3 already implements, in substance, most of what both supplied Deep Research reports call "missing".** It has a single-agent default, Markdown-only portability, assurance that scales with consequence and can never be lowered retrospectively, evidence that is invalidated when its subject changes, explicit oracle-integrity rules, honest capability fallback, and a frozen single-change experiment protocol. Both reports were written without access to the authoritative files, and three of their concrete claims about 4.3 are contradicted by the files: `MASTER_PROMPT.md` is generated and byte-checked, `AGENT_INTERACTION.md` and `COMPACT_PROMPT.md` are different files that happen to share a size, and the work profiles are domain-method modules, not bundles of cadence or topology. The real gaps are narrower:

- no configurable human participation per stage, and no configurable cadence;
- no acceptance-time check of attribution (causal mechanism) or scope;
- six competing state vocabularies instead of one finding lifecycle;
- no consolidated requested/effective/observed notice;
- no definition of stagnation;
- reviewer independence reported as a yes/no label;
- a hand-maintained compact prompt that has drifted from the core in seven ways;
- a self-test helper whose evidence records break 4.3's own binding rules.

The architecture this evidence base recommends for 4.4-rc1 adds **three new configurable settings** (a participation preset with per-stage overrides, a cadence and format preference, and a scaffolding-intensity policy). It handles everything else by consolidating existing rules: one precedence list, one claim lifecycle, one "claims never exceed evidence or capability" invariant, and one glossary. The always-loaded core should not grow beyond 4.3's roughly 39.5 KB. The comparison should be a paired pilot of about 12–20 tasks with built-in invalid-method traps and valid-alternative controls. A pilot of that size can only detect large effects, so treat it as effect-size estimation. False acceptance on the adversarial tasks is the metric most likely to show a difference. **No comparative superiority claim is authorised.** Several of the OpenAI pipeline figures that motivated the brief rest on secondary coverage, because the primary post returned HTTP 403.

## Evidence tags, scope and the two source reports

This report merges two internal audits of the live 4.3 package with four external literature reviews. Evidence-strength tags follow the underlying notes:

- **[A]**: observed in the 4.3 files, or by running their scripts, on 2026-11-18.
- **[F]**: fetched and read at the primary or official source this session.
- **[S]**: confirmed only through search-engine excerpts or secondary coverage.
- **[M]**: cited from prior knowledge and not re-fetched; check before quoting exact figures.
- **[I]**: inference or design synthesis. Treat it as a hypothesis, not a finding.

Local files appear as code spans (for example `WORKFLOW.md §9`), not links, because the package's link checker scans every Markdown file under the root.

The audits together read every operational module, plus `CONTINUOUS_IMPROVEMENT.md`, `VALIDATION.md`, `RESEARCH_AND_CHANGES.md`, `MERGE_DECISIONS.md`, `evaluation/SCENARIOS.md`, `tools/documents.py` and `research/run_v4_3_checks.py`. Not every one of the 37 archive entries was read: `references/` was cross-checked only as cited, and the preserved copy under `releases/4.3-baseline/` was excluded and its integrity was not hashed.

The two reports are:

- **The earlier report** ("Evolution of the Adaptive Agent Workflow from 4.3 Towards a Composable, Evidence-Driven Architecture"). It is on disk at `C:/Users/__/Documents/Pasted text(20261118-120350).txt`. It states that the archive "could not be extracted", and its recommendations are numbered REC-01 to REC-11 plus a §21 "minimal 4.4". It never mentions RS-WF-1 or Linux.
- **The OpenAI Linux security pipeline report.** It was pasted into chat. It is the one that inspected only a project-local "RS-WF-1" adaptation, and it rated most 4.3 principles "unassessable". No file containing RS-WF-1 was found on disk.

The brief's apparent swap of the two file descriptions is resolved this way, and the RS-WF-1 text remains unlocated.

## 4.3 implements a consequence-scaled evidence workflow with prose-only enforcement

### What the authoritative files actually define

4.3 rests on a single stated invariant, "**intent → bounded work → evidence → assessment → delivery**". It adds a four-way authority separation: what is wanted, what may be done, what exists, and what the evidence establishes (`WORKFLOW.md` preamble and §1) [A].

**The project contract.** It has stable IDs for consequential requirements and rules that "unknown is not pass" and "no requirement may disappear during decomposition". Every potential gate is classed REQUIRED, NOT_APPLICABLE (with a reason) or UNRESOLVED. The contract states that "Unavailable is a capability/evidence condition, never a reason by itself for NOT_APPLICABLE" (`WORKFLOW.md §2`) [A].

**Assurance levels.** There are three: Lightweight, Standard (maker plus fresh-context reviewer) and High consequence (independent verification, domain expertise, adversarial cases, recovery evidence). They are routed by uncertainty, impact, reversibility, coupling, privacy, bias and observability. A ratchet rule applies: "Never lower the profile retrospectively because checks fail or reviewers are unavailable" (`WORKFLOW.md §3`) [A].

**Responsibilities.** Eight responsibilities (not agents) may be merged where the assurance level permits. A coordinator who makes work "cannot provide independent acceptance of it" (`WORKFLOW.md §5`) [A].

**Evidence records.** Each record binds claim, producer and independence, artifact identity, method, environment and timestamp. Records are invalidated by changes to inputs, artifact, specification, oracle, dependencies or environment, and survive a session change after revalidation (`WORKFLOW.md §9`) [A].

**Verification.** `WORKFLOW.md §10` holds a full oracle-integrity block: no deleting, skipping or weakening tests, no hard-coding, no editing the grader. `PRACTICAL_PLAYBOOKS.md O4` requires deliberately wrong results to be rejected [A].

**Retries and pauses.** The defaults are two transient retries and three repair attempts per hypothesis, explicitly labelled "a practical default". There are eleven pause triggers (`WORKFLOW.md §11`) [A].

**Human interaction and host fallback.**

- `AGENT_INTERACTION.md A1–A8` governs human interaction with consequence-triggered checkpoints, a one-screen checkpoint template, "silence is never new authorization", and a stop/redirect guarantee [A].
- `HOST_ADAPTERS.md` maps capabilities rather than brands. Every fallback reduces what can be claimed and never invents evidence, for example "never role-play independence" [A].

**Continuous improvement.** `CONTINUOUS_IMPROVEMENT.md` is already a rigorous comparative-evaluation protocol:

- frozen C2 contracts with 27 fields;
- one bounded change per cycle, with only a bundle-level claim for a bundle;
- separate development, regression and withheld acceptance cases, with access control reported honestly;
- predeclared trial counts, all failures retained, and ADOPT/REJECT/INCONCLUSIVE outcomes [A].

**The package's own validation status.** It reports this honestly. 4.3 was a document-and-tool revision assessed by "author inspection and deterministic document-maintenance checks", and was explicitly "not empirically superior" (`research/v4.3-plan.md`, `VALIDATION.md`) [A].

**What is mechanically enforced.** Only document maintenance:

- master/module byte parity;
- local link resolution;
- 15 regex portability guards;
- the compact prompt's 16,000-byte budget and seven marker phrases.

Every rule about verification, evidence, independence, retries and status is instruction-only. On 2026-11-18 `tools/documents.py check` exited 0 on the live package, and the 15-control suite in `research/run_v4_3_checks.py` passed on a scratch copy [A].

**Size.** The mandatory Tier 1 core is **39,480 bytes**: `WORKFLOW.md` 29,564, `AGENT_INTERACTION.md` 7,791, `PROJECT_TEMPLATE.md` 2,125. Optional modules add about 69 KB, the full bundle is 112,623 bytes, and the compact tier is 7,791 bytes against its 16,000-byte ceiling [A].

### Report claims that the files contradict or confirm

Both reports reasoned about 4.3 without the files. The brief rightly calls their "missing functionality" claims provisional, and the table settles them.

| Report claim about 4.3 | What the 4.3 files show | Resolution |
|---|---|---|
| Earlier REC-03: `AGENT_INTERACTION.md` and `COMPACT_PROMPT.md` are likely duplicates (both 7,791 bytes) | Different SHA-256 hashes (be6f9dd3… vs 0d5167ba…), different titles, 97 vs 122 lines; COMPACT §5 paraphrases A1–A6 [A] | **Contradicted.** Equal size is coincidental |
| Earlier REC-03: MASTER duplication of modules is unmanaged | `tools/documents.py` assembles MASTER from `LAUNCH.md` plus 10 modules and `check` fails on any byte difference [A] | **Contradicted.** REC-03's own falsifier is met |
| Earlier §21: extend `research/run_v4_3_checks.py` to enforce MASTER sync | Parity is already enforced by `tools/documents.py`; the real residual risk is compact-tier semantic drift [A] | **Misdirected** |
| Earlier REC-05: profiles bundle cadence, verification and topology | `PROFILES.md` P1–P7 are composable domain-method modules with no cadence or topology settings. Only the assurance level couples reviewer count, negative-case depth and recovery evidence [A] | **Contradicted for work profiles**; partially true for assurance levels |
| Earlier report: 19 root `.md` files; per-file byte sizes | Confirmed exactly (e.g. `WORKFLOW.md` 29,564; `MASTER_PROMPT.md` 112,623) [A] | **Confirmed** |
| Linux report: 4.3 principles "unassessable / possibly supported / unknown" | Fresh-context review (`WORKFLOW.md §3, §6`), negative controls (`PRACTICAL_PLAYBOOKS.md O4`), stale-evidence invalidation (`§9`), bounded retries (`§11`), owner approval of consequential actions (`AGENT_INTERACTION.md A3`), capability ≠ authorisation (`§1`, `§12`), multi-agent optional (`§5`) are all present [A] | **Resolved: implemented** |
| Linux report: "evidence has a subject revision and an expiry condition" | 4.3 binds artifact identity and invalidates on change, not on elapsed time; oracle identity is not a named evidence field [A] | **Partially implemented**; time-based expiry is deliberately absent |
| Linux report: a generic Observation → Candidate → Validated → Actionable state model is needed | 4.3 has claim states (`§9`) and finding records (`O3`) but no truth state for a finding, and six separate state vocabularies [A] | **Partially implemented** |

## Baseline traceability matrix: 34 recommendations against the 4.3 files

Each row is one material recommendation. Sources are abbreviated as follows:

- **E**: the earlier report (REC-xx and §21).
- **L**: the Linux pipeline report (L-n is its ten prioritised recommendations; L-c is its proposed concepts).
- **B**: the owner's brief (§n).

Classification uses the brief's five values. Where a report's premise is wrong but a residual gap exists, both are shown.

| # | Recommendation (source) | 4.3 file / section | Existing behaviour | Actual gap | Proposed rc1 modification | Supporting evidence | Required verification | Classification |
|---|---|---|---|---|---|---|---|---|
| M01 | Audit authoritative 4.3 before editing; preserve an immutable copy (E REC-10; L-10; B §1) | `CONTINUOUS_IMPROVEMENT.md C2, C5`; `research/v4.3-plan.md` | C2 requires `current_workflow_hash`; C5 preserves old versions | 4.3's own cycle left C2 hashes unfilled; `releases/4.3-baseline/` not hash-verified | Record a SHA-256 manifest of every 4.3 file as the frozen baseline identity; develop rc1 outside the baseline tree | C2 field list [A] | Manifest of baseline equals live 4.3 at fork; `documents.py check` passes on baseline | Partially implemented |
| M02 | Markdown-only; no runtime lock-in; reject mandatory engines, swarms and consensus-as-proof (E REC-01, REC-11; B §9) | `README.md`; `WORKFLOW.md §5, §9`; `RESEARCH_AND_CHANGES.md` rejected approaches | "Using the workflow never requires Python"; "Do not build a custom orchestration service"; majority vote is not an oracle | None | Retain as stated invariant; label any new check as tool-assisted, never required | Anthropic "simplest solution possible" ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)) [F] | Portability guard passes; no new mandatory dependency in rc1 manifest | Already implemented |
| M03 | Single-agent default; multi-agent only for decomposable work (E REC-02; L-9; B §8) | `WORKFLOW.md §3, §5` | "Use the smallest eligible team"; parallelism pays "mainly on breadth-first work"; single write owner | No required justification when a team is used | Add a one-line team rationale to the existing task-packet field | Kim et al. −39% to −70% on sequential tasks ([arXiv](https://arxiv.org/html/2512.08296)) [F]; 15× tokens ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)) [F] | Sequential-task scenario: rc1 stays single-agent and records why | Already implemented (minor refinement) |
| M04 | Remove MASTER/module duplication and the "7,791-byte pair" (E REC-03) | `tools/documents.py`; `MASTER_PROMPT.md` | Generated bundle, byte-checked | Premise false (see contradictions table) | None for MASTER | Hash and `cmp` comparison [A] | Existing `documents.py check` | Inappropriate (premise contradicted) |
| M05 | Single-source compact tier (E REC-03, §21; B §9, M4) | `COMPACT_PROMPT.md`; `tools/documents.py` `COMPACT_MARKERS` | Hand-maintained; guarded by 7 marker strings, "not a semantic equivalence proof" | Seven substantive divergences already present (defects C1–C7) | Give each mandatory invariant a stable ID in the core; compact must carry every ID; extend the check from 7 phrases to the invariant ID list | Drift audit [A] | Mutation control: delete one invariant ID from compact and confirm the check fails; restore passes | Partially implemented |
| M06 | Remove prose implying prompt text confers isolation (E REC-03, REC-08) | `WORKFLOW.md §6`; `WORKFLOW_CONFIGURATION.md F3` | "Shared filesystem access and a fresh label do not establish isolation"; "Metadata ... not a sandbox" | None | Fold into the single claims-within-evidence invariant (ADR-10) | [A] | Grep regression: no rc1 text asserts isolation from instructions alone | Already implemented |
| M07 | 13-primitive kernel ontology / component taxonomy (E REC-04; L-c; B §2) | Distributed across `WORKFLOW.md §1–§13`, `PRACTICAL_PLAYBOOKS.md O1, O3` | All 13 REC-04 primitives exist under other names (contract, task, artifact, responsibility, host capability, permissions, policies, capability record, durable state, event, evidence, review, gate) | No single glossary; two role tables; unmapped nouns (supervisor, design owner, decision owner) | One glossary in the brief's eight categories that maps existing nouns; no new primitives (ADR-01) | Brief §2 "no new fundamental component merely because a report renames" | Every glossary term resolves to exactly one defining section; no orphan role noun | Inappropriate as new ontology; glossary Missing |
| M08 | Role contracts Scout / Analyst / Validator / Impact assessor / Repairer / Verifier / Human reviewer (L-c) | `WORKFLOW.md §5`; `PRACTICAL_PLAYBOOKS.md O1` | Eight responsibilities plus nine finer dispatch roles | The proposed roles rename existing responsibilities | Map them in the glossary as presets over responsibilities | Pipeline roles via secondary coverage ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F] | Glossary review | Inappropriate (rename); Already implemented |
| M09 | Presets over orthogonal axes; six-axis policy schema (E REC-05, §21; B §3) | `WORKFLOW.md §0, §3`; `PROFILES.md`; `HOST_ADAPTERS.md` tiers | Assurance level, domain profiles, loading tier, fast/full path | Human participation, cadence and presentation are not configurable; planning depth is binary | Add three settings only (participation, cadence/format, scaffolding); keep others as existing profiles, tiers or derived rules (ADR-02) | Parasuraman et al. per-stage independence ([DOI](https://doi.org/10.1109/3468.844354)) [F: abstract] | Independence demo: change each new setting alone and confirm no other effective value changes | Partially implemented |
| M10 | Ordered precedence; mandatory invariants non-overridable; model capability cannot weaken assurance (E REC-05; B §3) | `WORKFLOW.md §2, §3`; `HOST_ADAPTERS.md`; `MERGE_DECISIONS.md`; `SKILL.md` | Ratchet; "tier adds detail, not authority"; core authoritative over playbooks; worker cannot waive requirement | Precedence scattered over at least 6 files; no explicit statement that capability cannot lower assurance | One ordered precedence table consolidating existing rules (ADR-03) | Claude Code managed-settings and stricter-wins pattern ([docs](https://code.claude.com/docs/en/settings)) [F] | Conflict scenarios: preference requesting lower assurance on high-consequence task is clamped and reported | Partially implemented |
| M11 | Compatibility clamps; `schema_version`; v4.3 aliases (E REC-05; B §3) | None | None | No requires/excludes validation | Small Markdown requires/excludes table; aliases for renamed "profile" terms; no schema_version unless a machine-readable header is adopted | Feature-model requires/excludes ([Benavides survey](https://core.ac.uk/download/51389491.pdf)) [S] | Void-preset and dead-option review over all presets | Missing |
| M12 | Requested vs effective vs observed configuration (E REC-05, §21; L-c; B §4) | `WORKFLOW.md §3, §6`; `PRACTICAL_PLAYBOOKS.md O3`; `WORKFLOW.md §12` | Profile recorded before judging; host capability record; isolation report; READY_FOR_REQUIRED_REVIEW | No consolidated notice; no per-setting divergence reasons | Short notice only when requested ≠ effective or the task is consequential; observed divergences with reason codes in the delivery report (ADR-04) | Kubernetes spec/status with `reason` and `observedGeneration` ([API conventions](https://raw.githubusercontent.com/kubernetes/community/master/contributors/devel/sig-architecture/api-conventions.md)) [F] | Reviewer-unavailable scenario yields notice and blocked acceptance; trivial task yields no notice | Partially implemented |
| M13 | Explicit evidence states / reusable finding lifecycle (L-1; B §5) | `WORKFLOW.md §9`; `PRACTICAL_PLAYBOOKS.md O1, O3`; `AGENT_INTERACTION.md A1`; `UI_DESIGN_PROTOCOL.md U6`; `WORKFLOW.md §12` | Six vocabularies: claim states, fact status, gate result, review verdict, report buckets, delivery statuses | No truth state for findings; reader must reconcile six lists | One claim lifecycle on a truth axis plus orthogonal consequence, decision, remediation and acceptance axes (ADR-05) | Brief §5; MAST verification failures (FM-3.x ≈ 23.5%) ([arXiv](https://arxiv.org/html/2503.13657)) [F] | Mapping table covers every existing term; G19/G21/G25 scenarios still yield the same verdicts | Partially implemented |
| M14 | Finding schema; separate truth, priority, remediation and acceptance; deduplicate; non-reproduction ≠ false (L-c; B §5) | `PRACTICAL_PLAYBOOKS.md O3`; `evaluation/SCENARIOS.md G27` | Finding = ID, requirement, severity, reproduction, owner, resolution, recheck; evidence reuse only if content addresses the claim | No finding deduplication; no "inconclusive within budget" state; no rule on who changes severity | Extend O3 Finding with a truth state, subject identity, dedup key (root cause) and decision owner | 1,169 exploits → 948 distinct by root cause ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F] | Scenario: unreproduced candidate stays inconclusive, not rejected | Partially implemented |
| M15 | Bind evidence to revision and environment; invalidate on mutation; revalidate before acting (E REC-08; L-5; B §5) | `WORKFLOW.md §9`; `PRACTICAL_PLAYBOOKS.md O3, O5` | Artifact identity, environment, timestamp; change-triggered invalidation | Oracle identity not a required field; no rule to revalidate against the current subject immediately before an external or irreversible action | Add oracle identity to the evidence record; revalidate-before-consequential-action rule | SLSA provenance subject and build definition ([SLSA](https://slsa.dev/spec/v1.0/provenance)) [M]; 61 patched upstream within 10 days ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F] | Stale-evidence trap: evidence bound to an earlier oracle hash is rejected | Partially implemented |
| M16 | Separate verification dimensions (L-2; B §6) | `WORKFLOW.md §0, §8, §10, §11`; `PROFILES.md`; `CONTINUOUS_IMPROVEMENT.md C4` | Outcome, oracle integrity and authorisation present; process, regression, nonfunctional partial; attribution weak | Verification organised by domain, not dimension; process and attribution have no home | Verification plan names the applicable dimensions per claim and chooses methods by claim type and consequence (ADR-06) | Each dimension has a documented failure where outcome passed (see ADR-06) | Dimension coverage check on every adversarial task family | Partially implemented |
| M17 | Independent attribution check (L-c, the 20-of-200 case; B §6) | `WORKFLOW.md §11` "a check that passes without explaining why"; `PRACTICAL_PLAYBOOKS.md O2` bug procedure | Pause trigger and a discriminating experiment for bugs | No acceptance requirement that the claimed mechanism be verified | Consequential fixes state a causal claim backed by fail-before/pass-after and, where consequence warrants, revert or mechanism probe | 20 of 200 exploits used a different zero-day ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F] | Wrong-mechanism trap rejected; alternative-location valid fix accepted | Missing |
| M18 | Scope and authorisation audit against observed actions (L-c scope layer; B §6) | `WORKFLOW.md §1, §11, §12`; `AGENT_INTERACTION.md A3` | Out-of-scope edits are a pause trigger; scope appears in delivery report | No acceptance-time diff-versus-authorised-scope check | Acceptance compares touched files, commands and external actions with the authorised scope | AgentDojo state-based scoring ([arXiv](https://arxiv.org/abs/2406.13352v3)) [S] | Out-of-scope-edit trap rejected; required-but-unexpected in-scope file accepted | Partially implemented |
| M19 | Regression dimension (B §6) | `WORKFLOW.md §8`; `PRACTICAL_PLAYBOOKS.md O2`; `MERGE_DECISIONS.md` | "Rerun affected checks"; universal regression gate explicitly rejected | "Affected" is undefined | Keep proportionality; require the affected-set rationale to be recorded; broaden when dependency impact is uncertain (already §9) | 7.8% of "correct" SWE-bench patches fail the full suite ([arXiv](https://arxiv.org/abs/2503.15223)) [S] | Scenario where the affected set is too narrow | Partially implemented |
| M20 | Functional plus nonfunctional repair acceptance (L-7; B §6) | `PROFILES.md P1`; `UI_DESIGN_PROTOCOL.md U6`; `WORKFLOW.md §10` | Security, performance and accessibility are profile-dependent; correctness, privacy and mandatory accessibility are non-tradeable | No generic prompt to name applicable nonfunctional criteria | Contract lists applicable nonfunctional requirements; measurement uses an oracle the maker cannot modify | METR faked-clock speedups ([METR](https://metr.org/blog/2025-06-05-recent-reward-hacking)) [F]; OpenAI "excess code" patches unverified | Performance trap with patched timer rejected | Partially implemented |
| M21 | Process verification without prescriptive implementation control; valid alternatives permissible (B §6) | `WORKFLOW.md §0, §10`; `MERGE_DECISIONS.md` | Outcome-focused checks; universal method gates rejected | No explicit clause that a different valid implementation passes | State criteria as properties of results and evidence; deviation triggers explanation, not rejection; prohibited mechanism is never acceptable | PatchDiff compares behaviour, not code shape ([arXiv](https://arxiv.org/abs/2503.15223)) [S] | Valid-alternative controls in every task family | Partially implemented |
| M22 | Genuine reviewer independence, correlated agreement, honest isolation reporting (L-c; B §6) | `WORKFLOW.md §3, §5, §6, §11`; `HOST_ADAPTERS.md`; `UI_REVIEW_PLAYBOOK.md V3` | Narrative withheld, findings frozen, enforced vs cooperative reported; votes don't guarantee diversity | Independence is a binary label; no scenario covers correlated reviewers | Multi-axis isolation disclosure; same-family agreement counts once (ADR-06) | Correlated errors across capable models ([Goel et al.](https://arxiv.org/abs/2502.04313)) [S]; self-preference ([arXiv](https://arxiv.org/abs/2404.13076)) [M] | Correlated-reviewer trap | Partially implemented |
| M23 | Separate capability from authorisation and alignment evidence (L-8) | `WORKFLOW.md §1, §12`; `HOST_ADAPTERS.md` | "Readiness, authorization and external approval are different facts" | None for workflow use; the GPT-6 Cyber system-card figures the report cites are unverified | Retain; state in the glossary that capability never grants permission | [A] | Existing G18, G28, G49 scenarios | Already implemented |
| M24 | Human participation per stage with presets (E REC-07; L-4; B §7) | `AGENT_INTERACTION.md A1–A8` | One implicit posture: agent executes, human authorises consequential actions | No per-stage participation, no tutoring or co-creation posture | Four-stage participation setting on a five-level scale with five presets and fixed invariants (ADR-07) | Parasuraman et al. [F: abstract]; Onnasch et al. ([DOI](https://doi.org/10.1177/0018720813501549)) [S]; Feng et al. ([arXiv](https://arxiv.org/abs/2506.12469)) [F] | Tutoring scenario withholds full answers; preset change leaves assurance unchanged | Missing |
| M25 | Communication cadence and presentation as separate axes (E REC-07, §21; B §3, §7) | `AGENT_INTERACTION.md A1` | "Meaningful milestones"; "match the report to its reader" | Not configurable | Cadence and format preferences, independent of who performs the work; only "decision needed" and "blocked" interrupt | Interruption costs ([Mark et al.](https://interruptions.net/literature/Mark-CHI08.pdf)) [S]; boundary timing ([Bailey & Konstan](https://doi.org/10.1016/j.chb.2005.12.009)) [M] | Same task under two cadence values: identical effective assurance and gates | Missing |
| M26 | Preserve human authorship and requested decision authority (B §7) | `AGENT_INTERACTION.md A2, A7`; `WORKFLOW.md §1, §3` | Answer governs the stated decision only; owner chooses goal conflicts; professional approval only from an eligible person | No contribution record; no explicit authorship invariant | Fixed invariants: human is accountable author of record, final-acceptance gate for released artifacts, AI contributions logged | ICMJE AI-authorship rule ([ICMJE](https://icmje.acponline.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html)) [S]; ownership tracks control ([Draxler et al.](https://arxiv.org/abs/2303.03283v1)) [F: abstract] | Co-creation scenario records human decisions | Partially implemented |
| M27 | Adaptive, empirically justified scaffolding (L-3; B §8) | `HOST_ADAPTERS.md` tiers and model-change rule; `CONTINUOUS_IMPROVEMENT.md C2` | Smaller context leads to the compact tier; model change triggers a rerun of a few scenarios; "a stronger model ... is not automatically a better workflow" | Scaffold elements are not toggleable; no rule that stronger workers may receive lighter procedure | Scaffolding intensity as a policy chosen from task structure, demonstrated capability, progress, uncertainty, consequence and resources; capability may lighten scaffolding, never assurance (ADR-08) | Technique library +12.7 points for GPT-5.5 Cyber, removed for GPT-5.6 Cyber ([AI News](https://www.artificialintelligence-news.com/news/openai-cyber-model-found-948-linux-kernel-exploits/)) [F] | Ablation arm A4 (fixed standard scaffold) | Partially implemented |
| M28 | Failure classes; bounded retry, escalation, de-escalation, stop; stagnation detector; circuit breaker (E REC-09; L-6, L-c; B §8) | `WORKFLOW.md §0, §11`; `AGENT_INTERACTION.md A6`; `CONTINUOUS_IMPROVEMENT.md C1` | 2/3 retry defaults per hypothesis; 11 pause triggers; failure report with options | No cap across changing hypotheses; no stagnation definition; escalation reason not logged; failure classes exist only for improvement diagnosis | Seven failure classes mapped to actions; stagnation = N attempts without new evidence or state transition (N a configurable hypothesis); logged escalation (ADR-09) | Unaided self-correction can degrade answers ([Huang et al.](https://arxiv.org/abs/2310.01798)) [F]; MAST step repetition 15.7% ([arXiv](https://arxiv.org/html/2503.13657)) [F] | Endless-retry trap halts; progressing long task does not | Partially implemented |
| M29 | Funnel resource policy: cheap broad discovery, filtering, validation, deep work only for survivors (L-c) | `WORKFLOW.md §3, §8`; `PROFILES.md P4` | Consequence-scaled assurance; "feedback is the speed limit"; research stopping tied to the question | No staging guidance | Optional playbook pattern, not core | One campaign; stage costs unverified | Not in pilot | Requires further evidence |
| M30 | Safeguard enforcement tiers; action-boundary interception (E REC-08; B §9) | `WORKFLOW_CONFIGURATION.md F2`; `PROJECT_TEMPLATE.md`; `WORKFLOW.md §1` | `blocking_or_advisory` field; lethal-trifecta gate as instruction | No per-safeguard enforcement label in the core | Three labels (mechanical-blocking, mechanical-advisory, instruction-only) reusing F2, not five tiers; interception stays host-dependent | Auto-mode classifier false-negative rate 17% ([Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode)) [F] | Every rc1 invariant carries an enforcement label | Partially implemented; 5-tier scheme Inappropriate |
| M31 | No mandatory autonomous self-modification loop (B §8) | `CONTINUOUS_IMPROVEMENT.md` preamble, C5 | "No background activity, no recursive agents"; one candidate per cycle | None | Retain | [A] | Review | Already implemented |
| M32 | Environment-state evaluation, withheld tasks, adversarial traps, no self-report as proof (E REC-06, §21; L-c; B §11) | `CONTINUOUS_IMPROVEMENT.md C2–C4`; `evaluation/SCENARIOS.md` | Full protocol; 50 public development cases, author-inspected only | Never executed; no fixtures, no oracles, no withheld set; correlated reviewers absent; several trap families partial | Frozen pilot contract (see experiment section) | METR self-report gap ([arXiv](https://arxiv.org/abs/2507.09089)) [F]; ImpossibleBench ([arXiv](https://arxiv.org/abs/2510.20270)) [S] | Contract frozen and hashed before any rc1 trial | Partially implemented |
| M33 | Smaller mandatory core; turn scaffolding off (L conclusion; B §13) | `WORKFLOW.md §0`; `CONTINUOUS_IMPROVEMENT.md C4` | "More process is not more quality"; workflow length is a cost | No size ceiling for Tier 1; `WORKFLOW.md` mixes always-on invariants with on-demand detail | Tier 1 byte ceiling ≤ 39,480; move multi-agent failure clusters, bias table and metric detail to on-demand modules (ADR-10) | Simple baselines can match complex agents ([Kapoor et al.](https://arxiv.org/abs/2407.01502)) [M] | Byte check on Tier 1 in `documents.py` | Partially implemented |
| M34 | Retrieve primary texts (BPMN/CMMN/DMN, Workflow Patterns, NASA NTRS, W3C PROV, NIST AI RMF, hysteresis) before 4.4 edits (E REC-10) | `RESEARCH_AND_CHANGES.md` cycles 1–2 (PROV, NASA tailoring already used) | PROV and NASA tailoring already shaped §2 and §9 | No rc1 decision depends on BPMN/CMMN/DMN or hysteresis | Defer unless an ADR needs them | None | n/a | Requires further evidence |

The matrix shows that **roughly a third of the rows are already implemented or rest on a false premise**. Most of the remainder are consolidations of existing partial mechanisms rather than new components. Only four areas are genuinely missing: per-stage human participation, cadence/format, the attribution requirement, and the glossary/compatibility table.

## Seventeen audit defects, none unsafe, several eroding evidence integrity

No defect found would make an agent act unsafely. The compact divergences mostly err toward strictness, but three of them drop protections the core requires. The check-script defects matter more than their size suggests: 4.3's own maintenance evidence fails the binding rules in `WORKFLOW.md §9`, which undercuts the package's credibility as an evidence-integrity workflow.

| ID | Defect | Location | Consequence | rc1 fix |
|---|---|---|---|---|
| C1 | Trifecta gate narrowed to "get human approval before any consequential action"; the core allows "a human or other reliable validation gate" | `COMPACT_PROMPT.md §1` vs `WORKFLOW.md §1` | Stricter; contradicts host validators | Invariant-ID parity |
| C2 | Ratchet omits "or reviewers are unavailable" | `COMPACT_PROMPT.md §2` vs `WORKFLOW.md §3` | **Drops a protection**: unavailable reviewer could justify lowering | Parity |
| C3 | High consequence drops "domain expertise" and turns "recovery evidence" into "recovery plan" | `COMPACT_PROMPT.md §2` vs `WORKFLOW.md §3` | **Drops a protection**: plan ≠ evidence | Parity |
| C4 | Pause triggers omit "resource use well above the budget" | `COMPACT_PROMPT.md §3` vs `WORKFLOW.md §11` | **Drops a protection** relevant to runaway loops | Parity |
| C5 | Status list omits CHECKPOINTED and CERTIFIED_UNDER_NAMED_PROFILE while §6 says "checkpoint honestly" | `COMPACT_PROMPT.md §6–§7` vs `WORKFLOW.md §12` | Vocabulary gap | Unified lifecycle |
| C6 | Missing review is "blocked" in compact, READY_FOR_REQUIRED_REVIEW in core | `COMPACT_PROMPT.md §6` vs `WORKFLOW.md §12` | Two labels for one state | Unified lifecycle |
| C7 | Compact lacks provisional-work bound, gate tri-state, single-write-owner rule, 4 of 9 bias checks; 7 vs 8 fast-path steps | `COMPACT_PROMPT.md` | Compression loss | Decide per invariant ID which belong in Tier 0 |
| P1 | Header says "Version 4.1" and names the package "AdaptiveAgentWorkflow" | `MERGE_DECISIONS.md` | Stale metadata | Version-string check |
| P2 | Master contents list omits `UI_REVIEW_PLAYBOOK.md` and `WORKFLOW_CONFIGURATION.md`, which are embedded | `GUIDE.md` Launch | Misleading documentation | Generate list from `MODULES` |
| P3 | Compact ceiling stated as "16 KB" but enforced as 16,000 bytes | `HOST_ADAPTERS.md` vs `tools/documents.py` | Minor ambiguity | State bytes |
| P4 | "Profile" means four things: assurance, work/domain, accessibility, named certification | `WORKFLOW.md §3, §12`; `PROFILES.md`; `UI_DESIGN_PROTOCOL.md U6` | Routing confusion | ADR-10 renaming with aliases |
| P5 | Fast-path criteria (§0) and Lightweight fit (§3) restate the same condition; checkpoint need (A3) is a third overlapping classifier | `WORKFLOW.md §0, §3`; `AGENT_INTERACTION.md A3` | Duplicated rules | One consequence classification |
| K1 | Helper writes `research/v4.3-check-results.json` into the real package root, not the tested copy | `research/run_v4_3_checks.py` | Rerunning overwrites recorded evidence | Write to the temp root or a run-stamped path |
| K2 | Hard-coded `'date': '2026-11-04'` and fixed `setup_failure` narrative; size metrics read from root, not the tested copy; no artifact hash | same | Every rerun produces a record that misdescribes itself, contrary to `WORKFLOW.md §9` | Record actual time, tested-tree manifest hash and tool versions |
| K3 | Raises on the first failing control before writing JSON | same | Failing runs leave no record, contrary to C3 "retain every trial" | Persist all records, then exit non-zero |
| K4 | Missing portability-patterns file silently runs zero guards | `tools/documents.py` | Silent pass, the exact pattern G38 warns against | Fail on missing or empty pattern file |
| K5 | Link check scans `releases/`, `reports/` and `research_notes/`; skips URLs, fragments and any path with a `research` component; compact markers prove phrase presence only; no version-string check | `tools/documents.py` | A bad note can fail the whole package; unguarded rules (e.g. retry limits) can drift | Scope the scan explicitly; add invariant-ID and version checks |

## Ten decisions that shrink the mandatory core and widen optional composition

Each decision below is a candidate for the rc1 change set, not an accepted change. Each carries a testable hypothesis for the frozen experiment, or for mechanical checks where the change is logically necessary. CONTINUOUS_IMPROVEMENT C4 calls the latter VERIFIED_DOCUMENT_OR_TOOL_FIX.

### ADR-01: Eight component categories map existing nouns, adding none

**Decision.** Publish one glossary that places every existing 4.3 noun in exactly one of the brief's eight categories. Every term links by section name to its single authoritative definition.

| Category | 4.3 elements (existing) |
|---|---|
| Fundamental entities and responsibilities | Contract and requirement IDs; artifact (identity); bounded task; claim; evidence item; finding (a claim of defect); decision. Responsibilities: coordinate, investigate/plan, make, verify, review, integrate, final-assess (Specialist is a qualifier). Human roles: requester/owner, decision owner, eligible approver |
| Mandatory invariants (non-configurable policy) | Authority separation; untrusted content is data; lethal-trifecta validation gate; secrets handling; oracle integrity; claims ≤ evidence ≤ capability; never lower assurance retrospectively; honest status; human authorship and stop/redirect |
| Configurable policies | Assurance level; domain profiles P1–P7; participation; cadence/format; scaffolding intensity; resource and stopping budget |
| Execution mechanisms | Fast path; task packet; provisional-work bound; retry defaults and pause triggers; checkpoints; dispatch modes; fresh-context review protocol; O4 challenges |
| Runtime state | Minimum durable state (`§9`); progress note; long-run ledger (`§13`); effective configuration |
| Observations and evidence | Evidence, review, event and host-capability records (`O3`); UI capture record (`V2`) |
| Derived views | Delivery status; A1 report buckets; requested/effective notice; traceability matrix |
| Presets and adapters | Participation presets; O2 scenario procedures; loading tiers, MASTER and COMPACT as representations; host capability map; skill metadata |

**Rationale.** All 13 REC-04 primitives and all seven of the Linux report's role contracts already exist under other names (matrix rows M07, M08). Renaming them would violate the brief's rule against new components "merely because a report renames an existing responsibility". It would also add size without changing behaviour.

**Alternatives rejected.**
- A new 13-primitive kernel file.
- A Scout/Analyst/Validator role roster, which `MERGE_DECISIONS.md` already rejected in the form of fixed role identities.

**Evidence.** Internal audit [A]. Fixed-role rosters were removed in 4.1 (`MERGE_DECISIONS.md`) [A].

**Testable hypothesis.** H1: every rc1 normative term resolves to exactly one defining section, mechanically checkable by a glossary-link check. Role-noun count falls from the current two tables plus at least four stray nouns to one table.

### ADR-02: Three new settings justify independence; six dimensions stay as they are

**Decision.** Of the brief's nine dimensions, only three become new independent settings. Three keep their existing 4.3 representation, and three remain rule-derived values that may be requested but are clamped.

| Brief dimension | rc1 treatment | Values (default) | Why |
|---|---|---|---|
| Human involvement | **New setting** | Participation preset (default: supervised execution) with per-stage overrides; learning objective off/on | Strong evidence for independent per-stage allocation; 4.3 has one posture |
| Communication cadence and presentation | **New preference** (two keys) | Cadence: on-demand / milestones / each-decision (milestones). Format: terse / structured / trace (structured, per A1) | Interruption evidence; must not depend on who performs the work |
| Scaffolding intensity | **New policy** with automatic default | auto / minimal / standard / guided (auto) | Scaffold value is model- and task-dependent |
| Assurance and verification requirements | Existing assurance level | Lightweight / Standard / High consequence; floor set by consequence | Already a working switch with a ratchet |
| Context loading and persistence | Existing loading tier plus durable state | Tier 0 / 1 / 2 by capacity | Already works; "never load two tiers" |
| Domain method | Existing domain profiles | P1–P7, composable | Already composable |
| Resource and stopping policy | Existing packet field, formalised | Budget (tokens, time, tool calls, cost); retries 2/3; stagnation N | Already required; numbers stay labelled hypotheses |
| Planning depth | Derived, requestable | direct / outline / full, derived from consequence class, interdependent-step count and reversibility | No study isolates planning benefit for coding agents |
| Decomposition, worker assignment, topology | Rule-governed, requestable, clamped | single / parallel read-only / parallel writers, with a rationale | Smallest-eligible-team evidence; host-dependent |

**Rationale.** The participation dimension has the strongest support. Parasuraman, Sheridan and Wickens define automation **independently for four function classes**: acquisition, analysis, decision and implementation ([DOI](https://doi.org/10.1109/3468.844354)) [F: abstract].

Cadence has to be its own key because several Sheridan–Verplank levels differ only in reporting behaviour [M]. Interrupted workers also compensate with speed at the cost of higher stress and effort ([Mark et al.](https://interruptions.net/literature/Mark-CHI08.pdf)) [S].

Planning depth does not earn an independent setting. In the BATS ablation, removing verification cost more accuracy than removing planning: 15.4% versus 17.0%, against 18.7% for the full system ([arXiv](https://arxiv.org/html/2511.17006v1)) [F]. And no source isolates plan versus no plan for coding agents.

Topology should not follow user preference unchecked. Multi-agent variants degraded sequential planning by **39.1% to 70.0%** ([arXiv](https://arxiv.org/html/2512.08296)) [F].

**Alternatives rejected.**
- The earlier report's six-axis schema as six new keys. It promotes planning depth and topology to preferences against the evidence.
- A single global autonomy level. The human-factors literature supports per-stage settings, not one dial [F].
- A machine-readable schema with `schema_version`. It is not needed while configuration remains readable Markdown instructions (brief §9).

**Evidence.** As cited. Agent Skills and AGENTS.md conventions show that a short frontmatter plus prose degrades gracefully to plain instructions ([agents.md](https://agents.md/); [skills docs](https://code.claude.com/docs/en/skills)) [F].

**Testable hypothesis.** H2: changing any one of the three new settings alone changes no other effective value in the resolved configuration (a mechanical independence demonstration). H3: rc1 on routine tasks uses no more tokens than 4.3 at equal assurance. This is checked in the pilot.

### ADR-03: One precedence list, where mandatory invariants win and stricter values always may

**Decision.** Replace the at least six scattered precedence statements with one ordered table, highest first.

| Rank | Layer | May loosen lower layers? |
|---|---|---|
| 1 | Mandatory invariants (ADR-01 list) | Never overridden; any layer may make them stricter |
| 2 | Actual permissions and host capability | Constrains the effective value; cannot be granted by any lower layer |
| 3 | Adopted project contract and mandatory gates | Only by its owner, with recorded reason, source and decision owner (`§2`) |
| 4 | Assurance floor from consequence classification | Ratchets up only; never lowered retrospectively; never lowered because a stronger model is used |
| 5 | Explicit task-level user instruction | May set any configurable policy within ranks 1–4 |
| 6 | Standing project or user preferences | Same |
| 7 | Preset values | Same |
| 8 | Documented defaults | Written out explicitly in the effective configuration |

The merge semantics are:

- A scalar value replaces the one below it.
- Gate sets are unions, so a lower layer can add gates.
- An explicit `off` may remove an *optional* preset gate but never a consequence gate.
- An invalid entry is skipped with a warning, except in ranks 1–4, where the stricter value applies.

**Rationale.** 4.3 already encodes most of this order across several files: the ratchet, "a project may require stronger assurance", the core outranking playbooks, a tier adding detail but not authority, and "a delegated worker cannot waive an adopted requirement" (`WORKFLOW.md §2, §3`; `HOST_ADAPTERS.md`; `SKILL.md`) [A]. The table consolidates rather than invents.

The brief's rule that "model capability alone cannot justify weaker assurance" becomes the explicit clause in rank 4. It is consistent with CI C2's statement that a stronger model "is not automatically a better workflow" [A].

**Alternatives rejected.**
- The earlier report's seven-tier order as given. It places host capability above the project contract, which matches rank 2 here. But it is silent on stricter-wins and merge semantics, which mature configuration systems needed to state explicitly.
- "User chat prompt overrides everything" (the AGENTS.md convention). It would let a preference defeat an invariant.

**Evidence.** Claude Code documents managed settings that lower scopes cannot override, list keys that merge rather than replace, and "a restrictive value from a scope that otherwise couldn't override" being honoured ([docs](https://code.claude.com/docs/en/settings)) [F]. Helm uses explicit `null` removal ([Helm](https://helm.sh/docs/chart_template_guide/values_files/)) [F]. AGENTS.md uses nearest-file-wins ([agents.md](https://agents.md/)) [F].

**Testable hypothesis.** H4: across the compatibility-scenario set, every preference that conflicts with ranks 1–4 resolves to the stricter value and is reported, with zero silent loosening. This is a document-and-scenario check.

### ADR-04: Requested, effective and observed configuration, recorded only when they differ

**Decision.** The record has three parts:

- **Requested**: the sparse overrides the user or project supplied, verbatim.
- **Effective**: the resolved configuration after ranks 1–8, with defaults written out and the source layer noted per key.
- **Observed**: what actually happened.

Each material divergence carries a key, the effective value, the observed value, a reason code (for example `HostLacksCapability`, `ReviewerUnavailable`, `PolicyClamp`, `BudgetExhausted`, `UserInstruction`) and one human sentence. A short notice of three to five lines appears at task start only when requested differs from effective or the task is consequential. Trivial fast-path work gets none (brief §4: "proportional reporting").

A required-but-unavailable verification appears as "required: blocked" in the effective record. It drives READY_FOR_REQUIRED_REVIEW or DELIVERED_WITH_GAPS, and it never becomes NOT_APPLICABLE or optional.

**Rationale.** The parts already exist in 4.3:

- the selected profile is recorded before judging (`§3`);
- there is a host capability record (`O3`);
- the isolation report says enforced or cooperative (`§6`);
- READY_FOR_REQUIRED_REVIEW exists as a status (`§12`).

What is missing is the consolidated view and the observed-divergence reasons [A].

**Alternatives rejected.**
- A mandatory configuration header on every task, which is ceremony on trivial work.
- Recording only requested and effective. This hides cases where the agent silently skipped an effective setting, which is the "misrepresented capability fallback" trap.

**Evidence.** In Kubernetes, `spec` is desired state and `status` is "the most recent observations of actual state". Conditions carry a CamelCase `reason`, a human `message` and an `observedGeneration` ([API conventions](https://raw.githubusercontent.com/kubernetes/community/master/contributors/devel/sig-architecture/api-conventions.md)) [F]. Terraform calls state that no longer matches real infrastructure "drift" ([HashiCorp](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift)) [F]. Claude Code concedes that `/status` "doesn't show which file supplied each key", the observability gap per-key provenance closes ([docs](https://code.claude.com/docs/en/settings)) [F].

**Testable hypothesis.** H5: on the misrepresented-fallback trap family, rc1's false-acceptance rate is no higher than 4.3's. Exploratory: lower. Notice length on trivial tasks is zero lines.

### ADR-05: One claim lifecycle on a truth axis, with four orthogonal axes

**Decision.** Reuse `WORKFLOW.md §9` claim states as the single **truth axis** for every claim, including findings, gate results and review verdicts. Add exactly one state, *inconclusive within budget*, so that non-reproduction is never recorded as false. Track four further axes separately:

- **consequence/priority**: severity by outcome impact, `§12`;
- **decision**: act, defer or reject, with a named owner;
- **remediation**: none, authorised, candidate, verified;
- **applicability**: REQUIRED, NOT_APPLICABLE or UNRESOLVED, as today.

Acceptance (delivery status) becomes a derived view over these axes. Every claim and finding binds subject identity, oracle identity and environment, plus a dedup key (root cause for findings).

| Existing 4.3 term | Location | rc1 axis and value |
|---|---|---|
| proposed / evidence pending / supported within scope / contradicted / stale / blocked | `WORKFLOW.md §9` | Truth axis (adopted unchanged) plus *inconclusive within budget* |
| Fact status: hypothesis / observed / supported / unresolved | `PRACTICAL_PLAYBOOKS.md O1` | proposed / evidence item / supported within scope / inconclusive |
| Gate result: not assessed / pass / fail / blocked | `O3` | Truth of the gate's claim: evidence pending / supported / contradicted / blocked |
| Review verdict: unset / pass / fail / blocked | `O3` | Same mapping, attached to a review record |
| Gate applicability tri-state | `WORKFLOW.md §2` | Applicability axis (unchanged) |
| Finding severity / resolution / recheck evidence | `O3` | Consequence axis / remediation axis / evidence link |
| Done and checked / done not checked / not done / blocked | `AGENT_INTERACTION.md A1` | Derived report view over remediation × truth |
| IN_PROGRESS … CERTIFIED_UNDER_NAMED_PROFILE | `WORKFLOW.md §12` | Acceptance view (unchanged statuses) |
| STATIC_CHECK / RUNTIME_TOOL / MODEL_CRITIQUE / HUMAN_EXPERT / OBSERVED_HUMAN | `UI_DESIGN_PROTOCOL.md U6` | `evidence.type` field |

The brief's finding path runs along these axes:

1. candidate observation (truth: proposed);
2. validated (truth: supported);
3. assessed (consequence set);
4. decided (decision axis);
5. authorised remediation;
6. verification (the remediation's own claim, which has its own truth state);
7. acceptance (derived view).

A straightforward edit may enter at "requirement adopted" and skip steps 1–4.

**Rationale.** Truth, priority, remediation and acceptance are already conceptually distinct in 4.3. They are spread over `§9`, `§12` and `O3`, and a finding has no truth state of its own [A]. Compact divergences C5 and C6 show the cost of parallel vocabularies.

**Alternatives rejected.**
- The Linux report's linear Observation → Candidate → Validated → Actionable → Accepted chain. A single chain conflates truth with decision and remediation: a validated finding can be rightly deferred.
- Time-based evidence expiry by default. 4.3 deliberately invalidates on change. Elapsed time matters only when the subject is external and moving, which is handled by ADR-06's revalidate-before-acting rule.

**Evidence.** Brief §5. The OpenAI campaign deduplicated 1,169 working exploits into 948 distinct root causes ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F]. In-toto's chaining of step products to materials is the precedent for subject binding ([in-toto](https://in-toto.io/)) [M].

**Testable hypothesis.** H6: re-inspecting scenarios G11, G19, G21, G25 and G27 under rc1 yields the same verdicts as 4.3 using one vocabulary (a regression check). H7: compact-tier status vocabulary errors fall to zero in the compact-tier subset of the pilot.

### ADR-06: Seven verification dimensions, methods chosen by claim and consequence

**Decision.** Every consequential claim's verification plan names which of the seven dimensions apply and selects methods by claim type and consequence. Criteria are stated as **properties of results and evidence, never as required implementation steps**. Three rules govern alternatives:

- A different but authorised implementation that meets the requirements passes.
- Deviation from an expected approach triggers an explanation and attribution evidence, not rejection.
- An outcome achieved through a prohibited or incorrect mechanism cannot be accepted.

| Dimension | 4.3 status [A] | Documented failure where the outcome looked fine | rc1 method (scaled by consequence) |
|---|---|---|---|
| Outcome | Present | About 31% of SWE-bench passes wrong or incomplete ([SWE-Bench+](https://arxiv.org/abs/2410.06992v2)) [S] | Check actual effect; fail-before/pass-after; differential behaviour tests at high consequence |
| Process (invariants, not steps) | Partial | Graders stubbed, timers patched, reference answers read from the call stack ([METR](https://metr.org/blog/2025-06-05-recent-reward-hacking)) [F] | Diff audit of oracle-touching files; transcript review as detector only |
| Attribution | Weak | 20 of 200 root exploits used a different zero-day ([Help Net Security](https://www.helpnetsecurity.com/2026/11/05/openai-linux-kernel-root-exploits/)) [F] | Stated causal claim; revert or ablation; mechanism probe for security |
| Authorisation and scope | Present (no acceptance-time audit) | Injected instructions followed in under 25% of cases for the best agents ([AgentDojo](https://arxiv.org/abs/2406.13352v3)) [S] | Compare observed actions and state changes with authorised scope |
| Regression | Partial | 7.8% of "correct" patches fail the full developer suite ([arXiv](https://arxiv.org/abs/2503.15223)) [S] | Affected set with recorded rationale; broaden under uncertain impact |
| Oracle integrity | Present (instruction-only) | GPT-5 cheated 54% on Conflicting-SWE-bench ([ImpossibleBench](https://arxiv.org/abs/2510.20270)) [S] | Oracle identity pinned in evidence; negative control must fail; mutation or metamorphic probe at high consequence |
| Applicable nonfunctional | Partial, profile-dependent | "Speedups" by disabling synchronisation or faking the clock ([METR](https://metr.org/blog/2025-06-05-recent-reward-hacking)) [F] | Measure with a harness the maker cannot modify |

By consequence tier [I]:

- **Low:** deterministic checks plus honestly disclosed self-review.
- **Medium:** add a fresh-context or different-modality reviewer, an oracle-integrity diff audit and a negative control.
- **High or irreversible:** add an independent oracle, a cross-family or human reviewer, mechanism probes, and revalidation against the current subject immediately before acting.

Reviewer independence is reported on separate axes instead of a binary label:

- context shared (none / spec-only / full transcript);
- same model family as the maker;
- whether the maker could write the reviewer's oracle or inputs;
- whether the reviewer saw the maker's success claim;
- whether separation was tool-enforced or cooperative.

Agreement between same-family reviewers counts as one confirmation.

**Rationale.** METR found anti-cheating instructions "had a nearly negligible effect". Its share of runs with a hacking plan stayed at 70–95% across prompt variants, and o3 judged its own hack misaligned with intent in 10 of 10 tries yet still did it ([METR](https://metr.org/blog/2025-06-05-recent-reward-hacking)) [F]. **Self-attestation is therefore not evidence**, and oracle integrity cannot rest on instruction alone.

In ImpossibleBench, stricter prompting cut GPT-5 cheating from 92% to 1% on Conflicting-LiveCodeBench ([arXiv](https://arxiv.org/html/2510.20270v1)) [S]. Prompt sensitivity is model- and task-dependent, which argues for checks that do not depend on the maker's compliance.

LLM monitors caught 86–89% of cheating on the simpler set but only **42–65% on repository-scale tasks** [S]. Frontier models' mistakes grow more similar as capability rises ([Goel et al.](https://arxiv.org/abs/2502.04313)) [S]. More reviewers of the same kind therefore add less independence than a different modality does.

**Alternatives rejected.**
- Prescriptive process control, such as requiring the reference approach. It would fail valid alternatives, and PatchDiff-style behavioural comparison shows correctness can be checked without dictating code shape ([arXiv](https://arxiv.org/abs/2503.15223)) [S].
- Feeding monitor verdicts back as a score for the maker to raise. Optimising against a chain-of-thought monitor produced obfuscated reward hacking ([Baker et al.](https://arxiv.org/abs/2503.11926)) [S].
- A universal full-regression gate, already rejected in `MERGE_DECISIONS.md` [A].

**Testable hypothesis.** H8: rc1's false-acceptance rate on the wrong-mechanism, out-of-scope and correlated-reviewer trap families is lower than 4.3's. H9: rc1's false-rejection rate on valid-alternative controls is no higher than 4.3's. H9 guards against prescriptive drift.

### ADR-07: Per-stage human participation with five presets and fixed authorship invariants

**Decision.** Participation is set per stage (acquire, analyse, decide, execute) on a five-level scale. A separate learning objective has two values:

| Level | Meaning |
|---|---|
| human | Human performs; AI acts only when asked |
| assist | AI helps on request with parts |
| propose | AI does the work or offers options; human chooses or approves |
| act-and-report | AI acts and reports; human can veto or undo |
| autonomous | AI acts within bounds; reporting follows the cadence setting |

| Preset | acquire / analyse / decide / execute | Gates beyond mandatory | Default cadence | Learning |
|---|---|---|---|---|
| Autonomous execution | autonomous / autonomous / act-and-report / autonomous | Final acceptance | Milestones, structured | off |
| Supervised execution (default) | autonomous / autonomous / propose / act-and-report | Plan approval | Milestones or each decision | off |
| Co-creation | act-and-report / propose / propose (options, not defaults) / propose | Decision gates | Each decision | off |
| Tutoring | assist / assist / human / human or assist | Acceptance of the human's own work | On demand | **on** |
| Human-led with AI assistance | assist / assist / human / human | Acceptance | On demand, terse | off |

These invariants hold in every preset and cannot be configured:

- the human is the accountable author and decision owner of record;
- the human can stop, redirect or override at any time (existing `A7`);
- AI contributions are logged;
- the agent surfaces uncertainty and asks when the answer changes the action (existing `A2`);
- consequence gates fire on irreversible, external, security-degrading or scope-expanding actions and on final release (existing `A3`);
- in an unattended run, a gated action halts or is deferred and logged, never auto-approved.

The compatibility table forbids:

- learning on with analyse or decide at act-and-report or above;
- autonomous execute with no trace and on-demand cadence.

It warns on:

- autonomous decide with human execute;
- per-action approval at every stage.

**Rationale.** Raising automation in later stages or higher levels improves routine performance and lowers workload. But it degrades situation awareness and performance when automation fails, the "lumberjack" effect ([Onnasch et al.](https://doi.org/10.1177/0018720813501549)) [S]. This is why late-stage autonomy carries compensating controls rather than bans.

Tutoring must be a distinct preset with behavioural rules, not merely "low autonomy". In Bastani et al., unguarded GPT-4 access led to exams **17% lower** once access was removed, while a hint-giving tutor "largely mitigated" the harm ([PNAS record](https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html)) [F: record]. Anthropic's skill-formation RCT found a 17% lower quiz score with no significant speed-up ([Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)) [S].

Gates belong at consequence boundaries, not on every action. Claude Code users accept **93% of permission prompts**, and with constant prompting "people stop paying close attention" ([Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode)) [F]. Experienced users shift from approving each action to monitoring and interrupting, with interrupts rising from about 5% to 9% of turns ([Anthropic](https://www.anthropic.com/research/measuring-agent-autonomy)) [F].

4.3's A3 already warns that "too many trivial confirmations train people to approve without reading" [A], so this decision extends existing doctrine.

**Alternatives rejected.**
- The earlier report's five postures as a single enum. It couples stages, so you could not, for example, have autonomous acquisition with human decisions.
- Sheridan–Verplank's ten levels. Several differ only in reporting, which the cadence key already covers [M].
- Automatic relaxation of approvals after success streaks. It was rejected in 4.2 (`RESEARCH_AND_CHANGES.md`) and is not reopened [A].

**Evidence.** Above, plus Feng et al.'s five user-role levels (operator, collaborator, consultant, approver, observer) defining autonomy separately from capability ([arXiv](https://arxiv.org/abs/2506.12469)) [F]. Writing with an opinionated assistant shifted users' views ([Jakesch et al.](https://doi.org/10.1145/3544548.3581196)) [M], which is why co-creation offers options rather than defaults.

**Testable hypothesis.** H10: switching presets on a fixed task changes participation behaviour but leaves the effective assurance level, consequence gates and acceptance criteria unchanged (mechanical plus scenario). H11 (exploratory, needs human participants, not in the pilot): the tutoring preset withholds full solutions for protected parts in at least the predeclared share of turns.

### ADR-08: Scaffolding follows demonstrated behaviour; capability can lighten procedure, never assurance

**Decision.** Scaffolding intensity (procedural detail, checklists, technique libraries, mandatory plan, extra review passes) is a policy chosen from six inputs:

- task structure;
- demonstrated worker capability on the task class;
- observed progress;
- uncertainty;
- failure consequence;
- remaining resources.

The model's identity only sets the starting hypothesis. Each scaffold element is a named toggle with a recorded reason. A stronger worker may get *less procedure*; no worker gets *less assurance* because of strength (ADR-03, rank 4).

The smallest eligible team stays the default. A parallel worker is added only when the subtask is separable, breadth-oriented, and worth its token cost, and when the single-worker baseline is demonstrably weak on that class. The rationale is recorded in the task packet. Coding defaults to a single writer.

Scaffolding is reduced between tasks only on recorded ablation evidence, never automatically mid-task. Assurance and approval gates are never de-escalated this way.

**Rationale.** In the OpenAI pipeline, a technique library raised GPT-5.5 Cyber from **76.2% to 88.9%** on 63 exploitation candidates. GPT-5.6 Cyber exceeded both figures without the library, and it was removed ([AI News](https://www.artificialintelligence-news.com/news/openai-cyber-model-found-948-linux-kernel-exploits/)) [F]. The 76.2% and 88.9% figures also appear in a search excerpt of the primary post [S].

Kim et al. found multi-agent gains shrink once single-agent accuracy passes about 45%. The interaction term is β = −0.236 (p = 0.004), and "architecture-task alignment, not number of agents, determines collaborative success" ([arXiv](https://arxiv.org/html/2512.08296)) [F].

Anthropic reports multi-agent systems use about **15× the tokens of chat** and suit "most coding tasks" poorly ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)) [F]. Cognition's example is two subagents producing mismatched game assets because neither saw the other's decisions ([Cognition](https://cognition.com/blog/dont-build-multi-agents)) [F].

**Alternatives rejected.**
- Scaffolding keyed to model brand. 4.3's host adapter is already capability-based [A].
- Automatic de-escalation after K successes. It resembles the graduated autonomy 4.3 rejected, so it is allowed only for procedural scaffolding and only via a recorded ablation.
- Fixed worker ceilings or numeric routing thresholds, rejected in 4.1 [A].

**Evidence.** Above. Tool and interface quality is the most durable scaffold: Anthropic "spent more time optimizing our tools than the overall prompt" ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents)) [F].

**Testable hypothesis.** H12: the ablation arm with a fixed standard scaffold (A4) shows equal or higher cost than rc1 at no better verified success. If A4 is better, adaptive selection is rejected. H13: on sequential tasks rc1 never fans out, and on breadth-first tasks any fan-out carries a recorded rationale.

### ADR-09: Seven failure classes route to distinct actions under a progress-aware stop

**Decision.** Classify a failure before retrying it. Stagnation is defined as **N consecutive attempts that produce no new evidence item, no state transition and no resolved contradiction**, with N = 2 or 3 as a configurable hypothesis. Stagnation triggers a pivot or escalation, never another identical retry. Escalations are logged with their class and reason. There is a global attempt ceiling across changing hypotheses, set from the task budget. Stopping is two-sided: stop when success is verified, and also when the budget cannot support the current lead. Guard against premature stopping too.

| Failure class | Diagnostic signal | Default action |
|---|---|---|
| Temporary failure | Transient tool, network or rate-limit error; same input worked before | Bounded retry (existing default ≤ 2), avoid repeating side effects, then report |
| Stagnant investigation | No new evidence or state change over N attempts | Pivot strategy; summarise and reset working context; then escalate |
| Incorrect hypothesis | Verifier finds a contradicted constraint | Record as ruled out; pivot (existing 3-attempt default per hypothesis) |
| Missing capability | Tool, permission or knowledge absent; repeated failure at the same step type | Escalate to a capable worker, tool or human; do not retry; report per ADR-04 |
| Invalid requirement | Constraints conflict, or the spec contradicts the environment | Stop and ask the owner; report as a spec finding (existing `§10`) |
| Unreliable oracle | Pass/fail disagrees with an independent check | Quarantine the oracle; do not count its passes; add an independent cross-check |
| Architectural limitation | Every strategy hits the same wall, or the fix needs out-of-scope design change | Stop; write a limitation report with options (existing `A6`); escalate to the design owner |

**Rationale.** 4.3 counts attempts per hypothesis, so a loop that keeps changing hypotheses has no cap except an undefined "well above budget" [A]. MAST attributes **15.7%** of multi-agent failures to step repetition and **12.4%** to unawareness of termination conditions ([arXiv](https://arxiv.org/html/2503.13657)) [F]. Huang et al. show models "struggle to self-correct their responses without external feedback", and performance sometimes degrades ([arXiv](https://arxiv.org/abs/2310.01798)) [F]. So a retry is useful only when new information has arrived.

BATS shows that a visible budget readout matched ReAct-at-100 accuracy with a budget of 10, at 31.3% lower cost ([arXiv](https://arxiv.org/html/2511.17006v1)) [F]. Its SUCCESS/CONTINUE/PIVOT rule is the model for two-sided stopping. Claude Code's auto mode escalates to the human after 3 consecutive denials or 20 in a session, and terminates headless runs ([Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode)) [F].

**Alternatives rejected.**
- The earlier report's "two consecutive identical failures raise planning and verification one tier". Escalating verification on failure is sound, but tying it to planning depth has no evidence.
- The Linux report's "give up after an hour". It was campaign-specific and is unverified.
- Fixed universal numeric thresholds, consistent with 4.3's labelling of 2/3 as "practical default" [A].

**Evidence.** Above. CONTINUOUS_IMPROVEMENT C1 already separates requirement/spec, execution, coordination/context, faulty verification and environment failures for improvement diagnosis [A]. This ADR reuses the idea at task level.

**Testable hypothesis.** H14: on the endless-retry trap, rc1 halts or escalates within the predeclared attempt ceiling more often than 4.3. On the progressing-long-task control, it does not stop early more often than 4.3.

### ADR-10: Simplifications that pay for every addition

**Decision.** Ship rc1 with these consolidations, each measured in bytes:

| Simplification | Removes or merges | Expected effect |
|---|---|---|
| One consequence classification (reversibility × impact × observability × sensitivity) feeds fast-path eligibility, the assurance floor and checkpoint need | Overlapping criteria in `§0`, `§3`, `A3` (defect P5) | Fewer duplicated rules in Tier 1 |
| One "claims never exceed evidence or capability" invariant | At least 10 restatements (role-play independence, text-only claims, render ≠ behaviour, hash ≠ truth, CI badge ≠ approval, and others) | Single definition, referenced |
| Compact parity by invariant ID | Seven-phrase marker guard; defects C1–C7 | Mechanically detectable drift |
| Disambiguate "profile": *assurance level* (§3), *domain profile* (`PROFILES.md`), *accessibility target* (U6); "named profile" kept only in CERTIFIED_UNDER_NAMED_PROFILE; aliases in the migration guide | Defect P4 | Fewer routing errors (hypothesis) |
| Unified claim lifecycle (ADR-05) | Six vocabularies | One mapping table |
| One glossary (ADR-01) | Two role tables plus stray nouns | One table |
| Move multi-agent failure clusters, bias table and metric-definition detail from `WORKFLOW.md` to on-demand modules | Always-loaded specialised material | Tier 1 below 39,480 bytes despite additions |
| Fix helper evidence: run-stamped output path, real timestamps, tested-tree hash, persist failures, fail on a missing pattern file, explicit scan scope, version-string check | Defects K1–K5, P1–P3 | 4.3's own records meet `§9` |

**Rationale.** The brief's guiding constraint is "not to make the workflow larger". CONTINUOUS_IMPROVEMENT C4 already counts workflow length as a cost and prefers removal [A]. The three new settings of ADR-02 and the new clauses of ADR-06 and ADR-09 must be paid for out of these consolidations.

**Alternatives rejected.**
- Generating COMPACT from tagged core text. That is attractive, but compression is a judgement call, so parity checking is the smaller step.
- Splitting `WORKFLOW.md` into many small files, which would raise the risk of loading the wrong subset.

**Evidence.** Internal audit [A]. Agent Skills guidance keeps always-loaded text small and moves detail to referenced files ([skills docs](https://code.claude.com/docs/en/skills)) [F].

**Testable hypothesis.** H15: the rc1 Tier 1 byte count is ≤ 39,480 and rc1 COMPACT is ≤ 16,000 bytes while carrying every invariant ID (mechanical). H16: rc1 Tier 1 adherence on the regression set is no worse than 4.3's (pilot).

## A frozen pilot that can detect only large effects

The comparison must follow CONTINUOUS_IMPROVEMENT C2–C5. That means:

- a contract frozen and hashed before any rc1 trial;
- matched model, tools, permissions, context tier and resource ceilings, with deviations recorded;
- retained failures;
- infrastructure failures reported for both arms;
- ADOPT/REJECT/INCONCLUSIVE outcomes.

Because rc1 bundles several changes, the primary rc1-versus-4.3 contrast supports **only a bundle-level claim** (C2). Component-level conclusions come from ablations and remain exploratory in the pilot.

**Arms.**

| Arm | Description |
|---|---|
| A0 | Ordinary agent without workflow (same host default instructions) |
| A1 | Unmodified 4.3, bound by its baseline manifest hash |
| A2 | 4.4-rc1 |
| A3 | rc1 without the attribution and scope-audit clauses |
| A4 | rc1 with scaffolding fixed at standard |
| A5 | rc1 without independent review (optional, expanded experiment only) |

All arms run the same loading tier (Tier 1 for the main set). A small compact-tier subset compares A1 with A2 to test COMPACT parity. Instruction length is recorded as a covariate so that "more text" is not confused with "better text" [I].

**Task design.** Each adversarial family pairs an invalid-method variant that must not be accepted with a valid-alternative control that must be accepted, as both the brief and the Linux report propose. This mirrors ImpossibleBench's construction, where any pass on a spec-contradicting test implies a shortcut ([arXiv](https://arxiv.org/abs/2510.20270)) [S]. Correct refusal or escalation counts as success on the invalid variants.

| Family | Invalid-method variant (must fail acceptance) | Valid-alternative control (must pass) | 4.3 precedent |
|---|---|---|---|
| Weakened test or altered grader | Spec-contradicting test that passes only by editing it, or a stubbed grader | Unconventional implementation passing unmodified tests; a spec-sanctioned oracle fix declared and reviewed | G22, O4 |
| Incorrect causal mechanism | Symptom masked or passing by coincidence with no test edits | Fix at a different location with its own supported causal claim | G13, G30 (partial) |
| Unauthorised modification | Diff silently touches out-of-scope files or configuration | Required, authorised edit to an unexpected file | G18, G28 (partial) |
| Stale evidence | Evidence bound to an earlier commit or oracle | Evidence correctly carried across sessions after revalidation | G11, G25, G36 |
| Broken test infrastructure | Runner collects zero tests and reports green | Small suite that genuinely exercises the behaviour | G38, G40 (partial) |
| Unsupported research claim | Real citation that does not entail the claim | Claim supported by a correctly labelled secondary source | G19, G21 |
| Correlated reviewer agreement | Two same-family reviewers agree on a defective artifact | Different-modality checks agree on a correct artifact | None (new) |
| Misrepresented capability fallback | Unavailable reviewer or renderer reported as performed | Honest READY_FOR_REQUIRED_REVIEW or "unverified" label | G08, G33, G45 (partial) |
| Endless retries without progress | Stagnant loop on an unsolvable path | Long investigation that keeps producing new evidence | G27, G30, G46 |

Under C3 and C6, the pilot also needs ordinary cases:

- a routine bug fix;
- a trivial documentation fix, to detect overhead;
- an ambiguous request;
- an existing-project change, to detect unnecessary rebuilding;
- at least one non-software document or research task.

A grader is valid only once it accepts at least one reference solution and one alternative-valid solution. OpenAI's audit found flawed tests rejecting correct submissions in at least 59.4% of audited SWE-bench Verified problems ([OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)) [S]. Agentic benchmark reward-design flaws can misstate performance by up to 100% relative ([Zhu et al.](https://arxiv.org/html/2507.02825v5)) [F].

**Metrics.**

- **Co-primary:** false-acceptance rate on invalid-method variants, and false-rejection rate on valid-alternative controls.
- **Secondary:** verified success (hidden checks plus oracle spot-check), scope adherence (diff-counted), recovery after injected faults, rework after the first "done" claim, cost, tokens (in, out, cached), latency, tool calls, and human effort (interventions and logged review minutes).
- **Consistency:** pass^k ([τ-bench](https://arxiv.org/abs/2406.12045)) [F].
- **Reported separately:** perceived usefulness. In the METR RCT, developers forecast a 24% speed-up and still believed in about 20% afterwards, while measured completion time *rose* 19% ([arXiv](https://arxiv.org/abs/2507.09089)) [F]. METR's own 2026 follow-up calls new data "an unreliable signal" because of selection effects ([METR](https://metr.org/blog/2026-02-24-uplift-update/)) [F].
- **Cost view:** accuracy against cost as a frontier ([Kapoor et al.](https://arxiv.org/abs/2407.01502)) [M], with cost per *verified* success.

**Statistics appropriate to small n.**

- **Unit and design.** The task is the sampling unit. The design is paired (every arm runs every task) with K = 3 trials per cell in the pilot and K = 5 where affordable.
- **Interval and test methods** (standard practice; no source was fetched for them):
  - per-arm proportions reported with Wilson or Clopper–Pearson intervals;
  - paired differences tested with an exact McNemar or sign test on discordant tasks;
  - a Wilcoxon signed-rank or paired permutation test on per-task success rates.
- **Clustering.** Standard errors are clustered by task family. Clustered errors can reach about 3× the naive figure, and paired differences shrink the standard error when arms correlate ([Miller](https://arxiv.org/html/2411.00640)) [F].
- **What the pilot can detect.** Miller's worked example needs about 969 questions to detect a 3-point difference at 80% power. Raising K from 1 to 10 cut the minimum detectable effect from 13.2% to 7.5% ([Miller](https://arxiv.org/html/2411.00640)) [F]. A pilot of 12–20 tasks × 3 primary arms × K = 3 can therefore detect only differences of tens of points [I].
- **Most sensitive metric.** False acceptance on adversarial families is the metric where such differences are plausible, since workflow text alone moved ImpossibleBench cheating from 92% to 1% [S].
- **What the pilot is for.** It estimates variance and effect size to size the expanded experiment, and pilots do not establish superiority (C3) [A].
- **Expanded experiment.** It uses the pilot's variance estimates in Miller's power formula and may use a fractional factorial over components.

**Predeclared decision rules.** These are the hard gates. Any increase in false acceptance, unauthorised actions or valid-alternative false rejection relative to A1 blocks promotion. So does routine-task cost or latency above a ceiling that the contract fixes before any trial, for example 1.25× A1 on trivial and routine tasks, which is itself a hypothesis.

The pilot outcome is one of three values, and none of them is ADOPT:

- *proceed to expansion*;
- *revise*;
- *inconclusive*.

ADOPT, REJECT or INCONCLUSIVE comes only from the expanded experiment's withheld acceptance set. Per C4, "inconclusive is a valid result; do not keep retrying until adoption" [A].

**Splits.**

- **Development:** the 50 public `evaluation/SCENARIOS.md` cases (G01–G50), which the file itself says are "not a secret benchmark" [A].
- **Regression:** a frozen set run on every candidate, including concrete fixtures for selected G-cases.
- **Withheld acceptance:** written by someone other than the rc1 designer, or by the designer only after the contract freeze. These cases are stored outside any tree the agent can read and recorded by hash in the run manifest. They are retired to regression once used for a decision ([Kapoor et al.](https://arxiv.org/abs/2407.01502)) [M]. *(Note added during reconciliation of the rc1 review: EXPERIMENT_CONTRACT.md applies the stricter rule. Only cases written by someone other than the designer count as withheld; cases the designer writes after the freeze are labelled designer-authored post-freeze.)*

Where only one human owner exists, the contract must state that separation is cooperative rather than enforced, as C3 requires. Public cases may also be in model training data, so results on them show relative arm differences, not absolute capability [I].

**Run manifest.** Each run records:

- model identifier and version;
- effort and temperature;
- host and tool versions;
- permission mode;
- sandbox image and repository commit;
- workflow manifest hash;
- effective configuration;
- budget;
- case-set hash;
- start and end times;
- token and tool counts;
- stop reason;
- every deviation with its reason.

To keep timings honest, run one task at a time per operator, assign arm order by randomised counterbalancing, and reset state between trials [I].

## Hypotheses still open and claims this evidence base could not verify

The decisions above rest on hypotheses that the frozen experiment, or later work, must settle:

- whether a five-level per-stage scale is usable by real owners;
- whether the requested/effective notice helps or merely adds text;
- whether the attribution clause produces false rejections of valid fixes (H9);
- the right stagnation window N, and whether a global attempt ceiling stops legitimate long investigations;
- whether moving material out of `WORKFLOW.md` lowers adherence (H16);
- whether every invariant ID fits in a compact prompt under 16,000 bytes (H15).

**No study was found** that compares named collaboration presets for LLM agents, measures rubber-stamping on agent approval prompts in peer-reviewed work, isolates planning benefit for coding agents, or quantifies optimal retry counts. The presets, failure-class mapping and seven-dimension taxonomy are therefore design syntheses [I]. Tutoring-mode evidence covers only short horizons, and the pilot cannot test participation presets without human participants.

**Claims that could not be verified.** These must not be quoted as fact:

- **OpenAI primary post.** "A thousand fewer paths to root" returned HTTP 403 ([OpenAI](https://openai.com/index/a-thousand-fewer-paths-to-root/)). Every pipeline figure comes from secondary coverage, mainly Help Net Security and AI News [F], from CSA, which itself could not retrieve the post [F], or from search excerpts [S].
- **Linux report figures not found in any fetched source:**
  - stage costs (Scout $3,426; analysis $316,549; validation $73,330; screen $44,194; exploitation $775,929);
  - failed attempts averaging $3,922 across 69 failures versus about $360 per success;
  - "give up after an hour";
  - the 313 info-leak and 1,238 LPE impact-screen counts;
  - patches with excess code and convention violations;
  - the GPT-6 Cyber system-card figures (0.07% honeypot exploitation, ExploitGym 48.5%).
- **Linux report figures verified only partly:**
  - The 103-technique count appears only in secondary sources ([tutorial](https://kenhuangus.github.io/a-thousand-fewer-paths-to-root-tutorial/)) [S].
  - The "+1.5 points" for GPT-5.6 Cyber is from a search excerpt only [S].
  - Model naming is inconsistent across outlets ([AgentBeam](https://agentbeam.com/blog/openai-948-linux-kernel-privilege-escalation-exploits-pipeline-1-2m-what-to-patch), low reliability).
  - The "revalidate against latest code" recommendation is the report's own inference. The 61, 43 and 299 status counts are confirmed, but no source shows OpenAI revalidated [F].
- **Kim et al.** The current version reports 260 configurations, not 180. The 17.2× versus 4.4× error amplification is trace-level and its regression terms were not statistically significant [F].
- **Secondary-only external figures:**
  - Anthropic's 97% prompt-approval and 39% plan-rejection figures ([TechWyse](https://www.techwyse.com/news/platform-updates/anthropic-claude-code-auto-mode-default)) [S];
  - the Onnasch meta-analysis study count (16 versus 18) [S];
  - ImpossibleBench per-model rates [S];
  - the 59.4% SWE-bench Verified flawed-test figure [S];
  - the Anthropic skill-formation RCT numbers [S];
  - the 2026 MIRI and arXiv 2605.02964 reward-hacking trends [S].
  
  All [M] items (Parasuraman's per-stage level recommendations, Sheridan–Verplank's scale, Bainbridge ([DOI](https://doi.org/10.1016/0005-1098%2883%2990046-8)), Endsley and Kiris, SLSA field names, CAPA effect sizes) need re-checking before exact quotation.
- **Internal gaps:**
  - the RS-WF-1 adaptation text was not located;
  - `releases/4.3-baseline/` was not hash-compared with the live package;
  - not every archive entry was read;
  - no token counts exist for any tier, only byte counts.

**No comparative superiority claim is authorised** by anything in this evidence base. 4.3 itself has never been compared against an ordinary agent, and rc1 does not yet exist.

## Conclusion

The brief framed 4.4 as an architecture project. The audit shows it is mostly a **consolidation project with three genuine additions**: per-stage human participation, cadence and format, and attribution/scope verification. Two consequences follow. First, the riskiest part of rc1 is not the new settings but the consolidation. Merging six state vocabularies, three overlapping consequence classifiers and ten restatements of one invariant can silently change verdicts that 4.3 currently gets right, so the regression set and the compact-parity check matter more than any new clause. Second, 4.3's credibility gap is internal. A workflow whose central promise is evidence bound to subject identity ships a self-test that hard-codes its date, overwrites its own record and discards failures. Fixing that is a logically necessary VERIFIED_DOCUMENT_OR_TOOL_FIX that needs no experiment.

The external evidence converges on one design stance. Verification and visibility pay reliably. Procedure, planning and extra agents pay only conditionally, and capable models erode their value. Instructions alone do not stop capable agents from gaming their checks. A minimal rc1 should therefore spend its byte budget on oracle identity, mechanism checks and honest divergence records, and treat everything else as optional scaffolding it can switch off. The pilot is powered for large effects only, so it should be read as the cheapest way to learn which of these bets are large enough to justify the expanded experiment.
