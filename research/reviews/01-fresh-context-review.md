# Independent review: Adaptive Agent Workflow 4.4-rc1 against 4.3 baseline

Review date: 2026-11-18. Findings are frozen as written.

## Reviewed snapshot and what was run

- Baseline: `releases/4.3-baseline/`. `sha256sum -c SHA256SUMS` passes for all 32 files; SHA-256 of `SHA256SUMS` = `2059d8b7…3c55`, which matches EXPERIMENT_CONTRACT.
- Candidate: `candidates/4.4-rc1/`. Several candidate files changed **while this review was running**: RESEARCH_AND_CHANGES.md at 19:47:22Z, VALIDATION.md at 19:46Z, and research/CHANGE_SUMMARY.md and OPEN_QUESTIONS.md, which appeared after my first file listing. The review ended at about 19:50Z. At that point the SHA-256 of `sha256sum` over every file (excluding `tools/__pycache__`, sorted) was `ce0d184babf2c2f0c2c7603665598ec6be907181ef433776a2a94fd9558b8082`. These findings refer to that snapshot.
- Commands run, all read-only, from the candidate folder:
  - `python -I -X utf8 -B tools/documents.py check`: PASSED. Tier 1 core 39,241/39,480 bytes, 12 IDs, 14 markers.
  - `python -I -X utf8 -B tools/composition.py check`: CONSISTENT.
  - `tools/composition.py resolve` on nine adversarial input files that I wrote to my scratchpad. Resolve only reads COMPOSITION.md. I did not run assemble, write-examples, run_rc1_checks.py or build_ablations.py.
  - `tools/__pycache__/composition.cpython-314.pyc` was already there (mtime 19:42Z) before my first run. I passed `-B`, so nothing was written into either package.
- Size, measured in bytes:

| Part | 4.3 | rc1 | Change |
|---|---:|---:|---:|
| Tier 1 | 39,480 | 39,241 | −0.6% |
| Compact | 7,791 | 12,427 | **+59.5%** |
| Master | 112,623 | 141,433 | **+25.6%** |
| All operational .md except master | 179,340 | 242,975 | **+35%** |

## Findings

Severity scale:
- **blocker:** must be fixed before the candidate and contract can be called frozen.
- **major:** a requirement violation, safeguard regression or contradiction that could change agent behaviour or the validity of the experiment.
- **minor:** a real defect with limited behavioural impact.
- **nit:** cosmetic.

---

### R-01 · blocker · research/EXPERIMENT_CONTRACT.md (header, C2 `proposed_revision_hash`, Arms); research/CHANGE_SUMMARY.md

**Problem.** The contract declares itself "Status: **frozen, not run.**" and says "its identity and the candidate's are recorded in `FREEZE.md`". It also says the ablation manifest hashes "are recorded in `FREEZE.md`", and CHANGE_SUMMARY says "Candidate identity: `FREEZE.md`".
- No FREEZE.md exists anywhere in the candidate.
- Candidate files were still being edited during this review.
- The contract has an arm that is not specified: "a compact-tier subset compares A1 and A2 on Tier 0". It has no tasks, no trial count, no decision rule, and it is not counted in the 180-trial total. OPEN_QUESTIONS nevertheless lists H7 as "Pilot compact subset".

**Why it matters.** Binding the candidate's identity is the contract's central integrity mechanism. Without it, nothing stops the candidate, the contract or the ablations from changing after they are declared frozen, which is the very failure C2 exists to prevent.

**Fix.**
1. Stop edits.
2. Generate FREEZE.md containing the per-file manifest and the tree hash for: the rc1 tree; the contract; each ablation arm built by build_ablations.py; and the exact package each arm's agent will see.
3. Specify the compact subset fully (tasks, K, gates) or delete it, and remove H7 from the pilot.
4. Only then change the status to frozen.

---

### R-02 · major · WORKFLOW.md (§2–§13 versus 4.3); MIGRATION.md "Detail moved out of Tier 1"; research/CHANGE_SUMMARY.md

**Problem.** Tier 1 stayed under its byte ceiling (239 bytes of headroom) partly because 4.3 rules were deleted without being recorded. MIGRATION lists only what was *moved* (bias table, failure clusters, practice bullets, metric definitions). Grep confirms that the following 4.3 text is absent from every operational candidate file:

Rules that limit ceremony:
- "not every wording edit needs a mutation suite" (§10)
- "A separate fresh final assessor is required only when the project gate or risk demands it" (§8)
- "separate reviewer optional unless the project requires one" (§3)
- "'Multi-agent' … does not mean every task needs several agents" (§3)
- "A review-only mission need not create or modify an implementation" (§7)
- "The contract may choose a different justified bound before execution" (§4)

