"""Test suite for my_io.py"""

import os
import pytest
from assignment4.my_io import get_fh


# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

FILE_2_TEST = "test.txt"
FILE_2_TEST_PARSING = "test.fasta"
FASTA_STRING = """\
>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)
AACAGCACGGCAACGCTGTGCCTTGGGCACCANGCAGTACCAAACGGAACGATAGTGAAAACAATCACGA
ATGACCAAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGACAG
TCCTCATCAGATCCTTGATGGAGAAAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGTGAT
>EU521806 A/Arequipa/FLU3836/2006 2006// 4 (HA)
ATAAAAGCAACCAAAATGAAAGTAAAACTACTGGTTCTGTTATGTACATTTACAGCTACATATGCAGACA
TTTGGAGCCATTGCCGGTTTCATTGAAGGGGGGTGGACTGGAATGGTAGATGGTTGGTATGGTTATCATC
ATCAGAA
>EU521894 A/Arequipa/FLU3845/2006 2006// 4 (HA)
ACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCACGAATGACC
AGACCCAGAGTAAGGAATATCCCCAGCAGAATAAGCATCTATTGGACAATAGTAAAACCGGGAGACATAC
>EU521895 A/Arequipa/FLU3846/2006 2006// 4 (HA)
GACAACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAGTGAAAACAATCA
CGAATGACCAAATTGAAGTTACTAATGCTACTGAGCTGGTTCAGAGTTCCTCAACAGGTGAAATATGCGA
CAATCCTCATCAGATCCTTGATGGAGAGAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGT
"""
FILE_2_TEST_NT_STATS = "test.nucleotide_statistics_from_fasta.txt"


def test_existing_get_fh_4_reading():
    # does it open a file for reading
    # create a test file
    _create_test_file(FILE_2_TEST)
    # test
    test = get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    # does it open a file for writing
    # test
    test = get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_OSError():
    # does it raise OSError
    # this should exit
    with pytest.raises(OSError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise ValueError
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        get_fh("does_not_exist.txt", "rrr")
    os.remove(FILE_2_TEST)

def _create_test_file(file):
    # not actually run, the are just helper functions for the test script
    # create a test file
    open(file, "w").close()


def _create_test_fasta_file():
    fh = open(FILE_2_TEST_PARSING, "w")
    fh.write(FASTA_STRING)
    fh.close()
