# Generalization and research record

29 September 2026. Version 4 is a design revision, not evidence that all projects or environments have been successfully tested.

## Why another revision was necessary

The previous core had reusable ideas but still inherited project-specific constraints: a mandatory greenfield foundation/control plane, a three-tracer sequence, platform-specific failure names, signed-mobile-artifact terminology and certification-oriented completion. Its document checker also required one project's 57 sections and 126 source mappings. Renaming the folder alone would not have made it project-independent.

This package is separate from the preserved MolliKey package. It has its own generic master prompt and checker and does not need that project's files. The user's earlier product decisions remain valid for that product; they are not defaults for unrelated projects.

## Generalization before the new research

Saved [the initial general core](research/01_GENERAL_DRAFT.md) before the new source-reading/refinement pass. SHA-256: `c3c140348ff30b427d2b50a20785df47c01b5f5d826d799429b3d63cfa88e560`.

The interrupted preceding turn had already discovered candidate sources. After the user's clarification, the actual general draft was saved, then those sources were read to test and refine it. This distinction preserves the real sequence rather than claiming no earlier search occurred.

| Previous assumption | General rule now |
|---|---|
| Product-focused package/name | Neutral package; user-supplied project contract |
| Every project starts with a foundation | Reuse existing infrastructure; add only missing capabilities |
| Three prescribed tracers | Choose increments from actual integration uncertainty and dependencies |
| New project means clean room | Reuse/provenance policy is explicit and project-specific |
| Every outcome is a software release | Artifact-specific acceptance for software, UI, analysis, research, documents and operations |
| Supervisor never makes work | Roles may merge, but independent acceptance cannot be self-issued |
| Every nontrivial task uses a fixed review roster | Consequence-based assurance with the smallest eligible team |
| Target hardware, signing and UI implied | Only applicable requirements become gates |
| Platform failures in core | Generic failure categories; specialist profiles can extend them |
| Checker requires project catalogues | Generic assembly/link/portability checks with no project-file dependency |

## Research cycle 1 — tailor without rebuilding everything

The [first research revision](research/02_FIRST_RESEARCH_REVISION.md) records the initial conclusions. These are local design inferences from the following primary sources, not claims that those organizations endorse this package. All sources below were accessed 29 September 2026.

