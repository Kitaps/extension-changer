from os import rename, listdir

old_extension = ".txt"
new_extension = ".csv"

local_file_path_names_list = listdir()
for path in local_file_path_names_list:
    new_path = path.replace(old_extension, new_extension)
    rename(path, new_path)
    
    