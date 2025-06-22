import os

MAX_CHARS = 10000

def get_files_info(working_directory, directory=None):
    try:
        wd_contents = os.listdir(working_directory)
    except Exception as e:
        return f"Error: {e}"
        
    dir_path = '/'.join([working_directory, directory])
    
    try:
        is_dir = os.path.isdir(dir_path)
    except Exception as e:
        return f"Error: {e}"
    
    if directory not in wd_contents and directory != ".":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not is_dir:
        return f'Error: "{directory}" is not a directory'
    
    ret_str_arr = []

    try:
        for item in os.listdir(dir_path):
            item_path = '/'.join([dir_path, item])

            ret_str_arr.append(f"- {item}: file_size: {os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}")
    except Exception as e:
        return f"Error: {e}"

    return '\n'.join(ret_str_arr)


def get_file_content(working_directory, file_path):
    try:
        wd_contents = os.listdir(working_directory)
        if file_path.startswith('/'):
            full_path = working_directory + file_path
        else:
            full_path = '/'.join([working_directory, file_path])
        # print(f"full_path: {full_path}")
        is_file = os.path.isfile(full_path)
    except Exception as e:
        return f"Error: {e}"
    
    file_name = list(file_path.split('/'))[-1]
    # print(f"file_name: {file_name}")
    if file_name not in wd_contents:
        if not is_file:        
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
    

def write_file(working_directory, file_path, content):
    try:
        wd_contents = os.listdir(working_directory)
        if file_path.startswith('/'):
            full_path = working_directory + file_path
        else:
            full_path = '/'.join([working_directory, file_path])
        is_file = os.path.isfile(full_path)
    except Exception as e:
        return f"Error: {e}"
    
    file_path_arr = list(file_path.split('/'))
    curr_dir = working_directory
    for i in range(0, len(file_path_arr)):
        try:
            if file_path_arr[i] in os.listdir(curr_dir):
                curr_dir = f"{curr_dir}/{file_path_arr[i]}"
                if os.path.isdir(curr_dir): # is an existing folder           
                    continue
                else: # is a file, so overwrite                         
                    with open(curr_dir, "w") as f:
                        f.write(content)
                        return f'Successfully wrote to "{file_path_arr[i]}" ({len(content)} characters written)'
            else: 
                # See if it's a folder name or a file name
                item_name_arr = file_path_arr[i].split('.')
                if len(item_name_arr) == 1: # is folder, so is an error
                    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
                else:
                    # See is it's an allowed file extension (py, txt, md, etc.)
                    if item_name_arr[-1] == "py" or item_name_arr[-1] == "txt" or item_name_arr[-1] == "md":
                        full_file_path = curr_dir = f"{curr_dir}/{file_path_arr[i]}"
                        with open(full_file_path, "w") as f:
                            f.write(content)
                            return f'Successfully wrote to "{file_path_arr[i]}" ({len(content)} characters written)'
                    else:
                        return f'Error: Cannot write to "{file_path}" as it is not a permitted file extension type.'
        except Exception as e:
            return f"Error trying to create a file: {e}"

    