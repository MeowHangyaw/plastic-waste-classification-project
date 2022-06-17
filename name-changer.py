import os

def namechanger(path):
    global dirct
    dirct = os.listdir(path) #List of the Files
    number = len(dirct) #Length fo the list
    print(dirct)

    for i in range(number): #changing the name of the files in the folder
        print(i)
        image_number = '{0:04}'.format(i).zfill(4)
        print(image_number)
        new_file_name = f"{path}\{image_number}{'.png'}" #new_file_name = path + "\\" + str(i) + ".png"
        file_name = f'{path}\{dirct[i]}' #file_name = path + "\\" + dirct[i]
        print(file_name)
        os.rename(file_name, new_file_name)

    new_dirct = os.listdir(path)
    print(new_dirct)

def infolder(grandparentfolder):
    dirctgrandparentfolder = os.listdir(grandparentfolder)
    for a in range(len(dirctgrandparentfolder)):
        parentfolder = grandparentfolder + '/' + dirctgrandparentfolder[a]
        dirctparentfolder = os.listdir(parentfolder)
        print(dirctparentfolder)
        for b in range(len(dirctparentfolder)):
            folder = parentfolder + '/' + dirctparentfolder[b]
            print(folder)

grandparentfolder = "C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-project\images3"
infolder(grandparentfolder)