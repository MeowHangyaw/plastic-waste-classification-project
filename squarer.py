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

parrentfolder = r'C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-project\images2'
print(parrentfolder)
folderlist = os.listdir(parrentfolder)
print(folderlist)
for x in range(len(folderlist)):
    path = f"{parrentfolder}\{folderlist[x]}"
    e = os.listdir(path)
    for z in range(len(e)):
        newpath = path + '/' + e[z]
        print(newpath)
        lol = os.listdir(newpath)
        for i in range(len(lol)):
            newerpath = f'{newpath}\{lol[i]}'
            print(newerpath)
            img = Image.open(newerpath)
            img = img.resize((224,224))
            img.save(newerpath)

