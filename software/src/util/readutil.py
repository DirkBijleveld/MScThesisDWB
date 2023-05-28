from pathlib import Path

import pandas as pd


def read(path: Path) -> pd.DataFrame:
    """
    Performs the pandas read_*** functions based on given file extension.
    :param path: (Path) The path to the file to read.
    :return: (pd.DataFrame) The DataFrame of the given file.
    """
    match path.suffix:
        case ".csv":
            return pd.read_csv(path)
        case ".xlsx":
            return pd.read_excel(path)
