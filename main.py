import os
import base64
import pyperclip
from io import BytesIO
from PIL import Image, ImageGrab
import argparse

def to_image():

    try:
        image_bytes = base64.b64decode(pyperclip.paste())
    except Exception as err:
        print(f"Couldnt decode image in clipboard: {err}")
        return

    buffered = BytesIO(image_bytes)
    try:
        img = Image.open(buffered)
    except Exception as err:
        print(f"Critical error using given image: {err}")
        return

    print("Base64 converted to image")
    if args.shrink:
        img.thumbnail((args.shrink,args.shrink))

    if args.write:
        save_png(img)

    if args.show:
        img.show()

def to_text():

    buffered = BytesIO()

    try:
        args.clipboard
    except AttributeError:
        print("Required savemode argument")
        return

    if args.clipboard:
        img = ImageGrab.grabclipboard()
    elif os.path.exists(args.filename):
        try:
            img = Image.open(args.filename)
        except Exception as err:
            print(f"Critical error using given image: {err}")
            return
    else:
        print(args.filename)
        print("Image does not exist in given path")
        return

    try:
        img.save(buffered, format="PNG")
    except AttributeError:
        print("No image in clipboard")
        return

    if args.shrink:
        img.thumbnail((args.shrink,args.shrink))

    if args.write:
        save_png(img)

    if args.show:
        img.show()

    img_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    pyperclip.copy(img_data)
    print("Image encoded to Base64 and copied to clipboard")

def save_png(img):
    if not os.path.exists(f"image.png"):
        img.save("image.png")

        print(f"Data written to 'image.png'")
    else:
        i = 1
        while os.path.exists(f"image({i}).png"):
            i += 1
        new_filename = f"image({i}).png"
        img.save(new_filename)
        print(f"Data written to '{new_filename}'")

dispatcher = {"image":to_image,"text":to_text}

parser = argparse.ArgumentParser(
                    prog = 'Png to text',
                    description = 'Converts PNG to base64 and vice-versa')

parser.add_argument("mode", choices=["image","text"])
subparsers = parser.add_subparsers(dest='subparser_name',title='subcommands')
parser_image = subparsers.add_parser('getfrom', help='Source of image, file or clipboard')
group = parser_image.add_mutually_exclusive_group(required=True)
group.add_argument("-c","--clipboard", action='store_true')
group.add_argument("-f","--filename", help="File path to the PNG you want to convert")
parser.add_argument("-sh","--shrink", type=int, help="Shrink image to number")
parser.add_argument("-s", "--show", action="store_true", help="Show the image")
parser.add_argument("-w", "--write", action="store_true", help="Save the file")
args = parser.parse_args()

dispatcher[args.mode]()
