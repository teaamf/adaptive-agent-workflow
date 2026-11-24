# Adaptive Agent Workflow

**A reusable workflow for agent-assisted work that does not depend on the project, model or environment.** Version 4.4-rc1, 18 November 2026.

> **Experimental candidate.** 4.4-rc1 is a candidate successor to 4.3 prepared for comparative evaluation. It is not the stable release and no superiority over 4.3 has been shown. [MIGRATION.md](MIGRATION.md) lists what changed; the frozen comparison plan is in `research/EXPERIMENT_CONTRACT.md`.

Use it with your own project requirements. It prescribes no product, UI, programming language, operating system, editor, model family, model provider, agent framework or repository host. It adapts responsibilities, evidence and assurance to the actual task and to the capabilities actually available. No software or agent service is installed by this package.

## Pick a loading tier

Choose by the model's context size and tool access, not by its brand ([details](HOST_ADAPTERS.md)):

| Tier | Give the agent | Best for |
|---|---|---|
| 0 Compact | [COMPACT_PROMPT.md](COMPACT_PROMPT.md) (small; 10,500-byte maintenance ceiling) | Small-context or smaller models; quick tasks; per-turn instruction files |
| 1 Modular | [WORKFLOW.md](WORKFLOW.md) + [AGENT_INTERACTION.md](AGENT_INTERACTION.md) + [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md), then selected modules on demand | Agents that can read files |
| 2 Full | [MASTER_PROMPT.md](MASTER_PROMPT.md) (fully expanded) | Large-context models without file access |

All tiers share the same core rules. Load only one tier at a time. Tokenize for the receiving model when possible; the maintenance helper checks byte size, not a universal token limit.

## Reuse across projects

Treat this folder as read-only, shared guidance. Put everything specific to one project in that project's own contract (from [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md)) and its own instruction files, never in these modules. Then:

- one copy can serve many projects;
- updating the workflow never overwrites project facts;
- no project's assumptions leak into another.

To point a host at the workflow, add one line to the project's agent instruction file, in whatever form the host uses. Alternatively, paste the chosen tier into the conversation along with your request. [GUIDE.md](GUIDE.md) has a launch template.

Nothing needs configuring for ordinary work. To ask for a different way of working, such as co-creation, tutoring, terse reports or an unattended run, name a preset or a few keys from [COMPOSITION.md](COMPOSITION.md); [examples/CONFIGURATIONS.md](examples/CONFIGURATIONS.md) shows how requests resolve. Mandatory invariants and the assurance floor cannot be configured away.

[WORKFLOW_CONFIGURATION.md](WORKFLOW_CONFIGURATION.md) gives a short standing-rule example and separates on-demand procedures, verified checks and host adapters. For material UI work, [UI_REVIEW_PLAYBOOK.md](UI_REVIEW_PLAYBOOK.md) adds a bounded capture, critique, repair and recovery loop. These procedures load when relevant; a small task retains the fast path.

## Contents

- [GUIDE.md](GUIDE.md) — start here: adoption, launch and adaptation examples.
- [COMPACT_PROMPT.md](COMPACT_PROMPT.md) — standalone compact tier.
- [MASTER_PROMPT.md](MASTER_PROMPT.md) — self-contained full tier, assembled from the modules below.
- [WORKFLOW.md](WORKFLOW.md) — mandatory invariants and core coordination, evidence and verification rules, including the §0 fast path.
- [AGENT_INTERACTION.md](AGENT_INTERACTION.md) — how the agent reports, asks, checkpoints, resumes, calibrates trust and communicates failure.
- [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md) — per-project requirements, permissions, gates and capability tier.
- [COMPOSITION.md](COMPOSITION.md) — configurable policies, presets, precedence, compatibility rules and requested/effective/observed configuration.
- [GLOSSARY.md](GLOSSARY.md) — one authoritative definition per term, by component category.
- [examples/CONFIGURATIONS.md](examples/CONFIGURATIONS.md) — representative presets and custom configurations with resolved results.
- [MIGRATION.md](MIGRATION.md) — moving from 4.3 to 4.4-rc1.
- [PROFILES.md](PROFILES.md) — optional domain profiles: software, UI, data, research, document and operations methods.
- [UI_DESIGN_PROTOCOL.md](UI_DESIGN_PROTOCOL.md) — UI, accessibility and AI-feature guidance, selected only when relevant.
- [UI_REVIEW_PLAYBOOK.md](UI_REVIEW_PLAYBOOK.md) — readiness, visual-review findings, bounded refinement and recovery.
- [HOST_ADAPTERS.md](HOST_ADAPTERS.md) — loading tiers, model capability adaptation, workers and sessions.
- [WORKFLOW_CONFIGURATION.md](WORKFLOW_CONFIGURATION.md) — rule placement, effective enforcement and portable packaging.
- [CONTINUOUS_IMPROVEMENT.md](CONTINUOUS_IMPROVEMENT.md) — bounded research and evaluation of workflow revisions.
- [PRACTICAL_PLAYBOOKS.md](PRACTICAL_PLAYBOOKS.md) — optional role handoffs, scenario procedures, record fields and integration steps.
- [references/ENGINEERING_ADVICE_MAP.md](references/ENGINEERING_ADVICE_MAP.md) and [references/ADVICE_REGISTER.md](references/ADVICE_REGISTER.md) — the source-advice mappings cited by bracketed IDs.
- [evaluation/SCENARIOS.md](evaluation/SCENARIOS.md) — public cases for trying the workflow on a new model or host.
- [RESEARCH_AND_CHANGES.md](RESEARCH_AND_CHANGES.md), [MERGE_DECISIONS.md](MERGE_DECISIONS.md), [VALIDATION.md](VALIDATION.md) — provenance, history and the limits of what was checked. The `research/` folder holds the 4.4-rc1 traceability matrix, decision records, experiment contract and change summary.

The optional [SKILL.md](SKILL.md) is an adapter for hosts that discover skills by folder. When deploying it in the open skill format, name the containing package folder `adaptive-agent-workflow` to match its metadata and keep its relative resources together. The checkout can retain its current name. Other hosts use the tiers directly. Collaboration services, CI and trackers can be added through the optional integration contract in the playbooks. The research folder and provenance records describe the package's history; they are not instructions.

## Maintenance

Edit LAUNCH.md and the canonical modules, never the master directly. Then reassemble the master and run the checks. The optional helper uses only the Python standard library:

```text
python tools/documents.py assemble
python tools/documents.py check
```

The check confirms that:

- the master matches the modules;
- the invariant set is exactly INV-01 to INV-12, and the compact tier stays within its 10,500-byte budget and carries every ID;
- the Tier 1 core (WORKFLOW, AGENT_INTERACTION, PROJECT_TEMPLATE) stays within its 39,480-byte ceiling;
- every operational module declares the package version;
- the composition tables are consistent, each workflow preset sets one dimension, WORKFLOW §11 quotes the K5 defaults, and the recorded examples re-derive;
- every glossary entry resolves to an existing section;
- local links resolve;
- no operational file matches a pattern in [tools/portability_patterns.txt](tools/portability_patterns.txt) (project names, vendor or model names, machine paths).

Add your own product, client or host names to that file so they cannot leak in.

Without Python, maintain the package by hand:

1. Build the master as LAUNCH.md followed by each module in the order listed in `tools/documents.py`. Wrap each module in `<!-- BEGIN name -->` and `<!-- END name -->` markers, and separate the parts with `---`.
2. Update COMPACT_PROMPT.md whenever a core rule changes, keeping every INV-xx ID.
3. Search the operational files for the guard patterns.

Using the workflow never requires Python or any other tool.
