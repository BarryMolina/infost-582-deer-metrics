import os
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader
page_to_get = 1

input_dir = os.path.join(os.getcwd(), 'deer_reports')
output_dir = os.path.join(os.getcwd(), 'deer_reports_page_1')

for filename in os.listdir(input_dir):
    if not filename.startswith('.'): # ignore hidden files
        reader = PdfReader(os.path.join(input_dir, filename))
        print(reader.pages[page_to_get - 1].extract_text())
        # output = PdfWriter()
        # output.add_page(reader.pages[page_to_get - 1])
        # with open(os.path.join(output_dir, f"{Path(filename).stem}_{page_to_get}.pdf"), "wb") as output_stream:
        #     output.write(output_stream)

