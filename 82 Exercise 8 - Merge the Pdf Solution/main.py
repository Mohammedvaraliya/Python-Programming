from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf_files = [
    "82 Exercise 8 - Merge the Pdf Solution\pdf files\Research Synopsis (S091).pdf",
    "82 Exercise 8 - Merge the Pdf Solution\pdf files\Research Synopsis (S096).pdf",
    "82 Exercise 8 - Merge the Pdf Solution\pdf files\Research Synopsis (S105).pdf",
    "82 Exercise 8 - Merge the Pdf Solution\pdf files\Research Synopsis (S106).pdf",
    "82 Exercise 8 - Merge the Pdf Solution\pdf files\Research Synopsis (S110).pdf"
    ]

for pdf in pdf_files:
    merger.append(pdf)

merger.write("82 Exercise 8 - Merge the Pdf Solution\Merge-pdf.pdf")
merger.close()