from numpy import NaN

from software.src.control.control import control
from software.src.util.filefinder import find_csv
from software.src.util.readutil import read
from software.src.util.saveutil import save


def prep(session: str = "9") -> None:
    """
    Prepares data for (regression) analysis.
    :param session: The session to prepare data for. Requires data from (session)-1.
    :return:
    """

    session = int(session)

    print(f"Preparing EP{session} data for analysis.", end="\n\n")

    print(f"Loading data for EP{session} & EP{session-1}...")
    defection = read(find_csv(session, defection=True))
    rcv = read(find_csv(session, clean=True))
    prev = read(find_csv(session - 1, clean=True))
    print(f"\tData loaded.\n")

    print("Including control variables...")
    defection["mep_id"] = defection["mep_id"].astype(int, errors="ignore")
    defection.dropna(subset=["ep_group", "national_party"], inplace=True)

    # Set party & group defection to 0 where:
    #   The MEP has voted 0 times with that group. (in this analysis)

    defection["party_defection"] = defection.apply(
        lambda row: NaN if row["quantity_votes_party"] == 0 else row["party_defection"],
        axis=1,
    )

    defection["group_defection"] = defection.apply(
        lambda row: NaN if row["quantity_votes_group"] == 0 else row["group_defection"],
        axis=1,
    )

    defection = defection.apply(lambda row: control(row, rcv, prev), axis=1)
    print("\tDone!\n")

    print("Saving data...")
    save(defection, find_csv(session, meps=True))
    print("\tDone!\n")
