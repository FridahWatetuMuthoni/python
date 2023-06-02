import os

source = "test.txt"
destination = "/Users/pentagonagencieslimited/Desktop/text-files/text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} does not exist")
