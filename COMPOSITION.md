# Workflow composition

Version 4.4-rc2. On-demand module. Load it when someone asks for a non-default way of working, names a preset, when a host cannot provide a requested capability, or when adopting the package. **Most tasks configure nothing:** routine work uses the defaults and produces no configuration notice (WORKFLOW §0).

This module defines the configurable policies once. It does not define the mandatory invariants (WORKFLOW INV-01 to INV-12), the assurance levels (WORKFLOW §3), the domain profiles (PROFILES.md) or the loading tiers (HOST_ADAPTERS.md). Every setting can be followed as a plain-language instruction. The tables are also read by the optional `tools/composition.py` helper, which checks consistency and resolves examples but enforces nothing at run time (K9).

## K0. What can and cannot be configured

| Category | Configurable? |
|---|---|
| Mandatory invariants INV-01 to INV-12 | Never relaxed; any layer may add stricter rules |
| Assurance level (Lightweight, Standard, High consequence) | Raised only; the floor comes from the consequence class (K6) |
| Fast path (WORKFLOW §0) | Never chosen by preference: routine work at Lightweight assurance only; a request for more assurance takes the full path |
| Domain profiles P1–P7 | Selected by what the work is, not by preference |
| Loading tier | Chosen by host capacity (HOST_ADAPTERS.md) |
| Participation, cadence and format, scaffolding, planning depth, team topology, resources and stopping | Yes, within the layers above |
| Runtime state, evidence and derived views (progress note, evidence, delivery status, notice) | Recorded, not configured |

Named roles from other methods (scout, analyst, critic, tutor) map onto the responsibilities in WORKFLOW §5; they are not new components (GLOSSARY.md).

## K1. Human participation

Participation is set per stage of the work: acquiring information, analysing it, deciding, and executing. Each stage takes one level:

| Level | Meaning |
|---|---|
| human | The human performs this stage; the AI acts only when asked |
| assist | The AI helps on request with parts of the stage |
| propose | The AI prepares the work or options; the human chooses or approves. At the decide stage this covers consequential decisions and decisions the human owns; routine choices follow AGENT_INTERACTION A2 |
| act-and-report | The AI acts and reports; the human can veto or undo |
| autonomous | The AI acts within the contract's bounds; reporting follows cadence (K3) |

A participation preset sets all four stages and the learning objective; individual stages can then be overridden.

<!-- table:participation -->
| Preset | acquire | analyse | decide | execute | learning | Intended use |
|---|---|---|---|---|---|---|
| autonomous | autonomous | autonomous | act-and-report | autonomous | off | Delegated work the human reviews at acceptance |
| supervised | autonomous | autonomous | propose | act-and-report | off | Default: the AI works end to end; the human approves consequential decisions |
| co-creation | act-and-report | propose | propose | propose | off | Shared authorship; the AI offers options, the human chooses |
| tutoring | assist | assist | human | assist | on | The person is learning; the AI gives hints and checks, not finished answers |
| human-led | assist | assist | human | human | off | The human does the work; the AI assists on request |
<!-- end -->

Participation never changes the assurance level, the consequence gates or the acceptance criteria. Late-stage autonomy is reported to help routine performance while making failures harder to notice and recover from, so higher levels carry compensating controls rather than bans: an action record, reversible steps where possible, and a gate at consequence boundaries (AGENT_INTERACTION A3). The authorship rules in AGENT_INTERACTION A8 hold in every preset. With learning on, the agent protects the stated learning goal: hints, questions and checks on the parts being learned; finished answers only when asked, and then labelled.

`attended: no` declares that no human is available during the run. A gated decision or action then halts or is deferred and logged; it is never auto-approved (AGENT_INTERACTION A3).

## K2. Existing dimensions reused, not duplicated

- **Assurance.** `assurance` may be requested as `auto`, `lightweight`, `standard` or `high`. The effective value is the stricter of the request and the class floor (WORKFLOW §3); a lower request is clamped and reported (K6). Verification follows WORKFLOW §10.
- **Domain method.** Domain profiles combine freely (PROFILES.md). They add methods; they do not set cadence, topology or participation.
- **Context loading.** `tier` is `auto`, `compact`, `modular` or `full`; `auto` chooses by host capacity. A tier adds detail, never authority.

