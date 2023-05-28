import pandas as pd


def slice_rcv(df: pd.DataFrame) -> pd.DataFrame:
    begin = df[
        [
            "mep_id",
            "name_first",
            "name_last",
            "name",
            "country",
            "national_party",
            "ep_group",
        ]
    ]
    end = df.iloc[:, 10:]
    return pd.concat([begin, end], axis=1)
