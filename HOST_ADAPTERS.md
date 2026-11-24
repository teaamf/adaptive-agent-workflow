# Environment adaptation

Version 4.4-rc2. No particular editor, model, agent framework, shell, operating system, repository host or cloud service is required. This is a capability contract, not a claim that every available environment has been tested or can execute every project.

## Choose a loading tier by capacity, not brand

| Tier | Load | Use when |
|---|---|---|
| 0 Compact | COMPACT_PROMPT.md only (small; 10,500-byte maintenance ceiling) | Small context window; weaker long-instruction following; quick tasks; or a per-turn instruction budget |
| 1 Modular | WORKFLOW.md + AGENT_INTERACTION.md + PROJECT_TEMPLATE.md, then only the selected modules | Moderate context; file access, so modules can be read on demand |
| 2 Full | MASTER_PROMPT.md (fully expanded; measure for the receiving model) | Large context and no file access, where everything must be supplied at once |

Estimate the size against the model's actual context window, leaving room for the project's own inputs and working memory. As a rule of thumb, instructions should take a small fraction of the context. Never load two tiers together. Never truncate a tier silently: if even the compact tier does not fit, report the gap. A higher tier adds method detail, not authority. All three carry the mandatory invariants INV-01 to INV-12; the maintenance check confirms each ID is present in every tier, not that the wording is equivalent.

The maintenance helper checks bytes, not model tokens. Token counts depend on the receiving tokenizer. For standing-rule placement, progressive disclosure, effective enforcement and skill packaging use [WORKFLOW_CONFIGURATION.md](WORKFLOW_CONFIGURATION.md); load it during adoption or configuration changes, rather than on every task.

## Adapt to the model's capabilities

The protocol depends on no model family, vendor, reasoning mode, tool-call syntax, output schema or special feature. Observe what the model can actually do, and adapt:

| Capability | If present | If absent |
|---|---|---|
| Tool use / execution | Inspect and verify by running | Text-only mode: work from supplied material and state what could not be verified |
| Long context | Higher loading tier | Compact tier; durable notes; smaller task packets |
| Reliable structured output | Machine-readable records | Short plain-text records with the same fields |
| Separate sessions or workers | Independent review in a fresh context | Sequential manual sessions, or blocked independent acceptance; never role-play independence |
| Extended reasoning | May help planning | Not required; use explicit written plans and checks instead |

Observed capability on the task class is also the starting point for scaffolding intensity (COMPOSITION.md K4): a worker that demonstrably handles the class well may receive less procedure. It never receives less assurance (INV-07). Different model versions and vendors behave differently on the same prompt. When the model or host changes, treat earlier behavioral assumptions as unverified. Rerun a few relevant evaluation/SCENARIOS.md cases before relying on the workflow for consequential work. Different model names do not by themselves establish independent review.

## Map capabilities rather than brands

| Function | Meaning | Possible implementation |
|---|---|---|
| Inspect | Read relevant inputs and current state | File tools, APIs, supplied text or human-provided export |
| Produce | Make the authorized artifact/change | Editor, shell, authoring application or text response |
| Observe | Check the actual outcome | Tests, calculations, rendering, runtime interaction, source inspection |
| Dispatch | Give a bounded task to an eligible worker | Native worker or manual fresh session |
| Collect | Obtain findings and inspect referenced artifacts | Files, immutable report or verified API result |
| Cancel/checkpoint | Stop work and preserve side effects/state | Host interruption and durable handoff |
| Isolate | Separate context and write access | Restricted tools/workspaces, processes or honestly labelled cooperative boundaries |
| Accept | Apply the project gates to the exact result | Existing review system or coordinator-managed record |

Discover actual tools and their semantics before use. Use current official host documentation for uncertain mappings; do not guess command names, subagent limits or sandbox properties. Installations, paid services or external integration are not prerequisites unless the actual project makes them necessary and authorizes them.

## Native, sequential and single-context modes

Use native independent workers for parallel-ready tasks when available and authorized. Keep write ownership and integration explicit. Without native workers, manual fresh sessions can perform independent roles sequentially using frozen packets. In a single context, make authorized first-party progress and apply the selected assurance rules; do not simulate independence with role-play. A text-only environment can complete eligible text work but cannot make unsupported execution claims.

No fixed number of workers is required. A requested capability the host lacks is recorded as a divergence between requested and effective configuration with a reason code such as HostLacksCapability or ReviewerUnavailable (COMPOSITION.md K6); a required one stays required and blocked. If one environment cannot satisfy a gate, report the missing capability and hand off that bounded work to an eligible environment when available. Transferring work does not authorize exporting private data to a new service.

## Task packet

A text layout for the task-packet fields defined in WORKFLOW §6, plus identifiers and isolation:

```text
mission/task/worker identifiers, workflow and contract revision
role, concrete objective, relevant requirement/gate IDs
input/baseline/candidate identity and factual evidence
authorized artifact/workspace and allowed actions
actual context/write isolation and excluded persuasive inputs
expected output: result, observations, findings, evidence and limits
budget, stopping condition, effective configuration where it differs from defaults, and next dependency
team rationale when more than one worker is used
```

Load only relevant modules and requirements, with a completeness index held by the coordinator. Many hosts support the same progressive-disclosure pattern natively, in different forms:

- **Project instruction files.** For example, the cross-vendor AGENTS.md format or a host-specific equivalent.
- **Skill or plugin folders.** A short description is always loaded; the full instructions load only when needed.
- **Standardized tool connections.** For example, the Model Context Protocol.

These are examples, not requirements. Use whatever the host provides. Respect existing instruction files. Keep additions short, because they are loaded on every run. Each environment's actual loading rules decide what the agent sees; check them rather than assuming. The optional SKILL.md in this package is one such adapter. Where a host uses a different discovery format, a pointer to COMPACT_PROMPT.md or WORKFLOW.md works equally well. If input limits prevent consuming the master prompt, use modular files and a durable contract; never silently truncate scope. If neither file access nor adequate context is available, report that capability gap.

## Optional repository and service integration

Local artifact/task/evidence identities do not depend on a remote account. GitHub or another tracker can later carry issues, reviews, CI output and links when requested. Reconcile existing configuration and bind remote results to exact versions. Without Git, use an appropriate snapshot/version identifier. Without durable filesystem access, export a factual handoff through an authorized channel.

Remote approval, a CI badge and publication authorization are separate facts. No service connection can replace the project's required evidence. Preserve privacy, provenance and permissions across host transitions.
