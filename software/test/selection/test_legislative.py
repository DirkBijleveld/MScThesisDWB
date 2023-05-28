from software.src.selection.legislative import identify_legislative_votes

from software.test.fixtures.docfiles import mini_doc


def test_identify_legislative_votes(mini_doc):
    """
    This test grabs a test docs df and sees if the function returns the right vote IDs.
    :return:
    """
    assert identify_legislative_votes(mini_doc) == [1, 3, 8]
