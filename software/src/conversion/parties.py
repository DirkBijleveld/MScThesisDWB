import pandas as pd


def correct_national_parties(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function replaces the various uses of "Independent" with None.
    This makes it easier to separate them from national party delegations.
    """
    df["national_party"].replace(
        {
            "-": None,
            "Independente": None,
            "Independent": None,
            "Independiente": None,
            "Indépendent": None,
        },
        inplace=True,
    )

    return df
