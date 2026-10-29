---
name: hkqs-cost-estimation
description: Estimate Hong Kong specialist subcontract costs for instrumentation and monitoring, instrumented ground investigation and ground improvement. Use for quote build-ups, tender pricing, duration and frequency scenarios, plant and crew resources, monitoring services and specialist scope reconciliation.
---

# Specialist I&M, ground investigation and ground improvement estimates

Read [hkqs-general](../hkqs-general/SKILL.md) first, then
[cost and contract sources](../hkqs-general/references/cost-contract-sources.md) and the
[source register](../hkqs-general/references/source-register.json).
Use `CEDD-SMM-1992`, `CEDD-GS-2020`, `CEDD-PAH-2024` and the project's
particular preambles/specifications only where adopted. Technical scope does not itself
establish a separately payable item. This skill estimates work; it does not design it.

For an adopted CEDD SMM Section 2 GI instrument item, inspect clauses 2.27–2.30:
clause 2.30 places calibration, maintenance, readings and the required records within the
installation item's coverage. Keep these in the internal resource build-up, but do not
create extra payable items unless an adopted amendment/BOQ provision supports them.
Another project item or particular measurement schedule may use a different billing
structure; identify the actual item rather than assuming a general SMM instrumentation category.

## 1. Establish the commercial and technical basis

Record the specialist subcontract/tender scope, price date, HKD or other currency,
programme, working hours, access, exclusions, billing units and measurement edition.
Identify the contractor's issued requirements and incorporated main-contract provisions.
Do not assume that every main-contract obligation or notice rule flows into the subcontract.
Obtain instrument schedules, layouts, GI scope, treatment drawings, engineer-approved
methods, baseline/routine/event monitoring requirements and trial/acceptance obligations.
Identify who supplies power, communications, boreholes, platforms, access and protection.
Keep uncertain design quantities, installation depths and treatment extents visible.

## 2. Separate one-off, recurring and event costs

| Scope | Pricing evidence and boundary |
|---|---|
| Instrument supply or rental | Model, accuracy/range specified by designer, quantity, accessories, warranty, ownership |
| Installation | Crew, drilling/fixing, housings, cables, grouting, protection, survey and access |
| Calibration/commissioning | Factory/site calibration, reference checks, acceptance tests and handover |
| Data system | Logger, gateway, SIM/network, power, hosting, licences and integration |
| Monitoring service | Baseline, routine and event attendance/automatic service, review and reporting |
| Maintenance | Preventive visits, consumables, batteries, calibration and agreed repair scope |
| Removal/reinstatement | Recovery, abandonment if permitted, making good, disposal and data handover |
| GI operations | Mobilisation, drilling intervals, casing, samples/tests, instrumentation and sealing |
| Ground improvement | Trial area, treatment production, materials, QA/QC tests and monitoring interfaces |
| Standby/remobilisation | Trigger, authorisation, available resources, minimums and mitigation |

Do not price purchase and full-term rental for the same instrument unless scope requires
both. State who owns equipment during and after the works and who bears loss/damage.
Separate supplier warranty, contractor defects, ordinary maintenance and instructed replacement.

## 3. Build a traceable resource estimate

For each item retain scope ID, billing unit, resource quantity, unit, source, date, validity,
productivity basis, inclusions/exclusions, uncertainty and resulting amount.
Use actual supplier/subcontract quotations or evidenced historical costs adjusted explicitly.
Calculate resources from the planned method and site restrictions, not an invented HK norm.
For crew productivity, show crew composition, paid hours, productive hours and output;
avoid charging idle time both through reduced productivity and a separate standby allowance.
Record plant hire duration, minimum hire, transport, fuel, operator and support separately
unless the quotation already includes them. Identify shared crews/plant and allocate once.

### Illustrative rate build-up: one installed monitoring point

The quantities below are a structure for an estimate, not an official payment rule or market rate.

