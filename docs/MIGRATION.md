# Adaptation scope and provenance

## Upstream

- Repository: [kuikiun/qs-skills](https://github.com/kuikiun/qs-skills)
- Reviewed baseline commit: `f7e43136b454ec7dba0d39c1ae70e8fb3e4a63fe`
- Upstream structure: 10 ANZSMM building measurement skills and 9 ACMM cost-management skills.
- Licence: original MIT notice retained. It covers repository skill text, not third-party standards.

## Requested scope

The Hong Kong adaptation is limited to instrumentation and monitoring, associated ground investigation with instruments, and ground improvement with instruments. It does not preserve the original general building-trade curriculum.

| Upstream function | Focused replacement |
|---|---|
| General measurement | hkqs-general and adopted CEDD/project measurement basis |
| Building trade measurement | Removed from active skills; specialist I&M, GI and ground-improvement workflows added |
| Budgets and services pricing | hkqs-cost-estimation with specialist quotes, resources and service-period drivers |
| Construction cost management | hkqs-valuation-variations and hkqs-tender-review |
| ACMM element classifications and area rules | Removed from this package |
| Generic building life-cycle comparison | Removed; ownership, recurring monitoring/rental and close-out costs remain in specialist estimates |

New instructions are original workflow guidance. Australian numerical rules, item codes, cost examples, standard forms and area conventions were not relabelled as Hong Kong rules. Preserve the upstream baseline in Git history for provenance; it is not part of the active install set.

## Compatibility changes

All active skill names now start with `hkqs-`; the installer installs seven skills only. Install them together to preserve sibling references. Do not point an existing full skills directory at the repository root. Existing unrelated skills are not overwritten by the installer.

Source metadata was checked on 29 October 2026. The source register differentiates inspected text from verified metadata; neither automatically proves project incorporation. Modern monitoring/data services and treatment techniques may require bespoke measurement provisions.