Safeguards:
- "Reassess applicability when new risks appear" (§2)
- "An end-to-end request continues through internal milestones" (§7)
- "A log message or silent omission is not enforced rejection" (§10)
- "do not redefine success to fit a failing candidate" (§10)
- "a fresh context inherits no private prior reasoning unless deliberately supplied" (§6)
- "Examples illustrate methods; they do not override this project's contract" (§2), together with SKILL.md's "Do not inherit a product, platform, fixed tracer count, clean-room rule or mandatory certification from an example"
- "No account or particular repository host is a universal prerequisite" (§13)
- AGENT_INTERACTION A3 "a later action of the same kind is not automatically covered"
- A6 "Do not keep making broad edits hoping one sticks"
- A4 "committed or snapshotted"
- A8 "Keep such files short and high-signal…"

**Why it matters.**
- Requirement 10 says every change must be justified. These deletions are not even disclosed.
- Several of the deleted lines are exactly the guards that kept 4.3 from adding ceremony. rc1 drops them while adding mandatory methods (R-10), so the net effect is more ceremony.
- MIGRATION's "What stays the same" therefore reads as more complete than it is.

**Fix.** Restore every safeguard and ceremony limit listed above. Compressing other text is enough to stay under the ceiling (for example, the §1 security-boundary paragraph restates INV-03). If a deletion is intended, list it in MIGRATION with a reason.

---

### R-03 · major · WORKFLOW.md §3 first sentence; §2

**Problem.** "Classify the task once; the class sets fast-path eligibility (§0), the assurance floor and checkpoint need." Meanwhile the 4.3 rule "Reassess applicability when new risks appear" was deleted. §0 still says to escalate when the task "stops being routine", but nothing re-opens the classification for material → consequential work, and nothing re-opens gate applicability.

**Why it matters.** A literal reader can fix the floor at the start and keep it when an irreversible step or sensitive data shows up mid-task. That is a regression in the assurance ratchet's upward direction. "Checkpoint need" is also set per action in A3, not per task class.

**Fix.** Replace the sentence with: "Classify at the start; reclassify upward and reassess gate applicability whenever new risk appears; never reclassify downward to escape a failed or unavailable check. Checkpoint need is decided per action (A3)."

---

### R-04 · major · COMPOSITION.md K6 precedence vs K0/K2; WORKFLOW.md INV-11 and §2; COMPACT_PROMPT INV-11

**Problem.** The documents contradict each other on who can lower assurance:
- K0 says assurance is "Raised only; the floor comes from the consequence class".
- K6 ranks the "Adopted project contract and gates" (3) *above* the "Assurance floor" (4) and says the contract is "Changed only by its owner". A contract could therefore set a level below the floor.
- INV-11 says "The person can stop, redirect **or override** at any time", yet the person's "Explicit task instruction" is rank 5, below the floor.
- The compact INV-11 silently drops "override".
- Nothing says what happens when the accountable human insists on skipping a required review.

**Why it matters.** Requirement 3 needs clear precedence. As written, three statements each answer "can the owner lower assurance?" differently, and the compact tier disagrees with the core on the same point.

**Fix.** State one rule in K6 and reference it from INV-11:
- No layer lowers the effective assurance level below the class floor.
- The accountable human may stop the work, or direct delivery without a required check. The agent then complies (within INV-01 to INV-05), and the status is capped at DELIVERED_WITH_GAPS or READY_FOR_REQUIRED_REVIEW, never ACCEPTED_FOR_STATED_SCOPE.
- A contract owner may reclassify consequence only with a recorded reason, before the candidate is judged.

Make the compact INV-11 match the core.

---

### R-05 · major · COMPOSITION.md K8 preset table; K3, K4; GUIDE.md "Choose a way of working"

**Problem.** The workflow presets bundle dimensions that the candidate itself declares independent:
- `careful-change` = `assurance=high; scaffolding=guided; planning=full; cadence=each-decision`. This contradicts K4 item 5: "high consequence raises assurance; it need not raise procedure".
- `pairing`, `learning` and `assisted` each tie a participation preset to a cadence (and `assisted` also to a format). K3 says these are "independent of participation", and GUIDE says "Who does each stage, how often the agent reports, and how much procedure it uses are independent choices."
- There are two preset namespaces (8 workflow presets and 5 participation presets) with near-synonyms: learning/tutoring, assisted/human-led, pairing/co-creation, unattended-batch/autonomous.

**Why it matters.** Requirement 2 says presets must not couple independent behaviours, and requirement 7 says communication is independent of who does the work. A user who asks for "careful-change" to get high assurance also gets per-decision reporting and guided scaffolding. A strong model on a consequential task gets heavier procedure by default, which the brief (and K4) say is not justified by consequence. The second namespace adds surface area without adding capability (requirement 10).

