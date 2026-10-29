# One entry, task playbooks and domain references

## User-facing change

`hk-im-qs` is the only discoverable skill. The user describes the result they need; the receiving agent owns routing, execution, evidence checking and one final answer. Internal playbooks and references are ordinary Markdown files, not additional skill entries.

Version 0.2.0 consolidated the seven v0.1.0 skills into one entry, then named `hkqs-mode`. Version 0.3.0 renames that entry to `hk-im-qs` and gives it the display name **Hong Kong I&M Quantity Surveying**. The task playbooks and domain guidance are retained inside the same self-contained skill.

## Reference implementation and provenance

The design was informed by the original `cursor/plugins` pstack at commit **`1ba91fc25c0977741dd0e267849e6234b037ed0a`**, reviewed on **29 October 2026**:

- [poteto-mode routing and execution instructions](https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/SKILL.md)
- [Investigation playbook](https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/playbooks/investigation.md)
- [Feature playbook](https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/playbooks/feature.md)
- [pstack manifest](https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/plugin.json) and [MIT licence](https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/LICENSE), copyright 2026 Lauren Tan.

This is an independently written QS adaptation of the workflow pattern. It is not an official pstack port, does not vendor pstack's source files, and does not require its plugin, host-specific commands, agent types or model configuration. The original `kuikiun/qs-skills` MIT notice remains in the repository licence.

## Routing contract

Route on the intended output before the construction discipline. A work-domain word chooses supporting knowledge; it does not dictate the task. Prefer one primary playbook and add only supporting steps that the deliverable requires.

| Ambiguous-looking request | Decision rule |
|---|---|
| Compare quotes / review quote compliance | Cost comparison selects estimating; specification compliance selects tender review |
| Measure monthly work / prepare monthly payment | A quantity-only answer selects measurement; a payment output selects valuation with measurement support |
| Budget extended monitoring / claim extended monitoring | Cost scenario selects estimating; entitlement/event assessment selects change |
| Explain an inclusion / price the included activity | Sourced answer selects document explanation; resource costing selects estimating |
| Multiple works packages | Reuse the requested workflow with separate package bases and relevant domain references |
| Multiple requested outputs | Compose dependency-ordered playbooks with one authoritative ledger |
| Resume after revised information | Rebuild only affected basis/outputs and invalidate their previous checks |

A route is an agent decision, not a keyword-matching CLI guarantee. A clear frontmatter description makes natural-language discovery possible where supported. Explicit skill selection is the most portable entry mechanism.

## Execution contract

Each playbook has Inputs, Steps, Outputs and Completion checks. The router reads the selected playbook in full, tracks each step, records a reason for a skipped step and defines observable completion before substantial work. Small questions use a proportionate internal checklist rather than a visible process report.

One project basis holds package IDs, document revisions, scope coverage, quantities, rate assumptions and evidence. A downstream estimate or valuation consumes that basis. It does not create its own conflicting version. Large/mixed tasks retain a resumable record with the user's project artifacts; confidential data is not written into this public repository.

Independent source, quantity or quote checks may run in parallel when the host supports them. The receiving agent owns shared totals and the integrated output. A reviewer receives the actual artifact and source evidence; agreement between agents is not a substitute for reconciliation. A host without delegation uses a separate self-check and does not claim independent review.

## Embedded execution and secondary guidance

The execution contract above describes standalone work. An explicit bounded host task selects [embedded execution](../skills/hk-im-qs/references/embedded-workflow.md). The host owns the stage, canonical artifacts, completion gates and output publication. The skill returns findings against the existing project basis and source identifiers. It does not create a second inventory or turn a tender addendum into a post-award claim.

Three original commercial checklists load only for pricing anomalies, risk allowances or historical-rate comparisons. [Guide provenance](../skills/hk-im-qs/references/guide-provenance.json) records the pinned secondary source, reviewed sections and excluded defaults. The guide is separate from the official-source register. Its instructions and numerical examples do not override the host task, adopted sources or source-text gate. The bundled checklists need no upstream repository at runtime.

## Verification contract

Completion is demonstrated by the requested work product: reproducible quantities, reconciled totals, comparable quotation scope, traceable clauses and correctly separated payment stages. The router inspects the actual result before declaring it complete.

Process step states and commercial row statuses are distinct. `checked` means a step's evidence was inspected. `READY_FOR_QS_REVIEW` means the row has support for review, not that the engineer approved it, the contract grants entitlement or a payment was certified. A requested draft may be complete with `NEEDS_SOURCE` rows if it clearly identifies unresolved decisions and amounts.

## Scope and permission controls

The package continues to cover only I&M, GI involving instruments and ground improvement involving instruments. Technical criteria remain engineer-owned. Rate inclusions, service denominators, repeat-work treatment, contract incorporation and prior certificates/cash remain explicit.

The router follows the existing session's permissions. It does not inherit pstack's external-action defaults. Drafting an RFI, quotation, notice or payment application does not authorise sending, submission or certification. For a sourced explanation, do only the explanatory work requested.

## Maintenance

Change the routing table and associated playbook when a real task reveals a gap. Preserve six task playbooks unless another distinct user outcome earns a new one; do not add a separate discoverable skill for each instrument, trade or contract form. Keep technical details in the relevant domain/source references and reuse them.

Run the structure/installation checks and meaningful fresh-context routing scenarios after changes. Structural validation proves packaging and references, not semantic routing accuracy, professional correctness or current source applicability.
