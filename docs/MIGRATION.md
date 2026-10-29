# Migration to Hong Kong I&M Quantity Surveying

## Current version

**v0.3.0-hk-im** renames the single entry from `hkqs-mode` to **`hk-im-qs`**, with the display name **Hong Kong I&M Quantity Surveying**. The six task playbooks, three domain references and evidence controls remain within the self-contained skill. This is an entry-name and folder change in the pre-1.0 series.

Version 0.2.0 introduced the single router; version 0.1.0 exposed seven specialist entries. Both older installation layouts are detected during upgrade.

| Previous entry | Current location |
|---|---|
| hkqs-mode (v0.2.0) | [hk-im-qs entry skill](../skills/hk-im-qs/SKILL.md), including all internal playbooks and references |
| hkqs-general | [Project basis](../skills/hk-im-qs/references/project-basis.md) and the [router](../skills/hk-im-qs/SKILL.md) |
| hkqs-instrumentation-monitoring | [I&M domain reference](../skills/hk-im-qs/references/domains/instrumentation-monitoring.md) |
| hkqs-ground-investigation | [GI domain reference](../skills/hk-im-qs/references/domains/ground-investigation.md) |
| hkqs-ground-improvement | [Ground-improvement domain reference](../skills/hk-im-qs/references/domains/ground-improvement.md) |
| hkqs-cost-estimation | [Estimate/compare playbook](../skills/hk-im-qs/playbooks/estimate-and-compare-quotes.md) |
| hkqs-valuation-variations | [Value progress](../skills/hk-im-qs/playbooks/value-progress.md), [assess change](../skills/hk-im-qs/playbooks/assess-change.md), and [shared valuation rules](../skills/hk-im-qs/references/valuation-rules.md) |
| hkqs-tender-review | [Review tender](../skills/hk-im-qs/playbooks/review-tender.md) |

Measurement and sourced document questions retain their dedicated task playbooks. The source register retains the same 18 official references and verification dates; renaming the entry does not re-verify every source or change a project's adopted edition.

## Upgrade an existing installation

1. Locate the actual active skills directory configured in your host. Inspect any previous `hkqs-mode` entry or the seven earlier `hkqs-*` entries listed above, and retain any local customisation.
2. Move those legacy entries to a backup directory **outside** the active skills directory. Keep copies if they contain local edits. If entries are symlinks, move the links themselves; do not follow them and move the repository's source directories. Broken legacy links still count as entries.
3. Inspect any existing `hk-im-qs` destination before replacing it; the installer deliberately refuses to overwrite it. Archive your previous copy outside the active directory if you want to install this version again.
4. From the updated repository, run the installer with your explicit target and `--dry-run`, then `--mode copy` or `--mode symlink` as appropriate. See [installation](../README.md#install-one-skill).
5. Verify that the active installation exposes one entry named `hk-im-qs` and that its playbooks and references are present. Use your host's normal skill refresh/discovery mechanism if needed.

The installer never deletes or archives user skills automatically. It detects `hkqs-mode` and all seven older names, including broken symlinks, and refuses to write until those entries are moved. Existing unrelated entries remain intact. Only the current `hk-im-qs` entry should be active for this package.

The former `/hkqs-mode` name is not installed as an alias. Update saved prompts or shortcuts to `/hk-im-qs` where your host uses slash commands.

For a fresh installation, install only `skills/hk-im-qs/`; all internal dependencies travel with it. Do not replace an entire existing skills directory with this repository.

## Provenance

The repository originates from [kuikiun/qs-skills](https://github.com/kuikiun/qs-skills), reviewed at `f7e43136b454ec7dba0d39c1ae70e8fb3e4a63fe`. Its ten ANZSMM and nine ACMM building/cost-management modules were replaced in v0.1.0 by the focused Hong Kong package at `50f47f2534a5ec227160fe9cd871f431bc877266`.

Version 0.2.0 consolidated the package under `hkqs-mode` at `dc86bbe393726cdd05f589a82f0cccb30f7f8e7e`. Version 0.3.0 uses the approved I&M-specific name.

The current router follows the architectural pattern of pstack's `poteto-mode`; exact references and adaptations are in [ROUTER-DESIGN.md](ROUTER-DESIGN.md). Original MIT attribution is retained in [LICENSE](../LICENSE). The licence covers repository instructions/code, not third-party standards or private project documents.

Prior versions remain in Git history. Australian numerical rules, cost examples or item codes were not relabelled as Hong Kong rules. General building-trade work remains outside this package.
