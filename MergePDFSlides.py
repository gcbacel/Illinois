# Step 1: Download all slides (and videos, quizzes) using this tutorial: https://www.youtube.com/watch?v=xRk7TPobFvg&t=4s
# Step 2: Move all chapter folders (or the entire course) to the same directory
# step 3: Run the scipt below

from PyPDF2 import PdfFileMerger
import os
import warnings
warnings.filterwarnings("ignore")
source_dir = r'E:\Coursera\cs-498\finalexam'
merger = PdfFileMerger()
count = 0
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('pdf'):
            count += 1
            merger.append(open(os.path.join(root, file), 'rb'))
merger.write(os.path.join(source_dir, 'Allslides.pdf'))       
merger.close()
print(f"{count} pdf files were merged at {os.path.join(source_dir, 'Allslides.pdf')}")