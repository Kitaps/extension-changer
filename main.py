from os import rename, listdir

old_extension = input("Enter the old extension: ")
new_extension = input("Enter the new extension: ")

local_file_path_names_list = listdir()
for path in local_file_path_names_list:
    if(old_extension in path):
        new_path = path.replace(old_extension, new_extension)
        rename(path, new_path)
    
    