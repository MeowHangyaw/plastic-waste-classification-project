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

path = input("File path: ")
namechanger(path)
print(len(dirct))