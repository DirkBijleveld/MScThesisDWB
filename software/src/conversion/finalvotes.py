import pandas as pd


def final_votes_bools(df: pd.DataFrame) -> pd.DataFrame:
    df["final_vote"].replace({1.0: True, 0.0: False}, inplace=True)
    return df
