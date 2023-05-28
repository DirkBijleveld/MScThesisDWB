from pathlib import Path

import pandas as pd


def save(df: pd.DataFrame, path: Path) -> None:
    df.to_csv(path, index=False)
