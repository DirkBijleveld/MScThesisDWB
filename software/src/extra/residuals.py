from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.regressionplots import plot_regress_exog

from software.src.util.filefinder import find_csv
from software.src.util.readutil import read


def main():
    frame = read(find_csv(9, meps=True))

    frame = frame.dropna(subset=["party_defection", "national_party", "ep_group"])
    frame["far_right"] = frame["ep_group"].isin(["IDG"])
    frame["far_right"] = frame["far_right"].replace({True: 1, False: 0})

    frame = frame[frame["quantity_votes_party"] > 0]
    frame = frame[frame["party_size"] > 2]

    frame["quantity_votes_party"] /= frame["quantity_votes_party"].max()

    model = ols("meserve_score_party ~ party_country_ratio + far_right + quantity_votes_party + incumbent + C(country)",
                data=frame).fit()

    print(model.summary())



if __name__ == "__main__":
    main()