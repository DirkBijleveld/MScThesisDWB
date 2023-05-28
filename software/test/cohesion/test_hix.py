import pytest


from software.src.cohesion.hix import agreement_index


def test_agreement_index():
    # Tests whether the agreement index is calculated correctly.
    # Uses some pre-calculated values.
    assert agreement_index(1, 0, 0) == 1.0
    assert agreement_index(1.0, 0.0, 0) == 1  # Can combine float and int.
    assert agreement_index(1, 1, 0) == 0.25
    assert agreement_index(1, 1, 1) == 0
    with pytest.raises(ValueError):
        agreement_index(0, 0, 0)

    with pytest.raises(ValueError):
        agreement_index(-1, 6, 2)

    assert agreement_index(10, 0, 5) == 0.5
    assert (
        agreement_index(105, 55, 12)
        == 0.4156976744186046511627906976744186046511627906976744186046511627
    )
