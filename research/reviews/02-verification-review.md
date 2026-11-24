I've verified the reconciliation. The freeze is intact: every per-file hash matches. 25 of the 28 findings are fixed; R-02, R-14 and R-17 are partly fixed. I found 10 new defects: 1 major, 6 minor and 3 nits. None is a blocker, and none reaches the 4.3 invariants that were already sound (INV-03, INV-05, INV-08, "required: blocked").

**Commands run** (read-only, with `-I -X utf8 -B`; no `__pycache__` or `.pyc` files created; the per-file manifest re-verified after all runs)
- `tools/documents.py check`: PASSED. Tier 1 is 39,438 of 39,480 bytes; the compact tier is 10,150 bytes; 12 invariant IDs and 14 markers are present.
- `tools/composition.py check`: CONSISTENT.
- FREEZE.md manifest checked with `sha256sum -c`: 50 of 50 OK. No file has been added or changed since FREEZE.md was written.
- Recomputed hashes: the candidate tree (`616f45dd…`), the tested tree (`8905f0c0…`), the contract (`cc526ca5…`), the baseline `SHA256SUMS` (`2059d8b7…`) and the baseline tree (`0ce31aea…`) all match. They match only with the scripts' own sort order (see N-03).
- I rebuilt the five arms into my scratch folder with `build_ablations.py`. All five package hashes match FREEZE.
- I ran `resolve` on 12 adversarial configurations, stored in `C:\Temp\claude\a8cf641ce0f7dfdb\8118a3a1-0dc7-4a5e-a767-cd1de92dbd5b\scratchpad\verify2\cfg\`.

## 1. R-xx verification

| ID | Verdict | Evidence |
|---|---|---|
| R-01 | VERIFIED | FREEZE.md exists, covers the candidate, contract, baseline and every arm, and verifies. The compact subset is gone from the pilot (EXPERIMENT_CONTRACT:78-80), and H7 is moved to the expanded experiment (OPEN_QUESTIONS:61). See N-03 on reproducing the hashes. |
| R-02 | PARTIAL | All 17 listed sentences are present (WORKFLOW:7, 60, 70, 82, 95, 97, 107, 126, 171, 175, 177; SKILL:8; AGENT_INTERACTION:40, 46, 65, 80). But the claims "every 4.3 safeguard kept" (MIGRATION:29) and "every removal listed" are still false; see N-04. |
| R-03 | VERIFIED | WORKFLOW:66 and :60; COMPACT:24 |
| R-04 | VERIFIED | COMPOSITION:112-113 (floor ranked above the contract), :120 (owner override); WORKFLOW:23; COMPACT:19. See N-06. |
| R-05 | VERIFIED | COMPOSITION:186-208; composition.py:172-175; `preset_coupling` control |
| R-06 | VERIFIED | K4:72; composition.py:306; C-11 at COMPOSITION:169; examples 2 and 7. N-01 is the flip side of this fix. |
| R-07 | VERIFIED | C-01..C-06, C-12 and C-13 at COMPOSITION:159-171. The tutoring+propose, unattended+log-off and from-budget cases now resolve to the stricter values. |
| R-08 | VERIFIED | K9:245; OPEN_QUESTIONS:71; ADR-02 |
| R-09 | VERIFIED | WORKFLOW:148, 151, 153; PRACTICAL_PLAYBOOKS:76; COMPACT:48 |
| R-10 | VERIFIED | WORKFLOW:171 and :21 (INV-09); COMPACT:40 |
| R-11 | VERIFIED | K1:29 and :39; AGENT_INTERACTION A8:73; WORKFLOW:126; COMPACT:31 |
| R-12 | VERIFIED | AGENT_INTERACTION A3:40; COMPACT:59 |
| R-13 | VERIFIED | WORKFLOW:199-206 (bias list) and :99 (multi-agent failure clusters) |
| R-14 | PARTIAL | One packaging rule, each arm passes its own check, and the build reproduces. But A3 still leaks its removed component (N-05). The residual patterns are too narrow to catch it. |
| R-15 | VERIFIED | EXPERIMENT_CONTRACT:55, 88, 102-104, 68-72, 115. The 22 tasks and 234 trials re-add correctly. |
| R-16 | VERIFIED | VALIDATION:86-114; the results JSON has 41 records, all passing; its source manifest `8905f0…` matches my recomputation. |
| R-17 | PARTIAL | The author says so too. Compact grew +30.3% and the master +23.0%; both figures check. The stated reason ("every remaining line is an invariant or a 4.3 compact rule", REVIEW_RECONCILIATION:39) is inaccurate: COMPACT:33 (configuration), :41 (nine failure classes replacing 4.3's one-line retry rule) and :50 are new content. |
| R-18 | VERIFIED | documents.py:28 and :142; `core_invariant_deleted_everywhere` control; COMPACT:17 and :19 |
| R-19 | VERIFIED | Every item listed is fixed. Leftover nits are in N-09. |
| R-20 | VERIFIED | WORKFLOW:181-193 |
| R-21 | VERIFIED | composition.py:200 and :254-266. `Assurance: hgih` resolves to high; `oracle_integrity`, `honest_status` and `INV-11` are refused as MandatoryInvariant. |
| R-22 | VERIFIED | K8:237; K9:244; ADR-03 |
| R-23 | VERIFIED | COMPACT:33 and :39 |
| R-24 | VERIFIED | WORKFLOW:23; K3:61; AGENT_INTERACTION:76. See N-07. |
| R-25 | VERIFIED | WORKFLOW:175 |
| R-26 | VERIFIED | run_rc1_checks.py:129-139 and :41; no `__pycache__` |
| R-27 | VERIFIED | composition.py:318-319; K1:45 |
| R-28 | VERIFIED | TRACEABILITY:40 (last column); EVIDENCE_BASE:609 |

## 2. New findings

**N-01 · major · WORKFLOW.md:39, :66; COMPOSITION.md:13, :51, :205; tools/composition.py:306, :320**
- **Problem:** Asking for more assurance on routine work leaves the task on the fast path. The trigger can be `careful-change` (documented as "High assurance regardless of class"), `assurance: high`, or even a typo such as `hgih`. The helper resolves it to `path: fast` together with `independent_review: required`, and prints `NOTICE (none)`. §0 says routine work needs "no … separate reviewer" and ends with "Stop". Since the R-06 fix, "the class alone decides fast-path eligibility".
- **Failure scenario:** A user asks for `careful-change` on a one-line change to a payment config. The agent follows §0, skips the independent verification that High requires, and can report ACCEPTED_FOR_STATED_SCOPE at "assurance high". The user is never told, because no notice is printed.
- **Why it matters:** A stricter request is silently not honoured, and the requested, effective and observed values diverge.
- **Minimal fix:** State that the fast path applies only while effective assurance is Lightweight. In the helper, derive `path=full` whenever effective assurance is above the floor and emit a notice line. Add an example.

**N-02 · minor · COMPACT_PROMPT.md:33; LAUNCH.md:7; GUIDE.md:49 vs COMPOSITION.md:150; examples/CONFIGURATIONS.md:195; composition.py:298-300**
- **Problem:** These three files say any requested-but-unavailable capability keeps "the affected acceptance blocked". K6 blocks only *required* capabilities; other unavailable requests just fall back to a weaker value. Example 6 is a requested parallel topology that the host lacks, which falls back to `single`.
- **Failure scenario:** A compact-tier agent asked for a research brief on a single-session host marks the work READY_FOR_REQUIRED_REVIEW. That counts as a false rejection under H9.
- **Minimal fix:** Write "a *required* check or capability".

**N-03 · minor · FREEZE.md:11 vs run_rc1_checks.py:26 and build_ablations.py:100**
- **Problem:** FREEZE describes the tree hash as SHA-256 over the "sorted lines". Hashing the sorted lines gives `5effaf…`, not the recorded value. The scripts actually sort `Path` objects, which on Windows ignores case. A POSIX host gets a different order and a different hash: `32a942…` for the candidate, `ffd66a…` for A1, `261aa4…` for A2.
- **Failure scenario:** A harness on Linux or macOS cannot reproduce any recorded tree or package hash, and the arms have no per-file manifest to fall back on. An operator would then have to choose between distrusting the freeze and re-freezing.
- **Why it matters:** The freeze is the contract's central integrity mechanism.
- **Minimal fix:** Fix the description in FREEZE.md and give the explicit sort key (`as_posix().lower()`), or add per-file arm manifests. FREEZE.md is outside the tree hash, so this needs no new candidate.

**N-04 · minor · MIGRATION.md:29; CHANGE_SUMMARY.md:23, :50**
- **Problem:** These records claim every 4.3 safeguard and every 4.3 compact line is kept. The following 4.3 text is still missing from Tier 0 and Tier 1:
  - "discard or promote [prototypes] through the applicable checks" and "do not let them silently become the deliverable" (4.3 WORKFLOW:161, COMPACT:41; now only "Label prototypes" at rc1 WORKFLOW:124 and COMPACT:37);
  - A7 "If stopping would leave something broken or exposed, say so" (4.3 AGENT_INTERACTION:86);
  - A1 milestone progress updates and "Do not go silent" (4.3 AGENT_INTERACTION:16). This now lives only in on-demand K3 (COMPOSITION:63), which SKILL:12 does not load by default;
  - A4 "artificial incompleteness" (4.3 AGENT_INTERACTION:54);
  - "Resolving a faulty oracle needs … appropriate independent review" (4.3 WORKFLOW:210), weakened to "reviewed under the assurance level" (WORKFLOW:177).
- **Failure scenario:** A labelled prototype ships as the deliverable without its checks; or a default Tier-1 agent goes silent on a multi-hour task.
- **Minimal fix:** Restore these lines or list them in MIGRATION. Tier 1 has only 42 bytes of headroom, so restoring them means condensing elsewhere.

**N-05 · minor · LAUNCH.md:17 → A3 arm; build_ablations.py:86-87; EXPERIMENT_CONTRACT.md:51**
- **Problem:** LAUNCH.md:17 says "Accept a result only when its mechanism, scope and checks are sound". This line is new in rc1 and survives in A3's LAUNCH.md and MASTER_PROMPT.md, because none of the residual patterns match it. The contract's statement that an ablation "removes every statement that requires its component" is therefore false.
- **Failure scenario:** An A3 agent with file access reads LAUNCH and applies the mechanism and scope checks anyway. The A2-versus-A3 difference on F2 and F3 is biased toward zero.
- **Minimal fix:** Add the edit and a residual pattern, which means a new freeze. Otherwise record it as a known A3 limitation in the deviation log.

**N-06 · minor · COMPOSITION.md:120; OPEN_QUESTIONS.md:85 vs COMPOSITION.md:110; WORKFLOW.md:11**
- **Problem:** The owner override says the agent "complies within INV-01 to INV-05". Read by omission, INV-06 to INV-12 yield to the owner. That contradicts rank 1 ("Never overridden") and the core's statement that the invariants hold under every configuration.
- **Failure scenario:** The owner says "ship it and drop the failed runs from the report". The text can be read as allowing the agent to set aside INV-10.
- **Minimal fix:** "complies within every invariant; the override waives only the check".

**N-07 · minor · AGENT_INTERACTION.md:76 vs COMPOSITION.md:61, :63, :162-163**
- **Problem:** A8 says that in every preset, AI contributions are identifiable from the action record. Yet `action_log: off` is allowed for attended, non-autonomous work: C-04 and C-05 only cover autonomous execution and unattended runs.
- **Failure scenario:** `participation: co-creation` plus `action_log: off` resolves with no warning, and the authorship rule cannot be met.
- **Minimal fix:** Add a compatibility rule for this combination, or state that the host transcript always remains.

**N-08 · nit · LAUNCH.md:19**
- **Problem:** It says the master embeds the glossary. It does not (documents.py:10; MIGRATION:68; GUIDE:33). WORKFLOW:97 and COMPOSITION:19 point to GLOSSARY.md, which a full-tier agent without file access cannot open.
- **Minimal fix:** Remove "glossary" from LAUNCH.md:19.

**N-09 · nit · record and terminology mismatches**
- MIGRATION:29 says "sixteen" sentences were restored; REVIEW_RECONCILIATION:24 says "All 17".
- ADR-04 (ARCHITECTURE_DECISIONS:15) says "ten reason codes"; K6 has 11, and CHANGE_SUMMARY:15 says 11.
- MIGRATION:16 says checkpoint need was folded into the single classification; WORKFLOW:66 says it is decided per action.
- GLOSSARY:41 points the requirement ledger to §9; it is defined in §13 (WORKFLOW:228).
- WORKFLOW:97 and COMPOSITION:19 call scout and analyst "presets"; GLOSSARY:62 maps them to responsibilities.
- The review text the reconciliation answers is not bound by hash anywhere (REVIEW_RECONCILIATION:3).

**N-10 · nit · research/OPEN_QUESTIONS.md:59 vs EXPERIMENT_CONTRACT.md:105**
- **Problem:** H3 claims rc1 costs "no more" than 4.3 on routine tasks, but the gate tolerates up to 1.25× A1.
- **Minimal fix:** Restate H3 to match the gate.

## 3. Verdict

The candidate is fit to remain frozen as an experimental candidate. Its identity verifies exactly, every arm rebuilds to its recorded hash, and the contract is internally consistent. The contract makes no superiority claim and has no blocker.

Do not edit the frozen tree to fix these defects; any edit makes a new candidate. Instead:
- correct the "How to verify" rule in FREEZE.md, which is outside the tree hash (N-03);
- record N-01 and N-05 as known defects and pilot limitations, outside the tree or in the deviation log;
- fix N-01, N-02 and N-04 to N-07 in an rc2 only through a new freeze.

None of these defects is exercised by a pilot family except N-05 (through A3) and N-02 (through compact, which is not in the pilot).

## 4. My isolation

- **Context shared with me:** your brief, the earlier review, and the reconciliation file. No maker transcript.
- **Author's success claims:** yes, I saw them in REVIEW_RECONCILIATION, CHANGE_SUMMARY, VALIDATION and the checkers' success messages.
- **Model family:** very likely the same as the author's and the first reviewer's. My agreement with them should count as one confirmation, and we probably share blind spots.
- **Could the maker change my inputs:** in principle yes, through the shared filesystem. I saw no changes during the run; the manifest still verified at the end.
- **Separation:** cooperative only. No tool or process boundary enforced it.

My scratch files, including the extracted manifest, the rebuilt arms and the test configurations, are in `C:\Temp\claude\a8cf641ce0f7dfdb\8118a3a1-0dc7-4a5e-a767-cd1de92dbd5b\scratchpad\verify2\`.
