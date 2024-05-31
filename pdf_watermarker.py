import PyPDF2

# Acquiring files and defining variables for the watermarking function
template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('<watermark>.pdf','rb'))
output = PyPDF2.PdfFileWriter()

# Adding a watermark to all pages in super pdf
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)

