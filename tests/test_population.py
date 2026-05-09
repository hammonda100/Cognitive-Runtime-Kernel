from cpk.population import spawn_entity
from cpk.state import State


def test_spawn_entity():
    state = State()

    state, eid = spawn_entity(
        state,
        "root",
        {
            "et": "W",
            "caps": ["EXECUTE"],
            "attn": 1,
        },
    )

    assert eid in state.entities
