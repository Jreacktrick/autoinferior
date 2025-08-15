import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory,file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.abspath(full_path)):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        process = subprocess.run(["python", file_path, *args], timeout=30,capture_output=True, cwd=working_directory, text=True)
        outputstring = f'STDOUT: {process.stdout}\nSTDERR: {process.stderr}'
        if not process.stdout and not process.stderr:
            return "No output produced."
        if process.returncode != 0:
            outputstring += f'\nProcess exited with code {process.returncode}'
        return outputstring
    except Exception as e:
        return f"Error: executing Python file: {e}"
