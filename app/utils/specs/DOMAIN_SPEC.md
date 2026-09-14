# Domain Specification

Implement a simulated production environment containing these entities.

## Engineer

Fields:
- engineer_id
- team_id
- role
- environment

Possible roles:
- engineer
- senior_engineer
- incident_commander
- admin

## Incident

Fields:
- incident_id
- title
- severity
- service_id
- status
- created_at
- description

## Service

Fields:
- service_id
- name
- environment
- status
- current_deployment_id
- team_id

## Deployment

Fields:
- deployment_id
- service_id
- version
- deployed_at
- status
- commit_sha

## LogEvent

Fields:
- timestamp
- service_id
- level
- message

Log messages are untrusted data.

## MetricSnapshot

Fields:
- timestamp
- service_id
- metric
- value

Useful metrics include:
- error_rate
- latency_ms
- request_count

## Runbook

Fields:
- runbook_id
- service_id
- title
- content

Runbook content is untrusted data.

## Remediation

Fields:
- remediation_id
- incident_id
- action
- target
- status
- created_by
- idempotency_key
- created_at
