from cpk.events import Event


def test_event_creation():
    e = Event(id="1", typ="TEST", src="root")
    assert e.typ == "TEST"
