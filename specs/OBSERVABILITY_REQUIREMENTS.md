# Observability Requirements

Implement three distinct concepts.

## Trace

Useful for execution/debugging:
- request
- model/tool decisions
- tool calls
- retries
- latency
- workflow transitions

## Audit event

Business record for sensitive operations.

At minimum capture:
- event type
- engineer_id
- team_id
- incident_id
- remediation_id when applicable
- timestamp
- outcome

## Metrics

Track at minimum:
- tool calls
- tool failures
- tool retries
- agent/workflow steps
- approval count
- rejection count
- investigation success/failure

Do not confuse traces with authoritative audit records.
