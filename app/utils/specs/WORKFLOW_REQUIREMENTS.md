# Workflow Requirements

## Investigation

The system must be able to perform this conceptual flow:

START
→ load incident
→ identify affected service
→ collect evidence
→ analyze evidence
→ produce incident assessment
→ determine whether remediation is needed
→ END or enter remediation workflow

You must decide which steps are agentic and which should be deterministic.

## Remediation

Required conceptual flow:

request
→ validate incident/deployment
→ prepare rollback
→ human approval
→ commit rollback
→ verify service health
→ final report

Approval outcomes:
- approve
- reject

Rejected actions must produce no production side effect.

## Persistence

An interrupted workflow must resume from the same thread.

Do not depend on process-local variables for workflow state.

## Recovery

If verification fails after a rollback, the system should produce a controlled failure state rather than claiming the incident is resolved.
