# Made by: f4gm
# github.com/f4gm

import os

path = "insert-path"
files = os.listdir(path)
for file in files:
    file = file.replace(".", "_")
    os.mkdir(path + file)
