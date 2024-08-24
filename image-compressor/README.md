# Image-Compressor

A simple Python script to compress images to JPEG format with adjustable quality.

## Requirements
- Python 3
- Pillow (PIL) library

## Usage
Make sure you have Pillow installed:
```
pip install pillow
```
The script then can be run with the following command:
```
python main.py <input_image(s)/folder(s)> -o <output_folder> -q <quality>
```

### Arguments:
- `input`: The input image file(s) or folder(s) to compress. You can specify multiple files or folders.
- `-o, --output`: The output folder for the compressed images. If not specified, the compressed images will be saved in the same folder as the original images with a "compressed_" prefix.
- `-q, --quality`: The compression quality, ranging from 1 to 95. Lower values result in smaller file sizes with more compression artifacts, while higher values maintain better image quality. The default value is 50.

## Example
To compress all PNG and JPEG images in the current directory and save them in a new folder named "compressed_images" with a quality of 80:
```
python main.py *.png *.jpg -o compressed_images -q 80
```