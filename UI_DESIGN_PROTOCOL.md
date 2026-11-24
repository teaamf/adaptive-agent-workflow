# UI design protocol

Version 4.3. Apply to user-facing work within the governing workflow. This is an operational synthesis, not a claim that every design principle is a universal law. Use the relevant sections progressively; do not load a catalogue of hundreds of tips into every worker.

## U1. Establish the user outcome before the screen

For each material journey record: requirement ID; audience and abilities; real context of use; desired outcome; frequency and consequence of failure; starting state; completion evidence; recovery; and uncertainty. Distinguish source-backed observations from assumptions. A fictional persona can organize hypotheses but is not a study participant.

Separate three dimensions: immediate perceptual clarity and appeal; successful, recoverable behavior; and lasting trust, meaning and ownership. Define observable criteria for each relevant dimension. Do not reduce them to one weighted score that can conceal a serious failure. Familiarity and perceived ease can be useful hypotheses; they cannot establish correctness or accessibility.

Freeze critical task goals before viewing competing designs. Use goal-based scripts such as “find last month's invoice and send a copy to your accountant,” rather than telling the participant which controls to press. State whether success means unaided completion, completion with help, or a deterministic technical outcome. Set any time/error thresholds from context or baseline evidence; do not invent “industry-standard” numbers.

## U2. Integrate discovery and delivery

| Stage | Useful output | Decision to move forward |
|---|---|---|
| Understand | Small UX contract, evidence/assumption list, priority journeys | Uncertainty and intended outcome are explicit |
| Structure | Information architecture, domain vocabulary, route/state map | People can locate, act, recover and leave; permissions and data flows are understood |
| Explore | Low-cost alternatives for an unresolved consequential choice | Options address the same task and constraints; independent proposals frozen before comparison |
| Choose | One coherent direction with rationale and rejected tradeoffs | Task and accessibility hard gates survive; design owner integrates rather than averages votes |
| Prototype | The lowest-fidelity artifact capable of testing the actual uncertainty | No claim exceeds prototype fidelity; interactions are exercised when the question concerns behavior |
| Implement | Reusable components/tokens and complete relevant states | Executable slice meets the same contract; mocks and missing states labelled |
| Verify | Independent task, assistive, visual and trust findings | Required findings resolved on exact candidate; uncertainty remains visible |
| Learn | Small decision or improvement record | New evidence changes the relevant decision; no endless aesthetic churn |

Discovery may run ahead of delivery where dependencies allow, but cannot bypass the project's gates or expand its authorized scope. A local copy change may need only its task context and rendered check. An unfamiliar authoring model may need prototypes, research and alternatives. Prefer two meaningfully different proposals when uncertainty warrants exploration; neither “two” nor any fixed team size is a universal requirement.

## U3. Minimal design contract and records

Store these in existing project ledgers, with stable IDs and revision bindings:

```text
journey_id, requirement_ids, audience/context, evidence_or_assumption
start_state, goal, success_observation, error/recovery, supported_variants
priority/risk, acceptance_criteria, measurement_method, evidence_needed
design_decision, alternatives/tradeoffs, candidate_id, reviewer, findings
```

Maintain a compact screen/route/state map, selected-pattern decisions, token/component definitions and a coverage matrix. Each pattern decision names the user problem, fit, tradeoff and how to test it. Do not instantiate every named pattern. Canvas-plus-palette, progressive disclosure, overview/detail, direct manipulation and conventional forms are options selected by context.

For a new visual direction, record a short art-direction brief: intended character, typography hierarchy, color roles, density, imagery/icon approach and why they suit the audience. Use a few relevant visual references when authorized and useful; distinguish inspiration from licensed assets. Evaluate the actual implementation against that direction so generic defaults do not replace a deliberate design. A small fix should preserve an established coherent system unless evidence justifies changing it.

Reuse vocabulary and interaction conventions across the product. Tokens express typography, spacing, color roles, geometry, focus, motion and density; use the host's native implementation rather than forcing a particular token standard. Components include semantics and behavior, not just appearance. Record intentional exceptions. Preview and generated output must share the same authoritative model where practical; verify equivalence at the actual runtime boundary.

## U4. Behavior, states and recovery

For each meaningful action consider idle, selected/focused, busy, partial, empty, success, invalid, failed, permission-denied, offline, cancelled and restored states. Mark genuinely inapplicable states with a reason; this is not a requirement to invent loading spinners for synchronous controls. Define action availability, feedback, focus destination, data persistence and recovery for applicable transitions.

