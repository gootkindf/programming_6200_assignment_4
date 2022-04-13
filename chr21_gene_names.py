"""
files   : chr21_gene_names.py
history : 1-Nov-2021

This python script loops through the provided .txt file (default:
chr21_genes.txt) to search for gene names provided by the user.

Sample command for executing program:

python3 chr21_gene_names.py -i chr21_genes.txt
"""

import argparse
from assignment4 import my_io


def main():
    """ Business Logic """
    infile = get_args()
    fh_in = my_io.get_fh(infile, 'r')
    while True:
        gene_s = (input("\nEnter gene name of interest. Type quit to exit: "
                        )).upper()
        if gene_s in ('EXIT', 'QUIT'):
            print('Thanks for querying the data.')
            break
        gene_info = identify(gene_s, fh_in)
        if gene_info is False:
            print('Not a valid gene name.')
        else:
            print(f'\n{gene_s} found! Here is the description:\n'
                  f'{gene_info[gene_s]["Description"]}')


def identify(gene, fh_in):
    """
    This function loops through the provided input file and returns a
    dictionary of dictionaries containing the description and category
    keyed to the gene name
    :param gene: the gene of interest
    :param fh_in: the file provided by the user
    :return: nested dictionary of description and category keyed to gene name
    """

    for line in fh_in:
        gene_p = line.split('\t')
        if gene_p[0] == gene:
            gene_info = {gene: {'Description': gene_p[1],
                                'Category': gene_p[2]}}
            return gene_info
    return False


def get_args():
    """
    This function parses the arguments given in command line and returns a
    filename or help menu
    :return: the infile to be read and the outfile to be printed to
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and'
                                                 ' ask user for a gene name')
    # Add arguments
    parser.add_argument('-i', '--infile',
                        dest='INFILE',
                        type=str,
                        help='Path to the file to open',
                        required=False)
    inf = parser.parse_args().INFILE
    if inf is None:
        inf = 'chr21_genes.txt'
    return inf


if __name__ == "__main__":
    main()
