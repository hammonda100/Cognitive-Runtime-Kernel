from .population import spawn_entity, terminate_entity


def reduce_spawn(state, event):
    spec = event.payload.get("spec", {})
    return spawn_entity(state, event.src, spec)[0]


def reduce_terminate(state, event):
    return terminate_entity(state, event.tgt)


EVENT_REDUCERS = {
    "SPAWN": reduce_spawn,
    "TERMINATE": reduce_terminate,
}
