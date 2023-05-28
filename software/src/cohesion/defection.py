from numpy import NaN

from software.src.cohesion.hix import agreement_index


def is_modal_vote(vote_code: int, vote_quantities: tuple[int, int, int]) -> bool:
    """
    Check if the vote is (one of) the modal vote(s).
    :param vote_code: (int) The vote code of the vote to check. 1 = yes, 2 = no, 3 = abstain.
    :param vote_quantities: (tuple) The vote quantities of the vote to check.
    :return: (bool) Whether the vote is (one of) the modal vote(s).
    """
    if vote_code not in (1, 2, 3):
        raise ValueError("Vote code must be 1, 2, or 3.")
    # Determine the quantity of the modal vote code(s)
    max_vote_quantity = max(vote_quantities)
    # Reindex the vote code to be 0-indexed
    vote_code_indexed = vote_code - 1
    # Return whether the vote quantity of the vote code is the same as the modal vote quantity.
    # Doing it this way is clean and accounts for the possibility of a vote having multiple vote codes at max.
    return vote_quantities[vote_code_indexed] == max_vote_quantity


def defection_score(vote_code: int, vote_quantities: tuple[int, int, int]) -> float:
    if vote_code not in (1, 2, 3):
        raise ValueError("Vote code must be 1, 2, or 3.")
    vote_code_indexed = vote_code - 1
    adj_vote_quantities = [q for q in vote_quantities]
    adj_vote_quantities[vote_code_indexed] -= 1
    adj_vote_quantities = tuple(adj_vote_quantities)

    # A quick check to make sure no vote quantities are negative
    if any(q < 0 for q in adj_vote_quantities):
        raise ValueError(
            "Cannot calculate defection score for a vote with negative vote quantities."
        )
    if sum(adj_vote_quantities) == 0:
        raise ValueError("Cannot calculate defection score for a vote with no votes.")

    # Determine the presence of defection
    # If the vote is modal, there is no defection
    if is_modal_vote(vote_code, vote_quantities):
        return 0.0
    # Otherwise the defection score is the adj. AI
    return agreement_index(*adj_vote_quantities)


def multi_defection_scores(
    vote_quantities: tuple[int, int, int]
) -> tuple[float, float, float]:
    if sum(vote_quantities) in (0, 1):
        return NaN, NaN, NaN

    defection_yes = (
        NaN if vote_quantities[0] == 0 else defection_score(1, vote_quantities)
    )
    defection_no = (
        NaN if vote_quantities[1] == 0 else defection_score(2, vote_quantities)
    )
    defection_abstain = (
        NaN if vote_quantities[2] == 0 else defection_score(3, vote_quantities)
    )

    return defection_yes, defection_no, defection_abstain
