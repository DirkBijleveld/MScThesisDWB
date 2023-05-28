import pandas as pd
from numpy import NaN, mean
from pandas import DataFrame, Series


def create_mep_row(
    mep_id: int, rcv: DataFrame, np_matrix: DataFrame, epg_matrix: DataFrame
) -> Series:
    votes = rcv[rcv["mep_id"] == mep_id].iloc[0, 7:]
    votes = votes[~votes.isna()]

    party = rcv[rcv["mep_id"] == mep_id]["national_party"].iloc[0]
    group = rcv[rcv["mep_id"] == mep_id]["ep_group"].iloc[0]

    party_defection_scores = []
    group_defection_scores = []

    party_cohesion_scores = []
    group_cohesion_scores = []

    for vote_id, vote in votes.items():
        vote = int(vote)
        if pd.isna(party) and pd.isna(group):
            break
        if pd.isna(party):
            party_defection = NaN
            party_cohesion = NaN
        else:
            party_defection = np_matrix.loc[vote_id, party][1][vote - 1]
            party_cohesion = np_matrix.loc[vote_id, party][2]

        if pd.isna(group):
            group_defection = NaN
            group_cohesion = NaN
        else:
            group_defection = epg_matrix.loc[vote_id, group][1][vote - 1]
            group_cohesion = epg_matrix.loc[vote_id, group][2]

        if not pd.isna(party_defection):
            party_defection_scores.append(party_defection)
        if not pd.isna(group_defection):
            group_defection_scores.append(group_defection)
        if not pd.isna(party_cohesion):
            party_cohesion_scores.append(party_cohesion)
        if not pd.isna(group_cohesion):
            group_cohesion_scores.append(group_cohesion)

    average_party_defection = (
        NaN if len(party_defection_scores) == 0 else mean(party_defection_scores)
    )

    average_group_defection = (
        NaN if len(group_defection_scores) == 0 else mean(group_defection_scores)
    )

    average_party_cohesion = (
        NaN if len(party_cohesion_scores) == 0 else mean(party_cohesion_scores)
    )

    average_group_cohesion = (
        NaN if len(group_cohesion_scores) == 0 else mean(group_cohesion_scores)
    )

    return Series(
        [
            mep_id,
            party,
            group,
            len(party_defection_scores),
            len(group_defection_scores),
            average_party_defection,
            average_group_defection,
            average_party_cohesion,
            average_group_cohesion,
        ],
        index=[
            "mep_id",
            "national_party",
            "ep_group",
            "quantity_votes_party",
            "quantity_votes_group",
            "party_defection",
            "party_cohesion",
            "group_defection",
            "group_cohesion",
        ],
    )


def create_mep_frame(
    rcv: DataFrame, np_matrix: DataFrame, epg_matrix: DataFrame
) -> DataFrame:
    mep_list = rcv["mep_id"].dropna().unique().tolist()
    columns = [
        "mep_id",
        "national_party",
        "ep_group",
        "quantity_votes_party",
        "quantity_votes_group",
        "party_defection",
        "party_cohesion",
        "group_defection",
        "group_cohesion",
    ]
    mep_frame = DataFrame(None, index=mep_list, columns=columns)
    print("\t", end="")
    for mep in mep_list:
        print("|", end="")
        mep_frame.loc[mep] = create_mep_row(mep, rcv, np_matrix, epg_matrix)
    return mep_frame
