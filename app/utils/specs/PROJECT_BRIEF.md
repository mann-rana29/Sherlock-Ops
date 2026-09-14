# IncidentOps AI — Capstone Project

## Goal

Build a production-style AI incident-response assistant for a fictional software company.

An engineer should be able to ask IncidentOps to investigate a production incident, collect evidence from internal systems, identify a likely root cause, recommend remediation, and—only after human approval—execute a consequential production action.

The infrastructure is simulated. Do not use real production systems.

## Core examples

- "Investigate incident INC-1042."
- "Why is payments-service returning 500s?"
- "Prepare a rollback for the deployment that caused INC-1042."
- "Remember that I prefer concise incident reports."

## Design principle

The LLM is an agentic decision-maker, not the security or transaction boundary.

Trusted application code must own:
- authentication context
- authorization
- business rules
- side-effect validation
- retries
- persistence of authoritative business records
- audit events

## Final system should demonstrate

- agent tool use
- deterministic workflow orchestration
- runtime context
- short-term thread persistence
- long-term memory
- bounded memory retrieval
- tenant/team isolation
- guardrails
- prompt-injection resistance
- human approval
- structured output
- timeout/retry handling
- audit logging
- metrics
- tests
