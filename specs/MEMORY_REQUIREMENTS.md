# Memory Requirements

Implement long-term engineer preferences.

Example:

Engineer A:
"Remember that I prefer concise incident reports."

Later, using a new thread:
"Investigate INC-1042."

The agent should be able to use the preference.

## Isolation

Engineer A must not see Engineer B's preferences.

Different teams must not share private engineer memory.

## Retrieval

Do not dump all memories into the prompt.

Retrieve only relevant memories and impose a result limit.

## Correction

A newer explicit preference should replace the current preference.

The system must support forgetting a preference.

## Separation

- graph state/checkpointer = current execution/thread
- Store = durable application memory
- domain data = authoritative operational records
