import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        pathstore = []
        for path in os.listdir(full_path):
            
            pathstore.append(f'- {path}: file_size={os.path.getsize(os.path.join(full_path,path))} bytes, is_dir={os.path.isdir(os.path.join(full_path,path))}')
        return '\n'.join(pathstore)
    except Exception as e:
        return f'Error: {e}'
        

    
