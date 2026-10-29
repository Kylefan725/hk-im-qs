# Answer a sourced document question

Answer the user's question about a requirement, measurement rule, rate inclusion, edition, interface or contract provision. Keep the deliverable proportionate: a cited answer can finish the task without a BOQ, estimate, claim or multi-agent plan.

## Inputs

Use [project basis](../references/project-basis.md) for evidence rules and [source register](../references/source-register.json) to locate official publications. Load only the domain/source notes needed for the question. Obtain the relevant adopted document, edition/revision, particular amendments and supplied extract. For a generic question, state the edition being discussed rather than demanding an entire project file set.

## Steps

1. **Identify the decision.** Restate the precise question internally: what is included, how an item is measured, which version applies, which party owns an interface or what a provided clause means. Respect “explain only” and distinguish a general explanation from a determination under a particular contract.
2. **Locate the applicable evidence.** Inspect supplied clauses, schedules and amendments first. Use official publisher documents for external verification; inspect enough surrounding definitions, preambles and cross-references to understand coverage. Use authorised copies for licensed material. A source-register entry or search snippet alone does not prove the required clause.
3. **Separate requirements from consequences.** Distinguish technical requirements, measured units, inclusive rate coverage, internal cost and contractual entitlement. For GI instrument-installation questions, inspect the adopted `CEDD-SMM-1992` provisions and particular amendments before deciding whether calibration, maintenance or readings are separately payable. For modern ADMS, obtain the actual particular schedule when the standard does not resolve the unit.
4. **Resolve conflicts and uncertainty.** Apply the actual precedence/incorporation clauses if available. Record which document/revision conflicts and what would resolve it. Explain conditional interpretations where evidence is incomplete; do not silently select the newest standard or manufacture a clause number. For a request to set alarm limits or authorise resumption, identify the engineer-approved control documents needed and stay within supported QS/document analysis.
5. **Answer and verify.** Lead with the supported answer, cite exact source title/edition and clause/page where actually read, explain the practical effect and identify a specific remaining evidence gap if material. Check that citations support the claim and that no assumption has been presented as the official rule. If this is a supporting question inside a larger workflow, return its finding and status to that workflow without expanding the user's requested output.

## Outputs

Provide a concise sourced explanation or the requested comparison table. Cite user-supplied files by their actual file/page/clause and official web sources by verified URLs. Use `READY_FOR_QS_REVIEW` for a supported project-facing interpretation, `NEEDS_SOURCE` where the adopted rule is unavailable/conflicting, and `CALCULATION_ONLY` for any hypothetical arithmetic. Keep labels in the working record if displaying them would clutter a simple general explanation; never hide material uncertainty.

## Completion checks

- The answer addresses the actual question at the requested depth.
- Each specific rule or contractual conclusion has inspected evidence, correct applicability and a traceable citation.
- Technical obligation, payment coverage and an internal cost allowance are not conflated.
- Conditional statements and unresolved project amendments are visible; source metadata has not been treated as full-text verification.
- No unsolicited BOQ, quotation, variation submission, engineering criterion or external action was produced.
