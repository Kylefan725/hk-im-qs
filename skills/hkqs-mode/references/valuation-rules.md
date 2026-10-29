# Specialist valuations, changes and payment reconciliation

Use this shared reference for the [progress valuation](../playbooks/value-progress.md) or [change assessment](../playbooks/assess-change.md) playbook selected by [hkqs-mode](../SKILL.md). Apply only the sections needed for that decision and produce the calling playbook's required outputs; do not turn a payment reconciliation into an unsolicited change claim or notice.

Read [project basis and evidence controls](project-basis.md) first, then
[cost and contract sources](cost-contract-sources.md) and the
[source register](source-register.json).
Relevant sources: `CEDD-SMM-1992`, `CEDD-GS-2020`, `CEDD-PAH-2024`,
`DEVB-CONTRACTS`, `DEVB-NEC-HK`, `NEC-ECC-HK`, `DEVB-SOPO`,
`DEVB-SOPP-2021` and `CSD-CONSTRUCTION`. Confirm adoption and current applicability.
Prepare drafts for the authorised person; do not issue notices or certify payment.


## Contents

- [1. Identify the contract and payment mechanism](#1-identify-the-contract-and-payment-mechanism)
- [2. Assemble the valuation evidence](#2-assemble-the-valuation-evidence)
- [3. Measure progress and recurring services](#3-measure-progress-and-recurring-services)
- [4. Assess changes in two stages](#4-assess-changes-in-two-stages)
- [5. Preserve notice and payment deadlines](#5-preserve-notice-and-payment-deadlines)
- [6. Reconstruct cumulative payment](#6-reconstruct-cumulative-payment)
- [7. Deliver and reconcile](#7-deliver-and-reconcile)

## 1. Identify the contract and payment mechanism

Record contracting parties, subcontract tier, execution/acceptance dates, incorporated
documents, pricing mechanism, amendments, precedence provisions and relevant law.
Read the actual subcontract: main-contract terms are not automatically incorporated.
Distinguish quantities for pricing, quantities for measurement, activity completion,
milestones, time charges and reimbursable cost. Never assume a universal monthly entitlement.

| Route | Check before valuation or entitlement advice |
|---|---|
| Government GCC-based work | Actual GCC family/edition, SCC, preambles, instructions and rate provisions |
| NEC ECC/HK or other NEC form | Actual family/edition, main/secondary options, Contract Data, Scope, ACC and change mechanism |
| Bespoke/specialist subcontract | Express pricing, flow-down clauses, notice/service, approval and payment provisions |
| Statutory/contractual payment protection | Cap. 652 applicability or actual earlier SOPP terms; keep them distinct |

Use PAH as relevant administration guidance, not as an override of the selected contract.
Do not map every GCC variation/EOT automatically into an NEC compensation event.
Obtain authorised NEC text for clause-level conclusions; a publisher catalogue is insufficient.

## 2. Assemble the valuation evidence

| Work | Evidence to reconcile with the payable item |
|---|---|
| Instrument supply | Delivery, identity/serial, ownership/vesting and eligibility documents |
| Installation | Location, type, depth, installation record, drawing revision and acceptance |
| Calibration/commissioning | Calibration certificate, test results, acceptance and date |
| Monitoring service | Baseline/routine/event records, active dates, visits/data and required reports |
| GI drilling/testing | Signed logs, depth intervals, method/ground classification, samples and tests |
| Ground improvement | Treatment records, actual quantities, trials, QA/QC and acceptance records |
| Standby/remobilisation | Cause, instructions, dates, resources, availability and mitigation |
| Maintenance/removal | Work record, responsibility, authorisation and handover/reinstatement |

Record cut-off dates and quantities previously claimed, assessed, certified and paid.
Do not treat these stages as equivalent. Preserve the original and revised records.
Technical acceptance or a signed site record does not automatically establish extra payment.
Check whether items are deemed included in other rates by adopted preambles.

For adopted CEDD SMM Section 2 GI instrument items, check clauses 2.27–2.30 before
adding service lines: clause 2.30 already covers calibration, maintenance, readings and
the required records within the installation item. A separate internal cost component
does not become a separate payment. Check adopted amendments and the actual project item basis.

## 3. Measure progress and recurring services

Apply the adopted billing unit and source-backed measurement rule to evidenced progress.
Do not bill design quantities, sensor sample counts or database rows as payable work without
the contractual unit. Distinguish installed points, active points, channels and site visits.
For time-based services, verify commencement/cessation triggers, suspension, minimum
period, proration, frequency and required deliverables from the actual agreement.
Reconcile each instrument/service location to the billed period; avoid overlapping periods.
Separate supplied equipment, installed equipment, accepted systems and eligible stored
materials. Apply materials-on/off-site rules only when their requirements are evidenced.
Record rejected/defective work, rework and disputed quantities without silently writing them off.

## 4. Assess changes in two stages

First assess the contractual route and evidence; then calculate value under its pricing rules.
Register event ID, instruction/cause, date discovered, contractual clause, notice status,
baseline versus revised scope, programme effect, proposed valuation and approval state.
Keep notified, submitted, assessed and agreed/approved values separate.
For NEC, use the selected option's change valuation, cost components and fee provisions;
do not assume existing BQ rates or actual cost always determine a compensation event.
For GCC/bespoke terms, verify any existing-rate, analogous-rate, new-rate or daywork route.
Source attendance, overhead, profit, tax/levy and fluctuation treatment instead of inventing it.

Check specialist changes including extra points, deeper holes, revised monitoring frequency,
extended service/rental, relocation, replacement, access restrictions and repeated mobilisation.
Separate original inclusions, omissions, additional resources and avoided cost.
For extensions, calculate the incremental duration/resources; do not re-charge recovered
setup costs or claim both the same crew's productive work and full standby for the same time.
Distinguish engineer-approved design changes, instructed work and the contractor's own defects.
Quantified cost does not prove entitlement; identify causation, records and mitigation gaps.

## 5. Preserve notice and payment deadlines

Build a notice table from the actual clauses: event, trigger date, service method/recipient,
deadline rule, day convention, required content, supporting evidence and current status.
Never infer an upstream notice deadline binds the subcontract without incorporation evidence.
For Cap. 652, check the contract's date, main-contract scope/value, public/private exclusions,
subcontract chain and relevant current provisions. Distinguish older contractual SOPP.
Do not publish a legal deadline until the applicable text, trigger and service facts are verified.
Escalate time-critical missing facts promptly and draft the proposed action for human review.
Do not agree an extension, waive rights, admit liability or send a notice on the user's behalf.

## 6. Reconstruct cumulative payment

Use one consistent cumulative basis, with each deduction and release sourced:

`current_certificate = cumulative_eligible_gross_value`
`                    - cumulative_retention_currently_held`
`                    - cumulative_advance_recovery`
`                    - other_cumulative_deductions`
`                    + other_cumulative_additions`
`                    - previous_net_certificates`.

Explain each component. Respect the contract's retention base, percentage, cap and releases;
do not invent a default cap or apply retention twice. Record advance receipt separately.
Do not subtract cash paid instead of previous certificates in this certificate reconstruction;
show unpaid certificates and actual cash receipts in a separate payment ledger.
Use a different formula when the contract requires it, and explain the difference.

**Synthetic arithmetic check — `CALCULATION_ONLY`, not market rates or contract terms:**
Given cumulative eligible value HK$130,000, retention currently held HK$6,500,
advance recovered HK$3,000, other cumulative deductions HK$500 and previous net
certificates HK$100,000, the current net certificate is HK$20,000.
These inputs are assumed already verified for the example; they establish no entitlement.
If only HK$90,000 of prior certificates was paid, show the HK$10,000 unpaid balance
separately; the current certificate remains HK$20,000 under this reconstruction.

## 7. Deliver and reconcile

Provide the selected playbook's required outputs: use a measured-work schedule, cumulative
valuation and separate certified-versus-paid ledger for progress/payment work; use a change
register and notice/action table where the task involves changes or deadlines. Include exact
sources and unresolved items without generating unrelated schedules.
Use `NEEDS_SOURCE` for missing entitlement/rules, `CALCULATION_ONLY` for unsupported
scenarios and `READY_FOR_QS_REVIEW` for supported draft valuations.
Reconcile current/cumulative quantities, additions/omissions, retention movements,
advance recovery, previous certificates and cash; check duplicate IDs and cut-off dates.
Identify authorisations needed and the responsible reviewer without presenting approval as complete.
