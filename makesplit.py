import os

list = ['D:/Images/test','D:/Images/train','D:/Images/valid']
for e in range(len(list)):
    path = list[e]
    for i in range(7):
        directory = f"{path}/{i}"
        os.mkdir(directory)