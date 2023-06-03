from os import makedirs
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent.parent.parent / "data"

DOWNLOAD_DIR = DATA_DIR / "downloads"
makedirs(DOWNLOAD_DIR, exist_ok=True)

CSV_DIR = DATA_DIR / "csvs"
makedirs(CSV_DIR, exist_ok=True)

EXPORT_DIR = CSV_DIR / "export"
makedirs(EXPORT_DIR, exist_ok=True)

INTERMEDIARY_DIR = CSV_DIR / "intermediary"
makedirs(INTERMEDIARY_DIR, exist_ok=True)

DEFECTION_DIR = DATA_DIR / "defection"
makedirs(DEFECTION_DIR, exist_ok=True)

MEP_DIR = DATA_DIR / "meps"
makedirs(MEP_DIR, exist_ok=True)

VOTE_DIR = DATA_DIR / "votes"
makedirs(VOTE_DIR, exist_ok=True)

REGRESSION_RESULTS = Path(__file__).parent.parent.parent.parent / "regressionresults"
makedirs(REGRESSION_RESULTS, exist_ok=True)

BOXPLOTS = Path(__file__).parent.parent.parent.parent / "boxplots"
makedirs(BOXPLOTS, exist_ok=True)

CORRELATION = Path(__file__).parent.parent.parent.parent / "correlation"
makedirs(CORRELATION, exist_ok=True)


def refresh_readmes() -> None:
    """Refresh the README files."""
    if not (DATA_DIR / "readme.txt").is_file():
        with open(DATA_DIR / "readme.txt", "w") as file:
            file.write(
                "DIRECTORY STRUCTURE FOR DATA\n\n|\n|--> data\n      |\n      |--> downloads                Data as "
                "downloaded from VoteWatch EU (.xlsx, renamed)\n      |\n      |--> csvs                     Data as "
                ".csv files\n      |     |\n      |     |--> intermediary       Data as .csv files, intermediary "
                "format\n      |     |\n      |     |--> export             Data as .csv files, usable format\n      "
                "|\n      |--> defection                Aggregated defection data (for regression)\n      |\n      "
                "|--> meps                     Data on MEPs (for control variables)\n      |\n      |--> votes        "
                "            Data on votes"
            )
    if not (DOWNLOAD_DIR / "readme.txt").is_file():
        with open(DOWNLOAD_DIR / "readme.txt", "w") as file:
            file.write(
                "This folder contains .xlsx files as they are downloaded from the European University Institute "
                "website.\n Some changes are made to the files and filenames in order to use them.\nThis thesis "
                "exclusively uses the files for the 8th and 9th European Parliament Sessions.\n\nDownload url: "
                "https://cadmus.eui.eu/handle/1814/74918\n.zip download url (direct): "
                "https://cadmus.eui.eu/bitstream/handle/1814/74918/VoteWatch-EP-voting-data_2004-2022.zip?sequence=2"
                "&isAllowed=y\n\nFiles are renamed to match the following format:\n* EP[session number]_RCVs.xlsx - "
                "Files containing Roll Call Vote data\n* EP[session number]_Voted docs.xlsx - Files containing Vote "
                "Data\n\nThe following changes apply ONLY to the EP8_Voted docs.xlsx file,\nthe changes are needed "
                "due to mistakes made by the publishers of the .xlsx files.\nWithout these changes, the software does "
                'not function.\n1) Rename column 26 (Z) from "Final \\nvote?" to "Final vote?"\n    -> The "\\n" is '
                "erroneously included, but makes converting to .csv more difficult.\n2) Rename column 20 (T) from "
                '"De/Policy area" to "Policy area"\n\nYou may now proceed.'
            )


if __name__ == "__main__":
    refresh_readmes()
