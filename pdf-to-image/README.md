# PDF-to-Image

A simple Python script to extract pages from a PDF file and save them as individual image files.

## Requirements
- Python 3
- pymupdf

## Usage
Make sure you have pymupdf installed:
```
pip install PyMuPDF
```
Then, run the script with the following command:
```
python main.py <pdf_file> <output_folder>
```

Replace `<pdf_file>` with the path to the PDF file you want to extract pages from, and `<output_folder>` with the desired folder to save the extracted images.

For example:
```
python main.py input.pdf output_images
```

This will create a folder named `output_images` and save each page of the PDF as a separate image file in that folder.