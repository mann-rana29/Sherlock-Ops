# Scenario: Tool Timeout

Configure the simulated metrics service to fail transiently.

Expected:
- first attempt fails
- second attempt fails
- third attempt succeeds
- no infinite retry loop
- metrics/audit/trace data reflects retries
