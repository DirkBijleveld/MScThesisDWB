import pandas as pd
from pytest import fixture


@fixture
def mini_doc() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "vote_id": [1, 2, 3, 4, 5, 6, 7, 8],
            "title": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "policy": ["Z", "Z", "X", "X", "X", "Y", "Z", "X"],
            "final_vote": [True, False, True, False, False, False, False, True],
        }
    )


@fixture
def mini_doc_raw() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Vote ID": [1, 2, 3, 4, 5, 6, 7, 8],
            "File": [
                "FILE_A",
                "FILE_B",
                "FILE_C",
                "FILE_D",
                "FILE_E",
                "FILE_F",
                "FILE_G",
                "FILE_H",
            ],
            "Order of vote": [1, 1, 1, 1, 1, 1, 1, 1],
            "Date": ["DATE", "DATE", "DATE", "DATE", "DATE", "DATE", "DATE", "DATE"],
            "Title": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "Procedure": [
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
                "PROCEDURE",
            ],
            "Leg/Non-Leg/Bud": ["LEG", "LEG", "BUD", "LEG", "LEG", "LEG", "NON", "LEG"],
            "Type of Vote": [
                "TYPE",
                "TYPE",
                "TYPE",
                "TYPE",
                "TYPE",
                "TYPE",
                "TYPE",
                "TYPE",
            ],
            "Policy area": ["Z", "Z", "X", "X", "X", "Y", "Z", "X"],
            "Final vote?": [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        }
    )