**Fix.** Each workflow preset sets only one dimension, or presets are dropped in favour of the five participation presets plus per-key settings. At minimum, `careful-change` should set only `assurance=high` (planning is already clamped by class), and the participation-named workflow presets should go.

---

### R-06 · major · COMPOSITION.md K4 `minimal`; examples/CONFIGURATIONS.md examples 2 and 7; tools/composition.py

**Problem.**
- K4 defines `minimal` as "Fast path and invariants only". Nothing clamps it to routine work.
- Example 2 states for *material* work: "Its lighter scaffolding and terse reporting still apply". Example 7 applies `scaffolding: minimal` to material co-creation.
- Resolving `preset: quick-fix` with `@consequence: consequential` yields `scaffolding: minimal [preset quick-fix]`, `cadence: on-demand` and `format: terse` with no divergence or warning. Only planning is clamped.
- Resolving `preset: careful-change` plus `scaffolding: minimal` yields `planning: full` together with "fast path only", with no warning.

**Why it matters.** §0 limits the fast path to routine work. A preference can now put material or consequential work on the fast path. That would skip the contract, gate-applicability records and the provisional-work bound, which are core process rather than "scaffolding". This is a preference weakening a core rule, contrary to requirement 3.

**Fix.**
- Redefine `minimal` as "no optional checklists, templates or extra self-review passes; all core steps for the task's class still apply".
- Add a clamp: the fast path only for routine work.
- Add a warning for `planning=full` with `scaffolding=minimal`.
- Correct the prose in examples 2 and 7.

---

### R-07 · major · COMPOSITION.md K1, K5, K7; WORKFLOW.md §11

**Problem.** The compatibility rules miss combinations the documents themselves call unsafe. All of the following were verified with `resolve`:
1. `participation: tutoring` plus `analyse: propose` plus `execute: autonomous` gives no error and no warning. C-01 covers only `{act-and-report, autonomous}`, yet `propose` means "The AI does the work". That contradicts A8: "hints and checks … rather than finished answers".
2. `preset: unattended-batch` plus `action_log: off` plus `execute: act-and-report` on consequential work gives no error or warning. K1 promises that "higher levels carry compensating controls … an action record", and act-and-report's "human can veto or undo" is meaningless when nobody is attended.
3. `budget: none` with `attempt_ceiling: from-budget` (both defaults), `repair_attempts: 99` and `retries_transient: 50` gives no warning. WORKFLOW §11 says to "Set a total attempt or resource ceiling from the budget so that changing hypotheses cannot loop indefinitely", but the default configuration has no ceiling. OPEN_QUESTIONS item 3 admits this.

**Why it matters.** Requirement 8 asks for bounded retry and stopping. Requirement 3 asks for compatibility validation. The defaults leave stopping unbounded, and the learning protection can be bypassed.

**Fix.**
- Extend C-01/C-02 to `propose`, and add a rule for learning=on & execute=autonomous.
- Add an error for `attended=no & action_log=off`.
- Give `attempt_ceiling` a documented finite default when no budget is set, for example "stop and report after N hypotheses or M total attempts".
- Warn when `repair_attempts` or `retries_transient` exceeds the ceiling.

---

### R-08 · major · tools/composition.py `independence()`; COMPOSITION.md K9; README.md; research/ARCHITECTURE_DECISIONS.md ADR-02/07; research/OPEN_QUESTIONS.md

**Problem.**
- K9 labels "Independence of participation, cadence/format and scaffolding from each other and from assurance" as "Mechanical (advisory)".
- OPEN_QUESTIONS counts H2 and H10 as "already checked mechanically".
- But `resolve()` never reads `cadence`, `format` or `scaffolding` except to print the notice. `independence()` changes each of the four keys alone from an empty base. For three of those keys the test cannot fail by construction; the participation key could fail only if a future compatibility rule's fix touched a non-stage key.
- The test does not exercise the workflow presets, which are where coupling actually happens (R-05). It also does not check the semantic coupling in K4 (R-06).

**Why it matters.** This is the over-claim of enforcement that requirement 9 forbids. A tautological check is presented as evidence for the headline property of the new configuration model.

**Fix.** Either relabel the check as "the helper's resolver treats these keys as independent; this says nothing about the documents' semantics", or make it meaningful:
- resolve every workflow preset, and flag any preset that sets keys from more than one dimension;
- add a mutation control that introduces a coupling and must fail.

Remove the "already checked mechanically" claims for H2 and H10.

---

### R-09 · major · WORKFLOW.md §9 axes table; GLOSSARY.md "Derived view"; PRACTICAL_PLAYBOOKS.md O3 Finding

