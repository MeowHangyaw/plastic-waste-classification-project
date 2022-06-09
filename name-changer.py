import os

def namechanger(path):
    dirct = os.listdir(path) #List of the Files
    number = len(dirct) #Length fo the list
    print(dirct)

    for i in range(number): #changing the name of the files in the folder
        print(i)
        new_file_name = f"{path}\{'p'}{str(i)}{'.png'}" #new_file_name = path + "\\" + str(i) + ".png"
        file_name = f'{path}\{dirct[i]}' #file_name = path + "\\" + dirct[i]
        print(file_name)
        os.rename(file_name, new_file_name)

    new_dirct = os.listdir(path)
    print(new_dirct)

path = input("File path: ")
proceeding = bool(input("Do you wish to proceed: (True/False)"))
if proceeding == True:
    namechanger(path)
else:
    os.abort()