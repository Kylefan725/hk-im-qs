# Migration to the single HKQS entry

## Current version

**v0.2.0-hk-im** replaces the seven discoverable v0.1.0 skills with one self-contained `hkqs-mode` skill. The previous commercial and domain guidance is retained as internal playbooks and references. This is a breaking installation-layout change in the pre-1.0 series.

| Previous entry | New internal location |
|---|---|
| hkqs-general | [Project basis](../skills/hkqs-mode/references/project-basis.md) and the [router](../skills/hkqs-mode/SKILL.md) |
| hkqs-instrumentation-monitoring | [I&M domain reference](../skills/hkqs-mode/references/domains/instrumentation-monitoring.md) |
| hkqs-ground-investigation | [GI domain reference](../skills/hkqs-mode/references/domains/ground-investigation.md) |
| hkqs-ground-improvement | [Ground-improvement domain reference](../skills/hkqs-mode/references/domains/ground-improvement.md) |
| hkqs-cost-estimation | [Estimate/compare playbook](../skills/hkqs-mode/playbooks/estimate-and-compare-quotes.md) |
| hkqs-valuation-variations | [Value progress](../skills/hkqs-mode/playbooks/value-progress.md), [assess change](../skills/hkqs-mode/playbooks/assess-change.md), and [shared valuation rules](../skills/hkqs-mode/references/valuation-rules.md) |
| hkqs-tender-review | [Review tender](../skills/hkqs-mode/playbooks/review-tender.md) |

Measurement and sourced document questions now have explicit task playbooks. The source register retains the same 18 official references and verification dates; consolidating the workflow does not re-verify every source or change a project's adopted edition.

## Upgrade an existing installation

1. Locate the actual active skills directory configured in your host. Inspect the seven previous `hkqs-*` entries listed above and retain any local customisation.
2. Move those legacy entries to a backup directory **outside** the active skills directory. Keep copies if they contain local edits. If entries are symlinks, move the links themselves; do not follow them and move the repository's source directories. Broken legacy links still count as entries.
3. Inspect any existing `hkqs-mode` destination before replacing it; the installer deliberately refuses to overwrite it. Archive your previous copy outside the active directory if you want to install this version again.
4. From the updated repository, run the installer with your explicit target and `--dry-run`, then `--mode copy` or `--mode symlink` as appropriate. See [installation](../README.md#install-one-skill).
5. Verify that the active installation exposes one entry named `hkqs-mode` and that its playbooks and references are present. Use your host's normal skill refresh/discovery mechanism if needed.

The installer never deletes or archives user skills automatically. It detects all seven legacy names, including broken symlinks, and refuses to write until they are moved. Existing unrelated entries remain intact. Keeping the old skills active alongside the router would leave the fragmented interface in place, so this is not the default migration path.

For a fresh installation, install only `skills/hkqs-mode/`; all internal dependencies travel with it. Do not replace an entire existing skills directory with this repository.

## Provenance

The repository originates from [kuikiun/qs-skills](https://github.com/kuikiun/qs-skills), reviewed at `f7e43136b454ec7dba0d39c1ae70e8fb3e4a63fe`. Its ten ANZSMM and nine ACMM building/cost-management modules were replaced in v0.1.0 by the focused Hong Kong package at `50f47f2534a5ec227160fe9cd871f431bc877266`.

The current router follows the architectural pattern of pstack's `poteto-mode`; exact references and adaptations are in [ROUTER-DESIGN.md](ROUTER-DESIGN.md). Original MIT attribution is retained in [LICENSE](../LICENSE). The licence covers repository instructions/code, not third-party standards or private project documents.

Prior versions remain in Git history. Australian numerical rules, cost examples or item codes were not relabelled as Hong Kong rules. General building-trade work remains outside this package.