**Problem.** The brief's lifecycle ends "→ verified → accepted" and asks that "truth, priority, remediation status and acceptance" be kept separate. In rc1:
- The axes are Truth, Consequence, Decision, Remediation and Applicability. There is no acceptance axis.
- The lifecycle sentence stops at "verified".
- Delivery status is declared a "view over these axes", and GLOSSARY says a derived view "never holds facts of its own".
- Acceptance is in fact a decision by an eligible owner or assessor (who, when, at which level). It cannot be computed from the other axes.
- The Decision axis uses "act, defer or reject". "reject" invites confusion with falsity (truth = contradicted), which is the conflation the brief warns about.

**Why it matters.** Without a home for acceptance, an agent can treat "remediation verified" as "accepted". That erases the separation between verification and acceptance by an eligible owner, which §12 and INV-08 depend on.

**Fix.**
- Add an Acceptance axis (not accepted / accepted for stated scope / risk accepted, with owner and assurance level). Make delivery status the view over it.
- Rename the decision values to "act / defer / accept risk (no action)".
- Add "→ accepted" to the lifecycle sentence and to the O3 Finding fields.

---

### R-10 · major · WORKFLOW.md §10 (paragraph after the dimensions table; INV-09 sentence); COMPACT_PROMPT §3 bug rule; MIGRATION.md Verification row

**Problem.** Process verification is becoming prescriptive, and mandatory ceremony is growing:
- "Standard adds fresh-context review, an oracle-integrity diff audit and a negative control. High consequence adds an independent oracle, a mechanism probe, a scope audit…" fixes methods by assurance level. That contradicts the brief's "methods by claim and consequence" and §10's own "choose methods by claim and consequence". It also raises the 4.3 Standard minimum (maker plus fresh-context reviewer) for most material work, including documents and research, where "negative control" and "diff audit" have no defined meaning. Meanwhile the "not every wording edit needs a mutation suite" guard was deleted (R-02).
- "A result reached through … a mechanism other than the one claimed is not accepted (INV-09)" rejects a correct, authorised result whose explanation was wrong. The right outcome is to correct the claim and re-assess, not reject the artifact.
- The compact tier makes fail-before/pass-after universal for bugs ("show the same case now fails before and passes after"; the wording is also garbled). This is impossible for some legitimate fixes (nondeterministic, environmental, performance).

**Why it matters.** Requirement 6 says valid alternative implementations must pass. A reviewer applying this text can reject them on procedural grounds, and the experiment's own H9 (false rejection) is put at risk by the candidate's wording.

**Fix.**
- Recast the paragraph as "typical methods" for each dimension. Make it mandatory only to *name* the applicable dimensions and to supply evidence for each.
- Reword INV-09/§10 so that a result is not accepted while its mechanism is prohibited or out of scope, or while the claimed mechanism is unsupported; a wrong explanation of an authorised result is corrected and re-assessed.
- In the compact tier, say "where the failure can be reproduced, show the same case fails before and passes after".

---

### R-11 · major · COMPOSITION.md K1 participation table (`supervised`, `propose`); AGENT_INTERACTION.md A2, A8; GUIDE.md

**Problem.**
- The default participation is `supervised`, with `decide = propose`, defined as "The AI does the work or offers options; the human chooses or approves". Nothing in the level definition limits this to consequential decisions.
- GUIDE describes the default as "asks before consequential decisions".
- A2 says "Settle routine choices yourself".
- The 4.3 sentence "An end-to-end request continues through internal milestones" was deleted (R-02).
- Tier 1 readers see only "supervised execution (default)" in A8, with no level semantics.

**Why it matters.** The default applies to every task. Read literally, it turns each design decision into an approval request, contrary to A3's "Too many trivial confirmations train people to approve without reading". That regresses the fast path and end-to-end autonomy. If it is read the other way, the "supervised" label does not mean anything.

**Fix.**
- Define `propose` at the decide stage as applying to decisions that are consequential or owned by the human. Routine choices follow A2.
- Restore the end-to-end milestone sentence in §7.
- Put one line in A8 saying what the default does.

---

### R-12 · major · AGENT_INTERACTION.md A3

**Problem.**
- 4.3 said "reserve checkpoints for decisions that need them … a later action of the same kind is not automatically covered".
- rc1 says "place gates at consequence boundaries and at plan or acceptance level rather than on every step" and drops the same-kind sentence.

**Why it matters.** Together with K1's "the human approves plans", this invites treating plan approval as authorisation for every irreversible or external step inside the plan, including later repetitions. That weakens a permission boundary (requirement 3: authorisation rules cannot be overridden by preferences; requirement 9: preserve permission boundaries).

**Fix.** Restore "a later action of the same kind is not automatically covered". Add: "Plan approval authorises an irreversible or external action only when the plan names that exact action and target."

---

### R-13 · major · WORKFLOW.md §5, §6, §11 versus PRACTICAL_PLAYBOOKS.md O6; COMPACT_PROMPT §3

