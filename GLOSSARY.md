# Architecture and component glossary

Version 4.4-rc1. On-demand reference. Each term has exactly one authoritative definition, named in the last column; other modules refer to it rather than restating it. The categories separate what the workflow is made of from how it is configured, executed, recorded and presented. Most rows name an existing 4.3 concept. Rows new in 4.4-rc1 are the invariant IDs, consequence class as a single classification, participation, cadence and format, scaffolding intensity, compatibility rules, reason codes, isolation axes and the acceptance axis. Terms from other methods are mapped onto these rather than added. The maintenance check confirms that each named section exists, not that it defines the term well.

<!-- table:glossary -->
| Term | Category | Defined in |
|---|---|---|
| Project contract | Entity | WORKFLOW.md §2 |
| Requirement (stable ID) | Entity | WORKFLOW.md §2 |
| Artifact and subject identity | Entity | WORKFLOW.md §9 |
| Bounded task | Entity | WORKFLOW.md §8 |
| Claim | Entity | WORKFLOW.md §9 |
| Finding | Entity | WORKFLOW.md §9 |
| Decision and decision owner | Entity | WORKFLOW.md §9 |
| Coordinator, investigator/planner, maker, verifier, reviewer, specialist, integrator, final assessor | Responsibility | WORKFLOW.md §5 |
| Accountable owner (requester when none is named) | Responsibility | WORKFLOW.md Mandatory invariants |
| Mandatory invariants INV-01 to INV-12 | Invariant | WORKFLOW.md Mandatory invariants |
| Consequence class: routine, material, consequential | Policy | WORKFLOW.md §3 |
| Assurance level: lightweight, standard, high consequence | Policy | WORKFLOW.md §3 |
| Domain profile P1–P7 | Policy | PROFILES.md |
| Human participation and participation preset | Policy | COMPOSITION.md K1 |
| Cadence, format, action log | Policy | COMPOSITION.md K3 |
| Scaffolding intensity | Policy | COMPOSITION.md K4 |
| Planning depth, team topology, resource and stopping limits | Policy | COMPOSITION.md K5 |
| Precedence layers | Policy | COMPOSITION.md K6 |
| Compatibility rules | Policy | COMPOSITION.md K7 |
| Verification dimensions | Policy | WORKFLOW.md §10 |
| Failure classes | Policy | WORKFLOW.md §11 |
| Fast path | Mechanism | WORKFLOW.md §0 |
| Work loop | Mechanism | WORKFLOW.md §7 |
| Task packet | Mechanism | WORKFLOW.md §6 |
| Provisional-work bound | Mechanism | WORKFLOW.md §4 |
| Stagnation, pause triggers and stopping | Mechanism | WORKFLOW.md §11 |
| Retry, stagnation and attempt-ceiling values | Policy | COMPOSITION.md K5 |
| Fresh-context review and isolation axes | Mechanism | WORKFLOW.md §6 |
| Consequential-action checkpoint | Mechanism | AGENT_INTERACTION.md A3 |
| Assurance challenges and negative controls | Mechanism | PRACTICAL_PLAYBOOKS.md O4 |
| Scenario procedures | Mechanism | PRACTICAL_PLAYBOOKS.md O2 |
| Improvement cycle and frozen experiment | Mechanism | CONTINUOUS_IMPROVEMENT.md C2 |
| Progress note and resume routine | Runtime state | AGENT_INTERACTION.md A4 |
| Minimum durable state | Runtime state | WORKFLOW.md §9 |
| Requirement ledger | Runtime state | WORKFLOW.md §13 |
| Effective configuration | Runtime state | COMPOSITION.md K6 |
| Evidence record (subject and oracle identity) | Evidence | WORKFLOW.md §9 |
| Truth state and the five other claim axes, including acceptance | Evidence | WORKFLOW.md §9 |
| Task, host-capability, event, review, finding and configuration records | Evidence | PRACTICAL_PLAYBOOKS.md O3 |
| Observed configuration and reason codes | Evidence | COMPOSITION.md K6 |
| Delivery status | Derived view | WORKFLOW.md §12 |
| Report buckets: done and checked, done not checked, not done, blocked | Derived view | AGENT_INTERACTION.md A1 |
| Configuration notice | Derived view | COMPOSITION.md K6 |
| Workflow presets | Preset | COMPOSITION.md K8 |
| Participation presets | Preset | COMPOSITION.md K1 |
| Loading tiers: compact, modular, full | Adapter | HOST_ADAPTERS.md |
| Host capability map | Adapter | HOST_ADAPTERS.md |
| Enforcement labels and standing-rule placement | Adapter | WORKFLOW_CONFIGURATION.md F2 |
| Skill discovery metadata | Adapter | SKILL.md |
<!-- end -->

## Terms from other methods

| Term elsewhere | Maps to |
|---|---|
| Scout, analyst | Investigator/planner responsibility with a discovery task |
| Triage, validator | Verifier establishing a finding's truth state |
| Impact assessor | Reviewer or specialist setting the consequence axis |
| Repairer, patch generator | Maker with a remediation task |
| Critic, red team | Reviewer or adversarial evaluator (PRACTICAL_PLAYBOOKS.md O1) |
| Tutor, pair, co-author | Participation presets, not responsibilities |
| Autonomy level | Per-stage participation level |
| Agent team, swarm | A topology choice over the same responsibilities |

## Category meanings

- **Entity and responsibility:** what the work is about and who is accountable for each function.
- **Invariant:** a mandatory rule that no configuration relaxes.
- **Policy:** a choice that is configured or classified per task.
- **Mechanism:** a procedure that carries out policies.
- **Runtime state:** what is true about the work now.
- **Evidence:** observations and the records that bind them to subjects.
- **Derived view:** a presentation computed from state and evidence; it never holds facts of its own.
- **Preset:** a named bundle of policy values.
- **Adapter:** how the workflow maps to a host, a tier or a packaging format.

“Profile” now always means a domain profile. The 4.3 term *assurance profile* is *assurance level*; *accessibility profile* is *accessibility target*; *named profile* survives only in the status CERTIFIED_UNDER_NAMED_PROFILE (MIGRATION.md).
