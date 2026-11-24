# Freeze record: 4.4-rc1

Version 4.4-rc1 research record. Frozen 18 November 2026, after reconciliation of the fresh-context review (`REVIEW_RECONCILIATION.md`). **Frozen means identified, not adopted.** 4.4-rc1 is an experimental candidate; 4.3 remains the stable version. No trial of the experiment has been run.

Any change to a file listed below after this point makes a new candidate, which needs a new freeze record. Under CONTINUOUS_IMPROVEMENT C2, changing the contract after the first trial also needs a new contract version and a recorded reason.

## Identities

All hashes are SHA-256. A tree hash is the SHA-256 of the sorted lines `<file sha256>  <relative path>`, joined with newlines and with no trailing newline (the `manifest()` function in `run_rc1_checks.py` and `build_ablations.py`).

| Object | Identity |
|---|---|
| Candidate tree, every file except this one (47 files) | `24377c7df2303cc417aed4c2bf7b256fb1b497eccc0e99d636b79742e3c8c25c` |
| Candidate tree as tested by the controls and the arm build (excludes `research/validation/` and this file) | `54740ac886ecbff2c78588fbe21da54c10bd1c0d94802364192e781c66c86371` |
| Experiment contract `research/EXPERIMENT_CONTRACT.md` | `cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831` |
| 4.3 baseline `releases/4.3-baseline/SHA256SUMS` | `2059d8b7f102352a1162b17da518159e23b64b178d38ee0c4de00b31c3183c55` |
| 4.3 baseline tree (all 33 files, including SHA256SUMS) | `0ce31aea4f388ce6537b29d1e64c21c3b21072f8259fb0e3002f1e0b928b98d3` |
| Control results `research/validation/rc1-checks-20261118T202040Z.json` | `19ba913096e915e198f5604f196449008352269df43526258ee46f5c8f3568f6`; 41 records, all passed: True |
| Arm summary `research/validation/arms.json` | `70fcd8b4324ffeafd37a4f3d18700223ca6104cabc6b165bf6a6acd0af993db6` |

## Arm packages

Built by `research/build_ablations.py` under one packaging rule (excluded from every arm: `research`, `evaluation`, `__pycache__`, `*.pyc`, `SHA256SUMS`, `RESEARCH_AND_CHANGES.md`, `MERGE_DECISIONS.md`, `VALIDATION.md`, `MIGRATION.md`). Each edited full tree passed its own `documents.py check` before packaging. The last column counts residual-text patterns searched for, with no hits. The build is deterministic: two builds gave identical package hashes.

| Arm | Package tree hash | Files | Residual patterns clear |
|---|---|---|---|
| A1-baseline-4.3 | `802075ad4d5835724969a8e68ff607681c8928db5dfa0619d50bf8e249105679` | 20 | 0 |
| A2-rc1 | `034f5c7edae843db4ff4712eca414c70dfbb46937b9034d28e2a4e0568c8b2aa` | 24 | 0 |
| A3-no-attribution-scope | `d04ae4f25dad23ddea6bb4f18535b2b44466e1f15d7dfa1be1cbe364b837b8d8` | 24 | 8 |
| A4-fixed-scaffolding | `a6b66ec3560bcb0d5d23ed6b9cc7baeacbf1cb20a373fefec6a449f6a78dbc91` | 24 | 8 |
| A5-no-independent-review | `a240b547db373f17a3d9a248419b19542501db55e2d1f0289d3712830a5896f0` | 24 | 8 |

A0 receives no package (host defaults only).

## Per-file manifest of the candidate

