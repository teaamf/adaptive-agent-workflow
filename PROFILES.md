# Optional work profiles

Version 4.4-rc1. Select only relevant methods and record why each gate applies. Profiles compose: a data dashboard may need software, data and UI methods. These are starting points, not complete specialist standards. They do not grant external actions or supersede adopted requirements.

## P1. Software and systems

Use for applications, services, APIs, libraries, command-line tools, embedded systems and infrastructure code. Identify the actual stack, interfaces, supported environments, compatibility promises and acceptance boundary. Prefer existing tools and conventions. Add a build skeleton or test harness only when missing and needed; do not automatically build a general control plane.

Preserve pragmatic engineering practices: small reversible changes; explicit contracts/invariants; separation of stable mechanisms from real variability; typed/versioned configuration where warranted; controlled clocks/randomness in tests; semantic rather than syntactic duplication removal; composition and replaceable seams without gratuitous interfaces; and visible data flows. Handle expected errors through recovery rather than programmer assertions.

Design so that code is easy for agents and people to change safely. Agents reason best over small, local and explicit code [Pragmatic 14, 17, 44, 47, 50, 69]:

- narrow module boundaries;
- explicit inputs and outputs instead of hidden global state;
- deterministic seams for clocks, randomness and I/O;
- names drawn from the domain vocabulary.

Treat a hard-to-test unit as a design smell; do not fight the test harness to work around it. Use property-based tests where a clear invariant exists, and have a person review the critical properties [Pragmatic 71]. When a bug is fixed, prevent its class from recurring with a test, check or rule [Pragmatic 94]. For intermittent failures, record seeds, ordering and timing. Rerunning until green hides a real race [Pragmatic 58].

| Scenario | Distinctive method |
|---|---|
| Feature | Trace acceptance to external behavior and relevant regression checks |
| Ambiguous feature | Resolve the uncertain criterion with a bounded prototype or research |
| Bug | Establish the failing case before repair; show the same case after repair; document practical exceptions |
| Refactor | Freeze behavior/characterization criteria before changing structure |
| Competing solutions | Same baseline, workloads and hard gates; predeclared comparison |
| Security/privacy | Actual trust/data boundaries, misuse, dependencies, least privilege, safe input and failure behavior; for LLM/agent features, the core agent security boundary and OWASP agentic risks |
| Performance | Representative workload, controlled before/after measurement and raw samples |
| Concurrency | Predetermined stress/reproduction plan; retain failed runs and ordering/seed information |
| Migration | Integrity/compatibility checks, realistic rehearsal, restore limits and authorization for the actual change |

Integration uncertainty may justify tracer work across actual boundaries. Choose the number and order from the system's dependencies. Do not require a particular catalogue, language, platform, device or offline/network policy by default. Release signing, device testing and packaging are gates only when the selected target or project requires them. Freeze exact distributed bytes and verify effects on supported targets; a different export/build is not the tested artifact.

For detailed execution procedures use PRACTICAL_PLAYBOOKS O1–O4. For distributed behavior examine idempotency, duplicate delivery, timeout/retry budgets, resource cleanup and partial failures. Preserve reproducible dependency/toolchain information. Operational services need ownership, relevant telemetry, a runbook and recovery proportional to impact; these are conditional service concerns, not requirements to create a platform for every project.

## P2. Interfaces and human-facing design

Use UI_DESIGN_PROTOCOL.md for relevant human-facing work: apps, websites, tools, interactive data products and service interfaces. Apply user goals, contextual evidence, information architecture, coherent visual direction, discoverability, recovery, accessibility and trust. Interpret “screen,” “component” and “input” according to the actual medium rather than forcing a mobile-app model.

No UI module is required for a backend-only change. Conversely, a technically simple interface may still require substantial accessibility review. Choose standards and assistive environments for the actual platform; book-derived heuristics do not supply universal numerical gates. Human studies and platform-device checks are distinct evidence types with separately declared applicability.

## P3. Data and analytical work

Define the analytical question, intended use, population/time window, units, data provenance, access rights and limitations. Inspect missingness, duplication, joins, transformations, leakage, selection effects and assumptions. Preserve immutable inputs or source/version identifiers and a reproducible transformation path where possible. Do not expose sensitive raw data through evidence logs.

Define quantitative metrics before measuring: units, event boundaries, workload/sample, environment, statistic, threshold and rationale; keep targets distinct from observations and retain raw measurements. Check an independently calculated sample or known-value control in addition to executing the pipeline. Distinguish computational reproduction from valid inference: rerunning the same biased analysis can reproduce the same wrong conclusion. Quantify uncertainty using methods appropriate to the design; make causal claims only when the design supports them. Review charts for misleading scales, aggregation and labels. Specialist review depends on consequence and analytical complexity, not whether the output is a spreadsheet or code.

Deliver the requested report/data/code with methods, scope and limitations. A novel model, web dashboard or production deployment is not automatically part of an analysis request.

## P4. Research and evidence synthesis

Freeze the question, scope, relevant dates, inclusion/exclusion criteria and claim types. Prefer primary sources for technical claims; inspect source content rather than citing a search snippet as proof. Keep source findings, interpretation, inference and unresolved disagreement separate. Seek counterevidence and record material search gaps.

Check that each consequential claim is supported by its cited source and that dates, versions and contexts match. Repeated citations of one underlying study are not independent corroboration. A plausible synthesis can be complete with explicit uncertainty; an empirical result requires the corresponding actual observations. Do not invent participant testimony, citations or experiments.

Define a stopping condition tied to the question, evidence needs and budget. More search is warranted when it could change a material conclusion, not merely to increase source count. Respect copyright and data permissions. Publication remains a separate authorized action.

## P5. Documents and other content artifacts

Define audience, purpose, factual inputs, format, tone and acceptance. Check factual fidelity, terminology, logic, completeness, accessibility and structure. Render and inspect the delivered format when layout matters: source markup alone does not prove the exported document is readable. Check tables, figures, references, clipping and navigation where applicable.

Separate editorial preference from factual error. A lightweight correction may finish with focused first-party checks; a consequential report may require an independent factual/domain review. No app skeleton, code test suite or release certificate is implied.

## P6. Operations, infrastructure and external actions

Record the exact target, desired state, baseline, access boundary, impact, idempotency, observability and recovery/rollback limits. Inspect current state; rehearse consequential changes where practical. Verify the resulting external state, not merely a successful request or command exit. Retry only when duplicate effects are understood.

Use actual authorization for deployment, external communications, spending or destructive/irreversible work. A plan or optional module is not permission. Define monitoring ownership/window and stop conditions only when such monitoring is requested. If a domain requires qualified human approval or equipment, name that requirement rather than simulating it with an agent.

## P7. Adding a new domain

Supply its outcomes, characteristic failure modes, applicable standards, valid evidence/oracles, required expertise and tools, artifact identities, recovery and completion criteria. Test the profile on representative cases before claiming operational compatibility. Extend the domain profile rather than adding one project's specifics to the core. If expertise or a valid evaluation method is absent, restrict claims and identify the gap; “general” never means omniscient.
