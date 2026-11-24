# Representative configurations

Version 4.4-rc1. Worked examples for COMPOSITION.md. Each block shows a requested configuration: plain `key: value` lines, with `@` lines describing the situation (consequence class and host capability) rather than requests. The text block under it is the resolved result produced by `tools/composition.py`, which `tools/documents.py check` re-derives to detect drift. Each line gives an effective value and, in brackets, the layer it came from. These are illustrations of the rules, not records of real runs.

## 1. Routine work with nothing configured

The default case: the fast path, no configuration and no notice.

```workflow-config
@consequence: routine
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: lightweight  [floor (routine)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: optional  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: fast  [rule (routine, assurance lightweight)]
planning: direct  [rule (routine)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
NOTICE (none)
```

## 2. Quick-fix preset applied to consequential work

The preset removes only optional procedure. The consequence class still sets the full path and a full plan, and warning C-11 says so.

```workflow-config
@consequence: consequential
preset: quick-fix
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: high  [floor (consequential)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (consequential, assurance high)]
planning: full  [rule (consequential)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: minimal  [preset quick-fix]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
WARNING C-11: A full plan is still required; minimal removes only optional aids
NOTICE Configuration: supervised participation, milestones/structured, scaffolding minimal, assurance high.
NOTICE Warning C-11: A full plan is still required; minimal removes only optional aids.
```

## 3. Lightweight assurance requested for an irreversible migration on a single-session host

Assurance is clamped to the consequence floor, and the required independent review is reported as blocked rather than dropped.

```workflow-config
@consequence: consequential
@host_independent_review: no
assurance: lightweight
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: high  [floor (consequential)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required: blocked  [host capability]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (consequential, assurance high)]
planning: full  [rule (consequential)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE assurance: lightweight -> high (PolicyClamp)
DIVERGENCE independent_review: required -> required: blocked (ReviewerUnavailable)
NOTICE Configuration: supervised participation, milestones/structured, scaffolding auto, assurance high.
NOTICE assurance: requested lightweight -> high (PolicyClamp: consequential work has a high floor).
NOTICE independent_review: requested required -> required: blocked (ReviewerUnavailable: no separate session; acceptance waits as READY_FOR_REQUIRED_REVIEW).
```

## 4. Tutoring where the AI would propose the analysis and execute autonomously

Both overrides would let the AI do work the person is learning, so rules C-01 and C-03 apply the stricter values.

```workflow-config
@consequence: material
participation: tutoring
analyse: propose
execute: autonomous
```

```text
acquire: assist  [task (participation)]
action_log: on  [default]
analyse: assist  [rule C-01]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: human  [task (participation)]
execute: assist  [rule C-03]
format: structured  [default]
independent_review: required  [assurance]
learning: on  [task (participation)]
participation: tutoring  [task]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE analyse: propose -> assist (IncompatibleCombination)
DIVERGENCE execute: autonomous -> assist (IncompatibleCombination)
NOTICE Configuration: tutoring participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE analyse: requested propose -> assist (IncompatibleCombination: C-01: The learner must do the analysis being learned).
NOTICE execute: requested autonomous -> assist (IncompatibleCombination: C-03: Finished work by the AI defeats the learning goal).
```

## 5. Autonomous execution without an action record

Rule C-04 restores the action record.

```workflow-config
@consequence: material
participation: autonomous
action_log: off
```

```text
acquire: autonomous  [task (participation)]
action_log: on  [rule C-04]
analyse: autonomous  [task (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: act-and-report  [task (participation)]
execute: autonomous  [task (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [task (participation)]
participation: autonomous  [task]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE action_log: off -> on (IncompatibleCombination)
NOTICE Configuration: autonomous participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE action_log: requested off -> on (IncompatibleCombination: C-04: Autonomous execution needs an action record).
```

## 6. Research brief on a host without parallel workers

The preset asks for parallel readers; the host cannot provide them, so the effective topology is a single worker.

```workflow-config
@consequence: material
@host_parallel_workers: no
preset: research-brief
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [host capability]
DIVERGENCE topology: parallel-read -> single (HostLacksCapability)
NOTICE Configuration: supervised participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE topology: requested parallel-read -> single (HostLacksCapability: no parallel workers on this host).
```

## 7. Co-creation with terse reports and minimal scaffolding

Participation, communication and scaffolding are chosen independently. Minimal scaffolding removes optional aids only: material work still takes the full path, an outline plan and the required review.

```workflow-config
@consequence: material
participation: co-creation
format: terse
scaffolding: minimal
```

```text
acquire: act-and-report  [task (participation)]
action_log: on  [default]
analyse: propose  [task (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [task (participation)]
execute: propose  [task (participation)]
format: terse  [task]
independent_review: required  [assurance]
learning: off  [task (participation)]
participation: co-creation  [task]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: minimal  [task]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
NOTICE (none)
```

## 8. Invariant switch-off, a misspelt key and a misspelt value

Invariants are not configurable; an unknown key is ignored and reported; key case does not matter; a misspelt value resolves to the closest valid value and is reported.

