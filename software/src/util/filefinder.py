from pathlib import Path
from software.src.util.pathutil import DOWNLOAD_DIR, INTERMEDIARY_DIR, EXPORT_DIR


def construct_name(
    session: int,
    suffix: str,
    *,
    doc_bool: bool = False,
    intermediary: bool = False,
    clean: bool = False,
) -> str:
    """
    Constructs the name of the file for the given session, and the given parameters.
    :param session: (int) The session number.
    :param suffix: (str) The suffix of the file.
    :param doc_bool: (bool) Whether to construct the docfile or the RCV file.
    :param intermediary: (bool) Whether to construct an intermediary filename.
    :param clean: (bool) Whether to construct a clean filename.
    :return: (str) The name of the file.
    """
    if intermediary and clean:
        raise ValueError("Session file cannot be both intermediary and clean.")
    return (
        f"EP{session}_"
        + ("Voted docs" if doc_bool else "RCVs")
        + ("_INTERMEDIARY" if intermediary else "")
        + ("_CLEAN" if clean else "")
        + f".{suffix}"
    )


def deconstruct_name(file: str | Path) -> dict[str, bool | str | int]:
    """
    Deconstructs the name of the file for the given session, and the given parameters.
    :param file: (str) The name of the file.
    :return: (dict) The deconstructed information of the file.
    """
    if isinstance(file, Path):
        file = file.name

    suffix = file.split(".")[-1]
    file = file.removesuffix(f".{suffix}")
    file = file.split("_")
    session = int(file[0].removeprefix("EP"))
    doc_bool = "Voted docs" in file
    intermediary = "INTERMEDIARY" in file
    clean = "CLEAN" in file
    return {
        "session": session,
        "doc_bool": doc_bool,
        "intermediary": intermediary,
        "clean": clean,
        "suffix": suffix,
    }


def find_excel(session: int, doc_bool: bool = False) -> Path:
    """
    Finds the Excel file for the given session.
    Can find either the docfile or the RCV file.
    Raises an Exception if file does not exist.
    :param session: (int) The session number.
    :param doc_bool: (bool) Whether to find the docfile or the RCV file.
    :return: (Path) The path to the file.
    """

    path = DOWNLOAD_DIR / (construct_name(session, "xlsx", doc_bool=doc_bool))
    return path


def get_base_csv_path(intermediary: bool = False, clean: bool = False) -> Path:
    """
    Returns the base path for the CSV file.
    :param intermediary: (bool) Whether to find the intermediary file.
    :param clean: (bool) Whether to find the clean file.
    :return: (Path) The base path for the CSV file.
    """
    if intermediary and clean:
        raise ValueError("Session csv file cannot be both intermediary and clean.")
    if not intermediary and not clean:
        raise ValueError("Session csv file must be either intermediary or clean.")
    return INTERMEDIARY_DIR if intermediary else EXPORT_DIR


def find_csv(
    session: int,
    doc_bool: bool = False,
    intermediary: bool = False,
    clean: bool = False,
) -> Path:
    """
    Finds the CSV file for the given session.
    Can find either the docfile or the RCV file.
    Raises an Exception if file does not exist.
    :param session: (int) The session number.
    :param doc_bool: (bool) Whether to find the docfile or the RCV file.
    :param intermediary: (bool) Whether to find the intermediary file.
    :param clean: (bool) Whether to find the clean file.
    :return: (Path) The path to the file.
    """

    path = get_base_csv_path(intermediary=intermediary, clean=clean) / (
        construct_name(
            session,
            "csv",
            doc_bool=doc_bool,
            intermediary=intermediary,
            clean=clean,
        )
    )
    return path
