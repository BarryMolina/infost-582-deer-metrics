from PIL import Image
import pytesseract
from pathlib import Path
import os


input_dir = os.path.join(os.getcwd(), 'metric_screenshots')
output_dir = os.path.join(os.getcwd(), 'metric_text')


with open('metric_text.txt', 'w') as outfile:
    for filename in os.listdir(input_dir):
        if not filename.startswith('.'): # ignore hidden files
            text = pytesseract.image_to_string(Image.open(os.path.join(input_dir, filename)))
            outfile.write(text)
            outfile.write('==================================\n\n')