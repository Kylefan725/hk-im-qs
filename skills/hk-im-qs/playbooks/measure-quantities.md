# Measure quantities and prepare a BOQ

Prepare or check the quantities the user needs. Select this playbook for takeoff, drawing/log reconciliation and unpriced BOQs; let value-progress own the result when the user needs a payment application.

## Inputs

Use [project basis](../references/project-basis.md), [measurement sources](../references/measurement-sources.md), [output templates](../references/output-templates.md), and only the applicable [I&M](../references/domains/instrumentation-monitoring.md), [GI](../references/domains/ground-investigation.md) or [ground-improvement](../references/domains/ground-improvement.md) reference. Obtain the relevant drawings, schedules, logs, dates, units, adopted measurement rules and particular preambles. Work out supported raw quantities while recording missing contractual measurement evidence.

## Steps

1. **Fix the measurement boundary.** Record the purpose, package, revision, location/zone, date cut-off, work status and unit. Establish whether this is a design takeoff, as-built quantity, accepted work record or proposed bill. Identify superseded drawings and overlapping package ownership before counting.
2. **Build one physical ledger.** Link source records to stable instrument, point, channel, hole, interval or treatment-zone IDs. Retain source file/page, timestamps where relevant, raw value, units, calculation and evidence gaps. Record repeated, rejected, incomplete and superseded records explicitly rather than deleting their history.
3. **Apply the relevant domain method.** For I&M distinguish systems/stations/points/channels, baseline/routine/event/final observations, uploads, visits and reports; split active periods when counts or stages change. For GI separate drilling advance, recovered core, reaming, temporary/permanent casing and installation lengths/counts. For ground improvement separate gross/net treatment geometry, overlap, passes, material consumption and verification tests. Do not multiply unique ground volume by the number of passes without an adopted payable basis.
4. **Map raw work to bill coverage.** Read the adopted item and inclusions, not just its short description. Keep raw quantities, measurement adjustments, accepted quantities and proposed payable quantities in distinct columns. Check GI instrument-installation coverage under `CEDD-SMM-1992` 2.27–2.30 when adopted; a separately recorded calibration, maintenance visit or reading is not automatically a second payable item. Use working IDs labelled as such; do not invent official item codes.
5. **Resolve time and quantity denominators.** Establish what one system/month/point/visit means, the accepted start/stop triggers, calendar or other period convention and any partial-period rule. When a bill says only “monitoring — month”, present clearly labelled alternatives if useful and request the definition. Do not choose a denominator or treat six months as 180 days without a project rule.
6. **Reconcile and issue the requested schedule.** Recalculate interval and geometry totals, deduplicate shared assets and repeated records, reconcile totals by zone/package and record exclusions. Pass the same checked ledger to estimating or valuation only when those outputs are requested; do not restart a different quantity basis.

## Outputs

Produce the requested takeoff/BOQ with `working ID | source/revision | raw quantity and unit | calculation | adopted item/coverage | adjustment | proposed quantity | status`. Add only material interface or source questions. Show `CALCULATION_ONLY` for a scenario, `NEEDS_SOURCE` for unresolved measurement/payment coverage and `READY_FOR_QS_REVIEW` for supported draft rows. A raw quantity can be checkable while its payable treatment is unresolved.

## Completion checks

- Every reported quantity has a unit, scope, revision/cut-off and reproducible calculation or source record.
- IDs and ranges reconcile without duplicate counts, gaps concealed as zero, double-counted overlaps or re-used readings.
- Counts, lengths, volumes, consumption, passes and service periods remain distinguishable.
- Item coverage supports each proposed payable line; engineering work requirements alone have not created payment rights.
- Unsupported denominators and measurement amendments remain identified, with supported and unresolved quantities separate.
- The resulting table satisfies the user's requested scope and can be reused unchanged as an input to the next requested playbook.
