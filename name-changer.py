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
        new_file_name = f"{path}\{image_number}{'.jpg'}" #new_file_name = path + "\\" + str(i) + ".png"
        file_name = f'{path}\{dirct[i]}' #file_name = path + "\\" + dirct[i]
        print(file_name)
        os.rename(file_name, new_file_name)

    new_dirct = os.listdir(path)
    print(new_dirct)

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
                f_img = subsubpath+"/"+file
                namechanger(f_img)
                print(len(dirct))

folderer(f"C:\Users\chula\OneDrive\Documents\Code\projects\github\plastic-waste-classification-project\images3")