# 4.4-rc2: change record

Created 19 November 2026 from the frozen 4.4-rc1 tree (`c9c951079fea…79d3`), on the owner's decision after the second independent review (`experiments/OWNER_DECISIONS.md`, D8). **4.4-rc2 is an experimental candidate, not the stable version, and no comparative claim is made.** 4.3 stays the stable version and the comparison baseline. 4.4-rc1 is kept unchanged as a historical, reproducible candidate.

## Scope

Only the two resolver defects confirmed by the second independent review are corrected. Every other change is a version label.

| ID | Defect in rc1 | Severity | Correction in rc2 (`tools/composition.py`, `resolve`) |
|---|---|---|---|
| KD-01 | Key names are case-insensitive by specification, but `resolve()` called directly with `Preset: quick-fix` ignored the preset silently (scaffolding `auto` instead of `minimal`). `parse_block`, the documented entry point, already lowercased keys, so configuration blocks were not affected. | Medium | Keys are folded to lower case on entry. If two spellings of one key are given, the later value is used, with a warning. |
| KD-02 | A misspelt participation value (`participation: autonomou`) was corrected to `autonomous` inside the per-key loop. So the participation preset was applied after or before an explicit `execute: human` depending on key order, and could overwrite it. | High | Participation, whether valid or corrected to its single closest value, is resolved before every other explicit key. An explicit stage setting therefore always overrides the participation preset, in any order. The correction is still reported as an `InvalidValue` divergence. |

## Version label

`4.4-rc1` was replaced by `4.4-rc2` in the package's own version lines, and in `tools/documents.py`, `research/build_ablations.py` and `research/run_rc2_checks.py` (renamed from `run_rc1_checks.py`). Historical records keep their wording: the research and review texts, `RESEARCH_AND_CHANGES.md`'s rc1 section, `MERGE_DECISIONS.md` and `evaluation/SCENARIOS.md`. rc1's validation results are kept in `research/validation/rc1-history/`.

## Evidence

- `experiments/4.4-independence/test_known_defects.py` states the correct behaviour once and checks both candidates.
  - KD-01 and KD-02 fail on rc1 and hold on rc2.
  - Every single valid key and value, and every preset, resolves identically in rc1 and rc2.
  - rc1's `parse_block` path was never affected by KD-01.
- rc2 passes `tools/documents.py check`, `tools/composition.py check` and `independence`, and the 41 document-maintenance controls (`research/run_rc2_checks.py`).
- The arm build is deterministic: two builds gave identical package hashes (`FREEZE.md`). A1 is unchanged. A2–A5 change because they are built from rc2.

## Not changed

The mandatory invariants, every module's guidance, the presets, the tables, the examples, the experiment contract and the evidence base are all unchanged. The contract is amended outside the candidate by `experiments/CONTRACT_AMENDMENT_01.md` and `CONTRACT_AMENDMENT_02.md`.
