from numpy import NaN
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy

from software.src.cohesion.cohesion import cohesion_or_nan
from software.src.cohesion.defection import multi_defection_scores


def create_grouped_defection_frame(
    grouped: DataFrameGroupBy, votes: list[int]
) -> DataFrame:
    group = list(grouped.groups.keys())
    frame = DataFrame(None, index=votes, columns=group)
    # Cell format: tuple[yes, no, abstain], tuple[defection_yes, defection_no, defection_abstain], cohesion, N. MEPs
    for g in group:
        print(f"\tCalculating defection matrix for '{g}'...")
        p = grouped.get_group(g)
        if len(p) <= 1:
            for vote in votes:
                frame.at[vote, g] = ((NaN, NaN, NaN), (NaN, NaN, NaN), NaN, NaN)
            continue

        for vote in votes:
            if str(vote) not in p.columns:
                frame.at[vote, g] = ((0, 0, 0), (NaN, NaN, NaN), NaN, NaN)
                continue
            vote_counts = p[str(vote)].value_counts()
            yes, no, abstain = (
                vote_counts.get(1.0, 0),
                vote_counts.get(2.0, 0),
                vote_counts.get(3.0, 0),
            )
            total_votes = yes + no + abstain
            frame.at[vote, g] = (
                (yes, no, abstain),
                multi_defection_scores((yes, no, abstain)),
                cohesion_or_nan(yes, no, abstain),
                total_votes,
            )
    return frame
