# Bounded visual review and refinement

Version 4.4-rc1. Select for material UI polish, redesign or visual audit after establishing the user journey and supported variants in [UI_DESIGN_PROTOCOL.md](UI_DESIGN_PROTOCOL.md). A small UI fix needs a focused render and relevant behavior check. This procedure works with browser, native-app or other authorized rendering tools; it requires no particular language, model, framework or review service.

## V1. Freeze the review packet

Record the task goal, mandatory behavior/accessibility gates, visual direction, candidate and baseline identities, relevant states/variants, checks, review method, resource ceiling and stop condition. Choose a finite round/time/cost limit suited to the task before iteration. Required review comes from the assurance level; extra reviewers are optional and must be authorized. A single context can provide labelled first-party review where that assurance is sufficient.

Reuse the project's components and semantic design roles where they exist. Typography, spacing, geometry, focus, motion and interaction conventions should form a coherent system. Record a scoped exception when reuse cannot meet the user need. Prefer clear primary-action hierarchy, readable long content, distinguishable controls and restrained chrome. A particular color, spacing grid, radius formula, icon or component library is a project choice; none is universally banned or required.

Use references only when they resolve a concrete design question. Record source/date, the relevant principle and usage rights where applicable. References inspire direction; they are neither a requirement to copy competitors nor an outcome oracle. A baseline may contain known defects. Retain the small set of approved baselines/references and supporting evidence needed for review, using project storage/retention rules rather than forcing images into version control. Minimize private data and authorize any export to an external reviewer/service.

## V2. Capture trustworthy observations

Choose a risk-based subset of supported themes, sizes, text scales, locales, interaction mechanisms and failure states. Do not add unsupported themes or mobile targets merely to fill a fixed matrix. Loading and empty states are intentional test states, distinct from an unintentionally incomplete loaded-state capture.

For every required capture:

1. Identify the exact running/exported candidate, route/surface, fixture and intended state. Fix relevant data, time/randomness, locale, scale, fonts and renderer version where the tools permit it. Record uncontrolled variables.
2. Reach the state through the supported product controls or a documented test seam. Verify the actual selected theme, content, permissions and state after initialization. Forcing styling after load can hide a broken theme path; disclose any override and check the real path separately.
3. Wait for an explicit observable readiness condition with a bounded timeout, such as the expected record and enabled action. Confirm required fonts and assets loaded successfully where material. A navigation event, arbitrary delay, quiet network or absence of a spinner alone does not prove readiness.
4. Stabilize animations, caret, hover and other irrelevant variation when testing static appearance. Keep separate checks for motion, focus and loading behavior that those controls would suppress. Mask only justified irrelevant nondeterminism and record why.
5. Inspect the captured output. Missing files, wrong states, failed assets, unresolved readiness or unstable repeated captures produce a failed/incomplete observation. Preserve diagnostics; never swallow the failure and label the capture valid. Record candidate, fixture/state, environment, dimensions/scale, locale/theme, time, evidence reference and limitations.

Compare before/after under equivalent conditions. Renderer or environment changes need a justified new baseline or a qualified comparison, not an assumption of pixel parity. Pinning tools can reduce variability; it does not guarantee identical pixels on every machine. Live services that cannot be stabilized may need bounded manual observation with explicit limits.

Pair pixels with semantic/assistive inspection and the actual task outcome (U5). Check applicable loading, empty, overflow, invalid, failed and recovery paths. Include long dynamic content and relevant text enlargement. A screenshot cannot establish exact contrast ratios, keyboard operation, announcements, persistence or successful cancellation by itself; use the corresponding measurement or interaction. A source-only review may support implementation observations but leaves rendered quality unverified.

## V3. Critique, change and recheck

Use the least expensive adequate review first: mechanical checks and direct task observations, then targeted qualitative inspection. Obtain any required independent review before acceptance. Additional reviewers answer a specific unresolved question; they are not a default multi-model council.

Give reviewers the task, relevant facts and evidence with candidate/state identities. Withhold author identity, prior scores and the maker's persuasive narrative initially. For subjective scoring, reviewers receive rubric anchors but not the desired pass score; the decision owner retains the frozen acceptance criteria. Never hide task or mandatory accessibility requirements. Visual reviewers need the render; semantic or behavior reviewers may need implementation and runtime evidence. Freeze initial findings before reconciliation.

Use a short finding record, plain text or validated structured data:

```text
candidate/state, evidence location, observed defect or hypothesis
affected task/criterion, impact/severity, suggested correction
validation needed, confidence/limits
```

Check that the reviewer used the right evidence and returned valid, relevant findings. Missing/invalid output is an unresolved review, not a pass. Keep hierarchy, typography/readability, spacing/alignment, color/affordance and consistency separate where useful. Numeric ratings are optional subjective signals, not measured usability or universal release gates. A majority or median cannot cancel a demonstrated task failure.

Choose a small coherent set of actionable findings. Predict the improvement and possible regressions, edit, recapture affected views and rerun behavior/accessibility checks. Request a fresh critique when the evidence or unresolved question warrants it. Avoid repeating a full panel or optimizing to a decimal score without new evidence.

## V4. Recover and stop

Checkpoint before experiments and identify the agent-owned changes separately from existing user edits. When a change regresses a required outcome, preserve the failure and undo only that experiment using an inspected patch, isolated copy or project recovery mechanism. Verify the recovered state and affected checks. Never restore whole files or reset the workspace over unrelated work; uncertain ownership calls for reconciliation first. Git and automatic rollback are optional capabilities, not prerequisites.

Stop when the frozen contract is met and no material finding remains, or when the declared limit is reached. Repeated oscillation or nondeterminism triggers reassessment. At a limit, deliver the last verified candidate with unresolved findings and honest status; do not claim convergence or silently promote a failing experiment. New aesthetic preferences enter a bounded follow-up decision rather than moving the finish line.

Deliver candidate identity, relevant before/after evidence, behavior/accessibility results, resolved and open findings, uncovered variants and review limits. A score table is optional. A fresh session may help after context saturation using the factual handoff; it does not require a new branch, provider or restarted score chase.
