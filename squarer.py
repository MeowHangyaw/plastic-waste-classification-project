import PIL
import os
import os.path
from PIL import Image

def squarer(folder = str(input("Selected Folder: "))):
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
                f_img = subsubpath+"/"+file
                img = Image.open(f_img)
                img = img.resize((224,224))
                img.save(f_img)

squarer(folder = str(input("Selected Folder: ")))