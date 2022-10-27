# Made by: f4gm
# github.com/f4gm

import os
path = "insert-path"
files = os.listdir(path)
list_files = open(path + "list.txt", "w")
for file in files:
    list_files.write(file + "\n")
list_files.close()