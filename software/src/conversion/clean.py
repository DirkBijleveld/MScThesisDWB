import pandas as pd

from software.src.conversion.columns import (
    rename_rcv_file,
    strip_rcv_file,
    rename_doc_file,
    strip_doc_file,
)
from software.src.conversion.finalvotes import final_votes_bools
from software.src.conversion.groups import correct_epgs
from software.src.conversion.parties import correct_national_parties
from software.src.conversion.slice.doc import slice_doc_file
from software.src.conversion.slice.rcv import slice_rcv
from software.src.conversion.votes import simplify_votes


def clean_rcv(df: pd.DataFrame) -> pd.DataFrame:
    # Create the FullName Column if it does not exist.
    print("\tRenaming columns...")
    if "FullName" not in df.columns:
        print("\tFullName column not found. Creating...")
        df["FullName"] = df["Lname"] + ", " + df["Fname"]
    df = rename_rcv_file(df)
    df = strip_rcv_file(df)
    print("\tCorrecting EPG affiliations...")
    df = correct_epgs(df)
    print("\tCorrecting national party affiliations...")
    df = correct_national_parties(df)
    df = df[df["country"] != "United Kingdom"]
    print("\tRemoving unnecessary columns...")
    df = slice_rcv(df)
    print("\tChanging vote values...")
    df = simplify_votes(df)
    return df


def clean_doc_file(df: pd.DataFrame) -> pd.DataFrame:
    print("\tRenaming columns...")
    df = rename_doc_file(df)
    df = strip_doc_file(df)
    print("\tRemoving unnecessary columns...")
    df = slice_doc_file(df)
    print("\tChanging value types...")
    df = final_votes_bools(df)
    return df