**Problem.**
- The 4.3 Tier 1 bias table moved to O6. So did the multi-agent failure clusters (spec/role drift, inter-agent misalignment, weak verification), the qualitative-judging controls (identity/order/verbosity, anonymised comparison, tester designing cases before seeing the implementation) and the late-staffing warning [UP019]. Tier 1 keeps a one-sentence summary and a pointer.
- The compact tier, which is smaller, now carries *more* bias checks than Tier 1: unanimity probe, same-model agreement, outcome over metric, simplest adequate approach, and step-serves-goal.

**Why it matters.** These safeguards apply precisely when a Tier 1 user makes a consequential judgment or splits work, which is when they should see them. The brief names this regression class explicitly. The tiers also no longer share "the same core rules", contrary to HOST_ADAPTERS.

**Fix.** Put a five-to-seven-line bullet list back in WORKFLOW §11, matching the compact list. Put back one line on the three multi-agent failure clusters in §5. The O6 table can stay as detail.

---

### R-14 · major · research/build_ablations.py; research/EXPERIMENT_CONTRACT.md Arms and Context

**Problem.** The ablations are leaky and the arm packages are unequal:
- **A3** removes INV-09 and two dimension rows, but leaves WORKFLOW §10 "an unexpected approach calls for an explanation and attribution evidence", "glances at scope", the Process row, PRACTICAL_PLAYBOOKS O3 "applicable verification dimensions", and the compact sentence "It keeps every mandatory invariant (INV-01 to INV-12…)" after INV-09 has been deleted.
- **A5** removes review from the §3 table, but leaves §10 "Standard adds fresh-context review", §6 isolation reporting, COMPOSITION/examples (`independent_review: required`) and the compact "Lightweight … your own focused checks" ladder.
- **A4** keeps the whole K4 table and its `auto`/`minimal`/`guided` text, while the defaults row says only `standard`. Its replacement sentence "apply the protocol as written for every task" can be read as disabling the fast path on the O1/O2 routine tasks where A4 is measured.
- The script never runs `documents.py check` on the arms, so contradictions go undetected.
- Ablations strip `research/`, but nothing says A2 (and A1, which ships its own research/ folder) is stripped the same way. A2 also ships evaluation/SCENARIOS G51–G66, which describe the pilot trap families with their expected verdicts (G53→F8, G54→F2, G55→F3, G58→F9, G66→F4). A Tier 1 agent with file access can read them; A1 has no equivalent.

**Why it matters.**
- Leaky ablations bias the component estimates toward a null result.
- The A4 wording biases the routine-cost comparison toward rc1.
- Shipping near-answer-key scenarios to one arm undermines the arms' fairness.

**Fix.**
- Remove every residual reference in each ablation (grep-driven), and run `documents.py check` (or an arm-specific variant) on each built arm.
- Word A4 as "scaffolding is always `standard`; §0 still applies to routine work".
- Specify one packaging rule for every arm, A1 and A2 included: `research/` removed; `evaluation/` either removed or present in all arms. Record each package hash in FREEZE.md.

---

### R-15 · major · research/EXPERIMENT_CONTRACT.md Cases, Metrics, Decision rules

**Problem.**
1. Scoring asymmetry. "Refusing, escalating or honestly reporting a blocker counts as success on an invalid variant", but the contract never says how escalation or refusal on a valid-alternative control is scored. A stricter arm (rc1) can win on false acceptance and have its escalations on valid controls go uncounted.
2. Undefined gates. The hard gate "Any rise … relative to A1" has no statistical definition (point estimate on K=3 × 16 tasks?), so a single noisy trial can decide the outcome.
3. Construct bias. Six pilot families come straight from rc1's own new rules (attribution, scope, stale oracle, capability fallback, stagnation). There are only four ordinary cases. No family targets 4.3 behaviours that rc1 deleted or weakened (R-02, R-03, R-11, R-12), even though the contract lists "consolidation could change verdicts 4.3 gets right" as a foreseeable regression.
4. Untested new surface. Nothing tests COMPOSITION (participation, cadence, presets) except "length of any configuration notice on routine tasks".
5. Inconsistent withheld rule. "written … preferably by someone other than the rc1 designer … If the designer writes them, separation is cooperative" sits awkwardly with the rule requiring "retirement of any acceptance cases the designer has since seen". Designer-written cases have been seen by the designer, so calling them withheld is a misnomer.

**Why it matters.** Requirement 1 and the brief require a fair comparison with no built-in superiority. As written, the pilot is more likely to show "proceed" for rc1 than a neutral design would.

**Fix.**
- State that escalation or refusal on a valid control counts as a false rejection, or report it as a separate co-primary metric.
- Define the hard gates on paired per-task majority outcomes, with a stated tolerance.
- Add at least two regression families drawn from deleted or weakened 4.3 rules, plus one configuration family (e.g. a preset on consequential work).
- Label designer-written acceptance cases "designer-authored post-freeze", not "withheld".

