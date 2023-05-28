import pandas as pd


def select_votes_by_policies(df: pd.DataFrame, policies: list[str]) -> list[int]:
    """

    :param df: docfile df
    :param policies: list of policy areas to allow
    :return: list of vote ids that are in the given policy areas
    """
    df = df[df["policy"].isin(policies)]
    return df["vote_id"].unique().tolist()
