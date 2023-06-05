from datetime import datetime

from software.src.regression.quantile import quantile, make_formula
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

    if party:
        print("Running regression on party defection...")

        # Cleaning frame for party defection calculation
        # A deep copy of defection is used for this.

        frame = defection.copy()
        frame.dropna(subset=["party_defection", "national_party"], inplace=True)
        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

        # Dropping MEPs with no votes
        frame = frame[frame["quantity_votes_party"] > 0]

        # Normalizing values
        frame["party_country_ratio"] /= frame["party_country_ratio"].max()
        frame["quantity_votes_party"] /= frame["quantity_votes_party"].max()

        # Running regression
        print("---Running Party Defection Quantile Regression---")
        formula = make_formula(
            "party_defection",
            "party_country_ratio",
            "far_right",
            "quantity_votes_party",
            "incumbent",
            "C(country)",
        )

        fit = quantile(formula, frame)
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS / f"REGRESSION_{datetime.now().strftime('%Y%m%d%H%M%S')}_QUANTILE_PARTY.txt", "w+"
        ) as file:
            file.write(fit.summary().as_text())

        print("\tDone!\n")

    if group:
        print("Running regression on group defection...")

        # Cleaning frame for group defection calculation
        # A deep copy of defection is used for this.

        frame = defection.copy()
        frame.dropna(
            subset=["group_defection", "ep_group", "national_party"], inplace=True
        )
        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

        # Dropping MEPs with no votes
        frame = frame[frame["quantity_votes_group"] > 0]

        # Normalizing values
        frame["quantity_votes_group"] /= frame["quantity_votes_group"].max()
        frame["party_country_ratio"] /= frame["party_country_ratio"].max()

        # Running regression
        print("---Running Group Defection Quantile Regression---")
        formula = make_formula(
            "group_defection",
            "party_country_ratio",
            "far_right",
            "quantity_votes_group",
            "incumbent",
            "C(country)",
        )

        fit = quantile(formula, frame)
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS / f"REGRESSION_{datetime.now().strftime('%Y%m%d%H%M%S')}_QUANTILE_GROUP.txt", "w+"
        ) as file:
            file.write(fit.summary().as_text())
        print("\tDone!\n")

    if eurosceptic:
        print("Running regression on EPG Defection, including Eurosceptic control...")

        # Cleaning frame for eurosceptic defection calculation
        # A deep copy of defection is used for this.

        frame = defection.copy()
        frame.dropna(
            subset=["group_defection", "national_party", "ep_group"], inplace=True
        )
        frame["far_right"] = frame["ep_group"].isin(["IDG"])
        frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})
        frame["eurosceptic"] = frame["ep_group"].isin(["IDG", "ECR"])
        frame["eurosceptic"] = frame["eurosceptic"].replace({True: 1, False: 0})

        # Dropping MEPs with no votes
        frame = frame[frame["quantity_votes_party"] > 0]

        # Normalizing values
        frame["party_country_ratio"] /= frame["party_country_ratio"].max()
        frame["quantity_votes_group"] /= frame["quantity_votes_group"].max()

        # Running regression
        print("---Running Eurosceptic Defection Quantile Regression---")
        formula = make_formula(
            "group_defection",
            "party_country_ratio",
            "far_right",
            "eurosceptic",
            "quantity_votes_group",
            "incumbent",
            "C(country)",
        )

        fit = quantile(formula, frame)
        print(fit.summary(), end="\n\n")

        print("Saving results...")
        with open(
            REGRESSION_RESULTS
            / f"REGRESSION_{datetime.now().strftime('%Y%m%d%H%M%S')}_QUANTILE_EUROSCEPTIC.txt",
            "w+",
        ) as file:
            file.write(fit.summary().as_text())
        print("\tDone!\n")