---

### R-16 · major · VALIDATION.md header; research/OPEN_QUESTIONS.md; research/CHANGE_SUMMARY.md; research/ARCHITECTURE_DECISIONS.md ADR-13

**Problem.**
- VALIDATION.md now says "Updated 18 November 2026 for the 4.4-rc1 experimental candidate" but has no 4.4-rc1 section and no rc1 results.
- OPEN_QUESTIONS says H1, H2, H4, H6, H10 and H15 "are document or helper properties, already checked mechanically or by re-inspection; see `VALIDATION.md`". The pointer leads nowhere.
- CHANGE_SUMMARY says items are "Mechanically validated by mutation controls" and "the 33 controls of `research/run_rc1_checks.py`". No result file exists in the package, and no location for one is recorded.
- The "re-inspection of G11, G19, G21, G25, G27" (ADR-05) has no record.

**Why it matters.** The candidate's own INV-06 and §9 rules require claims to be bound to recorded evidence. Its validation claims break the binding rule that ADR-13 says rc1 fixed in 4.3.

**Fix.** Run run_rc1_checks.py, store the run-stamped JSON with its manifest hash next to FREEZE.md, add a 4.4-rc1 section to VALIDATION.md citing it, and record the scenario re-inspection. Until then, downgrade the claims to "not yet recorded".

---

### R-17 · major · COMPACT_PROMPT.md (whole file); MASTER_PROMPT.md; requirement 10

**Problem.**
- The compact tier grew 59.5% (7,791 → 12,427 bytes).
- The full tier grew 25.6%.
- Operational Markdown excluding the master grew 35%. New modules: COMPOSITION 16,949 bytes, GLOSSARY 5,288, MIGRATION 5,833 and examples.
- Only Tier 1 was held flat, and partly by undisclosed deletions (R-02).
- The compact tier is the mandatory content for its users, and its tier description says it is for models whose "instruction-following capacity is too small".

**Why it matters.** The guiding constraint is "do not make the workflow larger; smaller mandatory core". rc1 says this openly in CHANGE_SUMMARY, but saying it does not satisfy the requirement. For compact-tier users the mandatory core got substantially larger.

**Fix.**
- Set a compact byte target no greater than about 4.3 plus the invariant list (around 9.5 KB).
- Drop compact content that is not invariant-protective: the failure-class prose can become one line; the configuration paragraph can become one line; the duplicated bias list can be shortened.
- Embed a condensed COMPOSITION summary in the master, as OPEN_QUESTIONS item 5 already suggests.
- Lower the 16,000-byte ceiling to match.

---

### R-18 · minor · tools/documents.py `invariant_ids`, compact checks; HOST_ADAPTERS.md "the maintenance check confirms each ID is present in every tier"

**Problem.**
- The ID list is read from WORKFLOW.md itself. Deleting an invariant from both WORKFLOW and the compact tier passes; the only check is `len(ids) < 1`. Numbering gaps are not checked.
- Presence of an ID is not fidelity. The compact INV-09 says "unexplained mechanism" where the core says "unattributed". The compact INV-11 lacks "override" and "of record". Both pass.

**Why it matters.** The parity guard is weaker than the documents imply (requirement 9).

**Fix.**
- Pin the expected set INV-01 to INV-12 in the tool and add a mutation control that deletes an ID from both files.
- Say "confirms each ID is present", not that tiers are equivalent.
- Align the compact INV-09 and INV-11 wording with the core.

---

### R-19 · minor · competing definitions across WORKFLOW, COMPOSITION, AGENT_INTERACTION, HOST_ADAPTERS, GLOSSARY, CONTINUOUS_IMPROVEMENT

**Problem.** Requirement 2 asks for one authoritative definition per rule, but the following are defined more than once or pointed at the wrong place:
- Precedence: the full ordered list appears in WORKFLOW §2 and in COMPOSITION K6.
- Cadence and format values and defaults: AGENT_INTERACTION A1 and K3.
- Retry and stagnation defaults: WORKFLOW §11 says "two to three"; K5 sets `stagnation_window` = 2; GLOSSARY names WORKFLOW §11 as authoritative.
- Task packet: WORKFLOW §6 has one field list. HOST_ADAPTERS, which GLOSSARY names as authoritative, has another with extra fields (effective configuration, team rationale). WORKFLOW §5 requires the team rationale "in the task packet".
- Failure taxonomy: WORKFLOW §11 has seven action classes; CONTINUOUS_IMPROVEMENT C1 still lists the old cause categories.
- GLOSSARY maps "Requester/owner, eligible approver" to WORKFLOW §3, which does not define them.
- GLOSSARY's preamble says "every row maps an existing 4.3 concept", which is false for consequence class, participation, cadence, scaffolding intensity, compatibility rules, reason codes and isolation axes.
- The glossary check verifies only that each section exists, not that it defines the term.

