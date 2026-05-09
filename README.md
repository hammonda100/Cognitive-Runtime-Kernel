# CPK — Constitutional Cognitive Runtime Kernel

CPK is an experimental event-driven cognitive runtime implementing:

- UCRC v0.2
- ECL v0.1

Core concepts:

- deterministic event execution
- constitutional constraints
- capability-based cognition
- bounded attention economics
- replayable runtime state
- provider-agnostic cognition

## Quick Start

## Setup

1. Clone:
   git clone https://github.com/yourusername/cpk.git
2. Enter project directory:
   cd cpk
3. Create virtual environment:
   python -m venv .venv
4. Activate venv:
   source .venv/bin/activate  # macOS/Linux
   .\.venv\Scripts\activate   # Windows
5. Install dependencies:
   pip install -r requirements.txt
6. Run setup wizard:
   python -m cpk setup
```bash
git clone <repo>
cd cpk

pip install -e .[dev]

python -m cpk
```

## Development

```bash
pytest -v
```

## Project Structure

```text
src/cpk/
├── kernel.py
├── reducers.py
├── events.py
├── state.py
├── world.py
├── providers/
└── runtime/
```

## Status

Early runtime prototype.

## License

MIT
