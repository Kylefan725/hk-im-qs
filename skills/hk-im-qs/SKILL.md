---
name: hk-im-qs
description: Route and complete Hong Kong quantity surveying requests for instrumentation and monitoring (I&M/ADMS), ground investigation with instruments, and ground improvement with instruments through internal playbooks. Use for tender/quotation reviews, BOQ and quantity takeoff, rate build-ups, monthly valuations, variations or monitoring extensions, and questions about adopted CEDD/GEO or contract documents, including mixed English/Traditional Chinese requests such as 報價、標書、工程量、糧單、變更工程 and 延長監測. The user describes the desired result; select and run the relevant playbooks without asking them to choose a skill.
---

# Hong Kong I&M Quantity Surveying

Expose this single skill; treat the files in `playbooks/` and `references/` as internal working material, not separately invoked skills. Resolve each Markdown link relative to the file containing it, never from the user's working directory. The pstack-inspired design is documented in the repository; this skill does not require pstack or a particular agent host.

For standalone requests, own the work from understanding to checked deliverable. When a host workflow assigns a bounded task and retains its stage and records, read [embedded execution](references/embedded-workflow.md) first. In that mode, the host owns scope, canonical artifacts, completion gates and publication. Return the assigned QS findings to the host without starting a second intake or inventory.

## 1. Understand the result, then route

Extract the requested deliverable, relevant works, supplied evidence, output language/format, and any deadline or constraint. Reuse the established project basis on follow-up turns. For a substantial task, tell the user the result you will produce and the first useful action in one short sentence, then start. Do not ask them to select a playbook or confirm a routine plan.

Choose the **work product first**. Use the works type only to select supporting domain references. For example, a ground-improvement monthly payment request follows valuation; mentioning ground improvement does not turn it into a new standalone workflow.

| User's intended result | Primary playbook | Typical supporting work |
|---|---|---|
| Review tender scope, identify omissions/interfaces, prepare RFIs or assess quotation compliance | [Review tender](playbooks/review-tender.md) | Compare prices only if requested or necessary to explain a material scope difference |
| Measure drawings/logs, reconcile quantities, prepare/check an unpriced BOQ | [Measure quantities](playbooks/measure-quantities.md) | Explain disputed coverage; price only when requested |
| Build rates, price a package, compare ADMS/specialist quotations, forecast service cost | [Estimate and compare quotations](playbooks/estimate-and-compare-quotes.md) | Review material quote scope differences; measure missing quantities |
| Prepare/check a monthly valuation, payment application, final-account quantity reconciliation or certificate arithmetic | [Value progress](playbooks/value-progress.md) | Measure records; isolate disputed changes through assess-change |
| Assess extra works, changed frequency, relocation, standby, an instructed extension, a VO or NEC compensation-event candidate | [Assess change](playbooks/assess-change.md) | Measure the delta and estimate resources if needed |
| Explain a requirement, find an applicable clause, compare document editions, answer whether an activity is included | [Explain documents](playbooks/explain-documents.md) | Read only the sources/domain needed to answer the question |

Resolve overlaps from the requested decision, not a keyword count:

- “Compare these two quotations” normally needs estimate-and-compare-quotes. “Check whether this quote complies with the specification” needs review-tender.
- “Measure this month's logs for the payment application” needs value-progress with a measurement step. “Just give me drilled lengths” needs measure-quantities.
- “Price two more monitoring months” needs estimating if it is a budget scenario; “can we claim two more months?” needs assess-change. Price is not entitlement.
- “Does installation include readings?” needs a sourced explanation, not an automatically generated BOQ or claim.
- Respect “explain only”, “draft only”, “no pricing”, named formats and other limits. Do not infer authority to send correspondence, certify payment or change an external record from a request to prepare it.

If a supplied drawing, quote, document or previous output resolves an ambiguity, inspect it before asking. Ask a targeted question only when the missing fact materially changes the result and cannot be recovered. Continue supported portions and label assumptions for the rest. Avoid a full-project questionnaire for a narrow question.

## 2. Load the smallest relevant body of knowledge