Use clear labels, contextual validation, useful error messages and bounded choices. Preserve entered work across interruption where promised. Provide undo or a suitable reversible alternative for consequential authoring operations. Destructive confirmation is proportional to actual loss; do not add confirmation to every action. Back, cancel, close, undo, save draft and publish must have distinct and predictable meanings. Do not claim success before the effect occurred.

Support first-time discovery and repeated expert use without forcing one group through the other's path. Reveal advanced functions progressively without removing required capabilities. Keep frequent targets and navigation stable; automatic rearrangement must not destroy spatial learning. Test interruption, resize, orientation and changing context. Make gesture-only, drag-only or sensory-only actions reachable through appropriate alternatives.

## U5. Verify three complementary views

**Rendered view:** inspect actual output at declared viewport/device, locale, theme and scale. Check hierarchy, density, grouping, alignment, wrapping, clipping, target overlap, visible focus, contrast and motion. Screenshots must identify candidate, state, dimensions, font scale, locale and rendering environment. Mockups do not prove the implementation matches them.

**Semantic/assistive view:** inspect labels, roles, values, states, traversal and announcements. Exercise supported assistive technology on critical journeys, including custom canvases and dynamic state changes. Static labels and automated scanners cannot demonstrate all runtime behavior.

**Outcome view:** interact and observe the user's intended effect outside the component's own success log. Confirm navigation, publication, saved data, text delivery, undo, cancellation and error recovery. A screenshot can show a button; it cannot prove the button performs the correct action.

Choose a risk-based matrix rather than an uncontrolled Cartesian product. Cover every critical journey and distinct interaction mechanism; add representative viewport/device classes, large text, RTL/long translations, light/dark/high-contrast modes if supported, keyboard/switch/screen-reader paths and relevant failure states. Record uncovered combinations. Repeat shared-component checks where context changes behavior. Sample coverage does not prove untested combinations.

For screenshot regression, freeze stable data, fonts, scale and rendering conditions. Review baseline updates independently; do not accept a new image merely because the implementation changed. Mask only justified nondeterminism, never important labels, focus or task outcomes. Pixels, semantics and runtime checks can disagree; investigate the discrepancy rather than voting it away.

Use [UI_REVIEW_PLAYBOOK.md](UI_REVIEW_PLAYBOOK.md) for material visual refinement: explicit readiness and capture failure handling, evidence-bound findings, bounded iterations and recovery that preserves user edits. A focused UI fix needs only its relevant render and behavior checks. Supported states and themes come from the project, not a fixed screenshot matrix.

## U6. Accessibility profile and evidence limits

Freeze an applicable accessibility profile: target platform, standard/guidance versions, mapped criteria, test methods, supported assistive technology, devices and allowed exceptions with rationale. Recheck current official platform guidance when beginning implementation. Web WCAG criteria, informative WCAG2ICT guidance and native platform recommendations are distinct inputs; do not claim that one automated scan or a native app screenshot establishes universal WCAG conformance.

Select native, web or other medium-specific accessibility guidance for the actual deliverable. Record units, supported assistive mechanisms and runtime constraints explicitly. Dense or unusual interfaces need a justified accessibility strategy and tested alternatives; do not silently waive a criterion or transfer geometry thresholds between incompatible units and platforms. No specific operating system, input method, hardware or device matrix is imposed by this module.

Distinguish these evidence categories in reports:

| Category | Can support | Cannot establish alone |
|---|---|---|
| STATIC_CHECK | Declared properties, lint findings, code structure | Runtime usability |
| RUNTIME_TOOL | Observed behavior under a specified test/environment | Representative human experience |
| MODEL_CRITIQUE | Plausible concerns and design hypotheses | Human preference, lived experience, statistical evidence |
| HUMAN_EXPERT | Expert inspection of specified tasks/criteria | All audiences' real-world outcomes |
| OBSERVED_HUMAN | What named participant groups did under recorded conditions | Universal usability or complete standards conformance |

Where human research is possible, recruit relevant participants, use accessible non-leading tasks, record consent and minimize personal data. Report task results, assistance, errors, recovery and qualitative feedback separately. Include disabled people where relevant; do not generalize one participant's assistive setup to everyone. Participant recruitment, payment and external contact need their own authorization.

