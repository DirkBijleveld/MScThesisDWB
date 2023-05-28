from software.src.cohesion.frames import create_grouped_defection_frame
from software.src.cohesion.frames.mep import create_mep_frame
from software.src.util.filefinder import find_csv
from software.src.util.readutil import read
from software.src.util.saveutil import save


def defection(
    session: str,
) -> None:
    session = int(session)
    print(f"Calculating defection scores for EP{session}...", end="\n\n")

    # Load data
    print("Loading RCV data...")
    rcv = read(find_csv(session, clean=True))
    votes = rcv.columns[7:]

    # Create defection matrices for EPG and national parties.
    # Note that these CANNOT be saved as intermediaries due to having Python objects in cells.
    # (I also won't figure out another way to do this)
    print("Creating defection matrices...")
    print("\tDefection matrices for national parties...")
    rcv_grouped_np = rcv.groupby("national_party")
    rcv_np_matrix = create_grouped_defection_frame(rcv_grouped_np, votes)
    print("\tDefection matrices for EPGs...")
    rcv_grouped_epg = rcv.groupby("ep_group")
    rcv_epg_matrix = create_grouped_defection_frame(rcv_grouped_epg, votes)
    print("\tDone!")

    print("Creating MEP defection scores...")
    mep_defection_scores = create_mep_frame(rcv, rcv_np_matrix, rcv_epg_matrix)
    print("\tDone!")

    print("Saving MEP defection scores...")
    save(mep_defection_scores, find_csv(session, defection=True))
    print("\tDone!")
