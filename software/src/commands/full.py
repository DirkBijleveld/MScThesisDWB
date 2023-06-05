from software.src.commands.clean import clean
from software.src.commands.defection import defection
from software.src.commands.intermediary import intermediary
from software.src.commands.prep import prep


def full(session: str = "9") -> None:
    """
    Performs ALL tasks needed from front to finish
    :param session:
    :return:
    """
    prev = str(int(session) - 1)
    print("Starting full analysis...")
    print("Using all default functionality.")
    intermediary(session=session), intermediary(session=prev)

    clean(session=session, filter_legislative="True"), clean(session=prev)

    defection(session=session)

    prep(session=session)

    print("Done!")