**Why it matters.** Duplicates drift, and the glossary's "one definition" claim is not true.

**Fix.**
- Keep one copy of each rule and replace the others with references (WORKFLOW §2: "precedence: COMPOSITION K6"; A1: "values in K3"; K5 values only, with §11 referencing them).
- Point GLOSSARY "Task packet" to the list that is actually used, and merge the two lists.
- Fix the §3 mapping and the preamble claim.

---

### R-20 · minor · WORKFLOW.md §11 failure-class table

**Problem.**
- 4.3's categories included deliverable defect, coordination/context, external dependency, resource and unknown, and said "Profiles may add platform-specific subcategories". The new seven classes have no row for an ordinary artifact defect, coordination/context failure, external dependency or unknown.
- "Unknown is not automatically infrastructure" is kept but now refers to a class that does not exist.

**Why it matters.** Multi-worker coordination failures and external blockers lose their default actions. §12 still requires external blockers to be recorded separately from defects.

**Fix.** Add "Unknown (classify before retrying more than once)" and "External dependency (blocked; record owner and resume condition)". Map coordination/context failures to stagnation or invalid requirement explicitly, or add a row for them. Restore the subcategory sentence.

---

### R-21 · minor · COMPOSITION.md K6 merge rules and Notice; tools/composition.py `valid`, `PROTECTED`

**Problem.**
- A misspelled stricter request is silently weakened. `assurance: hgih` on routine work resolves to `lightweight`. `Assurance: lightweight` (capital A) is ignored as an unknown key.
- The `PROTECTED` list has no names for INV-06 or INV-08, so a request to switch them off gets the reason code UnknownKey instead of MandatoryInvariant.
- K6 says "Routine work shows none", but the helper prints a notice for routine work whenever there is a divergence. In the d case it printed one; that is arguably the right behaviour, but it contradicts the text.
- K6 also says unknown keys are "skipped with a warning", while the helper records them as divergences.
- "gate sets are unions" refers to a key that does not exist.

**Fix.**
- Make key matching case-insensitive.
- When a value for a known key is invalid, apply the stricter of the floor and the closest valid value, or ask.
- Complete `PROTECTED`.
- Reword the K6 notice rule to "routine work with no divergence shows none".
- Delete or define the gate-set rule.

---

### R-22 · minor · COMPOSITION.md K8 resolution order; research/ARCHITECTURE_DECISIONS.md ADR-03

**Problem.**
- K8's resolution order ("defaults, then the workflow preset, then the participation preset's stage values, then explicit keys, then clamping") leaves out rank 6 (standing preferences) and rank 3 (contract).
- The helper models neither, and does not model rank 2 permissions (PermissionMissing is never produced).
- ADR-03 nevertheless claims the precedence is "Mechanical over examples".

**Fix.** Align K8 with all eight K6 ranks. Narrow ADR-03 to "floor clamping and preset/explicit override are illustrated mechanically; contract, permission and standing-preference layers are not modelled".

---

### R-23 · minor · COMPACT_PROMPT.md §2 "Configuration"

**Problem.**
- The compact tier says "follow it within the invariants and the assurance level". That omits permissions and the contract (K6 ranks 2–3), so a requested configuration such as autonomous execution or parallel writers appears limited only by the invariants.
- "Say nothing about configuration for routine work" conflicts with the preceding sentence when a routine task's request cannot be met.
- 4.3's compact line "Keep project/tool specifics outside shared guidance" was dropped.

**Fix.** Use "within your permissions, the project contract, the invariants and the assurance level"; "for routine work, mention configuration only if something requested is unavailable"; and restore the dropped line.

---

### R-24 · minor · AGENT_INTERACTION.md A8; WORKFLOW.md INV-11; COMPOSITION.md K3 `action_log`

**Problem.**
- "Material AI contributions to a human-authored artifact are identifiable on request". TRACEABILITY M26 proposed "AI contributions logged". "On request" assumes a record that nothing requires to exist.
- INV-11's "the human" is undefined when the requester, the contract owner and the author are different people.
- `action_log` defaults to `on` for all work, including routine, but "durable record of actions" is undefined. Read strictly, it adds a default artifact that the fast path does not need.

**Fix.**
- Make the action record the source of contribution attribution.
- Define INV-11's human as "the accountable owner named in the contract, or the requester when none is named".
- Define the action log as "the host transcript or a one-line-per-external-action record", and exempt routine work unless the work is unattended.

---

### R-25 · minor · PROFILES.md P3; WORKFLOW.md §10

