# sudo apt install texlive-full
import os
import subprocess
from pathlib import Path

# Specify the folder path
folder_path = "data/"

# List all files and directories in the folder
all_items = os.listdir(folder_path)

# Filter out only files (excluding directories)
files = [item for item in all_items if os.path.isfile(os.path.join(folder_path, item))]

print("Files in the folder:")
for file in files:
    file_docx = os.path.join(folder_path, file)
    file_pdf = os.path.join(folder_path, Path(file).stem + ".pdf")

    command = ["pandoc", file_docx, "-o", file_pdf, "--pdf-engine=xelatex"]
    result = subprocess.run(
        command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
