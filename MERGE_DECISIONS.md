# Selective merge of the three folders

> Historical record of the version 4.1 merge, kept unchanged in substance. In 4.4-rc1 it remains authoritative unless superseded by `research/ARCHITECTURE_DECISIONS.md`; "assurance profile" in this record means what 4.4-rc1 calls an assurance level.

Version 4.1. This is a consolidation of compatible knowledge, not a concatenation of competing instructions or an implementation of a new agent runtime.

## Decision

Use **AdaptiveAgentWorkflow** as the sole active general package. Preserve the previous package snapshot and leave the other two input directories unchanged. No original source directory is a runtime dependency of the merged package.

| Input | What it actually contains | Treatment |
|---|---|---|
| AdaptiveAgentWorkflow | General core, domain profiles, UI/design, host adaptation, improvement protocol and master prompt | Governing architecture retained; practical detail added as an optional module |
| pragmatic-workflow | Earlier software-focused skill, nine detailed scenarios, role/evidence contracts, host/GitHub guidance, Python structural checker and tests | Compatible procedures adapted into the practical playbooks; engineering advice mapping retained as reference |
| workflow-review-h9g46ee9 | Ten files forming a synthetic review/checker fixture, including placeholder identities and canned reports | Used as a negative evidence example and evaluation case; not imported as instructions or live project evidence |

## Useful detail recovered

- Role-specific initial inputs and exclusions, including reproducer/diagnostician separation when bias risk warrants it.
- Detailed procedures for ambiguity, bugs, refactors, independent alternatives, security, benchmarks, concurrency and migrations.
- Concrete task, event, evidence, review, finding and delivery record fields, without prefilled passing verdicts.
- Targeted checks of the assurance mechanism using known-bad inputs and clean controls.
- Distributed-system concerns such as duplicates, partial failures and retry budgets; operational ownership/runbooks where applicable.
- An explicit mapping from local task/candidate/evidence records to a future collaboration or CI service.

These additions are in [PRACTICAL_PLAYBOOKS.md](PRACTICAL_PLAYBOOKS.md), embedded in the self-contained master and discoverable from the software profile and guide. The general core remains authoritative for assurance, role merging, capability limits, allowed work and completion.

## Conflicts deliberately resolved

| Earlier rule | Merged treatment and reason |
|---|---|
| Governor never implements | Keep the general role model: a coordinator can also make work, but then cannot independently accept that work |
| No fresh contexts means stop before implementation | Keep bounded first-party progress; required independent acceptance remains blocked |
| Fixed worker ceiling and numeric routing thresholds | Retain consequence-based routing and actual host limits; old numbers are not universal evidence-backed thresholds |
| Every nontrivial task must have three distinct role identities | Keep the declared assurance profile; role strings do not prove independence and a small task should not inherit a fixed roster |
| Every completion must include build/static-analysis/regression | Apply software checks where relevant; research and documents require their own valid methods |
| One prescribed filesystem/state layout | Reuse existing authoritative records; schemas or a custom service are not universally required |
| Generic LOCAL_READINESS label | Do not import it into active acceptance; structural validity and supported conclusions remain separate |
| Old host-specific dispatch examples | Retain capability-based host adaptation instead of fixed vendor commands |

The old Python helper is not copied or promoted into a v4.1 certifier. It encodes the older software-specific model and cannot verify evidence truth. Porting it would require a separately scoped implementation and validation effort. Its passing test count would not establish the new protocol's correctness.

## What the fixture actually showed

During this review, the old helper was run read-only on workflow-review-h9g46ee9. It returned `LOCAL_READINESS` and explicitly noted that only structural/integrity checks had passed and that evidence truth still needed inspection. The fixture uses `baseline-sha` and `candidate-sha`, and its evidence file contains only “candidate tests passed.” This is a useful demonstration of the checker boundary, not product verification.

The merged playbook treats such a bundle as insufficient for claimed acceptance. The evaluation table includes this case, but no actual future agent trial has yet demonstrated that the protocol reliably rejects every misleading bundle. No fabricated PASS record was added to live state.

## Preservation and scope

The current general package was snapshotted before edits as `AdaptiveAgentWorkflow-pre-merge-v4.zip` alongside the directories. The older v4 ZIP also remains. The two other source folders were inventoried before work and checked for unchanged contents after consolidation. The new distributable is self-contained and excludes old checker code, bytecode caches and synthetic passing reports.

This pass compared local sources and resolved their contradictions; it did not perform a new internet research cycle. The prior research and iterative improvement protocol remain available. No application, deployment, remote integration or background automation was created by merging the workflow documents.
