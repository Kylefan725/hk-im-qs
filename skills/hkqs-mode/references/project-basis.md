# Project basis and evidence controls

Use this shared reference when the [hkqs-mode router](../SKILL.md) or selected playbook needs project scope, measurement or evidence controls. Populate only fields material to the current request; a narrow document question does not require a complete project setup. Read the relevant domain reference and source passage on demand. Treat these instructions as an original QS workflow, not as the text of an official standard or a certification of compliance.

## Scope boundary

Cover instrumentation and monitoring (I&M), associated instrumented ground investigation, and ground improvement packages involving instruments. Assign `I&M_ONLY`, `GI_WITH_I&M`, or `GROUND_IMPROVEMENT_WITH_I&M` to each relevant package from its actual scope. A single request may cover several scope modes; retain package IDs and a separate adopted measurement/contract basis for each instead of forcing one mode onto the whole request. In I&M-only work, cost drilling, treatment, access or reinstatement only where it belongs to that package; show interfaces owned by others. Do not expand to unrelated building trades, whole-building elemental cost planning or general civil works.

Keep design decisions with the responsible engineer: do not invent instrument locations, accuracy requirements, trigger/action/alarm limits, acceptable movements, treatment pressures/dosages, acceptance criteria or permission to resume works. Extract approved requirements, price their consequences and flag omissions. If an actual exceedance is supplied, highlight it against the provided plan and its stated escalation route; do not present a commercial assessment as clearance to continue work.

## 1. Establish the project basis

Start from the documents supplied. Record missing fields; ask only for information that changes the current decision. Use the [project basis template](project-basis-template.yaml) and [output templates](output-templates.md).

| Field | Record |
|---|---|
| Scope | Project, employer, main contractor/subcontractor, public/private sector, applicable specialist scope mode per package, location and output purpose |
| Contract | Form, edition, execution/acceptance dates, pricing mechanism, relevant options, special/additional conditions, amendments and stated precedence clause |
| Measurement | Exact standard title, edition, incorporated corrigenda, BOQ preambles and particular measurement amendments for **each package** |
| Technical scope | Specifications, revisions, drawings/models and status, schedules, addenda, instructions and interface responsibilities |
| Monitoring basis | Instrument/point/hole/channel IDs, installation and acceptance dates, baseline and routine stages, reading/visit/upload/report frequencies, monitoring end and maintenance end |
| Cost basis | HKD unless instructed otherwise; quote/base date, programme, quantity denominator, supply/rental/ownership terms, rate inclusions and source |
| Authority | Document issuer, revision, supplied file/page/clause, date verified, contractual incorporation and unresolved conflicts |

Use SI units, but obtain the **billing unit and measurement precision** from the adopted rules. Currency and SI defaults do not establish a rule for measuring an item. Ask before any conversion where the original basis is uncertain. Respond in the user's requested language; use Traditional Chinese when Chinese is requested and retain official English titles and clause references.

Do not assume all documents on a publisher's website are incorporated in the contract. Identify applicable mandatory law separately; a contract cannot automatically override it. For contractual document conflicts, read the actual precedence and discrepancy provisions. If unresolved, flag the affected item and responsible reviewer instead of inventing a universal order of precedence.

## 2. Select the Hong Kong reference route

| Task/context | Reference route | What must be confirmed |
|---|---|---|
| Civil/GI measurement | `CEDD-SMM-1992` and particular preambles | Adopted corrigenda, exact item coverage and project departures; do not substitute UK CESMM |
| GI technical scope | `CEDD-GS-2020` Section 7 Part 2; `GEO-GEOGUIDE-2` and `GEO-GEOGUIDE-3` | Adopted specifications, investigation plan, logging/test standards and instrument borehole interfaces |
| I&M technical scope | `CEDD-GS-2020` Section 7 Part 6; `LESB-ESPG-2025` Chapter 7 | Actual instrument schedule, approved I&M plan, specified accuracy/frequency, baseline, records and maintenance |
| Ground improvement with I&M | Relevant parts of `CEDD-GS-2020`, project treatment specification and `GEO-TGN54-2024` where applicable | Method, trials, production/QA quantities, engineer-approved controls and instrument interfaces |
| Deep excavation monitoring | `GEO-PUB-1-2023`, especially Chapters 9–10 | ELS-specific guidance and adopted project controls; not a universal trigger table |
| Marine reclamation treatment | Applicable `CEDD-PWDM3-2023` / `CEDD-PWDM4-2026` | Marine scope and project incorporation; do not extend it automatically to land-based works |
| Government GCC contracts | `DEVB-CONTRACTS`, signed contract and `CEDD-PAH-2024` where applicable | Actual GCC family/year, special conditions, chapter revision and applicable law |
| NEC contracts | `DEVB-NEC-HK`, `NEC-ECC-HK` and project documents | Actual NEC generation/HK edition/family, options, Contract Data, Scope and ACC |
| Specialist/bespoke subcontract | Executed subcontract, order, BOQ, specification, incorporated main-contract documents | Express flow-down, precedence, notice recipient, payment basis and scope; do not import main-contract obligations automatically |

