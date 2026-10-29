# Prepare or check a progress valuation

Own the requested payment application, valuation reconciliation or certificate arithmetic. Use measurement and change assessment as supporting steps while retaining one cumulative ledger.

## Inputs

Read [project basis](../references/project-basis.md), [valuation rules](../references/valuation-rules.md) and [cost/contract sources](../references/cost-contract-sources.md). Use only relevant domain references selected by the router. Obtain the valuation cut-off, contract/payment basis, adopted items/rates, accepted records, prior certificates, prior applications and cash receipts as distinct records, and applicable deduction/release rules. Do not require a full tender re-review if those inputs are already established.

## Steps

1. **Establish the payment basis and cut-off.** Identify the actual contract and options, amendments, period, claimed/certified status, valuation mechanism and source of each deduction or addition. Do not infer remeasurement from the existence of a BOQ or convert subcontract obligations from a named main contract without incorporation evidence.
2. **Reconcile completed work to evidence.** Reuse a checked quantity ledger or run the necessary [measure-quantities](measure-quantities.md) steps. Separate work done, technical acceptance, contractual eligibility and arithmetic. Trace I&M service periods, GI intervals and treatment records to IDs and accepted evidence. Flag missing records, outages, disputed quantities and incomplete services using the actual assessment rule.
3. **Assess changed work separately.** Run [assess-change](assess-change.md) for an extension, instruction, changed frequency or other disputed scope; keep original obligations, supported changes and unresolved candidates separate. Do not include a priced scenario in the supported valuation merely because its arithmetic is correct. Record provisional/claimed treatment only if the user's requested application and contract support that presentation.
4. **Calculate the cumulative valuation.** Apply evidenced rates, inclusions, retention, releases, advance recovery and other adjustments once to the correct base. Reconcile gross and net cumulative amounts, previous certificates and this-period certificate. Separate prior certified-but-unpaid cash from the current valuation; never subtract cash received instead of previous certificates when calculating the current certificate.
5. **Check the actual payment schedule.** Independently recompute material quantities, rates, adjustment bases and totals. Trace changes since the preceding application and prevent a repeated claim for the same point, period or installed asset. Check rounding and units. Obtain a second review for a substantial or ambiguous valuation when available, using source records and the produced schedule.
6. **Deliver the requested draft.** Return the current application/reconciliation, explain supported versus unresolved rows and identify material missing evidence. Prepare any covering correspondence as a draft unless the user explicitly authorised sending it. Do not claim certification or approval to proceed with works.

## Outputs

Provide a schedule of `item | cumulative quantity/value | previous certified amount | current amount | evidence | adjustment/deduction basis | status`, plus a separate cash reconciliation if requested or material. Use `CALCULATION_ONLY` for an arithmetic scenario, `NEEDS_SOURCE` for missing eligibility/rate evidence and `READY_FOR_QS_REVIEW` for supported draft rows. Report the supported subtotal, unpriced/unresolved amounts and their effect without silently combining them.

## Completion checks

- Work quantities, accepted service periods and rates trace to the adopted basis and current records.
- Changes carry their own evidence and are allocated once to the original or changed work.
- Cumulative gross/net amounts, current valuation and previous certificates reconcile; prior cash shortfalls are separate.
- Retention, release, recovery and any deduction use supplied or verified rules, not generic percentages.
- The actual schedule has been checked; unsupported rows remain visible rather than being labelled a fully settled account.
- The deliverable is a QS review draft with the user's requested cut-off and format.
