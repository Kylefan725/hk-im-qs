# Working output templates

These are original internal working formats. They are not official Hong Kong forms, standard item codes or contract certificates. Omit unused columns; keep evidence and uncertainty visible.

## Project basis header

`Project | package | purpose | contract/form/edition/options | measurement edition/corrigenda | particular preambles | specification revision | drawing/model revision | price date | currency | source verification date`

## Measurement / BOQ working schedule

| Item ID | Location/system | Description and scope | Drawing/model + revision | Dimensions/formula | Gross geometric quantity | Adopted rule/page | Adjustments and reason | Billing quantity/unit | Rate/evidence/date | Amount HKD | Status / action |
|---|---|---|---|---|---:|---|---|---|---|---:|---|
| DRAFT-001 | To identify | To describe | Required | Required | Unknown | Required | Unverified | Unknown | Unpriced | Unknown | NEEDS_SOURCE: identify missing rule/input |

Keep gross geometry and bill quantity in distinct columns. A unit in a working example is an assumption until verified. For a missing rate, leave the amount unpriced; show priced subtotal and unpriced scope rather than treating the row as zero.

## Source/rule decision log

| Decision ID | Source ID / document | Edition + revision | Clause / page | Access level | Project incorporation | Original summary of rule | Affected rows | Reviewer/status |
|---|---|---|---|---|---|---|---|---|

A metadata-only source cannot support a clause-level decision. For conflicting documents, record both positions and the identified precedence provision; escalate an unresolved conflict.

## Tender scope, payment and quotation coverage

For material tender findings, follow [the tender coverage checklist](tender-coverage-review.md). Use one record across the brief, working schedule and evidence appendix. In embedded mode, populate the host's existing fields and return any unsupported link as a gap.

`Finding/obligation/payment-question IDs | source tree + file/revision + locator | applicable commercial/programme package + window | requirement | responsibility | quantity value/unit/denominator/basis | monitoring/maintenance/rental period references | payment position + evidence | quote/revision/item + coverage/exclusion | consequence | action/owner | evidence state | commercial review status`

Use `included`, `separately_payable`, `unclear_allocation` or `outside_package` for payment position. Keep quantity basis and human acceptance separate. A source-supported zero differs from unknown. Preserve all sides of a scope, quantity or payment conflict.

Record each service period separately:

`Period ID | service | covered IDs | source/revision + locator | start trigger | stop trigger | stated duration/unit | frequency/fixed count/event | minimum/partial-period rule | quote coverage | unresolved action`

Keep monitoring, maintenance and rental rows distinct even when their dates coincide. Unknown bounds remain unknown; do not fill them from the overall works programme.

Present three financial groups: cited source totals/supportable subtotals with currency and allowance IDs; derived `CALCULATION_ONLY` scenarios with input citations, formula and units; and unquantified or disputed exposure. Never add a scenario or unknown amount into a supported contractual subtotal. Show source-check and revision status so a corrected finding refreshes every dependent projection.

## Cost plan and reconciliation

| Work package / element | Classification source/code | Cost/area scope | Quantity and unit | Base rate/source | Base cost | Time adjustment basis | Other identified allowance | Forecast | Confidence/action |
|---|---|---|---|---|---:|---|---:|---:|---|

Show base works, preliminaries, other distinct project costs, risk allowance and escalation separately where required by the selected methodology. Preserve any source-defined treatment of preliminaries. Reconcile previous approved baseline + documented scope/design changes + price changes + risk movements = current comparable forecast. State any exclusions from that reconciliation.

## Contract change and notice register

| Event ID | Contract branch | Instruction/event + date | Clause/ACC | Awareness/service evidence | Deadline basis | Entitlement status | Quantity/rate basis | Claimed | Assessed | Agreed/certified | Forecast treatment | Next action |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|

Derive deadlines from actual documents and applicable law, including day counting, service, amendments and exceptions. Distinguish notification, quotation, assessment and payment stages. A cost forecast is not an admission of entitlement; certified and paid are different states.

## Element crosswalk

| Source BOQ item | Amount | Target classification/version | Element/code | Source definition/page | Allocation fraction | Allocated amount | Exclusion/interface owner | Review state |
|---|---:|---|---|---|---:|---:|---|---|

Require allocation fractions per source item to total 1.00, or document the deliberately excluded portion. Check that allocations reconcile to the defined source total. Do not invent official code labels.

## Uncertainty / next actions

| Row/decision | Status | What is known | What is missing or conflicting | Effect on result | Required source/person | Next action |
|---|---|---|---|---|---|---|

Use only `CALCULATION_ONLY`, `NEEDS_SOURCE`, or `READY_FOR_QS_REVIEW` for working result status. Scope-screening or entitlement labels are separate fields. `READY_FOR_QS_REVIEW` is not permission to certify or issue a contractual document.