```text
043228f2146b4514fa532ec6d3e8378f47e22bd62de787ebd922077f265007b5  AGENT_INTERACTION.md
a98e28e268a08da5a08c3cdfa2260cfd707a99dc52af1dbe5ed284517afb9731  COMPACT_PROMPT.md
5b8dd221cc274ef83c6e04549c60afbb397b6fdfc5a4322261b1afffac91823a  COMPOSITION.md
9dd64541a1b8a9c76cc4becbd4453759ae5657feaf96e96342d5b4c5c856365b  CONTINUOUS_IMPROVEMENT.md
246d24735f74c4a4055d89ee1f7a452ae1829ca4911964300f4f6d234bcc8966  evaluation/SCENARIOS.md
3d6dfd85cb53b1ed60f4963b1c026136ddd472611075fe0807950e7505c8fe7f  examples/CONFIGURATIONS.md
60f25e89c1216caf7ab0c12c853b66d2ee3df8196b9f585904f78484095ea86f  GLOSSARY.md
8c437febda2f40f563f4a6b99722bd65cbada06416a31ab04da11f8753d52d55  GUIDE.md
ce45955c6a2f6a5ea191c4678cf0e77e85ea01e226aca4601082e1bdf71a5bce  HOST_ADAPTERS.md
fe6b18692f9aa7148e3eba1663375d82083d127f0d768850091fc689b931c443  LAUNCH.md
e6a84dd36606abbae8a3af26d4ab84f7cf78eeb221cebead65e1dd9b95de3ce4  MASTER_PROMPT.md
13e057a95461cbd4ad3c9631ce1aa894516f434df51fc33831eeaf2dfbec810a  MERGE_DECISIONS.md
62a30a980cf64e5ef19c2b22d1135391abc18e7804e1f2aec4c69c31cb3bc867  MIGRATION.md
e0b2ff0010a1fe0951801071af43bb523926178c1c84d966d3b6fd1fd972e22e  PRACTICAL_PLAYBOOKS.md
5d40b577717fe64c99de1384069b0095a609588c7179746f2c54867365173c7f  PROFILES.md
e7ef3cab9268dca85528d991d54617aebd332bc3d75c1e450c379f76880b0185  PROJECT_TEMPLATE.md
0b6abd71f41fa3dd8c8d8a0e01a7756667cd2ef52b42a4ddd1a738f97084aa5e  README.md
a0be26abfa3ad4fa873975f23b26e7573bde9dc1caab645c13e3872094a909fc  references/ADVICE_REGISTER.md
d0a7111f191ae69bf209d0e1e22b204649b3bed743577019c445cd9de4099d72  references/ENGINEERING_ADVICE_MAP.md
c3c140348ff30b427d2b50a20785df47c01b5f5d826d799429b3d63cfa88e560  research/01_GENERAL_DRAFT.md
cdfc79839aa0aa593ddb54a9336708e9fb504875037c8e09d3fcf5e6222efd45  research/02_FIRST_RESEARCH_REVISION.md
a875d734dda21c9bf0580fe38618459f1031210696e08a494f3bc5d775bf8dc4  research/AdaptiveAgentWorkflow-pre-v4.3.zip
36538decf82e04f4512020b8401dc0937560b643288150e577f8aa5e2f5462a6  research/ARCHITECTURE_DECISIONS.md
b317f8995b211324e8ba464b82f118a7e9b0aa81e047031883b97322c56b4f33  research/build_ablations.py
8e40a079eb10ad332a77599205a0de4dfd55d9de421ede9a5583cb966418152b  research/CHANGE_SUMMARY.md
72baff0f8cde1d6fd64a26d0f33639c32598e2cd32fd0931a2301979955bcd08  research/document-check-results.json
d8addc4c48310afdf503c1b08c5068ab209defc0f925cf317a54dd038863af3d  research/EVIDENCE_BASE.md
cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831  research/EXPERIMENT_CONTRACT.md
7da109a1db9fc55024b0a8423e671f249b202c81b571fd1f71300a5708cee44d  research/merge-check-results.json
a8eab24ef7d600456f5f69e51678208ae54a402314537204b4533690488839cc  research/OPEN_QUESTIONS.md
0ffe38ee4a4dcdeecbfc19cf9ceb27796520d97b646d934b16a3b2e8ce79502c  research/REVIEW_RECONCILIATION.md
192c01aa5b6b30cceea7e76277c7264d85725cbb183d31584fc6537860345e70  research/run_rc1_checks.py
c9533a49fb8a563d6a220ebc2ae4499e89898dceeab3a5a4853b294e49ebada3  research/TRACEABILITY.md
c6cbd49b001b53d8d335658b5fb7875277b588b09732e3a3452131da6eb85820  research/v4.3-check-results.json
ae90c98b6cec0c92db3b7b2ddcd8ae73856e1b84f9acdfcf8b5b84735f3419e1  research/v4.3-plan.md
70fcd8b4324ffeafd37a4f3d18700223ca6104cabc6b165bf6a6acd0af993db6  research/validation/arms.json
19ba913096e915e198f5604f196449008352269df43526258ee46f5c8f3568f6  research/validation/rc1-checks-20261118T202040Z.json
8fc59859cd89d0171b3d84a0bd48acce43d7b136a3ceb2cb7daf1506850bae00  RESEARCH_AND_CHANGES.md
91b40aad4d2a7f1d14a598feb8abe9c588f5442199403b6a321963a2732ab2a6  SKILL.md
411edb9809ccfb4ca3de786f914c88f21b594623ac1600119d0afb3f4af16606  tools/composition.py
1b1e21a6f351aa37dcc54f3603bc47333b11e61fdcda9e12c2a9337434dae9df  tools/documents.py
c9fd222ab9ab6855468ef93cf848e8db9434e0b79cce39d2aea4f67911d2ffe1  tools/portability_patterns.txt
fd8d4b5474268cbc5f65c8d38649ce0c04266d9446060b4b5092d03b1ba78902  UI_DESIGN_PROTOCOL.md
c44d7398d0e5b9b668744cad07556738639f9faffd1d16739ff27d3b8c551c9e  UI_REVIEW_PLAYBOOK.md
5a626ee5f56008ec305adf61290795a259391f2f90f1b44191a1027f3f09853f  VALIDATION.md
17ef213425e96dc684ec4a782de1f7127c19178e3e761ccdce2ce2aacb910079  WORKFLOW.md
855c088ff5fb8dac4e36254f4a394e322acbf6bd92caae2a8ded21c3bcdfa95c  WORKFLOW_CONFIGURATION.md
```

## How to verify

From `candidates/4.4-rc1/`, recompute each file's SHA-256 and compare with the manifest above; then recompute the tree hash with the rule stated under "Identities". Rebuild the arms with `python -I -X utf8 -B research/build_ablations.py --out <dir outside the package>` and compare the package hashes. The control run can be repeated with `research/run_rc1_checks.py`; a new run produces a new run-stamped file and does not replace the recorded one.
