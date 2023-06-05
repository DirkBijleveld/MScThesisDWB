from matplotlib import pyplot as plt

from software.src.plots.boxplot import create_boxplot
from software.src.util.filefinder import find_csv
from software.src.util.pathutil import BOXPLOTS
from software.src.util.readutil import read


def boxplot(
    session: str = "9",
    party: str = "True",
    group: str = "True",
    outliers: str = "False",
    eurosceptic: str = "True",
    cohesion: str = "True",
) -> None:
    session = int(session)
    party = party.lower() in ["true", "t", "1", "yes", "y"]
    group = group.lower() in ["true", "t", "1", "yes", "y"]
    outliers = outliers.lower() in ["true", "t", "1", "yes", "y"]
    eurosceptic = eurosceptic.lower() in ["true", "t", "1", "yes", "y"]
    cohesion = cohesion.lower() in ["true", "t", "1", "yes", "y"]

    print(
        f"Preparing to create box plot images on defection measures for EP{session} data."
    )

    print(f"Loading data for EP{session}...")
    defection = read(find_csv(session, meps=True))
    print(f"\tData loaded.\n")

    if party:
        print("Creating box plot for party defection...")

        frame = defection.copy()
        frame["ID"] = frame["ep_group"].isin(["IDG"])
        frame["ID"] = frame["ID"].replace({True: "Far-Right", False: "Other"})

        create_boxplot(
            frame,
            y="party_defection",
            x="ID",
            caption="Party Defection by Far-Right Affiliation",
            outliers=outliers,
            ylabel="Party Defection Score",
            xlabel="Far-Right Affiliation",
            labels=["Far-Right", "Other"],
            colors=["#b50505", "#54d7e8"],
            ymax=0.025,
        )
        plt.savefig(BOXPLOTS / "boxplot_party_defection.png")
        print("Box plot for party defection saved.\n")

    if group:
        print("Creating box plot for group defection...")

        frame = defection.copy()
        frame["ID"] = frame["ep_group"].isin(["IDG"])
        frame["ID"] = frame["ID"].replace({True: "Far-Right", False: "Other"})

        create_boxplot(
            frame,
            y="group_defection",
            x="ID",
            caption="EPG Defection by Far-Right Affiliation",
            outliers=outliers,
            ylabel="EPG Defection Score",
            xlabel="Far-Right Affiliation",
            labels=["Far-Right", "Other"],
            colors=["#b50505", "#54d7e8"],
            ymax=0.25,
        )
        plt.savefig(BOXPLOTS / "boxplot_group_defection.png")
        print("Box plot for group defection saved.\n")

    if eurosceptic:
        print("Creating box plot for eurosceptic defection...")

        frame = defection.copy()
        frame.loc[frame["ep_group"] == "IDG", "EPG"] = "ID"
        frame.loc[frame["ep_group"] == "ECR", "EPG"] = "ECR"
        frame.loc[~frame["ep_group"].isin(["IDG", "ECR"]), "EPG"] = "Other"

        create_boxplot(
            frame,
            y="group_defection",
            x="EPG",
            caption="EPG Defection by Party Group",
            outliers=outliers,
            ylabel="EPG Defection Score",
            xlabel="EPG",
            labels=["ECR", "ID", "Other"],
            colors=["#e8b754", "#b50505", "#54d7e8"],
            order=[1, 0, 2],
        )
        plt.savefig(BOXPLOTS / "boxplot_eurosceptic_defection_epg.png")
        print("Box plot for eurosceptic defection saved.\n")

        create_boxplot(
            frame,
            y="party_defection",
            x="EPG",
            caption="Party Defection by Party Group",
            outliers=outliers,
            ylabel="Party Defection Score",
            xlabel="EPG",
            labels=["ECR", "ID", "Other"],
            colors=["#e8b754", "#b50505", "#54d7e8"],
            order=[1, 0, 2],
        )
        plt.savefig(BOXPLOTS / "boxplot_eurosceptic_defection_party.png")
        print("Box plot for eurosceptic defection saved.\n")

    if cohesion:
        if party:
            print("Creating box plot for party cohesion...")

            frame = defection.copy()
            frame["ID"] = frame["ep_group"].isin(["IDG"])
            frame["ID"] = frame["ID"].replace({True: "Far-Right", False: "Other"})

            create_boxplot(
                frame,
                y="party_cohesion",
                x="ID",
                caption="Party Cohesion by Far-Right Affiliation",
                outliers=outliers,
                ylabel="Party Cohesion Score",
                xlabel="Far-Right Affiliation",
                labels=["Far-Right", "Other"],
                colors=["#b50505", "#54d7e8"],
            )
            plt.savefig(BOXPLOTS / "boxplot_party_cohesion.png")
            print("Box plot for party cohesion saved.\n")

        if group:
            print("Creating box plot for group cohesion...")

            frame = defection.copy()
            frame["ID"] = frame["ep_group"].isin(["IDG"])
            frame["ID"] = frame["ID"].replace({True: "Far-Right", False: "Other"})

            create_boxplot(
                frame,
                y="group_cohesion",
                x="ID",
                caption="EPG Cohesion by Far-Right Affiliation",
                outliers=outliers,
                ylabel="EPG Cohesion Score",
                xlabel="Far-Right Affiliation",
                labels=["Far-Right", "Other"],
                colors=["#b50505", "#54d7e8"],
            )
            plt.savefig(BOXPLOTS / "boxplot_group_cohesion.png")
            print("Box plot for group cohesion saved.\n")

        if eurosceptic:
            print("Creating box plot for eurosceptic cohesion...")

            frame = defection.copy()
            frame.loc[frame["ep_group"] == "IDG", "EPG"] = "ID"
            frame.loc[frame["ep_group"] == "ECR", "EPG"] = "ECR"
            frame.loc[~frame["ep_group"].isin(["IDG", "ECR"]), "EPG"] = "Other"

            create_boxplot(
                frame,
                y="group_cohesion",
                x="EPG",
                caption="EPG Cohesion by Party Group",
                outliers=outliers,
                ylabel="EPG Cohesion Score",
                xlabel="EPG",
                labels=["ECR", "ID", "Other"],
                colors=["#e8b754", "#b50505", "#54d7e8"],
                order=[1, 0, 2],
            )
            plt.savefig(BOXPLOTS / "boxplot_eurosceptic_cohesion_epg.png")
            print("Box plot for eurosceptic cohesion saved.\n")

            create_boxplot(
                frame,
                y="party_cohesion",
                x="EPG",
                caption="Party Cohesion by Party Group",
                outliers=outliers,
                ylabel="Party Cohesion Score",
                xlabel="EPG",
                labels=["ECR", "ID", "Other"],
                colors=["#e8b754", "#b50505", "#54d7e8"],
                order=[1, 0, 2],
            )
            plt.savefig(BOXPLOTS / "boxplot_eurosceptic_cohesion_party.png")
            print("Box plot for eurosceptic cohesion saved.\n")