# Freeze record: 4.4-rc2

Version 4.4-rc2 research record. Frozen 19 November 2026, after the two resolver corrections recorded in `research/RC2_CHANGES.md`. **Frozen means identified, not adopted.** 4.4-rc2 is an experimental candidate; 4.3 remains the stable version; 4.4-rc1 is kept unchanged at `candidates/4.4-rc1/` (its freeze record SHA-256 `2e1e0cf64553eb2230f2b3e3a9f72afafabc0d31aab76a28401cb2babcdcaa12`). No trial of the experiment has been run.

Any change to a file listed below makes a new candidate, which needs a new freeze record. rc1's validation results are kept for history in `research/validation/rc1-history/`.

## Identities

Tree hashes follow rc1's rule: SHA-256 of the lines `<file sha256>  <relative path>`, sorted by POSIX relative path in code-point order, joined with newlines, no trailing newline; `__pycache__` skipped.

| Object | Identity |
|---|---|
| Candidate tree, every file except this one (58 files) | `11373794ed0d08a335508d25c16276ba3556088b267e0b11b984ff96c76e93ca` |
| Candidate tree as tested by the controls and the arm build (before their results and this file were added) | `9f04e41e352770a79d1513602f298c297c255933f76ce2172db829629ba23936` |
| Derived from rc1 tree | `c9c951079fea1f4c8bfebb8bf5cafdfc97264b97eb07e45b8420d9ab727179d3` |
| Experiment contract `research/EXPERIMENT_CONTRACT.md` (unchanged from rc1) | `cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831` |
| 4.3 baseline tree (all 33 files, including SHA256SUMS) | `581b7530f34f82e5fd60f455bc914b72d6bf3c07b66cca514165574327b876c4` |
| Control results `research/validation/rc2-checks-20261119T131948Z.json` | `d7b228ca944715272c7f61959e93975103758bb05e2b13f50a1ac5020bb4b8d9`; 41 records, all passed |
| Arm summary `research/validation/arms.json` | `a43fdf7791e00f3cbe29ee60c5f863dca7c4345b088291d71ca3b8abf03cefb5` |
| Change record `research/RC2_CHANGES.md` | `860638be8400b9820cf3c6e2972df55765b101cc3a0a23aff15a6d124d96bb88` |

## Arm packages

Built by `research/build_ablations.py` under rc1's packaging rule. Two builds gave identical hashes. A1 is the unchanged 4.3 package; A2–A5 are built from rc2.

| Arm | Package tree hash | Files | Residual patterns clear |
|---|---|---|---|
| A1-baseline-4.3 | `ffd66a0c907f41ca7c7f43114a7f266dc28928a37b15331fb4c630bd8d259cf6` | 20 | 0 |
| A2-rc2 | `f39da607688117c2c38883ee9eba52bcfe86d7bfd98118951dd31dbd6171ee50` | 24 | 0 |
| A3-no-attribution-scope | `3bcd487b7c07be1f6495277badaec824d69c303c373c80d927fd3500d58b02df` | 24 | 10 |
| A4-fixed-scaffolding | `c86c8764b8aa48db96dcf737452f7ba0eb791640365f92e0c42598e03a929ce1` | 24 | 8 |
| A5-no-independent-review | `99604d9ede3227f93969ef3748e97ee0b88087f546c4d04814856e3b0173f728` | 24 | 8 |

A0 receives no package (host defaults only).

## Per-file manifest of the candidate

