import pandas as pd
from pytest import fixture


@fixture
def mini_rcv() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "mep_id": [1, 2, 3],
            "name_first": ["Marie", "Hank", "Gustav"],
            "name_last": ["Smith", "Johnson", "Williams"],
            "name": ["SMITH, Marie", "JOHNSON, Hank", "WILLIAMS, Gustav"],
            "country": ["Germany", "France", "Italy"],
            "national_party": ["CDU", "PS", "Lega"],
            "ep_group": ["EPP", "S&D", "ID"],
            "1": [1, 1, 1],
            "2": [2, 2, 2],
            "3": [3, 3, 3],
            "4": [1, 1, None],
            "5": [2, 2, 2],
            "6": [3, 3, 3],
            "7": [1, 1, 1],
            "8": [None, 2, 2],
        }
    )


@fixture
def mini_rcv_raw() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "WebisteEpID": [1, 2, 3],
            "Fname": ["Marie", "Hank", "Gustav"],
            "Lname": ["Smith", "Johnson", "Williams"],
            "FullName": ["SMITH, Marie", "JOHNSON, Hank", "WILLIAMS, Gustav"],
            "Country": ["Germany", "France", "Italy"],
            "Party": ["CDU", "PS", "Lega"],
            "EPG": ["EPP", "S&D", "ID"],
            "Activ": [1, 1, 1],
            "Start": ["DATE", "DATE", "DATE"],
            "End": ["DATE", "DATE", "DATE"],
            "1": [1, 1, 1],
            "2": [2, 2, 2],
            "3": [3, 3, 3],
            "4": [1, 1, 5],
            "5": [2, 2, 2],
            "6": [3, 3, 3],
            "7": [1, 1, 1],
            "8": [4, 2, 2],
        }
    )