Keep technical requirements, internal cost components, payable BOQ items, contractual entitlement and statutory obligations distinct. A separate activity in a cost build-up is **not automatically a separately payable item**. In particular, inspect the adopted SMM Section 2 instrument-installation coverage before splitting maintenance and monitoring out for payment. Modern ADMS, telemetry and data-service items need their actual particular preambles/schedule; do not invent standard item codes.

## 3. Use evidence at the level it supports

Read the [source register](source-register.json) to find official documents and their access status. Its `verified_on` is a review date, not a perpetual claim of currency. For a new live task, recheck amendments, legal commencement/applicability and time-sensitive indices. Save the selected edition and observation period in the work record.

| Evidence level | Permitted use |
|---|---|
| `OFFICIAL_TEXT_REVIEWED` | Support the identified passage; retrieve the exact relevant page/clause before applying a rule. It does not mean the whole document was audited. |
| `OFFICIAL_METADATA_VERIFIED` | Support title, edition, availability or listed revision only. It cannot support a numerical deduction rule, legal deadline or entitlement. |
| `PROJECT_DOCUMENT` | Support a project-specific rule once its identity, revision, authority and incorporation are checked. |
| `UNAVAILABLE` | State the gap and request the specific document or authorised excerpt needed. |

For each material rule, record `source_id`, exact document edition/revision, clause or page, a short original explanation, applicability and the calculation affected. Distinguish assumptions and professional judgement from sourced rules. Do not invent clause numbers, standard item codes, numerical thresholds, lap/waste allowances, minimum deductions, default retention, notice periods, fee percentages or statutory scope.

**Source-text gate:** A catalogue reference to an NEC product or another licensed standard does not supply its text. Obtain a lawful project copy or the needed excerpt. Do not substitute Australian ANZSMM/ACMM provisions, a different NEC edition, or generic building measurement rules. Do not fetch unauthorised copies or redistribute source books or contract text.

## 4. Keep useful work moving

Apply status **per row or conclusion**, with a short reason and next action:

| Status | Meaning |
|---|---|
| `CALCULATION_ONLY` | Traceable arithmetic, geometry or a stated scenario; adopted billing rules/entitlement have not been established. |
| `NEEDS_SOURCE` | A specified missing source, input or unresolved conflict prevents the affected rule/valuation from being settled. Name exactly what is needed. |
| `READY_FOR_QS_REVIEW` | Sources, incorporation, inputs, calculations and scope interfaces support the draft. This is ready for professional review, not approval or certification. |

Continue supported rows and draft descriptions. Isolate uncertainty; do not block the whole BOQ for one missing detail. Never convert a provisional quantity into a conforming billed quantity merely because its geometry is correct. Put unresolved monetary amounts in a separate subtotal and label whether excluded, allowed provisionally or shown as a scenario. Do not silently count an unknown as zero.

Example: four monitoring stations operate as one system for six full agreed months. That is 6 system-months or 24 station-months under two different denominators. Use only the denominator in the relevant item; do not add both. A five-second upload interval describes a data service, not a billable reading unit unless the contract says so.

## 5. Load supporting guidance only when needed

Let the [hkqs-mode router](../SKILL.md) select the requested deliverable and playbook. Use this reference to constrain that work; do not choose a different task merely because a source or domain term appears in the request.

| Relevant package or decision | Supporting reference |
|---|---|
| Instrument/point schedules, baseline and recurring monitoring | [Instrumentation and monitoring](domains/instrumentation-monitoring.md) |
| Instrument boreholes and associated investigation/testing | [Ground investigation](domains/ground-investigation.md) |
| Instrumented treatment trials, production and verification | [Ground improvement](domains/ground-improvement.md) |
| Payment mechanisms, contract change evidence and cumulative reconciliation | [Valuation and change rules](valuation-rules.md) |

Read additional references only for an actual dependency. Reuse one shared evidence record across linked playbooks; preserve separate package rules and avoid repeating an intake already completed.

## 6. Deliver a reviewable result

Scale the response to the selected playbook and requested deliverable. A narrow document question can be a sourced answer with its applicability limits; do not generate a BOQ, estimate or valuation unless the task needs one. For a commercial work package, lead with the result and its status, then show the applicable parts below:

1. Project/edition basis, key source references and applicable document revisions.
2. Calculation or valuation schedule with dimensions, formulas, units, quantities, rate evidence, amounts and per-row status.
3. Inclusions, exclusions, measurement/contract deviations and package interfaces.
4. Reconciliation of totals, rounding, changes and uncertainty; do not add overlapping allowances twice.
5. A short action list naming the missing evidence, responsible person and decision it will resolve.

Use [output templates](output-templates.md) and the [measurement source map](measurement-sources.md). Read [GI references](ground-investigation-sources.md) or [ground-improvement references](ground-improvement-sources.md) only for those scopes. For cost and contract work read [cost/contract sources](cost-contract-sources.md). Present notices and certificates as drafts for the authorised person; do not issue, sign, submit or certify them without explicit user instruction and the required authority.