## K3. Communication cadence and format

| Key | Values | Default | Meaning |
|---|---|---|---|
| cadence | on-demand, milestones, each-decision | milestones | How often the agent reports unprompted |
| format | terse, structured, trace | structured | Outcome only; outcome, evidence and limits (A1); or a step-by-step account |
| action_log | on, off | on | Whether a record of actions is kept: the host transcript, or one line per external, irreversible or gated action. Routine attended work needs nothing beyond the host transcript |

These are preferences about communication, independent of participation: an autonomous run can report at each decision, and a human-led session can stay terse. Whatever the setting, decisions needed, blockers and failures are reported promptly, and nothing goes silent for long on long work. A preference changes how often and how much is said, never what is true, which gates apply, or the separation of checked and unchecked work (INV-10). The action record is also the source for identifying AI contributions (AGENT_INTERACTION A8).

## K4. Scaffolding intensity

Scaffolding is optional procedural support: explicit plans beyond the class minimum, checklists, worked techniques, extra self-review passes and structured templates. It is a policy, not a measure of model quality. Assurance and the core steps for the task's class are not scaffolding and are never reduced by this setting (INV-07). The fast path is set by the consequence class and assurance level, never by scaffolding.

| Value | Behaviour |
|---|---|
| auto (default) | Choose from the inputs below and record the reason when it matters |
| minimal | No optional checklists, templates or extra self-review passes; all core steps for the task's class still apply |
| standard | The core protocol as written |
| guided | Add explicit plans, checklists and step templates for the task class |

Selection inputs for `auto`:

1. **Task structure:** sequential and tightly coupled work favours a single worker with an explicit plan; breadth-first work tolerates parallel readers.
2. **Demonstrated capability** of this worker on this task class. Model identity is only a starting hypothesis.
3. **Observed progress:** stagnation or repeated incorrect hypotheses justify more structure (WORKFLOW §11).
4. **Uncertainty:** unclear requirements favour a short outline and an early question.
5. **Consequence:** high consequence raises assurance; it need not raise procedure.
6. **Resources:** remaining budget bounds how much structure is affordable.

Escalate scaffolding within a task when progress stalls. Reduce it between tasks only on recorded evidence that the lighter procedure does as well on that task class; never automatically mid-task. Approval gates and assurance are never de-escalated this way.

## K5. Planning, topology, resources and stopping

This table holds the authoritative numeric defaults; WORKFLOW §11 quotes them.

| Key | Values | Default | Rule |
|---|---|---|---|
| planning | auto, direct, outline, full | auto | `auto` follows WORKFLOW §7. A requested lighter plan applies only where that rule allows it |
| topology | auto, single, parallel-read, parallel-write | auto | `auto` is the smallest eligible team (WORKFLOW §5). Parallel workers need a recorded rationale; parallel writers need separate workspaces and a single integrator, and are clamped to `single` for tightly coupled artifacts |
| retries_transient | integer | 2 | Retries of a suspected transient condition |
| repair_attempts | integer | 3 | Attempts against one hypothesis |
| stagnation_window | integer | 2 | Attempts without new evidence before changing strategy |
| attempt_ceiling | integer or from-budget | 12 | Total attempts on one problem across hypotheses; `from-budget` needs a stated budget |
| budget | text | none | Tokens, time, tool calls or cost; required for long or costly runs |

Numeric defaults are configurable hypotheses, not established constants.

## K6. Precedence, requested, effective and observed

Layers, highest first. A lower layer may always choose a stricter value.

<!-- table:precedence -->
| Rank | Layer | Effect |
|---|---|---|
| 1 | Mandatory invariants | Never overridden |
| 2 | Actual permissions and host capability | Bound what is effective; cannot be granted by a lower layer |
| 3 | Assurance floor from the consequence class | No layer lowers effective assurance below it; never lowered for a stronger model |
| 4 | Adopted project contract and gates | May add gates or raise assurance; changed only by its owner with a recorded reason |
| 5 | Explicit task instruction | Sets any configurable policy within ranks 1–4 |
| 6 | Standing project or user preferences | Same, below the task instruction |
| 7 | Preset values | Same, below explicit preferences |
| 8 | Documented defaults | Written out in the effective configuration |
<!-- end -->

