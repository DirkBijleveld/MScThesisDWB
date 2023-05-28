import pytest
from numpy import NaN

from software.src.cohesion.defection import (
    is_modal_vote,
    defection_score,
    multi_defection_scores,
)


def test_is_modal_vote():
    assert is_modal_vote(1, (5, 0, 0))
    assert is_modal_vote(2, (0, 5, 0))
    assert is_modal_vote(3, (0, 0, 5))
    assert is_modal_vote(1, (5, 5, 0))
    assert is_modal_vote(2, (5, 5, 5))
    assert not is_modal_vote(3, (0, 5, 3))
    assert is_modal_vote(1, (0, 0, 0))
    with pytest.raises(ValueError):
        is_modal_vote(0, (0, 0, 0))


def test_defection_score():
    assert defection_score(1, (5, 0, 0)) == 0.0
    assert defection_score(2, (0, 5, 0)) == 0.0
    assert defection_score(1, (5, 5, 0)) == 0.0

    assert defection_score(1, (1, 5, 0)) == 1.0
    assert defection_score(2, (2, 1, 2)) == 0.25
    assert defection_score(3, (1, 2, 1)) == 0.5

    with pytest.raises(ValueError):
        defection_score(0, (0, 0, 0))

    with pytest.raises(ValueError):
        defection_score(4, (1, 2, 3))

    with pytest.raises(ValueError):
        defection_score(1, (0, 0, -1))


def test_multi_defection_scores():
    assert multi_defection_scores((1, 1, 1)) == (0.0, 0.0, 0.0)
    assert multi_defection_scores((1, 2, 3)) == (0.4, 0.4, 0.0)
    assert multi_defection_scores((0, 2, 1)) == (NaN, 0.0, 1.0)
    assert multi_defection_scores((0, 0, 0)) == (NaN, NaN, NaN)

    with pytest.raises(ValueError):
        multi_defection_scores((0, 0, -1))
