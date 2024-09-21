import os
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader
input_dir = os.path.join(os.getcwd(), 'deer_reports_test')
output_dir = os.path.join(os.getcwd(), 'deer_report_pages_test')
for filename in os.listdir(input_dir):
    if not filename.startswith('.'): # ignore hidden files
        county = filename.split('_')[0]
        if not os.path.exists(os.path.join(output_dir, county)):
            os.makedirs(os.path.join(output_dir, county))
        print(county)
        reader = PdfReader(os.path.join(input_dir, filename))
        print(len(reader.pages))
        for i in range(len(reader.pages)):
            output = PdfWriter()
            output.add_page(reader.pages[i])
            with open(os.path.join(output_dir, county, f"{Path(filename).stem}_{i+1}.pdf"), "wb") as output_stream:
                output.write(output_stream)

