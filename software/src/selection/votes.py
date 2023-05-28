import pandas as pd


def select_votes(df: pd.DataFrame, votes: list[int]) -> pd.DataFrame:
    """
    Selects the votes from the DataFrame that are in the given list.
    :param df: RCVs df
    :param votes: list of votes
    :return: RCVs df with only the votes in the list
    """
    votes = [str(vote) for vote in votes]
    start = df.iloc[:, :7]
    end = df.iloc[:, 7:]
    end = end.drop(columns=[col for col in end if col not in votes])
    return pd.concat([start, end], axis=1)
