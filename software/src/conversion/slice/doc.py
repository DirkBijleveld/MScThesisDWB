import pandas as pd


def slice_doc_file(df: pd.DataFrame) -> pd.DataFrame:
    return df[
        [
            "vote_id",
            "title",
            "policy",
            "final_vote",
        ]
    ]
