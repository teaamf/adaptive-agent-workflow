# Freeze record: 4.4-rc1

Version 4.4-rc1 research record. Frozen 18 November 2026, after reconciliation of the fresh-context review and of the verification review (`REVIEW_RECONCILIATION.md`). **Frozen means identified, not adopted.** 4.4-rc1 is an experimental candidate; 4.3 remains the stable version. No trial of the experiment has been run.

This record supersedes two earlier freezes made the same day, both reopened before any trial. The first (tree `24377c7d…c25c`) was reopened under the session instruction to continue rather than defer, to cut the compact tier from 10,821 to 10,150 bytes by wording alone and to lower its ceiling to 10,500 bytes; its record is in `research/validation/superseded-freeze-1/`. The second (tree `616f45dd…07f5`) was reopened to fix the ten defects found by the verification review, under a stopping rule set before that review: one round, one new freeze, then stop. Its record is in `research/validation/superseded-freeze-2/`. The second record described its tree hash as a sort of path strings, but its scripts sorted Windows path objects, which ignore case (finding N-03); its hashes reproduce only with that order.

Any change to a file listed below after this point makes a new candidate, which needs a new freeze record. Under CONTINUOUS_IMPROVEMENT C2, changing the contract after the first trial also needs a new contract version and a recorded reason.

## Identities

All hashes are SHA-256. A tree hash is the SHA-256 of the lines `<file sha256>  <relative path>`, one per file, sorted by the POSIX relative path in Unicode code-point order (case-sensitive, the same on every platform), joined with newlines and with no trailing newline (the `manifest()` functions in `run_rc1_checks.py` and `build_ablations.py`). `__pycache__` folders are skipped.