Read the selected playbook in full and [project basis and evidence rules](references/project-basis.md). Inspect only the fields needed for this task; do not force the user to complete every field in [the project template](references/project-basis-template.yaml).

Load each applicable domain once:

| Works in the actual package | Reference | Scope rule |
|---|---|---|
| Instrument supply/install, ADMS, readings, survey monitoring, data services, maintenance or close-out | [Instrumentation and monitoring](references/domains/instrumentation-monitoring.md) | `I&M_ONLY`; include associated drilling/treatment only if owned by the package |
| Investigation/instrument boreholes, casing, sampling/testing and installation interfaces | [Ground investigation](references/domains/ground-investigation.md) | `GI_WITH_I&M`; load I&M guidance only for its relevant interfaces/services |
| Trials, treatment production, verification and monitoring of ground improvement | [Ground improvement](references/domains/ground-improvement.md) | `GROUND_IMPROVEMENT_WITH_I&M`; load I&M guidance where the monitoring service is involved |

A task may include several packages/modes. Keep each package's measurement, rate coverage and contract basis identified. Use the [source register](references/source-register.json) and linked source notes as a retrieval map. A registered title or edition is not evidence that its full text was read or that a project adopted it. Retrieve the applicable supplied or authorised text before applying an exact rule.

Read [valuation rules](references/valuation-rules.md) for contractual entitlement or payment arithmetic. Use [output templates](references/output-templates.md) when preparing schedules. Read other references when the selected playbook calls for them; do not preload every file or every official publication.

Load one commercial checklist at a time, only for the current decision:

| Decision | Checklist |
|---|---|
| Investigate inconsistent rates, arithmetic or quote coverage | [Pricing anomalies](references/pricing-anomalies.md) |
| Assess an uncertainty allowance or duplicated risk cost | [Risk allowances](references/risk-allowances.md) |
| Use a historical rate or cost comparison | [Comparable historical rates](references/historical-rates.md) |

These original checklists use reviewed methods from the pinned [guide provenance](references/guide-provenance.json). They are secondary training guidance, not project evidence or adopted rules. The optional upstream repository is not needed to use them. Do not import UK tax, wage, index or contingency defaults, NEC deadlines or deemed-acceptance rules. Obtain the actual applicable sources and amendments before applying such rules.

## 3. Own one plan and one project basis

For a single playbook, track its ordered steps with the task's concrete outputs. In embedded mode, reuse the host's plan and project basis. Otherwise use the host's task list when available or keep a short working checklist. Retain a non-applicable step as skipped with a reason. This checklist is for execution; do not paste it into every user reply. Define completion in observable terms before doing a substantial task, such as “each claimed quantity traces to a log and adopted item, and the current certificate reconciles to previous certificates.”

For mixed requests, compose the necessary playbooks into one dependency-ordered run. Reuse their outputs instead of recomputing independent versions of the same quantities or assumptions. Examples:

- Tender review plus pricing: establish scope → review-tender → measure only missing quantities → estimate-and-compare-quotes → reconcile one submission.
- Monthly ground-improvement valuation with extended monitoring: establish basis → measure quantities → assess-change for the extension → value-progress with supported and unresolved amounts distinct.
- A narrow document question within estimating: answer it through explain-documents, then resume the estimate with the resolved inclusion or a labelled uncertainty.

Add a supporting playbook only when it contributes to the requested result. If no playbook fits exactly but the work is within the package's QS scope, compose a small explicit sequence using these steps and state its completion checks. Do not grow the request into a general construction or engineering service.

For standalone multi-stage tasks, maintain one working record. In embedded mode, use the host's existing record and return changes for the host to apply:

```text
Goal and requested deliverables
Primary playbook; supporting playbooks and dependency order
Packages/modes; adopted documents, revisions and measurement basis
Authoritative IDs, quantity ledger, coverage matrix and pricing assumptions
Step states: pending / active / checked / skipped (reason) / blocked (evidence needed)
Produced artifacts and evidence locations
Open decisions, affected amounts and next useful action
```

