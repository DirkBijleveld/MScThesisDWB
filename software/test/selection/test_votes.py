from software.src.selection.legislative import identify_legislative_votes
from software.src.selection.policy import select_votes_by_policies
from software.src.selection.votes import select_votes
from software.test.fixtures.docfiles import mini_doc
from software.test.fixtures.rcvs import mini_rcv


def test_select_votes(mini_doc, mini_rcv):
    assert (
        len(select_votes(mini_rcv, identify_legislative_votes(mini_doc)).columns) == 10
    )
    assert (
        len(select_votes(mini_rcv, select_votes_by_policies(mini_doc, ["X"])).columns)
        == 11
    )

    df = select_votes(mini_rcv, select_votes_by_policies(mini_doc, ["X"]))
    assert len(select_votes(df, identify_legislative_votes(mini_doc)).columns) == 9
