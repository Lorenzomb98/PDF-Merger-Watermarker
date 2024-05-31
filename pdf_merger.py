# Importing necessary modules
import PyPDF2
import sys

# Taking input pdfs
inputs = sys.argv[1:]

# Function that merges pdfs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

# To use, simple write "python pdf_merger.py <pdf1>.pdf <pdf2>.pdf ...", you can write in as many pdfs as you want
pdf_combiner(inputs)

