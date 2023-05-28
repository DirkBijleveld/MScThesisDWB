from software.src.conversion.clean import clean_rcv, clean_doc_file
from software.src.selection.legislative import identify_legislative_votes
from software.src.selection.votes import select_votes
from software.src.util.filefinder import find_csv
from software.src.util.readutil import read
from software.src.util.saveutil import save


def clean(
    session: str,
    doc_only: str = "False",
    rcv_only: str = "False",
    filter_legislative: str = "True",
) -> None:
    """
    Converts the given EP Session .csv to a clean .csv file in the predetermined location.
    :param session: (int) The session number.
    :param doc_only: (str->bool) Whether to convert the docfile.
    :param rcv_only: (str->bool) Whether to only convert the RCV file (Mutually exclusive with doc_only).
    :param filter_legislative: (str->bool) Whether to filter out legislative votes.
    :return: Nothing.
    """
    session = int(session)
    doc_only = doc_only.lower() == "true"
    rcv_only = rcv_only.lower() == "true"
    filter_legislative = filter_legislative.lower() == "true"

    if doc_only and rcv_only:
        raise ValueError(
            "Cannot create a clean file for neither the RCV or the DOC file."
        )

    print(f"Performing cleaning operations on EP{session} data.", end="\n\n")

    if not rcv_only:
        print("Cleaning Documentation file...")
        df = read(find_csv(session, doc_bool=True, intermediary=True))
        print(f"\tDocumentation file found. Cleaning {len(df)} rows...")
        df = clean_doc_file(df)
        print(f"\tDone! Saving file...")
        save_path = find_csv(session, doc_bool=True, clean=True)
        save(df, save_path)
        print(f"\tFile saved to {save_path.absolute()}", end="\n\n")

    if not doc_only:
        print("Cleaning RCV file...")
        df = read(find_csv(session, intermediary=True))
        print(
            f"\tRCV file found. Cleaning {len(df)} rows and {len(df.columns)} columns..."
        )
        df = clean_rcv(df)
        print(f"\tCleaned!")
        if filter_legislative:
            print(
                f"\tFiltering out legislative votes.\n\tThis can be disabled by using the filter_legislative=False flag."
            )
            doc = read(find_csv(session, doc_bool=True, clean=True))
            legislative_votes = identify_legislative_votes(doc)
            df = select_votes(df, legislative_votes)
            print(f"\tFiltered!")
        print(f"\tSaving file...")
        save_path = find_csv(session, clean=True)
        save(df, save_path)
        print(f"\tFile saved to {save_path.absolute()}", end="\n\n")