| Component | Quantity basis | Rate input |
|---|---|---|
| Sensor and accessories | Specified equipment per point | `quoted_supply_cost` |
| Installation labour | `crew_hours_per_point` | `evidenced_crew_hour_cost` |
| Plant/access | Allocated resource hours or package share | `quoted_plant_or_access_rate` |
| Cables/protection/consumables | Measured lengths/counts and stated allowances | Supplier quotation |
| Calibration/commissioning | Defined tests per point or allocated batch | Quoted test cost |
| Project overhead/risk/profit | Stated pricing policy and nonduplicated cost base | Explicit assumption |

`direct_cost_per_point = supply + labour + allocated_plant + consumables + tests`.
Add overhead, risk and profit using stated bases; do not invent a mandatory percentage.
Record rental, routine monitoring and recurring data fees separately in the internal
analysis, then allocate them to the payable rate wherever its adopted coverage includes them,
even if the short BOQ description does not repeat that coverage. Disclose the service period
and frequency; an unknown included duration prevents a settled all-in rate.
An estimate quantity is not automatically the measured quantity eligible for payment.

## 4. Price monitoring duration and frequency

Record installed points, active channels, logger count and visits as different drivers.
Distinguish sensor sampling, data upload, processing, human review and report frequency.
A one-second sample or five-second upload does not imply a separately billable reading.
For manual monitoring, account for route/shift capacity, travel, access and report preparation;
do not multiply a whole-site visit price separately by every point without justification.
For automatic monitoring, separate setup from continuing equipment, network, hosting,
maintenance, exception handling, reporting and out-of-hours response obligations.
Compute chargeable periods from the specified start/end triggers and proration terms.
Do not assume a month is 30 days, continuous rental starts at delivery, or all installed
points remain active until the overall main contract finishes.
Show baseline, normal service, extensions, intensified/event monitoring and removal separately.
For example, `service_cost = active_point_periods × quoted_point_period_rate`
applies only when that unit and its inclusions are actually offered; otherwise build resources.

## 5. Price GI and ground improvement with the correct drivers

Break drilling quantities into supported depth/diameter/material/method intervals and
distinguish drilling, casing, samples, in-situ tests, laboratory work and instrument installation.
Read the preambles before treating overlaps or ancillary operations as separate payment.
For treatment work, separate trial mobilisation, working-platform/access needs, production,
injected/mixed materials, spoil/waste handling, records, verification testing and monitoring.
Check whether drilling length, treated volume, grout/material consumption, time or a lump
sum governs the priced item. Do not infer the billing basis from the engineering method.
Keep design quantities, estimated consumption and actual measurable work separate.
Use low/base/high resource scenarios for uncertain ground or access with explicit drivers.
Do not select grout mix, pressure, treatment spacing, instrument thresholds or acceptance limits.

## 6. Check price evidence and contingencies

Prefer supplier quotes and bottom-up resources for specialist work. `CEDD-CEWTPI`
expressly excludes ground investigation and E&M installations among other work; do not
use it as a blanket index for a GI or instrument package. Verify suitability by component.
Use `CSD-CONSTRUCTION` for contractual fluctuation only if the actual contract specifies
the series, base, weights and formula; do not substitute it for specialist market evidence.
Record currency, delivery, quote validity, minimum order/hire and escalation separately.
Identify disposal, restricted hours, permits, safety access, third-party attendance and
outage requirements from the actual scope; remove duplicated allowances across packages.
Treat provisional sums, uncertainty allowances and contingency as distinct priced records.

## 7. Deliver and verify

Provide the scope matrix, resource/rate build-ups, quotation register, quantity basis,
programme/service assumptions, exclusions, alternatives and total reconciliation.
Show extension and frequency-change scenarios without implying contractual entitlement.
Assign `CALCULATION_ONLY` to assumptions and illustrative arithmetic; use `NEEDS_SOURCE`
for missing measurement/price inputs and `READY_FOR_QS_REVIEW` for supported draft items.
Report supported and unresolved subtotals separately; never turn missing costs into zero.
Check unit conversions, interval totals, durations, point/channel counts, shared costs,
ownership, recurring fees, additions/omissions and presentation rounding before handover.
