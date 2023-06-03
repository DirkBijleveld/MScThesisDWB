from datetime import datetime

import numpy as np
from pandas.core import frame
from statsmodels.discrete.discrete_model import Logit
from statsmodels.formula.api import ols, quantreg, logit, glm
from statsmodels.genmod.families import Binomial
from statsmodels.othermod.betareg import BetaModel
from statsmodels.regression.linear_model import GLS, WLS

from software.src.util.filefinder import find_csv
from software.src.util.pathutil import REGRESSION_RESULTS
from software.src.util.readutil import read

import pymc3 as pm
import arviz as az


def best(
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

    frame["far_right"] = frame["ep_group"].isin(["IDG"])
    frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

    frame = frame[frame["quantity_votes_party"] > 0]

    frame["party_size"] /= frame["party_size"].max()
    frame["party_country_ratio"] /= frame["party_country_ratio"].max()
    frame["quantity_votes_party"] /= frame["quantity_votes_party"].max()

    with pm.Model() as model:

