import pandas as pd


def rename_rcv_file(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(
        columns={
            "WebisteEpID": "mep_id",
            "Fname": "name_first",
            "Lname": "name_last",
            "FullName": "name",
            "Country": "country",
            "Party": "national_party",
            "EPG": "ep_group",
        }
    )


def rename_doc_file(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(
        columns={
            "Vote ID": "vote_id",
            "Title": "title",
            "Policy area": "policy",
            "Final vote?": "final_vote",
        }
    )


def strip_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for column in columns:
        df[column] = df[column].str.strip()
    return df


def strip_rcv_file(df: pd.DataFrame) -> pd.DataFrame:
    return strip_columns(
        df,
        [
            "name_first",
            "name_last",
            "name",
            "country",
            "national_party",
            "ep_group",
        ],
    )


def strip_doc_file(df: pd.DataFrame) -> pd.DataFrame:
    return strip_columns(
        df,
        [
            "title",
            "policy",
        ],
    )
