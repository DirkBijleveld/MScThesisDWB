from pandas import Series, DataFrame


def control(row: Series, rcv: DataFrame, prev: DataFrame) -> Series:
    mep_id = row["mep_id"]
    mep_info = rcv[rcv["mep_id"] == mep_id].iloc[0]

    # Is the MEP incumbent? (1 = yes, 0 = no)
    incumbent = 1 if len(prev[prev["mep_id"] == mep_id]) == 1 else 0

    # Determine how many MEPs are in this national party
    national_party_size = len(rcv[rcv["national_party"] == mep_info["national_party"]])
    country_size = len(rcv[rcv["country"] == mep_info["country"]])
    party_country_ratio = national_party_size / country_size

    # Relative party group size
    party_group_size = len(rcv[rcv["ep_group"] == mep_info["ep_group"]])
    party_group_ratio = national_party_size / party_group_size

    # Duration that country has been in EP (in # of sessions)
    country_duration_dict = {
        "Belgium": 9,
        "Ireland": 9,
        "Denmark": 9,
        "Germany": 9,
        "Italy": 9,
        "Luxembourg": 9,
        "Netherlands": 9,
        "United Kingdom": 9,
        "France": 9,
        "Greece": 8,
        "Spain": 7,
        "Portugal": 7,
        "Austria": 5,
        "Finland": 5,
        "Sweden": 5,
        "Cyprus": 4,
        "Czech Republic": 4,
        "Estonia": 4,
        "Hungary": 4,
        "Latvia": 4,
        "Lithuania": 4,
        "Malta": 4,
        "Poland": 4,
        "Slovakia": 4,
        "Slovenia": 4,
        "Bulgaria": 3,
        "Romania": 3,
        "Croatia": 2,
    }

    country_duration = country_duration_dict[mep_info["country"]]

    return Series(
        {
            "incumbent": incumbent,
            "national_party": row["national_party"],
            "ep_group": row["ep_group"],
            "country": mep_info["country"],
            "country_duration": country_duration,
            "quantity_votes_party": row["quantity_votes_party"],
            "quantity_votes_group": row["quantity_votes_group"],
            "party_size": national_party_size,
            "largest_party_size": row["largest_party_size"],
            "largest_group_size": row["largest_group_size"],
            "party_country_ratio": party_country_ratio,
            "party_group_size": party_group_size,
            "party_group_ratio": party_group_ratio,
            "party_defection": row["party_defection"],
            "party_cohesion": row["party_cohesion"],
            "group_defection": row["group_defection"],
            "group_cohesion": row["group_cohesion"],
            "meserve_score_party": row["meserve_score_party"],
            "meserve_score_group": row["meserve_score_group"],
        }
    )
