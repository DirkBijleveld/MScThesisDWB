from datetime import datetime

import numpy as np
from pandas.core import frame
from statsmodels.discrete.discrete_model import Logit
from statsmodels.formula.api import ols, quantreg, logit
from statsmodels.othermod.betareg import BetaModel
from statsmodels.regression.linear_model import GLS, WLS

from software.src.util.filefinder import find_csv
from software.src.util.pathutil import REGRESSION_RESULTS
from software.src.util.readutil import read


def regression(
    session: str = "9",
    party: str = "True",
    group: str = "True",
    eurosceptic: str = "True",
) -> None:
    session = int(session)
    party = party.lower() in ["true", "t", "1", "yes", "y"]
    group = group.lower() in ["true", "t", "1", "yes", "y"]
    eurosceptic = eurosceptic.lower() in ["true", "t", "1", "yes", "y"]

    print(f"Preparing to run OLS regression on EP{session} data.", end="\n\n")

    print(f"Loading data for EP{session}...")
    defection = read(find_csv(session, meps=True))
    print(f"\tData loaded.\n")

    frame = defection.copy()

    frame.dropna(
        subset=[
            "party_defection",
            "national_party",
            "party_size",
            "quantity_votes_party",
            "incumbent",
        ],
        inplace=True,
    )

    frame["far_right"] = frame["ep_group"].isin(["IDG"])
    frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

    frame["country_duration"] /= frame["country_duration"].max()

    frame["party_defection"] = np.sqrt(frame["party_defection"])
    frame["quantity_votes_party"] /= frame["quantity_votes_party"].max()
    frame["party_size"] /= frame["party_size"].max()

    frame = frame[frame["party_defection"] > 0.0]

    models = ols(
        "party_defection ~ "
        + "far_right + "
        + "C(country) + "
        + "incumbent + "
        + "party_country_ratio + "
        + "party_size +"
        + "quantity_votes_party",
        data=frame,
    )
    fit = models.fit()
    print(fit.summary(), end="\n\n")

    print("hi")
    print("Saving results...")


"""
    if party:
        print("Running OLS regression on party defection...")
        frame = defection.copy()
        frame.dropna(subset=["party_defection", "national_party"], inplace=True)

        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

        model = ols(
            "party_defection ~ "
            + "far_right + "
            + "C(country) +"
            + "incumbent + "
            + "country_duration + "
            + "party_country_ratio + "
            + "party_group_ratio",
            data=frame,
        )

        fit = model.fit()
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS / f"REGRESSION_{datetime.now()}_OLS_PARTY.txt", "w+"
        ) as file:
            file.write(fit.summary().as_text())
        print("\tDone!\n")

    if group:
        print("Running OLS regression on group defection...")
        frame = defection.copy()
        frame.dropna(subset=["group_defection", "ep_group"], inplace=True)

        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

        model = ols(
            "group_defection ~ "
            + "far_right + "
            + "incumbent + "
            + "country_duration + "
            + "quantity_votes_group + "
            + "party_country_ratio + "
            + "party_group_ratio",
            data=frame,
        )

        fit = model.fit()
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS / f"REGRESSION_{datetime.now()}_OLS_GROUP.txt", "w+"
        ) as file:
            file.write(fit.summary().as_text())
        print("\tDone!\n")

    if eurosceptic:
        print("Running OLS regression on eurosceptic defection...")
        frame = defection.copy()
        frame.dropna(subset=["group_defection", "ep_group"], inplace=True)

        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

        frame["eurosceptic"] = frame["ep_group"].isin(["IDG", "ECR"])
        frame["eurosceptic"] = frame["eurosceptic"].replace({True: 1, False: 0})

        model = ols(
            "group_defection ~ "
            + "far_right + "
            + "eurosceptic +"
            + "incumbent + "
            + "country_duration + "
            + "quantity_votes_party + "
            + "party_country_ratio + "
            + "party_group_ratio",
            data=frame,
        )

        fit = model.fit()
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS / f"REGRESSION_{datetime.now()}_OLS_EUROSCEPTIC.txt",
            "w+",
        ) as file:
            file.write(fit.summary().as_text())
        print("\tDone!\n")
"""
