import pandas as pd
from matplotlib import pyplot as plt

from software.src.util.filefinder import find_csv
from software.src.util.readutil import read


def main():
    defection = read(find_csv(9, meps=True))

    defection = defection.dropna(subset=["group_defection", "group_cohesion", "ep_group"])

    group = defection.groupby("ep_group")[["group_defection", "group_cohesion"]].mean()
    plot = group.plot.scatter(x="group_defection", y="group_cohesion")
    plt.show()

    group = defection.groupby("ep_group")[["group_defection", "meserve_score_group"]].mean()
    plot = group.plot.scatter(x="group_defection", y="meserve_score_group")
    plt.show()
    print(group)



if __name__ == '__main__':
    main()