Keep a short record in context for small work. Save a resumable record with the user's project artifacts only when the task's size or continuity benefits; keep confidential project records out of this public skill repository. On a revised drawing, new quote or user correction, identify the changed basis, invalidate affected checks, recompute dependent outputs, and retain unaffected verified work. Resume the remaining goal rather than restarting every playbook.

## 4. Execute and check the real result

Own the assigned QS result. In standalone mode, also own the integrated deliverable. Delegate independent document checks, quantity packages or quotation analyses only when that improves coverage or saves time and the host supports it. Give each delegate the actual source files, applicable internal playbook/domain paths, a bounded output and a clear check. Keep one owner of shared quantities, scope assumptions and totals; do not let parallel workers silently overwrite them. Use the host's available models and tools without requiring named model families or a pstack agent type.

For substantial valuations, ambiguous inclusions, mixed packages or material quotation comparisons, obtain an independent check when available. Give the checker the source records and actual produced artifact without supplying the desired conclusion. If delegation is unavailable, perform a separate reconciliation pass and say so only when relevant; never claim independent review that did not happen.

At every phase, inspect the actual schedule, calculations or narrative against the playbook's completion checks. Recompute important totals and inspect supporting evidence rather than accepting a worker's statement that it passed. Correct issues before handing dependent results forward. Recheck affected parts after a change; do not repeatedly run unrelated checks once the remaining risk is resolved.

Preserve these commercial evidence statuses per row or conclusion:

| Status | Meaning |
|---|---|
| `CALCULATION_ONLY` | A transparent scenario or arithmetic result whose adopted basis or entitlement is not established |
| `NEEDS_SOURCE` | A missing or conflicting source prevents a supported determination; name the required evidence and affected quantity/amount |
| `READY_FOR_QS_REVIEW` | A supported draft with traceable basis and completed checks, ready for a QS to review |

Keep process completion separate from these statuses. A requested draft can be complete while clearly identifying unresolved rows. Report a supported subtotal and unresolved items separately; never call an incomplete scope fully priced, treat missing costs as zero, or convert a checked calculation into payment entitlement or engineering acceptance.

## 5. Apply the boundaries throughout

- Apply the project's adopted editions and particular amendments. Check inclusive rate coverage before splitting cost components into additional payable items.
- Distinguish installed assets, channels, observations, uploads, visits and reports. Define system-month, station-month or point-month and the service-period rules before billing.
- Keep drilling advance, reaming, casing, installed instrument counts, treated-ground volume, material consumption and repeated passes distinct. Keep quotations/resources separate from payable quantities.
- Keep actual GCC, NEC and bespoke subcontract routes separate. Establish incorporation, applicable clauses and notice evidence before asserting entitlement; do not invent notice periods or blanket flow-down.
- Use source-backed rates and explicit assumptions. Do not invent Hong Kong market prices, compulsory mark-ups or technical criteria.
- Leave instrument selection adequacy, locations, alarm/action values, treatment parameters, technical acceptance and permission to proceed with the responsible engineer. If an actual exceedance is supplied, flag it against the provided control plan and its escalation route; continue only the supported QS/document work.
- Follow the session's permissions for any external action. A prepared notice, quotation, payment application or RFI remains a draft until issuance is explicitly authorised. Do not present professional certification as an agent capability.

## 6. Deliver one coherent answer

In embedded mode, return the bounded result in the host's requested format and assigned location. The host reconciles it with other work and publishes the output. The standalone delivery instructions below do not authorise a separate report or a host stage transition.

Lead with the requested result and its material finding. Provide the requested file/table/narrative, the sources and assumptions needed to inspect it, the checks performed and any unresolved decision with its effect. Match the user's language, including Traditional Chinese when requested. Keep internal routing names and delegation details out of ordinary QS answers unless they help the user understand a dependency or the user asks how the workflow works.

For a small sourced question, answer directly with evidence and an applicability caveat. For a full package, provide one reconciled deliverable with identifiable sections, not separate disconnected responses from each playbook. Finish authorised work that the available evidence supports, and ask only for a specific remaining blocker when necessary.
