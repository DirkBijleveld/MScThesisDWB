from statistics import mode

import pandas as pd
from matplotlib import pyplot as plt
from numpy import mean

from software.src.cohesion.hix import agreement_index
from software.src.util.pathutil import FIGURES


def main():
    # Compute Cohesion, Meserve, and Defection (averages) for a group of 100 with: 100-0 through 0-100
    # Plot the results

    indices = [i for i in range(101)]

    df = pd.DataFrame(index=indices, columns=["Cohesion", "%SIDE", "Defection"])

    for i in indices:
        df.at[i, "Cohesion"] = agreement_index(100-i, i)

        votes = [1]*(100-i) + [0]*i

        meserve_list = []
        modal = mode(votes)
        for v in votes:
            if v == modal:
                meserve_list.append(0)
            else:
                meserve_list.append(1)

        df.at[i, "%SIDE"] = mean(meserve_list)
        if i == 50:
            df.at[i, "%SIDE"] = 0

        defection_list = []
        if i != 0 and i != 50 and i != 100:
            ai1 = agreement_index(99-i, i)
            ai2 = agreement_index(100-i, i-1)
            for v in votes:
                if v == 1:
                    if v == modal:
                        defection_list.append(0)
                    else:
                        defection_list.append(ai1)
                else:
                    if v == modal:
                        defection_list.append(0)
                    else:
                        defection_list.append(ai2)
            df.at[i, "Defection"] = mean(defection_list)
        elif i == 0:
            df.at[i, "Defection"] = 0
        elif i == 50:
            df.at[i, "Defection"] = 0
        elif i == 100:
            df.at[i, "Defection"] = 0




    plot = df.plot(xticks=[0, 50, 100])
    plot.grid(axis="x")

    plt.suptitle("Measures of Cohesion & Defection by vote-share")
    plt.xlabel("Percentage of MEPs Voting 'No'")

    plt.savefig(FIGURES / "cohesion-defection.png")


if __name__ == "__main__":
    main()
