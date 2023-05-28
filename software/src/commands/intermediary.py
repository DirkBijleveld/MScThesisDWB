from software.src.util.filefinder import find_excel, find_csv
from software.src.util.readutil import read
from software.src.util.saveutil import save


def intermediary(
    session: str, doc_only: str = "False", rcv_only: str = "False"
) -> None:
    """
    Converts the given EP Session .xlsx to an intermediary .csv file in the predetermined location.
    :param session: (int) The session number.
    :param doc_only: (bool) Whether to convert the docfile.
    :param rcv_only: (bool) Whether to only convert the RCV file (Mutually exclusive with doc_only).
    :return: Nothing.
    """
    session = int(session)
    doc_only = doc_only.lower() == "true"
    rcv_only = rcv_only.lower() == "true"

    if doc_only and rcv_only:
        raise ValueError(
            "Cannot create an intermediary file for neither the RCV or the DOC file."
        )

    print(f"Converting EP{session} data files to .csv", end="\n\n")

    if not doc_only:
        print("Converting RCV file...")
        xlsx = find_excel(session)
        df = read(xlsx)
        print("\tRCV file loaded. Saving intermediary file as .csv...")
        save_path = find_csv(session, intermediary=True)
        save(df, save_path)
        print(f"\tFile saved to {save_path.absolute()}", end="\n\n")

    if not rcv_only:
        print("Converting Documentation file...")
        xlsx = find_excel(session, doc_bool=True)
        df = read(xlsx)
        print("\tDocumentation file loaded. Saving intermediary file as .csv...")
        save_path = find_csv(session, doc_bool=True, intermediary=True)
        save(df, save_path)
        print(f"\tFile saved to {save_path.absolute()}", end="\n\n")
