import pytest

from software.src.util.filefinder import (
    construct_name,
    deconstruct_name,
    find_excel,
    find_csv,
    get_base_csv_path,
)
from software.src.util.pathutil import DOWNLOAD_DIR, INTERMEDIARY_DIR, EXPORT_DIR


def test_construct_name():
    assert construct_name(9, "xlsx") == "EP9_RCVs.xlsx"
    assert construct_name(9, "xlsx", doc_bool=True) == "EP9_Voted docs.xlsx"
    assert construct_name(9, "csv", intermediary=True) == "EP9_RCVs_INTERMEDIARY.csv"
    assert (
        construct_name(9, "csv", doc_bool=True, clean=True)
        == "EP9_Voted docs_CLEAN.csv"
    )
    assert (
        construct_name(6, "xlsx", doc_bool=True, intermediary=True)
        == "EP6_Voted docs_INTERMEDIARY.xlsx"
    )
    assert (
        construct_name(9, "csv", doc_bool=True, clean=True)
        == "EP9_Voted docs_CLEAN.csv"
    )
    with pytest.raises(ValueError):
        construct_name(9, "xlsx", intermediary=True, clean=True)


def test_deconstruct_name():
    assert deconstruct_name("EP6_RCVs.xlsx") == {
        "session": 6,
        "doc_bool": False,
        "intermediary": False,
        "clean": False,
        "defection": False,
        "suffix": "xlsx",
    }
    assert deconstruct_name("EP6_Voted docs.xlsx") == {
        "session": 6,
        "doc_bool": True,
        "intermediary": False,
        "clean": False,
        "defection": False,
        "suffix": "xlsx",
    }
    assert deconstruct_name("EP6_RCVs_INTERMEDIARY.xlsx") == {
        "session": 6,
        "doc_bool": False,
        "intermediary": True,
        "clean": False,
        "defection": False,
        "suffix": "xlsx",
    }
    assert deconstruct_name("EP8_Voted docs_INTERMEDIARY.xlsx") == {
        "session": 8,
        "doc_bool": True,
        "intermediary": True,
        "clean": False,
        "defection": False,
        "suffix": "xlsx",
    }
    assert deconstruct_name("EP8_Voted docs_CLEAN.xlsx") == {
        "session": 8,
        "doc_bool": True,
        "intermediary": False,
        "clean": True,
        "defection": False,
        "suffix": "xlsx",
    }
    assert deconstruct_name("EP9_Voted docs_CLEAN.csv") == {
        "session": 9,
        "doc_bool": True,
        "intermediary": False,
        "clean": True,
        "defection": False,
        "suffix": "csv",
    }
    with pytest.raises(ValueError):
        deconstruct_name("EPEIGHT_Voted docs_CLEAN.csv")


def test_find_excel():
    files = list(DOWNLOAD_DIR.glob("*.xlsx"))
    for file in files:
        info = deconstruct_name(file)
        assert find_excel(info["session"], doc_bool=info["doc_bool"]) == file


def test_get_base_csv_path():
    assert get_base_csv_path(intermediary=True, clean=False) == INTERMEDIARY_DIR
    assert get_base_csv_path(intermediary=False, clean=True) == EXPORT_DIR
    with pytest.raises(ValueError):
        get_base_csv_path(intermediary=True, clean=True)
        get_base_csv_path(intermediary=False, clean=False)


def test_find_csv():
    files = list(INTERMEDIARY_DIR.glob("*.csv"))
    for file in files:
        info = deconstruct_name(file)
        assert (
            find_csv(info["session"], doc_bool=info["doc_bool"], intermediary=True)
            == file
        )

    files = list(EXPORT_DIR.glob("*.csv"))
    for file in files:
        info = deconstruct_name(file)
        assert find_csv(info["session"], doc_bool=info["doc_bool"], clean=True) == file
