import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{full_path}"'
    
    char_limit_msg = f'[...File "{file_path}" truncated at 10000 characters]'
    try:
        with open(full_path, "r") as file:
            content = file.read(MAX_CHARS)
            next_char = file.read(1)
            if next_char:
                content += char_limit_msg
            return content
    except Exception as e:
        return f'Error: {e}'
        

