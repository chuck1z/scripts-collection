import argparse
from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        
        img.save(output_path, 'JPEG', optimize=True, quality=quality)

def compress_images(input_paths, output_folder, quality=85):
    if output_folder != "default":
        os.makedirs(output_folder, exist_ok=True)

    for input_path in input_paths:
        if os.path.isdir(input_path):
            # If input_path is a directory, process all images in it
            for filename in os.listdir(input_path):
                file_path = os.path.join(input_path, filename)
                process_single_file(file_path, output_folder, quality)
        else:
            # If input_path is a file, process it directly
            process_single_file(input_path, output_folder, quality)

def process_single_file(input_path, output_folder, quality):
    if os.path.isfile(input_path) and input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        directory, filename = os.path.split(input_path)
        name, _ = os.path.splitext(filename)
        
        if output_folder == "default":
            output_path = os.path.join(directory, f"compressed_{name}.jpg")
        else:
            output_path = os.path.join(output_folder, f"{name}.jpg")
        
        compress_image(input_path, output_path, quality)
        print(f"Compressed: {input_path} -> {output_path}")
    else:
        print(f"Skipped: {input_path} (not a supported image file)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress images to JPEG format")
    parser.add_argument("input", nargs='+', help="Input image file(s) or folder(s)")
    parser.add_argument("-o", "--output", default="default", help="Output folder for compressed images")
    parser.add_argument("-q", "--quality", type=int, default=50, help="Compression quality (1-95, default: 50)")

    args = parser.parse_args()

    compress_images(args.input, args.output, args.quality)