import os

list = ['C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-projectimages2/test','C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-project\images2/train','C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-project\images2/valid']
for e in range(len(list)):
    path = list[e]
    for i in range(13):
        directory = f"{path}/{i}"
        os.mkdir(directory)