from __future__ import annotations

from dataclasses import dataclass, field

from .primitives import EntityState, EntityType


@dataclass
class Entity:
    id: str
    type: EntityType
    state: EntityState = EntityState.SPAWNED
    capabilities: set = field(default_factory=set)
    mailbox: list = field(default_factory=list)
    attention: float = 0.0


@dataclass
class State:
    entities: dict[str, Entity] = field(default_factory=dict)
    history: list[dict] = field(default_factory=list)
    clock: int = 0
