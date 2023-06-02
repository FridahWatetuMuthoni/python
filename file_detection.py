import os 

path = "/Users/pentagonagencieslimited/Desktop/text-files/text.txt"

#checking if the text file exists
if os.path.exists(path):
    print("The location of the file exists")
    #checking if the file in that path location is a file
    if os.path.isfile(path):
        print("This is a file")
    #checking if the file in that path location is a directory
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("The files does not exists")