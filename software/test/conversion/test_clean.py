from software.src.conversion.clean import clean_rcv, clean_doc_file
from software.test.fixtures.docfiles import mini_doc, mini_doc_raw
from software.test.fixtures.rcvs import mini_rcv, mini_rcv_raw


def test_clean_rcv(mini_rcv, mini_rcv_raw):
    df = clean_rcv(mini_rcv_raw)
    assert df.equals(mini_rcv)


def test_clean_doc(mini_doc, mini_doc_raw):
    df = clean_doc_file(mini_doc_raw)
    assert df.equals(mini_doc)
