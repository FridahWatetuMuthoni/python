import os
import shutil

path = "text.txt"

try:
    #removing a file
    os.remove(path)
    #removing an empty directory
    os.rmdir(path)
    #removing a folder with files
    shutil.rmtree(path)
except FileNotFoundError:
    print("The file was not found")
except PermissionError:
    print("You dont have the permission to remove this file")
except OSError:
    print("This directory is not empty")