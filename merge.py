from PyPDF2 import PdfMerger
import re
import os

# Change this for your desired merged pdf name.
# Or simply rename the file after the operation is done!
file_name = "Merged_Documents.pdf"

def main():
    global file_name

    merger = PdfMerger()

    # Check the current directory for PDF files.
    for file in os.listdir():
        if is_pdf(file):
            merger.append(file)
    
    # Saves the file.
    merger.write(file_name)
    merger.close()

# Check if the file is a pdf
def is_pdf(pdf_filename: str) -> bool:
    if re.search(r"(\w+(?:.pdf)+)", pdf_filename):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
