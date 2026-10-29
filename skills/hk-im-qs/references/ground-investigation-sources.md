# Hong Kong ground investigation source guide

Verified on **29 October 2026**. This guide identifies sources and retrieval locations for instrument-related GI quantity surveying. It is an original workflow guide, not a substitute for the incorporated documents.

## Verified official publications

| Source ID | Document and edition | Official source | Verification / use |
|---|---|---|---|
| `CEDD-SMM-1992` | Standard Method of Measurement for Civil Engineering Works, 1992 Edition; official consolidated version listed September 2011 | [CEDD catalogue](https://www.cedd.gov.hk/eng/publications/standards-spec-handbooks-cost/stan-smm/index.html) · [consolidated PDF](https://www.cedd.gov.hk/filemanager/eng/content_79/cesmm_rev_10.pdf) | Official text inspected for Section 2 and instrument-installation coverage. Apply only when incorporated, with actual particular preambles. |
| `CEDD-GS-2020` | General Specification for Civil Engineering Works, 2020 Edition, Volume 1; current catalogue update 23 July 2026, incorporating Amendment 3/2026 | [CEDD catalogue](https://www.cedd.gov.hk/eng/publications/standards-spec-handbooks-cost/stan-gs-2020/index.html) · [current Volume 1 PDF](https://www.cedd.gov.hk/filemanager/eng/content_978/GS%202020%20Vol%201%20Rev%208_clean.pdf) | Official contents and selected Section 7 passages inspected. Technical requirements; separate payment requires the measurement/contract basis. |
| `GEO-GEOGUIDE-2` | Guide to Site Investigation, Geoguide 2, 2017 Version; continuously updated 18 December 2017 | [Official publication page](https://www.cedd.gov.hk/eng/publications/geo/geoguides/geo-g2/index.html) · [official PDF](https://www.cedd.gov.hk/filemanager/eng/content_108/eg2_20171218.pdf) | Official metadata and stated purpose verified. Technical guidance; retrieve the relevant text before applying a technical recommendation. |
| `GEO-GEOGUIDE-3` | Guide to Rock and Soil Descriptions, Geoguide 3, 2017 Version; continuously updated 29 August 2017 | [Official publication page](https://www.cedd.gov.hk/eng/publications/geo/geoguides/geo-g3/index.html) · [official PDF](https://www.cedd.gov.hk/filemanager/eng/content_110/eg3_20170829.pdf) | Official metadata and stated purpose verified. Description guidance; does not by itself establish a contract's payable material category. |

The Geoguide 2 [version history](https://www.cedd.gov.hk/eng/publications/geo/geoguides/geo-g2/geo-g2-version/index.html) lists the first edition in September 1987 and Amendment GG2/01/2017. The Geoguide 3 [version history](https://www.cedd.gov.hk/eng/publications/geo/geoguides/geo-g3/geo-g3-version/index.html) lists the first edition in July 1988 and Amendment GG3/01/2017. Record the selected consolidated version and any project requirement to use an earlier version.

All links above lead to lawfully public publisher pages/files. Public availability does not confer permission to republish the full documents. Retain links and concise original explanations; keep downloaded working copies outside the distributed skill text.

## Retrieve the right part

For CEDD SMM, inspect **Section 2 — Ground Investigation**, printed pages 26–32, together with the general provisions and project preambles. For instrument installation, inspect **2.27–2.30** and reconcile coverage before separating monitoring charges. Use the companion [measurement source guide](measurement-sources.md) for the wider measurement route.

For GS 2020 Volume 1, the correct technical route is **Section 7 — Geotechnical Works**:

- **Part 2 — Ground Investigation**, beginning at 7.09; operational provisions begin at 7.29.
- **Part 6 — Geotechnical Instrumentation**, beginning at 7.262.

These references identify locations, not a complete audit of all provisions. Read the adopted edition's actual clause, amendments and particular specification at the point of use. Do not confuse GS section numbering with SMM section numbering.

## Assemble the project source set

Before final measurement, obtain the applicable BQ or schedule, general/particular preambles, specification and drawings, the investigation/instrument schedule, relevant instructions and records. Identify their revisions and contractual status. For contract valuation or notice questions, also establish the actual contract form and amendments.

Build the evidence record in this form:

```text
source_id:
document_title:
edition_and_amendments:
project_incorporation_reference:
clause_or_printed_page:
short_original_explanation:
affected_hole_instrument_or_bill_item:
verified_on:
unresolved_difference_or_information_request:
```

Use factual field records to establish what happened, technical documents to establish required performance/scope, and the incorporated measurement/contract documents to establish billing treatment. A requirement to perform an activity does not by itself create a separate payment item.

## Avoid unsupported substitutions

- Do not relabel UK CESMM, ANZSMM or a contractor's customary schedule as the Hong Kong Government SMM.
- Do not infer a borehole's payable depth from sensor length, recovered-core length or a nominal design depth.
- Do not infer that each data reading, test stage or report file is a separately payable unit.
- Do not treat geological terminology as a universal excavation or drilling payment classification.
- Do not use a catalogue entry to claim a numerical installation rule, acceptance threshold or guaranteed measurement accuracy.
- Recheck official amendment pages for a live task; retain the contractually selected edition until a valid project instruction establishes a change.

Where an exact rule or field input is missing, identify the affected item as `NEEDS_SOURCE`. Continue the rest of the register and retain supported arithmetic as `CALCULATION_ONLY`.
