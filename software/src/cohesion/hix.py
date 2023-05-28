def agreement_index(*args: int | float) -> float:
    """
    Return the agreement index (Hix et al. 2005) of a group.
    """
    m = max(args)
    s = sum(args)
    if s == 0:
        raise ValueError(
            "Cannot determine an agreement index for a group with no votes."
        )
    if any(arg < 0 for arg in args):
        raise ValueError(
            "Cannot determine an agreement index for a group with negative votes."
        )

    """
    Agreement Index (AI) = (max[Y, N, A] - 0.5 * ((Y + N + A) - max[Y, N, A])) / (Y + N + A)
    See Hix et al. 2005, p. 215.
    """
    return (m - 0.5 * (s - m)) / s