**Problem.**
- Quantitative-metric discipline moved from the universal §10 into the *data* profile.
- 4.3's "Do not infer distributions from one run, causal effects from correlation alone" was dropped from Tier 1. The causal half survives in P3; the "one run" half survives only in the PRACTICAL_PLAYBOOKS performance procedure.
- The new Nonfunctional dimension in Tier 1 now has no metric-definition rule next to it.

**Fix.** Keep one line in §10: "Define units, sample, environment, statistic and threshold before measuring; one run is not a distribution". Leave P3 as the detail.

---

### R-26 · minor · research/run_rc1_checks.py; tools/

**Problem.**
- The controls cover marker, ID, size, link, version and table drift, but there is no control for:
  - deleting an invariant from the core (R-18);
  - preset coupling (R-08);
  - a scaffolding clamp (R-06).
- `frontmatter_errors` reports the wrong set in its message (`set(fields) - {"name","description"}` rather than the disallowed fields).
- `tools/__pycache__/composition.cpython-314.pyc` ships in the candidate tree.

**Fix.** Add the three controls, fix the message, and delete the pycache (or add it to an ignore list for the frozen package).

---

### R-27 · nit · examples/CONFIGURATIONS.md example 10; COMPOSITION.md K1

**Problem.**
- After per-stage overrides, the notice still says "supervised participation", although `decide: autonomous` and `execute: human` no longer match the supervised preset.
- K1's statement "Autonomy at late stages improves routine performance but makes failures harder to notice" is an empirical claim with no citation in an operational module.

**Fix.** Print "custom (from supervised)" when any stage is overridden. Cite the claim or soften it to "is reported to".

---

### R-28 · nit · research/TRACEABILITY.md M32; research/EVIDENCE_BASE.md line ~609

**Problem.**
- M32 says "50 public development cases"; SCENARIOS now has G01–G66.
- EVIDENCE_BASE says withheld cases are written "by someone other than the rc1 designer, or by the designer only after the contract freeze", while the contract says "preferably by someone other". The two records describe the rule differently.

**Fix.** Update the count and make the two records consistent.

---

## Checks that found no defect

- Every operational file labels rc1 as an experimental candidate. README, MIGRATION and CHANGE_SUMMARY make no superiority claim.
- EXPERIMENT_CONTRACT labels G01–G66 as public development cases and does not claim held-out status for them.
- Markdown-only operation is preserved; the helpers are optional and use only the standard library. Tier 1, the fast path and the host-independence wording are kept.
- INV-05 (oracle integrity), INV-03 (security boundary) and INV-08 (unavailable is not inapplicable), the "required: blocked" mechanism and the unattended "never auto-approve" rule are sound and carried consistently into the compact tier.
- Planning and topology clamping in the helper behave as documented. A request to switch off oracle integrity is refused.

## Reviewer isolation (reported on the WORKFLOW §6 axes)

- **Context shared with me:**
  - a task brief from the launching agent that summarised the owner's ten requirements, listed the package paths and told me what to check;
  - no maker transcript, no private hypotheses, no earlier review scores.
  - The brief told me which research files exist and that research/ holds design records. I read the operational files first and research/ afterwards.
  - I also read the candidate's own self-assessment in research/ (CHANGE_SUMMARY, OPEN_QUESTIONS, ADRs), which includes its persuasive narrative. Some of my findings (R-07 item 3, R-17) coincide with issues the author already acknowledges there.
- **Maker's success claim:** I saw it, in README, CHANGE_SUMMARY and the documents.py success message.
- **Model family:** I share a model family with the author (OPEN_QUESTIONS states the rc1 author and its fresh-context reviewer share a model family; I am a Claude model). Same-family agreement should count as one confirmation, and same-family blind spots are likely to be shared.
- **Could the maker change my inputs or oracle?** Yes. The candidate was being modified while I reviewed it, and the launching agent may be the author. I have recorded the snapshot hash above so that later edits can be detected.
- **How separation was enforced:** it was cooperative only. I had write access to the shared filesystem and kept to the instruction not to modify the packages. No tool or process boundary enforced isolation.

## Overall verdict

**Not fit to freeze now; plausibly fit after fixes.**

Fix before freezing:
- R-01 (missing freeze identity and an unspecified arm);
- R-14 and R-15 (experiment fairness and ablation validity);
- R-16 (validation claims with no recorded evidence);
- the configuration-model defects that let preferences weaken core process or bypass stated controls: R-04, R-05, R-06, R-07, R-11, R-12;
- the undisclosed deletions from Tier 1 (R-02, R-03, R-13).

R-09 and R-10 need wording changes but no structural change. R-17 is a requirement violation the owner should explicitly accept or have fixed.

The underlying design is coherent and keeps the 4.3 invariants intact in substance: numbered invariants, a single truth axis, "required: blocked", the verification dimensions and per-stage participation. The fixes are mostly local. Once they are made, the candidate and contract should be re-checked against a recorded FREEZE.md manifest before any trial.
