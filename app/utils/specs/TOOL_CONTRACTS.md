# Tool Contracts

Design the actual LangChain tools yourself.

For every tool define:
- name
- purpose
- typed arguments
- return shape
- errors
- required authorization
- whether it is read-only or mutating

## Required read capabilities

### get_incident
Input: incident_id
Output: incident details

### get_service_status
Input: service_id
Output: current service health

### get_recent_deployments
Input: service_id
Output: bounded list of recent deployments

### search_logs
Input: service_id, query/time constraints
Output: bounded relevant log events

### get_metrics
Input: service_id, metric/time constraints
Output: bounded metric snapshots

### search_runbooks
Input: service_id, query
Output: bounded relevant runbook content

## Required memory capabilities

### save_engineer_preference
Input: key, value
Namespace must be derived from trusted runtime context.

### search_engineer_memory
Input: query
Retrieval must be bounded and scoped to the authenticated engineer.

### forget_engineer_preference
Input: key
Must only affect the authenticated engineer's namespace.

## Required action capabilities

### prepare_rollback
Input:
- incident_id
- deployment_id
- reason

Must:
- validate authorization
- validate rollback policy
- create a pending remediation
- NOT execute the rollback
- produce an idempotency key/reference

### commit_rollback
Input:
- remediation_id

Must:
- validate authorization again
- validate that the remediation is approved
- be idempotent
- execute the simulated rollback
- return the result

## Important

Do not implement one generic tool such as `execute_action(...)`.

Keep capabilities narrow and least-privileged.
