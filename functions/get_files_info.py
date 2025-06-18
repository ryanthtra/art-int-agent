import os


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