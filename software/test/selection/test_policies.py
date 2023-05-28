from software.src.selection.policy import select_votes_by_policies
from software.test.fixtures.docfiles import mini_doc


def test_select_votes_by_policies(mini_doc):
    assert select_votes_by_policies(mini_doc, ["X", "Y"]) == [3, 4, 5, 6, 8]
