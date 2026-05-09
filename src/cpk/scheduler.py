def select_next(state):
    for entity in state.entities.values():
        if entity.mailbox:
            return entity
    return None
