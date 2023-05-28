import pandas as pd


def identify_legislative_votes(df: pd.DataFrame) -> list[int]:
    """
    Identifies the legislative votes in the given DataFrame. Requires a docs file.
    :param df: The **CLEANED** docs DataFrame.
    :return: A list of vote IDs
    """
    df = df[df["final_vote"] == 1.0]
    return df["vote_id"].unique().tolist()
