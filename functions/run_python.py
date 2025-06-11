import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_directory = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_filepath.startswith(abs_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_filepath):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python", abs_filepath], capture_output=True, timeout=30, text=True)
        output = f"STDOUT: {result.stdout} STDERR: {result.stderr}"
        if result.returncode != 0:
            output += "\nProcess exited with code X"
            return output
        if result.stderr == "" and result.stdout == "":
            return "No output produced"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Needs a path to the file to run",
            ),
        },
    ),
)
