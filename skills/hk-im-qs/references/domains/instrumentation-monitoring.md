# Hong Kong instrumentation and monitoring QS

Use this domain reference only for a package selected by [hk-im-qs](../../SKILL.md). Apply its relevant constraints within the chosen playbook; it is supporting guidance, not an additional worklist. Do not execute every numbered section or produce every listed schedule automatically. Load another domain only where a real package interface needs it.

Read [project basis and evidence controls](../project-basis.md) first. Use the [measurement source map](../measurement-sources.md), [source register](../source-register.json) and [output templates](../output-templates.md). Read only the relevant adopted documents.


## Contents

- [1. Fix the package boundary](#1-fix-the-package-boundary)
- [2. Build the physical asset and location register](#2-build-the-physical-asset-and-location-register)
- [3. Map activities to payable items](#3-map-activities-to-payable-items)
- [4. Define the monitoring service denominator](#4-define-the-monitoring-service-denominator)
- [5. Worked quantity comparison — hypothetical only](#5-worked-quantity-comparison--hypothetical-only)
- [6. Assemble evidence and assess changes](#6-assemble-evidence-and-assess-changes)
- [7. Deliver and check](#7-deliver-and-check)

## 1. Fix the package boundary

Obtain the tender/contract BOQ, particular preambles, specification, I&M drawings/schedule, approved monitoring plan, installation details, programme, access arrangements and relevant instructions. Confirm who supplies the equipment, drills holes, installs cables, provides power/connectivity, operates the system, checks data, reports results, maintains assets and removes/hands them over.

Record which work is included: standalone I&M, investigation plus instruments, or treatment plus I&M. For associated boreholes within the requested scope, use [ground investigation](ground-investigation.md) and for actual treatment interfaces use [ground improvement](ground-improvement.md). Do not price another contractor's production works as part of the monitoring package.

Extract the engineer-approved purpose, accuracy/range, monitoring locations and control requirements. Record unresolved engineering choices for the responsible engineer. Do not decide acceptable deformation, control-point layout, trigger values, reading intervals or resumption of works from a QS cost assumption.

## 2. Build the physical asset and location register

| Asset group | Minimum scope distinctions |
|---|---|
| Automated/manual survey systems | Total station, bracket/pillar, protective housing, controller, power, weather/atmospheric inputs if specified, reference network, monitored prisms/targets and checking surveys |
| Settlement/deformation | Surface/deep settlement point, plate, levelling mark, extensometer, survey target, crack gauge and tiltmeter; distinguish observation point from instrument/readout |
| Groundwater | Standpipe, piezometer tip/transducer, response zone, seals, protective cover, readout/logger and pumping-test interface |
| Inclinometers | Borehole, casing length, base/termination, headworks, manual probe versus in-place sensor chain, cabling, logger and reading profile |
| Structural/vibration instruments | Load cell, strain gauge, tilt/vibration sensor, fixing, channel, calibration, logger and supplied approved performance specification |
| Shared infrastructure | Datalogger, multiplexing, gateway, telemetry/SIM, network/power, software/data service, alert delivery, licences and backup |

Use an immutable asset ID, location, drawing revision, parent system, instrument type/model, serial number where relevant, physical quantity, installed depth/length, ownership and acceptance record. Show proposed, installed, accepted, active, damaged/replaced and decommissioned states separately.

Count one physical asset once. A multi-channel instrument is not automatically several installations. A shared logger/reference prism is not automatically chargeable once per station. Keep monitoring points and reference/control points separate. Do not count an instrument's cable, tip and readout as separate instruments unless the adopted bill distinguishes them.

## 3. Map activities to payable items

Create a coverage matrix before calculating totals:

| Work component | Internal cost record | Contract item mapping |
|---|---|---|
| Survey/design submissions and mobilisation | Labour/plant/time evidence | Named preliminaries/item or included elsewhere |
| Equipment supply or rental | Quote, ownership and recovery assumptions | Supply/install/lump-sum item as written |
| Holes, casing, grouting, seals and headworks | Hole and installation ledgers | GI item, installation coverage or expressly separate item |
| Installation/calibration/acceptance/baseline | Event, certificate and acceptance evidence | Verify item coverage; do not split by default |
| Routine monitoring and reporting | Stage, denominator, frequency and duration | Included or separately measurable under the actual preamble |
| Telemetry, data service and alerts | Capacity, retention/service term and inclusions | Included operating cost or expressly priced service |
| Maintenance/replacement/relocation | Cause, instruction, ownership and evidence | Existing obligation or evidenced potential change |
| Final readings/removal/handover | Scope and acceptance records | Contractual end obligations; not automatic removal |

For instrument installations in completed investigation holes, read `CEDD-SMM-1992` clauses 2.27–2.30 and General Preambles before itemisation. Treat the exact inclusive coverage and any particular amendment as the payment test. Do not presume that each cost component above earns additional payment. For modern ADMS/telemetry or other bespoke arrangements, obtain the applicable particular measurement description rather than manufacturing an SMM item number.

## 4. Define the monitoring service denominator

Capture **all** relevant clocks separately:

1. Sensor sampling interval and measurement cycle.
2. Upload/transmission interval and delivery/availability requirement.
3. Accepted observation set or full reading profile.
4. Manned visit/shift and minimum attendance, if expressly required.
5. Data checking/reporting interval and required deliverables.
6. Baseline, construction, hold, post-treatment and maintenance stages.

A five-second upload need not mean a new survey of every prism every five seconds. Do not infer technical throughput or cost from upload frequency alone. A logger's raw records, accepted observations, a technician visit and a submitted report are different quantities.

For a recurring item record:

`covered IDs/system | stage | start trigger | stop trigger | date convention | billing unit | required frequency | accepted evidence | partial-period rule | overlap exclusions | item coverage`

Use calendar months, days, weeks or shifts only as defined in the schedule. Do not silently replace a month by 30 days, bill installation-to-removal if the start is acceptance, or use the construction completion date as the monitoring/maintenance end without evidence.

When quantities change, split the ledger by effective date, IDs and agreed stage. Reconcile extensions, added points, relocated points and frequency changes separately; apply each event once. Retain the original baseline after relocation and create a new baseline/re-baselining record where required; do not erase historic comparisons.

## 5. Worked quantity comparison — hypothetical only

Assume the user expressly supplies: four stations form one complete system; 40 monitored prisms; six full service months; all accepted and continuously in service. These figures are illustrative, not a real project or a standard rule.

| Express item basis | Arithmetic | Quantity |
|---|---|---:|
| Complete system per month | 1 × 6 | 6 system-months |
| Station per month | 4 × 6 | 24 station-months |
| Monitored prism per month | 40 × 6 | 240 point-months |

These are alternative billing denominators, **not three amounts to add** for the same included service. If the bill just says “monitoring — month”, mark `NEEDS_SOURCE` and ask what a month covers. You may show the three scenarios as `CALCULATION_ONLY`; do not choose the largest.

## 6. Assemble evidence and assess changes

Link each claimed unit to the installed asset register, approved installation/as-built records, calibration/acceptance certificates and the accepted monitoring log. Preserve original timestamps/time zone, units, reference/baseline version and quality flags. Record sensor outages, rejected/duplicate readings, loss of sight, damaged markers and manual substitutes; do not fabricate missing observations.

Check the actual contract treatment of incomplete service. Do not automatically treat downtime as payable, apply an invented availability penalty or deduct the whole month. Log the fact and request the agreed assessment rule where missing.

For extra instruments, emergency visits, increased frequency, night work, extension of duration or relocation: compare instructed scope against priced inclusions; record who instructed what and when, contractual authority, notice/service evidence, resource effect and remaining mitigation. Use [valuation and variations](../valuation-rules.md) for entitlement and [cost estimation](../../playbooks/estimate-and-compare-quotes.md) for the build-up.

## 7. Deliver and check

Return an instrument/point register, item-coverage matrix, quantity and service-period ledger, priced/unpriced subtotal, source/rule log and focused RFIs. Mark each conclusion `CALCULATION_ONLY`, `NEEDS_SOURCE` or `READY_FOR_QS_REVIEW`.

Before release check:

- Physical counts, sensor channels, monitored points and control points are not conflated.
- Drilling and installation lengths have not been billed twice for the same included work.
- Included calibration/maintenance/readings are not charged again as new items.
- Baseline, routine, event and final readings have explicit scope and evidence.
- Billing denominator, stage dates, changing counts and partial-period treatment are established.
- System availability, data checking, reporting and platform service obligations are separately understood.
- Extended monitoring and defects/maintenance obligations are not assumed to end together.
- Equipment ownership, damage responsibility, relocation, final condition and handover are evidenced.
