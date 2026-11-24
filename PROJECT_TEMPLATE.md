# Project contract template

Fill from the user's request and inspected context. Omit irrelevant fields with a reason; do not create a long form the user must complete for a simple task. Unresolved material decisions stay visible. This template contains no default product requirements.

```text
Project/mission ID and objective:
Requested mode: create / modify / investigate / review / repair / other
Deliverables and definition of done:
Full authorized scope and explicit exclusions:
Requirements and source/version references:
Inputs, current baseline and allowed reuse/provenance:
Audience/use context, if relevant:
Glossary of key domain terms, if ambiguity is likely:
Existing agent instruction files or conventions to respect:
Model/host capability tier (compact / modular / full) and known limits:
Hard / soft / inferred constraints (test inferred ones before relying on them):
Security posture: untrusted inputs? private data? external actions? (all three → validation gate):
Applicable work profiles and rationale:
Assurance: lightweight / standard / high consequence; why:
Existing process/tools to reuse:
Authorized workspace or artifact access; permissions:
Environment capabilities and gaps:
Required acceptance gates and valid evidence:
Consequential rules: automated/advisory/manual enforcement, coverage and owner:
UI work, if applicable: visual direction, supported state/variant matrix and capture readiness:
Not-applicable gates and rationale:
Unresolved applicability/decisions:
Specialist/human/device/external requirements, if any:
Optional publication/integration target and authorization:
Resource limits, retry policy and stopping boundary:
For iterative refinement: baseline, per-round evidence and recovery preserving existing work:
Provisional-work bound where required reviews are pending:
Artifact/evidence storage and retention:
Owner, next ready action and handoff needs:
```

For a simple task, a short paragraph may cover these decisions. For a long project, maintain stable requirement and task IDs. An example profile must never populate facts about an unrelated project automatically.
