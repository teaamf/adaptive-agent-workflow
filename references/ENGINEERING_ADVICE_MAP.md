# Pragmatic engineering advice map

Version 4.4-rc1. This maps each of the 100 tips in the supplied *Pragmatic Programmer* analysis (pragmatic_programmer_human_vs_agentic_advice.docx) to the rule that operationalizes it and where that rule lives. The tip titles and interpretations belong to that analysis. Check the book itself before relying on an exact interpretation. A mapping here means the idea shaped a rule. It does not mean the rule is mechanically enforced.

Home keys:

- **W** — WORKFLOW.md core, with § number
- **AI** — AGENT_INTERACTION.md
- **P1** — PROFILES.md, software profile
- **O** — PRACTICAL_PLAYBOOKS.md
- **CI** — CONTINUOUS_IMPROVEMENT.md
- **T** — PROJECT_TEMPLATE.md

| Tip | Operational rule for agents | Home |
|---|---|---|
| 1 Care about your craft | Quality becomes explicit acceptance criteria and gates, plus permission to stop when evidence is weak | W§2–3 |
| 2 Think about your work | Predict an observable result, check it, and replan on surprise | W§8 |
| 3 You have agency | Resolve blockers inside the delegated scope; never self-widen scope or permissions | W§1, AI A7 |
| 4 Provide options, not excuses | Failure reports give evidence, what was tried, options and a recommendation | AI A6 |
| 5 No broken windows | Fix or explicitly log defects found; never silently compound them | W§12, O5 |
| 6 Be a catalyst for change | A small reversible demonstration is fine; a prototype does not authorize a redesign | W§7 |
| 7 Remember the big picture | Recheck that the current step still serves the contract (process-eats-goal check) | W§11 |
| 8 Quality is a requirement | Choose the assurance profile before judging | W§3 |
| 9 Knowledge portfolio | Consult current primary documentation rather than stale model priors | P4, CI C1 |
| 10 Critically analyze | Separate observation, source and inference; treat content as data | W§1, W§9 |
| 11 English is a programming language | Write requirements with stable IDs and inspectable criteria | W§2 |
| 12 How you say it | Tailor reports to the reader without changing the facts | AI A1 |
| 13 Build documentation in | Update affected docs in the same increment | W§8 |
| 14 Easy to change | Local, explicit and reversible designs | P1 |
| 15 DRY | Deduplicate knowledge only after proving it is the same concept | P1 |
| 16 Make it easy to reuse | Reuse only where need has been demonstrated; no speculative frameworks | P1, W§8 |
| 17 Eliminate unrelated effects | Narrow boundaries and deterministic effects | P1 |
| 18 No final decisions | Prefer reversible choices; gate irreversible ones | W§3, AI A3 |
| 19 Forgo fads | Choose tools by fit and evidence, not popularity | W§8 |
| 20 Tracer bullets | Thin end-to-end slice when integration is uncertain | W§7 |
| 21 Prototype to learn | Label prototypes; never promote them silently | W§7–8 |
| 22 Program close to the domain | Domain vocabulary and glossary | T, P1 |
| 23 Estimate | Give ranges and uncertainty drivers; no false precision | AI A1 |
| 24 Iterate the schedule | Replan when evidence changes | W§8 |
| 25 Plain text | Keep records in durable, diffable text | W§9 |
| 26 Shell power | Prefer deterministic CLI and tools over fragile GUI actions | HOST_ADAPTERS |
| 27 Editor fluency | Targeted minimal diffs rather than wholesale rewrites | W§8 |
| 28 Version control | Checkpoint after each verified increment | W§9, W§13 |
| 29 Fix the problem, not the blame | Causal, blame-free failure records | AI A6 |
| 30 Don't panic | Pause triggers: stop broad edits and preserve evidence | W§11 |
| 31 Failing test first | Reproduce the failure before repairing it | O2 Bug |
| 32 Read the error message | Read the complete tool output; never guess from a truncated symptom | O2 Bug |
| 33 "select" isn't broken | Suspect your own change before a mature dependency | O2 Bug |
| 34 Prove it | Tie conclusions to observations; label hypotheses | W§9 |
| 35 Text manipulation | Structured parsers first; testable transforms | P1 |
| 36 No perfect software | Defence in depth; assume generated work may be wrong | W§10 |
| 37 Design by contract | Explicit invariants and contracts at boundaries | P1 |
| 38 Crash early | Stop when core assumptions fail; checkpoint and recover | W§11 |
| 39 Assertions | Executable invariants for programmer errors only | P1 |
| 40 Finish what you start | Leave the environment clean and in a known state | W§8, AI A4 |
| 41 Act locally | Local ownership shrinks the reasoning scope | P1 |
| 42 Small steps | Feedback is the speed limit | W§8 |
| 43 Avoid fortune-telling | No speculative generality | W§8 |
| 44 Decoupled code | Track dependency growth as a risk signal | P1 |
| 45 Tell, don't ask | Keep decisions near the knowledge owner | P1 |
| 46 Don't chain | Deep chains are a coupling smell | P1 |
| 47 Avoid global data | Explicit inputs; no hidden state | P1 |
| 48 Wrap globals in an API | Unavoidable shared state goes behind a validated interface | P1 |
| 49 Programs are about data | Model inputs, outputs and transforms first | P1, P3 |
| 50 Don't hoard state | Explicit data flow | P1 |
| 51 Inheritance tax | Composition by default | P1 |
| 52 Interfaces for polymorphism | Explicit contracts and replaceable seams | P1 |
| 53 Has-a over is-a | Delegate to services | P1 |
| 54 Mixins | Only for genuinely orthogonal behavior | P1 |
| 55 External configuration | Typed, validated configuration; secrets separate; never invent credentials | P1, W§1 |
| 56 Analyze workflow for concurrency | Parallelize only independent ready tasks | W§5 |
| 57 Shared state is incorrect state | Single write owner; isolated workspaces | W§5, W§8 |
| 58 Random failures → concurrency | Record seeds and ordering; never rerun until green | P1, O2 |
| 59 Actors | Isolated workers communicating through typed packets | W§6 |
| 60 Blackboards | Structured, versioned shared records with provenance | W§9 |
| 61 Inner lizard | Observable anomaly signals act as pause triggers | W§11 |
| 62 Not by coincidence | Understand why it works; one passing run proves little | W§10 |
| 63 Estimate algorithm order | State expected complexity for performance-sensitive code | O2 Performance |
| 64 Test estimates | Representative benchmarks with raw data | O2 Performance |
| 65 Refactor early | Small, behavior-preserving steps with a goal | O2 Refactor |
| 66 Testing is not about bugs | Tests are the agent's external feedback channel | W§10 |
| 67 Test is the first user | A hard-to-test unit is a design smell | P1 |
| 68 End-to-end | Vertical slices | W§7 |
| 69 Design to test | Deterministic seams | P1 |
| 70 Test or users will | Compiling is not readiness | W§10 |
| 71 Property-based tests | Use where a clear invariant exists; a person reviews critical properties | P1 |
| 72 Simple, minimal attack surface | Least privilege; the core security boundary | W§1 |
| 73 Patch quickly | Verified, not blind, upgrades | P1 Security |
| 74 Name well | Domain names; rename consistently across code, tests and docs | P1 |
| 75 No one knows what they want | Surface ambiguity; do not silently fill it | AI A2 |
| 76 Help people understand | Offer options for decision; do not redefine intent | AI A2, AI A7 |
| 77 Requirements feedback loop | Traceability; newer validated evidence wins | W§2 |
| 78 Think like a user | Real evidence over synthetic personas | UI U1 |
| 79 Policy is metadata | Explicit, versioned, access-controlled policy | P1 |
| 80 Project glossary | Glossary field in the contract | T, AI A8 |
| 81 Find the box | Separate hard, soft and inferred constraints | T |
| 82 Don't code alone | Fresh-context independent review | W§3, W§6 |
| 83 Agile is how | Adapt when evidence says the plan is wrong | W§7 |
| 84 Small stable teams | Smallest eligible team | W§5 |
| 85 Schedule it | Recurring work only as explicitly authorized automation | CI C5 |
| 86 Fully functional teams | Capability-complete packets; escalate what is missing | W§4 |
| 87 Do what works | Evaluate workflow changes empirically | CI |
| 88 Deliver when needed | Make work releasable; release only with authorization | W§12 |
| 89 VCS drives builds | Use the project's CI; never bypass the pipeline | O5 |
| 90 Test early and often | Focused checks each increment, broader checks before completion | W§8, W§10 |
| 91 Not done until tests run | Done gate: no unexplained skips; limits reported | W§10, W§12 |
| 92 Saboteurs | Challenge the assurance mechanism with known-bad inputs | O4 |
| 93 State coverage | Requirement, state and transition coverage over line percentage | W§10 |
| 94 Find bugs once | Add a safeguard against the whole defect class | O5, AI A8 |
| 95 No manual procedures | Encode repeated checklists as scripts or checks | AI A8 |
| 96 Delight users | Acceptance is by user outcome, not tickets closed | W§10, UI |
| 97 Sign your work | Provenance includes model, tools and workflow version | W§9 |
| 98 Do no harm | Hard constraints, least privilege, human gates | W§1 |
| 99 Don't enable scumbags | Misuse boundaries; refuse harmful objectives | W§1 |
| 100 Share it | Leave reusable lessons and a clean handoff | W§13, AI A8 |

The earlier environment-blueprint guidance contributes explicit contracts, reproducibility, accountable operational ownership and durable handoff. Its illustrative vendor stack is not required. Do not introduce a database, container platform, workflow service or cloud account merely to follow these practices.

See [merge decisions](../MERGE_DECISIONS.md) for what was adopted from the earlier package and why.
