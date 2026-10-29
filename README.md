# Hong Kong I&M Quantity Surveying Skills

Seven focused AI skills for **instrumentation and monitoring (I&M), ground investigation involving instruments, and ground improvement involving instruments** in Hong Kong.

Adapted from [kuikiun/qs-skills](https://github.com/kuikiun/qs-skills). The original's Australian building measurement and broad cost-management modules have been replaced with specialist Hong Kong workflows. Original MIT attribution is retained in [LICENSE](LICENSE). See [migration and scope](docs/MIGRATION.md).

[繁體中文說明](README.zh-HK.md)

## What this version does

Review specialist tender scope, build an auditable BOQ/quantity schedule, develop rates from quotations and resources, reconcile progress valuations, and assess monitoring extensions or instructed changes. Link instruments, boreholes, treatment zones, accepted observations, service periods and bill items through stable IDs.

Select one of three package modes:

- **I&M only:** instrument supply/install, baseline, monitoring, data services, maintenance and close-out, with associated works only where in this package.
- **GI with I&M:** investigation/instrument boreholes, specified testing and instrument-installation/monitoring interfaces.
- **Ground improvement with I&M:** treatment trials, production and verification linked to the monitoring package and approved control plan.

This is a QS workflow toolkit. Engineering design, instrument selection adequacy, trigger values, treatment parameters and technical acceptance remain with the responsible engineer. A source-supported draft is ready for review, not a certificate or permission to continue works.

## Seven skills

| Skill | Main work |
|---|---|
| [hkqs-general](skills/hkqs-general/SKILL.md) | Scope, project documents, adopted editions, contract route, evidence and task routing |
| [hkqs-instrumentation-monitoring](skills/hkqs-instrumentation-monitoring/SKILL.md) | Instrument/point register, ADMS, monitoring stages, duration/frequency and payment denominators |
| [hkqs-ground-investigation](skills/hkqs-ground-investigation/SKILL.md) | Hole intervals, tests, instrument installations, groundwater records and GI/I&M interfaces |
| [hkqs-ground-improvement](skills/hkqs-ground-improvement/SKILL.md) | Trials, treatment quantities, overlapping zones/passes, verification and I&M interfaces |
| [hkqs-cost-estimation](skills/hkqs-cost-estimation/SKILL.md) | Supplier/resource-based rates, purchase/rental, telemetry, attendance, recurring cost and scenarios |
| [hkqs-valuation-variations](skills/hkqs-valuation-variations/SKILL.md) | Measured progress, cumulative payments, changes, extensions, notice evidence and contract routes |
| [hkqs-tender-review](skills/hkqs-tender-review/SKILL.md) | BOQ/specification/quote reconciliation, responsibility matrix, gaps and focused RFIs |

Load the general core and only the specialists needed for the current task. Install all seven together because they use sibling references and one shared source register.

## Hong Kong documents used

The [source register](skills/hkqs-general/references/source-register.json) records **18 official sources**, verified on **29 October 2026**, with edition, URL, evidence level and applicability limits. Principal references are:

| Purpose | Reference route |
|---|---|
| Measurement/payment coverage | CEDD **Standard Method of Measurement for Civil Engineering Works, 1992 Edition**, consolidated through Corrigendum 1/2011, plus adopted particular preambles |
| GI, grouting and instrumentation technical scope | CEDD **General Specification for Civil Engineering Works, 2020 Edition**, Volume 1 Section 7 Parts 2, 4 and 6; selected consolidated amendment set |
| Investigation/logging context | GEO **Geoguide 2** and **Geoguide 3**, 2017 consolidated versions |
| Monitoring surveys | **Engineering Survey Practice Guides for Works Projects**, August 2025 update, Chapter 7 |
| Geotechnical monitoring/control | **GEO Publication 1/2023**, **TGN54** and relevant project-approved I&M documents |
| Treatment verification and marine context | **TGN18**, and relevant **Port Works Design Manual Parts 3/4** when the marine scope fits |
| Contract and payment administration | Actual GCC/NEC/bespoke subcontract documents, relevant PAH chapter, and verified statutory/contractual payment provisions |

Use the edition incorporated into the project. The newest publication does not retrospectively amend a contract. The general building HKSMM/ArchSD elemental route is not part of this focused version.

The repository contains original instructions and links, not full source publications. Public availability does not mean unrestricted redistribution. Obtain any authorised NEC base contract or other licensed project document needed for a live task. See [source handling](docs/README.md).

## Commercial controls that matter

- **Separate cost from payment.** An internal allowance for calibration, maintenance or readings does not establish a separate payable BOQ item. Check the adopted inclusive coverage first.
- **Define the denominator.** System-month, station-month, point-month, reading set and site visit are different measures. A data upload interval is not automatically a payable observation.
- **Link physical work to evidence.** Drilled depth, recovered core, casing length and installed instrument count are different records. Two treatment passes do not automatically double net treated-ground volume.
- **Keep contract routes separate.** GCC changes, NEC compensation events and bespoke subcontract provisions require their actual wording. Upstream obligations do not automatically flow down.
- **Preserve uncertainty.** Use `CALCULATION_ONLY`, `NEEDS_SOURCE` and `READY_FOR_QS_REVIEW` per row. Continue supported work and isolate missing sources or unresolved amounts.
- **Use real price evidence.** No fabricated Hong Kong market rates, universal percentages, notice periods or engineering thresholds are embedded.

## Install from a local checkout

Python 3 is required only for the installer and validation tools. The skills themselves are Markdown and JSON/YAML reference files. The installer creates each individual skill beneath an existing skills directory and refuses to overwrite any existing destination.

```bash
# Run from this repository. Preview first; this writes nothing.
python3 scripts/install_skills.py --target ~/.claude/skills --dry-run

# Install per-skill symlinks: updates in this checkout are immediately reflected.
python3 scripts/install_skills.py --target ~/.claude/skills --mode symlink

# Or use copies where symlinks are unsuitable; later updates require replacing the copies.
python3 scripts/install_skills.py --target ~/.claude/skills --mode copy
```

For a project-scoped Claude installation, use `.claude/skills` as the target from that project's intended working directory, or give its absolute path. For a Codex installation, supply the skills directory supported by your environment explicitly. Do not replace an entire existing skills directory with this repository.

Windows PowerShell example:

```powershell
python scripts/install_skills.py --target "$env:USERPROFILE\.claude\skills" --mode copy
```

If received as a Git bundle, restore the complete repository first:

```bash
git clone qs-skills-hk-im.bundle qs-skills-hk
cd qs-skills-hk
git switch hong-kong-edition
```

Installation into ChatGPT's personal Skills directory is a separate action; this repository does not claim it has been installed there.

## Example requests

> Review this I&M tender and identify unclear instrument counts, monitoring duration, reading frequency, maintenance and borehole interfaces. Produce a responsibility matrix and RFIs in Traditional Chinese.

> Use the specified CEDD measurement basis to reconcile these drilling logs and piezometer installations. Show raw quantities, payable quantities, included activities and missing evidence separately.

> Compare two ADMS quotations on the same system scope, six-month service period, acceptance requirements and reporting obligations. Show equipment ownership, monthly costs and extension scenarios.

> Prepare the monthly valuation for instrumented ground improvement. Reconcile treatment zones, verification tests, monitoring periods, previous certificates, retention and outstanding cash receipts.

## Validate and maintain

```bash
python3 scripts/validate_repository.py
```

This checks the seven-skill structure, frontmatter, relative references, source IDs, source metadata and distribution exclusions. It does not certify technical/legal correctness or prove future URLs remain current. Practical checks are recorded in [VALIDATION.md](docs/VALIDATION.md).

When updating, verify publisher revisions, preserve contract applicability, amend the shared source register, then review affected workflows. Do not bulk-import source standards or confidential project records. Keep examples synthetic and label assumptions.

**Adaptation version:** `0.1.0-hk-im` — specialist Hong Kong I&M scope.
