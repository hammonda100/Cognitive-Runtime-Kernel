from cpk.constraints import check_constraints
from cpk.state import State


def test_constraints_exist():
    assert check_constraints(State()) == []
