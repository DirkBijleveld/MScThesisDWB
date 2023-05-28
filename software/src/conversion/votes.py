import numpy as np
import pandas as pd


def simplify_votes(df: pd.DataFrame) -> pd.DataFrame:
    # Replace every value that is not 1, 2, or 3 with None
    df.iloc[:, 7:] = df.iloc[:, 7:].replace({4: np.NaN, 5: np.NaN, 6: np.NaN})
    return df
