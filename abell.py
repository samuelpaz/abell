#!/usr/bin/env python3
# author: arkham (https://github.com/samuelpaz/abell)

import sys
import filetype
from PIL import Image

if len(sys.argv) != 4 and len(sys.argv) != 3:
    print("usage:\n")
    print(f"hide message in image:           {sys.argv[0]} --hide [image file] [message]")
    print(f"show hidden message in image:    {sys.argv[0]} --show [image file]")
    sys.exit(0)

kind = filetype.guess(sys.argv[2])

try:
    if kind.mime not in ["image/png", "image/jpeg"]:
        print("Invalid jpg or png file!")
        sys.exit(0)
except:
    print("Invalid jpg or png file!")
    sys.exit(0)

input_image = Image.open(sys.argv[2])
pixel_map = input_image.load()
width, height = input_image.size

if width < 1000 or height < 1000:
    print("The image need be a minimum 1000x1000 size")
    sys.exit(0)

if sys.argv[1] == "--hide":
    m_size = len(sys.argv[3])
    list = [ord(i) for i in sys.argv[3]]
    color_list = [list[x:x+3] for x in range(0, len(list), 3)]
    
    w, h = width, height

    for color in color_list:
        w, h = w//2, h//2
        if len(color) == 3:
            pixel_map[w, h] = (color[0], color[1], color[2])
        elif len(color) == 2:
            pixel_map[w, h] = (color[0], color[1], 0)
        else:
            pixel_map[w, h] = (color[0], 0, 0)

    pixel_map[width-1, height-1] = (13, 37, m_size)
    input_image.save("output.png", format="png")

elif sys.argv[1] == "--show":
    r, g, b = input_image.getpixel((width-1, height-1))

    if r == 13 and g == 37:
        msg_size = b
    else:
        print("No hidden message")
        sys.exit(0)

    w, h = width, height
    final_msg = ""
    for i in range(msg_size//2):
        w, h = w//2, h//2
        r, g, b = input_image.getpixel((w, h))
        final_msg += chr(r) + chr(g) + chr(b)
    print(final_msg)

else:
    print(f"Invalid argument: {sys.argv[1]}")
