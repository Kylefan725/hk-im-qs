# Validation record

Scope: **v0.3.0-hk-im**, one `hk-im-qs` entry with six internal playbooks and three domain references. Review date: **29 October 2026**.

## Lifecycle and coverage checklist update — 30 October 2026

The review-tender playbook now links an original checklist for bidirectional requirement/BQ/quotation/operation checks, scoped finding identities, lifecycle duties, separate monitoring/maintenance/rental periods and critical source checks. Embedded returns and working output fields use the same distinctions. The entry skill, installer, official source register and pinned guide provenance are unchanged; no private project evidence is bundled.

Observed on Windows with Python 3.10.11: `python -B scripts/validate_repository.py` passed. The 10 installation tests ran: eight passed; symlink installation and the broken-symlink legacy fixture failed with `WinError 1314` (required privilege not held). A run outside the execution sandbox produced the same two failures. Copy installation, copied-byte/local-link checks, dry-run, conflict preservation, rollback and malformed-package rejection passed. These failures remain open host limitations, not passing or skipped checks. No system settings or active skill directories were changed.

The skill-creator `quick_validate.py` passed using the installed Python 3.14 with `-X utf8`. The default Python 3.10 lacked its `yaml` dependency, and Python 3.14 without UTF-8 mode could not decode the existing multilingual entry skill under the Windows default code page. `git diff --check` passed. These checks establish packaging and instruction structure; fresh-context execution of the new lifecycle/coverage cases and professional adjudication remain separate verification.

## Structural and installation checks

Run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

The validator checks the single discoverable `SKILL.md`, frontmatter, six required playbooks and their completion contracts, core/domain links, self-contained local references, source IDs/metadata and distribution exclusions. It also checks the guide revision, source URL pins, reviewed-section metadata and three bundled checklist paths. The test suite exercises dry-run, copy/symlink installation, destination conflicts, legacy entries (including broken symlinks), unrelated-entry preservation and malformed-package rejection.

The v0.3.0 baseline passed the repository validator, the skill-creator frontmatter validator and all **8** installation/validation tests. The embedded-guidance change passes the repository validator and **10** tests. The copied-install test compares file bytes and resolves local links inside the installed folder. New cases reject an unpinned guide revision, an unpinned source URL and a missing checklist before installation writes the target. `git diff --check` passed. No test installed skills into the user's actual active directory.

These are structural and installation results. Fresh-context standalone/embedded scenarios, guide-unavailable behavior and repeated base/head model performance comparisons remain unverified for this change. Earlier scenarios below do not satisfy those checks.

The source register is unchanged from v0.1.0: 18 official entries with their existing evidence levels and review dates. No full source publications or private project records are bundled. Structural checks do not prove future URL availability or technical/legal applicability.

## Routing and execution checks from v0.2.0

The following checks were run before the entry-name change, against v0.2.0. Version 0.3.0 changes the skill identifier, folder, display title and references without changing playbook behaviour. The rename is covered by packaging and installation checks; these scenarios were not rerun as new v0.3.0 checks.

Three fresh-context agents received the entry skill path, a task and supplied project facts without the expected route or answer. After producing their answers, each reported the playbook files actually read; no expected route was supplied during execution.

| Request | Observed route and result |
|---|---|
| Traditional Chinese comparison of a five-station ADMS over eight months, unpriced removal in one quote, and a two-month budget extension | Read estimate-and-compare-quotes only, with project/I&M references. Calculated A HK$240,000 including removal and B HK$218,000 plus unresolved removal. Used the HK$22,000 removal-price break-even, kept the missing price out of a false cheapest-total conclusion, and calculated extension budgets of HK$36,000 and HK$47,000 without starting a claim workflow. |
| Cumulative GI/ground-improvement October valuation, separately billed reaming/casing, included routine readings, overlapping treatment zones, prior certificates/cash and an unsupported monitoring-extension request | Read value-progress, measure-quantities and assess-change. Reconciled 720 m³ unique ground, HK$225,000 supported gross, HK$11,250 retention and HK$63,750 current net. Kept HK$10,000 prior unpaid cash separate, removed the duplicate HK$1,200 readings and isolated the HK$18,000 extension as pricing with unresolved entitlement. Produced a draft RFI without sending it. |
| A short interpretation of supplied installation/baseline clauses plus a request to fill a blank alarm value | Read explain-documents only. Preserved routine readings within installation while recognising separately measured baseline survey. Identified the engineer-owned missing alarm limit, provided a bounded answer within 250 words and produced no BOQ, estimate, claim or external action. |

The valuation agent attempted an independent checker but the host's thread limit prevented it; it performed and accurately reported a separate self-check. This exercised the documented fallback, not an independent professional review. The parent also reconciled the scenario's arithmetic and evidence distinctions.

These checks demonstrate the observed routes and outputs for three synthetic tasks. They are not exhaustive coverage of every playbook, language variant, contract situation or future model behaviour.

## Preserved v0.1.0 checks

The preceding specialist version passed two independent usage scenarios:

| Scenario | Observed result |
|---|---|
| Piezometer installation with proposed extra calibration/maintenance/readings; ambiguous monthly ADMS and five-second uploads | Identified inclusive coverage and double-payment risk; kept internal costing distinct; separated 6 system-months and 24 station-months; did not equate uploads with billable observations or six months with 180 days |
| GI advance/reaming/casing; overlapping treatment areas and repeated passes; re-treatment and monitoring extension; payment ledger | Separated quantities, calculated 696 m³ unique ground, retained entitlement gaps and separated current certificate 20,000 from prior unpaid cash 10,000 |

Those results are historical checks of the prior structure, not evidence that the new router has already passed the same cases. Current results are recorded separately above.

## Limits

The skills support traceable QS drafts. They do not certify engineering adequacy, establish contractual entitlement without the actual adopted text, or certify payment. Source metadata is distinguished from inspected text, and exact rules require task-specific retrieval. LLM routing remains an instructed behaviour; it is not a deterministic software guarantee.

No personal-skill installation, sending of contract correspondence, payment certification or engineering acceptance is performed by repository validation.