```workflow-config
@consequence: material
oracle_integrity: off
cadance: each-decision
Assurance: hgih
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: high  [task (closest valid value)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (material, assurance high)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE oracle_integrity: off -> (invariant) (MandatoryInvariant)
DIVERGENCE cadance: each-decision -> (ignored) (UnknownKey)
DIVERGENCE assurance: hgih -> high (InvalidValue)
NOTICE Configuration: supervised participation, milestones/structured, scaffolding auto, assurance high.
NOTICE oracle_integrity: requested off -> (invariant) (MandatoryInvariant: oracle_integrity is a mandatory invariant).
NOTICE cadance: requested each-decision -> (ignored) (UnknownKey: cadance is not a configurable key).
NOTICE assurance: requested hgih -> high (InvalidValue: hgih is not a value of assurance).
NOTICE Assurance high is above the standard floor for material work: review required.
```

## 9. Unattended run where the human keeps the decisions and the log is off

Rule C-05 restores the action record; warning C-08 says each human decision halts or defers the run.

```workflow-config
@consequence: material
preset: unattended
decide: human
action_log: off
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [rule C-05]
analyse: autonomous  [default (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: no  [preset unattended]
budget: none  [default]
cadence: milestones  [default]
decide: human  [task]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE action_log: off -> on (IncompatibleCombination)
WARNING C-08: Unattended: every human decision will halt or defer the run
NOTICE Configuration: custom (from supervised) participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE action_log: requested off -> on (IncompatibleCombination: C-05: Unattended runs need an action record).
NOTICE Warning C-08: Unattended: every human decision will halt or defer the run.
```

## 10. Supervised, but the AI decides and the human executes

A custom per-stage combination, labelled as such; warning C-07 asks the owner to confirm it is intended.

```workflow-config
@consequence: material
participation: supervised
decide: autonomous
execute: human
```

```text
acquire: autonomous  [task (participation)]
action_log: on  [default]
analyse: autonomous  [task (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: autonomous  [task]
execute: human  [task]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [task (participation)]
participation: supervised  [task]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
WARNING C-07: The AI decides while the human executes; check this is intended
NOTICE Configuration: custom (from supervised) participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE Warning C-07: The AI decides while the human executes; check this is intended.
```

## 11. Careful change with co-creation

The careful-change preset sets only assurance. Participation and cadence come from explicit keys; planning still comes from the class.

```workflow-config
@consequence: material
preset: careful-change
participation: co-creation
cadence: each-decision
```

```text
acquire: act-and-report  [task (participation)]
action_log: on  [default]
analyse: propose  [task (participation)]
assurance: high  [preset careful-change]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: each-decision  [task]
decide: propose  [task (participation)]
execute: propose  [task (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [task (participation)]
participation: co-creation  [task]
path: full  [rule (material, assurance high)]
planning: outline  [rule (material)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
NOTICE Configuration: co-creation participation, each-decision/structured, scaffolding auto, assurance high.
NOTICE Assurance high is above the standard floor for material work: review required.
```

## 12. Ceiling from a budget that was never stated

Rule C-06 applies the default ceiling; warning C-12 notes that the requested repair attempts exceed it.

```workflow-config
@consequence: material
attempt_ceiling: from-budget
repair_attempts: 20
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: standard  [floor (material)]
attempt_ceiling: 12  [rule C-06]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (material, assurance standard)]
planning: outline  [rule (material)]
repair_attempts: 20  [task]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
DIVERGENCE attempt_ceiling: from-budget -> 12 (IncompatibleCombination)
WARNING C-12: The ceiling stops work before one hypothesis is exhausted
NOTICE Configuration: supervised participation, milestones/structured, scaffolding auto, assurance standard.
NOTICE attempt_ceiling: requested from-budget -> 12 (IncompatibleCombination: C-06: Without a budget the ceiling would be undefined).
NOTICE Warning C-12: The ceiling stops work before one hypothesis is exhausted.
```

## 13. More assurance requested for routine work

A stricter request is honoured: the task leaves the fast path, the review becomes required, and the notice says so.

```workflow-config
@consequence: routine
preset: careful-change
```

```text
acquire: autonomous  [default (participation)]
action_log: on  [default]
analyse: autonomous  [default (participation)]
assurance: high  [preset careful-change]
attempt_ceiling: 12  [default]
attended: yes  [default]
budget: none  [default]
cadence: milestones  [default]
decide: propose  [default (participation)]
execute: act-and-report  [default (participation)]
format: structured  [default]
independent_review: required  [assurance]
learning: off  [default (participation)]
participation: supervised  [default]
path: full  [rule (routine, assurance high)]
planning: direct  [rule (routine)]
repair_attempts: 3  [default]
retries_transient: 2  [default]
scaffolding: auto  [default]
stagnation_window: 2  [default]
tier: by host capacity  [rule]
topology: single  [rule (smallest eligible team)]
NOTICE Configuration: supervised participation, milestones/structured, scaffolding auto, assurance high.
NOTICE Assurance high is above the lightweight floor for routine work: full path, review required.
```