**Owner override.** The accountable owner (named in the contract, otherwise the requester) may stop the work, narrow it, or direct delivery without a required check. The agent complies within every invariant (the override waives only the check), records the instruction, and caps the status at DELIVERED_WITH_GAPS or READY_FOR_REQUIRED_REVIEW, never ACCEPTED_FOR_STATED_SCOPE. Reclassifying the consequence class needs a recorded reason before the candidate is judged, never after a failed or unavailable check (INV-07).

Merge rules: a value replaces the one below it; a lower layer may add gates but never remove one; `off` can remove an optional feature but never a consequence gate; key names are matched without regard to case; an unknown key is ignored and reported (UnknownKey); an invalid value for a known key resolves to the closest valid value when unambiguous, else the default, and for assurance and planning to the stricter of that and the floor, and is reported (InvalidValue); a request that conflicts with ranks 1–4 resolves to the stricter value and is reported.

**Requested** is what the user or project asked for, recorded sparsely and verbatim. **Effective** is the resolved value of every key with its source layer. **Observed** is what actually happened. A material divergence between any two is recorded with a reason code:

<!-- table:reasons -->
| Code | Meaning |
|---|---|
| PolicyClamp | A request conflicted with the assurance floor, the contract or a clamping rule and the stricter value applies |
| MandatoryInvariant | A request tried to relax an invariant and was refused |
| HostLacksCapability | The host cannot provide the requested capability |
| ReviewerUnavailable | A required independent review cannot be obtained; acceptance is blocked, not waived |
| PermissionMissing | The action needs an authorization that has not been given |
| IncompatibleCombination | A compatibility rule (K7) rejected or adjusted the combination |
| UnknownKey | The key is not defined here and was ignored |
| InvalidValue | The value is not one of the key's values; the resolved value is reported |
| BudgetExhausted | Work stopped at the resource ceiling |
| StagnationStop | Work stopped or changed strategy because attempts produced no new evidence |
| UserInstruction | The person changed the configuration during the run |
<!-- end -->

**Notice.** At task start, show a notice of at most five lines when requested and effective differ materially, a warning applies, or the task is consequential. Routine work with no divergence or warning shows none. Example:

```text
Configuration: supervised participation, milestones/structured, scaffolding auto.
Requested assurance lightweight → effective high consequence (PolicyClamp: irreversible migration).
Requested independent review → required: blocked (ReviewerUnavailable: no separate session on this host).
```

A required but unavailable capability appears as **required: blocked**. It drives READY_FOR_REQUIRED_REVIEW or DELIVERED_WITH_GAPS and never becomes optional or not applicable (INV-08). Observed divergences, such as a skipped planned check or a mid-run change of preset, go in the delivery report with their reason codes.

## K7. Compatibility rules

Errors make a combination invalid; the stricter alternative applies and the divergence is reported. Warnings are reported and allowed.

<!-- table:compatibility -->
| ID | Severity | Condition | Reason |
|---|---|---|---|
| C-01 | error | learning=on & analyse in {propose, act-and-report, autonomous} | The learner must do the analysis being learned |
| C-02 | error | learning=on & decide in {propose, act-and-report, autonomous} | The learner must own the decisions being learned |
| C-03 | error | learning=on & execute in {propose, act-and-report, autonomous} | Finished work by the AI defeats the learning goal |
| C-04 | error | execute=autonomous & action_log=off | Autonomous execution needs an action record |
| C-05 | error | attended=no & action_log=off | Unattended runs need an action record |
| C-06 | error | attempt_ceiling=from-budget & budget=none | Without a budget the ceiling would be undefined |
| C-07 | warn | decide in {act-and-report, autonomous} & execute in {human, assist} | The AI decides while the human executes; check this is intended |
| C-08 | warn | attended=no & decide in {human, propose} | Unattended: every human decision will halt or defer the run |
| C-09 | warn | acquire=propose & analyse=propose & decide=propose & execute=propose & cadence=each-decision | Approval at every stage invites approval without reading |
| C-10 | warn | topology=parallel-write | Parallel writers need separate workspaces, a single integrator and a recorded rationale |
| C-11 | warn | planning=full & scaffolding=minimal | A full plan is still required; minimal removes only optional aids |
| C-12 | warn | repair_attempts > attempt_ceiling | The ceiling stops work before one hypothesis is exhausted |
| C-13 | warn | retries_transient > attempt_ceiling | The ceiling stops work before transient retries are exhausted |
| C-14 | warn | action_log=off | AI contributions are then identifiable only from the host transcript (AGENT_INTERACTION A8) |
<!-- end -->