| Source | Relevant finding and limit | Application |
|---|---|---|
| [NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf) | Outcome-based practices are intended for risk-based customization; not a universal checklist | Separate core outcomes from selected methods; preserve applicable security requirements |
| [NASA: Tailoring and customization](https://www.nasa.gov/reference/3-11-tailoring-and-customization-of-npr-7123-1-requirements/) | Engineering rigor and documented tailoring respond to project context; institutional approval rules are NASA-specific | Record why consequential gates apply or do not; do not import institutional bureaucracy |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024) | Vendor experience favors simple composable patterns and complexity justified by value; tooling has since evolved | Task-appropriate roles and optional concurrency, without adopting a framework/API |
| [UKHSA: RAP implementation plan](https://www.gov.uk/government/publications/ukhsa-reproducible-analytical-pipelines-rap-implementation-plan/rap-implementation-plan-financial-years-2023-to-2024-and-2024-to-2025) (2024) | Reproducible analysis requires tools, capability and quality practices; this is an institutional plan | Add an analytical profile with traceable inputs/transforms and appropriate review, not an app-development ceremony |

The retained UI methods still separate appearance, task behavior and trust; the pragmatic software profile retains the nine scenario families. Generality did not mean deleting the useful specialist detail. It means loading and applying it where warranted.

## Research cycle 2 — challenge excessive flexibility

Question: could tailoring allow a worker to skip failed gates, or mistake a portable artifact for a valid result? Revisited NIST/NASA applicability guidance and inspected two further primary sources:

| Source | Relevant finding and limit | Application |
|---|---|---|
| [W3C PROV Overview](https://www.w3.org/TR/prov-overview/) (2013) | Provenance relates entities, activities and responsible agents; it informs assessment | Generic input → activity → output → responsibility records, without requiring an ontology or database |
| [ACM SIGSIM PADS: Artifact evaluation](https://sigsim.acm.org/conf/pads/2024/blog/artifact-evaluation/) (2024) | Availability, functionality, reuse and independently reproduced results are distinguishable properties in its research setting | Separate artifact availability/inspectability from supported conclusions; no ACM badge or certification claim |

The central ACM policy page could not be fetched; the report relies on the accessible first-party conference guidance and does not claim to have reviewed the inaccessible policy in full.

Final refinements: consequential tailoring records source/reason/owner; required-but-unavailable is never not-applicable; project changes trigger applicability reassessment; provenance records are verified assertions; executable analyses still need inferential review; broad transfer claims need diverse cases and actual host trials.

## What was retained from the supplied design material

The advice documents are user-supplied interpretations, not direct author instructions. Their 450-item title index remains available in [references/ADVICE_REGISTER.md](references/ADVICE_REGISTER.md). It is a reference catalogue, not 450 required checks or a runtime dependency.

Emotional Design contributes separate visual, behavioral and trust/meaning lenses; Designing Interfaces contributes goal-based structure, context-sensitive patterns, states, navigation and recovery; Universal Principles contributes measurement, bias and contextual design heuristics. Their agentic opinions remain interpretations. Numerical folklore, stereotypes and engagement manipulation do not become acceptance criteria.

Earlier research-informed controls remain: [accessibility tools need judgment](https://www.w3.org/WAI/test-evaluate/tools/selecting/); [model judges have biases](https://arxiv.org/abs/2306.05685v4); and [multi-agent benefits depend on task and architecture](https://arxiv.org/abs/2512.08296v3). The present package carries their bounded design implications, not numerical performance guarantees.

## Version 4.2 — from indexed advice to operational rules, plus research cycle 3

### What the supplied documents showed was missing

A re-read of the four supplied analyses against v4.1 found that the design advice was indexed by title but had been applied only to *products*. The Pragmatic Programmer advice was mapped in ten coarse ranges. Three gaps followed.

1. **The agent's own interface.** Norman's chapters on autonomous systems (ED089–ED118) cover legible internal state, stated capability limits, override policy, goal conflicts and resource awareness. Designing Interfaces covers progress indicators, cancelability, undo, preview, deferred choices, good defaults and changes midstream. Both apply directly to how an agent reports, asks and checkpoints. The package had no rules for this. New module: [AGENT_INTERACTION.md](AGENT_INTERACTION.md).
2. **Bias as an operational hazard.** Universal Principles' synthesis names bias principles as the most valuable controls for multi-agent work. In v4.1 they were only index entries. They are now a judgment-check table and a list of pause triggers in WORKFLOW §11. The triggers replace Pragmatic Tip 61, “listen to your inner lizard”, with observable signals.
3. **Process overhead.** KISS, signal-to-noise, progressive disclosure and process-eats-goal [UP103, UP170, UP147, UP145] all argue against applying a long protocol to trivial work. v4.1 said as much but had no short path. New: WORKFLOW §0, an eight-step fast path with explicit escalation triggers.

The engineering map now maps all 100 tips individually to rules and locations.

### Research cycle 3 — current agent practice (sources accessed 29 September 2026)

| Source | Finding and limit | Application |
|---|---|---|
| [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Nov 2025) | Long runs failed through early “done” claims, broken handoffs and features marked done without end-to-end tests. A feature list starting as all-failing, a progress file, a start-up script, one feature per session and commits helped. The prompt forbade removing or editing tests. This is vendor experience, not a controlled trial. | W§13 multi-session records; AI A4 resume routine; W§10 oracle integrity |
| [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025) | Context is a finite attention budget and degrades with length. Recommends just-in-time retrieval, compaction, structured notes and sub-agents with clean contexts. | W§6 context paragraph |
| [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) (Jun 2025) | Parallel sub-agents helped on breadth-first research at roughly 15 times the tokens of chat. Delegation needed precise objectives, formats and boundaries. Figures come from an internal evaluation. | W§5 when to parallelize |
| [Cognition: Don't build multi-agents](https://cognition.com/blog/dont-build-multi-agents) (Jun 2025) | Parallel workers make conflicting implicit decisions without shared context. The author later softened the stance for specific flows. | W§5 shared decisions; single writer |
| [Cemri et al.: Why do multi-agent LLM systems fail? (MAST)](https://arxiv.org/abs/2503.13657) (2025) | 14 failure modes in three groups: specification/system design, inter-agent misalignment and task verification. Derived from annotated traces of particular frameworks. | W§5 failure clusters |
| [Zhong et al.: ImpossibleBench](https://arxiv.org/abs/2510.20270) (Oct 2025) | Agents frequently exploit tests that conflict with the specification, including modifying tests and special-casing. Prompting and restricted test access changed the rates. Benchmark conditions are not every project. | W§10 oracle integrity; O4 test-tampering case; G22 |
| [Meta: Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (Oct 2025), after S. Willison's “lethal trifecta” | Without reliable injection defences, a session should not combine untrusted input, sensitive access and external state change without supervision. A heuristic, not a complete threat model. | W§1 agent security boundary; T security field; G23 |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (Dec 2025) | ASI01–ASI10 include goal hijack, tool misuse, privilege abuse, supply chain, code execution, memory poisoning, inter-agent communication, cascading failures and human over-trust. | W§1 guard list; AI A5; P1 security |
| [Amershi et al.: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) (CHI 2019) | 18 guidelines across four phases: initially, during interaction, when wrong and over time. Validated with practitioners on existing products. | UI U9; AI A1, A3, A7 |
| [Dhanorkar, Passi & Vorvoreanu: Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391) (Jun 2026) | Developers perform a priori control, co-planning, real-time monitoring and post hoc review. Some treat test results as a guarantee of correctness. Preprint, qualitative. | AI A3 checkpoints; W§10 “a green suite is not a guarantee” |
| [Park et al.: The work behind delegation](https://arxiv.org/abs/2609.24234) (Sep 2026) | Experienced developers concentrate effort in planning, delegate supervision to other agents and turn recurring guidance into reusable assets. Preprint, 19 developers. | AI A8 reusable assets |
| [METR: Early-2025 AI and experienced open-source developers](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (Jul 2025) and [2026 design update](https://metr.org/blog/2026-02-24-uplift-update/) | In the RCT, completion was 19% slower while developers believed they were faster. The later study found participation bias that makes new estimates unreliable. A specific population and tool generation. | CI C4: measure outcomes, not perceived speed |
| [AGENTS.md and the Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/) (Dec 2025); [Agent Skills](https://agentskills.io/) | Cross-vendor repository instruction files and progressively disclosed skill folders. | HOST_ADAPTERS; AI A8 |

Counterevidence and limits: vendor engineering posts describe their own systems and incentives. Several 2026 papers are preprints. MAST and ImpossibleBench measure particular frameworks and benchmarks. Multi-agent guidance is contested and changing. No rule here claims a measured improvement for this package; each is a design inference to be tested under CONTINUOUS_IMPROVEMENT.

### Deliberately not adopted

- **Graduated autonomy that relaxes approvals automatically after a streak of successes.** Commonly recommended, but a success streak is weak evidence for rare high-impact failures. Relaxation stays an explicit owner decision.
- **A mandatory initializer agent or fixed file names** such as progress.txt. The functions are adopted; the host and project choose the form.
- **Emotion inference or persuasive engagement techniques** in agent communication. These conflict with ED097, ED126 and the manipulation limits in U7.

## Rejected approaches and limits

A mere rename was rejected because it would preserve hidden project assumptions. A lowest-common-denominator workflow was rejected because it would discard useful engineering/design methods. A compulsory large team, new runtime service, fixed framework or universal certification path was rejected because it would impose effort unrelated to many tasks.

The result is a common coordination/evidence protocol plus selected methods and an actual project contract. It is not a guarantee of specialist competence, regulated approval, tool availability or performance in every environment. Document checks and author scenario inspection are reported separately from future empirical trials in [VALIDATION.md](VALIDATION.md).

## Version 4.3 — configuration and bounded visual refinement

4 November 2026. Input: the supplied pasted analysis, *Two-Tier Agent Configuration Architecture for Production-Grade Frontend Engineering*. The request was to improve this general package, not implement its sample frontend stack or call its model APIs. Baseline and revision criteria were recorded before edits in [research/v4.3-plan.md](research/v4.3-plan.md); the original package is preserved in [research/AdaptiveAgentWorkflow-pre-v4.3.zip](research/AdaptiveAgentWorkflow-pre-v4.3.zip).

The v4.2 rules already covered progressive disclosure, independent judgment, user outcomes and accessibility. The missing pieces were an adoption procedure separating rule lifecycles, a check that claimed enforcement really blocks violations, and an operational visual-refinement loop with explicit capture failures and safe recovery. Adding these as optional procedures avoids putting their full detail into standing instructions. This is a design rationale, not a measured reduction in cost or defects.

### Primary sources checked on 4 November 2026

| Source | What was checked | Use and limit |
|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Required name/description, folder-name match, progressive loading, optional resources, experimental tool metadata | Short skill entry point; deployment-folder clarification; capabilities remain host-dependent. Read directly in the in-app browser. Discovery was not exercised in multiple hosts. |
| [Playwright page readiness API](https://playwright.dev/docs/api/class-page#page-wait-for-load-state) | The documentation discourages network-idle readiness for testing and recommends assertions | V2 requires an observable intended state with a timeout. The tool-specific example motivates a capability-neutral procedure; no browser tool is imposed on native UI. |
| [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) | Rendering varies with environment; comparisons need consistent conditions | V2 records environment, stabilizes irrelevant variation and qualifies baseline changes. A pinned container is not presented as a universal pixel-parity guarantee. |
| [W3C WAI accessibility evaluation overview](https://www.w3.org/WAI/test-evaluate/) (updated 12 August 2026) | No tool alone determines standards conformance; knowledgeable human assessment is needed | Retain U5/U6's distinct rendered, semantic and outcome evidence and their limits. Model critique is not conformance certification. |
| [Design Tokens Format Module](https://www.designtokens.org/tr/drafts/format/) (draft dated 8 September 2026) | The format addresses interchange of design tokens | Supports treating token representation as an adapter choice. No mandatory exchange format or new token tool was introduced. |

### Input decisions

| Supplied idea | Decision in this revision |
|---|---|
| Standing rules plus on-demand procedures | Adapted in WORKFLOW_CONFIGURATION F1, with one authoritative rule source and a short standing excerpt; no new mandatory instruction file |
| Compile/lint/hook enforcement | Adapted as F2's effective-configuration and violation/control checks; no claim that prose, a hook or a missing utility guarantees rejection |
| Semantic tokens and primitive reuse | Retained as project-owned design roles/components, with explicit scoped exceptions; no imported framework, palette, spacing scale or raw-element ban |
| Stable visual capture | Adapted in V2: state readiness, assets/fonts, controlled variation, diagnostics and comparable conditions. The pasted script catches a readiness failure and proceeds; that behavior is expressly rejected |
| Blind reviewers and staged cost | Adapted in V3: task-aware initial findings, no maker persuasion or desired beauty threshold, targeted review only when useful/required; permissions and real isolation still apply |
| Fixed providers, three-model council, decimal targets and eight rounds | Not adopted. Review resources and finite limits come from the task; aesthetic numbers are optional signals, not release evidence |
| Automatic rollback on a small score regression | Replaced with outcome-based reassessment and ownership-aware recovery. The pasted whole-file checkout can discard user edits; V4 forbids that behavior |
| Separate session/branch for higher scores | Optional context reset with durable state and remaining budget; no mandatory Git, new session or second polish mission |
| Always version-control competitor captures | Replaced with provenance, rights, privacy and retention decisions in the adopting project; no mandatory competitor collection or repository bloat |
| Host discovery/compaction guarantees and skill-security statistics | Not adopted as general facts. Host mappings need current documentation; statistics and exact cross-vendor behavior were not independently established in this cycle |

Related usability correction: A3 and the compact tier now inspect existing authorization before asking again, prepare a concrete checkpoint when permission is missing, and preserve action-time host requirements. This is a local design judgment about unnecessary interruptions; it does not expand permissions.

The optional skill entry point now selects a tier before loading modules. Universal token-count claims were replaced with a byte-budget description and receiving-tokenizer guidance. New public cases G37–G50 cover configuration, capture failures, recovery, review limits and authorization. They remain development scenarios, not an executed agent benchmark or independent acceptance set.

All revised procedures were inspected by their author. No independent reviewer, live UI refinement, external council, human study or cross-model/environment performance trial ran. [VALIDATION.md](VALIDATION.md) records actual maintenance checks separately. Future benefit claims require the existing controlled improvement protocol; the supplied analysis alone cannot establish them.
