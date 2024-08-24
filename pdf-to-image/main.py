import argparse
import os
import pymupdf

def extract_pages_to_images(pdf_file, output_folder):
    """
    Extract pages from a PDF file and save them as images.
    Args:
        pdf_file (str): Path to the PDF file.
        output_folder (str): Folder where the images will be saved.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    doc = pymupdf.open(pdf_file)

    # Iterate through the pages
    for i in range(len(doc)):
        # Get the page
        page = doc.load_page(i)

        # Convert page to image
        pix = page.get_pixmap()

        # Save image
        pix.save(os.path.join(output_folder, f'page_{i+1}.png'))

    # Close the document
    doc.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract PDF pages to images')
    parser.add_argument('pdf_file', help='Path to the PDF file')
    parser.add_argument('output_folder', help='Folder where the images will be saved')
    args = parser.parse_args()

    extract_pages_to_images(args.pdf_file, args.output_folder)