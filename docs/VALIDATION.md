# Validation record

Scope: the seven-skill Hong Kong I&M adaptation. Review date: **29 October 2026**.

## Structural and installation checks

Use `python3 scripts/validate_repository.py` to check the expected seven skills, frontmatter, status labels, local references, declared source IDs, required source metadata and absence of source-document binaries in the active skill folders.

All seven skills passed the bundled skill-creator frontmatter validator. The repository validator passed with 7 skills and 18 source entries, including all local Markdown references and source-ID references.

Installation checks passed in temporary directories: dry-run made no changes; copy and symlink modes each installed the complete seven-skill set; repeated installation refused existing destinations; and an unrelated sentinel file was preserved in both modes. No installation into the user's actual skills directory was performed.

## Practical forward checks

Two independent agents used the relevant skill files with task prompts and supplied project facts; the prompts did not give the expected conclusion.

| Scenario | Observed result |
|---|---|
| 12 piezometers; adopted unamended SMM GI coverage; separate calibration/maintenance/readings proposed; ambiguous four-station monthly monitoring and five-second uploads | Identified inclusive installation coverage and duplicate-payment risk; retained cost build-up components; distinguished 6 system-months from 24 station-months; refused to equate uploads with billable readings or six months with 180 days |
| 30 m hole plus reaming and inclinometer casing; overlapping treatment zones and two passes; failed test/re-treatment/monitoring extension; agreed payment ledger | Kept advance, reaming and casing separate; calculated 696 m³ unique ground; did not infer variation entitlement; calculated current certificate 20,000 and prior unpaid 10,000 separately |

These checks exercise measurement scope, denominator control, evidence gaps and payment arithmetic. They are synthetic scenarios, not real contract determinations, professional certification or comprehensive testing of every rule.

## Source verification limits

The source register explicitly distinguishes selected official text reviewed from publication metadata verified. Detailed proprietary NEC clauses are not bundled or represented as reviewed. Most source documents are lengthy; targeted retrieval is required for each actual applied rule. Official dates identify the review snapshot, not a promise that sources remain current.

No local installation into the user's personal Skills directory, issue of a contract notice, payment certification or engineering acceptance is claimed by this record.
