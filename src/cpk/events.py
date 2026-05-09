from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Event:
    id: str
    typ: str
    src: str
    tgt: str | None = None
    payload: dict = field(default_factory=dict)
    cost: float = 0.0
    ttl: int = 5
