# Assignment 4

This assignment contains 3 major python files: chr21_gene_names.py, categories.py, and 
intersection.py. chr21_gene_names.py reads through a list of chr21 genes, queries a user for a
gene of interest, and returns the description of the gene of interest. categories.py reads through
a list of chr21 genes and a list of gene categories, then returns the category, number of
occurences, and a description in a .txt file. intersection.py reads through a pair of .txt files
containing genes and returns a set of genes found in both files, as well as genes unique to each
file.

## Description

These programs can be called provided they have the correct arguments given. chr21_gene_names.py
requires a .txt file containing a properly formatted list of genes. categories.py requires two
arguments, a .txt file containing a properly formatted list of genes and a list of categories.
intersection.py requires two properly formatted .txt files containing a list of genes.

chr21_gene_names.py reads through a .txt file and asks for a gene name to search for. If the gene
name can be found, the description is returned. If no gene is found, the program returns "Not a
valid gene name." If the user enters "exit" or "quit", the program is terminated.

categories.py reads through a .txt file of gene names and a .txt file of gene categories. It
returns a .txt file containing the number of occurrences of each category seen in the file.

intersection.py reads through a pair of .txt files containing lists of gene names. It then returns
a .txt output file containing the genes occurring in both files, as well as printing out the number
of unique and shared gene names seen in the files.

## Getting Started

### Dependencies

* Python 3

### Executing program

* Call chr21_gene_names.py with an input argument
* Call categories.py with an input and guiding argument
* Call intersection.py with two input arguments
```
python3 chr21_gene_names.py -i myfile.txt
python3 categories.py -i1 myfile1.txt -i2 myfile2.txt
python3 intersection.py -i1 myfile1.txt -i2 myfile2.txt
```

## Help

If you run into any problems, run the help command
```
python3 chr21_gene_names.py -h
python3 categories.py -h
python3 intersection.py -h
```

## Authors
Fredrick Gootkind

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.
https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md_

