# Freeze record: 4.4-rc1

Version 4.4-rc1 research record. Frozen 18 November 2026, after reconciliation of the fresh-context review (`REVIEW_RECONCILIATION.md`). **Frozen means identified, not adopted.** 4.4-rc1 is an experimental candidate; 4.3 remains the stable version. No trial of the experiment has been run.

This record supersedes a first freeze made earlier the same day (tree `24377c7d…c25c`). That freeze was reopened before any trial, under the session instruction to continue rather than defer, to cut the compact tier from 10,821 to 10,150 bytes by wording alone and to lower its ceiling to 10,500 bytes. The first record and its results are kept in `research/validation/superseded-freeze-1/`.

Any change to a file listed below after this point makes a new candidate, which needs a new freeze record. Under CONTINUOUS_IMPROVEMENT C2, changing the contract after the first trial also needs a new contract version and a recorded reason.

## Identities

All hashes are SHA-256. A tree hash is the SHA-256 of the sorted lines `<file sha256>  <relative path>`, joined with newlines and with no trailing newline (the `manifest()` function in `run_rc1_checks.py` and `build_ablations.py`).

| Object | Identity |
|---|---|
| Candidate tree, every file except this one (50 files) | `616f45ddfe138d863fc06d1a306798f89738e1b676e230d35b05852ce47407f5` |
| Candidate tree as tested by the controls and the arm build (before the current results and this file were added) | `8905f0c0c5430a77638c17567c10b1f2a94e3e6fa6511fbafa32a43a06bb42e5` |
| Experiment contract `research/EXPERIMENT_CONTRACT.md` | `cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831` |
| 4.3 baseline `releases/4.3-baseline/SHA256SUMS` | `2059d8b7f102352a1162b17da518159e23b64b178d38ee0c4de00b31c3183c55` |
| 4.3 baseline tree (all 33 files, including SHA256SUMS) | `0ce31aea4f388ce6537b29d1e64c21c3b21072f8259fb0e3002f1e0b928b98d3` |
| Control results `research/validation/rc1-checks-20261118T202324Z.json` | `5fca07d48a88bea4fb3a36137c688b450a5ad06fc397d304288103c081cee546`; 41 records, all passed: True |
| Arm summary `research/validation/arms.json` | `9ff356cab1360c76458bdc6c32dadcf3deede95c57719af79acf07c13381cfe9` |

## Arm packages

Built by `research/build_ablations.py` under one packaging rule (excluded from every arm: `research`, `evaluation`, `__pycache__`, `*.pyc`, `SHA256SUMS`, `RESEARCH_AND_CHANGES.md`, `MERGE_DECISIONS.md`, `VALIDATION.md`, `MIGRATION.md`). Each edited full tree passed its own `documents.py check` before packaging. The last column counts residual-text patterns searched for, with no hits. The build is deterministic: two builds gave identical package hashes.

| Arm | Package tree hash | Files | Residual patterns clear |
|---|---|---|---|
| A1-baseline-4.3 | `802075ad4d5835724969a8e68ff607681c8928db5dfa0619d50bf8e249105679` | 20 | 0 |
| A2-rc1 | `d01571dde4ec9088720d906b7f283fde125c8b99e9af1612c2bccfcc7af579bb` | 24 | 0 |
| A3-no-attribution-scope | `f48f57669503711c1ccc22babeff8fe8307a3513f983ea503835aca4e6bb5160` | 24 | 8 |
| A4-fixed-scaffolding | `48f1ac5c3667f9331a28e32a52b094ec718a2ef3f588b65613a62708e5028aa6` | 24 | 8 |
| A5-no-independent-review | `37acae5e05ddf0acbb35fba0a0f020c0794a20b8a0de232f91b743e747e56248` | 24 | 8 |

A0 receives no package (host defaults only).

## Per-file manifest of the candidate

