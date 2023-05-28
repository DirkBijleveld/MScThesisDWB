import pandas as pd

from software.src.util.filefinder import find_excel, find_csv


def convert_to_csv(session: int, doc_bool: bool = False) -> None:
    """
    Converts the given EP Session .xlsx to an intermediary .csv file in the predetermined location.
    :param session: (int) The session number.
    :param doc_bool: (bool) Whether to convert the docfile or the RCV file.
    :return: Nothing.
    """
    path = find_excel(session, doc_bool=doc_bool)
    df = pd.read_excel(path)
    csv_path = find_csv(session, intermediary=True, doc_bool=doc_bool)
    df.to_csv(csv_path, index=False)
