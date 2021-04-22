import os
import shutil

destination = "\\"

def identifier(ext):
    '''The function returns the destination folder according to the extension parsed'''
    global destination
    if ext == ".pdf" or ext == ".doc" or ext == ".docx":
        destination = "Documents"
        return destination
    if ext == ".mp3":
        destination = "Music"
        return destination
    if ext == ".jpg" or ext == ".JPG" or ext == ".JPEG" or ext == ".jpeg" or ext == ".png":
        destination = "Pictures"
        return destination
    if ext == ".mkv" or ext == ".mp4":
        destination = "Videos"
        return destination
    if ext == ".exe":
        destination = "Downloads\\exe files"
        return destination
    
    
    
ext_list = [".pdf", ".mp4", ".mp3", ".mkv", ".jpg", ".jpeg", ".exe", ".JPG", ".JPEG", ".docx", ".doc"]

path = "C:\\Users\\himan\\Downloads\\Oh Soldier pritify my folder\\" #path of the folder in which all the files are stored
itemlist = []

for items in os.walk(path):
    itemlist.append(items)


for everything in itemlist:
    for files in everything[2]:
        filepath = path + str(files)
        print(filepath)
        for ext in ext_list:
            if ext in files:
                identifier(ext)
                target_path = "C:\\Users\\himan\\" + destination
                print(target_path)
                shutil.move(filepath,target_path)
                break
