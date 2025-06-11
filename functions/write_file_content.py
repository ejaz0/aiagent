import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_filepath.startswith(abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.isdir(os.path.dirname(abs_filepath)):
            os.makedirs(os.path.dirname(abs_filepath))
        with open(abs_filepath, 'w') as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Needs a path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            )
        },
    ),
)

