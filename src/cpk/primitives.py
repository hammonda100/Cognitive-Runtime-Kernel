from __future__ import annotations

import time
import uuid
from enum import Enum


def uid() -> str:
    return str(uuid.uuid4())[:10]


def now() -> float:
    return time.time()


class EntityType(Enum):
    REASONER = "R"
    WORKER = "W"
    MEMORY = "M"
    TOOL = "T"
    POLICY = "P"


class EntityState(Enum):
    SPAWNED = 0
    ACTIVE = 1
    PAUSED = 2
    FAULTED = 3
    TERM = 4


A_TOTAL = 100.0
