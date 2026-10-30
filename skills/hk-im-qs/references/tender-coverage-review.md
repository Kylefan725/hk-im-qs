# Reconcile tender obligations, service periods and quotation coverage

Use with [review-tender](../playbooks/review-tender.md) for a material scope, payment or quotation finding. Apply only the checks relevant to the assigned package. This is an original working checklist: it creates no contractual obligation, payment right, standard percentage or technical acceptance criterion. The existing [guide provenance](guide-provenance.json) remains limited to its named secondary methods; the adopted project sources control the finding.

## Keep one traceable finding

Reuse existing obligation and payment-question IDs. For a new standalone review, assign working IDs and identify them as internal. For each material finding retain:

`requirement and source -> applicability/scope -> responsible party -> quantity basis -> service period -> payment position -> quotation coverage -> consequence -> action/owner`

Keep the source document tree and revision, commercial package, programme package/window and any host record membership distinct. Similar package names do not establish a mapping. GI means Ground Investigation; GIMP means Ground Improvement. Do not transfer a GI allowance, inherited requirement or period into GIMP or another document tree without cited applicability and any local override.

- **Requirement:** cite the current file/revision and physical page, printed label, clause, drawing detail or sheet/cell as applicable. Retain conflicting evidence rather than selecting the convenient source.
- **Applicability and responsibility:** identify the source-backed package, work stage and party. If responsibility is unclear, leave it open; do not allocate it merely because another package has no price.
- **Quantity:** retain value, unit, denominator, scope, revision and basis. Distinguish contractual BQ quantity, scheduled requirement, drawing-observed count, accepted map count and estimating assumption. A missing quantity is unknown (`null` in structured output); a cited zero is a different fact. A source table quantity does not establish surveyed locations or accepted installed assets.
- **Period:** retain the original starting and ending conditions, frequency and affected IDs. Record monitoring, maintenance and equipment rental separately, including unknown bounds.
- **Payment:** use `included`, `separately_payable`, `unclear_allocation` or `outside_package`, with the supporting preamble/item/clarification or an explicit evidence gap. Requirement, cost and payment entitlement are separate questions.
- **Quotation coverage:** identify the quote/revision/item, inclusion, exclusion, limit or unresolved wording. Missing quote coverage is not an agreed tender exclusion or zero cost.
- **Consequence and action:** explain the affected scope, quantity, service period, duplicated allowance or unquantified exposure. Name the evidence or decision needed, owner and affected records.

Keep source confidence separate from commercial readiness. Use Confirmed, Inferred, Unclear or Missing where the host supports those evidence classifications; retain its existing vocabulary otherwise. `READY_FOR_QS_REVIEW` remains a supported draft, not accepted interpretation or authority to issue.

## Check both directions

| Comparison | Forward check | Reverse check |
|---|---|---|
| Specification/drawing and BQ | Where is each applicable requirement measured or included? | What current requirement and quantity basis supports each relevant BQ item? |
| BQ and quotation | Does the quote cover the bill's unit, denominator, period and inclusions? | Does every quoted item or qualification map to required, optional, duplicated or outside-package scope? |
| Quotation and operating obligations | Can the quoted attendance, data service, equipment and end duties support the required operation? | Is every applicable operating duty covered, excluded, limited or still unpriced? |

Use the same finding/coverage record across these checks. An item already included in installation cannot become another payable readings item merely because the supplier prices readings separately. Retain that supplier cost when it is relevant to the internal estimate and flag the potential overlap. Do not delete an exclusion or select a cheapest complete quote while a material gap is unpriced.

## Investigate lifecycle and interfaces from the actual scope

| Prompt | Evidence to seek |
|---|---|
| Mobilisation and baseline | Required visits/moves, access and possessions, baseline timing and acceptance, repeat baseline after relocation |
| Supply, installation and commissioning | Ownership/rental, drilling/casing/seals, survey control, power/connectivity, submissions, calibration and witnessing |
| Monitoring and data service | Required observations, attendance, checking/reporting, upload versus sampling, retention/export and alert duties |
| Maintenance and change | Maintenance start/end, calibration, damage/replacement, relocation, standby and emergency attendance responsibilities |
| Removal and handover | Final readings, removal versus retained operation, reinstatement, data/as-builts, equipment ownership and acceptance |

These are search prompts. Record not applicable, not specified, unreadable or unresolved with a reason where material; checklist coverage cannot establish that a duty exists. Inspect boundaries between I&M, GI, GIMP, survey control, drilling/casing, power/connectivity and site access without assigning them by abbreviation alone.

For recurring duties compare three separate records: required monitoring, required maintenance and quoted rental. Preserve each start/stop trigger and minimum/partial-period rule. A rental end before the maintenance trigger can expose a scope gap even when routine monitoring ends earlier. A works planning window is not automatically any instrument's attendance period. Preserve daily, fortnightly, fixed-count and event-triggered duties exactly; do not convert fortnightly to twice monthly or a fixed count into a recurring interval.

## Keep financial evidence and scenarios distinct

Retain submitted prices and literal source totals with their currency, scope and period. Deduplicate the same allowance before reporting a supported subtotal. List unknown costs and disputed payment positions separately; a supported subtotal is not the complete tender price.

Only when useful to the requested decision, show a derived scenario with cited inputs, units, formula, assumptions and `CALCULATION_ONLY` status. Separate it from source totals and supported contractual subtotals. A rate multiplied by an assumed duration is neither a quoted total nor evidence of entitlement. Missing rates or period boundaries leave the affected amount unknown. Use [estimating](../playbooks/estimate-and-compare-quotes.md) for detailed rate-building; do not invent a market rate to finish this checklist.

## Check original evidence and refresh affected findings

For critical conclusions and material ambiguities, inspect the original page/table or workbook cells, including headings, units, continuation notes and exclusions. Retain physical PDF page versus printed label and sheet/cell locations. Record unreadable pages, hidden-sheet review gaps, candidate/reference dispositions and any omitted source unit. A negative search, valid JSON or agreement between readers does not establish absence or correct interpretation.

Obtain an independent source check for those conclusions when the host supports it. Give the checker the source and proposed finding without a preferred answer. Record the checked source/revision and outcome. If a critical interpretation cannot be checked, retain the specific open action; do not label it professionally accepted.

When a source, quote, drawing or applicability changes, reopen affected findings/decisions and refresh dependent quantities, periods, comparisons and outputs. Keep prior positions and unaffected current findings. Reuse the same scoped question when its basis is unchanged; similar wording in another tree does not make it the same question. Return changes through the host in embedded mode.
