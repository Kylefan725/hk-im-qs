# Ground improvement with instrumentation — Hong Kong QS

Use this domain reference only for a package selected by [hk-im-qs](../../SKILL.md). Apply its relevant constraints within the chosen playbook; it is supporting guidance, not an additional worklist. Do not execute every numbered section or produce every listed schedule automatically. Load another domain only where a real package interface needs it.

Read [project basis and evidence controls](../project-basis.md) first and [ground-improvement sources](../ground-improvement-sources.md) before selecting technical references. Read [instrumentation and monitoring](instrumentation-monitoring.md) when the selected task needs the instrument/service schedule.

Limit this reference to commercial and measurement work for instrumented ground-improvement packages. Treat named methods below as possible project-adopted methods, not as methods all covered by one Hong Kong standard. The workflows and examples are original; they do not replace technical specifications or create payment rights.


## Contents

- [1. Fix the treatment and commercial basis](#1-fix-the-treatment-and-commercial-basis)
- [2. Build a scope matrix before pricing](#2-build-a-scope-matrix-before-pricing)
- [3. Maintain three linked ledgers](#3-maintain-three-linked-ledgers)
- [4. Resolve method-specific measurement questions](#4-resolve-method-specific-measurement-questions)
- [5. Tie instruments to treatment stages](#5-tie-instruments-to-treatment-stages)
- [6. Normalise tenders and build the estimate](#6-normalise-tenders-and-build-the-estimate)
- [7. Prepare valuation and change records](#7-prepare-valuation-and-change-records)
- [8. Check with a transparent geometric example](#8-check-with-a-transparent-geometric-example)
- [9. Deliver and apply status](#9-deliver-and-apply-status)

## 1. Fix the treatment and commercial basis

Obtain the selected method, approved treatment layout, investigation baseline, trial requirements, acceptance criteria, monitoring plan, pricing schedule, adopted measurement method and particular preambles. Record the responsible designer and the authority that can release hold points or accept treatment.

| Basis field | Minimum record |
|---|---|
| Treatment | Zone and element IDs, design revision, target strata, plan boundary, top/bottom levels, method and sequence |
| Instrumentation | Instrument IDs, locations/depths, purpose, stage, baseline, monitoring duration, reporting requirements and package owner |
| Verification | Trial versus production requirements, tests, acceptance lots, interpretation basis, reviewer and release evidence |
| Commercial | Item wording, bill unit, quantity basis, inclusions, method-related costs, change mechanism and adoption evidence |
| Constraints | Access, working platform, services, sensitive receivers, water/spoil management and programme restrictions affecting the package |

Use `CEDD-SMM-1992` only to the extent adopted and relevant. Identify a missing project-specific rule where the chosen treatment has no established billing basis. Use `CEDD-GS-2020` for the applicable technical scope; retrieve the relevant text instead of treating every ground-improvement process as geotechnical grouting.

Do not select a treatment method, prescribe engineering dosage/pressure, set trigger limits or decide adequate strength, permeability or settlement performance. Obtain those decisions from the responsible engineer and approved project documents. Continue scoped quantities and pricing comparisons with the resulting uncertainty identified.

## 2. Build a scope matrix before pricing

Split responsibilities across the improvement contractor, investigation/testing provider, I&M provider and main contractor. Assign each cost once.

| Workstream | Commercial definition to resolve | Evidence / interface |
|---|---|---|
| Mobilisation and setup | Number of setups, moves, platform/access, utilities and removal included | Site plan, programme and package boundaries |
| Pre-treatment work | Instrumented investigation, surveys and baseline monitoring included | Investigation schedule, asset register and baseline acceptance |
| Trials | Trial locations, treatment, instruments, tests, reports, changes and disposal | Trial plan, results, instruction and approval for production |
| Production | Treatment zones/elements, depth ranges, sequence and method-specific activities | Adopted bill descriptions and installation records |
| Routine QA | Materials/process records, surveys, samples and tests included or separately billed | Inspection/test plan and acceptance-lot mapping |
| I&M services | Supply, installation, calibration, baseline, operation, reporting and maintenance | One shared instrument/service schedule with named owner |
| Hold periods | Monitoring, plant/staff, maintenance and verification during waiting periods | Defined duration/events, programme and contract provision |
| Close-out | Final verification, records, removal, handover and making good | Agreed deliverables and completion/acceptance records |

Separate trial treatment that becomes permanent work from sacrificial trials. Confirm whether trial quantities transfer to production totals or remain a separately priced item; never count both without an express basis.

## 3. Maintain three linked ledgers

1. **Treatment ledger:** `zone/element_id | method | revision | date | plan_geometry | top/bottom_levels | drilled_length | treated_length | pass/stage | material_records | calculated_quantity | acceptance_lot | instruction_id`.
2. **Monitoring/verification ledger:** `instrument_or_test_id | treatment_zone | purpose | stage | baseline_id | period | raw_record | processed_report | quality_issue | technical_review | hold/release_reference`.
3. **Valuation ledger:** `bill_item | source_clause | unit_definition | measured_quantity | adjustment | proposed_bill_quantity | rate_source | amount | previously_valued | current_delta | status | unresolved_action`.

Join these by stable IDs rather than informal descriptions. Preserve rejected, superseded and reworked records without including them automatically in accepted or payable totals.

## 4. Resolve method-specific measurement questions

### Geometry, passes and treatment boundaries

- Separate borehole/penetration depth from active treatment depth, and both from column or treated-ground volume.
- Calculate non-overlapping ground geometry from the adopted limits. Record treatment-element overlap, interlocking zones, variable levels, exclusions and interfaces explicitly.
- Keep gross process output and net unique treated ground as separate measures. Do not call either the bill quantity until the agreed rule selects it.
- Record every pass, lift, stage and repeat operation. Repeated work in the same ground does not increase its unique geometric volume; payment per pass requires a supported unit definition.
- Retain theoretical, as-executed and technically accepted quantities separately. Survey differences, overruns and actual consumption do not alone establish entitlement.

### Mixing and grouting

- For mixing, record element identity, penetration and treatment intervals, overlap geometry, process logs and verification lots. Resolve whether the bill measures an element, treated length, area, volume or another expressly defined basis.
- For grouting, distinguish drilling, installation of injection equipment, injection stages, grout input, losses/returns, testing and monitoring. Check whether these are bundled or separately priced.
- Reconcile delivered, batched, injected, returned and discarded quantities where records permit. Do not equate grout input with the geometric volume of improved soil or convert between them using an invented factor.
- Separate approved additional treatment from corrective re-treatment. Identify instruction, cause, technical disposition and contractual valuation basis before including additional value.

### Granular columns, compaction and consolidation treatments

- For granular columns or compaction, distinguish installation positions, depth intervals, treatment footprint, process passes and material consumption. Select the contractual unit rather than deriving it from the plant log format.
- For vertical drainage, preloading or vacuum treatment, distinguish drain installation, treatment area, surcharge/temporary materials, equipment, operation period and monitoring period where the project adopts them.
- Define start/stop events and any period proration. Do not infer completion from elapsed time, fill placement or a single sensor trend when technical acceptance is outstanding.
- Treat design loading sequence, treatment effectiveness and instrumentation adequacy as engineering decisions. Price their expressly required resources and duration without inventing design criteria.

## 5. Tie instruments to treatment stages

| Stage | Scope and evidence to obtain | QS control |
|---|---|---|
| Before treatment | Instrument readiness, calibration, datum/pre-treatment survey and accepted baseline | Confirm setup versus continuing-service allocation |
| Trial treatment | Process records, monitoring and trial verification linked to trial zones | Identify trial-only assets and reusable assets |
| Production | Treatment logs linked to movement, pore-pressure or other specified observations | Keep reading frequency separate from the service billing unit |
| Hold/review | Engineer's trigger/hold instruction, observations, response and release record | Track resources and time; resolve entitlement separately |
| Verification | Post-treatment survey/tests and engineer's interpretation by acceptance lot | Separate test execution, technical acceptance and payment status |
| Post-treatment | Required continuing observations, maintenance and removal/handover | Confirm end event and responsibility for extensions |

Use project-specified settlement, heave, lateral movement, pore-pressure, vibration or other monitoring as applicable. Obtain approved alert/action and response arrangements from the engineering team. For marine/reclamation work, use the scope-qualified PWDM references; do not apply them to every inland treatment project.

If records show a trigger breach or unresolved technical rejection, identify it promptly for the responsible engineer and follow the approved response process. Do not issue a restart, treatment-acceptance or safety conclusion from this QS workflow.

## 6. Normalise tenders and build the estimate

- Compare bids against one common scope, treatment geometry, method, programme and I&M service period. Retain each bidder's exclusions and qualifications alongside the adjusted comparison.
- Isolate mobilisation, trials, production, instruments/services, verification, hold-period resources and close-out. Do not spread excluded scope into a headline treatment rate without showing the adjustment.
- Require quoted-rate date, currency, unit, quantity band, validity and relevant assumptions. Obtain vendor evidence for specialist equipment, calibration, data services or rental costs.
- Quantify plausible scope/programme scenarios using stated assumptions. Keep risk allowance separate from already priced tasks and from a claim for an actual event.
- Identify possible duplication between an all-inclusive treatment rate, a separate I&M bill, and a specialist subcontract quotation. Produce a responsibility/inclusion matrix and resolve the overlap.

## 7. Prepare valuation and change records

Reconcile cumulative treatment, accepted lots, instrument-service periods and previous valuation by item. Present changed quantities and rates separately; retain instruction and notice records under the selected contract procedure.

For failed tests, lost data or re-treatment, distinguish an invalid test, a valid adverse result, a contractor correction, a changed design and instructed additional scope. Record the technical determination and contractual allocation; do not presume either automatic extra payment or automatic non-payment for all cases.

Separate normal recurring monitoring from instructed extended monitoring. Record why the extension occurred, what service continued, its actual period, the responsible party's instruction and the applicable pricing mechanism.

## 8. Check with a transparent geometric example

Assume two rectangular treatment zones of uniform 6 m thickness: A = 10 m × 8 m and B = 8 m × 6 m. Their overlap is a 2 m × 6 m rectangle through the full thickness.

- Gross zone volumes: A = 480 m³ and B = 288 m³; overlap = 72 m³.
- Unique geometric treatment volume: 480 + 288 − 72 = **696 m³**.
- Two passes over this same ground leave **696 m³ of unique ground**, not 1,392 m³. A contract may define another process-based billing measure; retrieve that definition before valuing it.
- Label the arithmetic `CALCULATION_ONLY`. Mark the unresolved billing conversion `NEEDS_SOURCE`; do not claim the example is a CEDD measurement rule or evidence of treatment acceptance.

## 9. Deliver and apply status

Return the package basis, scope/interface matrix, treatment quantity workings, instrument/verification schedule, tender or valuation comparison, reconciliation and concise unresolved-action register.

Use `NEEDS_SOURCE` for an unresolved adopted rule, unit, inclusion, instruction or material technical disposition. Use `CALCULATION_ONLY` for supported geometry or scenarios pending that evidence. Use `READY_FOR_QS_REVIEW` only when the draft's adopted basis, records, calculations and interfaces are traceable and material uncertainties are resolved; it does not certify engineering acceptance or payment.

Keep supported rows progressing and unresolved amounts outside confirmed totals. Name the exact missing document, reviewer and effect on price or quantity so the next action is concrete.
