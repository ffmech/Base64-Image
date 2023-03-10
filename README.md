Base64-Image
================

Encodes images to base64 and copies the string to the clipboard.

Installation
------------

1.  Clone the repository: `git clone -b main https://github.com/ffmech/Base64-Image.git`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Run the program: `python main.py --help`

Usage
-----

This program uses a command line interface to give the user various options for image encoding. The user can either encode to base64 or decode by passing the `text` or `image` arguments when running the program.

### Decoding

To  decode the base64 into an image, save it and resize it to 100 pixels run the script with the following flags: `python main.py image --show --shrink 100 --write`
The flag `--show` previews the image with an image viewer whilst the `--write` flag saves the image in the current working directory. The `--shrink` flag lets the user resize the image without changing the aspect ratio.


### Encoding to Base64

To encode simply run the following command : `python main.py text getfrom -c`
This will convert an image saved to the clipboard to base64 and save it in the clipboard. The user has two choices either `getfrom -c` which retrieves the image from the clipboard or `getfrom -f FILENAME` which gets it from a file, in this case the user will have to specify the image path. Furthermore, all the flags used with the image argument can be used here aswell.
