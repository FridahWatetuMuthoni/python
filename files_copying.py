#copyfile(source, destination) = copies contents of a file
#copy= copyfile(source, destination) + permission mode + destination can be a directory
#copy2()= copy(source, destination) + copies metadata(files creation and modification times)

import shutil

shutil.copyfile("src.txt", "dest.txt")