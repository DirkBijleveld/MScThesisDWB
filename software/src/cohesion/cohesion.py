from numpy import NaN

from software.src.cohesion.hix import agreement_index


def cohesion_or_nan(*args: int) -> float:
    """
    Return the cohesion of a group, or None if the group has no votes.
    """
    if sum(args) == 0:
        return NaN
    return agreement_index(*args)