Absence of participants does not block unrelated implementation. The contract states which human studies are release gates and which are desired learning. If a required study is unavailable, record the exact gate as blocked; otherwise deliver the declared technical assessment with a human-validation limitation. Never manufacture participant quotes, satisfaction scores or research coverage.

## U7. Emotional quality and trustworthy interaction

Use tone, hierarchy and feedback suited to context: clear and calm under error or stress, efficient during repeated work, exploratory where reversible. Optional delight must not delay essential actions or obscure consequences. Permit control over sound, haptics, animation and other sensory feedback where applicable; retain alternative feedback channels.

Anxiety narrows attention [ED011, ED015, ED021, ED022]. For stressful, time-critical or safety-relevant flows:

- show only the essential information and keep the critical state continuously visible;
- make the safe action the obvious one;
- do not require recall or creative problem-solving at the moment of stress;
- rehearse rare critical paths [ED017].

Treat every interruption as a cost to the person's attention [ED084–ED086]. Notifications, modals and prompts must earn their place, and people should be able to control when they are available.

Make ownership and persistence legible. Show what is a draft, what is active, what is shared and what will be lost. Explain system limitations and uncertain outcomes at the point they affect a decision. An AI-enabled feature, if in scope, must make its scope, correction and cancellation available; this does not add AI features to products that do not need them.

Do not optimize compulsive use, fabricate urgency or social proof, exploit vulnerable users, infer emotional state from appearance, or substitute anthropomorphic reassurance for evidence. Trust is evaluated through understandable effects, correction, privacy and user control. Measure satisfaction only when there is a defensible method and actual observations.

Treat numerical folklore and aesthetic theories as optional hypotheses. “Seven items,” golden ratios, gender stereotypes, facial appeal and similar claims do not become quality gates. Prefer contextual tests of comprehension, target acquisition, error rates and user goals. A beauty score cannot cancel a blocked task.

## U8. Independent design judgment

Give reviewers the task contract, artifact and relevant factual evidence before the designer's persuasion. Freeze initial findings, then reconcile known defects and design rationale. The design owner resolves coherence; the supervisor applies release gates. Reviewers identify observable failures and tradeoffs rather than redesigning to personal taste.

For comparative model judging, hide author/model identity, use the same task and rubric, control irrelevant verbosity and reverse order on consequential comparisons. Require cited observations for each finding. Calibrate model judgments against task results and human-reviewed examples when available; disclose absence of calibration. Disagreement or order sensitivity is uncertainty to resolve, not something a larger vote necessarily fixes.

Keep quality dimensions separate. Correctness, privacy and mandatory accessibility are gates; aesthetic preference informs selection among eligible designs. Stop iterating when the frozen contract is met and no material defect or bounded learning question justifies another cycle. A new hypothesis enters the improvement backlog rather than continually moving the finish line.

Agent-generated interfaces fail in characteristic ways. Check for each explicitly:

- generic default styling in place of the recorded art direction;
- the happy path implemented with empty, error, loading and permission states missing;
- controls that render but do nothing or do the wrong thing;
- inconsistent components across runs;
- previews that differ from the real output [UP199];
- claims of visual quality that were never actually rendered.

Render and interact before judging.

## U9. AI-enabled and autonomous features

Apply this section only when the product itself contains AI-driven or autonomous behavior. The following is condensed from Microsoft's 18 human-AI interaction guidelines, together with the related advice [ED093–ED115, DI122]. Use it as a checklist of observable behaviors, not as a score.

| Moment | Required behavior to design and test |
|---|---|
| Before use | Make clear what the feature can do and how reliably it does it; do not imply capabilities it lacks |
| During use | Show relevant context; time suggestions to the task; make invocation, dismissal and correction efficient; match social norms; avoid reinforcing social bias |
| When wrong | Scope back when uncertain; explain why it acted where that aids correction; make undo and override obvious; keep human judgment for consequential outcomes |
| Over time | Remember recent interactions and adapt cautiously; ask for feedback at a useful grain; convey the consequences of the user's choices; offer global controls; notify people when behavior changes |

Autonomous actions taken on a user's behalf need visible intent, a preview or confirmation proportional to consequence, cancellation and an audit trail [ED109, ED111]. Do not present artificial social behavior as real understanding or emotion [ED096, ED102]. If emotional state is inferred at all, treat it as a weak signal requiring consent [ED097]. Test failure cases as deliberately as success cases.
