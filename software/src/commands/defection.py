from software.src.util.filefinder import find_csv
from software.src.util.readutil import read


def defection(
    session: str,
) -> None:
    session = int(session)
    print(f"Calculating defection scores for EP{session}...", end="\n\n")

    # Load data
    rcv = read(find_csv(session, clean=True))
    doc = read(find_csv(session, doc_bool=True, clean=True))
