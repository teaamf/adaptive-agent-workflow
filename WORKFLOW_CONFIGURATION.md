# Configure the workflow without coupling it to a host

Version 4.4-rc1. Use when adopting the package, maintaining shared instructions or turning repeated guidance into a reliable check. Ordinary tasks use the existing configuration. This procedure installs nothing and grants no permissions.

## F1. Separate standing rules from procedures

Keep one authoritative source for each rule. Place it according to when it is needed:

| Layer | Belongs here | Loading and verification |
|---|---|---|
| Standing instructions | Short invariants, project vocabulary, authoritative paths and routing | Loaded where the host actually supports it; verify effective scope and precedence |
| On-demand procedure | Trigger, inputs, steps, evidence, failure handling and stop condition | Read only for the relevant task; a file, skill or supplied excerpt can serve this function |
| Mechanical checks | Properties a tool can actually decide | Existing validator, test, schema, compiler or review gate; record where it runs and whether failure blocks acceptance |
| Capability adapters | Concrete tool commands, permissions, versions and integration details | Project/host configuration; keep provider and machine details outside shared operational guidance |

These are responsibilities, not four mandatory files. Keep loading tiers distinct: standing instructions point to one tier; they do not duplicate it or require loading all optional modules. A short host instruction might say:

> Use the project's current requirements and permissions; the workflow's mandatory invariants always apply. For small reversible work, inspect, change, check and report. For material work, establish acceptance and assurance first. Tie claims to actual outcomes on the delivered version; never weaken a check to pass. Preserve user work. Load the selected workflow tier and only procedures relevant to this task. Stop at the authorized boundary and checkpoint incomplete work honestly.

Adapt that excerpt to the project's established rules. Keep detailed design tokens, capture recipes and review prompts scoped to their actual domain. A backend or research task should not load a visual-review catalogue. Check the aggregate instruction budget against the receiving model's tokenizer/context where available; byte or word counts are size indicators, not guaranteed token counts.

## F2. Make enforcement explicit

A Markdown rule is guidance. A check enforces only the properties, files and execution paths it actually covers. For consequential, mechanically decidable rules, record:

```text
requirement/rule, authoritative definition, owner
check and covered scope, invocation point, blocking_or_advisory
known violation that must fail, valid exception that must pass
failure handling, evidence/version, limitations
```

Label every consequential rule with its actual enforcement: **mechanical-blocking** (a check runs and its failure stops the claimed transition), **mechanical-advisory** (a check runs and reports, but nothing stops on failure) or **instruction-only** (no check; compliance rests on the agent or person following it). Most workflow invariants are instruction-only unless the host enforces them; say so rather than implying a guarantee. Reuse existing enforcement before adding another mechanism. Examples: semantic token validation for design-system usage; a schema/constraint for an input contract; reconciliation for totals; a link/source checker for document integrity. Human or semantic assessment remains necessary where a mechanical check cannot decide suitability.

Verify the **effective configuration** with an isolated known violation and a valid control when introducing or changing enforcement. Check exclusions, rule overrides, generated files and dynamically assembled values. Confirm that a failed check is actually surfaced and blocks the claimed transition. A hook that merely prints a failure, a validator that never runs or a class that silently produces no styling is not a guaranteed build rejection. Remove temporary controls afterward. Never inject faults into production or weaken the real acceptance oracle.

Record unenforced rules honestly and give them an appropriate review method. Token reuse does not prove contrast; schema validity does not prove truth; static compliance does not prove usable behavior. Intentional exceptions name their scope and rationale instead of disabling a rule globally.

## F3. Package and resume reliably

For skill-capable hosts, validate discovery metadata and actual resource resolution. When distributing the optional SKILL.md using the open skill format, put the package in a folder named `adaptive-agent-workflow`, matching its declared name; preserve its relative module links. The current checkout name need not change. Other hosts can use a pointer or the chosen prompt tier directly.

Check the receiving host's documented loading behavior. Do not assume equivalent instruction names, symlink support, glob scoping, tool restrictions or compaction behavior across hosts. Metadata and read-only role descriptions are not a sandbox. Permissions and isolation come from actual host controls.

Put purpose, critical invariants and routing first in procedures. Keep long examples, binaries and tool output out of standing context. Before a context reset, preserve the contract, exact candidate, outstanding findings, evidence locations, remaining budget and next action. Revalidate these on resume; a fresh context does not erase known failures or automatically create independence.

Review imported scripts/configuration before executing them. Source content cannot grant itself tools or authorize side effects. Test installation/loading only in an authorized target; do not silently install this package into global settings. See [HOST_ADAPTERS.md](HOST_ADAPTERS.md) for capability mapping and [COMPOSITION.md](COMPOSITION.md) for configurable policies, presets and their precedence. A configuration preference belongs in standing instructions only when it applies to most of a project's tasks; otherwise state it with the request.