```text
043228f2146b4514fa532ec6d3e8378f47e22bd62de787ebd922077f265007b5  AGENT_INTERACTION.md
7d03572f11b452abfc23b3d9d321e1ebc5d885e4a99816483c69c4ea41d51417  COMPACT_PROMPT.md
5b8dd221cc274ef83c6e04549c60afbb397b6fdfc5a4322261b1afffac91823a  COMPOSITION.md
9dd64541a1b8a9c76cc4becbd4453759ae5657feaf96e96342d5b4c5c856365b  CONTINUOUS_IMPROVEMENT.md
246d24735f74c4a4055d89ee1f7a452ae1829ca4911964300f4f6d234bcc8966  evaluation/SCENARIOS.md
3d6dfd85cb53b1ed60f4963b1c026136ddd472611075fe0807950e7505c8fe7f  examples/CONFIGURATIONS.md
60f25e89c1216caf7ab0c12c853b66d2ee3df8196b9f585904f78484095ea86f  GLOSSARY.md
8c437febda2f40f563f4a6b99722bd65cbada06416a31ab04da11f8753d52d55  GUIDE.md
24fb5b9c92b91aede8f194941e7763bb41dd83682f1fe8dde80fc83ed15f5b70  HOST_ADAPTERS.md
fe6b18692f9aa7148e3eba1663375d82083d127f0d768850091fc689b931c443  LAUNCH.md
684eb5a8b41f2807ce066d8f6db0e48c4925f579ee748aa3fcb9ebf0527d188e  MASTER_PROMPT.md
13e057a95461cbd4ad3c9631ce1aa894516f434df51fc33831eeaf2dfbec810a  MERGE_DECISIONS.md
20f1ee0eb9ea178a5c864a9df3ed79f80e25bdff91393baf83736bdc72c7e0e6  MIGRATION.md
e0b2ff0010a1fe0951801071af43bb523926178c1c84d966d3b6fd1fd972e22e  PRACTICAL_PLAYBOOKS.md
5d40b577717fe64c99de1384069b0095a609588c7179746f2c54867365173c7f  PROFILES.md
e7ef3cab9268dca85528d991d54617aebd332bc3d75c1e450c379f76880b0185  PROJECT_TEMPLATE.md
acab840112d96f047cf21e6b7628fb68be2cf15929e6a6e6fb69a712ea7577c6  README.md
a0be26abfa3ad4fa873975f23b26e7573bde9dc1caab645c13e3872094a909fc  references/ADVICE_REGISTER.md
d0a7111f191ae69bf209d0e1e22b204649b3bed743577019c445cd9de4099d72  references/ENGINEERING_ADVICE_MAP.md
c3c140348ff30b427d2b50a20785df47c01b5f5d826d799429b3d63cfa88e560  research/01_GENERAL_DRAFT.md
cdfc79839aa0aa593ddb54a9336708e9fb504875037c8e09d3fcf5e6222efd45  research/02_FIRST_RESEARCH_REVISION.md
a875d734dda21c9bf0580fe38618459f1031210696e08a494f3bc5d775bf8dc4  research/AdaptiveAgentWorkflow-pre-v4.3.zip
3cce4fb8a7d6632324c1aeba71f3dedd63c1bab8413d565df289b9477b857a78  research/ARCHITECTURE_DECISIONS.md
b317f8995b211324e8ba464b82f118a7e9b0aa81e047031883b97322c56b4f33  research/build_ablations.py
a054510a042433f4cdaf84ff04e6dc6188f55ec477d24c0930863cd3e4968590  research/CHANGE_SUMMARY.md
72baff0f8cde1d6fd64a26d0f33639c32598e2cd32fd0931a2301979955bcd08  research/document-check-results.json
d8addc4c48310afdf503c1b08c5068ab209defc0f925cf317a54dd038863af3d  research/EVIDENCE_BASE.md
cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831  research/EXPERIMENT_CONTRACT.md
7da109a1db9fc55024b0a8423e671f249b202c81b571fd1f71300a5708cee44d  research/merge-check-results.json
f44d329cc83e5f317aba6d1ecd577c7317a5d0818584469b3ef09d00705df0b3  research/OPEN_QUESTIONS.md
4e01c7c83a6507cb616bbc14b76d783de57bea3e505678718eca392ff189aa9d  research/REVIEW_RECONCILIATION.md
71079ed44f5700ed7f5e275744841f0234b40895ee8ba165475cf0f235601661  research/run_rc1_checks.py
c9533a49fb8a563d6a220ebc2ae4499e89898dceeab3a5a4853b294e49ebada3  research/TRACEABILITY.md
c6cbd49b001b53d8d335658b5fb7875277b588b09732e3a3452131da6eb85820  research/v4.3-check-results.json
ae90c98b6cec0c92db3b7b2ddcd8ae73856e1b84f9acdfcf8b5b84735f3419e1  research/v4.3-plan.md
9ff356cab1360c76458bdc6c32dadcf3deede95c57719af79acf07c13381cfe9  research/validation/arms.json
5fca07d48a88bea4fb3a36137c688b450a5ad06fc397d304288103c081cee546  research/validation/rc1-checks-20261118T202324Z.json
70fcd8b4324ffeafd37a4f3d18700223ca6104cabc6b165bf6a6acd0af993db6  research/validation/superseded-freeze-1/arms.json
33a7da3e8775916d2368e87bda4b7d7d597eb0207dfda1512d0469b9a32c337c  research/validation/superseded-freeze-1/FREEZE.md
19ba913096e915e198f5604f196449008352269df43526258ee46f5c8f3568f6  research/validation/superseded-freeze-1/rc1-checks-20261118T202040Z.json
8fc59859cd89d0171b3d84a0bd48acce43d7b136a3ceb2cb7daf1506850bae00  RESEARCH_AND_CHANGES.md
91b40aad4d2a7f1d14a598feb8abe9c588f5442199403b6a321963a2732ab2a6  SKILL.md
411edb9809ccfb4ca3de786f914c88f21b594623ac1600119d0afb3f4af16606  tools/composition.py
1b354ecbe4b86d7902465b62d6bd8242240fceaf7645d3e800dc4cc324d53f04  tools/documents.py
c9fd222ab9ab6855468ef93cf848e8db9434e0b79cce39d2aea4f67911d2ffe1  tools/portability_patterns.txt
fd8d4b5474268cbc5f65c8d38649ce0c04266d9446060b4b5092d03b1ba78902  UI_DESIGN_PROTOCOL.md
c44d7398d0e5b9b668744cad07556738639f9faffd1d16739ff27d3b8c551c9e  UI_REVIEW_PLAYBOOK.md
a191e85e5736a3543d4405655eb4b43fa4fab8eb4fa835d544aec37a392c62fb  VALIDATION.md
17ef213425e96dc684ec4a782de1f7127c19178e3e761ccdce2ce2aacb910079  WORKFLOW.md
855c088ff5fb8dac4e36254f4a394e322acbf6bd92caae2a8ded21c3bcdfa95c  WORKFLOW_CONFIGURATION.md
```

## How to verify

From `candidates/4.4-rc1/`, recompute each file's SHA-256 and compare with the manifest above; then recompute the tree hash with the rule stated under "Identities". Rebuild the arms with `python -I -X utf8 -B research/build_ablations.py --out <dir outside the package>` and compare the package hashes. The control run can be repeated with `research/run_rc1_checks.py`; a new run produces a new run-stamped file and does not replace the recorded one.
