# Review a tender or quotation scope

Use for tender/quotation compliance, missing scope, unclear interfaces and RFIs. A request solely to compare prices can start with estimate-and-compare-quotes and use only the scope checks it needs.

## Inputs

Obtain the relevant issued tender documents, BOQ/preambles, specifications/drawings, clarifications/addenda, programme and quotations or scope statements. Use established project facts from the current run. Read only the selected domains; a narrow scope query does not require every tender discipline to be re-reviewed.

Read [project basis](../references/project-basis.md) first. Use the [source register](../references/source-register.json), [measurement map](../references/measurement-sources.md) and [cost/contract references](../references/cost-contract-sources.md). Review the supplied documents; do not silently invent exclusions to make a quote appear complete.


## Steps

### 1. Establish the tender baseline

In embedded mode, use the host's document index and return missing evidence or revision conflicts to the host. For standalone work, create an index of the relevant tender/order, subcontract conditions, referenced main-contract extracts, BOQ/schedule, preambles, specification, drawings, plans, programme, clarification replies and addenda. Record issue/revision/date and conflicts. Do not combine superseded quantities with revised specifications.

Treat a tender addendum as a revision to the tender basis. In embedded mode, keep it within the host's addendum review. Do not infer a post-award variation or compensation event unless that separate assessment is requested.

Identify scope mode, employer/main-contractor responsibilities, whether design is included, tender return requirements, rate/price validity and quote currency/base date. Distinguish fixed lump sum, remeasurement, schedule-of-rates, activity schedule, target-cost or bespoke arrangements. Do not turn an internal BOQ into a remeasurement right where the contract does not provide one.

For a subcontract, inspect the incorporation and flow-down clauses and exact documents furnished. A named main contract is not proof that every upstream condition, deadline or risk transfers unchanged. Separate subcontract notice recipients/time limits from the main contract. Screen applicable payment legislation using `DEVB-SOPO`; do not assume universal coverage or that contractual SOPP and statutory adjudication are identical.

### 2. Reconcile scope in both directions

Check the specification/drawings against the BOQ, the BOQ against the supplier/subcontractor quote, and the quote against programme/operating obligations, then check each relationship in reverse. Use [the tender coverage checklist](../references/tender-coverage-review.md) for material findings, lifecycle duties and service-period mismatches. Record source-backed responsibility or an explicit unresolved interface. Use internal IDs clearly labelled as working IDs, not standard SMM codes; reuse the host's existing IDs in embedded mode.

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

### 3. Test bill coverage before proposing extras

Read relevant units, measurement, itemisation and inclusive coverage together, including the particular amendments. For investigation instrument installations, check `CEDD-SMM-1992` 2.27–2.30. An activity shown in the cost build-up may already sit within the installation or other bill rate.

Distinguish four findings:

- `included`: a required activity clearly included in an existing payable item.
- `separately_payable`: a required activity with a clear separate bill item.
- `unclear_allocation`: a required activity whose payment allocation is unclear.
- `outside_package`: scope supported as outside the requested package. Record an optional alternative explicitly; do not imply that it is a required extra.

Do not label all unlisted activities as variations or all listed quantities as guaranteed. Do not convert missing pricing coverage into an agreed exclusion without written clarification. Record any proposed qualified quote, the requirement it conflicts with, its cost effect and the approval needed before issue.

### 4. Compare quotations on a common basis

Normalize physical quantities, scope, duration, frequency, ownership, site attendance and deliverables before comparing totals. Show tendered totals and explicit comparison adjustments separately. Preserve unpriced items as unknown; do not set them to zero or fabricate market allowances.

When a rate, arithmetic or coverage discrepancy affects the comparison, read [pricing anomalies](../references/pricing-anomalies.md). Keep recalculated arithmetic separate from the submitted tender price.

Use [cost estimation](estimate-and-compare-quotes.md) for rate build-ups. For each adjustment retain supplier evidence or a labelled scenario. Show base, programme extension and frequency-change sensitivities if these are material. Confirm whether a supplier's “month” means calendar month, minimum rental block or another period.

### 5. Produce focused RFIs and risk actions

Use this RFI structure:

`ID | document/clause/drawing | inconsistency or missing definition | proposed interpretation (if supportable) | quantity/rate/programme consequence | requested response | owner | status`

Examples of precise questions:

1. “Item IM-07 is per month. Does one unit cover the complete system or each accepted instrument, and what starts/stops the service period?”
2. “Please identify the amendment separating routine readings from the inclusive installation coverage, or confirm the intended rate allocation.”
3. “Who provides and pays for the borehole required by piezometer P-03, and does the installation item include grout/seals/headworks?”
4. “If treatment is paused, which monitoring, maintenance and standby duties continue, and how is an instructed extension valued?”
5. “Is the specified five-second requirement sensor sampling, upload or complete valid observation delivery? Which acceptance test establishes it?”

These are sample working item IDs and questions, not statements about a real tender.

### 6. Reconcile the review and prepare the requested response

Check each material finding against its actual document/revision and avoid duplicate RFIs for one missing definition within the same applicability scope. Reconcile scope/quantity/pricing assumptions with any supporting measurement or estimate. Inspect original evidence for critical conclusions and material ambiguities under the tender coverage checklist; record unresolved source checks. Keep source totals, CALCULATION_ONLY scenarios and unquantified exposure separate. In embedded mode, return the assigned findings and proposed clarifications for the host to reconcile and publish. Otherwise produce the requested review or draft clarification with practical owners/actions; do not issue correspondence unless explicitly authorised.

## Outputs


Lead with the supported pricing basis, significant unresolved decisions and estimated exposure only where evidence permits quantification. Provide:

1. Document/edition basis and scope responsibility matrix.
2. BOQ-to-specification-to-quotation coverage schedule.
3. Comparable quotation table with adjustments and unpriced gaps.
4. Prioritised RFIs, commercial assumptions and change scenarios.
5. A short checklist of evidence needed for an authorised quotation/award decision.

Use `CALCULATION_ONLY`, `NEEDS_SOURCE` and `READY_FOR_QS_REVIEW` per row. A small unresolved interface need not stop unrelated supported quantities, but do not claim the entire tender is settled while material scope/payment definitions remain open. Prepare correspondence as a draft; issuing it requires explicit user instruction.

## Completion checks

- Every material finding traces source/revision, applicability, responsibility, quantity basis, period, payment position, quote coverage, consequence and action, or names the specific missing link.
- BOQ, specification, quotation and operating obligations are reconciled in both directions for the relevant package, using the same finding IDs.
- Included activities, separately payable items, unclear allocations and optional scope remain distinct.
- Monitoring, maintenance and rental denominators/start-stop obligations, GI/GIMP interfaces and responsibility for shared services are resolved or identified as open.
- Critical source checks and material unreadable/hidden/omitted-source limitations are explicit; changed sources reopen affected findings without discarding unaffected work.
- Comparison adjustments use evidence or CALCULATION_ONLY scenarios; unresolved inputs remain NEEDS_SOURCE and supported draft findings are READY_FOR_QS_REVIEW.
- The requested review and focused RFIs are complete, with no unsupported claim that the whole tender is settled or correspondence has been sent.