| Object | Identity |
|---|---|
| Candidate tree, every file except this one (55 files) | `c9c951079fea1f4c8bfebb8bf5cafdfc97264b97eb07e45b8420d9ab727179d3` |
| Candidate tree as tested by the controls and the arm build (before the current results and this file were added) | `31cc09cc445c28feff07979329741acad14ede0dca0dc84c0b726e9d8a90988d` |
| Experiment contract `research/EXPERIMENT_CONTRACT.md` | `cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831` |
| 4.3 baseline `releases/4.3-baseline/SHA256SUMS` | `2059d8b7f102352a1162b17da518159e23b64b178d38ee0c4de00b31c3183c55` |
| 4.3 baseline tree (all 33 files, including SHA256SUMS) | `581b7530f34f82e5fd60f455bc914b72d6bf3c07b66cca514165574327b876c4` |
| Control results `research/validation/rc1-checks-20261118T204117Z.json` | `0c63a309ea16837815062fd84ff9b49a36f6d7d4b69b42ab2a706edf44dbb3be`; 41 records, all passed: True |
| Arm summary `research/validation/arms.json` (includes each arm's per-file manifest) | `769ef4725cfe35930e671331ba2fd8833216c9eff996ec17df8a51c336280ba8` |
| First review text `research/reviews/01-fresh-context-review.md` | `1a32c989ee85632585dfdc9dc5a1b567b0a739e54d88cc9bcdacb1884b2a98b5` |
| Verification review text `research/reviews/02-verification-review.md` | `5a91921c4ee5fd67c540a69900d0e43a2086f49bb881980cc7c87d0c95006e7a` |

## Arm packages

Built by `research/build_ablations.py` under one packaging rule (excluded from every arm: `research`, `evaluation`, `__pycache__`, `*.pyc`, `SHA256SUMS`, `RESEARCH_AND_CHANGES.md`, `MERGE_DECISIONS.md`, `VALIDATION.md`, `MIGRATION.md`). Each edited full tree passed its own `documents.py check` before packaging. The last column counts residual-text patterns searched for, with no hits. The build is deterministic: two builds gave identical package hashes.

| Arm | Package tree hash | Files | Residual patterns clear |
|---|---|---|---|
| A1-baseline-4.3 | `ffd66a0c907f41ca7c7f43114a7f266dc28928a37b15331fb4c630bd8d259cf6` | 20 | 0 |
| A2-rc1 | `14641be852438f0cc230e70e36482e46cfb64f830d4d323dd85b4d3b364aa412` | 24 | 0 |
| A3-no-attribution-scope | `e29fd432e7a0e9bc036609bec07d20bb0c203d6fe2aa48c4c506b6f6d8236354` | 24 | 10 |
| A4-fixed-scaffolding | `e6017ab46fcb71dff6bde149f9665041567c4d33fd94839ef206325db2f60206` | 24 | 8 |
| A5-no-independent-review | `df5d290d3f9751840a155c95afb20a645a9cdef7e80a8cf3099cabf7b03d68a1` | 24 | 8 |

A0 receives no package (host defaults only).

## Per-file manifest of the candidate

```text
e1032e5e5a0b3b8c367acba9486a719d3e326bf241161c2714e4598341ba0f89  AGENT_INTERACTION.md
eea6ea35353ea8b63d29230080560ca1d91f260aacecba65c1ebac1f72fe201a  COMPACT_PROMPT.md
c462fafa342a1e6df1977cc470bb164f8a94c20133cbdd5be95782775bf878fa  COMPOSITION.md
9dd64541a1b8a9c76cc4becbd4453759ae5657feaf96e96342d5b4c5c856365b  CONTINUOUS_IMPROVEMENT.md
e85a9d91df04733e22646c229a7eda3491280ce05208d5f0c551bd24df7f0b87  GLOSSARY.md
e6f29d05f54a2977e792bdb2846717537e8e10fbf1cd2e8a3a7bfde5e1e2e878  GUIDE.md
24fb5b9c92b91aede8f194941e7763bb41dd83682f1fe8dde80fc83ed15f5b70  HOST_ADAPTERS.md
ee7edace43a23efaa760716feb3b935e0aff9681379700fc7c49f4569fad0603  LAUNCH.md
60fb0597edd7cdd2d4ccd6df8ce24913b7b25c87fc0143605b1123d5d358b67f  MASTER_PROMPT.md
13e057a95461cbd4ad3c9631ce1aa894516f434df51fc33831eeaf2dfbec810a  MERGE_DECISIONS.md
a37bccdaaad4a5790baadf2d3e9c7d07b21bc9fcbe457e8a6df39a640f5ed901  MIGRATION.md
e0b2ff0010a1fe0951801071af43bb523926178c1c84d966d3b6fd1fd972e22e  PRACTICAL_PLAYBOOKS.md
5d40b577717fe64c99de1384069b0095a609588c7179746f2c54867365173c7f  PROFILES.md
e7ef3cab9268dca85528d991d54617aebd332bc3d75c1e450c379f76880b0185  PROJECT_TEMPLATE.md
acab840112d96f047cf21e6b7628fb68be2cf15929e6a6e6fb69a712ea7577c6  README.md
ffb9c740ff5b75720d0c04edbd724a9381729ad711310aa7e9d033a1dbe6ea9c  RESEARCH_AND_CHANGES.md
91b40aad4d2a7f1d14a598feb8abe9c588f5442199403b6a321963a2732ab2a6  SKILL.md
fd8d4b5474268cbc5f65c8d38649ce0c04266d9446060b4b5092d03b1ba78902  UI_DESIGN_PROTOCOL.md
c44d7398d0e5b9b668744cad07556738639f9faffd1d16739ff27d3b8c551c9e  UI_REVIEW_PLAYBOOK.md
549066c891ca6059d3be41bec0495928aabd51454a9d3ce7d9e4a9db74e0af12  VALIDATION.md
e5dbba8492f74b6bd1d90739541d702af6511afbd00f30ec7aafd4fc6240a1d5  WORKFLOW.md
855c088ff5fb8dac4e36254f4a394e322acbf6bd92caae2a8ded21c3bcdfa95c  WORKFLOW_CONFIGURATION.md
246d24735f74c4a4055d89ee1f7a452ae1829ca4911964300f4f6d234bcc8966  evaluation/SCENARIOS.md
90d0244a9b29665d5da3ffd9d8610543f109a623b46ec6205b4c2dd8fc0b9f8a  examples/CONFIGURATIONS.md
a0be26abfa3ad4fa873975f23b26e7573bde9dc1caab645c13e3872094a909fc  references/ADVICE_REGISTER.md
d0a7111f191ae69bf209d0e1e22b204649b3bed743577019c445cd9de4099d72  references/ENGINEERING_ADVICE_MAP.md
c3c140348ff30b427d2b50a20785df47c01b5f5d826d799429b3d63cfa88e560  research/01_GENERAL_DRAFT.md
cdfc79839aa0aa593ddb54a9336708e9fb504875037c8e09d3fcf5e6222efd45  research/02_FIRST_RESEARCH_REVISION.md
d1d35fb49e5931b928f10623cfa4315a51727f3d8d141c8e3c86b2b8b77de15d  research/ARCHITECTURE_DECISIONS.md
a875d734dda21c9bf0580fe38618459f1031210696e08a494f3bc5d775bf8dc4  research/AdaptiveAgentWorkflow-pre-v4.3.zip
c06b7aca8936140da3e168d1f3eb20aa3536e14654c3f82d8aa460d429fdb0e7  research/CHANGE_SUMMARY.md
d8addc4c48310afdf503c1b08c5068ab209defc0f925cf317a54dd038863af3d  research/EVIDENCE_BASE.md
cc526ca554f30e27730e1b23dec26ed0332678d26ffc3cfff0ad1257044ae831  research/EXPERIMENT_CONTRACT.md
4bac8e5fd39318b7346ddd30c105df13955c8b111b861456ddf0ab111ea5c1d9  research/OPEN_QUESTIONS.md
60481eefffb53da3401dd1e91f1b3d1cc7bdea2fbaa3c9d2446a4a71e30cb38d  research/REVIEW_RECONCILIATION.md
c9533a49fb8a563d6a220ebc2ae4499e89898dceeab3a5a4853b294e49ebada3  research/TRACEABILITY.md
114eccb20c370d851c091f24200b13ed83a09700f8fef08caf141cf72b54828f  research/build_ablations.py
72baff0f8cde1d6fd64a26d0f33639c32598e2cd32fd0931a2301979955bcd08  research/document-check-results.json
7da109a1db9fc55024b0a8423e671f249b202c81b571fd1f71300a5708cee44d  research/merge-check-results.json
1a32c989ee85632585dfdc9dc5a1b567b0a739e54d88cc9bcdacb1884b2a98b5  research/reviews/01-fresh-context-review.md
5a91921c4ee5fd67c540a69900d0e43a2086f49bb881980cc7c87d0c95006e7a  research/reviews/02-verification-review.md
df298eefad323abef937f748073d4ecf344c3325b3b1e3e57937ea58b2e2d767  research/run_rc1_checks.py
c6cbd49b001b53d8d335658b5fb7875277b588b09732e3a3452131da6eb85820  research/v4.3-check-results.json
ae90c98b6cec0c92db3b7b2ddcd8ae73856e1b84f9acdfcf8b5b84735f3419e1  research/v4.3-plan.md
769ef4725cfe35930e671331ba2fd8833216c9eff996ec17df8a51c336280ba8  research/validation/arms.json
0c63a309ea16837815062fd84ff9b49a36f6d7d4b69b42ab2a706edf44dbb3be  research/validation/rc1-checks-20261118T204117Z.json
33a7da3e8775916d2368e87bda4b7d7d597eb0207dfda1512d0469b9a32c337c  research/validation/superseded-freeze-1/FREEZE.md
70fcd8b4324ffeafd37a4f3d18700223ca6104cabc6b165bf6a6acd0af993db6  research/validation/superseded-freeze-1/arms.json
19ba913096e915e198f5604f196449008352269df43526258ee46f5c8f3568f6  research/validation/superseded-freeze-1/rc1-checks-20261118T202040Z.json
c75d50949791c131d8ed2c978640686b3c4c723e81740334f05f600f53820816  research/validation/superseded-freeze-2/FREEZE.md
9ff356cab1360c76458bdc6c32dadcf3deede95c57719af79acf07c13381cfe9  research/validation/superseded-freeze-2/arms.json
5fca07d48a88bea4fb3a36137c688b450a5ad06fc397d304288103c081cee546  research/validation/superseded-freeze-2/rc1-checks-20261118T202324Z.json
24faf711da94cd495196234556bf058470ec2478f5233be83484d6de49ecedf9  tools/composition.py
1b354ecbe4b86d7902465b62d6bd8242240fceaf7645d3e800dc4cc324d53f04  tools/documents.py
c9fd222ab9ab6855468ef93cf848e8db9434e0b79cce39d2aea4f67911d2ffe1  tools/portability_patterns.txt
```

## How to verify

From `candidates/4.4-rc1/`, recompute each file's SHA-256 and compare with the manifest above; then recompute the tree hash with the rule stated under "Identities". Rebuild the arms with `python -I -X utf8 -B research/build_ablations.py --out <dir outside the package>` and compare the package hashes. The control run can be repeated with `research/run_rc1_checks.py`; a new run produces a new run-stamped file and does not replace the recorded one.
