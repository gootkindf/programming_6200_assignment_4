"""
files   : categories.py
history : 1-Nov-2021

This program takes two arguments: INFILE1, the text file to be read, and
INFILE2, the text file providing the gene classifications. This program reads
through the chr21_genes.txt file and the chr21_genes_categories.txt file. It
then classifies all genes in the chr21_genes.txt file and returns the total
number of genes of each classification.

Sample command for executing program:

python3 chr21_gene_names.py -i chr21_genes.txt
"""

import argparse
from assignment4 import my_io


def main():
    """Business logic."""
    args = get_args()
    genes = my_io.get_fh(args[0], 'r')
    cats = my_io.get_fh(args[1], 'r')
    categories = cat_count(cats)  # Dictionary of dictionaries
    get_counts(genes, categories)
    file_name = 'OUTPUT/categories.txt'
    outfile = open(file_name, 'w')
    make_output(outfile, categories)
    outfile.close()


def make_output(outfile, to_write):
    """
    This function first outputs the category, occurrence, and description
    headers in a tab separated format to the outfile. It then reads through
    the dictionary counting up the gene categories and prints the key, Count,
    and Description of each dictionary entry to the outfile.
    :param outfile: The file being written to.
    :param to_write: Writing the dictionary entries to the .txt file
    """
    outfile.write('Category\tOccurrence\tDescription\n')
    for key in to_write:
        outfile.write(f"{key}\t{to_write[key]['Count']}\t"
                      f"{to_write[key]['Description']}\n")


def cat_count(cats):
    """
    This function creates a dictionary entry containing the count, initially
    set to 0, and description of a gene keyed to the gene classification.
    :param cats: The .txt file containing the gene categories
    :return: A dictionary containing the gene category as key and the count
    and description of that gene.
    """
    gene_cats = {}
    for line in cats:
        cat_read = line.split('\t')
        gene_cats[cat_read[0]] = {'Count': 0, 'Description': cat_read[1].rstrip('\n')}
    return gene_cats


def get_counts(genes, categories):
    """
    This function receives the file containing the list of all chr21 genes and
    the dictionary of dictionaries containing all gene categories. It then
    counts up the number of occurrences of each gene type and returns the
    amended dictionary.
    :param genes: The file containing all chr21 genes
    :param categories: The dictionary containing all gene categories with
    descriptions and count.
    :return: Amended categories dictionary
    """
    list_of_cats = []
    for line in genes:
        line_s = line.split('\t')
        line_cat = line_s[2].rstrip('\n')
        if line_cat != 'Category':
            list_of_cats.append(line_cat)
    for key in categories:
        for ent in list_of_cats:
            if ent == key:
                categories[key]['Count'] += 1
    return categories


def get_args():
    """
    This function parses the arguments given in command line and returns
    filenames or help menu
    :return: the infile to be read and the outfile to be printed to
    """
    parser = argparse.ArgumentParser(description='Combine on gene name and '
                                                 'count the category occurrence')
    # Add arguments
    parser.add_argument('-i1', '--infile1',
                        dest='INFILE1',
                        type=str,
                        help='Path to the gene description file to open',
                        required=True)
    parser.add_argument('-i2', '--infile2',
                        dest='INFILE2',
                        type=str,
                        help='Path to the gene category to open',
                        required=True)
    inf = [parser.parse_args().INFILE1, parser.parse_args().INFILE2]
    return inf


if __name__ == "__main__":
    main()
