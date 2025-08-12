import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if os.path.abspath(directory) not in full_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
    try:
        for path in os.listdir(full_path):
            if os.path.isfile(path):
                return f'{path}: {os.path.getsize(path)}, is_dir={os.path.isdir(path)}'
    except:
        raise Exception(f'Error:{Exception}')

    
