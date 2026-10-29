---
name: hkqs-tender-review
description: Review Hong Kong specialist tenders and subcontract scope for instrumentation and monitoring, instrumented ground investigation and instrumented ground improvement. Use to identify missing BOQ coverage, unclear monitoring duration/frequency, drilling/treatment interfaces, pricing risks, contractual flow-down and RFIs before quotation or award.
---

# Specialist tender and scope review

Read [hkqs-general](../hkqs-general/SKILL.md) first. Use the [source register](../hkqs-general/references/source-register.json), [measurement map](../hkqs-general/references/measurement-sources.md) and [cost/contract references](../hkqs-general/references/cost-contract-sources.md). Review the supplied documents; do not silently invent exclusions to make a quote appear complete.

## 1. Establish the tender baseline

Create a document index: tender/order, subcontract conditions, referenced main-contract extracts, BOQ/schedule, general and particular preambles, specification, drawings, I&M plan, treatment/investigation plan, programme, clarification replies and addenda. Record issue/revision/date and conflicts. Do not combine superseded quantities with revised specifications.

Identify scope mode, employer/main-contractor responsibilities, whether design is included, tender return requirements, rate/price validity and quote currency/base date. Distinguish fixed lump sum, remeasurement, schedule-of-rates, activity schedule, target-cost or bespoke arrangements. Do not turn an internal BOQ into a remeasurement right where the contract does not provide one.

For a subcontract, inspect the incorporation and flow-down clauses and exact documents furnished. A named main contract is not proof that every upstream condition, deadline or risk transfers unchanged. Separate subcontract notice recipients/time limits from the main contract. Screen applicable payment legislation using `DEVB-SOPO`; do not assume universal coverage or that contractual SOPP and statutory adjudication are identical.

## 2. Reconcile scope in three directions

Check the specification/drawings against the BOQ, the BOQ against the supplier/subcontractor quote, and the quote against programme/operating obligations. Assign one responsible package to each interface. Use internal IDs clearly labelled as working IDs, not standard SMM codes.

| Review area | Questions to resolve |
|---|---|
| Instruments and monitoring points | Correct types, ranges/accuracy, accepted equivalents, counts, locations, depth, spares, redundancy, control/reference points and shared systems? |
| Investigation interfaces | Who drills, logs, samples/tests, provides casing, installs instruments, seals/backfills, surveys and reinstates? What happens to an aborted/reused hole? |
| Ground improvement | Who provides trial area, rigs, treatment materials, production records, verification testing and repeat work? Is monitoring a prerequisite for each treatment stage? |
| Mobilisation and access | Number of mobilisations/rig moves, working platform/access by whom, possessions/permits, restricted hours, utilities and site support? |
| Installation and acceptance | Submissions, calibration, protection, commissioning, baseline, as-builts, witnessing and acceptance criteria? |
| Monitoring service | Defined system/point/instrument/visit/reading/month basis, start/stop triggers, programme stages, holidays, report cycle and partial periods? |
| Automatic/data services | Sampling versus scan versus upload intervals, valid observation requirements, power/connectivity, storage/retention/export, software licences, support and alert recipients? |
| Changes and interruptions | Added/replaced/relocated instruments, higher frequency, standby, emergency/night visits, delayed commencement, programme extension and remobilisation? |
| Maintenance and end obligations | Maintenance duration versus monitoring duration, damage allocation, calibration replacements, removal/reinstatement versus leaving operational equipment, ownership and handover? |
| Commercial terms | Payment evidence, valuation dates, retention/security/insurance if specified, variation route, notices, testing responsibility, exclusions and limitations? |

Technical adequacy and threshold selection remain with the responsible engineer. Request missing approved performance/trigger requirements instead of proposing a cheaper unsupported default. Do not assume every possible modern monitoring feature is required; mark “not specified” and ask only if it changes price or deliverability.

## 3. Test bill coverage before proposing extras

Read relevant units, measurement, itemisation and inclusive coverage together, including the particular amendments. For investigation instrument installations, check `CEDD-SMM-1992` 2.27–2.30. An activity shown in the cost build-up may already sit within the installation or other bill rate.

Distinguish four findings:

- A required activity clearly included in an existing payable item.
- A required activity with a clear separate bill item.
- A required activity whose payment allocation is unclear.
- An optional alternative or scope outside the requested package.

Do not label all unlisted activities as variations or all listed quantities as guaranteed. Do not convert missing pricing coverage into an agreed exclusion without written clarification. Record any proposed qualified quote, the requirement it conflicts with, its cost effect and the approval needed before issue.

## 4. Compare quotations on a common basis

Normalize physical quantities, scope, duration, frequency, ownership, site attendance and deliverables before comparing totals. Show tendered totals and explicit comparison adjustments separately. Preserve unpriced items as unknown; do not set them to zero or fabricate market allowances.

Use [cost estimation](../hkqs-cost-estimation/SKILL.md) for rate build-ups. For each adjustment retain supplier evidence or a labelled scenario. Show base, programme extension and frequency-change sensitivities if these are material. Confirm whether a supplier's “month” means calendar month, minimum rental block or another period.

## 5. Produce focused RFIs and risk actions

Use this RFI structure:

`ID | document/clause/drawing | inconsistency or missing definition | proposed interpretation (if supportable) | quantity/rate/programme consequence | requested response | owner | status`

Examples of precise questions:

1. “Item IM-07 is per month. Does one unit cover the complete system or each accepted instrument, and what starts/stops the service period?”
2. “Please identify the amendment separating routine readings from the inclusive installation coverage, or confirm the intended rate allocation.”
3. “Who provides and pays for the borehole required by piezometer P-03, and does the installation item include grout/seals/headworks?”
4. “If treatment is paused, which monitoring, maintenance and standby duties continue, and how is an instructed extension valued?”
5. “Is the specified five-second requirement sensor sampling, upload or complete valid observation delivery? Which acceptance test establishes it?”

These are sample working item IDs and questions, not statements about a real tender.

## 6. Deliver an actionable review

Lead with the supported pricing basis, significant unresolved decisions and estimated exposure only where evidence permits quantification. Provide:

1. Document/edition basis and scope responsibility matrix.
2. BOQ-to-specification-to-quotation coverage schedule.
3. Comparable quotation table with adjustments and unpriced gaps.
4. Prioritised RFIs, commercial assumptions and change scenarios.
5. A short checklist of evidence needed for an authorised quotation/award decision.

Use `CALCULATION_ONLY`, `NEEDS_SOURCE` and `READY_FOR_QS_REVIEW` per row. A small unresolved interface need not stop unrelated supported quantities, but do not claim the entire tender is settled while material scope/payment definitions remain open. Prepare correspondence as a draft; issuing it requires explicit user instruction.
