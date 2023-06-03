import pandas as pd

from software.src.util.filefinder import find_csv
from software.src.util.pathutil import CORRELATION
from software.src.util.readutil import read


def correlation(session: str = "9") -> None:
    session = int(session)

    print(
        f"Preparing to create correlation matrices on defection measures for EP{session} data."
    )

    print(f"Loading data for EP{session}...")
    defection = read(find_csv(session, meps=True))
    print(f"\tData loaded.\n")

    print("Creating correlation matrix for Party defection...")
    meps = defection[["party_defection", "party_cohesion"]].corr()

    party = (
        defection.groupby("national_party")[["party_defection", "party_cohesion"]]
        .mean()
        .corr()
    )
    group = (
        defection.groupby("ep_group")[["party_defection", "party_cohesion"]]
        .mean()
        .corr()
    )
    party_corr_mep = meps.at["party_defection", "party_cohesion"]
    party_corr_party = party.at["party_defection", "party_cohesion"]
    party_corr_group = group.at["party_defection", "party_cohesion"]

    print(f"Creating correlation matrix for EPG defection...")

    meps = defection[["group_defection", "group_cohesion"]].corr()

    party = (
        defection.groupby("national_party")[["group_defection", "group_cohesion"]]
        .mean()
        .corr()
    )

    group = (
        defection.groupby("ep_group")[["group_defection", "group_cohesion"]]
        .mean()
        .corr()
    )

    group_corr_mep = meps.at["group_defection", "group_cohesion"]
    group_corr_party = party.at["group_defection", "group_cohesion"]
    group_corr_group = group.at["group_defection", "group_cohesion"]

    print("Saving correlation matrices...")

    df = pd.DataFrame(
        {
            "": ["MEP Aggregate", "Party Aggregate", "EPG Aggregate"],
            "Party Defection": [party_corr_mep, party_corr_party, party_corr_group],
            "EPG Defection": [group_corr_mep, group_corr_party, group_corr_group],
        }
    )

    df.to_csv(CORRELATION / f"correlation_matrix_ep{session}.csv", index=False)

    print("Done!")
