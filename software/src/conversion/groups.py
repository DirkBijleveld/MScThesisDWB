import pandas as pd


def correct_epgs(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function makes the non-Inscrits (NI) not a part of any EPG (rather than it being an EPG).
    :param df: The RCV df.
    :return: The RCV df with the NI EPG removed.
    """
    df["ep_group"].replace(
        {
            "NI": None,
            "Non-attached Members": None,
        },
        inplace=True,
    )
    return df
