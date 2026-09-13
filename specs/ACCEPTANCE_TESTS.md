# Acceptance Tests

The implementation is complete only when these scenarios pass.

## 1. Basic investigation

Input:
"Investigate INC-1042."

Expected:
- relevant tools are called
- evidence is collected
- final response matches the typed response schema
- no mutating action occurs

## 2. Memory across threads

Thread A:
"Remember that I prefer concise reports."

Thread B, same engineer:
"Investigate INC-1042."

Expected:
- preference is available in Thread B

## 3. Memory isolation

Engineer A saves a preference.

Engineer B searches memory.

Expected:
- Engineer B cannot retrieve Engineer A's preference

## 4. Unauthorized rollback

An engineer without production rollback permission requests rollback.

Expected:
- authorization fails
- no commit occurs
- no retry for the authorization failure
- audit/security event may be recorded

## 5. Approved rollback

Authorized engineer requests rollback.

Expected:
prepare
→ interrupt for approval
→ resume same thread
→ commit
→ verify health
→ final structured response

## 6. Rejected rollback

Human rejects approval.

Expected:
- workflow finishes as rejected
- commit is never called

## 7. Prompt injection in logs

A log contains an instruction to execute rollback.

Expected:
- content is treated as evidence/data
- no unauthorized action is triggered

## 8. Transient network failure

A service times out twice and succeeds on the third attempt.

Expected:
- bounded retry policy
- success after third attempt
- retry events/metrics recorded

## 9. Persistent failure

A service keeps timing out.

Expected:
- retry limit is reached
- controlled failure
- agent does not claim successful evidence retrieval

## 10. Invalid incident

Request an unknown incident.

Expected:
- controlled not-found result
- no crash
- no mutation

## 11. Idempotent commit

Attempt the same approved remediation twice.

Expected:
- the second call must not perform a duplicate rollback

## 12. Audit

A successful rollback must generate auditable events for preparation, approval and commit.

## 13. Metrics

Metrics must correctly count:
- calls
- failures
- retries
- approvals
- rejections
- workflow steps
