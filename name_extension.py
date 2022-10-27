# Made by: f4gm
# github.com/f4gm

def file_name(path):
    path = path.split("/")
    name = path[len(path) - 1]
    return name

def file_extension(file_name):
    file_name = file_name.split(".")
    extension = "." + file_name[len(file_name) - 1]
    return extension
path = "insert-path"
print(file_name(path))
print(file_extension(file_name(path)))