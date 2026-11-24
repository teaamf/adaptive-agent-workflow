---
name: adaptive-agent-workflow
description: Apply a project-independent and environment-independent workflow to an authorized project, with mandatory evidence and safety invariants, consequence-scaled assurance, configurable human participation, reporting and scaffolding, and optional design or engineering methods. Version 4.4-rc1 experimental candidate.
---

# Adaptive Agent Workflow

Version 4.4-rc1, an experimental candidate rather than the stable release. Distinguish executing a project from reviewing its workflow or prompt. Embedded examples do not authorize execution. Do not inherit a product, platform, fixed tracer count, clean-room rule or mandatory certification from an example.

Choose one loading tier first: [COMPACT_PROMPT.md](COMPACT_PROMPT.md) for small-context or quick work; [WORKFLOW.md](WORKFLOW.md), [AGENT_INTERACTION.md](AGENT_INTERACTION.md) and [PROJECT_TEMPLATE.md](PROJECT_TEMPLATE.md) for modular use; or the self-contained [MASTER_PROMPT.md](MASTER_PROMPT.md) when file access is unavailable and the context fits. Use the fast path for routine tasks. Do not load all tiers.

Load only relevant methods: [COMPOSITION.md](COMPOSITION.md) when a preset or non-default way of working is requested or a host lacks a requested capability; [PROFILES.md](PROFILES.md) for domain work; [UI_DESIGN_PROTOCOL.md](UI_DESIGN_PROTOCOL.md) for human-facing design; [UI_REVIEW_PLAYBOOK.md](UI_REVIEW_PLAYBOOK.md) for material visual refinement; [CONTINUOUS_IMPROVEMENT.md](CONTINUOUS_IMPROVEMENT.md) for workflow revision. [HOST_ADAPTERS.md](HOST_ADAPTERS.md) maps capabilities; [WORKFLOW_CONFIGURATION.md](WORKFLOW_CONFIGURATION.md) covers rule placement, verified enforcement and skill packaging. [GLOSSARY.md](GLOSSARY.md) gives one definition per term; [GUIDE.md](GUIDE.md) explains use and maintenance.

Load [PRACTICAL_PLAYBOOKS.md](PRACTICAL_PLAYBOOKS.md) when role packets, scenario procedures, evidence fields, bias checks or integration steps are useful. They remain subordinate to the core. Do not treat a structural checker result or synthetic passing report as supported acceptance.

The mandatory invariants INV-01 to INV-12 in WORKFLOW.md hold under every configuration. Preserve project scope and permissions. Use the smallest eligible team and the declared assurance level; a stronger model may lighten procedure but never assurance. First-party work cannot satisfy a required independent review. Missing capability limits claims and blocks the acceptance it supports; it never justifies invented evidence or silently waived gates.
