from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf_files = [
    "76 Exercise 8 Merge the PDF\pdf files\Research Synopsis (S091).pdf",
    "76 Exercise 8 Merge the PDF\pdf files\Research Synopsis (S096).pdf",
    "76 Exercise 8 Merge the PDF\pdf files\Research Synopsis (S105).pdf",
    "76 Exercise 8 Merge the PDF\pdf files\Research Synopsis (S106).pdf",
    "76 Exercise 8 Merge the PDF\pdf files\Research Synopsis (S110).pdf"
    ]

for pdf in pdf_files:
    merger.append(pdf)

merger.write("82 Exercise 8 - Merge the Pdf Solution\Merge-pdf.pdf")
merger.close()