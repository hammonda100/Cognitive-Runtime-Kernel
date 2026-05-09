from .events import Event
from .primitives import uid


def act(state, entity, event, world):
    if event.typ == "USER":
        return [
            Event(
                id=uid(),
                typ="SPAWN",
                src=entity.id,
                payload={
                    "spec": {
                        "et": "W",
                        "caps": ["EXECUTE"],
                        "attn": 5,
                    }
                },
            )
        ]

    return []
