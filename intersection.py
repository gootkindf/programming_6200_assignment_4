"""
file    : intersection.py
history : 3-Nov-2021

This program reads through two .txt files containing a set of gene symbols in
the first column. It then parses these lines, creates sets containing all gene
symbols in each file, and checks for shared gene symbols. The shared gene
symbols are added to a common set and removed from the two prior sets. The
program then prints out the number of unique and common gene symbols and
prints and ordered list of the common gene symbols to the .txt file
OUTPUT/intersection_output.txt.

Sample command

python3 intersection.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
"""

import argparse
from assignment4 import my_io


def main():
    """Business logic"""
    args = get_args()
    gene_f1 = my_io.get_fh(args[0], 'r')
    gene_f2 = my_io.get_fh(args[1], 'r')
    gene_s1 = get_genes(gene_f1)
    gene_s2 = get_genes(gene_f2)
    common = find_common(gene_s1, gene_s2)[0]
    new_file = 'OUTPUT/intersection_output.txt'
    outfile = open(new_file, 'w')
    print(f'Number of unique genes in {gene_f1.name}: {len(gene_s1)}')
    print(f'Number of unique genes in {gene_f2.name}: {len(gene_s2)}')
    print(f'Number of common symbols found: {len(common)}')
    set_ord = order_set(common)
    for gene in set_ord:
        outfile.write(f'{gene}\n')
    outfile.close()
    print(f'Output stored in {new_file}')


def order_set(in_set):
    """
    This function creates a list of the common gene symbols from the common
    set, orders them, then returns the ordered list.
    :param in_set: The set of common gene symbols
    :return: Ordered list of the gene symbols
    """
    set_ord = []
    for element in in_set:
        set_ord.append(element)
    set_ord.sort()
    return set_ord


def find_common(gene_s1, gene_s2):
    """
    This function accepts two arguments in the form of sets containing the
    genes found in each dataset provided. It then looks for common genes
    between the two sets and adds common genes to a single set called
    common_set, while also removing them from the two provided sets. It then
    returns the common_set and the amended sets containing only genes unique
    to each set.
    :param gene_s1: Gene symbols found in the first dataset
    :param gene_s2: Gene symbols found in the second dataset
    :return: The set of gene symbols found in both sets and the amended
    original sets
    """
    common_set = set()
    for gene in gene_s1.copy():
        if gene in gene_s2:
            common_set.add(gene)
            gene_s1.remove(gene)
            gene_s2.remove(gene)
    return common_set, gene_s1, gene_s2


def get_genes(gene_l):
    """
    This function reads through the file containing the genes of interest. It
    skips the header line and adds the gene symbols to a set of gene symbols
    found in the file (avoiding duplicates in the file).
    :param gene_l: The file containing the genes of interest
    :return: A set containing all unique gene symbols in that file.
    """
    gene_set = set()
    for line in gene_l.readlines()[1:]:
        gene_p = line.split('\t')
        gene_set.add(gene_p[0])
    return gene_set


def get_args():
    """
    This function parses the arguments given in command line and returns
    filenames or help menu
    :return: the infiles to be read and compared.
    """
    parser = argparse.ArgumentParser(description='Provide two gene list '
                                                 '(ignore header line), find '
                                                 'intersection')
    # Add arguments
    parser.add_argument('-i1', '--infile1',
                        dest='INFILE1',
                        type=str,
                        help='Gene list 1 to open',
                        required=True)
    parser.add_argument('-i2', '--infile2',
                        dest='INFILE2',
                        type=str,
                        help='Gene list 2 to open',
                        required=True)
    inf = [parser.parse_args().INFILE1, parser.parse_args().INFILE2]
    return inf


if __name__ == "__main__":
    main()
