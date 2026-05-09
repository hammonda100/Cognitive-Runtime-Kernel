from .primitives import EntityState, EntityType, uid
from .state import Entity


def spawn_entity(state, parent_id, spec):
    entity_id = uid()

    entity = Entity(
        id=entity_id,
        type=EntityType(spec["et"]),
        state=EntityState.ACTIVE,
        capabilities=set(spec.get("caps", [])),
        attention=float(spec.get("attn", 1.0)),
    )

    state.entities[entity_id] = entity

    state.history.append({
        "type": "SPAWN",
        "entity": entity_id,
        "parent": parent_id,
    })

    return state, entity_id


def terminate_entity(state, entity_id):
    if entity_id in state.entities:
        state.entities[entity_id].state = EntityState.TERM

    state.history.append({
        "type": "TERMINATE",
        "entity": entity_id,
    })

    return state
