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
