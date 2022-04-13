#!/usr/bin/env python3
"""
File   :  pdb_fasta_splitter.py

This program takes in a fasta file with Protein sequence and
and secondary structure information and splits the same into two
output files.

Sample command for executing the program:

python3 pdb_fasta_splitter.py -i ss.txt
"""


import sys


def get_fh(file=None, mode=None):
    """
    filehandle : get_fh(infile, "r")
    Takes : 2 arguments file name and mode i.e. what is needed to be done with
    this file. This function opens the file based on the mode passed in
    the argument and returns filehandle.
    @:param file: The file to open for the mode
    @:param mode: They way to open the file, e.g. reading, writing, etc
    @return: filehandle
    """

    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