The rules are deliberately few. Add one only for a demonstrated incoherent or unsafe combination.

## K8. Configuration blocks and workflow presets

A configuration is a short block of `key: value` lines. It works as plain text for a person or model; a helper can also read it. Only keys that differ from the defaults are needed.

```workflow-config
preset: careful-change
participation: co-creation
cadence: each-decision
```

Each workflow preset sets keys from one dimension only, so choosing one never changes another dimension; combine presets with explicit keys. Participation presets are in K1.

<!-- table:dimensions -->
| Dimension | Keys |
|---|---|
| participation | participation, acquire, analyse, decide, execute, learning, attended |
| communication | cadence, format, action_log |
| procedure | scaffolding, planning |
| topology | topology |
| assurance | assurance |
| resources | retries_transient, repair_attempts, stagnation_window, attempt_ceiling, budget |
| loading | tier |
<!-- end -->

<!-- table:presets -->
| Preset | Values | Use |
|---|---|---|
| quick-fix | scaffolding=minimal | No optional procedure; the class still sets the path |
| standard-change | (defaults) | Most material work |
| careful-change | assurance=high | High assurance regardless of class |
| research-brief | topology=parallel-read | Breadth-first reading and synthesis |
| unattended | attended=no | Runs with nobody available to approve |
<!-- end -->

Defaults for every key:

<!-- table:defaults -->
| Key | Values | Default |
|---|---|---|
| participation | autonomous, supervised, co-creation, tutoring, human-led | supervised |
| acquire | human, assist, propose, act-and-report, autonomous | from participation |
| analyse | human, assist, propose, act-and-report, autonomous | from participation |
| decide | human, assist, propose, act-and-report, autonomous | from participation |
| execute | human, assist, propose, act-and-report, autonomous | from participation |
| learning | off, on | from participation |
| attended | yes, no | yes |
| cadence | on-demand, milestones, each-decision | milestones |
| format | terse, structured, trace | structured |
| action_log | on, off | on |
| scaffolding | auto, minimal, standard, guided | auto |
| planning | auto, direct, outline, full | auto |
| topology | auto, single, parallel-read, parallel-write | auto |
| assurance | auto, lightweight, standard, high | auto |
| tier | auto, compact, modular, full | auto |
| retries_transient | integer | 2 |
| repair_attempts | integer | 3 |
| stagnation_window | integer | 2 |
| attempt_ceiling | integer, from-budget | 12 |
| budget | text | none |
<!-- end -->

Resolution follows K6 from the bottom up: documented defaults (8); preset values (7), the workflow preset and then any participation preset it names; standing preferences (6); the explicit task instruction (5), a named participation preset first, then stage keys, then other keys; then the bounds of ranks 1–4 (contract, assurance floor, permissions and host capability, invariants) and the compatibility rules of K7. Example configurations with their resolved results are in `examples/CONFIGURATIONS.md`.

## K9. What is enforced and what is instruction

| Element | Status |
|---|---|
| Table consistency: presets use defined keys and values, each workflow preset sets one dimension, every preset passes K7, defaults are complete, WORKFLOW §11 quotes the K5 defaults | Mechanical (advisory): `tools/composition.py check`, run by `tools/documents.py check` |
| Resolution of an example block into effective values, divergences and reason codes | Mechanical (advisory): `tools/composition.py resolve`. Models ranks 1, 3, 5, 7 and 8 and host capability; does not model the contract's own settings, standing preferences or permissions (PermissionMissing is never produced) |
| Resolver independence: changing participation, cadence, format or scaffolding alone changes only its own keys | Mechanical (advisory) about the helper's resolver only; says nothing about how an agent interprets the settings |
| The agent actually behaving as configured during a run | Instruction only; observed behaviour is reported, not enforced |
| Mandatory invariants | Instruction, plus whatever the host enforces (WORKFLOW_CONFIGURATION F2) |

The helper is optional. Without it, a person applies this module by reading it.
