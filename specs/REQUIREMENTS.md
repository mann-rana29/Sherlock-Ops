# Requirements

## Functional requirements

1. Authenticate every request with trusted runtime context.
2. Investigate incidents using multiple read-only capabilities.
3. Retrieve relevant logs, metrics, deployments and runbooks.
4. Allow engineers to save and retrieve explicit preferences.
5. Support preparation of a production rollback.
6. Require human approval before committing a production rollback.
7. Resume interrupted workflows using the same thread.
8. Verify service health after a committed rollback.
9. Return a typed final incident report.
10. Record sensitive business events in an audit log.

## Minimum capabilities

Investigation:
- get incident
- get service status
- get recent deployments
- search logs
- get metrics
- search runbooks

Memory:
- save preference
- search memory
- forget preference

Actions:
- prepare rollback
- commit rollback

## Non-functional requirements

- typed inputs and outputs
- tenant/team authorization
- bounded retrieval
- retry only transient failures
- no unbounded retries
- no unauthorized side effects
- no secrets in logs
- deterministic policy checks near side effects
- graph state is execution context, not the business database