```text
3a30b84d515ddb3442c3775758e866397ed36e8e76077bc3b6937f29ae23e244  AGENT_INTERACTION.md
5cce0f14475a25a7edadcddb5e29f02ed5d66ea797cd05311d51c2ea67a95999  COMPACT_PROMPT.md
68aeb35661f4067431d3532af5fd8b2690c4aa14d75934056d93b53e79e529fe  COMPOSITION.md
02d5268b97054f09f3ecae56bb13e07e88ef9e2ebfa54805ba3e67b21cc6e48d  CONTINUOUS_IMPROVEMENT.md
f523fa86ea9148f5a8eeaaff595ad5ce30c61897f2db9fe51b400bd1e2eaeded  GLOSSARY.md
e6f29d05f54a2977e792bdb2846717537e8e10fbf1cd2e8a3a7bfde5e1e2e878  GUIDE.md
3f20396e09c726de3918a2bf37ee49e9ea5bdfa23328fd7c016bd2dc4c6de505  HOST_ADAPTERS.md
b06f6e41ccdd18b433d4afc46ef6e1466313bc1a5b886aab88156e1d7b3f4827  LAUNCH.md
24f80b93fb8113f90d2af6705631e7491fdd18e56477109e6b2ac724225d114b  MASTER_PROMPT.md
13e057a95461cbd4ad3c9631ce1aa894516f434df51fc33831eeaf2dfbec810a  MERGE_DECISIONS.md
e430e19e750b644f875c842d0aea766c1b74300b5bc364bbe88d744523de086a  MIGRATION.md
dd3dc82c4139ca8e1f9ade7ad64b5421f7fa83314e3be499bca9becb881e0cc2  PRACTICAL_PLAYBOOKS.md
76c17298464e760e17242978dae14f11367e61adcb2327831dee83dcb839482a  PROFILES.md
e7ef3cab9268dca85528d991d54617aebd332bc3d75c1e450c379f76880b0185  PROJECT_TEMPLATE.md
121581a13ac3f7f275ffa655608073603f2d5a5eced99e9a7de88bf981bddf95  README.md
1f96f9958680328f039281e7eb9d6acfed61935dfbcc6ed5f3492f693e863a4d  RESEARCH_AND_CHANGES.md
de49f62ed88bc38241a2ad1bde8d8011ac920b4de86442da4e8c938245587505  SKILL.md
fb7a45caacb263b9d704aa642e7a4acdc8681fd877eab5d9d8ed669852e04900  UI_DESIGN_PROTOCOL.md
ce0ca5fd7d8379dac2473e2f1e2b7e6df1badcf7ead4e2f36140cbbbe4082b8a  UI_REVIEW_PLAYBOOK.md
62912d3e3145df9ac163ee24bca53eefe1227d21bef5e1fa5f5d80b088bcb5f8  VALIDATION.md
41dc497aaea42c633b0cee72dce260741cdcde5050587217ba731e06da218c99  WORKFLOW.md
f9ff2a3382d82557840b67947df16674a63581f720ba5c9490639b42fdcd4f00  WORKFLOW_CONFIGURATION.md
246d24735f74c4a4055d89ee1f7a452ae1829ca4911964300f4f6d234bcc8966  evaluation/SCENARIOS.md
9a4531fbe568bc006fb015abd6ac06e9fe3b01314e0855b39ff11459bb535d60  examples/CONFIGURATIONS.md
a0be26abfa3ad4fa873975f23b26e7573bde9dc1caab645c13e3872094a909fc  references/ADVICE_REGISTER.md
8fb5ee4c06ca579d7de1b82e1084511d25468af7412ccaf37dc975c31b8a8009  references/ENGINEERING_ADVICE_MAP.md
c3c140348ff30b427d2b50a20785df47c01b5f5d826d799429b3d63cfa88e560  research/01_GENERAL_DRAFT.md
cdfc79839aa0aa593ddb54a9336708e9fb504875037c8e09d3fcf5e6222efd45  research/02_FIRST_RESEARCH_REVISION.md
d1d35fb49e5931b928f10623cfa4315a51727f3d8d141c8e3c86b2b8b77de15d  research/ARCHITECTURE_DECISIONS.md
a875d734dda21c9bf0580fe38618459f1031210696e08a494f3bc5d775bf8dc4  research/AdaptiveAgentWorkflow-pre-v4.3.zip
c06b7aca8936140da3e168d1f3eb20aa3536e14654c3f82d8aa460d429fdb0e7  research/CHANGE_SUMMARY.md
d8addc4c48310afdf503c1b08c5068ab209defc0f925cf317a54dd038863af3d  research/EVIDENCE_BASE.md
cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831  research/EXPERIMENT_CONTRACT.md
4bac8e5fd39318b7346ddd30c105df13955c8b111b861456ddf0ab111ea5c1d9  research/OPEN_QUESTIONS.md
860638be8400b9820cf3c6e2972df55765b101cc3a0a23aff15a6d124d96bb88  research/RC2_CHANGES.md
60481eefffb53da3401dd1e91f1b3d1cc7bdea2fbaa3c9d2446a4a71e30cb38d  research/REVIEW_RECONCILIATION.md
c9533a49fb8a563d6a220ebc2ae4499e89898dceeab3a5a4853b294e49ebada3  research/TRACEABILITY.md
f915e6bac8c28e88a9b4ab43df96c4e060ebd63eae6dfa32155d417e260ff825  research/build_ablations.py
72baff0f8cde1d6fd64a26d0f33639c32598e2cd32fd0931a2301979955bcd08  research/document-check-results.json
7da109a1db9fc55024b0a8423e671f249b202c81b571fd1f71300a5708cee44d  research/merge-check-results.json
1a32c989ee85632585dfdc9dc5a1b567b0a739e54d88cc9bcdacb1884b2a98b5  research/reviews/01-fresh-context-review.md
5a91921c4ee5fd67c540a69900d0e43a2086f49bb881980cc7c87d0c95006e7a  research/reviews/02-verification-review.md
2c2e8eed04587186f95d4dc5c90e981fcdf5bc09ae9a67f3b986684427d958e0  research/run_rc2_checks.py
c6cbd49b001b53d8d335658b5fb7875277b588b09732e3a3452131da6eb85820  research/v4.3-check-results.json
ae90c98b6cec0c92db3b7b2ddcd8ae73856e1b84f9acdfcf8b5b84735f3419e1  research/v4.3-plan.md
a43fdf7791e00f3cbe29ee60c5f863dca7c4345b088291d71ca3b8abf03cefb5  research/validation/arms.json
769ef4725cfe35930e671331ba2fd8833216c9eff996ec17df8a51c336280ba8  research/validation/rc1-history/arms.json
0c63a309ea16837815062fd84ff9b49a36f6d7d4b69b42ab2a706edf44dbb3be  research/validation/rc1-history/rc1-checks-20261118T204117Z.json
33a7da3e8775916d2368e87bda4b7d7d597eb0207dfda1512d0469b9a32c337c  research/validation/rc1-history/superseded-freeze-1/FREEZE.md
70fcd8b4324ffeafd37a4f3d18700223ca6104cabc6b165bf6a6acd0af993db6  research/validation/rc1-history/superseded-freeze-1/arms.json
19ba913096e915e198f5604f196449008352269df43526258ee46f5c8f3568f6  research/validation/rc1-history/superseded-freeze-1/rc1-checks-20261118T202040Z.json
c75d50949791c131d8ed2c978640686b3c4c723e81740334f05f600f53820816  research/validation/rc1-history/superseded-freeze-2/FREEZE.md
9ff356cab1360c76458bdc6c32dadcf3deede95c57719af79acf07c13381cfe9  research/validation/rc1-history/superseded-freeze-2/arms.json
5fca07d48a88bea4fb3a36137c688b450a5ad06fc397d304288103c081cee546  research/validation/rc1-history/superseded-freeze-2/rc1-checks-20261118T202324Z.json
d7b228ca944715272c7f61959e93975103758bb05e2b13f50a1ac5020bb4b8d9  research/validation/rc2-checks-20261119T131948Z.json
42467f04d85c359907520ff204014b4096dfc030d94bf5674514aa2d354ddb3f  tools/composition.py
731693d54dbd86d12944cf8c643e2914adcb19c01b60eb1e4d92d845bf046014  tools/documents.py
c9fd222ab9ab6855468ef93cf848e8db9434e0b79cce39d2aea4f67911d2ffe1  tools/portability_patterns.txt
```
