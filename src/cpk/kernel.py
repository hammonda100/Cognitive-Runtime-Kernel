from __future__ import annotations

import asyncio

from .agent import act
from .events import Event
from .primitives import A_TOTAL, EntityState, EntityType, uid
from .reducers import EVENT_REDUCERS
from .state import Entity, State
from .world import WorldInterface


class Kernel:

    def __init__(self):
        self.state = State()
        self.world = WorldInterface()
        self.queue = []
        self._boot()


    def _boot(self):
        reasoner = Entity(
            id=uid(),
            type=EntityType.REASONER,
            state=EntityState.ACTIVE,
            capabilities={"SPAWN", "PLAN", "EXECUTE"},
            attention=20.0,
        )

        self.state.entities[reasoner.id] = reasoner

        self.queue.append(
            Event(
                id=uid(),
                typ="USER",
                src="USER",
                payload={"text": "compute 2+2"},
            )
        )


    def apply_event(self, event):
        reducer = EVENT_REDUCERS.get(event.typ)

        if reducer:
            self.state = reducer(self.state, event)

        self.state.clock += 1


    async def run(self):
        print("CPK Runtime Starting")
        print("=" * 40)

        while self.queue:
            event = self.queue.pop(0)

            print(f"EVENT -> {event.typ}")

            self.apply_event(event)

            for entity in self.state.entities.values():
                generated = act(self.state, entity, event, self.world)
                self.queue.extend(generated)

            await asyncio.sleep(0.1)

        print("Runtime Complete")


def main():
    kernel = Kernel()
    asyncio.run(kernel.run())
