# Contributing to CPK

## Setup

```bash
git clone <repo>
cd cpk
pip install -e .[dev]
pytest
```

## Principles

CPK prioritizes:

- deterministic execution
- event-sourced state mutation
- constitutional constraints
- replayability
- provider-agnostic cognition

## Pull Requests

Please:

- include tests
- avoid hidden mutation
- preserve determinism
- document architectural changes
