import PIL
import os
import os.path
from PIL import Image, ImageDraw, ImageFilter
import glob

def crop_center(pil_img, crop_width, crop_height):
    global img_width, img_height
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def folderer(folder):
    path = os.listdir(folder)
    print(path)
    for a in range(len(path)):
        subpath = f'{folder}/{path[a]}'
        print(subpath)
        subpath = os.listdir(subpath)
        print(subpath)
        for b in range(len(subpath)):
            subsubpath = f'{folder}/{path[a]}/{subpath[b]}'
            for file in os.listdir(subsubpath):
                f_img = subsubpath + "/" + file
                print(f_img)
                img = Image.open(f_img)
                img = img.resize((224,224))
                img.save(f_img)

folderer(folder = str(input("Selected Folder: ")))