import os
from config import MAX_CHARS
from google.genai import types


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
        
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Extracts file content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to extract data from, limited to 10,000 characters. If not provided, returns an error message.",
            ),
        },
    ),
)
