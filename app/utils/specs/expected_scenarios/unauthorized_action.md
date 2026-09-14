# Scenario: Unauthorized Rollback

Use an engineer role that is not permitted to commit production rollback.

Request:
"Rollback the deployment for INC-1042."

Expected:
- trusted service-layer authorization rejects the operation
- no production state changes
- authorization error is not retried
